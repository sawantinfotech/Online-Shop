from flask import render_template, request, redirect, url_for, flash, session, jsonify, send_file
from werkzeug.utils import secure_filename
from app import app, db
from admin import admin_bp
from models import Service, Payment, Delivery, Category, User, DeliveryProfile, DeliveryVehicle, DeliveryAssignment, PasswordReset, App, MatrimonyProfile
from forms import UserRegisterForm, PaymentSettingsForm, LoginForm
import os
import json
import csv
import io
from datetime import datetime
from utils import allowed_file, save_uploaded_file, calculate_delivery_charges, generate_invoice_pdf
from payment_gateways import process_payment
from sms_service import send_sms
from email_service import (
    send_email, test_email_connection, send_test_email, get_email_settings,
    send_order_confirmation_email, send_payment_confirmation_email
)
import logging

# Session management decorators
def login_required(f):
    from functools import wraps
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in to access this page.', 'error')
            return redirect(url_for('user_login'))
        return f(*args, **kwargs)
    return decorated_function

# BUSINESS SERVICE DISCONNECTED - business_login_required decorator moved to business folder
# def business_login_required - REMOVED (business-dependent)

@app.route('/')
def index():
    # BUSINESS SERVICE DISCONNECTED - removed business_dashboard redirect
    
    if 'user_id' in session:
        return redirect(url_for('subscriber_dashboard'))
    
    # Get featured products and businesses for public home page
    featured_services = Service.query.filter_by(is_active=True).order_by(Service.created_at.desc()).limit(8).all()
    services = Service.query.all()
    
    # Get featured products from Product service
    try:
        from product.product_models import ProductItem
        featured_products = ProductItem.query.filter_by(
            status='active', featured=True
        ).order_by(ProductItem.created_at.desc()).limit(8).all()
    except Exception as e:
        logging.error(f"Error loading featured products: {e}")
        featured_products = []
    
    # BUSINESS SERVICE DISCONNECTED
    featured_businesses = []  # Business entities disconnected
    categories = Category.query.all()
    
    # Get delivery profiles for carousel
    try:
        delivery_profiles = db.session.query(DeliveryProfile).join(
            User, DeliveryProfile.user_id == User.id
        ).filter(DeliveryProfile.verification_status == 'verified').limit(10).all()
    except Exception as e:
        logging.error(f"Error fetching delivery profiles: {e}")
        delivery_profiles = []
    
    # Get featured apps for carousel (include new submissions from last 7 days)
    from datetime import datetime, timedelta
    seven_days_ago = datetime.utcnow() - timedelta(days=7)
    featured_apps = App.query.filter(
        (App.status == 'active') | 
        ((App.status == 'pending') & (App.created_at >= seven_days_ago))
    ).order_by(App.featured.desc(), App.created_at.desc()).limit(20).all()
    
    # Get matrimony profiles for carousel
    matrimony_profiles = MatrimonyProfile.query.filter_by(profile_visible=True).order_by(MatrimonyProfile.created_at.desc()).limit(10).all()
    
    # Get active subscribers for active users section
    try:
        active_subscribers = User.query.filter_by(user_type='subscriber').limit(20).all()
    except Exception as e:
        logging.error(f"Error fetching active subscribers: {e}")
        active_subscribers = []
    
    return render_template('public_home.html', 
                    featured_services=featured_services,
                    featured_products=featured_products,
                    featured_businesses=featured_businesses,
            services=services,
            categories=categories,
                         delivery_profiles=delivery_profiles,
            featured_apps=featured_apps,
                         matrimony_profiles=matrimony_profiles,
                         active_subscribers=active_subscribers)

# BUSINESS SERVICE DISCONNECTED - All business registration functionality moved to business folder

# BUSINESS SERVICE DISCONNECTED - All business login/logout/dashboard functionality moved to business folder

# BUSINESS SERVICE DISCONNECTED - Products route moved to business folder
# @app.route('/product/products') - REMOVED (business-dependent)

# BUSINESS SERVICE DISCONNECTED - All product management routes moved to business folder
# Product add/edit/delete routes - REMOVED (business-dependent)

# BUSINESS SERVICE DISCONNECTED - All customer management routes moved to business folder
# Customer list/add/edit routes - REMOVED (business-dependent)

# BUSINESS SERVICE DISCONNECTED - All order management routes moved to business folder
# Order list/details/status/invoice routes - REMOVED (business-dependent)

# BUSINESS SERVICE DISCONNECTED - Business settings route moved to business folder
# Settings route - REMOVED (business-dependent)

# BUSINESS SERVICE DISCONNECTED - Product import route moved to business folder
# Product import route - REMOVED (business-dependent)

@app.route('/api/delivery_charges', methods=['POST'])
@login_required
def get_delivery_charges():
    data = request.get_json()
    charges = calculate_delivery_charges(
        weight=data.get('weight', 0),
        dimensions=data.get('dimensions', ''),
        location=data.get('location', ''),
        delivery_type=data.get('delivery_type', 'standard')
    )
    return jsonify({'charges': charges})

@app.route('/api/process_payment', methods=['POST'])
@login_required
def process_payment_api():
    data = request.get_json()
    result = process_payment(
        amount=data.get('amount'),
        payment_method=data.get('payment_method'),
        customer_info=data.get('customer_info')
    )
    return jsonify(result)

    # Initialize services
    # Moved to app.py initialization
    def create_default_services():
        if Service.query.count() == 0:
            services = [ Service(service_name='E-commerce', description='Online shopping platform'),
                                          Service(name='Blog', description='Bloging platform'),
                        Service(name='Product', description='  '),
                        Service(name='Business', description=''),
                        Service(name='Apps', description=''),
                        Service(name='Matrimony', description=''),
                        Service(name='Delivery', description='On-demand delivery services'),
                        Service(name='Bank', description=''),
                        Service(name='Finance', description=''),
                        Service(name='Share Market', description=''),
                        Service(name='Stock Exchange', description=''),
                        Service(name='Education', description=''),
                        Service(name='Politics', description=''),
                        Service(name='Sport', description=''),
                        Service(name='Job', description=''),
                        Service(name='Government', description=''),
                       ]
            for service in services:
                db.session.add(service)

            db.session.commit()
            
# Initialize categories
# Moved to app.py initialization
def create_default_categories():
    if Category.query.count() == 0:
        categories = [
            Category(name='Electronics', description='Electronic devices and accessories'),
            Category(name='Clothing', description='Apparel and fashion items'),
            Category(name='Home & Garden', description='Home improvement and gardening'),
            Category(name='Sports', description='Sports equipment and accessories'),
            Category(name='Books', description='Books and educational materials'),
            Category(name='Health & Beauty', description='Health and beauty products'),
            Category(name='Food & Beverages', description='Food items and beverages'),
            Category(name='Other', description='Other products')
        ]
        
        for category in categories:
            db.session.add(category)
        
        db.session.commit()

# Email testing routes
@app.route('/test-email', methods=['GET', 'POST'])
@login_required
def test_email():
    """Test email functionality"""
    if request.method == 'POST':
        test_email_address = request.form.get('test_email')
        
        if not test_email_address:
            flash('Please provide an email address for testing', 'error')
            return redirect(url_for('test_email'))
        
        # Test email connection
        connection_status = test_email_connection()
        
        if connection_status:
            # Send test email
            email_sent = send_test_email(test_email_address)
            if email_sent:
                flash(f'Test email sent successfully to {test_email_address}', 'success')
            else:
                flash('Failed to send test email. Check email configuration.', 'error')
        else:
            flash('Email connection failed. Please check your email settings.', 'error')
        
        return redirect(url_for('test_email'))
    
    # Get email settings
    email_settings = get_email_settings()
    return render_template('/test_email.html', email_settings=email_settings)

@app.route('/email-settings')
@login_required
def email_settings():
    """Display email configuration status"""
    settings = get_email_settings()
    return render_template('/email_settings.html', settings=settings)

# Delivery System Routes

@app.route('/job/job')
def job():
    """Delivery job page"""
    return render_template('job/job_home.html')

@app.route('/delivery/apply_delivery', methods=['GET', 'POST'])
def apply_delivery():
    """Apply for delivery rider position - requires user login"""
    if 'user_id' not in session:
        flash('Please log in to apply for delivery rider position.', 'error')
        return redirect(url_for('user_login'))
    
    user_id = session['user_id']
    business_id = session['servie_id']
    user = User.query.get(user_id, business_id)
    
    # Check if user already has delivery profile
    existing_profile = DeliveryProfile.query.filter_by(user_id=user_id, business_id=business_id).first()
    if existing_profile:
        flash('You have already applied for delivery rider position.', 'warning')
        return redirect(url_for('delivery_dashboard'))
    
    if request.method == 'POST':
        # Get form data
        driving_license = request.form.get('driving_license')
        aadhar_number = request.form.get('aadhar_number')
        emergency_contact = request.form.get('emergency_contact')
        delivery_zone = request.form.get('delivery_zone')
        
        # Vehicle information
        vehicle_type = request.form.get('vehicle_type')
        vehicle_number = request.form.get('vehicle_number')
        license_plate = request.form.get('license_plate')
        insurance_number = request.form.get('insurance_number')
        
        # Create delivery profile
        delivery_profile = DeliveryProfile(
            user_id=user_id,
            business_id=business_id,
            driving_license=driving_license,
            aadhar_number=aadhar_number,
            emergency_contact=emergency_contact,
            delivery_zone=delivery_zone,
            status='pending',
            verification_status='pending'
        )
        
        db.session.add(delivery_profile)
        db.session.flush()  # Get the ID
        
        # Create vehicle
        vehicle = DeliveryVehicle(
            delivery_profile_id=delivery_profile.id,
            vehicle_type=vehicle_type,
            vehicle_number=vehicle_number,
            license_plate=license_plate,
            insurance_number=insurance_number
        )
        
        # Handle vehicle photo
        vehicle_photo = request.files.get('vehicle_photo')
        if vehicle_photo and allowed_file(vehicle_photo.filename):
            vehicle_filename = save_uploaded_file(vehicle_photo, 'vehicles')
            vehicle.vehicle_photo = vehicle_filename
        
        db.session.add(vehicle)
        db.session.commit()
        
        flash('Delivery rider application submitted! Please pay registration fee of ₹500 for verification.', 'success')
        return redirect(url_for('delivery_payment'))
    
    return render_template('/delivery/delivery_application.html', user=user)

# Removed user_login - now using unified subscriber authentication

@app.route('/delivery/delivery_dashboard')
def delivery_dashboard():
    """Unified delivery dashboard"""
    if 'user_id' not in session:
        flash('Please log in to access the dashboard.', 'error')
        return redirect(url_for('user_login'))
    
    user_id = session['user_id', 'business_id']
    user = User.query.get(user_id, business_id)
    delivery_profile = DeliveryProfile.query.filter_by(user_id=user_id, business_id=business_id).first()
    
    if not delivery_profile:
        flash('You need to apply for delivery rider position first.', 'error')
        return redirect(url_for('apply_delivery'))
    
    # Get recent assignments
    recent_assignments = DeliveryAssignment.query.filter_by(
        delivery_profile_id=delivery_profile.id
    ).order_by(DeliveryAssignment.created_at.desc()).limit(10).all()
    
    # Get statistics
    total_deliveries = DeliveryAssignment.query.filter_by(
        delivery_profile_id=delivery_profile.id,
        status='delivered'
    ).count()
    
    pending_deliveries = DeliveryAssignment.query.filter(
        DeliveryAssignment.delivery_profile_id == delivery_profile.id,
        DeliveryAssignment.status.in_(['assigned', 'picked_up', 'in_transit'])
    ).count()
    
    total_earnings = db.session.query(db.func.sum(DeliveryAssignment.delivery_fee)).filter_by(
        delivery_profile_id=delivery_profile.id,
        status='delivered'
    ).scalar() or 0
    
    stats = {
        'total_deliveries': total_deliveries,
        'pending_deliveries': pending_deliveries,
        'total_earnings': total_earnings,
        'rating': delivery_profile.rating
    }
    
    return render_template('/delivery/delivery_dashboard.html', 
                         user=user,
                         delivery_profile=delivery_profile,
                         assignments=recent_assignments,
                         stats=stats)

@app.route('/logout')
def user_logout():
    """User logout"""
    session.pop('user_id', None)
    session.pop('user_email', None)
    session.pop('user_mobile', None)
    session.pop('user_name', None)
    session.pop('user_role', None)
    session.pop('business_id', None)
    session.pop('delivery_profile_id', None)
    session.pop('is_delivery_rider', None)
    flash('You have been logged out successfully.', 'info')
    return redirect(url_for('index'))

@app.route('/user/subscriber_dashboard')
def subscriber_dashboard():
    """Subscriber dashboard"""
    if 'user_id' not in session:
        flash('Please log in to access your dashboard.', 'error')
        return redirect(url_for('user_login'))
    
    user_id = session['user_id']
    user = User.query.get(user_id)
    delivery_profile = DeliveryProfile.query.filter_by(user_id=user_id).first()
    
    return render_template('/user/subscriber_dashboard.html', user=user, delivery_profile=delivery_profile)

# User Registration Route (Main registration page)
@app.route('/user_register', methods=['GET', 'POST'])
def user_register():
    """Handle subscriber registration"""
    if request.method == 'POST':
        # Get form data
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        mobile = request.form.get('mobile')
        password = request.form.get('password')
         # Check if user already exists-optional
        from sqlalchemy import or_
        user = User.query.filter(or_(User.email == login, User.username == login)).first()

        # Check if user already exists
        existing_user = User.query.filter_by(email=email).first()
        existiog_user = User.query.filter_by(mobile=mobile).first()
        if existing_user:
            flash('Email already registered. Please login instead.', 'error')
            flash('Mobile already registered. Please login instead.',)
            return render_template('/user_register.html')
        
        # Create new user
        try:
            user = User()
            user.email = email
            user.mobile = mobile
            user.first_name = first_name
            user.last_name = last_name
            user.user_type = 'subscriber'
            user.set_password(password)
            
            db.session.add(user)
            db.session.commit()
            
            # Login the user immediately after registration
            session['user_id'] = user.id
            session['user_email'] = user.email
            session['user_mobile'] = user.mobile
            session['user_name'] = user.first_name
            session['user_type'] = user.user_type
            flash('Registration successful! Welcome to Mobile Shop Hub!', 'success')
            
            # Redirect to subscriber dashboard
            return redirect(url_for('/user/subscriber_dashboard'))
            
        except Exception as e:
            logging.error(f"Error creating user: {e}")
            flash('Registration failed. Please try again.', 'error')
            return render_template('/user_register.html')
    
    return render_template('/user_register.html')

# User Login Route
@app.route('/user_login', methods=['GET', 'POST'])
def user_login():
    """Handle subscriber login"""
    if request.method == 'POST':
        email = request.form.get('email')
        mobile = request.form.get('mobile')
        password = request.form.get('password')
        
        # Find user
        user = User.query.filter_by(email=email).first() or User.query.filter_by(mobile=mobile).first()
        if user and user.check_password(password):
            # Update online status
            user.is_online = True
            user.last_seen = datetime.utcnow()
            db.session.commit()
            
            # Set session
            session['user_id'] = user.id
            session['user_email'] = user.email
            session['user_mobile'] = user.mobile
            session['user_name'] = user.full_name
            session['user_type'] = user.user_type
            flash('Login successful!', 'success')
            
            # Redirect to subscriber dashboard
            return redirect(url_for('subscriber_dashboard'))
        else:
            flash('Invalid email or password.', 'error')
            return render_template('/user_login.html')
    
    return render_template('/user_login.html')

# Subscriber Dashboard
@app.route('/user/subscriber_dashboard')
def subscriber_dashboard():
    """Display subscriber dashboard with all subscriptions and services"""
    if 'user_id' not in session:
        flash('Please login to access your dashboard.', 'error')
        return redirect(url_for('user_login'))
    
    user = User.query.get(session['user_id'])
    if not user:
        flash('User not found. Please login again.', 'error')
        return redirect(url_for('user_login'))
    
    # Get user's app submissions
    submitted_apps = App.query.filter_by(user_id=user.id).all()
    approved_apps = [app for app in submitted_apps if app.status == 'approved']
    pending_apps = [app for app in submitted_apps if app.status == 'pending']
    total_downloads = sum(app.downloads or 0 for app in submitted_apps)
    
    # Get user's service requests
    service_requests = Service.query.filter_by(user_id=user.id).all()
    pending_requests = len([s for s in service_requests if s.status == 'pending'])
    approved_requests = len([s for s in service_requests if s.status == 'approved'])
    
    # Get user's products (Product Service)
    try:
        from product.product_models import ProductItem
        user_products = ProductItem.query.filter_by(added_by=user.id).all()
        active_products = [p for p in user_products if p.status == 'active']
        featured_user_products = [p for p in user_products if p.featured and p.status == 'active']
        total_product_views = sum(p.view_count or 0 for p in user_products)
    except Exception as e:
        logging.error(f"Error loading user products: {e}")
        user_products = []
        active_products = []
        featured_user_products = []
        total_product_views = 0
    
    return render_template('/user/subscriber_dashboard.html', 
                         user=user,
                         submitted_apps=submitted_apps,
                         approved_apps=approved_apps,
                         pending_apps=pending_apps,
                         total_downloads=total_downloads,
                         service_requests=service_requests,
                         pending_requests=pending_requests,
                         approved_requests=approved_requests,
                         user_products=user_products,
                         active_products=active_products,
                         featured_user_products=featured_user_products,
                         total_product_views=total_product_views)

# Subscriber Profile
@app.route('/user/subscriber_profile')
def subscriber_profile():
    """Display subscriber profile"""
    if 'user_id' not in session:
        flash('Please login to access your profile.', 'error')
        return redirect(url_for('user_login'))
    
    user = User.query.get(session['user_id'])
    if not user:
        flash('User not found. Please login again.', 'error')
        return redirect(url_for('user_login'))
    
    return render_template('/user/subscriber_profile.html', user=user)

# Update Subscriber Profile
@app.route('/user/subscriber_profile', methods=['GET', 'POST'])
def update_subscriber_profile():
    """Handle subscriber profile updates"""
    if 'user_id' not in session:
        flash('Please login to access this page.', 'error')
        return redirect(url_for('user_login'))
    
    user = User.query.get(session['user_id'])
    if not user:
        flash('User not found. Please login again.', 'error')
        return redirect(url_for('user_login'))
    
    if request.method == 'POST':
        try:
            # Update user profile
            user.service = request.form.get('service', user.service)
            user.subscription = request.form.get('subscription', user.subscription)
            user.profile_photo = request.form.get('profile_photo', user.profile_photo)
            user.full_name = request.form.get('full_name', user.full_name)
            user.first_name = request.form.get('first_name', user.first_name)
            user.last_name = request.form.get('last_name', user.last_name)
            user.email = request.form.get('email', user.email)
            user.mobile = request.form.get('mobile', user.mobile)
            user.gender = request.form.get('gender', user.gender)
            user.dob = request.form.get('dob', user.dob)
            user.age = request.form.get('age', user.age)
            user.marital_status = request.form.get('marital_status', user.marital_status)
            user.religion = request.form.get('religion', user.religion)
            user.caste = request.form.get('caste', user.caste)
            user.subcaste = request.form.get('subcaste', user.subcaste)
            user.nationality = request.form.get('nationality', user.nationality)
            user.blood_group = request.form.get('blood_group', user.blood_group)
            user.height = request.form.get('height', user.height)
            user.weight = request.form.get('weight', user.weight)
            user.body_type = request.form.get('body_type', user.body_type)
            user.complexion = request.form.get('complexion', user.complexion)
            user.eye_color = request.form.get('eye_color', user.eye_color)
            user.hair_color = request.form.get('hair_color', user.hair_color)
            user.skin_tone = request.form.get('skin_tone', user.skin_tone)
            user.physical_disability = request.form.get('physical_disability', user.physical_disability)
            user.mental_disability = request.form.get('mental_disability', user.mental_disability)
            user.address = request.form.get('address', user.address)
            user.city = request.form.get('city', user.city)
            user.district = request.form.get('district', user.district)
            user.pincode = request.form.get('pincode', user.pincode)
            user.state = request.form.get('state', user.state)
            user.country = request.form.get('country', user.country)
            user.language = request.form.get('language', user.language)
            user.education = request.form.get('education', user.education)
            user.occupation = request.form.get('occupation', user.occupation)
            user.about_me = request.form.get('about_me', user.about_me)
            user.hobbies = request.form.get('hobbies', user.hobbies)
            user.website = request.form.get('website', user.website)
            user.buddhistan = request.form.get('buddhistan', user.buddhistan)
            user.facebook = request.form.get('facebook', user.facebook)
            user.twitter = request.form.get('twitter', user.twitter)
            user.instagram = request.form.get('instagram', user.instagram)
            user.linkedin = request.form.get('linkedin', user.linkedin)
            user.whatsapp = request.form.get('whatsapp', user.whatsapp)
            user.youtube = request.form.get('youtube', user.youtube)
            
            
            user.plan = request.form.get('plan', user.plan)
            user.plan_expiry = request.form.get('plan_expiry', user.plan_expiry)
            user.plan_status = request.form.get('plan_status', user.plan_status)
            user.plan_renewal = request.form.get('plan_renewal', user.plan_renewal)
            user.order = request.form.get('order', user.order)
            user.order_status = request.form.get('order_status', user.order_status)
            user.payment = request.form.get('payment', user.payment)
            user.payment_status = request.form.get('payment_status', user.payment_status)
            user.job_status = request.form.get('job_status', user.job_status)
            user.relationship_status = request.form.get('relationship_status', user.relationship_status)
            user.relationship_type = request.form.get('relationship_type', user.relationship_type)
            user.relationship_preference = request.form.get('relationship_preference', user.relationship_preference)
            user.relationship_interest = request.form.get('relationship_interest', user.relationship_interest)   
            user.bank_account = request.form.get('bank_account', user.bank_account)
            user.political_status = request.form.get('political_status', user.political_status)
            user.political_party = request.form.get('political_party', user.political_party)
            user.political_interest = request.form.get('political_interest', user.political_interest)
            user.console_filecode = request.form.get('console_filecode', user.console_filecode)
           
            
            # Update password if provided
            new_password = request.form.get('new_password')
            if new_password:
                user.set_password(new_password)
            
            db.session.commit()
            flash('Profile updated successfully!', 'success')
            return redirect(url_for('subscriber_profile'))
            
        except Exception as e:
            logging.error(f"Error updating profile: {e}")
            flash('Profile update failed. Please try again.', 'error')
    
    return render_template('/user/subscriber_profile.html', user=user)

# Service Home Pages (accessible to logged-in subscribers)
@app.route('/app/app_home')
def apps_home():
    """Apps service home page"""
    if 'user_id' not in session:
        flash('Please login to access this service.', 'error')
        return redirect(url_for('user_login'))
    
    user = User.query.get(session['user_id', 'business_id'])
    # Include newly created apps (last 7 days) and active apps
    from datetime import datetime, timedelta
    seven_days_ago = datetime.utcnow() - timedelta(days=7)
    featured_apps = App.query.filter(
        (App.status == 'active') | 
        ((App.status == 'pending') & (App.created_at >= seven_days_ago))
    ).order_by(App.featured.desc(), App.created_at.desc()).limit(12).all()
    return render_template('app/app_home.html', user=user, featured_apps=featured_apps)

@app.route('/business/business_home')
# BUSINESS SERVICE DISCONNECTED
# def business_home():
#     """Business service home page"""
#     if 'user_id' not in session:
#         flash('Please login to access this service.', 'error')
#         return redirect(url_for('user_login'))
#     
#     user = User.query.get(session['user_id', 'business_id'])
#     featured_businesses = Business.query.filter_by(verification_status='verified').limit(12).all()
#     return render_template('/business/business_home.html', user=user, featured_businesses=featured_businesses)

@app.route('/matrimony/matrimony_home')
def matrimony_home():
    """Matrimony service home page"""
    if 'user_id' not in session:
        flash('Please login to access this service.', 'error')
        return redirect(url_for('user_login'))
    
    user = User.query.get(session['user_id', 'business_id'])
    featured_profiles = MatrimonyProfile.query.filter_by(profile_visible=True).limit(12).all()
    return render_template('/matrimony/matrimony_home.html', user=user, featured_profiles=featured_profiles)

@app.route('/delivery/delivery_home')
def delivery_home():
    """Delivery service home page"""
    if 'user_id' not in session:
        flash('Please login to access this service.', 'error')
        return redirect(url_for('user_login'))
    
    user = User.query.get(session['user_id', 'business_id'])
    return render_template('/delivery/delivery_home.html', user=user)

@app.route('/bank/bank_home')
def bank_home():
    """Banking service home page"""
    if 'user_id' not in session:
        flash('Please login to access this service.', 'error')
        return redirect(url_for('user_login'))
    
    user = User.query.get(session['user_id', 'business_id'])
    return render_template('bank/bank_home.html', user=user)

@app.route('/finance/finance_home') 
def finance_home():
    """Finance service home page"""
    if 'user_id' not in session:
        flash('Please login to access this service.', 'error')
        return redirect(url_for('user_login'))
    
    user = User.query.get(session['user_id', 'business_id'])
    return render_template('finance/finance_home.html', user=user)

@app.route('/education/education_home')
def education_home():
    """Education service home page"""
    if 'user_id' not in session:
        flash('Please login to access this service.', 'error')
        return redirect(url_for('user_login'))
    
    user = User.query.get(session['user_id', 'business_id'])
    return render_template('education/education_home.html', user=user)

@app.route('/news/news_home')
def news_home():
    """News service home page"""
    if 'user_id' not in session:
        flash('Please login to access this service.', 'error')
        return redirect(url_for('user_login'))
    
    user = User.query.get(session['user_id', 'servcie_id'])
    return render_template('/news/news_home.html', user=user)

@app.route('/event/event_home')
def event_home():
    """Events service home page"""
    if 'user_id' not in session:
        flash('Please login to access this service.', 'error')
        return redirect(url_for('user_login'))
    
    user = User.query.get(session['user_id', 'business_id'])
    return render_template('/event/event_home.html', user=user)

@app.route('/offer/offer_home')
def offer_home():
    """Offer service home page"""
    if 'user_id' not in session:
        flash('Please login to access this service.', 'error')
        return redirect(url_for('user_login'))
    
    user = User.query.get(session['user_id', 'business_id'])
    return render_template('/offer/offer_home.html', user=user)

# Public accessible service home pages (no login required)

@app.route('/job/job_home')
def job_home():
    """Job service home page - Public access"""
    return render_template('job/job_home.html')

@app.route('/ai/ai_home')
def ai_home():
    """AI service home page - Public access"""
    return render_template('artificial_intelligence/ai_home.html')

@app.route('/brainlo/brainlo_home')
def brainlo_home():
    """Brainlo service home page - Public access"""
    return render_template('brainlo/brainlo_home.html')

@app.route('/console/console_home')
def console_home():
    """Console service home page - Public access"""
    return render_template('console/console_home.html')

@app.route('/chat/chat_home')
def chat_home():
    """Chat service home page - Public access"""
    return render_template('chat/chat_home.html')

@app.route('/social/social_home')
def social_home():
    """Social Media service home page - Public access"""
    return render_template('social/social_home.html')

@app.route('/email/email_home')
def email_home():
    """Email service home page - Public access"""
    return render_template('email/email_home.html')

@app.route('/sms/sms_home')
def sms_home():
    """SMS service home page - Public access"""
    return render_template('sms/sms_home.html')

@app.route('/news/news_home')
def news_home():
    """News service home page - Public access"""
    return render_template('news/news_home.html')

@app.route('/blog/blog_home')
def blog_home():
    """Blog service home page - Public access"""
    return render_template('blog/blog_home.html')

@app.route('/post/post_home')
def post_home():
    """Post service home page - Public access"""
    return render_template('post/post_home.html')

@app.route('/story/story_home')
def story_home():
    """Story service home page - Public access"""
    return render_template('story/story_home.html')

@app.route('/reel/reel_home')
def reel_home():
    """Reel service home page - Public access"""
    return render_template('reel/reel_home.html')

@app.route('/legal/legal_home')
def legal_home():
    """Legal service home page - Public access"""
    return render_template('legal/legal_home.html')

@app.route('/ca/ca_home')
def ca_home():
    """Chartered Accountant service home page - Public access"""
    return render_template('chartered_accountant/ca_home.html')

@app.route('/govt/govt_home')
def govt_home():
    """Government service home page - Public access"""
    return render_template('government/govt_home.html')

@app.route('/police/police_home')
def police_home():
    """Police service home page - Public access"""
    return render_template('police/police_home.html')

@app.route('/politics/politics_home')
def politics_home():
    """Politics service home page - Public access"""
    return render_template('politics/politics_home.html')

@app.route('/marketing/marketing_home')
def marketing_home():
    """Marketing service home page - Public access"""
    return render_template('marketing/marketing_home.html')

@app.route('/advertise/advertise_home')
def advertise_home():
    """Advertise service home page - Public access"""
    return render_template('advertise/advertise_home.html')

@app.route('/property/property_home')
def property_home():
    """Property service home page - Public access"""
    return render_template('property/property_home.html')

@app.route('/public_market/publicmarket_home')
def public_home():
    """Public Market service home page - Public access"""
    return render_template('public_market/publicmarket_home.html')

@app.route('/agriculture/agriculture_home')
def agriculture_home():
    """Agriculture service home page - Public access"""
    return render_template('agriculture/agriculture_home.html')

@app.route('/sport/sport_home')
def sport_home():
    """Sport service home page - Public access"""
    return render_template('sport/sport_home.html')

@app.route('/event/event_home')
def event_home():
    """Event service home page - Public access"""
    return render_template('event/event_home.html')

@app.route('/language/language_home')
def language_home():
    """Language service home page - Public access"""
    return render_template('language/language_home.html')

@app.route('/live/live_home')
def live_home():
    """Live service home page - Public access"""
    return render_template('live/live_home.html')

@app.route('/creditpoint/creditpoint_home')
def creditpoint_home():
    """Credit Points service home page - Public access"""
    return render_template('creditpoint/creditpoint_home.html')

@app.route('/partner/partner_home')
def partner_home():
    """Partner service home page"""
    if 'user_id' not in session:
        flash('Please login to access this service.', 'error')
        return redirect(url_for('user_login'))
    
    user = User.query.get(session['user_id', 'business_id'])
    return render_template('/partner/partner_home.html', user=user)

# Service Registration Routes (for plan selection and payment)
@app.route('/app/app_registration')
def app_registration():
    """App service registration with plan selection"""
    if 'user_id' not in session:
        flash('Please login to register for this service.', 'error')
        return redirect(url_for('user_login'))
    
    user = User.query.get(session['user_id', 'business_id'])
    # Here you would fetch pricing plans from database
    return render_template('/app/app_registration.html', user=user)

# BUSINESS SERVICE DISCONNECTED
# @app.route('/business/business_register')
# def business_register():
#     """Business service registration with plan selection"""
#     if 'user_id' not in session:
#         flash('Please login to register for this service.', 'error')
#         return redirect(url_for('user_login'))
#     
#     user = User.query.get(session['user_id', 'business_id'])
#     return render_template('/business/business_register.html', user=user)

@app.route('/matrimony/matrimony_register')
def matrimony_register():
    """Matrimony service registration with plan selection"""
    if 'user_id' not in session:
        flash('Please login to register for this service.', 'error')
        return redirect(url_for('user_login'))
    
    user = User.query.get(session['user_id', 'business_id'])
    return render_template('/matrimony/matrimony_register.html', user=user)

# Note: user_logout route already exists above at line 654

# Removed delivery_login - now using unified subscriber authentication

@app.route('/delivery/delivery_application', methods=['GET', 'POST'])
def delivery_application():
    """Delivery rider application form"""
    if 'user_id' not in session:
        flash('Please log in to apply for delivery rider position.', 'error')
        return redirect(url_for('user_login'))
    
    user_id = session['user_id']
    business_id = session['business_id']
    user = User.query.get(user_id, business_id)
    
    # Check if user already has delivery profile
    existing_profile = DeliveryProfile.query.filter_by(user_id=user_id).first()
    if existing_profile:
        flash('You have already applied for delivery rider position.', 'warning')
        return redirect(url_for('delivery_dashboard'))
    
    if request.method == 'POST':
        driving_license = request.form.get('driving_license')
        aadhar_number = request.form.get('aadhar_number')
        emergency_contact = request.form.get('emergency_contact')
        delivery_zone = request.form.get('delivery_zone')
        
        # Create delivery profile
        delivery_profile = DeliveryProfile(
            user_id=user_id,
            business_id=business_id,
            driving_license=driving_license,
            aadhar_number=aadhar_number,
            emergency_contact=emergency_contact,
            delivery_zone=delivery_zone,
            status='pending',
            verification_status='pending'
        )
        db.session.add(delivery_profile)
        db.session.commit()
        
        flash('Application submitted successfully! Please complete the registration fee payment.', 'success')
        return redirect(url_for('delivery_payment'))
    
    return render_template('/delivery/delivery_application.html', user=user)

@app.route('/delivery/delivery_payment')
def delivery_payment():
    """Delivery registration fee payment"""
    if 'user_id' not in session:
        flash('Please log in to access this page.', 'error')
        return redirect(url_for('user_login'))
    
    user_id = session['user_id']
    delivery_profile = DeliveryProfile.query.filter_by(user_id=user_id).first()
    
    if not delivery_profile:
        flash('No delivery application found.', 'error')
        return redirect(url_for('apply_delivery'))
    
    if delivery_profile.registration_fee_paid:
        flash('Registration fee already paid.', 'info')
        return redirect(url_for('subscriber_dashboard'))
    
    return render_template('/delivery/delivery_payment.html', delivery_profile=delivery_profile)

# Password Reset Routes

@app.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    """Forgot password page"""
    if request.method == 'POST':
        email = request.form.get('email')
        mobile = request.form.get('mobile')
        user_type = request.form.get('user_type', 'subscriber','')
        
        # Generate reset token
        import secrets
        reset_token = secrets.token_urlsafe(32)
        
        # Check if user exists
        user_exists = False
        if user_type == 'subscriber':
            user_exists = Subscriber.query.filter_by(email=email).first() or Subscriber.query.filter_by(mobile=mobile).first()
        elif user_type == 'user':
            user_exists = User.query.filter_by(email=email).first() or User.query.filter_by(mobile=mobile).first()
        if user_exists:
            # Create password reset record
            from datetime import datetime, timedelta
            reset_record = PasswordReset(
                email=email,
                mobile=mobile,
                user_type=user_type,
                reset_token=reset_token,
                expires_at=datetime.utcnow() + timedelta(hours=1)
            )
            db.session.add(reset_record)
            db.session.commit()
            
            # Send email (in real implementation)
            # send_password_reset_email(email, reset_token)
            
            flash('Password reset link has been sent to your email.', 'success')
        else:
            flash('Email address not found.', 'error')
    
    return render_template('/forgot_password.html')

@app.route('/reset-password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    """Reset password with token"""
    reset_record = PasswordReset.query.filter_by(reset_token=token, used=False).first()
    
    if not reset_record or reset_record.expires_at < datetime.utcnow():
        flash('Invalid or expired reset link.', 'error')
        return redirect(url_for('forgot_password'))
    
    if request.method == 'POST':
        new_password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        if new_password != confirm_password:
            flash('Passwords do not match.', 'error')
            return render_template('/reset_password.html', token=token)
        
        # Update password based on user type
        if reset_record.user_type == 'subscriber':
            user = Subscriber.query.filter_by(email=reset_record.email).first()
        elif reset_record.user_type == 'user':
            user = User.query.filter_by(email=reset_record.email).first()
        
        if user:
            user.set_password(new_password)
            reset_record.used = True
            db.session.commit()
            
            flash('Password has been reset successfully. You can now log in.', 'success')
            if reset_record.user_type == 'subscriber':
                return redirect(url_for('user_login'))
            elif reset_record.user_type == 'user':
                return redirect(url_for('user_login'))
        else:
            flash('User not found.', 'error')
    
    return render_template('/reset_password.html', token=token)

# Apps Routes

@app.route('/app/apps')
def apps():
    """Apps showcase page"""
    apps = App.query.filter_by(status='active').order_by(App.featured.desc(), App.downloads.desc()).all()
    services = db.session.query(App.service).distinct().all()
    categories = db.session.query(App.category).distinct().all()
    return render_template('/app/apps.html', apps=apps, services=services, categories=categories)

@app.route('/app/app_detail/<slug>')
@app.route('/app/apps/<slug>')
def app_detail(slug):
    """Individual app detail page"""
    app_detail = App.query.filter_by(slug=slug, status='active').first_or_404()
    return render_template('/app/app_detail.html', app=app_detail)

# API endpoints for favorites, follows, and shares
@app.route('/api/app/favorite/<int:app_id>', methods=['POST'])
def toggle_app_favorite(app_id):
    """Toggle favorite status for an app"""
    try:
        if 'user_id' not in session:
            return jsonify({'success': False, 'message': 'Please log in to add favorites'}), 401
        
        from models import AppFavorite
        user_id = session['user_id']
        
        # Check if already favorited
        existing_favorite = AppFavorite.query.filter_by(user_id=user_id, app_id=app_id).first()
        
        if existing_favorite:
            db.session.delete(existing_favorite)
            db.session.commit()
            return jsonify({'success': True, 'is_favorite': False, 'message': 'Removed from favorites'})
        else:
            new_favorite = AppFavorite(user_id=user_id, app_id=app_id)
            db.session.add(new_favorite)
            db.session.commit()
            return jsonify({'success': True, 'is_favorite': True, 'message': 'Added to favorites'})
            
    except Exception as e:
        return jsonify({'success': False, 'message': f'Error: {str(e)}'}), 500

@app.route('/api/developer/follow', methods=['POST'])
def toggle_developer_follow():
    """Toggle follow status for a developer"""
    try:
        if 'user_id' not in session:
            return jsonify({'success': False, 'message': 'Please log in to follow developers'}), 401
        
        from models import AppFollow
        user_id = session['user_id']
        developer_email = request.form.get('developer_email')
        
        if not developer_email:
            return jsonify({'success': False, 'message': 'Developer email required'}), 400
        
        # Check if already following
        existing_follow = AppFollow.query.filter_by(user_id=user_id, developer_email=developer_email).first()
        
        if existing_follow:
            db.session.delete(existing_follow)
            db.session.commit()
            return jsonify({'success': True, 'is_following': False, 'message': 'Unfollowed developer'})
        else:
            new_follow = AppFollow(user_id=user_id, developer_email=developer_email)
            db.session.add(new_follow)
            db.session.commit()
            return jsonify({'success': True, 'is_following': True, 'message': 'Now following developer'})
            
    except Exception as e:
        return jsonify({'success': False, 'message': f'Error: {str(e)}'}), 500

@app.route('/api/app/share/<int:app_id>', methods=['POST'])
def record_app_share(app_id):
    """Record app share action"""
    try:
        from models import AppShare
        platform = request.form.get('platform', 'unknown')
        user_id = session.get('user_id')
        
        # Record share
        new_share = AppShare(
            app_id=app_id,
            user_id=user_id,
            platform=platform
        )
        db.session.add(new_share)
        db.session.commit()
        
        return jsonify({'success': True, 'message': f'Shared on {platform}'})
        
    except Exception as e:
        return jsonify({'success': False, 'message': f'Error: {str(e)}'}), 500

@app.route('/api/app/download/<int:app_id>', methods=['POST'])
def record_app_download(app_id):
    """Record app download action"""
    try:
        # Increment download count
        app = App.query.get(app_id)
        if app:
            app.downloads += 1
            db.session.commit()
            return jsonify({'success': True, 'message': 'Download recorded'})
        else:
            return jsonify({'success': False, 'message': 'App not found'}), 404
            
    except Exception as e:
        return jsonify({'success': False, 'message': f'Error: {str(e)}'}), 500

@app.route('/app/all_apps')
def all_apps():
    """All apps listing page"""
    apps = App.query.filter_by(status='active').order_by(App.featured.desc(), App.downloads.desc()).all()
    categories = db.session.query(App.category).distinct().all()
    return render_template('/app/all_apps.html', apps=apps, categories=categories)

@app.route('/app/apps/service/<service>')
@app.route('/app/apps/category/<category>')
def apps_by_category(category=None, service=None):
    """Apps filtered by category or service"""
    if category:
        apps = App.query.filter_by(category=category, status='active').order_by(App.downloads.desc()).all()
    elif service:
        apps = App.query.filter_by(service=service, status='active').order_by(App.downloads.desc()).all()
    else:
        apps = App.query.filter_by(status='active').order_by(App.downloads.desc()).all()
    
    categories = db.session.query(App.category).distinct().all()
    return render_template('/app/all_apps.html', apps=apps, categories=categories, selected_category=category)

@app.route('/service/services','/category/categories')
def services_categories():
    """Categories page with listings for all service types"""
    # Get counts for each category
    business_count = Business.query.filter_by(verification_status='verified').count()
    product_count = Product.query.filter_by(is_active=True).count()
    app_count = App.query.filter_by(status='active').count()
    delivery_count = DeliveryProfile.query.filter_by(verification_status='verified').count()
    matrimony_count = MatrimonyProfile.query.filter_by(is_verified=True).count()
    console_count = ConsoleFilecode.query.filter_by(is_verified=True).count()
    
    # Get sample listings for each service & category
    featured_services = Service.query.filter_by(is_active=True).limit(6).all()
    featured_businesses = Business.query.filter_by(verification_status='verified').limit(6).all()
    # Get featured products from Product service
    try:
        from product.product_models import ProductItem
        featured_products = ProductItem.query.filter_by(
            status='active', featured=True
        ).order_by(ProductItem.created_at.desc()).limit(6).all()
    except Exception as e:
        logging.error(f"Error loading featured products: {e}")
        featured_products = []
    featured_apps = App.query.filter_by(status='active').limit(6).all()
    featured_delivery = DeliveryProfile.query.filter_by(verification_status='verified').limit(6).all()
    featured_matrimony = MatrimonyProfile.query.filter_by(is_verified=True).limit(6).all()
    featured_console = ConsoleFilecode.query.filter_by(is_verified=True).limit(6).all()
    service_data = {
        'business': {
            'count': business_count,
            'items': featured_businesses,
            'title': 'Business Listings',
            'icon': 'fas fa-store',
            'color': 'primary'
        },
        'product': {
            'count': product_count,
            'items': featured_products,
            'title': 'Product Listings',
            'icon': 'fas fa-box',
            'color': 'success'
        },
        'app': {
            'count': app_count,
            'items': featured_apps,
            'title': 'App Listings',
            'icon': 'fas fa-mobile-alt',
            'color': 'info'
        },
        'delivery': {
            'count': delivery_count,
            'items': featured_delivery,
            'title': 'Delivery Partners',
            'icon': 'fas fa-truck',
            'color': 'warning'
        },
        'matrimony': {
            'count': matrimony_count,
            'items': featured_matrimony,
            'title': 'Matrimonial Listings',
            'icon': 'fas fa-heart',
            'color': 'danger'
        },
        'console': {
            'count': console_count,
            'items': featured_console,
            'title': 'Console Listings',
            'icon': 'fas fa-code',
            'color': 'info'
        },
    }
    category_data = {
        'business': {
            'count': business_count,
            'items': featured_businesses,
            'title': 'Business Listings',
            'icon': 'fas fa-store',
            'color': 'primary'
        },
        'product': {
            'count': product_count,
            'items': featured_products,
            'title': 'Product Listings',
            'icon': 'fas fa-box',
            'color': 'success'
        },
        'app': {
            'count': app_count,
            'items': featured_apps,
            'title': 'App Listings',
            'icon': 'fas fa-mobile-alt',
            'color': 'info'
        },
        'delivery': {
            'count': delivery_count,
            'items': featured_delivery,
            'title': 'Delivery Partners',
            'icon': 'fas fa-truck',
            'color': 'warning'
        },
        'matrimony': {
            'count': matrimony_count,
            'items': featured_matrimony,
            'title': 'Matrimonial Listings',
            'icon': 'fas fa-heart',
            'color': 'danger'
        },
        'console': {
            'count': console_count,
            'items': featured_console,
            'title': 'Console Listings',
            'icon': 'fas fa-code',
            'color': 'info'
        },
    }
    
    return render_template('/service/service_home.html', service_data=service_data, category_data=category_data)

@app.route('/product/all-products')
def all_products():
    """All products page with grid/list view toggle"""
    view_type = request.args.get('view', 'grid')
    search = request.args.get('search', '')
    service_id = request.args.get('service', '')
    category_id = request.args.get('category', '')
    
    query = Product.query.filter_by(is_active=True)
    
    if search:
        query = query.filter(Product.product_name.contains(search))
        
    if category_id:
        query = query.filter_by(category_id=category_id)
    
    products = query.order_by(Product.created_at.desc()).all()
    services = Service.query.all()
    categories = Category.query.all()
    
    return render_template('/product/all_products.html', 
                         products=products, 
                         services=services,  
                         categories=categories,
                         view_type=view_type,
                         search=search,
                         category_id=category_id)

# BUSINESS SERVICE DISCONNECTED
# @app.route('/business/all_businesses')
# def all_businesses():
#     """All businesses page with grid/list view toggle"""
#     view_type = request.args.get('view', 'grid', 'list')
#     search = request.args.get('search', '')
#     business_type = request.args.get('type', '')
#     
#     query = Business.query.filter_by(verification_status='verified')
#     
#     if search:
#         query = query.filter(Business.business_name.contains(search))
#     if business_type:
#         query = query.filter_by(business_type=business_type)
#     
#     businesses = query.order_by(Business.created_at.desc()).all()
#     business_types = db.session.query(Business.business_type).distinct().all()
#     
#     return render_template('/business/all_businesses.html', 
#                          businesses=businesses,
#                          business_types=business_types,
#                          view_type=view_type,
#                          search=search,
#                          business_type=business_type)

@app.route('/app/all_apps')
def all_apps():
    """All apps page with grid/list view toggle"""
    view_type = request.args.get('view', 'grid', 'list')
    search = request.args.get('search', '')
    service = request.args.get('service', '')
    category = request.args.get('category', '')
    
    query = App.query.filter_by(status='active')
    
    if search:
        query = query.filter(App.name.contains(search))
    if service: query = query.filter_by(service=service)
    
    if category:
        query = query.filter_by(category=category)
    
    apps = query.order_by(App.downloads.desc()).all()
    services = db.session.query(App.service).distinct().all()
    categories = db.session.query(App.category).distinct().all()
    
    return render_template('/app/all_apps.html', 
                         apps=apps,
                         services=services,  
                         categories=categories,
                         view_type=view_type,
                         search=search,
selected_service=service,                         selected_category=category)

@app.route('/app/app_registration', methods=['GET', 'POST'])
def submit_app():
    """App registration/submission page"""
    from forms import AppSubmissionForm
    from models import AppSubmission
    
    form = AppSubmissionForm()
    
    if form.validate_on_submit():
        try:
            # Create new app submission
            submission = AppSubmission()
            
            # Basic app information
            submission.business_id = session.get('business_id')
            submission.user_id = session.get('user_id')
            submission.app_name = form.app_name.data
            submission.app_description = form.app_description.data
            submission.app_category = form.app_category.data
            submission.app_version = form.app_version.data
            submission.app_website = form.app_website.data
            submission.app_download_url = form.app_download_url.data
            
            # Verification method and authentication
            submission.verification_method = form.verification_method.data
            submission.github_repo_url = form.github_repo_url.data
            submission.google_play_url = form.google_play_url.data
            submission.apple_store_url = form.apple_store_url.data
            submission.official_website_url = form.official_website_url.data
            
            # Developer information
            submission.developer_name = form.developer_name.data
            submission.developer_email = form.developer_email.data
            submission.developer_phone = form.developer_phone.data
            submission.developer_company = form.developer_company.data
            submission.developer_website = form.developer_website.data
            
            # Handle file uploads
            if form.app_logo.data:
                logo_path = save_uploaded_file(form.app_logo.data, 'app_logos')
                submission.app_logo = logo_path
            
            if form.app_screenshots.data:
                screenshots_path = save_uploaded_file(form.app_screenshots.data, 'app_screenshots')
                submission.set_screenshots_list([screenshots_path])
            
            if form.app_apk_file.data:
                apk_path = save_uploaded_file(form.app_apk_file.data, 'app_files')
                submission.app_apk_file = apk_path
            
            if form.app_documentation.data:
                doc_path = save_uploaded_file(form.app_documentation.data, 'app_documentation')
                submission.app_documentation = doc_path
            
            # App details
            features = [f.strip() for f in form.app_features.data.split('\n') if f.strip()]
            submission.set_features_list(features)
            submission.target_audience = form.target_audience.data
            submission.app_size = form.app_size.data
            submission.minimum_os_version = form.minimum_os_version.data
            
            if form.permissions_required.data:
                permissions = [p.strip() for p in form.permissions_required.data.split('\n') if p.strip()]
                submission.set_permissions_list(permissions)
            
            # Pricing
            submission.app_price = form.app_price.data
            submission.monetization_model = form.monetization_model.data
            
            # Legal
            submission.privacy_policy_url = form.privacy_policy_url.data
            submission.terms_of_service_url = form.terms_of_service_url.data
            submission.terms_accepted = form.terms_accepted.data
            
            submission.status = 'pending'
            
            db.session.add(submission)
            db.session.commit()
            
            flash('App submitted successfully! We will review your submission and get back to you within 3-5 business days.', 'success')
            return redirect(url_for('app_registration'))
            
        except Exception as e:
            db.session.rollback()
            flash(f'Error submitting app: {str(e)}', 'error')
    
    # Prepare categories for the template
    categories = ['Business', 'Communication', 'Education', 'Entertainment', 'Finance', 
                 'Health & Fitness', 'Lifestyle', 'Productivity', 'Shopping', 'Social', 
                 'Travel', 'Utilities', 'Games', 'News', 'Photography', 'Music', 'Sports',
                 'Weather', 'Books', 'Food & Drink', 'Medical', 'Navigation', 'Real Estate',
                 'Reference', 'Legal', 'Security', 'Public Services', 'Job', 'Other']
    
    return render_template('/app/app_registration_multistep.html', form=form, categories=categories)

@app.route('/download/app/<int:app_id>')
def download_app_file(app_id):
    """Handle app file downloads"""
    try:
        # Check if user is logged in
        if 'user_id' not in session and 'business_id' not in session:
            flash('Please log in to download files.', 'error')
            return redirect(url_for('user_login'))
        
        # First try to find in App table
        app = App.query.get(app_id)
        if app and hasattr(app, 'app_file_path') and app.app_file_path:
            file_path = app.app_file_path
            if os.path.exists(file_path):
                # Increment download count
                app.downloads = (app.downloads or 0) + 1
                db.session.commit()
                return send_file(file_path, as_attachment=True)
        
        # Then try AppSubmission table
        submission = AppSubmission.query.get(app_id)
        if submission and submission.app_apk_file:
            file_path = submission.app_apk_file
            if os.path.exists(file_path):
                return send_file(file_path, as_attachment=True)
        
        # If verification method is not upload, redirect to external link
        if submission:
            if submission.verification_method == 'github' and submission.github_repo_url:
                return redirect(submission.github_repo_url)
            elif submission.verification_method == 'store':
                if submission.google_play_url:
                    return redirect(submission.google_play_url)
                elif submission.apple_store_url:
                    return redirect(submission.apple_store_url)
            elif submission.verification_method == 'website' and submission.official_website_url:
                return redirect(submission.official_website_url)
        
        flash('File not found or download link unavailable.', 'error')
        return redirect(url_for('app_home'))
        
    except Exception as e:
        logging.error(f'Error downloading file: {str(e)}')
        flash(f'Error downloading file: {str(e)}', 'error')
        return redirect(url_for('app_home'))

@app.route('/subscriber/dashboard')
def subscriber_dashboard():
    """Subscriber dashboard showing app submissions and status"""
    if 'user_id' not in session and 'business_id' not in session:
        flash('Please log in to access the dashboard.', 'error')
        return redirect(url_for('user_login'))
    
    user_id = session.get('user_id')
    business_id = session.get('business_id')
    
    # Get user info
    user = None
    if user_id:
        user = User.query.get(user_id)
    elif business_id:
        user = Business.query.get(business_id)
    
    # Get app submissions for this user/business
    query = AppSubmission.query
    if user_id:
        query = query.filter_by(user_id=user_id)
    elif business_id:
        query = query.filter_by(business_id=business_id)
    
    submitted_apps = query.order_by(AppSubmission.submission_date.desc()).all()
    
    # Categorize apps by status
    approved_apps = [app for app in submitted_apps if app.status == 'approved']
    pending_apps = [app for app in submitted_apps if app.status == 'pending']
    
    # Calculate total downloads (this would need to be implemented if tracking downloads)
    total_downloads = sum(getattr(app, 'downloads', 0) for app in approved_apps)
    
    return render_template('user/subscriber_dashboard.html',
                         user=user,
                         submitted_apps=submitted_apps,
                         approved_apps=approved_apps,
                         pending_apps=pending_apps,
                         total_downloads=total_downloads)

@app.route('/matrimony/matrimony')
def matrimony():
    """Matrimony platform page"""
    # Get some sample profiles for display
    profiles = MatrimonyProfile.query.filter_by(profile_visible=True).limit(10).all()
    return render_template('/matrimony/matrimony.html', profiles=profiles)

@app.route('/matrimony/matrimony_register_step', methods=['GET', 'POST'])
@app.route('/matrimony/matrimony_register_step/<int:step>', methods=['GET', 'POST'])
def matrimony_register_step(step=1):
    """Multi-step matrimony registration page"""
    from forms import MatrimonyRegistrationForm
    form = MatrimonyRegistrationForm()
    
    # Ensure step is between 1 and 4
    step = max(1, min(6, step))
    
    if request.method == 'POST':
        action = request.form.get('action', 'next')
        
        if action == 'previous' and step > 1:
            return redirect(url_for('matrimony_register_step', step=step-1))
        elif action == 'next' and step < 6:
            # Store form data in session for multi-step
            if not session.get('matrimony_form_data'):
        session['matrimony_form_data'] = {}
            
            # Store current step data
            if step == 1:
                # User Basic Information
                session['matrimony_form_data'].update({
                    'business_id': session.get('business_id'),
                     'created_by': request.form.get('created_by'),
                    'full_name': request.form.get('full_name'),
                    'first_name': request.form.get('first_name'),
                    'last_name': request.form.get('last_name'),
                    'dob': request.form.get('dob'),
                    'age': request.form.get('age'),
                    'gender': request.form.get('gender'),
                    'marital_status':             request.form.get('marital_status'),
                    'religion': request.form.get('religion'),
                    'language': request.form.get('language'),
                    'relationship_interest': request.form.get('relationship_interest'),
               
                },)
                
            elif step == 2:
                # User Pysical Details
                session['matrimony_form_data'].update({
                    
                    'height': request.form.get('height'),
                    'weight': request.form.get('weight'),
                    'body_type': request.form.get('body_type'),
                    'complexion': request.form.get('complexion'),
                    'eye_color': request.form.get('eye_color'),
                    'hair_color': request.form.get('hair_color'),
                    'skin_tone': request.form.get('skin_tone'),
                    'physical_disability': request.form.get('physical_disability'),
                    'mental_disability': request.form.get('mental_disability'),
                    'blood_group': request.form.get('blood_group'),
            # User Family Details
                    'father_name': request.form.get('father_name'),
                    'mother_name': reqiest.form.get('mother_name'),
                    'brothers': request.form.get('brothers'),
                    'sisters': request.form.get('sisters'),
                    'family_type': request.form.get('family_type'),
                    'family_status': request.form.get('family_status'),
                    'family_values' = request.form.get('family_values'),
                    'ancestral_origin' = request.form.get('ancestral_origin')


                },)
                
            elif step == 3:
           # User Professional Details
session['matrimony_form_data'].update({

                    'education': request.form.get('education'),
                    'occupation': request.form.get('occupation'),
                    'annual_income': request.form.get('annual_income'),
                    'company_name': request.form.get('company_name'),
                    # About User
                    'about_yourself': request.form.get('about_yourself'),
                    # User Life Style
                    'hobbies': request.form.get('hobbies'),
                    'smoking': request.form.get('smoking'),
                    'drinking':   request.form.get('drinking'),
                    'food': request.form.get('food'),
             # User Horoscope Details
   'religion': request.form.get('religion'),
   'caste': request.form.get('caste'),
   'subcaste': request.form.get('subcaste'),
   'gothra': request.form.get('gothra'),
   'dosham': request.form.get('dosham'),
   'star': request.form.get('star'),
   'raasi': request.form.get('raasi'),
   'horoscope': request.form.get('horoscope'),
                    
             # User Membership Plan      
                    'membership_type': request.form.get('membership_type')
                
                  },)
                
            elif step == 4:
                
session['matrimony_form_data'].update({
 # User Location Details
                    'address': request.form.get('address'),
                    'city': request.form.get('city'),
                    'district':
request.form.get('district'),
                    'pincode': request.form.get('pincode'),
                    'state': request.form.get('state'),
                    'country': request.form.get('country'),
                    'nationality': request.form.get('nationality'),
                    'future_lives_in': request.form.get('future_lives_in'),
    # User Contact Information
    'email': request.form.get('email'),
    'mobile': request.form.get('mobile'),
    'phone': request.form.get('phone'),
    # Social Media
                'whatsapp': request.form.get('whatsapp'),
                'buddhistan': request.form.get('buddhistan'),
               'facebook': request.form.get('facebook'),
                'twitter': request.form.get('twitter'),
 'x': request.form.get('x'),
                'instagram': request.form.get('instagram'),
               'linkedin': request.form.get('linkedin'),
               'youtube': request.form.get('youtube'),
               'telegram': request.form.get('telegram'),
               'website': request.form.get('website'),

                        },)

            elif step == 5:
         # Partner Preferred Details (Optional)

                # Partner Basic Preferences
session['matrimony_form_data'].update({

    'created_by': request.form.get('created_by'),
                'partner_gender': request.form.get('partner_gender'),
                'partner_marital_status': request.form.get('partner_marital_status'),
                'partner_age_min': request.form.get('partner_age_min'),
                'partner_age_max': request.form.get('partner_age_max'),
    'relationship_interest': request.form.get('relationship_interest'),
     # Partner Professional Preferences
                'partner_education': request.form.get('partner_education'),
                'partner_occupation': request.form.get('partner_occupation'),
                'partner_annual_income': request.form.get('partner_annual_income'),
 # Partner Family Preferences
'partner_father_name': request.form.get('partner_father_name'),
'partner_mother_name': request.form.get('partner_mother_name'),
'partner_brothers': request.form.get('partner_brothers'),
'partner_sisters': request.form.get('partner_sisters'),
'partner_family_type': request.form.get('partner_family_type'),
'partner_family_status': request.form.get('partner_family_status'),
'partner_family_values': request.form.get('partner_family_values'),
'partner_ancestral_origin': request.form.get('partner_ancestral_origin'),
# Partner Religious Preferences
'partner_religion': request.form.get('partner_religion'),
'partner_language': request.form.get('partner_language'),
# Partner Life Style Preferences
'partner_hobbies': request.form.get('partner_hobbies'),
'partner_smoking': request.form.get('partner_smoking'),
'partner_drinking':   request.form.get('partner_drinking'),
'partner_food': request.form.get('partner_food'),
# Partner Location Preferences
'partner_address': request.form.get('partner_address'),
'partner_city': request.form.get('partner_city'),
'partner_district': request.form.get('partner_district'),
'partner_pincode': request.form.get('partner_pincode'),
'partner_state': request.form.get('partner_state'),
'partner_country': request  .form.get('partner_country'),
'partner_nationality': request.form.get('partner_nationality'),
'partner_future_lives_in': request.form.get('partner_future_lives_in'),
# Partner Membership Preferences
'partner_membership_type': request.form.get('partner_membership_type')
  
             },)

              elif step == 6:
 # User & Partner Documents and Verification
session['matrimony_form_data'].update({
   
    'id_proof': request.form.get('id_proof')
    'family_photo_proof': request.form.get('family_photo_proof')
    'address_proof': request.from.get('address_proof')
    'passport_proof': request.form.get('passport_proof')
    'education_proof': request.form.get('education_proof')
    'occupation_proof': request.form.get('occupation_proof')
    'income_proof': request.form.get('income_proof')
    'horoscope_proof': request.form.get('horoscope_proof')
    'marriage_proof': request.form.get('marriage_proof')
    'divorce_proof': request.form.get('divorce_proof')
    'children_proof': request.form.get('children_proof')
    'property_proof': request.form.get('property_proof')
    'medical_proof': request.form.get('medical_proof')
    'sexual_proof': request.form.get('sexual_proof')
    'mental_proof': request.form.get('mental_proof')
    'physical_proof': request.form.get('physical_proof')
    'criminal_proof': request.form.get('criminal_proof')
     'police_noc_proof': request.form.get('police_noc_proof')
     'caste_certificate_proof': request.form.get('caste_certificate_proof')
     'biometric_proof': request.form.get('biometric_proof')

             },)
    
            return redirect(url_for('matrimony_register_step', step=step+1))
        
        elif action == 'submit' and step == 6:
            # Process final submission
            form_data = session.get('matrimony_form_data', {})
            
            try:
          # Check if email already exists
                email = form_data.get('email')
                if email:
                    existing_profile = MatrimonyProfile.query.filter_by(email=email).first()
                    if existing_profile:
                        flash('Email already registered. Please use a different email.', 'error')
                        
                        return redirect(url_for('matrimony_register_step', step=1))
         # Check if mobile already exists
                mobile = form_data.get('mobile')
                if mobile:
                    existing_profile = MatrimonyProfile.query.filter_by(mobile=mobile).first()            if existing_profile:
                    flash('Mobile already registered. Please use a different mobile.', 'error')  
                    return redirect(url_for('matrimony_register_step', step=1)) 
                # Create new profile
                profile = MatrimonyProfile()
                
                # Basic Information
                profile.user_id = session.get('user_id')
                profile.business_id = session.get('business_id')
                profile.created_by = form_data.get('created_by', 'self', 'admin', '')
                profile.full_name = form_data.get('full_name')
                profile.first_name = form_data.get('first_name')
                profile.last_name = form_data.get('last_name')
                profile.date_of_birth = form_data.get('date_of_birth')
                profile.age = int(form_data.get('age', 15))
                profile.gender = form_data.get('gender')
                profile.marital_status = form_data.get('marital_status')
                profile.lives_in = form_data.get('lives_in')
                profile.resident_status = form_data.get('resident_status', 'Permanent', 'Temporary', '')
            profile.relationship_interest = form_data.get('relationship_interest', 'marriage', 'relationship', 'friendship', 'for party', 'open', 'dating', 'contract', 'livein', 'enjoyment', 'travel', 'work', 'family', 'sex for baby', 'volunteer', 'not specified')

                # Contact Information
                profile.email = email
                profile.mobile = mobile
                profile.phone = form_data.get('phone')
                # Social Media
                profile.whatsapp = form_data.get('whatsapp')
                profile.buddhistan = form_data.get('buddhistan')
                profile.facebook = form_data.get('facebook')
                profile.twitter = form_data.get('twitter')
                profile.x = form_data.get('x')
                profile.instagram = form_data.get('instagram')
                profile.linkedin = form_data.get('linkedin')
                profile.youtube = form_data.get('youtube')
                profile.telegram = form_data.get('telegram')
                profile.website = form_data.get('website')

                # Physical Details
                profile.height = form_data.get('height')
                profile.weight = form_data.get('weight')
                profile.body_type = form_data.get('body_type')
                profile.complexion = form_data.get('complexion')
                profile.eye_color = form_data.get('eye_color')
                profile.hair_color = form_data.get('hair_color')
                profile.skin_tone = form_data.get('skin_tone')
                profile.physical_disability = form_data.get('physical_disability')
                profile.mental_disability = form_data.get('mental_disability')
                profile.blood_group = form_data.get('blood_group')
                                
                # Famiy Details
                profile.father_name = form_data.get('father_name')
                profile.mother_name = form_data.get('mother_name')
                profile.brothers = form_data.get('brothers')
                profile.sisters = form_data.get('sisters')
                profile.family_type = form_data.get('family_type')
                profile.family_status = form_data.get('family_status')
                profile.family_values = form_data.get('family_values')
                profile.ancestral_origin = form_data.get('ancestral_origin')

                # Horoscope Details
                profile.religion = form_data.get('religion')
                profile.caste = form_data.get('caste')
                profile.subcaste = form_data.get('subcaste')
                profile.gothra = form_data.get('gothra')
                profile.dosham = form_data.get('dosham')
                profile.star = form_data.get('star')
                profile.raasi = form_data.get('raasi')
                profile.horoscope = form_data.get('horoscope')
                
                # Location
                profile.address = form_data.get('address')
                profile.city = form_data.get('city')
                profile.district = form_data.get('district')
                profile.pincode = form_data.get('pincode')
                profile.state = form_data.get('state')
                profile.country = form_data.get('country', 'Buddistan', 'India','')
                profile.nationality = form_data.get('nationality', 'Buddistan', 'Indian', '')
                profile.lives_in = form_data.get('lives_in', 'Buddistan', 'Indian', '')
                profile.resident_status = form_data.get('resident_status', 'Permanent', 'Temporary', 'Not Specified')
                profile.future_lives_in = form_data.get('future_lives_in')

            # Proffesional Education & Career
                profile.education = form_data.get('education')
                profile.occupation = form_data.get('occupation')
                profile.annual_income = form_data.get('annual_income')
                profile.company_name = form_data.get('company_name')
                
                # About and Hobbies
                profile.bio = form_data.get('about_yourself')

                # Life Style
                profile.hobbies = form_data.get('hobbies')
                profile.smoking = form_data.get('smoking','occasionally', 'no', 'not specified', '')
                profile.drinking = form_data.get('drinking', 'occasionally', 'no', 'not specified', '')
                profile.food = form_data.get('food', 'vegetarian', 'non-vegetarian', 'not specified', '')

         # Documents and Verification
                profile.id_proof = form_data.get('id_proof')
                profile.family_photo_proof = form_data.get('family_photo_proof')
                profile.address_proof = from_data.get('address_proof')
                profile.passport_proof = form_data.get('passport_proof')
                profile.education_proof = form_data.get('education_proof')
                profile.occupation_proof = form_data.get('occupation_proof')
                profile.income_proof = form_data.get('income_proof')
                profile.horoscope_proof = form_data.get('horoscope_proof')
                profile.marriage_proof = form_data.get('marriage_proof')
                profile.divorce_proof = form_data.get('divorce_proof')
                profile.children_proof = form_data.get('children_proof')
                profile.property_proof = form_data.get('property_proof')
                profile.medical_proof = form_data.get('medical_proof')
                profile.sexual_proof = form_data.get('sexual_proof')
                profile.mental_proof = form_data.get('mental_proof')
                profile.physical_proof = form_data.get('physical_proof')
                profile.criminal_proof = form_data.get('criminal_proof')
                 profile.police_noc_proof = form_data.get('police_noc_proof')
                profile.caste_certificate_proof = form_data.get('caste_certificate_proof')
                profile.biometric_proof = form_data.get('biometric_proof')

                # User Membership
                profile.membership_badge = form_data.get('membership_type', 'basic')
                profile.premium_member = profile.membership_badge in ['gold', 'platinum']
                # User Privace
                profile.privacy_settings = form_data.get('privacy_settings', 'public', 'private', 'friends', 'family', 'workplace', 'school', 'college', 'university', 'government', 'military', 'army', 'navy', 'airforce', 'police', 'fire', 'ambulance', 'hospital', 'doctor', 'nurse', 'pharmacist', 'pharmacy', 'lawyer', 'judge', 'magistrate', 'prosecutor', 'defender', 'journalist', 'reporter', 'editor', 'writer', 'author', 'poet', 'painter', 'singer', 'dancer', 'actor', 'actress', 'model', 'musician', 'sportsman', 'sportswoman', 'coach', 'trainer', 'teacher', 'student', 'researcher', 'developer', 'engineer', 'scientist', 'researcher', 'investor', 'entrepreneur', 'businessman', 'businesswoman', 'farmer', 'worker', 'laborer', 'maid', 'cook', 'driver', 'cleaner', 'gardener', 'painter', 'plumber', 'electrician', 'mechanic', 'welder', 'carpenter', 'joiner', 'tailor', 'barber', 'beautician', 'hairdresser', 'cosmetologist', 'makeup_artist', 'nail_artist', 'massage_therapist', 'yoga_teacher', 'fitness_trainer', 'dietician', 'nutritionist', 'psychologist', 'leader', 'manager', 'supervisor', 'employee', 'assistant', 'secretary', 'receptionist', 'guard', 'security', 'dilivery', 'courier', 'captan', 'pilot', 'crew', 'passenger', 'traveler', 'tourist', 'host' )

        # Partner Preferences Details
            # Partner Basic Preferences
                profile.partner_age_min = int(form_data.get('partner_age_min', 18))
                profile.partner_age_max = int(form_data.get('partner_age_max', 35))
                profile.partner_gender = form_data.get('partner_gender'),
                profile.partner_marital_status = form_data.get('partner_marital_status'),           
            profile.partner_relationship_interest = form_data.get('partner_relationship_interest', 'marriage', 'relationship', 'friendship', 'for party', 'open', 'dating', 'contract', 'livein', 'enjoyment', 'travel', 'work', 'family', 'sex for baby', 'volunteer', 'not specified')

                # Religious Preferences
                profile.partner_religion = form_data.get('partner_religion'),
                profile.partner_language = form_data.get('partner_language'),

                # Professional Preferences
                profile.partner_education = form_data.get('partner_education'),
                 profile.partner_occupation = form_data.get('partner_occupation'),
                profile.partner_anual_income = form_data.get('partner_anual_income'),

                 # Family Preferences
                profile.partner_father_name = form_data.get('partner_father_name')
                profile.partner_mother_name = form_data.get('partner_mother_name')
                profile.partner_brothers = form_data.get('partner_brothers')
                profile.partner_sisters = form_data.get('partner_sisters')
                profile.partner_family_type = form_data.get('partner_family_type')
                profile.partner_family_status = form_data.get('partner_family_status')
                profile.partner_family_values = form_data.get('partner_family_values')
                profile.partner_ancestral_origin = form_data.get('partner_ancestral_origin')

                # Life Style Preferences
                profile.partner_hobbies = form_data.get('partner_hobbies')
                profile.partner_smoking = form_data.get('partner_smoking','occasionally', 'no', 'not specified', '')
                profile.partner_drinking = form_data.get('partner_drinking', 'occasionally', 'no', 'not specified', '')
                profile.partner_food = form_data.get('partner_food', 'vegetarian', 'non-vegetarian', 'not specified', '')

                # Location Preferences
                profile.partner_address = form_data.get('partner_address')
                profile.partner_city = form_data.get('partner_city')
                profile.partner_district = form_data.get('partner_district')
                profile.partner_pincode = form_data.get('partner_pincode')
                profile.partner_state = form_data.get('partner_state')
                profile.partner_country = form_data.get('partner_country', 'Buddistan', 'India','')
                profile.partner_nationality = form_data.get('partner_nationality', 'Buddistan', 'Indian', '')
                profile.lives_in = form_data.get('partner_lives_in', 'Buddistan', 'Indian', '')
                profile.partner_resident_status = form_data.get('partner_resident_status', 'Permanent', 'Temporary', 'Not Specifc')
                profile.partner_future_lives_in = form_data.get('partner_future_lives_in')

                # Membership Preferences
                profile.partner_membership_type = form_data.get('partner_membership_type')
                profile.partner_premium_member = profile.partner_membership_type in ['gold', 'platinum']                
                # Handle profile images
                if 'profile_images' in request.files:
                    files = request.files.getlist('profile_images')
                    uploaded_images = []
                    
                    for file in files[:5]:  # Maximum 5 images
                        if file and file.filename:
                            filename = secure_filename(file.filename)
                            if filename:
                                import uuid
                                unique_filename = str(uuid.uuid4()) + '_' + filename
                                file_path = os.path.join(app.config['UPLOAD_FOLDER'], 'matrimony', unique_filename)
                                
                                os.makedirs(os.path.dirname(file_path), exist_ok=True)
                                file.save(file_path)
                                uploaded_images.append(f'matrimony/{unique_filename}')
                    
                    if uploaded_images:
                        profile.profile_images = json.dumps(uploaded_images)
                        profile.profile_photo = uploaded_images[0]
                        profile.family_photo = uploaded_images[1] if len(uploaded_images) > 1 else None 
                
                # Set defaults
                profile.profile_visible = True
                profile.is_verified = False
                profile.profile_views = 0
                profile.followers_count = 0
                profile.following_count = 0
                profile.shares_count = 0
                profile.created_at = datetime.utcnow()
                
                # Check photo blur for basic members
                if profile.membership_badge == 'basic':
                    profile.check_photo_blur_status()
                
                from werkzeug.security import generate_password_hash
                profile.password_hash = generate_password_hash('password123')
                
                db.session.add(profile)
                db.session.commit()
                
                # Clear form data from session
                session.pop('matrimony_form_data', None)
                
                flash('Registration successful! Your profile is now active.', 'success')
                return redirect(url_for('matrimony_profile', profile_id=profile.id))
                
            except Exception as e:
                db.session.rollback()
                flash(f'Registration failed: {str(e)}', 'error')
                return redirect(url_for('matrimony_register_step', step=step))
    
    # Pre-populate form with session data
    form_data = session.get('matrimony_form_data', {})
    
    return render_template('/matrimony/matrimony_register_step.html', form=form, step=step, form_data=form_data)

@app.route('/matrimony/matrimony_profile/<int:profile_id>')
def matrimony_profile(profile_id):
    """View matrimony profile"""
    profile = MatrimonyProfile.query.get_or_404(profile_id)
    
    # Increment profile views
    profile.profile_views += 1
    db.session.commit()
    
    return render_template('/matrimony/matrimony_profile.html', profile=profile)

@app.route('/matrimony/matrimony_profiles')
def matrimony_profiles():
    """Browse all matrimony profiles"""
    page = request.args.get('page', 1, type=int)
    per_page = 12
    
    profiles = MatrimonyProfile.query.filter_by(profile_visible=True).paginate(
        page=page, per_page=per_page, error_out=False
    )
    
    return render_template('/matrimony/matrimony_profiles.html', profiles=profiles)

@app.route('/matrimony/matrimony/interact/<int:profile_id>/<action>')
def matrimony_interact(profile_id, action):
    """Handle matrimony interactions (like, dislike, follow, share)"""
    profile = MatrimonyProfile.query.get_or_404(profile_id)
    
    if action == 'like':
        flash('Interest sent!', 'success')
    elif action == 'dislike':
        flash('Profile noted.', 'info')
    elif action == 'follow':
        # Increment followers count
        profile.followers_count += 1
        db.session.commit()
        flash('You are now following this profile!', 'success')
    elif action == 'share':
        # Increment shares count
        profile.shares_count += 1
        db.session.commit()
        flash('Profile shared successfully!', 'success')
    
    return redirect(request.referrer or url_for('matrimony_profiles'))

@app.route('/matrimony/matrimony/share/<int:profile_id>/<platform>')
def matrimony_share(profile_id, platform):
    """Handle profile sharing to different platforms"""
    profile = MatrimonyProfile.query.get_or_404(profile_id)
    
    # Increment shares count
    profile.shares_count += 1
    db.session.commit()
    
    profile_url = url_for('matrimony_profile', profile_id=profile_id, _external=True)
    share_text = f"Check out {profile.full_name}'s profile on our matrimony platform!"
    
    if platform == 'facebook':
        share_url = f"https://www.facebook.com/sharer/sharer.php?u={profile_url}"
    elif platform == 'whatsapp':
        share_url = f"https://wa.me/?text={share_text} {profile_url}"
    elif platform == 'buddhistan':
        # Custom platform sharing
        share_url = f"https://buddhistan.com/share?url={profile_url}&text={share_text}"
    else:
        flash('Invalid sharing platform', 'error')
        return redirect(request.referrer or url_for('matrimony_profiles'))
    
    return redirect(share_url)

@app.route('/user/all_user')
def all_user():
    """Display all active subscribers/user with filtering and pagination"""
    # Get filter parameters
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 12, type=int)
    plan_filter = request.args.get('plan', '')
    gender_filter = request.args.get('gender', '')
    status_filter = request.args.get('status', '')
    view_mode = request.args.get('view', 'grid', 'list')
    
    # Build query
    query = User.query
    
    # Apply filters
    if plan_filter:
        query = query.filter(User.user_type == plan_filter)
    if gender_filter:
        query = query.filter(User.gender == gender_filter)
    if status_filter == 'online':
        query = query.filter(User.is_online == True)
    elif status_filter == 'verified':
        query = query.filter(User.verification_status == 'verified')
    
    # Get paginated results
    users_pagination = query.paginate(
        page=page, per_page=per_page, error_out=False
    )
    users = users_pagination.items
    
    # Get statistics
    total_users = User.query.count()
    active_users = User.query.filter_by(is_online=True).count()
    verified_users = User.query.filter_by(verification_status='verified').count()
    male_users = User.query.filter_by(gender='male').count()
    female_users = User.query.filter_by(gender='female').count()
    
    return render_template('/user/all_user.html', 
                         users=users,
                         pagination=users_pagination,
                         total_users=total_users,
                         active_users=active_users,
                         verified_users=verified_users,
                         male_users=male_users,
                         female_users=female_users,
                         current_filters={
                             'plan': plan_filter,
                             'gender': gender_filter,
                             'status': status_filter,
                             'per_page': per_page,
                             'view': view_mode
                         },)

@app.route('/service/all_services')
def all_services():
    """Display all available services with filtering and search"""
    # Get filter parameters
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 12, type=int)
    service_filter = request.args.get('service', '')
    category_filter = request.args.get('category', '')
    search_query = request.args.get('search', '')
    view_mode = request.args.get('view', 'grid', 'list')
    
    # Service categories with data
    services_data = [
        {
            'id': 'blog',
            'name': 'Blog',
            'icon': 'fas fa-blog',
            'description': 'Create and manage your blog posts, articles, and content marketing',
            'category': 'content',
            'features': ['Rich Text Editor', 'SEO Optimization', 'Comments System', 'Social Sharing'],
            'count': 45,
            'active': True
        },
        {
            'id': 'product',
            'name': 'Product',
            'icon': 'fas fa-box',
            'description': 'Manage your product catalog, inventory, and sales',
            'category': 'ecommerce',
            'features': ['Inventory Management', 'Price Controls', 'Photo Gallery', 'CSV Import/Export'],
            'count': 128,
            'active': True
        },
        {
            'id': 'business',
            'name': 'Business',
            'icon': 'fas fa-building',
            'description': 'Register and manage your business profile and services',
            'category': 'business',
            'features': ['Business Verification', 'Profile Management', 'Document Upload', 'Analytics'],
            'count': 67,
            'active': True
        },
        {
            'id': 'app',
            'name': 'App',
            'icon': 'fas fa-mobile-alt',
            'description': 'Showcase and distribute your mobile applications',
            'category': 'technology',
            'features': ['App Store', 'Version Control', 'User Reviews', 'Download Analytics'],
            'count': 89,
            'active': True
        },
        {
            'id': 'matrimony',
            'name': 'Matrimony',
            'icon': 'fas fa-heart',
            'description': 'Find your perfect life partner through our matrimony platform',
            'category': 'social',
            'features': ['Profile Matching', 'Photo Gallery', 'Privacy Controls', 'Premium Memberships'],
            'count': 234,
            'active': True
        },
        {
            'id': 'delivery',
            'name': 'Delivery',
            'icon': 'fas fa-shipping-fast',
            'description': 'On-demand delivery services for your business',
            'category': 'logistics',
            'features': ['Real-time Tracking', 'Partner Network', 'Route Optimization', 'Payment Integration'],
            'count': 156,
            'active': True
        },
        {
            'id': 'bank',
            'name': 'Bank',
            'icon': 'fas fa-university',
            'description': 'Banking services and financial institution partnerships',
            'category': 'finance',
            'features': ['Account Management', 'Transaction History', 'Digital Payments', 'Security'],
            'count': 78,
            'active': True
        },
        {
            'id': 'finance',
            'name': 'Finance',
            'icon': 'fas fa-dollar-sign',
            'description': 'Personal and business financial management tools',
            'category': 'finance',
            'features': ['Budget Planning', 'Investment Tracking', 'Loan Calculator', 'Tax Management'],
            'count': 92,
            'active': True
        },
        {
            'id': 'sharemarket',
            'name': 'Share Market',
            'icon': 'fas fa-chart-line',
            'description': 'Stock market trading and investment platform',
            'category': 'finance',
            'features': ['Live Market Data', 'Portfolio Management', 'Trading Tools', 'Market Analysis'],
            'count': 145,
            'active': True
        },
        {
            'id': 'education',
            'name': 'Education',
            'icon': 'fas fa-graduation-cap',
            'description': 'Online learning and educational content platform',
            'category': 'education',
            'features': ['Course Management', 'Video Lectures', 'Assignments', 'Certificates'],
            'count': 203,
            'active': True
        },
        {
            'id': 'politics',
            'name': 'Politics',
            'icon': 'fas fa-flag',
            'description': 'Political news, campaigns, and civic engagement',
            'category': 'news',
            'features': ['News Updates', 'Campaign Management', 'Voting Information', 'Political Analysis'],
            'count': 56,
            'active': True
        },
        {
            'id': 'job',
            'name': 'Job',
            'icon': 'fas fa-briefcase',
            'description': 'Job search, career development, and professional networking',
            'category': 'professional',
            'features': ['Job Listings', 'Resume Builder', 'Skill Assessment', 'Career Guidance'],
            'count': 187,
            'active': True
        },
        {
            'id': 'console',
            'name': 'Console',
            'icon': 'fas fa-code',
            'description': 'code editor, code lerning, auto coding, code search, codeing development, and professional coding',
            'category': 'programming',
            'features': ['Code Editing', 'Webpage Builder', 'Skill Assessment', 'Career Guidance' 'Agent Extaintion' 'Code Testing' 'Code Preview',
            'count': 287,
            'active': True
        },
    ]
    
    # Apply filters
    filtered_services = services_data
    if category_filter:
        filtered_services = [s for s in filtered_services if s['category'] == category_filter]
    if search_query:
        filtered_services = [s for s in filtered_services if 
                           search_query.lower() in s['name'].lower() or 
                           search_query.lower() in s['description'].lower()]

    # Get services for filter dropdown
    services = list(set(s['name'] for s in services_data)) 
    services.sort()
    # Get categories for filter dropdown
    categories = list(set(s['category'] for s in services_data))
    categories.sort()
    
    # Statistics
    total_services = len(services_data)
    active_services = len([s for s in services_data if s['active']])
    total_users_count = sum(s['count'] for s in services_data)
    
    return render_template('/service/all_services.html',
                         services=filtered_services,
categories=categories,
                         total_services=total_services,
                         active_services=active_services,
                         total_users_count=total_users_count,
                         category_filter=category_filter,
search_query=search_query,
view_mode=view_mode)

# Template Viewer Route
@app.route('/console/template/view/<path:template_name>')
def view_template(template_name):
    """View template files as sample templates"""
    try:
        import os
        template_path = os.path.join('templates', template_name)
        
        # Security check - only allow files within templates directory
        if not os.path.exists(template_path) or '..' in template_name:
            flash('Template not found.', 'error')
            return redirect(url_for('index'))
        
        # Read the template file content
        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Create an advanced HTML page with split-screen capabilities
        html_content = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Advanced Template Viewer - {template_name}</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
            <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
            <link href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-tomorrow.min.css" rel="stylesheet">
            <link href="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/codemirror.min.css" rel="stylesheet">
            <link href="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/theme/monokai.min.css" rel="stylesheet">
            <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-core.min.js"></script>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/plugins/autoloader/prism-autoloader.min.js"></script>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/codemirror.min.js"></script>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/mode/xml/xml.min.js"></script>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/mode/javascript/javascript.min.js"></script>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/mode/css/css.min.js"></script>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/mode/htmlmixed/htmlmixed.min.js"></script>
            <style>
                body, html {{
                    height: 100vh;
                    overflow: hidden;
                },}
                
                .main-container {{
                    height: 100vh;
                    display: flex;
                    flex-direction: column;
                },}
                
                .fixed-outer-frame {{
                    height: calc(100vh - 120px);
                    border: 2px solid #343a40;
                    background: #f8f9fa;
                    position: relative;
                    overflow: hidden;
                },}
                
                .screen-viewport {{
                    height: 100%;
                    overflow: auto;
                    padding: 10px;
                },}
                
                .screen-controls {{
                    background: #f8f9fa;
                    padding: 10px;
                    border-bottom: 1px solid #dee2e6;
                    flex-shrink: 0;
                },}
                
                .screen-part {{
                    border: 1px solid #dee2e6;
                    min-height: 600px;
                    position: relative;
                    resize: both;
                    overflow: hidden;
                    margin-bottom: 10px;
                },}
                
                .screen-part-controls {{
                    background: #343a40;
                    color: white;
                    padding: 8px;
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    cursor: move;
                    flex-shrink: 0;
                },}
                
                .screen-part-content {{
                    height: calc(100% - 45px);
                    overflow: auto;
                },}
                
                .code-view pre {{
                    margin: 0;
                    height: 100%;
                    overflow: auto;
                    background: #2d3748;
                    color: #e2e8f0;
                    padding: 15px;
                    font-size: var(--font-size, 14px);
                },}
                
                .frontend-view {{
                    background: white;
                    height: 100%;
                    border: none;
                    width: 100%;
                    transform: scale(var(--zoom-level, 1));
                    transform-origin: top left;
                },}
                
                .editor-view {{
                    height: 100%;
                },}
                
                .CodeMirror {{
                    height: 100% !important;
                    font-size: var(--font-size, 14px) !important;
                },}
                
                .moveable-toolbar {{
                    position: fixed;
                    top: 70px;
                    right: 20px;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    border-radius: 8px;
                    padding: 8px;
                    box-shadow: 0 4px 20px rgba(0,0,0,0.3);
                    z-index: 1000;
                    cursor: move;
                    user-select: none;
                    width: auto;
                },}
                
                .toolbar-horizontal {{
                    width: auto;
                    max-width: 90vw;
                },}
                
                .toolbar-vertical-left,
                .toolbar-vertical-right {{
                    width: auto;
                    max-height: 80vh;
                },}
                
                .toolbar-handle {{
                    background: rgba(255,255,255,0.2);
                    padding: 3px;
                    margin: -8px -8px 5px -8px;
                    border-radius: 8px 8px 0 0;
                    text-align: center;
                    color: white;
                    font-weight: bold;
                    cursor: move;
                    font-size: 11px;
                },}
                
                .toolbar-grid {{
                    display: flex;
                    gap: 5px;
                    flex-wrap: nowrap;
                },}
                
                .toolbar-horizontal .toolbar-grid {{
                    flex-direction: row;
                },}
                
                .toolbar-vertical-left .toolbar-grid,
                .toolbar-vertical-right .toolbar-grid {{
                    flex-direction: column;
                },}
                
                .tool-box {{
                    width: 32px;
                    height: 32px;
                    background: rgba(255,255,255,0.9);
                    border-radius: 6px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    cursor: pointer;
                    transition: all 0.3s ease;
                    position: relative;
                    flex-shrink: 0;
                },}
                
                .tool-box:hover {{
                    background: white;
                    transform: scale(1.05);
                    box-shadow: 0 2px 8px rgba(0,0,0,0.2);
                },}
                
                .tool-tooltip {{
                    position: absolute;
                    top: -50px;
                    left: 50%;
                    transform: translateX(-50%);
                    background: #333;
                    color: white;
                    padding: 4px 6px;
                    border-radius: 4px;
                    font-size: 10px;
                    white-space: nowrap;
                    opacity: 0;
                    visibility: hidden;
                    transition: all 0.3s ease;
                    z-index: 1001;
                    max-width: 120px;
                    text-align: center;
                },}
                
                .tool-tooltip::after {{
                    content: '';
                    position: absolute;
                    top: 100%;
                    left: 50%;
                    transform: translateX(-50%);
                    border-left: 5px solid transparent;
                    border-right: 5px solid transparent;
                    border-top: 5px solid #333;
                },}
                
                .tool-box:hover .tool-tooltip {{
                    opacity: 1;
                    visibility: visible;
                },}
                
                .zoom-controls {{
                    display: flex;
                    align-items: center;
                    gap: 5px;
                    margin: 10px 0;
                },}
                
                .zoom-slider {{
                    width: 100px;
                },}
                
                .orientation-controls {{
                    display: flex;
                    gap: 5px;
                    margin-top: 10px;
                },}
                
                .btn-group-sm .btn {{
                    padding: 4px 8px;
                    font-size: 12px;
                },}
                
                .active-mode {{
                    background-color: #0d6efd !important;
                    border-color: #0d6efd !important;
                },}
                
                .size-controls {{
                    display: flex;
                    gap: 5px;
                    align-items: center;
                },}
                
                .size-btn {{
                    background: #495057;
                    border: 1px solid #6c757d;
                    color: white;
                    padding: 2px 6px;
                    font-size: 10px;
                    cursor: pointer;
                    border-radius: 2px;
                },}
                
                .size-btn:hover {{
                    background: #6c757d;
                },}
                
                .connection-indicator {{
                    position: absolute;
                    top: 50%;
                    right: -10px;
                    transform: translateY(-50%);
                    width: 20px;
                    height: 20px;
                    background: #28a745;
                    border-radius: 50%;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    color: white;
                    font-size: 10px;
                    z-index: 10;
                },}
                
                .connected {{
                    animation: pulse 2s infinite;
                },}
                
                @keyframes pulse {{
                    0% {{ opacity: 1; }}
                    50% {{ opacity: 0.5; }}
                    100% {{ opacity: 1; }}
                },}
                
                .toolbar-horizontal {{
                    top: auto;
                    bottom: 20px;
                    left: 50%;
                    transform: translateX(-50%);
                    right: auto;
                    width: 80%;
                    max-width: 800px;
                },}
                
                .toolbar-vertical-left {{
                    left: 20px;
                    right: auto;
                },}
                
                .toolbar-vertical-right {{
                    right: 20px;
                    left: auto;
                },}
            </style>
        </head>
        <body class="bg-light">
            <div class="main-container">
                <nav class="navbar navbar-dark bg-primary flex-shrink-0">
                    <div class="container-fluid">
                        <a class="navbar-brand" href="{url_for('index')}">
                            <i class="fas fa-mobile-alt me-2"></i>Mobile Shop - Advanced Template Viewer
                        </a>
                        <div class="d-flex">
                            <span class="navbar-text me-3">
                                <i class="fas fa-file-code me-1"></i>{template_name}
                            </span>
                            <a href="{url_for('index')}" class="btn btn-outline-light btn-sm">
                                <i class="fas fa-home me-1"></i>Home
                            </a>
                        </div>
                    </div>
                </nav>
            
            <!-- Screen Layout Controls -->
            <div class="screen-controls">
                <div class="container-fluid">
                    <div class="row align-items-center">
                        <div class="col-md-6">
                            <label class="form-label me-3"><strong>Screen Layout:</strong></label>
                            <div class="btn-group" role="group">
                                <input type="radio" class="btn-check" name="screenLayout" id="single" value="single" checked>
                                <label class="btn btn-outline-primary btn-sm" for="single">
                                    <i class="fas fa-square me-1"></i>Single
                                </label>
                                
                                <input type="radio" class="btn-check" name="screenLayout" id="double" value="double">
                                <label class="btn btn-outline-primary btn-sm" for="double">
                                    <i class="fas fa-columns me-1"></i>Double
                                </label>
                                
                                <input type="radio" class="btn-check" name="screenLayout" id="triple" value="triple">
                                <label class="btn btn-outline-primary btn-sm" for="triple">
                                    <i class="fas fa-th me-1"></i>Triple
                                </label>
                            </div>
                        </div>
                        <div class="col-md-6 text-end">
                            <small class="text-muted">
                                <i class="fas fa-info-circle me-1"></i>
                                Use the floating toolbar for all controls
                            </small>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Fixed Outer Frame -->
            <div class="fixed-outer-frame">
                <div class="screen-viewport">
                    <div class="row" id="screenContainer">
                        <!-- Screen Part 1 -->
                        <div class="col-12" id="screenPart1" data-part="1">
                        <div class="screen-part">
                            <div class="screen-part-controls">
                                <div class="d-flex align-items-center">
                                    <span class="badge bg-light text-dark me-2">Panel 1</span>
                                    <select class="form-select form-select-sm me-2" style="width: auto; font-size: 11px;" onchange="connectPanel(1, this.value)">
                                        <option value="">Connect to...</option>
                                        <option value="2">Panel 2</option>
                                        <option value="3">Panel 3</option>
                                        <option value="all">All Panels</option>
                                    </select>
                                </div>
                                <div class="btn-group btn-group-sm" role="group">
                                    <button type="button" class="btn btn-light active-mode" onclick="setMode(1, 'code')">
                                        <i class="fas fa-code me-1"></i>Code
                                    </button>
                                    <button type="button" class="btn btn-light" onclick="setMode(1, 'frontend')">
                                        <i class="fas fa-eye me-1"></i>Preview
                                    </button>
                                    <button type="button" class="btn btn-light" onclick="setMode(1, 'editor')">
                                        <i class="fas fa-edit me-1"></i>Editor
                                    </button>
                                    <button type="button" class="btn btn-success" onclick="downloadTemplate(1)">
                                        <i class="fas fa-download me-1"></i>Download
                                    </button>
                                </div>
                                <div class="connection-indicator d-none" id="indicator1">
                                    <i class="fas fa-link"></i>
                                </div>
                            </div>
                            <div class="screen-part-content">
                                <div class="code-view" id="codeView1">
                                    <pre><code class="language-html">{content.replace('<', '&lt;').replace('>', '&gt;')}</code></pre>
                                </div>
                                <div class="frontend-view d-none" id="frontendView1">
                                    <iframe srcdoc="{content.replace('"', '&quot;')}" class="frontend-view"></iframe>
                                </div>
                                <div class="editor-view d-none" id="editorView1">
                                    <textarea id="editor1">{content}</textarea>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Screen Part 2 (Hidden by default) -->
                    <div class="col-6 d-none" id="screenPart2" data-part="2">
                        <div class="screen-part">
                            <div class="screen-part-controls">
                                <div class="d-flex align-items-center">
                                    <span class="badge bg-light text-dark me-2">Panel 2</span>
                                    <select class="form-select form-select-sm me-2" style="width: auto; font-size: 11px;" onchange="connectPanel(2, this.value)">
                                        <option value="">Connect to...</option>
                                        <option value="1">Panel 1</option>
                                        <option value="3">Panel 3</option>
                                        <option value="all">All Panels</option>
                                    </select>
                                </div>
                                <div class="btn-group btn-group-sm" role="group">
                                    <button type="button" class="btn btn-light active-mode" onclick="setMode(2, 'code')">
                                        <i class="fas fa-code me-1"></i>Code
                                    </button>
                                    <button type="button" class="btn btn-light" onclick="setMode(2, 'frontend')">
                                        <i class="fas fa-eye me-1"></i>Preview
                                    </button>
                                    <button type="button" class="btn btn-light" onclick="setMode(2, 'editor')">
                                        <i class="fas fa-edit me-1"></i>Editor
                                    </button>
                                    <button type="button" class="btn btn-success" onclick="downloadTemplate(2)">
                                        <i class="fas fa-download me-1"></i>Download
                                    </button>
                                </div>
                                <div class="connection-indicator d-none" id="indicator2">
                                    <i class="fas fa-link"></i>
                                </div>
                            </div>
                            <div class="screen-part-content">
                                <div class="code-view" id="codeView2">
                                    <pre><code class="language-html">{content.replace('<', '&lt;').replace('>', '&gt;')}</code></pre>
                                </div>
                                <div class="frontend-view d-none" id="frontendView2">
                                    <iframe srcdoc="{content.replace('"', '&quot;')}" class="frontend-view"></iframe>
                                </div>
                                <div class="editor-view d-none" id="editorView2">
                                    <textarea id="editor2">{content}</textarea>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Screen Part 3 (Hidden by default) -->
                    <div class="col-4 d-none" id="screenPart3" data-part="3">
                        <div class="screen-part">
                            <div class="screen-part-controls">
                                <div class="d-flex align-items-center">
                                    <span class="badge bg-light text-dark me-2">Panel 3</span>
                                    <select class="form-select form-select-sm me-2" style="width: auto; font-size: 11px;" onchange="connectPanel(3, this.value)">
                                        <option value="">Connect to...</option>
                                        <option value="1">Panel 1</option>
                                        <option value="2">Panel 2</option>
                                        <option value="all">All Panels</option>
                                    </select>
                                </div>
                                <div class="btn-group btn-group-sm" role="group">
                                    <button type="button" class="btn btn-light active-mode" onclick="setMode(3, 'code')">
                                        <i class="fas fa-code me-1"></i>Code
                                    </button>
                                    <button type="button" class="btn btn-light" onclick="setMode(3, 'frontend')">
                                        <i class="fas fa-eye me-1"></i>Preview
                                    </button>
                                    <button type="button" class="btn btn-light" onclick="setMode(3, 'editor')">
                                        <i class="fas fa-edit me-1"></i>Editor
                                    </button>
                                    <button type="button" class="btn btn-success" onclick="downloadTemplate(3)">
                                        <i class="fas fa-download me-1"></i>Download
                                    </button>
                                </div>
                                <div class="connection-indicator d-none" id="indicator3">
                                    <i class="fas fa-link"></i>
                                </div>
                            </div>
                            <div class="screen-part-content">
                                <div class="code-view" id="codeView3">
                                    <pre><code class="language-html">{content.replace('<', '&lt;').replace('>', '&gt;')}</code></pre>
                                </div>
                                <div class="frontend-view d-none" id="frontendView3">
                                    <iframe srcdoc="{content.replace('"', '&quot;')}" class="frontend-view"></iframe>
                                </div>
                                <div class="editor-view d-none" id="editorView3">
                                    <textarea id="editor3">{content}</textarea>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- Moveable Toolbar -->
            <div class="moveable-toolbar" id="moveableToolbar">
                <div class="toolbar-handle">
                    <i class="fas fa-grip-horizontal"></i> Tools
                </div>
                
                <div class="toolbar-grid" id="toolbarGrid">
                    <!-- Layout Tools -->
                    <div class="tool-box" onclick="setScreenLayout('single')">
                        <i class="fas fa-square"></i>
                        <div class="tool-tooltip">Single View</div>
                    </div>
                    
                    <div class="tool-box" onclick="setScreenLayout('double')">
                        <i class="fas fa-columns"></i>
                        <div class="tool-tooltip">Double View</div>
                    </div>
                    
                    <div class="tool-box" onclick="setScreenLayout('triple')">
                        <i class="fas fa-th"></i>
                        <div class="tool-tooltip">Triple View</div>
                    </div>
                    
                    <!-- Connection Tool -->
                    <div class="tool-box" onclick="autoConnectPanels()">
                        <i class="fas fa-link"></i>
                        <div class="tool-tooltip">Auto Connect</div>
                    </div>
                    
                    <!-- Reset Size Tool -->
                    <div class="tool-box" onclick="resetAllSizes()">
                        <i class="fas fa-expand-arrows-alt"></i>
                        <div class="tool-tooltip">Reset Sizes</div>
                    </div>
                    
                    <!-- Font Size Tools (Combined Zoom) -->
                    <div class="tool-box" onclick="zoomIn()">
                        <i class="fas fa-plus"></i>
                        <div class="tool-tooltip">Zoom In (+)</div>
                    </div>
                    
                    <div class="tool-box" onclick="zoomOut()">
                        <i class="fas fa-minus"></i>
                        <div class="tool-tooltip">Zoom Out (-)</div>
                    </div>
                    
                    <!-- Download Tool -->
                    <div class="tool-box" onclick="downloadCurrentTemplate()">
                        <i class="fas fa-download"></i>
                        <div class="tool-tooltip">Download</div>
                    </div>
                    
                    <!-- Toolbar Position Tools -->
                    <div class="tool-box" onclick="moveToolbar('top')">
                        <i class="fas fa-arrow-up"></i>
                        <div class="tool-tooltip">Move Top</div>
                    </div>
                    
                    <div class="tool-box" onclick="moveToolbar('bottom')">
                        <i class="fas fa-arrow-down"></i>
                        <div class="tool-tooltip">Move Bottom</div>
                    </div>
                    
                    <div class="tool-box" onclick="moveToolbar('left')">
                        <i class="fas fa-arrow-left"></i>
                        <div class="tool-tooltip">Move Left</div>
                    </div>
                    
                    <div class="tool-box" onclick="moveToolbar('right')">
                        <i class="fas fa-arrow-right"></i>
                        <div class="tool-tooltip">Move Right</div>
                    </div>
                </div>
            </div>
            
            </div> <!-- End main-container -->
            
            <script>
                let editors = {{}};
                let connections = {{}};
                let panelSizes = {{1: 'normal', 2: 'normal', 3: 'normal'}};
                let currentFontSize = 14;
                let isDragging = false;
                let dragOffset = {{ x: 0, y: 0 }};
                const originalContent = `{content}`;
                
                // Initialize CodeMirror editors
                function initializeEditors() {{
                    for (let i = 1; i <= 3; i++) {{
                        if (document.getElementById(`editor${{i}}`)) {{
                            editors[i] = CodeMirror.fromTextArea(document.getElementById(`editor${{i}}`), {{
                                mode: 'htmlmixed',
                                theme: 'monokai',
                                lineNumbers: true,
                                autoCloseTags: true,
                                foldGutter: true,
                                gutters: ['CodeMirror-linenumbers', 'CodeMirror-foldgutter']
                            },});
                            
                            // Add change listener for real-time updates
                            editors[i].on('change', function() {{
                                updateConnectedPanels(i);
                            },});
                        },}
                    },}
                },}
                
                // Adjust panel sizes
                function adjustSize(partNum, action) {{
                    const panel = document.getElementById(`screenPart${{partNum}}`);
                    const currentHeight = panel.offsetHeight;
                    const currentWidth = panel.offsetWidth;
                    
                    let newHeight = currentHeight;
                    let newWidth = currentWidth;
                    
                    if (action === 'increase') {{
                        newHeight = Math.min(currentHeight + 100, window.innerHeight - 200);
                        newWidth = Math.min(currentWidth + 100, window.innerWidth - 100);
                        panelSizes[partNum] = 'large';
                    },} else if (action === 'decrease') {{
                        newHeight = Math.max(currentHeight - 100, 400);
                        newWidth = Math.max(currentWidth - 100, 300);
                        panelSizes[partNum] = 'small';
                    },} else if (action === 'reset') {{
                        newHeight = 600;
                        newWidth = 'auto';
                        panelSizes[partNum] = 'normal';
                    },}
                    
                    panel.style.height = newHeight + 'px';
                    if (newWidth !== 'auto') {{
                        panel.style.width = newWidth + 'px';
                    },} else {{
                        panel.style.width = '';
                    },}
                    
                    // Refresh editors after resize
                    setTimeout(() => {{
                        if (editors[partNum]) {{
                            editors[partNum].refresh();
                        },}
                    },}, 100);
                },}
                
                // Reset all panel sizes
                function resetAllSizes() {{
                    for (let i = 1; i <= 3; i++) {{
                        adjustSize(i, 'reset');
                    },}
                },}
                
                // Connect panels for synchronized editing
                function connectPanel(sourcePanel, targetPanel) {{
                    if (!targetPanel) {{
                        // Disconnect
                        delete connections[sourcePanel];
                        document.getElementById(`indicator${{sourcePanel}}`).classList.add('d-none');
                        return;
                    },}
                    
                    connections[sourcePanel] = targetPanel;
                    document.getElementById(`indicator${{sourcePanel}}`).classList.remove('d-none');
                    document.getElementById(`indicator${{sourcePanel}}`).classList.add('connected');
                    
                    console.log(`Panel ${{sourcePanel}} connected to ${{targetPanel}}`);
                },}
                
                // Auto-connect panels in a useful way
                function autoConnectPanels() {{
                    const layout = document.querySelector('input[name="screenLayout"]:checked').value;
                    
                    if (layout === 'triple') {{
                        // Panel 1: Code, Panel 2: Editor, Panel 3: Preview
                        setMode(1, 'code');
                        setMode(2, 'editor');
                        setMode(3, 'frontend');
                        connectPanel(2, '3'); // Editor connects to Preview
                        
                        document.querySelector('#screenPart2 select').value = '3';
                        
                    },} else if (layout === 'double') {{
                        // Panel 1: Editor, Panel 2: Preview
                        setMode(1, 'editor');
                        setMode(2, 'frontend');
                        connectPanel(1, '2'); // Editor connects to Preview
                        
                        document.querySelector('#screenPart1 select').value = '2';
                    },}
                    
                    alert('Panels auto-connected for optimal editing workflow!');
                },}
                
                // Update connected panels when editor changes
                function updateConnectedPanels(sourcePanel) {{
                    const target = connections[sourcePanel];
                    if (!target || !editors[sourcePanel]) return;
                    
                    const newContent = editors[sourcePanel].getValue();
                    
                    if (target === 'all') {{
                        // Update all other panels
                        for (let i = 1; i <= 3; i++) {{
                            if (i !== sourcePanel) {{
                                updatePanelContent(i, newContent);
                            },}
                        },}
                    },} else {{
                        // Update specific target panel
                        updatePanelContent(parseInt(target), newContent);
                    },}
                },}
                
                // Update content in a specific panel
                function updatePanelContent(panelNum, newContent) {{
                    // Update code view
                    const codeView = document.querySelector(`#codeView${{panelNum}} code`);
                    if (codeView) {{
                        codeView.textContent = newContent;
                        Prism.highlightElement(codeView);
                    },}
                    
                    // Update frontend preview if it's active
                    const frontendView = document.getElementById(`frontendView${{panelNum}}`);
                    if (frontendView && !frontendView.classList.contains('d-none')) {{
                        const iframe = frontendView.querySelector('iframe');
                        if (iframe) {{
                            iframe.srcdoc = newContent;
                        },}
                    },}
                    
                    // Update editor if it's different from source
                    if (editors[panelNum] && editors[panelNum].getValue() !== newContent) {{
                        const cursor = editors[panelNum].getCursor();
                        editors[panelNum].setValue(newContent);
                        editors[panelNum].setCursor(cursor);
                    },}
                },}
                
                // Screen layout change handler
                document.querySelectorAll('input[name="screenLayout"]').forEach(radio => {{
                    radio.addEventListener('change', function() {{
                        const layout = this.value;
                        const part1 = document.getElementById('screenPart1');
                        const part2 = document.getElementById('screenPart2');
                        const part3 = document.getElementById('screenPart3');
                        
                        // Reset all parts
                        part1.className = 'col-12';
                        part2.className = 'col-6 d-none';
                        part3.className = 'col-4 d-none';
                        
                        if (layout === 'single') {{
                            part1.className = 'col-12';
                        },} else if (layout === 'double') {{
                            part1.className = 'col-6';
                            part2.className = 'col-6';
                        },} else if (layout === 'triple') {{
                            part1.className = 'col-4';
                            part2.className = 'col-4';
                            part3.className = 'col-4';
                        },}
                        
                        // Refresh editors after layout change
                        setTimeout(() => {{
                            Object.values(editors).forEach(editor => {{
                                if (editor) editor.refresh();
                            },});
                        },}, 100);
                    },});
                },});
                
                // Set viewing mode for a panel
                function setMode(partNum, mode) {{
                    const codeView = document.getElementById(`codeView${{partNum}}`);
                    const frontendView = document.getElementById(`frontendView${{partNum}}`);
                    const editorView = document.getElementById(`editorView${{partNum}}`);
                    const buttons = document.querySelector(`#screenPart${{partNum}} .btn-group`).children;
                    
                    // Hide all views
                    codeView.classList.add('d-none');
                    frontendView.classList.add('d-none');
                    editorView.classList.add('d-none');
                    
                    // Remove active class from all buttons
                    Array.from(buttons).forEach(btn => btn.classList.remove('active-mode'));
                    
                    // Show selected view and activate button
                    if (mode === 'code') {{
                        codeView.classList.remove('d-none');
                        buttons[0].classList.add('active-mode');
                        // Re-highlight code
                        Prism.highlightAll();
                    },} else if (mode === 'frontend') {{
                        frontendView.classList.remove('d-none');
                        buttons[1].classList.add('active-mode');
                        // Update iframe content if editor was used
                        if (editors[partNum]) {{
                            const iframe = frontendView.querySelector('iframe');
                            iframe.srcdoc = editors[partNum].getValue();
                        },}
                        // Update connected panels
                        updateConnectedPanels(partNum);
                    },} else if (mode === 'editor') {{
                        editorView.classList.remove('d-none');
                        buttons[2].classList.add('active-mode');
                        // Refresh editor
                        if (editors[partNum]) {{
                            setTimeout(() => editors[partNum].refresh(), 50);
                        },}
                    },}
                },}
                
                // Download template function
                function downloadTemplate(partNum) {{
                    let content = originalContent;
                    
                    // If editor mode was used, get the edited content
                    if (editors[partNum]) {{
                        content = editors[partNum].getValue();
                    },}
                    
                    // Show download options modal
                    const formats = ['html', 'txt', 'json'];
                    const format = prompt('Choose download format:\\n1. HTML (.html)\\n2. Text (.txt)\\n3. JSON (.json)\\n\\nEnter 1, 2, or 3:', '1');
                    
                    let filename = '{template_name}';
                    let mimeType = 'text/html';
                    
                    if (format === '2') {{
                        filename = filename.replace('.html', '.txt');
                        mimeType = 'text/plain';
                    },} else if (format === '3') {{
                        const jsonContent = {{
                            filename: '{template_name}',
                            content: content,
                            timestamp: new Date().toISOString(),
                            panel: partNum
                        },};
                        content = JSON.stringify(jsonContent, null, 2);
                        filename = filename.replace('.html', '.json');
                        mimeType = 'application/json';
                    },}
                    
                    // Create and trigger download
                    const blob = new Blob([content], {{ type: mimeType }});
                    const url = URL.createObjectURL(blob);
                    const a = document.createElement('a');
                    a.href = url;
                    a.download = filename;
                    document.body.appendChild(a);
                    a.click();
                    document.body.removeChild(a);
                    URL.revokeObjectURL(url);
                },}
                
                // Font size and zoom functions
                function setFontSize(size) {{
                    currentFontSize = parseInt(size);
                    document.documentElement.style.setProperty('--font-size', size + 'px');
                    document.getElementById('fontSizeDisplay').textContent = size + 'px';
                    
                    // Refresh all editors with new font size
                    Object.values(editors).forEach(editor => {{
                        if (editor) {{
                            editor.refresh();
                        },}
                    },});
                },}
                
                function zoomIn() {{
                    const newSize = Math.min(currentFontSize + 2, 24);
                    document.getElementById('fontSizeSlider').value = newSize;
                    setFontSize(newSize);
                },}
                
                function zoomOut() {{
                    const newSize = Math.max(currentFontSize - 2, 8);
                    document.getElementById('fontSizeSlider').value = newSize;
                    setFontSize(newSize);
                },}
                
                function resetZoom() {{
                    document.getElementById('fontSizeSlider').value = 14;
                    setFontSize(14);
                },}
                
                // Screen layout functions
                function setScreenLayout(layout) {{
                    document.getElementById(layout).checked = true;
                    document.getElementById(layout).dispatchEvent(new Event('change'));
                },}
                
                // Toolbar movement functions
                function moveToolbar(position) {{
                    const toolbar = document.getElementById('moveableToolbar');
                    
                    // Remove all position classes
                    toolbar.classList.remove('toolbar-horizontal', 'toolbar-vertical-left', 'toolbar-vertical-right');
                    
                    // Reset styles
                    toolbar.style.top = '';
                    toolbar.style.bottom = '';
                    toolbar.style.left = '';
                    toolbar.style.right = '';
                    toolbar.style.transform = '';
                    
                    switch(position) {{
                        case 'top':
                            toolbar.style.top = '70px';
                            toolbar.style.left = '50%';
                            toolbar.style.transform = 'translateX(-50%)';
                            toolbar.classList.add('toolbar-horizontal');
                            break;
                        case 'bottom':
                            toolbar.style.bottom = '20px';
                            toolbar.style.left = '50%';
                            toolbar.style.transform = 'translateX(-50%)';
                            toolbar.classList.add('toolbar-horizontal');
                            break;
                        case 'left':
                            toolbar.style.top = '70px';
                            toolbar.style.left = '20px';
                            toolbar.classList.add('toolbar-vertical-left');
                            break;
                        case 'right':
                            toolbar.style.top = '70px';
                            toolbar.style.right = '20px';
                            toolbar.classList.add('toolbar-vertical-right');
                            break;
                    },}
                },}
                
                // Download current template
                function downloadCurrentTemplate() {{
                    // Get content from the active editor or original content
                    let content = originalContent;
                    for (let i = 1; i <= 3; i++) {{
                        if (editors[i] && !document.getElementById(`screenPart${{i}}`).classList.contains('d-none')) {{
                            content = editors[i].getValue();
                            break;
                        },}
                    },}
                    
                    downloadTemplate(1, content);
                },}
                
                // Make toolbar draggable
                function initializeToolbarDragging() {{
                    const toolbar = document.getElementById('moveableToolbar');
                    const handle = toolbar.querySelector('.toolbar-handle');
                    
                    handle.addEventListener('mousedown', function(e) {{
                        isDragging = true;
                        const rect = toolbar.getBoundingClientRect();
                        dragOffset.x = e.clientX - rect.left;
                        dragOffset.y = e.clientY - rect.top;
                        
                        document.addEventListener('mousemove', handleDrag);
                        document.addEventListener('mouseup', stopDrag);
                    },});
                    
                    function handleDrag(e) {{
                        if (!isDragging) return;
                        
                        const x = e.clientX - dragOffset.x;
                        const y = e.clientY - dragOffset.y;
                        
                        // Keep toolbar within viewport
                        const maxX = window.innerWidth - toolbar.offsetWidth;
                        const maxY = window.innerHeight - toolbar.offsetHeight;
                        
                        toolbar.style.left = Math.max(0, Math.min(x, maxX)) + 'px';
                        toolbar.style.top = Math.max(0, Math.min(y, maxY)) + 'px';
                        toolbar.style.right = 'auto';
                        toolbar.style.bottom = 'auto';
                        toolbar.style.transform = 'none';
                    },}
                    
                    function stopDrag() {{
                        isDragging = false;
                        document.removeEventListener('mousemove', handleDrag);
                        document.removeEventListener('mouseup', stopDrag);
                    },}
                },}
                
                // Initialize everything when page loads
                document.addEventListener('DOMContentLoaded', function() {{
                    initializeEditors();
                    initializeToolbarDragging();
                    Prism.highlightAll();
                    
                    // Set initial font size
                    setFontSize(14);
                    
                    // Remove font size slider if exists (moved to toolbar)
                    const fontSlider = document.getElementById('fontSizeSlider');
                    if (fontSlider) {{
                        fontSlider.parentElement.style.display = 'none';
                    },}
                },});
            </script>
        </body>
        </html>
        """
        
        return html_content
        
    except Exception as e:
        flash(f'Error viewing template: {str(e)}', 'error')
        return redirect(url_for('index'))

# Register admin blueprint
# Admin blueprint is registered in app.py
