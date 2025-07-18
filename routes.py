from flask import render_template, request, redirect, url_for, flash, session, jsonify, send_file
from werkzeug.utils import secure_filename
from app import app, db
from admin import admin_bp
from models import Business, Product, Customer, Order, OrderItem, Payment, Delivery, Category, SMSTemplate, User, DeliveryProfile, DeliveryVehicle, DeliveryAssignment, PasswordReset, App, MatrimonyProfile
from forms import BusinessRegistrationForm, ProductForm, CustomerForm, OrderForm, PaymentSettingsForm, LoginForm, SMSTemplateForm
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

# Session management
def login_required(f):
    from functools import wraps
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'business_id' not in session:
            flash('Please log in to access this page.', 'error')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def index():
    if 'business_id' in session:
        return redirect(url_for('dashboard'))
    
    # Get featured products and businesses for public home page
    featured_products = Product.query.filter_by(is_active=True).order_by(Product.created_at.desc()).limit(12).all()
    featured_businesses = Business.query.filter_by(verification_status='verified').order_by(Business.created_at.desc()).limit(8).all()
    categories = Category.query.all()
    
    # Get delivery profiles for carousel
    delivery_profiles = db.session.query(DeliveryProfile).join(
        User, DeliveryProfile.user_id == User.id
    ).filter(DeliveryProfile.verification_status == 'verified').limit(10).all()
    
    # Get featured apps for carousel
    featured_apps = App.query.filter_by(status='active').order_by(App.featured.desc(), App.downloads.desc()).limit(20).all()
    
    # Get matrimony profiles for carousel
    matrimony_profiles = MatrimonyProfile.query.filter_by(profile_visible=True).order_by(MatrimonyProfile.created_at.desc()).limit(10).all()
    
    # Get recent reviews and ratings (if available)
    # recent_reviews = Review.query.order_by(Review.created_at.desc()).limit(5).all()
    
    return render_template('public_home.html', 
                         featured_products=featured_products,
                         featured_businesses=featured_businesses,
                         categories=categories,
                         delivery_profiles=delivery_profiles,
                         featured_apps=featured_apps,
                         matrimony_profiles=matrimony_profiles)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = BusinessRegistrationForm()
    if form.validate_on_submit():
        # Check if business already exists
        existing_business = Business.query.filter_by(email=form.email.data).first()
        if existing_business:
            flash('Business with this email already exists!', 'error')
            return render_template('business_register.html', form=form)
        
        # Create new business
        business = Business(
            business_name=form.business_name.data,
            contact_number=form.contact_number.data,
            email=form.email.data,
            address=form.address.data,
            business_type=form.business_type.data,
            license_number=form.license_number.data
        )
        business.set_password(form.password.data)
        
        # Handle file uploads
        documents = []
        if form.logo.data:
            logo_path = save_uploaded_file(form.logo.data, 'logos')
            business.logo_url = logo_path
        
        if form.business_card.data:
            documents.append(save_uploaded_file(form.business_card.data, 'documents'))
        if form.id_proof.data:
            documents.append(save_uploaded_file(form.id_proof.data, 'documents'))
        if form.business_proof.data:
            documents.append(save_uploaded_file(form.business_proof.data, 'documents'))
        
        business.set_documents(documents)
        
        db.session.add(business)
        db.session.commit()
        
        flash('Business registration successful! Please wait for verification.', 'success')
        return redirect(url_for('login'))
    
    return render_template('business_register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        business = Business.query.filter_by(email=form.email.data).first()
        if business and business.check_password(form.password.data):
            if business.verification_status == 'verified':
                session['business_id'] = business.id
                session['business_name'] = business.business_name
                flash('Login successful!', 'success')
                return redirect(url_for('dashboard'))
            else:
                flash('Your business account is pending verification.', 'warning')
        else:
            flash('Invalid email or password.', 'error')
    
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    business_id = session['business_id']
    
    # Get statistics
    total_products = Product.query.filter_by(business_id=business_id).count()
    total_customers = Customer.query.filter_by(business_id=business_id).count()
    total_orders = Order.query.filter_by(business_id=business_id).count()
    
    # Recent orders
    recent_orders = Order.query.filter_by(business_id=business_id).order_by(Order.created_at.desc()).limit(5).all()
    
    # Low stock products
    low_stock_products = Product.query.filter_by(business_id=business_id).filter(Product.quantity <= 10).all()
    
    return render_template('dashboard.html', 
                         total_products=total_products,
                         total_customers=total_customers,
                         total_orders=total_orders,
                         recent_orders=recent_orders,
                         low_stock_products=low_stock_products)

@app.route('/products')
@login_required
def products():
    business_id = session['business_id']
    page = request.args.get('page', 1, type=int)
    search = request.args.get('search', '')
    category_id = request.args.get('category', '', type=str)
    
    query = Product.query.filter_by(business_id=business_id)
    
    if search:
        query = query.filter(Product.product_name.contains(search))
    
    if category_id:
        query = query.filter_by(category_id=int(category_id))
    
    products = query.order_by(Product.created_at.desc()).paginate(
        page=page, per_page=10, error_out=False
    )
    
    categories = Category.query.all()
    
    return render_template('products.html', products=products, categories=categories, search=search, category_id=category_id)

@app.route('/products/add', methods=['GET', 'POST'])
@login_required
def add_product():
    form = ProductForm()
    form.category_id.choices = [(0, 'Select Category')] + [(c.id, c.name) for c in Category.query.all()]
    
    if form.validate_on_submit():
        product = Product(
            business_id=session['business_id'],
            product_name=form.product_name.data,
            description=form.description.data,
            price=form.price.data,
            quantity=form.quantity.data,
            weight=form.weight.data,
            dimensions=form.dimensions.data,
            is_active=form.is_active.data
        )
        
        if form.category_id.data:
            product.category_id = form.category_id.data
        
        if form.images.data:
            image_path = save_uploaded_file(form.images.data, 'products')
            product.set_images([image_path])
        
        db.session.add(product)
        db.session.commit()
        
        flash('Product added successfully!', 'success')
        return redirect(url_for('products'))
    
    return render_template('product_form.html', form=form, title='Add Product')

@app.route('/products/<int:product_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_product(product_id):
    product = Product.query.filter_by(id=product_id, business_id=session['business_id']).first_or_404()
    form = ProductForm(obj=product)
    form.category_id.choices = [(0, 'Select Category')] + [(c.id, c.name) for c in Category.query.all()]
    
    if form.validate_on_submit():
        product.product_name = form.product_name.data
        product.description = form.description.data
        product.price = form.price.data
        product.quantity = form.quantity.data
        product.weight = form.weight.data
        product.dimensions = form.dimensions.data
        product.is_active = form.is_active.data
        
        if form.category_id.data:
            product.category_id = form.category_id.data
        
        if form.images.data:
            image_path = save_uploaded_file(form.images.data, 'products')
            product.set_images([image_path])
        
        db.session.commit()
        flash('Product updated successfully!', 'success')
        return redirect(url_for('products'))
    
    return render_template('product_form.html', form=form, product=product, title='Edit Product')

@app.route('/products/<int:product_id>/delete', methods=['POST'])
@login_required
def delete_product(product_id):
    product = Product.query.filter_by(id=product_id, business_id=session['business_id']).first_or_404()
    db.session.delete(product)
    db.session.commit()
    flash('Product deleted successfully!', 'success')
    return redirect(url_for('products'))

@app.route('/customers')
@login_required
def customers():
    business_id = session['business_id']
    page = request.args.get('page', 1, type=int)
    search = request.args.get('search', '')
    
    query = Customer.query.filter_by(business_id=business_id)
    
    if search:
        query = query.filter(Customer.name.contains(search))
    
    customers = query.order_by(Customer.created_at.desc()).paginate(
        page=page, per_page=10, error_out=False
    )
    
    return render_template('customers.html', customers=customers, search=search)

@app.route('/customers/add', methods=['GET', 'POST'])
@login_required
def add_customer():
    form = CustomerForm()
    
    if form.validate_on_submit():
        customer = Customer(
            business_id=session['business_id'],
            name=form.name.data,
            phone_number=form.phone_number.data,
            email=form.email.data,
            address=form.address.data
        )
        
        if form.groups.data:
            groups = [g.strip() for g in form.groups.data.split(',')]
            customer.set_groups(groups)
        
        db.session.add(customer)
        db.session.commit()
        
        flash('Customer added successfully!', 'success')
        return redirect(url_for('customers'))
    
    return render_template('customer_form.html', form=form, title='Add Customer')

@app.route('/customers/<int:customer_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_customer(customer_id):
    customer = Customer.query.filter_by(id=customer_id, business_id=session['business_id']).first_or_404()
    form = CustomerForm(obj=customer)
    
    if form.validate_on_submit():
        customer.name = form.name.data
        customer.phone_number = form.phone_number.data
        customer.email = form.email.data
        customer.address = form.address.data
        
        if form.groups.data:
            groups = [g.strip() for g in form.groups.data.split(',')]
            customer.set_groups(groups)
        
        db.session.commit()
        flash('Customer updated successfully!', 'success')
        return redirect(url_for('customers'))
    
    return render_template('customer_form.html', form=form, customer=customer, title='Edit Customer')

@app.route('/orders')
@login_required
def orders():
    business_id = session['business_id']
    page = request.args.get('page', 1, type=int)
    status = request.args.get('status', '')
    
    query = Order.query.filter_by(business_id=business_id)
    
    if status:
        query = query.filter_by(order_status=status)
    
    orders = query.order_by(Order.created_at.desc()).paginate(
        page=page, per_page=10, error_out=False
    )
    
    return render_template('orders.html', orders=orders, status=status)

@app.route('/orders/<int:order_id>')
@login_required
def order_details(order_id):
    order = Order.query.filter_by(id=order_id, business_id=session['business_id']).first_or_404()
    return render_template('order_details.html', order=order)

@app.route('/orders/<int:order_id>/update_status', methods=['POST'])
@login_required
def update_order_status(order_id):
    order = Order.query.filter_by(id=order_id, business_id=session['business_id']).first_or_404()
    new_status = request.form.get('status')
    
    if new_status in ['pending', 'confirmed', 'processing', 'shipped', 'delivered', 'cancelled']:
        order.order_status = new_status
        db.session.commit()
        
        # Send SMS notification
        try:
            message = f"Your order #{order.id} status has been updated to {new_status}."
            send_sms(order.customer.phone_number, message)
        except Exception as e:
            logging.error(f"Failed to send SMS: {e}")
        
        flash('Order status updated successfully!', 'success')
    else:
        flash('Invalid status!', 'error')
    
    return redirect(url_for('order_details', order_id=order_id))

@app.route('/orders/<int:order_id>/invoice')
@login_required
def generate_invoice(order_id):
    order = Order.query.filter_by(id=order_id, business_id=session['business_id']).first_or_404()
    
    # Generate PDF invoice
    pdf_path = generate_invoice_pdf(order)
    
    return send_file(pdf_path, as_attachment=True, download_name=f'invoice_{order.id}.pdf')

@app.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    business = Business.query.get(session['business_id'])
    form = PaymentSettingsForm(obj=business)
    
    if form.validate_on_submit():
        business.gpay_enabled = form.gpay_enabled.data
        business.paytm_enabled = form.paytm_enabled.data
        business.brainlo_enabled = form.brainlo_enabled.data
        
        db.session.commit()
        flash('Settings updated successfully!', 'success')
        return redirect(url_for('settings'))
    
    return render_template('settings.html', form=form, business=business)

@app.route('/profile')
@login_required
def profile():
    business = Business.query.get(session['business_id'])
    return render_template('business_profile.html', business=business)

@app.route('/products/import', methods=['POST'])
@login_required
def import_products():
    if 'file' not in request.files:
        flash('No file selected!', 'error')
        return redirect(url_for('products'))
    
    file = request.files['file']
    if file.filename == '':
        flash('No file selected!', 'error')
        return redirect(url_for('products'))
    
    if file and allowed_file(file.filename, ['csv', 'xlsx']):
        try:
            # Read CSV file
            stream = io.StringIO(file.stream.read().decode("UTF8"), newline=None)
            csv_input = csv.DictReader(stream)
            
            imported_count = 0
            for row in csv_input:
                if 'product_name' in row and 'price' in row:
                    product = Product(
                        business_id=session['business_id'],
                        product_name=row['product_name'],
                        description=row.get('description', ''),
                        price=float(row['price']),
                        quantity=int(row.get('quantity', 0)),
                        weight=float(row.get('weight', 0)) if row.get('weight') else None,
                        dimensions=row.get('dimensions', ''),
                        is_active=True
                    )
                    db.session.add(product)
                    imported_count += 1
            
            db.session.commit()
            flash(f'Successfully imported {imported_count} products!', 'success')
            
        except Exception as e:
            flash(f'Error importing products: {str(e)}', 'error')
    else:
        flash('Invalid file format! Please upload CSV or Excel file.', 'error')
    
    return redirect(url_for('products'))

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
    return render_template('test_email.html', email_settings=email_settings)

@app.route('/email-settings')
@login_required
def email_settings():
    """Display email configuration status"""
    settings = get_email_settings()
    return render_template('email_settings.html', settings=settings)

# Delivery System Routes

@app.route('/careers')
def careers():
    """Delivery careers page"""
    return render_template('careers.html')

@app.route('/apply-delivery', methods=['GET', 'POST'])
def apply_delivery():
    """Apply for delivery partner position - requires user login"""
    if 'user_id' not in session:
        flash('Please log in to apply for delivery partner position.', 'error')
        return redirect(url_for('user_login'))
    
    user_id = session['user_id']
    user = User.query.get(user_id)
    
    # Check if user already has delivery profile
    existing_profile = DeliveryProfile.query.filter_by(user_id=user_id).first()
    if existing_profile:
        flash('You have already applied for delivery partner position.', 'warning')
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
        
        flash('Delivery partner application submitted! Please pay registration fee of ₹500 for verification.', 'success')
        return redirect(url_for('delivery_payment'))
    
    return render_template('delivery_application.html', user=user)

@app.route('/user/login', methods=['GET', 'POST'])
def user_login():
    """User login - unified system"""
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        
        if user and user.check_password(password):
            session['user_id'] = user.id
            session['user_name'] = user.full_name
            session['user_role'] = user.role
            
            # Check if user has delivery profile
            delivery_profile = DeliveryProfile.query.filter_by(user_id=user.id).first()
            if delivery_profile:
                session['delivery_profile_id'] = delivery_profile.id
                session['is_delivery_partner'] = True
            
            flash('Login successful!', 'success')
            
            # Redirect based on role and delivery status
            if delivery_profile and delivery_profile.verification_status == 'verified':
                return redirect(url_for('delivery_dashboard'))
            else:
                return redirect(url_for('user_dashboard'))
        else:
            flash('Invalid email or password!', 'error')
    
    return render_template('user_login.html')

@app.route('/delivery/dashboard')
def delivery_dashboard():
    """Unified delivery dashboard"""
    if 'user_id' not in session:
        flash('Please log in to access the dashboard.', 'error')
        return redirect(url_for('user_login'))
    
    user_id = session['user_id']
    user = User.query.get(user_id)
    delivery_profile = DeliveryProfile.query.filter_by(user_id=user_id).first()
    
    if not delivery_profile:
        flash('You need to apply for delivery partner position first.', 'error')
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
    
    return render_template('delivery_dashboard.html', 
                         user=user,
                         delivery_profile=delivery_profile,
                         assignments=recent_assignments,
                         stats=stats)

@app.route('/user/logout')
def user_logout():
    """User logout"""
    session.pop('user_id', None)
    session.pop('user_name', None)
    session.pop('user_role', None)
    session.pop('delivery_profile_id', None)
    session.pop('is_delivery_partner', None)
    flash('You have been logged out successfully.', 'info')
    return redirect(url_for('index'))

@app.route('/user/dashboard')
def user_dashboard():
    """User dashboard"""
    if 'user_id' not in session:
        flash('Please log in to access your dashboard.', 'error')
        return redirect(url_for('user_login'))
    
    user_id = session['user_id']
    user = User.query.get(user_id)
    delivery_profile = DeliveryProfile.query.filter_by(user_id=user_id).first()
    
    return render_template('user_dashboard.html', user=user, delivery_profile=delivery_profile)

@app.route('/user/register', methods=['GET', 'POST'])
def user_register():
    """User registration"""
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        full_name = request.form.get('full_name')
        phone_number = request.form.get('phone_number')
        address = request.form.get('address')
        password = request.form.get('password')
        
        # Check if user already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('User with this email already exists!', 'error')
            return render_template('user_register.html')
        
        # Create new user
        user = User(
            username=username,
            email=email,
            full_name=full_name,
            phone_number=phone_number,
            address=address,
            role='user'
        )
        user.set_password(password)
        
        db.session.add(user)
        db.session.commit()
        
        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('user_login'))
    
    return render_template('user_register.html')

@app.route('/delivery/login', methods=['GET', 'POST'])
def delivery_login():
    """Delivery partner login"""
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Find user with delivery role
        user = User.query.filter_by(email=email, role='delivery').first()
        if user and user.check_password(password):
            # Get delivery profile
            delivery_profile = DeliveryProfile.query.filter_by(user_id=user.id).first()
            if delivery_profile:
                session['user_id'] = user.id
                session['user_name'] = user.full_name
                session['user_role'] = 'delivery'
                session['delivery_profile_id'] = delivery_profile.id
                session['is_delivery_partner'] = True
                
                flash('Login successful!', 'success')
                return redirect(url_for('delivery_dashboard'))
            else:
                flash('No delivery profile found. Please apply for delivery partner position.', 'error')
        else:
            flash('Invalid email or password.', 'error')
    
    return render_template('delivery_login.html')

@app.route('/delivery/application', methods=['GET', 'POST'])
def delivery_application():
    """Delivery partner application form"""
    if 'user_id' not in session:
        flash('Please log in to apply for delivery partner position.', 'error')
        return redirect(url_for('user_login'))
    
    user_id = session['user_id']
    user = User.query.get(user_id)
    
    # Check if user already has delivery profile
    existing_profile = DeliveryProfile.query.filter_by(user_id=user_id).first()
    if existing_profile:
        flash('You have already applied for delivery partner position.', 'warning')
        return redirect(url_for('delivery_dashboard'))
    
    if request.method == 'POST':
        driving_license = request.form.get('driving_license')
        aadhar_number = request.form.get('aadhar_number')
        emergency_contact = request.form.get('emergency_contact')
        delivery_zone = request.form.get('delivery_zone')
        
        # Create delivery profile
        delivery_profile = DeliveryProfile(
            user_id=user_id,
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
    
    return render_template('delivery_application.html', user=user)

@app.route('/delivery/payment')
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
        return redirect(url_for('user_dashboard'))
    
    return render_template('delivery_payment.html', delivery_profile=delivery_profile)

# Password Reset Routes

@app.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    """Forgot password page"""
    if request.method == 'POST':
        email = request.form.get('email')
        user_type = request.form.get('user_type', 'business')
        
        # Generate reset token
        import secrets
        reset_token = secrets.token_urlsafe(32)
        
        # Check if user exists
        user_exists = False
        if user_type == 'business':
            user_exists = Business.query.filter_by(email=email).first()
        elif user_type == 'user':
            user_exists = User.query.filter_by(email=email).first()
        
        if user_exists:
            # Create password reset record
            from datetime import datetime, timedelta
            reset_record = PasswordReset(
                email=email,
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
    
    return render_template('forgot_password.html')

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
            return render_template('reset_password.html', token=token)
        
        # Update password based on user type
        if reset_record.user_type == 'business':
            user = Business.query.filter_by(email=reset_record.email).first()
        elif reset_record.user_type == 'user':
            user = User.query.filter_by(email=reset_record.email).first()
        
        if user:
            user.set_password(new_password)
            reset_record.used = True
            db.session.commit()
            
            flash('Password has been reset successfully. You can now log in.', 'success')
            if reset_record.user_type == 'business':
                return redirect(url_for('login'))
            elif reset_record.user_type == 'user':
                return redirect(url_for('user_login'))
        else:
            flash('User not found.', 'error')
    
    return render_template('reset_password.html', token=token)

# Apps Routes

@app.route('/apps')
def apps():
    """Apps showcase page"""
    apps = App.query.filter_by(status='active').order_by(App.featured.desc(), App.downloads.desc()).all()
    categories = db.session.query(App.category).distinct().all()
    return render_template('apps.html', apps=apps, categories=categories)

@app.route('/apps/<slug>')
def app_detail(slug):
    """Individual app detail page"""
    app_detail = App.query.filter_by(slug=slug, status='active').first_or_404()
    return render_template('app_detail.html', app=app_detail)

@app.route('/apps/category/<category>')
def apps_by_category(category):
    """Apps filtered by category"""
    apps = App.query.filter_by(category=category, status='active').order_by(App.downloads.desc()).all()
    categories = db.session.query(App.category).distinct().all()
    return render_template('apps.html', apps=apps, categories=categories, selected_category=category)

@app.route('/submit-app', methods=['GET', 'POST'])
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
            submission.app_name = form.app_name.data
            submission.app_description = form.app_description.data
            submission.app_category = form.app_category.data
            submission.app_version = form.app_version.data
            submission.app_website = form.app_website.data
            submission.app_download_url = form.app_download_url.data
            
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
            return redirect(url_for('submit_app'))
            
        except Exception as e:
            db.session.rollback()
            flash(f'Error submitting app: {str(e)}', 'error')
    
    return render_template('app_registration.html', form=form)

@app.route('/matrimony')
def matrimony():
    """Matrimony platform page"""
    # Get some sample profiles for display
    profiles = MatrimonyProfile.query.filter_by(profile_visible=True).limit(10).all()
    return render_template('matrimony.html', profiles=profiles)

@app.route('/matrimony/register', methods=['GET', 'POST'])
@app.route('/matrimony/register/<int:step>', methods=['GET', 'POST'])
def matrimony_register(step=1):
    """Multi-step matrimony registration page"""
    from forms import MatrimonyRegistrationForm
    form = MatrimonyRegistrationForm()
    
    # Ensure step is between 1 and 4
    step = max(1, min(4, step))
    
    if request.method == 'POST':
        action = request.form.get('action', 'next')
        
        if action == 'previous' and step > 1:
            return redirect(url_for('matrimony_register', step=step-1))
        elif action == 'next' and step < 4:
            # Store form data in session for multi-step
            if not session.get('matrimony_form_data'):
                session['matrimony_form_data'] = {}
            
            # Store current step data
            if step == 1:
                session['matrimony_form_data'].update({
                    'full_name': request.form.get('full_name'),
                    'age': request.form.get('age'),
                    'gender': request.form.get('gender'),
                    'marital_status': request.form.get('marital_status'),
                    'relationship_type': request.form.get('relationship_type'),
                    'email': request.form.get('email'),
                    'phone': request.form.get('phone')
                })
            elif step == 2:
                session['matrimony_form_data'].update({
                    'height': request.form.get('height'),
                    'weight': request.form.get('weight'),
                    'body_type': request.form.get('body_type'),
                    'complexion': request.form.get('complexion'),
                    'city': request.form.get('city'),
                    'state': request.form.get('state'),
                    'country': request.form.get('country', 'India'),
                    'about_yourself': request.form.get('about_yourself'),
                    'hobbies': request.form.get('hobbies')
                })
            elif step == 3:
                session['matrimony_form_data'].update({
                    'education': request.form.get('education'),
                    'occupation': request.form.get('occupation'),
                    'annual_income': request.form.get('annual_income'),
                    'company_name': request.form.get('company_name'),
                    'preferred_age_min': request.form.get('preferred_age_min'),
                    'preferred_age_max': request.form.get('preferred_age_max'),
                    'preferred_education': request.form.get('preferred_education'),
                    'membership_type': request.form.get('membership_type')
                })
            
            return redirect(url_for('matrimony_register', step=step+1))
        
        elif action == 'submit' and step == 4:
            # Process final submission
            form_data = session.get('matrimony_form_data', {})
            
            try:
                # Check if email already exists
                email = form_data.get('email')
                if email:
                    existing_profile = MatrimonyProfile.query.filter_by(email=email).first()
                    if existing_profile:
                        flash('Email already registered. Please use a different email.', 'error')
                        return redirect(url_for('matrimony_register', step=1))
                
                # Create new profile
                profile = MatrimonyProfile()
                
                # Basic Information
                profile.full_name = form_data.get('full_name')
                profile.age = int(form_data.get('age', 25))
                profile.gender = form_data.get('gender')
                profile.marital_status = form_data.get('marital_status')
                profile.relationship_type = form_data.get('relationship_type', 'marriage')
                profile.email = email
                profile.phone = form_data.get('phone')
                
                # Physical Details
                profile.height = form_data.get('height')
                profile.weight = form_data.get('weight')
                profile.body_type = form_data.get('body_type')
                profile.complexion = form_data.get('complexion')
                
                # Location
                profile.city = form_data.get('city')
                profile.state = form_data.get('state')
                profile.country = form_data.get('country', 'India')
                
                # Education & Career
                profile.education = form_data.get('education')
                profile.occupation = form_data.get('occupation')
                profile.annual_income = form_data.get('annual_income')
                profile.company_name = form_data.get('company_name')
                
                # About and Hobbies
                profile.bio = form_data.get('about_yourself')
                profile.hobbies = form_data.get('hobbies')
                
                # Partner Preferences
                profile.partner_age_min = int(form_data.get('preferred_age_min', 18))
                profile.partner_age_max = int(form_data.get('preferred_age_max', 35))
                profile.partner_education = form_data.get('preferred_education')
                
                # Membership
                profile.membership_badge = form_data.get('membership_type', 'basic')
                profile.premium_member = profile.membership_badge in ['gold', 'platinum']
                
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
                return redirect(url_for('matrimony_register', step=step))
    
    # Pre-populate form with session data
    form_data = session.get('matrimony_form_data', {})
    
    return render_template('matrimony_register_step.html', form=form, step=step, form_data=form_data)

@app.route('/matrimony/profile/<int:profile_id>')
def matrimony_profile(profile_id):
    """View matrimony profile"""
    profile = MatrimonyProfile.query.get_or_404(profile_id)
    
    # Increment profile views
    profile.profile_views += 1
    db.session.commit()
    
    return render_template('matrimony_profile.html', profile=profile)

@app.route('/matrimony/profiles')
def matrimony_profiles():
    """Browse all matrimony profiles"""
    page = request.args.get('page', 1, type=int)
    per_page = 12
    
    profiles = MatrimonyProfile.query.filter_by(profile_visible=True).paginate(
        page=page, per_page=per_page, error_out=False
    )
    
    return render_template('matrimony_profiles.html', profiles=profiles)

@app.route('/matrimony/interact/<int:profile_id>/<action>')
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

@app.route('/matrimony/share/<int:profile_id>/<platform>')
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

# Register admin blueprint
# Admin blueprint is registered in app.py
