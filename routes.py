from flask import render_template, request, redirect, url_for, flash, session, jsonify, send_file
from werkzeug.utils import secure_filename
from app import app, db
from models import Business, Product, Customer, Order, OrderItem, Payment, Delivery, Category, SMSTemplate
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
    return render_template('index.html')

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
