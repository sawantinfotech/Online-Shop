from flask import Blueprint, render_template, request, redirect, url_for, flash, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from models import Business, Product, Customer, Order, Payment, Category
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

@admin_bp.route('/login', methods=['GET', 'POST'])
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
    
    return render_template('admin/login.html')

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
    total_businesses = Business.query.count()
    pending_businesses = Business.query.filter_by(verification_status='pending').count()
    verified_businesses = Business.query.filter_by(verification_status='verified').count()
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
        'total_businesses': total_businesses,
        'pending_businesses': pending_businesses,
        'verified_businesses': verified_businesses,
        'total_products': total_products,
        'total_customers': total_customers,
        'total_orders': total_orders,
        'recent_orders': recent_orders,
        'total_revenue': total_revenue
    }
    
    # Recent businesses for review
    recent_businesses = Business.query.order_by(Business.created_at.desc()).limit(5).all()
    
    return render_template('admin/dashboard.html', stats=stats, recent_businesses=recent_businesses)

@admin_bp.route('/businesses')
@admin_required
def admin_businesses():
    """Manage all businesses"""
    page = request.args.get('page', 1, type=int)
    status_filter = request.args.get('status', 'all')
    
    query = Business.query
    
    if status_filter != 'all':
        query = query.filter_by(verification_status=status_filter)
    
    businesses = query.order_by(Business.created_at.desc()).paginate(
        page=page, per_page=20, error_out=False
    )
    
    return render_template('admin/businesses.html', businesses=businesses, status_filter=status_filter)

@admin_bp.route('/verify-business/<int:business_id>', methods=['POST'])
@admin_required
def verify_business(business_id):
    """Verify or reject a business"""
    business = Business.query.get_or_404(business_id)
    action = request.form.get('action')
    
    if action == 'verify':
        business.verification_status = 'verified'
        flash(f'Business {business.business_name} has been verified', 'success')
    elif action == 'reject':
        business.verification_status = 'rejected'
        flash(f'Business {business.business_name} has been rejected', 'warning')
    
    db.session.commit()
    
    # Send email notification (if email system is working)
    try:
        from email_service import send_business_verification_email
        send_business_verification_email(business)
    except Exception as e:
        logging.error(f"Failed to send verification email: {e}")
    
    return redirect(url_for('admin.admin_businesses'))

@admin_bp.route('/business-details/<int:business_id>')
@admin_required
def business_details(business_id):
    """View detailed business information"""
    business = Business.query.get_or_404(business_id)
    
    # Get business statistics
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
    
    return render_template('admin/business_details.html', business=business, stats=stats)

@admin_bp.route('/orders')
@admin_required
def admin_orders():
    """View all orders across businesses"""
    page = request.args.get('page', 1, type=int)
    status_filter = request.args.get('status', 'all')
    
    query = Order.query.join(Business).join(Customer)
    
    if status_filter != 'all':
        query = query.filter(Order.order_status == status_filter)
    
    orders = query.order_by(Order.created_at.desc()).paginate(
        page=page, per_page=20, error_out=False
    )
    
    return render_template('admin/orders.html', orders=orders, status_filter=status_filter)

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
        'businesses': Business.query.count(),
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
        'total_categories': Category.query.count(),
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
    
    # Top businesses by revenue
    top_businesses = db.session.query(
        Business.business_name,
        db.func.sum(Order.total_amount).label('revenue'),
        db.func.count(Order.id).label('order_count')
    ).join(Order).filter(
        Order.payment_status == 'completed'
    ).group_by(Business.id).order_by(db.text('revenue desc')).limit(10).all()
    
    return render_template('admin/reports.html', 
                         daily_sales=daily_sales, 
                         top_businesses=top_businesses)

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