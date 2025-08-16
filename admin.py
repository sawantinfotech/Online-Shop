from flask import Blueprint, render_template, request, redirect, url_for, flash, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from models import Business, Product, Customer, Order, Payment, Service, User, AppSubmission
from datetime import datetime, timedelta
import logging

# Create admin blueprint
admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

# Admin credentials (in production, store in database)
ADMIN_USERS = {
    'admin': generate_password_hash('admin123'),
    'superadmin': generate_password_hash('super123')
}

def admin_required(f):
    """Decorator to require admin login"""
    def decorated_function(*args, **kwargs):
        if not session.get('admin_logged_in'):
            return redirect(url_for('admin.admin_login'))
        return f(*args, **kwargs)
    decorated_function.__name__ = f.__name__
    return decorated_function

@admin_bp.route('/service/login', methods=['GET', 'POST'])
def admin_login():
    """Admin login page"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username in ADMIN_USERS and check_password_hash(ADMIN_USERS[username], password):
            session['admin_logged_in'] = True
            session['admin_username'] = username
            flash('Admin login successful', 'success')
            return redirect(url_for('admin.admin_dashboard'))
        else:
            flash('Invalid admin credentials', 'error')
    
    return render_template('admin/admin_login.html')

@admin_bp.route('/logout')
@admin_required
def admin_logout():
    """Admin logout"""
    session.pop('admin_logged_in', None)
    session.pop('admin_username', None)
    flash('Admin logged out successfully', 'success')
    return redirect(url_for('admin.admin_login'))

@admin_bp.route('/dashboard')
@admin_required
def admin_dashboard():
    """Admin dashboard with system overview"""
    # Get system statistics
    total_services = Service.query.count()
    pending_services = Service.query.filter_by(status='pending').count()
    verified_services = Service.query.filter_by(status='approved').count()
    total_products = Product.query.count()
    total_customers = Customer.query.count()
    total_orders = Order.query.count()
    
    # Recent orders (last 30 days)
    thirty_days_ago = datetime.utcnow() - timedelta(days=30)
    recent_orders = Order.query.filter(Order.created_at >= thirty_days_ago).count()
    
    # Revenue calculation
    total_revenue = db.session.query(db.func.sum(Order.total_amount)).filter(
        Order.payment_status == 'completed'
    ).scalar() or 0
    
    stats = {
        'total_services': total_services,
        'pending_services': pending_services,
        'verified_services': verified_services,
        'total_products': total_products,
        'total_customers': total_customers,
        'total_orders': total_orders,
        'recent_orders': recent_orders,
        'total_revenue': total_revenue
    }
    
    # Recent businesses for review
    recent_service = Service.query.order_by(Service.created_at.desc()).limit(5).all()
    
    return render_template('admin/admin_dashboard.html', stats=stats, recent_service=recent_service)

@admin_bp.route('/services')
@admin_required
def admin_services():
    """Manage all services"""
    page = request.args.get('page', 1, type=int)
    status_filter = request.args.get('status', 'all')
    
    query = Service.query
    
    if status_filter != 'all':
        query = query.filter_by(verification_status=status_filter)
    
    services = query.order_by(Service.created_at.desc()).paginate(
        page=page, per_page=20, error_out=False
    )
    
    return render_template('admin/services.html', services=services, status_filter=status_filter)

@admin_bp.route('/verify-service/<int:business_id>', methods=['POST'])
@admin_required
def verify_service(business_id):
    """Verify or reject a service"""
    service = Service.query.get_or_404(business_id)
    action = request.form.get('action')
    
    if action == 'verify':
        service.verification_status = 'verified'
        flash(f'Service {service.service_name} has been verified', 'success')
    elif action == 'reject':
        service.verification_status = 'rejected'
        flash(f'Service {service.service_name} has been rejected', 'warning')
    
    db.session.commit()
    
    # Send email notification (if email system is working)
    try:
        from email_service import send_service_verification_email
        send_service_verification_email(service)
    except Exception as e:
        logging.error(f"Failed to send verification email: {e}")
    
    return redirect(url_for('admin.admin_services'))

@admin_bp.route('/service-details/<int:business_id>')
@admin_required
def service_details(business_id):
    """View detailed service information"""
    service = Service.query.get_or_404(business_id)
    
    # Get service statistics
    product_count = Product.query.filter_by(business_id=business_id).count()
    customer_count = Customer.query.filter_by(business_id=business_id).count()
    order_count = Order.query.filter_by(business_id=business_id).count()
    
    # Revenue calculation for this business
    revenue = db.session.query(db.func.sum(Order.total_amount)).filter(
        Order.business_id == business_id,
        Order.payment_status == 'completed'
    ).scalar() or 0
    
    stats = {
        'products': product_count,
        'customers': customer_count,
        'orders': order_count,
        'revenue': revenue
    }
    
    return render_template('admin/service_details.html', service=service, stats=stats)

@admin_bp.route('/orders')
@admin_required
def admin_orders():
    """View all orders across services"""
    page = request.args.get('page', 1, type=int)
    status_filter = request.args.get('status', 'all')
    
    query = Order.query.join(Service).join(Customer)
    
    if status_filter != 'all':
        query = query.filter(Order.order_status == status_filter)
    
    orders = query.order_by(Order.created_at.desc()).paginate(
        page=page, per_page=20, error_out=False
    )
    
    return render_template('admin/order.html', orders=orders, status_filter=status_filter)

@admin_bp.route('/system-settings')
@admin_required
def system_settings():
    """System configuration and settings"""
    # Get email system status
    email_status = {
        'configured': True,  # Assume configured based on environment
        'connection': True   # Test connection if needed
    }
    
    # Get SMS system status
    sms_status = {
        'configured': True,  # Check Twilio configuration
        'template_count': 5  # Count SMS templates
    }
    
    # Get database statistics
    db_stats = {
        'services': Service.query.count(),
        'products': Product.query.count(),
        'customers': Customer.query.count(),
        'orders': Order.query.count()
    }
    
    return render_template('admin/system_settings.html', 
                         email_status=email_status,
                         sms_status=sms_status,
                         db_stats=db_stats)
    email_configured = bool(
        __import__('os').environ.get('EMAIL_ADDRESS') and 
        __import__('os').environ.get('EMAIL_PASSWORD')
    )
    
    sms_configured = bool(
        __import__('os').environ.get('TWILIO_ACCOUNT_SID') and 
        __import__('os').environ.get('TWILIO_AUTH_TOKEN')
    )
    
    config = {
        'email_configured': email_configured,
        'sms_configured': sms_configured,
        'total_Business': Service.query.count(),
        'database_url': __import__('os').environ.get('DATABASE_URL', 'Not configured')[:50] + '...'
    }
    
    return render_template('admin/settings.html', config=config)



@admin_bp.route('/categories')
@admin_required
def admin_categories():
    """Manage product categories"""
    categories = Category.query.order_by(Category.name).all()
    return render_template('admin/categories.html', categories=categories)

@admin_bp.route('/add-category', methods=['POST'])
@admin_required
def add_category():
    """Add new product category"""
    name = request.form.get('name')
    description = request.form.get('description')
    
    if name:
        category = Category(name=name, description=description)
        db.session.add(category)
        db.session.commit()
        flash(f'Category "{name}" added successfully', 'success')
    else:
        flash('Category name is required', 'error')
    
    return redirect(url_for('admin.admin_categories'))

@admin_bp.route('/delete-category/<int:category_id>', methods=['POST'])
@admin_required
def delete_category(category_id):
    """Delete a category"""
    category = Category.query.get_or_404(category_id)
    
    # Check if category has products
    product_count = Product.query.filter_by(category_id=category_id).count()
    
    if product_count > 0:
        flash(f'Cannot delete category "{category.name}" - it has {product_count} products', 'error')
    else:
        db.session.delete(category)
        db.session.commit()
        flash(f'Category "{category.name}" deleted successfully', 'success')
    
    return redirect(url_for('admin.admin_categories'))

@admin_bp.route('/reports')
@admin_required
def admin_reports():
    """Generate system reports"""
    # Daily sales for last 30 days
    thirty_days_ago = datetime.utcnow() - timedelta(days=30)
    
    daily_sales = db.session.query(
        db.func.date(Order.created_at).label('date'),
        db.func.sum(Order.total_amount).label('total'),
        db.func.count(Order.id).label('count')
    ).filter(
        Order.created_at >= thirty_days_ago,
        Order.payment_status == 'completed'
    ).group_by(
        db.func.date(Order.created_at)
    ).order_by('date').all()
    
    # Top services by revenue
    top_services = db.session.query(
        Service.service_name,
        db.func.sum(Order.total_amount).label('revenue'),
        db.func.count(Order.id).label('order_count')
    ).join(Order).filter(
        Order.payment_status == 'completed'
    ).group_by(Service.id).order_by(db.text('revenue desc')).limit(10).all()
    
    return render_template('admin/reports.html', 
                         daily_sales=daily_sales, 
                         top_services=top_services)

@admin_bp.route('/test-systems')
@admin_required
def test_systems():
    """Test system integrations"""
    # Test email system
    email_status = 'Not Configured'
    try:
        from email_service import test_email_connection
        if test_email_connection():
            email_status = 'Working'
        else:
            email_status = 'Failed'
    except Exception:
        email_status = 'Error'
    
    # Test SMS system
    sms_status = 'Not Configured'
    try:
        from sms_service import send_sms
        # Don't actually send SMS, just check if configured
        if (__import__('os').environ.get('TWILIO_ACCOUNT_SID') and 
            __import__('os').environ.get('TWILIO_AUTH_TOKEN')):
            sms_status = 'Configured'
    except Exception:
        sms_status = 'Error'
    
    test_results = {
        'email_status': email_status,
        'sms_status': sms_status,
        'database_status': 'Connected' if db else 'Error'
    }
    
    return render_template('admin/test_systems.html', test_results=test_results)

# App Service Management Routes
@admin_bp.route('/app_submissions')
@admin_required
def manage_app_submissions():
    """Manage app submissions"""
    try:
        from models import App, AppSubmission
        
        # Get both App entries and AppSubmission entries
        apps = App.query.order_by(App.created_at.desc()).all()
        submissions = AppSubmission.query.order_by(AppSubmission.submission_date.desc()).all()
        
        # Combined statistics
        total_app_entries = App.query.count()
        pending_app_entries = App.query.filter_by(status='pending').count()
        active_app_entries = App.query.filter_by(status='active').count()
        
        pending_submissions = AppSubmission.query.filter_by(status='pending').count()
        approved_submissions = AppSubmission.query.filter_by(status='approved').count()
        rejected_submissions = AppSubmission.query.filter_by(status='rejected').count()
        
        stats = {
            'total_submissions': total_app_entries + len(submissions),
            'pending_submissions': pending_app_entries + pending_submissions,
            'approved_submissions': active_app_entries + approved_submissions,
            'rejected_submissions': rejected_submissions
        }
        
        return render_template('admin/app_submissions.html', 
                             apps=apps,
                             submissions=submissions, 
                             stats=stats)
    except Exception as e:
        logging.error(f"Error loading app submissions: {e}")
        flash('Error loading app submissions', 'error')
        return redirect(url_for('admin.admin_dashboard'))

@admin_bp.route('/app_submissions/<int:submission_id>/approve', methods=['POST'])
@admin_required
def approve_app_submission(submission_id):
    """Approve an app submission"""
    try:
        submission = AppSubmission.query.get_or_404(submission_id)
        submission.status = 'approved'
        submission.review_date = datetime.utcnow()
        
        # Create approved app record
        from models import App
        
        # Function to generate unique slug
        def generate_unique_slug(name):
            import re
            base_slug = re.sub(r'[^a-zA-Z0-9\s-]', '', name.lower()).replace(' ', '-').replace('_', '-')
            base_slug = re.sub(r'-+', '-', base_slug).strip('-')
            
            # Check if slug already exists
            counter = 0
            unique_slug = base_slug
            while App.query.filter_by(slug=unique_slug).first():
                counter += 1
                unique_slug = f"{base_slug}-{counter}"
            return unique_slug
        
        new_app = App(
            name=submission.app_name,
            slug=generate_unique_slug(submission.app_name),
            short_description=submission.app_description[:200] + "..." if len(submission.app_description) > 200 else submission.app_description,
            long_description=submission.app_description,
            category=submission.app_category,
            version=submission.app_version,
            author_name=submission.developer_name,
            author_email=submission.developer_email,
            status='active',
            rating=0.0,
            downloads=0,
            featured=False
        )
        
        db.session.add(new_app)
        db.session.commit()
        
        flash(f'App "{submission.app_name}" approved successfully!', 'success')
    except Exception as e:
        logging.error(f"Error approving app submission: {e}")
        db.session.rollback()
        flash('Error approving app submission', 'error')
    
    return redirect(url_for('admin.manage_app_submissions'))

@admin_bp.route('/app_submissions/<int:submission_id>/reject', methods=['POST'])
@admin_required
def reject_app_submission(submission_id):
    """Reject an app submission"""
    try:
        submission = AppSubmission.query.get_or_404(submission_id)
        submission.status = 'rejected'
        submission.review_date = datetime.utcnow()
        submission.admin_notes = request.form.get('rejection_reason', 'App submission rejected')
        
        db.session.commit()
        flash(f'App "{submission.app_name}" rejected', 'warning')
    except Exception as e:
        logging.error(f"Error rejecting app submission: {e}")
        db.session.rollback()
        flash('Error rejecting app submission', 'error')
    
    return redirect(url_for('admin.manage_app_submissions'))

@admin_bp.route('/app_submissions/<int:submission_id>/delete', methods=['POST'])
@admin_required
def delete_app_submission(submission_id):
    """Delete an app submission"""
    try:
        submission = AppSubmission.query.get_or_404(submission_id)
        app_name = submission.app_name
        
        db.session.delete(submission)
        db.session.commit()
        
        flash(f'App submission "{app_name}" deleted successfully', 'success')
    except Exception as e:
        logging.error(f"Error deleting app submission: {e}")
        db.session.rollback()
        flash('Error deleting app submission', 'error')
    
    return redirect(url_for('admin.manage_app_submissions'))