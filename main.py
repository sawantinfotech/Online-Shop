from app import app, db
# Import routes for full functionality
# import routes  # noqa: F401 - temporarily disabled due to syntax errors
# import csv_routes  # noqa: F401 - temporarily commented

# Import and register Product service blueprint
from product.product_routes import product_bp
app.register_blueprint(product_bp)

# Add essential routes directly
from flask import render_template, request, redirect, url_for, session, flash, send_from_directory
import os

# Configure file upload settings
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
app.config['UPLOAD_FOLDER'] = 'uploads'

# Route to serve uploaded files
@app.route('/uploads/<path:filename>')
def uploaded_file(filename):
    """Serve uploaded files"""
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/')
def index():
    # Get active subscribers for display
    try:
        from models import User, App
        from product.product_models import ProductItem
        active_subscribers = User.query.filter_by(user_type='subscriber').limit(10).all()
        # Get featured apps and newly submitted apps for home page carousel
        featured_apps = App.query.filter(App.status.in_(['active', 'pending'])).order_by(App.created_at.desc()).limit(8).all()
        # Get featured products for home page display
        featured_products = ProductItem.query.filter_by(status='active', featured=True).order_by(ProductItem.created_at.desc()).limit(8).all()
    except Exception as e:
        active_subscribers = []
        featured_apps = []
        featured_products = []
    
    # Temporarily disable complex queries to focus on user registration
    categories = []
    featured_services = []
    featured_businesses = []
    services = []
    delivery_profiles = []
    matrimony_profiles = []
    
    # Add datetime import for template
    from datetime import datetime
    
    return render_template('public_home.html',
                         categories=categories,
                         featured_services=featured_services,
                         featured_products=featured_products,
                         featured_businesses=featured_businesses,
                         services=services,
                         delivery_profiles=delivery_profiles,
                         featured_apps=featured_apps,
                         matrimony_profiles=matrimony_profiles,
                         active_subscribers=active_subscribers,
                         now=datetime.now)

@app.route('/user/register', methods=['GET', 'POST'])
def user_register():
    from models import User
    from werkzeug.security import generate_password_hash
    
    if request.method == 'POST':
        email = request.form.get('email')
        mobile = request.form.get('mobile')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        password = request.form.get('password')
        
        # Generate username from email
        username = email.split('@')[0] if email else ''
        
        # Check if user already exists  
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('User with this email or username already exists!', 'error')
            return render_template('user_register.html')
        
        # Create new subscriber user
        full_name = f"{first_name} {last_name}" if first_name and last_name else ""
        new_user = User()
        new_user.username = username
        new_user.email = email
        new_user.mobile = mobile
        new_user.full_name = full_name
        new_user.user_type = 'subscriber'
        new_user.verification_status = 'verified'
        new_user.set_password(password)
        
        try:
            db.session.add(new_user)
            db.session.commit()
            # Auto-login the user after successful registration
            session['user_id'] = new_user.id
            session['username'] = new_user.username
            session['user_type'] = new_user.user_type
            flash('Registration successful! Welcome to your dashboard.', 'success')
            return redirect(url_for('user_subscriber_dashboard'))
        except Exception as e:
            import logging
            logging.error(f"Registration error: {e}")
            db.session.rollback()
            flash(f'Registration failed: {str(e)}', 'error')
            return render_template('user_register.html')
    
    return render_template('user_register.html')

@app.route('/user/login', methods=['GET', 'POST'])  
def user_login():
    from models import User
    
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email, user_type='subscriber').first()
        if user and user.check_password(password):
            session['user_id'] = user.id
            session['username'] = user.username
            session['user_type'] = user.user_type
            flash('Login successful!', 'success')
            return redirect(url_for('user_subscriber_dashboard'))
        else:
            flash('Invalid email or password.', 'error')
    
    return render_template('user_login.html')

@app.route('/user/logout')
def user_logout():
    session.clear()
    flash('Logged out successfully', 'info')
    return redirect(url_for('index'))

def login_required(f):
    from functools import wraps
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in to access this page.', 'error')
            return redirect(url_for('user_login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/user/subscriber_dashboard')
@login_required
def user_subscriber_dashboard():
    from models import User, Service, App
    from product.product_models import ProductItem
    user = User.query.get(session['user_id'])
    
    # If user doesn't exist, create a default user
    if not user:
        user = User()
        user.email = f"user{session['user_id']}@demo.com"
        user.full_name = f"User {session['user_id']}"
        user.user_type = 'subscriber'
        db.session.add(user)
        db.session.commit()
    
    # Get user's service requests
    service_requests = Service.query.filter_by(requested_by=user.id).order_by(Service.created_at.desc()).all()
    
    # Get user's app submissions
    app_submissions = App.query.filter_by(submitted_by=user.id).order_by(App.created_at.desc()).all()
    
    # Get user's product submissions
    product_submissions = ProductItem.query.filter_by(added_by=user.id).order_by(ProductItem.created_at.desc()).all()
    
    # Statistics for dashboard
    total_requests = len(service_requests)
    pending_requests = len([s for s in service_requests if s.status == 'pending'])
    approved_requests = len([s for s in service_requests if s.status == 'approved'])
    rejected_requests = len([s for s in service_requests if s.status == 'rejected'])
    
    # App submission statistics - pass actual lists to template
    total_apps = len(app_submissions)
    pending_apps_list = [a for a in app_submissions if a.status == 'pending']
    active_apps_list = [a for a in app_submissions if a.status == 'active']
    approved_apps_list = [a for a in app_submissions if a.status == 'approved']
    rejected_apps_list = [a for a in app_submissions if a.status == 'rejected']
    
    # Product submission statistics - pass actual lists to template
    total_products = len(product_submissions)
    pending_products_list = [p for p in product_submissions if p.status == 'pending']
    active_products_list = [p for p in product_submissions if p.status == 'active']
    approved_products_list = [p for p in product_submissions if p.status == 'approved']
    rejected_products_list = [p for p in product_submissions if p.status == 'rejected']
    
    return render_template('user/subscriber_dashboard.html', 
                         user=user,
                         service_requests=service_requests,
                         app_submissions=app_submissions,
                         product_submissions=product_submissions,
                         submitted_apps=app_submissions,  # For template compatibility
                         total_requests=total_requests,
                         pending_requests=pending_requests,
                         approved_requests=approved_requests,
                         rejected_requests=rejected_requests,
                         total_apps=total_apps,
                         pending_apps=pending_apps_list,
                         active_apps=active_apps_list,
                         approved_apps=approved_apps_list,
                         rejected_apps=rejected_apps_list,
                         total_products=total_products,
                         pending_products=pending_products_list,
                         active_products=active_products_list,
                         approved_products=approved_products_list,
                         rejected_products=rejected_products_list)

@app.route('/user/services')
@login_required
def subscriber_services():
    from models import User, Service
    user = User.query.get(session['user_id'])
    
    # Get all user's service requests with detailed view
    service_requests = Service.query.filter_by(requested_by=user.id).order_by(Service.created_at.desc()).all()
    
    return render_template('user/subscriber_services.html', 
                         user=user, 
                         service_requests=service_requests)

@app.route('/user/profile', methods=['GET', 'POST'])
@login_required  
def subscriber_profile():
    from models import User

    
    user = User.query.get(session['user_id'])
    
    if request.method == 'POST':
        # Update user profile
        if user:
            user.full_name = request.form.get('full_name', user.full_name or '')
            user.mobile = request.form.get('mobile', user.mobile or '')
            user.address = request.form.get('address', user.address or '')
        
        try:
            db.session.commit()
            flash('Profile updated successfully!', 'success')
        except Exception as e:
            flash('Profile update failed. Please try again.', 'error')
        
        return redirect(url_for('subscriber_profile'))
    
    return render_template('user/subscriber_profile.html', user=user)


# Account route
@app.route('/user/all_user')
def all_user_route():
    from models import User
    users = User.query.all()
    current_filters = {'plan': '', 'status': '', 'search': ''}
    return render_template('user/all_user.html', users=users, current_filters=current_filters)
# Specific service routes for better structure - public access
@app.route('/hospital/hospital_home')
def hospital_home():
    return render_template('Hospital/hospital_home.html')

# Removed duplicate medical_home route

@app.route('/bank/bank_home')
def bank_home():
    return render_template('bank/bank_home.html')


# Removed duplicate currancy_home route

@app.route('/education/education_home')
def education_home():
    return render_template('education/education_home.html')

# Removed duplicate career_home route

@app.route('/job/job_home')
def job_home():
    return render_template('job/job_home.html')

@app.route('/legal/legal_home')
def legal_home():
    return render_template('legal/legal_home.html')

@app.route('/chartered_accountant/ca_home')
def ca_home():
    return render_template('chartered_accountant/ca_home.html')

@app.route('/government/govt_home')
def govt_home():
    return render_template('government/govt_home.html')

@app.route('/police/police_home')
def police_home():
    return render_template('police/police_home.html')

@app.route('/politics/politics_home')
def politics_home():
    return render_template('politics/politics_home.html')

@app.route('/chat/chat_home')
def chat_home():
    return render_template('chat/chat_home.html')

@app.route('/social/social_home')
def social_home():
    return render_template('social/social_home.html')

@app.route('/email/email_home')
def email_home():
    return render_template('email/email_home.html')

@app.route('/sms/sms_home')
def sms_home():
    return render_template('sms/sms_home.html')

@app.route('/news/news_home')
def news_home():
    return render_template('news/news_home.html')

@app.route('/blog/blog_home')
def blog_home():
    return render_template('blog/blog_home.html')

@app.route('/post/post_home')
def post_home():
    return render_template('post/post_home.html')

@app.route('/story/story_home')
def story_home():
    return render_template('story/story_home.html')

@app.route('/reel/reel_home')
def reel_home():
    return render_template('reel/reel_home.html')

# Additional routes for missing services
@app.route('/career/career_home')
def career_home():
    return render_template('career/career_home.html')

# Removed duplicate finance_home route



@app.route('/currancy/currancy_home')
def currancy_home():
    return render_template('currancy/currancy_home.html')

@app.route('/stock_exchange/stockexchange_home')
def stockexchange_home():
    return render_template('stock_exchange/stockexchange_home.html')

@app.route('/share_market/sharemarket_home')
def sharemarket_home():
    return render_template('share_market/sharemarket_home.html')


@app.route('/investor/investor_home')
def investor_home():
    return render_template('investor/investor_home.html')

@app.route('/finance/finance_home')
def finance_home():
    return render_template('finance/finance_home.html')

@app.route('/medical/medical_home')
def medical_home():
    return render_template('medical/medical_home.html')

# Removed duplicate delivery_home route - already defined as delivery_home_service

@app.route('/live/live_home')
def live_home():
    return render_template('live/live_home.html')

@app.route('/property/property_home')
def property_home():
    return render_template('property/property_home.html')

@app.route('/agriculture/agriculture_home')
def agriculture_home():
    return render_template('agriculture/agriculture_home.html')

@app.route('/sport/sport_home')
def sport_home():
    return render_template('sport/sport_home.html')

@app.route('/event/event_home')
def event_home():
    return render_template('event/event_home.html')

@app.route('/artificial_intelligence/ai_home')
def ai_home():
    return render_template('artificial_intelligence/ai_home.html')

@app.route('/brainlo/brainlo_home')
def brainlo_home():
    return render_template('brainlo/brainlo_home.html')

@app.route('/marketing/marketing_home')
def marketing_home():
    return render_template('marketing/marketing_home.html')

@app.route('/advertise/advertise_home')
def advertise_home():
    return render_template('advertise/advertise_home.html')

@app.route('/order/order_home')
def orders_home():
    return render_template('order/order_home.html')

# Alias route for admin template compatibility
@app.route('/admin/order_home')
def order_home():
    return render_template('order/order_home.html')

# Removed duplicate advertise_home route

@app.route('/public_market/publicmarket_home')
def publicmarket_home():
    return render_template('public_market/publicmarket_home.html')

@app.route('/creditpoint/creditpoint_home')
def creditpoints_home():
    return render_template('creditpoint/creditpoint_home.html')

@app.route('/customer/customer_home')
def customer_home():
    return render_template('customer/customer_home.html')

@app.route('/office/office_home')
def office_home():
    return render_template('office/office_home.html')

@app.route('/language/language_home')
def language_home():
    return render_template('language/language_home.html')

# Removed duplicate family_home route - already defined above

@app.route('/app/app_home')
def app_home():
    """App marketplace home page with featured apps and categories"""
    from models import App, User
    
    # Get featured apps and statistics (Point 2 & 3)
    featured_apps = App.query.filter_by(featured=True, status='active').limit(6).all()
    # Get recently added apps (highlight new - Point 3) - include both active and pending
    new_apps = App.query.filter(App.status.in_(['active', 'pending'])).order_by(App.created_at.desc()).limit(6).all()
    # Get pending apps for admin review (Point 3)
    pending_apps = App.query.filter_by(status='pending').order_by(App.created_at.desc()).limit(3).all()
    
    total_apps = App.query.filter(App.status.in_(['active', 'pending'])).count()
    total_downloads = db.session.query(db.func.sum(App.downloads)).scalar() or 0
    total_developers = App.query.with_entities(App.author_email).distinct().count()
    
    # Get popular categories - include both active and pending apps
    categories = db.session.query(
        App.category, 
        db.func.count(App.id).label('count')
    ).filter(App.status.in_(['active', 'pending'])).group_by(App.category).all()
    
    # Add datetime import for template
    from datetime import datetime
    
    return render_template('app/app_home.html',
                          featured_apps=featured_apps,
                          new_apps=new_apps,
                          pending_apps=pending_apps,
                          total_apps=total_apps,
                          total_downloads=total_downloads,
                          total_developers=total_developers,
                          categories=categories,
                          now=datetime.now)

@app.route('/delivery/delivery_home')
def delivery_home():
    return render_template('delivery/delivery_home.html')

@app.route('/matrimony/matrimony_home')
def matrimony_home():
    return render_template('matrimony/matrimony_home.html')

# Product home route removed - handled by product blueprint at /product/

@app.route('/offer/offer_home')
def offer_home():
    return render_template('offer/offer_home.html')

@app.route('/help_support/help_support_home')
def help_support_home():
    return render_template('help_support/help_support_home.html')

@app.route('/contact/contact_home')
def contact_home():
    return render_template('contact/contact_home.html')

@app.route('/family/family_home')
def family_home():
    return render_template('family/family_home.html')

# App Interaction Routes (Point 4, 5, 6 - favorites, follows, shares)

@app.route('/api/app/favorite/<int:app_id>', methods=['POST'])
@login_required
def toggle_app_favorite(app_id):
    """Toggle app favorite status for current user"""
    from models import AppFavorite, App
    import json
    
    user_id = session.get('user_id')
    app = App.query.get_or_404(app_id)
    
    # Check if already favorited
    existing_favorite = AppFavorite.query.filter_by(user_id=user_id, app_id=app_id).first()
    
    if existing_favorite:
        # Remove from favorites
        db.session.delete(existing_favorite)
        is_favorite = False
        message = "Removed from favorites"
    else:
        # Add to favorites
        favorite = AppFavorite()
        favorite.user_id = user_id
        favorite.app_id = app_id
        db.session.add(favorite)
        is_favorite = True
        message = "Added to favorites"
    
    db.session.commit()
    
    return json.dumps({
        'success': True,
        'is_favorite': is_favorite,
        'message': message
    })

@app.route('/api/developer/follow', methods=['POST'])
@login_required
def toggle_developer_follow():
    """Toggle developer follow status for current user"""
    from models import DeveloperFollow
    import json
    
    user_id = session.get('user_id')
    developer_email = request.form.get('developer_email')
    
    if not developer_email:
        return json.dumps({'success': False, 'message': 'Developer email required'})
    
    # Check if already following
    existing_follow = DeveloperFollow.query.filter_by(user_id=user_id, developer_email=developer_email).first()
    
    if existing_follow:
        # Unfollow
        db.session.delete(existing_follow)
        is_following = False
        message = "Unfollowed developer"
    else:
        # Follow
        follow = DeveloperFollow()
        follow.user_id = user_id
        follow.developer_email = developer_email
        db.session.add(follow)
        is_following = True
        message = "Now following developer"
    
    db.session.commit()
    
    return json.dumps({
        'success': True,
        'is_following': is_following,
        'message': message
    })

@app.route('/api/app/share/<int:app_id>', methods=['POST'])
@login_required
def record_app_share(app_id):
    """Record app share action"""
    from models import AppShare, App
    import json
    
    user_id = session.get('user_id')
    platform = request.form.get('platform', 'unknown')
    app = App.query.get_or_404(app_id)
    
    # Record the share
    share = AppShare()
    share.user_id = user_id
    share.app_id = app_id
    share.platform = platform
    
    db.session.add(share)
    db.session.commit()
    
    return json.dumps({
        'success': True,
        'message': f'App shared on {platform}'
    })

@app.route('/api/app/download/<int:app_id>', methods=['POST'])
@login_required
def record_app_download(app_id):
    """Record app download action"""
    from models import App
    import json
    
    user_id = session.get('user_id')
    app = App.query.get_or_404(app_id)
    
    # Increment download count
    app.downloads += 1
    db.session.commit()
    
    return json.dumps({
        'success': True,
        'message': 'Download recorded',
        'downloads': app.downloads
    })

# Comprehensive App Service Routes

@app.route('/app/app_registration', methods=['GET', 'POST'])
@login_required
def app_registration():
    """App submission/registration page for developers"""
    from models import AppSubmission, User
    from werkzeug.utils import secure_filename
    import os
    import logging
    
    # BUSINESS SERVICE DISCONNECTED - Use demo user instead
    user_id = session.get('user_id', 1)  # Default to demo user
    
    if request.method == 'POST':
        try:
            # Create new app submission
            submission = AppSubmission()
            
            # Basic app information
            submission.user_id = user_id  # Use user_id instead of business_id
            submission.app_name = request.form.get('app_name')
            submission.app_description = request.form.get('app_description')
            submission.app_category = request.form.get('app_category')
            submission.app_version = request.form.get('app_version', '1.0.0')
            submission.app_website = request.form.get('app_website')
            submission.app_download_url = request.form.get('app_download_url')
            
            # Developer information
            submission.developer_name = request.form.get('developer_name')
            submission.developer_email = request.form.get('developer_email')
            submission.developer_phone = request.form.get('developer_phone')
            submission.developer_company = request.form.get('developer_company')
            submission.developer_website = request.form.get('developer_website')
            
            # App details
            submission.target_audience = request.form.get('target_audience')
            submission.app_size = request.form.get('app_size')
            submission.minimum_os_version = request.form.get('minimum_os_version')
            submission.app_price = request.form.get('app_price', 'Free')
            submission.monetization_model = request.form.get('monetization_model', 'Free')
            
            # Plan selection
            submission.plan_type = request.form.get('plan_type', 'basic')
            
            # Features (convert to JSON)
            features = request.form.get('app_features', '').split('\n')
            features = [f.strip() for f in features if f.strip()]
            submission.set_features_list(features)
            
            # Permissions (convert to JSON)
            permissions = request.form.get('permissions_required', '').split('\n')
            permissions = [p.strip() for p in permissions if p.strip()]
            submission.set_permissions_list(permissions)
            
            # Handle file uploads
            upload_folder = 'uploads/apps'
            os.makedirs(upload_folder, exist_ok=True)
            
            # App logo upload
            if 'app_logo' in request.files:
                logo_file = request.files['app_logo']
                if logo_file and logo_file.filename:
                    filename = secure_filename(logo_file.filename)
                    logo_path = f"{upload_folder}/logo_{submission.app_name.replace(' ', '_')}_{filename}"
                    logo_file.save(logo_path)
                    submission.app_logo = logo_path
            
            db.session.add(submission)
            db.session.commit()
            
            # Automatically create approved app for demo (Point 2 - show in featured apps)
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
            
            new_app = App()
            new_app.name = submission.app_name
            new_app.slug = generate_unique_slug(submission.app_name)
            new_app.logo_url = f"/{submission.app_logo}" if submission.app_logo else None
            new_app.short_description = submission.app_description[:200] + "..." if len(submission.app_description) > 200 else submission.app_description
            new_app.long_description = submission.app_description
            new_app.category = submission.app_category
            new_app.version = submission.app_version
            new_app.downloads = 0
            new_app.rating = 0.0
            new_app.reviews_count = 0
            new_app.features = submission.app_features
            new_app.author_name = submission.developer_name
            new_app.author_email = submission.developer_email
            new_app.author_website = submission.developer_website
            new_app.support_email = submission.developer_email
            new_app.status = 'pending'  # Point 3 - pending status for admin approval
            new_app.featured = False    # Will be set to True after admin approval
            new_app.submitted_by = session.get('user_id')  # Track who submitted the app
            
            db.session.add(new_app)
            db.session.commit()
            
            logging.info(f"App submission and app created: {submission.app_name}")
            flash('App submitted successfully! It will be reviewed by our team and appear in the marketplace after approval.', 'success')
            return redirect(url_for('user_subscriber_dashboard'))
            
        except Exception as e:
            db.session.rollback()
            logging.error(f"App submission error: {str(e)}")
            flash(f'Error submitting app: {str(e)}', 'error')
    
    # Get categories for dropdown
    categories = [
        'Productivity', 'Games', 'Social', 'Education', 'Business', 
        'Entertainment', 'Health', 'Finance', 'Shopping', 'Travel',
        'Photography', 'Music', 'News', 'Sports', 'Weather'
    ]
    
    return render_template('app/app_registration_multistep.html', categories=categories)

@app.route('/app/all_apps')
def all_apps():
    """App marketplace - browse all apps with filtering and search (Point 2)"""
    from models import App, AppFavorite, DeveloperFollow
    
    # Get query parameters
    search = request.args.get('search', '')
    category = request.args.get('category', '')
    view_type = request.args.get('view', 'grid')
    sort_by = request.args.get('sort', 'downloads')
    page = int(request.args.get('page', 1))
    per_page = 12
    
    # Build query - show both active and pending apps
    query = App.query.filter(App.status.in_(['active', 'pending']))
    
    # Apply search filter
    if search:
        query = query.filter(
            db.or_(
                App.name.ilike(f'%{search}%'),
                App.short_description.ilike(f'%{search}%'),
                App.long_description.ilike(f'%{search}%')
            )
        )
    
    # Apply category filter
    if category:
        query = query.filter_by(category=category)
    
    # Apply sorting
    if sort_by == 'downloads':
        query = query.order_by(App.downloads.desc())
    elif sort_by == 'rating':
        query = query.order_by(App.rating.desc())
    elif sort_by == 'newest':
        query = query.order_by(App.created_at.desc())
    elif sort_by == 'name':
        query = query.order_by(App.name.asc())
    
    # Paginate results
    apps_pagination = query.paginate(
        page=page, per_page=per_page, error_out=False
    )
    apps = apps_pagination.items
    
    # Get all categories for filter dropdown - include both active and pending
    categories = db.session.query(
        App.category, 
        db.func.count(App.id).label('count')
    ).filter(App.status.in_(['active', 'pending'])).group_by(App.category).all()
    
    # Add datetime import for template
    from datetime import datetime
    
    return render_template('app/all_apps.html',
                          apps=apps,
                          categories=categories,
                          search=search,
                          selected_category=category,
                          view_type=view_type,
                          sort_by=sort_by,
                          pagination=apps_pagination,
                          now=datetime.now)

@app.route('/app/app_detail')
@app.route('/app/app_detail/<int:app_id>')
@app.route('/app/app_detail/<slug>')
def app_detail(app_id=None, slug=None):
    """App detail page with full information, screenshots, and reviews"""
    from models import App, User
    
    if slug:
        # Find app by slug
        app = App.query.filter_by(slug=slug).first_or_404()
    elif app_id is None:
        # Show demo app if no ID provided
        app_id = 1
        app = App.query.get_or_404(app_id)
    else:
        app = App.query.get_or_404(app_id)
    
    # Increment view count (downloads as proxy)
    app.downloads += 1
    db.session.commit()
    
    # Get related apps (same category)
    related_apps = App.query.filter(
        App.category == app.category,
        App.id != app.id,
        App.status == 'active'
    ).limit(4).all()
    
    # Get app reviews (mock for now)
    reviews = []
    
    return render_template('app/app_detail.html',
                          app=app,
                          related_apps=related_apps,
                          reviews=reviews)

# Additional App category routes
@app.route('/app/gaming_apps')
def gaming_apps():
    """Gaming apps category page"""
    from models import App
    apps = App.query.filter_by(category='Games', status='active').all()
    return render_template('app/category_apps.html', apps=apps, category='Gaming Apps')

@app.route('/app/productivity_apps')
def productivity_apps():
    """Productivity apps category page"""
    from models import App
    apps = App.query.filter_by(category='Productivity', status='active').all()
    return render_template('app/category_apps.html', apps=apps, category='Productivity Apps')

@app.route('/app/social_apps')
def social_apps():
    """Social apps category page"""
    from models import App
    apps = App.query.filter_by(category='Social', status='active').all()
    return render_template('app/category_apps.html', apps=apps, category='Social Apps')

@app.route('/app/business_apps')
def business_apps():
    """Business apps category page"""
    from models import App
    apps = App.query.filter_by(category='Business', status='active').all()
    return render_template('app/category_apps.html', apps=apps, category='Business Apps')

@app.route('/app/education_apps')
def education_apps():
    """Education apps category page"""
    from models import App
    apps = App.query.filter_by(category='Education', status='active').all()
    return render_template('app/category_apps.html', apps=apps, category='Education Apps')

# Initialize demo app data
def create_demo_apps():
    """Create demo apps for testing"""
    from models import App
    
    if App.query.count() > 0:
        return  # Demo apps already exist
    
    demo_apps = [
        {
            'name': 'TaskMaster Pro',
            'slug': 'taskmaster-pro',
            'short_description': 'Professional task management and productivity suite',
            'long_description': 'TaskMaster Pro is a comprehensive productivity solution designed for professionals and teams. Features include advanced task scheduling, team collaboration, time tracking, and detailed analytics.',
            'category': 'Productivity',
            'version': '2.1.0',
            'downloads': 15420,
            'rating': 4.8,
            'reviews_count': 312,
            'features': '["Task Management", "Team Collaboration", "Time Tracking", "Analytics Dashboard", "Calendar Integration", "Mobile Sync"]',
            'author_name': 'ProductiveTech Solutions',
            'author_email': 'developer@productivetech.com',
            'featured': True,
            'status': 'active'
        },
        {
            'name': 'RetroGaming Hub',
            'slug': 'retro-gaming-hub',
            'short_description': 'Classic retro games collection with modern features',
            'long_description': 'Experience nostalgia with RetroGaming Hub - featuring over 50 classic arcade games, updated with modern graphics, achievements system, and multiplayer capabilities.',
            'category': 'Games',
            'version': '1.5.2',
            'downloads': 8925,
            'rating': 4.6,
            'reviews_count': 145,
            'features': '["50+ Classic Games", "HD Graphics", "Achievements", "Multiplayer Mode", "Leaderboards", "Cloud Save"]',
            'author_name': 'RetroGames Studio',
            'author_email': 'team@retrogames.com',
            'featured': True,
            'status': 'active'
        },
        {
            'name': 'SocialConnect Plus',
            'slug': 'social-connect-plus',
            'short_description': 'Advanced social networking and community platform',
            'long_description': 'SocialConnect Plus offers a modern approach to social networking with privacy-first design, community building tools, and advanced messaging features.',
            'category': 'Social',
            'version': '3.0.1',
            'downloads': 12680,
            'rating': 4.4,
            'reviews_count': 198,
            'features': '["Private Communities", "Encrypted Messaging", "Event Planning", "Photo Sharing", "Live Streaming", "Group Video Calls"]',
            'author_name': 'Social Innovations Inc',
            'author_email': 'hello@socialinnovations.com',
            'featured': True,
            'status': 'active'
        },
        {
            'name': 'BizManager Suite',
            'slug': 'biz-manager-suite',
            'short_description': 'Complete business management solution for SMEs',
            'long_description': 'BizManager Suite provides everything small and medium enterprises need: CRM, inventory management, accounting, and employee management in one integrated platform.',
            'category': 'Business',
            'version': '4.2.0',
            'downloads': 5432,
            'rating': 4.9,
            'reviews_count': 89,
            'features': '["CRM System", "Inventory Management", "Accounting", "Employee Management", "Report Generation", "API Integration"]',
            'author_name': 'Enterprise Solutions Ltd',
            'author_email': 'support@enterprisesolutions.com',
            'featured': False,
            'status': 'active'
        },
        {
            'name': 'LearnSmart Academy',
            'slug': 'learn-smart-academy',
            'short_description': 'Interactive learning platform with AI-powered tutorials',
            'long_description': 'LearnSmart Academy revolutionizes education with AI-powered personalized learning paths, interactive tutorials, and comprehensive progress tracking for students of all ages.',
            'category': 'Education',
            'version': '1.8.3',
            'downloads': 9876,
            'rating': 4.7,
            'reviews_count': 156,
            'features': '["AI-Powered Learning", "Interactive Tutorials", "Progress Tracking", "Multi-subject Support", "Offline Content", "Parent Dashboard"]',
            'author_name': 'EdTech Innovations',
            'author_email': 'team@edtechinnovations.com',
            'featured': True,
            'status': 'active'
        },
        {
            'name': 'HealthTracker Pro',
            'slug': 'health-tracker-pro',
            'short_description': 'Comprehensive health and fitness monitoring app',
            'long_description': 'Monitor your health with HealthTracker Pro - featuring workout tracking, nutrition planning, sleep analysis, and integration with popular fitness devices.',
            'category': 'Health',
            'version': '2.3.1',
            'downloads': 7234,
            'rating': 4.5,
            'reviews_count': 123,
            'features': '["Workout Tracking", "Nutrition Planning", "Sleep Analysis", "Device Integration", "Progress Reports", "Goal Setting"]',
            'author_name': 'FitTech Solutions',
            'author_email': 'info@fittechsolutions.com',
            'featured': False,
            'status': 'active'
        }
    ]
    
    try:
        for app_data in demo_apps:
            app = App()
            for key, value in app_data.items():
                setattr(app, key, value)
            db.session.add(app)
        
        db.session.commit()
        print("Demo apps created successfully!")
    except Exception as e:
        db.session.rollback()
        print(f"Error creating demo apps: {e}")

# Call this function during app initialization
with app.app_context():
    create_demo_apps()

@app.route('/partner/partner_home')
@login_required
def partner_home():
    return render_template('partner/partner_home.html')

# Additional routes for service home pages
@app.route('/csv/csv_home')
@login_required
def csv_home():
    return render_template('csv/csv_home.html')

@app.route('/console/console_home')
def console_home():
    return render_template('console/console_home.html')

# Console Development Tools Routes
@app.route('/console/api_management')
def console_api_management():
    return render_template('console/api_management.html')

@app.route('/console/application_hosting')
def console_application_hosting():
    return render_template('console/application_hosting.html')

@app.route('/console/analytics')
def console_analytics():
    return render_template('console/analytics.html')

@app.route('/console/database_manager')
def console_database_manager():
    return render_template('console/database_manager.html')

@app.route('/console/code_editor')
def console_code_editor():
    """Template File Editor - Three screen view with code editing and frontend preview"""
    return render_template('console/code_editor.html')

@app.route('/console/file_manager')
def console_file_manager():
    """File Manager for browsing and managing template files"""
    return render_template('console/file_manager.html')

@app.route('/console/terminal')
def console_terminal():
    return render_template('console/terminal.html')

@app.route('/console/logs')
def console_logs():
    return render_template('console/logs.html')

@app.route('/console/deployments')
def console_deployments():
    return render_template('console/deployments.html')

@app.route('/console/monitoring')
def console_monitoring():
    return render_template('console/monitoring.html')

@app.route('/console/backup')
def console_backup():
    return render_template('console/backup.html')

@app.route('/console/user_management')
def console_user_management():
    return render_template('console/user_management.html')

@app.route('/console/permissions')
def console_permissions():
    return render_template('console/permissions.html')

@app.route('/console/api_keys')
def console_api_keys():
    return render_template('console/api_keys.html')

# Template View Routes for Template Editor
@app.route('/template/view/<path:template_path>')
def template_viewer(template_path):
    """Template viewer/editor for live preview and editing"""
    try:
        # Basic template viewing - can be expanded to full editor functionality
        return render_template(template_path)
    except:
        return f"Template {template_path} not found or error loading", 404

@app.route('/widgets/widgets_home')
def widgets_home():
    return render_template('widgets/widgets_home.html')

@app.route('/plan/plan_home')
@login_required
def plans_home():
    return render_template('plan/plan_home.html')

@app.route('/notification/notification_home')
@login_required
def notification_home():
    return render_template('notification/notification_home.html')

@app.route('/service/service_home')
def service_home_page():
    """Service directory - view all available services"""
    from models import Service, User
    
    # Get all active services
    services = Service.query.all()
    
    # Get featured services (you can add a featured flag to Service model later)
    featured_services = services[:6] if services else []
    
    return render_template('service/service_home.html', 
                         services=services, 
                         featured_services=featured_services)

@app.route('/service/service_registration', methods=['GET', 'POST'])
@login_required
def service_registration():
    """Service registration - users can request new services"""
    from models import Service, User
    
    if request.method == 'POST':
        service_name = request.form.get('service_name')
        service_description = request.form.get('service_description')
        service_category = request.form.get('service_category')
        service_type = request.form.get('service_type', 'request')  # request or direct_add
        
        user = User.query.get(session['user_id'])
        
        if service_name and service_description:
            # Create new service (pending approval if user is not admin)
            new_service = Service()
            new_service.name = service_name
            new_service.description = service_description
            new_service.category = service_category
            new_service.status = 'approved' if user.role == 'admin' else 'pending'
            new_service.requested_by = user.id
            new_service.service_type = service_type
            
            try:
                db.session.add(new_service)
                db.session.commit()
                
                if user.role == 'admin':
                    flash('Service added successfully!', 'success')
                    return redirect(url_for('service_home_page'))
                else:
                    flash('Service request submitted! Admin will review and approve.', 'info')
                    return redirect(url_for('user_subscriber_dashboard'))
            except Exception as e:
                db.session.rollback()
                flash('Error submitting service request. Please try again.', 'error')
    
    return render_template('service/service_registration.html')

@app.route('/service/all_service')
@login_required
def all_service():
    """Admin view - manage all services"""
    from models import Service, User
    
    user = User.query.get(session['user_id'])
    
    # Check if user is admin
    if user.role != 'admin':
        flash('Access denied. Admin privileges required.', 'error')
        return redirect(url_for('service_home_page'))
    
    # Get all services with filters
    status_filter = request.args.get('status', 'all')
    category_filter = request.args.get('category', 'all')
    
    query = Service.query
    
    if status_filter != 'all':
        query = query.filter_by(status=status_filter)
    
    if category_filter != 'all':
        query = query.filter_by(category=category_filter)
    
    services = query.order_by(Service.created_at.desc()).all()
    
    # Get unique categories for filter dropdown
    categories = db.session.query(Service.category).distinct().all()
    categories = [cat[0] for cat in categories if cat[0]]
    
    return render_template('service/all_service.html', 
                         services=services, 
                         categories=categories,
                         current_filters={'status': status_filter, 'category': category_filter})

@app.route('/service/approve_service/<int:service_id>')
@login_required
def approve_service(service_id):
    """Approve a pending service"""
    from models import Service, User
    
    user = User.query.get(session['user_id'])
    if user.role != 'admin':
        flash('Access denied. Admin privileges required.', 'error')
        return redirect(url_for('service_home_page'))
    
    service = Service.query.get_or_404(service_id)
    service.status = 'approved'
    
    try:
        db.session.commit()
        flash(f'Service "{service.name}" approved successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash('Error approving service.', 'error')
    
    return redirect(url_for('all_service'))

@app.route('/service/reject_service/<int:service_id>')
@login_required
def reject_service(service_id):
    """Reject a pending service"""
    from models import Service, User
    
    user = User.query.get(session['user_id'])
    if user.role != 'admin':
        flash('Access denied. Admin privileges required.', 'error')
        return redirect(url_for('service_home_page'))
    
    service = Service.query.get_or_404(service_id)
    service.status = 'rejected'
    
    try:
        db.session.commit()
        flash(f'Service "{service.name}" rejected.', 'info')
    except Exception as e:
        db.session.rollback()
        flash('Error rejecting service.', 'error')
    
    return redirect(url_for('all_service'))

@app.route('/service/use_service/<int:service_id>')
@login_required
def use_service(service_id):
    """Use a service with free trial or premium plan"""
    from models import Service, User, ServiceUsage
    
    service = Service.query.get_or_404(service_id)
    user = User.query.get(session['user_id'])
    
    # Check if service is available
    if service.status != 'approved':
        flash('Service is not available at the moment.', 'error')
        return redirect(url_for('service_home_page'))
    
    # Create service usage record
    usage = ServiceUsage()
    usage.user_id = user.id
    usage.service_id = service.id
    usage.plan_type = 'free_trial'  # Default to free trial
    usage.status = 'active'
    
    try:
        db.session.add(usage)
        db.session.commit()
        flash(f'Started using {service.name} with free trial!', 'success')
    except Exception as e:
        db.session.rollback()
        flash('Error starting service usage.', 'error')
    
    return redirect(url_for('service_detail', service_id=service_id))

@app.route('/service/detail/<int:service_id>')
def service_detail(service_id):
    """Service detail page"""
    from models import Service, ServiceUsage
    
    service = Service.query.get_or_404(service_id)
    
    user_usage = None
    if 'user_id' in session:
        user_usage = ServiceUsage.query.filter_by(
            user_id=session['user_id'], 
            service_id=service_id
        ).first()
    
    return render_template('service/service_detail.html', 
                         service=service, 
                         user_usage=user_usage)

# Admin Routes - Integrated from admin.py
@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    """Admin login page"""
    from werkzeug.security import generate_password_hash, check_password_hash
    
    # Admin credentials (in production, store in database)
    ADMIN_USERS = {
        'admin': generate_password_hash('admin123'),
        'superadmin': generate_password_hash('super123')
    }
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username in ADMIN_USERS and check_password_hash(ADMIN_USERS[username], password):
            session['admin_logged_in'] = True
            session['admin_username'] = username
            session['user_type'] = 'admin'
            flash('Admin login successful', 'success')
            return redirect(url_for('admin_home'))
        else:
            flash('Invalid admin credentials', 'error')
    
    return render_template('admin/admin_login.html')

@app.route('/admin/home')
def admin_home():
    """Admin dashboard home page"""
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    
    # Get system statistics
    try:
        from models import Service, User
        total_services = Service.query.count()
        pending_services = Service.query.filter_by(status='pending').count()
        approved_services = Service.query.filter_by(status='approved').count()
        total_users = User.query.count()
        # total_businesses = Business.query.count()  # BUSINESS SERVICE DISCONNECTED
        total_businesses = 0  # Business service disconnected
        # total_products = Product.query.count()  # BUSINESS SERVICE DISCONNECTED  
        total_products = 0  # Business product service disconnected
        
        stats = {
            'total_services': total_services,
            'pending_services': pending_services,
            'approved_services': approved_services,
            'total_users': total_users,
            'total_businesses': total_businesses,
            'total_products': total_products
        }
        
        # Recent services for review
        recent_services = Service.query.order_by(Service.created_at.desc()).limit(5).all()
        
    except Exception as e:
        stats = {
            'total_services': 0,
            'pending_services': 0,
            'approved_services': 0,
            'total_users': 0,
            'total_businesses': 0,
            'total_products': 0
        }
        recent_services = []
    
    return render_template('admin/admin_home.html', 
                         stats=stats, 
                         recent_services=recent_services,
                         admin_username=session.get('admin_username'))

@app.route('/admin/logout')
def admin_logout():
    """Admin logout"""
    session.pop('admin_logged_in', None)
    session.pop('admin_username', None)
    session.pop('user_type', None)
    flash('Admin logged out successfully', 'success')
    return redirect(url_for('admin_login'))

@app.route('/admin/profile')
def admin_profile():
    """Admin profile page"""
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    
    return render_template('admin/admin_profile.html', 
                         admin_username=session.get('admin_username'))

@app.route('/admin/dashboard')
def admin_dashboard():
    """Admin dashboard with detailed analytics"""
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    
    return redirect(url_for('admin_home'))

# Additional missing service routes - public access (resolved conflicts)

# post_home route already exists above

# Removed duplicate delivery route - already exists as delivery_home_service above

# Business routes DISCONNECTED - Service isolated
# @app.route('/business/business_home')
# def business_home():
#     return render_template('business/business_home.html')

# @app.route('/business/business_register')
# def business_register_route():
#     return render_template('business/business_register.html')

# Removed duplicate matrimony_home route - already defined above

# Additional missing routes


# Matrimony registration route
@app.route('/matrimony/matrimony_register_step', methods=['GET', 'POST'])
@app.route('/matrimony/matrimony_register_step/<int:step>', methods=['GET', 'POST'])
def matrimony_register_step(step=1):
    """Multi-step matrimony registration page"""
    
    if request.method == 'POST':
        action = request.form.get('action', 'next')
        
        if action == 'previous' and step > 1:
            return redirect(url_for('matrimony_register_step', step=step-1))
        elif action == 'next' and step < 6:
            # Store form data in session for multi-step
            if not session.get('matrimony_form_data'):
                session['matrimony_form_data'] = {}
            
            # Store current step data
            for key, value in request.form.items():
                if key != 'action':
                    session['matrimony_form_data'][key] = value
            
            return redirect(url_for('matrimony_register_step', step=step+1))
        elif action == 'submit' and step == 6:
            flash('Profile registration completed successfully!', 'success')
            return redirect(url_for('index'))
    
    # Pre-populate form with session data
    form_data = session.get('matrimony_form_data', {})
    
    return render_template('matrimony/matrimony_register_step.html', form=None, step=step, form_data=form_data)

# Additional Admin Routes
@app.route('/admin/users')
def all_users():
    """Admin page to manage all users"""
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    
    try:
        from models import User, ServiceUsage, Service
        # Get all users with their service usage statistics
        users = User.query.all()
        user_stats = []
        
        for user in users:
            # Get user's service usage count
            usage_count = ServiceUsage.query.filter_by(user_id=user.id).count()
            active_services = ServiceUsage.query.filter_by(user_id=user.id, status='active').count()
            
            user_stats.append({
                'user': user,
                'total_services': usage_count,
                'active_services': active_services,
                'status': 'Active' if user.is_active else 'Inactive'
            })
            
    except Exception as e:
        user_stats = []
        flash(f'Error loading users: {str(e)}', 'error')
    
    return render_template('admin/all_users.html', user_stats=user_stats)

@app.route('/admin/customers')
def admin_customers():
    """Admin page to manage customers"""
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    
    try:
        from models import Customer, Order
        customers = Customer.query.all()
        customer_stats = []
        
        for customer in customers:
            order_count = Order.query.filter_by(customer_id=customer.id).count()
            customer_stats.append({
                'customer': customer,
                'total_orders': order_count,
                'status': 'Active'
            })
            
    except Exception as e:
        customer_stats = []
        flash(f'Error loading customers: {str(e)}', 'error')
    
    return render_template('admin/admin_customers.html', customer_stats=customer_stats)

@app.route('/admin/plans')
def admin_plans():
    """Admin page to manage subscription plans"""
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    
    plans = [
        {
            'name': 'Basic',
            'price': '₹0/month',
            'features': ['5 Services', 'Basic Support', 'Community Access'],
            'subscribers': 150,
            'status': 'Active'
        },
        {
            'name': 'Silver',
            'price': '₹299/month',
            'features': ['20 Services', 'Priority Support', 'Analytics Dashboard'],
            'subscribers': 89,
            'status': 'Active'
        },
        {
            'name': 'Gold',
            'price': '₹599/month',
            'features': ['50 Services', '24/7 Support', 'Advanced Analytics', 'API Access'],
            'subscribers': 45,
            'status': 'Active'
        },
        {
            'name': 'Platinum',
            'price': '₹999/month',
            'features': ['Unlimited Services', 'Dedicated Manager', 'Custom Integration'],
            'subscribers': 12,
            'status': 'Active'
        }
    ]
    
    return render_template('admin/admin_plans.html', plans=plans)

@app.route('/admin/accounts')
def admin_accounts():
    """Admin page to manage user accounts"""
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    
    return render_template('admin/admin_accounts.html')

@app.route('/admin/offers')
def admin_offers():
    """Admin page to manage offers and promotions"""
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    
    offers = [
        {
            'title': 'New User Bonus',
            'description': '50% off first month subscription',
            'discount': '50%',
            'valid_until': '2025-12-31',
            'status': 'Active',
            'used_count': 45
        },
        {
            'title': 'Annual Plan Discount',
            'description': '2 months free on annual subscription',
            'discount': '17%',
            'valid_until': '2025-12-31',
            'status': 'Active',
            'used_count': 23
        }
    ]
    
    return render_template('admin/admin_offers.html', offers=offers)

@app.route('/admin/sms')
def admin_sms():
    """Admin page to manage SMS services"""
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    
    return render_template('admin/admin_sms.html')

@app.route('/admin/email')
def admin_email():
    """Admin page to manage email services"""
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    
    return render_template('admin/admin_email.html')

@app.route('/admin/notifications')
def admin_notifications():
    """Admin page to manage notifications"""
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    
    return render_template('admin/admin_notifications.html')

@app.route('/admin/office')
def admin_office():
    """Admin page to manage office settings"""
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    
    return render_template('admin/admin_office.html')

@app.route('/admin/contact')
def admin_contact():
    """Admin page to manage contact information"""
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    
    return render_template('admin/admin_contact.html')

# Additional admin service management routes for fixing redirect issues
@app.route('/admin/manage_services')
def admin_manage_services():
    """Admin service management"""
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    
    try:
        services = Service.query.order_by(Service.created_at.desc()).all()
        pending_count = Service.query.filter_by(status='pending').count()
        approved_count = Service.query.filter_by(status='approved').count()
        
        return render_template('admin/admin_services.html', 
                             services=services,
                             pending_count=pending_count,
                             approved_count=approved_count)
    except Exception as e:
        logging.error(f"Error loading services: {e}")
        flash('Error loading services', 'error')
        return redirect(url_for('admin_home'))

@app.route('/admin/all_services')
def admin_all_services():
    """View all services"""
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    
    return redirect(url_for('admin_manage_services'))

@app.route('/admin/add_service')
def admin_add_service():
    """Add new service"""
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    
    return render_template('admin/add_service.html')

@app.route('/admin/view_all_services') 
def admin_view_all_services():
    """View all services"""
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    
    return redirect(url_for('admin_manage_services'))

@app.route('/admin/review_pending')
def admin_review_pending():
    """Review pending submissions"""
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    
    try:
        # Get pending services
        pending_services = Service.query.filter_by(status='pending').all()
        
        # Get pending app submissions (Point 6 - admin approval for apps)
        from models import AppSubmission, App
        pending_apps = AppSubmission.query.filter_by(status='pending').all()
        pending_app_entries = App.query.filter_by(status='pending').all()
        
        return render_template('admin/admin_pending_review.html', 
                             pending_services=pending_services,
                             pending_apps=pending_apps,
                             pending_app_entries=pending_app_entries)
                             
    except Exception as e:
        logging.error(f"Error in admin review: {e}")
        flash('Error loading pending reviews', 'error')
        return redirect(url_for('admin_home'))

# Admin App Approval Routes (Point 6)
@app.route('/admin/approve_app/<int:app_id>', methods=['POST'])
def admin_approve_app(app_id):
    """Admin route to approve a pending app"""
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    
    try:
        from models import App
        app = App.query.get_or_404(app_id)
        
        if app.status == 'pending':
            app.status = 'active'
            app.featured = True  # Make approved apps featured (Point 2)
            db.session.commit()
            
            flash(f'App "{app.name}" has been approved and is now featured!', 'success')
            logging.info(f"App approved: {app.name}")
        
        return redirect(url_for('admin_review_pending'))
        
    except Exception as e:
        logging.error(f"Error approving app: {e}")
        flash('Error approving app', 'error')
        return redirect(url_for('admin_review_pending'))

@app.route('/admin/reject_app/<int:app_id>', methods=['POST'])
def admin_reject_app(app_id):
    """Admin route to reject a pending app"""
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    
    try:
        from models import App
        app = App.query.get_or_404(app_id)
        
        if app.status == 'pending':
            app.status = 'rejected'
            db.session.commit()
            
            flash(f'App "{app.name}" has been rejected.', 'warning')
            logging.info(f"App rejected: {app.name}")
        
        return redirect(url_for('admin_review_pending'))
        
    except Exception as e:
        logging.error(f"Error rejecting app: {e}")
        flash('Error rejecting app', 'error')
        return redirect(url_for('admin_review_pending'))
        
        # Get pending app submissions
        from models import AppSubmission
        pending_apps = AppSubmission.query.filter_by(status='pending').all()
        
        return render_template('admin/review_pending.html',
                             pending_services=pending_services,
                             pending_apps=pending_apps)
    except Exception as e:
        logging.error(f"Error loading pending items: {e}")
        flash('Error loading pending items', 'error')
        return redirect(url_for('admin_home'))

@app.route('/admin/manage_users')
def admin_manage_users():
    """Manage users"""
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    
    return redirect(url_for('all_users'))

# Fix app submissions route
@app.route('/admin/app_submissions')
def admin_app_submissions():
    """Admin app submissions management"""
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    
    try:
        from models import AppSubmission
        submissions = AppSubmission.query.order_by(AppSubmission.submission_date.desc()).all()
        pending_count = AppSubmission.query.filter_by(status='pending').count()
        approved_count = AppSubmission.query.filter_by(status='approved').count()
        rejected_count = AppSubmission.query.filter_by(status='rejected').count()
        
        stats = {
            'total_submissions': len(submissions),
            'pending_submissions': pending_count,
            'approved_submissions': approved_count,
            'rejected_submissions': rejected_count
        }
        
        return render_template('admin/app_submissions.html', 
                             submissions=submissions, 
                             stats=stats)
    except Exception as e:
        logging.error(f"Error loading app submissions: {e}")
        flash('Error loading app submissions', 'error')
        return redirect(url_for('admin_home'))

# Missing admin routes for template compatibility
@app.route('/admin/payment')
def admin_payment():
    """Admin payment management"""
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    
    return render_template('admin/admin_payment.html')

@app.route('/admin/seo')
def admin_seo():
    """Admin SEO and sitemap management"""
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    
    return render_template('admin/admin_seo.html')

# API endpoints for app interactions
@app.route('/api/app/download/<int:app_id>', methods=['POST'])
def api_app_download(app_id):
    """API endpoint to handle app downloads"""
    from models import App
    import json
    
    app_data = App.query.get_or_404(app_id)
    # Increment download count
    app_data.downloads = (app_data.downloads or 0) + 1
    db.session.commit()
    
    return json.dumps({
        'success': True,
        'message': 'Download count updated',
        'downloads': app_data.downloads
    })

@app.route('/api/app/favorite', methods=['POST'])
def api_app_favorite():
    """API endpoint to toggle app favorite status"""
    from models import App, User
    import json
    
    if 'user_id' not in session:
        return json.dumps({'success': False, 'message': 'Login required'})
    
    app_id = request.form.get('app_id')
    if not app_id:
        return json.dumps({'success': False, 'message': 'App ID required'})
    
    # For now, we'll just return success since favorites aren't fully implemented
    # In a full implementation, you'd have a favorites table
    return json.dumps({
        'success': True,
        'is_favorite': True,
        'message': 'Added to favorites'
    })

@app.route('/api/developer/follow', methods=['POST'])
def api_developer_follow():
    """API endpoint to follow a developer"""
    from models import User
    import json
    
    if 'user_id' not in session:
        return json.dumps({'success': False, 'message': 'Login required'})
    
    developer_email = request.form.get('developer_email')
    if not developer_email:
        return json.dumps({'success': False, 'message': 'Developer email required'})
    
    # For now, we'll just return success since following isn't fully implemented
    return json.dumps({
        'success': True,
        'message': 'Now following developer!'
    })

# Enhanced app detail route
@app.route('/app/detail/<int:app_id>')
def app_detail_view(app_id):
    """App detail page"""
    from models import App, User
    
    app_data = App.query.get_or_404(app_id)
    
    # Note: View tracking will be implemented in future updates
    # For now, we'll just load the app without tracking views
    
    # Get other apps by same developer
    similar_apps = App.query.filter_by(
        author_email=app_data.author_email,
        status='active'
    ).filter(App.id != app_id).limit(3).all()
    
    return render_template('app/app_detail.html', 
                         app=app_data, 
                         similar_apps=similar_apps)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
