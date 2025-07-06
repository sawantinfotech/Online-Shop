from datetime import datetime
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
import json

class Business(db.Model):
    __tablename__ = 'businesses'
    
    id = db.Column(db.Integer, primary_key=True)
    business_name = db.Column(db.String(200), nullable=False)
    logo_url = db.Column(db.String(500))
    license_number = db.Column(db.String(100))
    contact_number = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    address = db.Column(db.Text)
    business_type = db.Column(db.String(100))
    verification_status = db.Column(db.String(20), default='pending')
    documents = db.Column(db.Text)  # JSON string of document URLs
    gpay_enabled = db.Column(db.Boolean, default=False)
    paytm_enabled = db.Column(db.Boolean, default=False)
    brainlo_enabled = db.Column(db.Boolean, default=False)
    password_hash = db.Column(db.String(256))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    products = db.relationship('Product', backref='business', lazy=True, cascade='all, delete-orphan')
    orders = db.relationship('Order', backref='business', lazy=True, cascade='all, delete-orphan')
    customers = db.relationship('Customer', backref='business', lazy=True, cascade='all, delete-orphan')
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def get_documents(self):
        return json.loads(self.documents) if self.documents else []
    
    def set_documents(self, documents_list):
        self.documents = json.dumps(documents_list)

class Category(db.Model):
    __tablename__ = 'categories'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    products = db.relationship('Product', backref='category', lazy=True)

class Product(db.Model):
    __tablename__ = 'products'
    
    id = db.Column(db.Integer, primary_key=True)
    business_id = db.Column(db.Integer, db.ForeignKey('businesses.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    product_name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, default=0)
    images = db.Column(db.Text)  # JSON string of image URLs
    weight = db.Column(db.Float)  # in kg
    dimensions = db.Column(db.String(100))  # LxWxH format
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    order_items = db.relationship('OrderItem', backref='product', lazy=True)
    
    def get_images(self):
        return json.loads(self.images) if self.images else []
    
    def set_images(self, images_list):
        self.images = json.dumps(images_list)

class Customer(db.Model):
    __tablename__ = 'customers'
    
    id = db.Column(db.Integer, primary_key=True)
    business_id = db.Column(db.Integer, db.ForeignKey('businesses.id'), nullable=False)
    name = db.Column(db.String(200), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(120))
    address = db.Column(db.Text)
    social_media = db.Column(db.Text)  # JSON string
    groups = db.Column(db.Text)  # JSON string of group names
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    orders = db.relationship('Order', backref='customer', lazy=True)
    
    def get_social_media(self):
        return json.loads(self.social_media) if self.social_media else {}
    
    def set_social_media(self, social_dict):
        self.social_media = json.dumps(social_dict)
    
    def get_groups(self):
        return json.loads(self.groups) if self.groups else []
    
    def set_groups(self, groups_list):
        self.groups = json.dumps(groups_list)

class Order(db.Model):
    __tablename__ = 'orders'
    
    id = db.Column(db.Integer, primary_key=True)
    business_id = db.Column(db.Integer, db.ForeignKey('businesses.id'), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    order_status = db.Column(db.String(20), default='pending')
    total_amount = db.Column(db.Float, nullable=False)
    delivery_charges = db.Column(db.Float, default=0.0)
    payment_status = db.Column(db.String(20), default='pending')
    payment_method = db.Column(db.String(20))
    delivery_address = db.Column(db.Text)
    order_date = db.Column(db.DateTime, default=datetime.utcnow)
    delivery_date = db.Column(db.DateTime)
    invoice_url = db.Column(db.String(500))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    order_items = db.relationship('OrderItem', backref='order', lazy=True, cascade='all, delete-orphan')
    payments = db.relationship('Payment', backref='order', lazy=True, cascade='all, delete-orphan')
    deliveries = db.relationship('Delivery', backref='order', lazy=True, cascade='all, delete-orphan')

class OrderItem(db.Model):
    __tablename__ = 'order_items'
    
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    total = db.Column(db.Float, nullable=False)

class Payment(db.Model):
    __tablename__ = 'payments'
    
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    payment_method = db.Column(db.String(20), nullable=False)
    transaction_id = db.Column(db.String(100))
    status = db.Column(db.String(20), default='pending')
    gateway_response = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Delivery(db.Model):
    __tablename__ = 'deliveries'
    
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    delivery_type = db.Column(db.String(20), default='standard')
    charges = db.Column(db.Float, nullable=False)
    estimated_time = db.Column(db.DateTime)
    actual_time = db.Column(db.DateTime)
    status = db.Column(db.String(20), default='pending')
    tracking_number = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class SMSTemplate(db.Model):
    __tablename__ = 'sms_templates'
    
    id = db.Column(db.Integer, primary_key=True)
    business_id = db.Column(db.Integer, db.ForeignKey('businesses.id'), nullable=False)
    template_name = db.Column(db.String(100), nullable=False)
    template_content = db.Column(db.Text, nullable=False)
    template_type = db.Column(db.String(50))  # order_confirmation, delivery_update, etc.
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
