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

# New models for enhanced features

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256))
    full_name = db.Column(db.String(200))
    profile_photo = db.Column(db.String(500))
    phone_number = db.Column(db.String(15))
    address = db.Column(db.Text)
    is_online = db.Column(db.Boolean, default=False)
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    role = db.Column(db.String(20), default='user')  # user, manager, admin, super_admin
    business_id = db.Column(db.Integer, db.ForeignKey('businesses.id'))
    credit_points = db.Column(db.Integer, default=0)
    subscription_plan = db.Column(db.String(50), default='free')
    custom_homepage = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    reviews = db.relationship('Review', backref='user', lazy=True)
    likes = db.relationship('Like', backref='user', lazy=True)
    comments = db.relationship('Comment', backref='user', lazy=True)
    followers = db.relationship('Follow', foreign_keys='Follow.followed_id', backref='followed', lazy='dynamic')
    following = db.relationship('Follow', foreign_keys='Follow.follower_id', backref='follower', lazy='dynamic')
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def get_followers_count(self):
        return self.followers.count()
    
    def get_following_count(self):
        return self.following.count()

class Follow(db.Model):
    __tablename__ = 'follows'
    
    id = db.Column(db.Integer, primary_key=True)
    follower_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    followed_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Like(db.Model):
    __tablename__ = 'likes'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    target_type = db.Column(db.String(20), nullable=False)  # product, business
    target_id = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Comment(db.Model):
    __tablename__ = 'comments'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    target_type = db.Column(db.String(20), nullable=False)  # product, business
    target_id = db.Column(db.Integer, nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Review(db.Model):
    __tablename__ = 'reviews'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    target_type = db.Column(db.String(20), nullable=False)  # product, business
    target_id = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Integer, nullable=False)  # 1-5 stars
    review_text = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Favorite(db.Model):
    __tablename__ = 'favorites'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    target_type = db.Column(db.String(20), nullable=False)  # product, business
    target_id = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Advertisement(db.Model):
    __tablename__ = 'advertisements'
    
    id = db.Column(db.Integer, primary_key=True)
    business_id = db.Column(db.Integer, db.ForeignKey('businesses.id'), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text)
    media_url = db.Column(db.String(500))  # image or video URL
    media_type = db.Column(db.String(20))  # image, video
    duration = db.Column(db.Integer, default=5)  # seconds for video
    target_audience = db.Column(db.Text)  # JSON for targeting
    status = db.Column(db.String(20), default='pending')  # pending, approved, rejected
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    budget = db.Column(db.Float, default=0.0)
    impressions = db.Column(db.Integer, default=0)
    clicks = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class PricingPlan(db.Model):
    __tablename__ = 'pricing_plans'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    billing_cycle = db.Column(db.String(20))  # monthly, yearly
    features = db.Column(db.Text)  # JSON array of features
    max_products = db.Column(db.Integer, default=-1)  # -1 for unlimited
    max_orders = db.Column(db.Integer, default=-1)
    max_customers = db.Column(db.Integer, default=-1)
    custom_homepage = db.Column(db.Boolean, default=False)
    advanced_analytics = db.Column(db.Boolean, default=False)
    priority_support = db.Column(db.Boolean, default=False)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class UserSubscription(db.Model):
    __tablename__ = 'user_subscriptions'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    plan_id = db.Column(db.Integer, db.ForeignKey('pricing_plans.id'), nullable=False)
    start_date = db.Column(db.DateTime, default=datetime.utcnow)
    end_date = db.Column(db.DateTime)
    status = db.Column(db.String(20), default='active')  # active, expired, cancelled
    payment_method = db.Column(db.String(50))
    transaction_id = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class BusinessManager(db.Model):
    __tablename__ = 'business_managers'
    
    id = db.Column(db.Integer, primary_key=True)
    business_id = db.Column(db.Integer, db.ForeignKey('businesses.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    role = db.Column(db.String(50), default='manager')  # manager, assistant_manager
    permissions = db.Column(db.Text)  # JSON array of permissions
    status = db.Column(db.String(20), default='active')
    assigned_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Unified Delivery System - Links to existing User accounts

class DeliveryProfile(db.Model):
    __tablename__ = 'delivery_profiles'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, unique=True)
    business_id = db.Column(db.Integer, db.ForeignKey('businesses.id'), nullable=True)  # If assigned to specific business
    driving_license = db.Column(db.String(100))
    aadhar_number = db.Column(db.String(20))
    emergency_contact = db.Column(db.String(15))
    delivery_zone = db.Column(db.String(20), default='local')  # local, outdoor
    is_available = db.Column(db.Boolean, default=False)
    rating = db.Column(db.Float, default=5.0)
    total_deliveries = db.Column(db.Integer, default=0)
    status = db.Column(db.String(20), default='pending')  # pending, active, inactive, suspended
    verification_status = db.Column(db.String(20), default='pending')
    registration_fee_paid = db.Column(db.Boolean, default=False)
    registration_fee_amount = db.Column(db.Float, default=500.00)
    payment_reference = db.Column(db.String(100))
    approved_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    user = db.relationship('User', foreign_keys=[user_id], backref='delivery_profile')
    business = db.relationship('Business', backref='delivery_staff')
    vehicles = db.relationship('DeliveryVehicle', backref='delivery_profile', lazy=True, foreign_keys='DeliveryVehicle.delivery_profile_id')
    deliveries = db.relationship('DeliveryAssignment', backref='delivery_profile', lazy=True, foreign_keys='DeliveryAssignment.delivery_profile_id')

class DeliveryVehicle(db.Model):
    __tablename__ = 'delivery_vehicles'
    
    id = db.Column(db.Integer, primary_key=True)
    delivery_profile_id = db.Column(db.Integer, db.ForeignKey('delivery_profiles.id'), nullable=False)
    vehicle_type = db.Column(db.String(20), nullable=False)  # cycle, bike, car, tempo
    vehicle_number = db.Column(db.String(20), nullable=False)
    license_plate = db.Column(db.String(20))
    insurance_number = db.Column(db.String(100))
    registration_date = db.Column(db.Date)
    insurance_expiry = db.Column(db.Date)
    vehicle_photo = db.Column(db.String(500))
    documents = db.Column(db.Text)  # JSON array of document URLs
    is_active = db.Column(db.Boolean, default=True)
    verification_status = db.Column(db.String(20), default='pending')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class DeliveryAssignment(db.Model):
    __tablename__ = 'delivery_assignments'
    
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    delivery_profile_id = db.Column(db.Integer, db.ForeignKey('delivery_profiles.id'), nullable=False)
    pickup_address = db.Column(db.Text, nullable=False)
    delivery_address = db.Column(db.Text, nullable=False)
    pickup_lat = db.Column(db.Float)
    pickup_lng = db.Column(db.Float)
    delivery_lat = db.Column(db.Float)
    delivery_lng = db.Column(db.Float)
    pickup_time = db.Column(db.DateTime)
    delivery_time = db.Column(db.DateTime)
    estimated_time = db.Column(db.Integer)  # minutes
    actual_time = db.Column(db.Integer)  # minutes
    distance = db.Column(db.Float)  # kilometers
    delivery_fee = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), default='assigned')  # assigned, picked_up, in_transit, delivered, failed
    notes = db.Column(db.Text)
    customer_rating = db.Column(db.Integer)  # 1-5 stars
    customer_feedback = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class PasswordReset(db.Model):
    __tablename__ = 'password_resets'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False)
    user_type = db.Column(db.String(20), nullable=False)  # business, user, delivery
    reset_token = db.Column(db.String(100), nullable=False, unique=True)
    expires_at = db.Column(db.DateTime, nullable=False)
    used = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class App(db.Model):
    __tablename__ = 'apps'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    slug = db.Column(db.String(200), unique=True, nullable=False)
    logo_url = db.Column(db.String(500))
    short_description = db.Column(db.Text)
    long_description = db.Column(db.Text)
    category = db.Column(db.String(100))
    version = db.Column(db.String(20))
    downloads = db.Column(db.Integer, default=0)
    rating = db.Column(db.Float, default=0.0)
    reviews_count = db.Column(db.Integer, default=0)
    
    # Features and screenshots
    features = db.Column(db.Text)  # JSON array of features
    screenshots = db.Column(db.Text)  # JSON array of screenshot URLs
    
    # Author information
    author_name = db.Column(db.String(200))
    author_email = db.Column(db.String(200))
    author_website = db.Column(db.String(500))
    author_bio = db.Column(db.Text)
    author_avatar = db.Column(db.String(500))
    
    # Support and contact
    support_email = db.Column(db.String(200))
    support_phone = db.Column(db.String(20))
    support_website = db.Column(db.String(500))
    documentation_url = db.Column(db.String(500))
    
    # Social links
    social_links = db.Column(db.Text)  # JSON object with social media links
    
    # App status
    status = db.Column(db.String(20), default='active')  # active, inactive, pending
    featured = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def get_features(self):
        if not self.features:
            return []
        try:
            return json.loads(self.features)
        except (json.JSONDecodeError, ValueError):
            # Handle case where features is not valid JSON
            return self.features.split('\n') if self.features else []
    
    def set_features(self, features_list):
        self.features = json.dumps(features_list)
    
    def get_screenshots(self):
        if not self.screenshots:
            return []
        try:
            return json.loads(self.screenshots)
        except (json.JSONDecodeError, ValueError):
            return []
    
    def set_screenshots(self, screenshots_list):
        self.screenshots = json.dumps(screenshots_list)
    
    def get_social_links(self):
        if not self.social_links:
            return {}
        try:
            return json.loads(self.social_links)
        except (json.JSONDecodeError, ValueError):
            return {}

class AppSubmission(db.Model):
    __tablename__ = 'app_submissions'
    
    id = db.Column(db.Integer, primary_key=True)
    
    # Basic app information
    app_name = db.Column(db.String(200), nullable=False)
    app_description = db.Column(db.Text, nullable=False)
    app_category = db.Column(db.String(100), nullable=False)
    app_version = db.Column(db.String(20), nullable=False)
    app_website = db.Column(db.String(500))
    app_download_url = db.Column(db.String(500))
    
    # Developer information
    developer_name = db.Column(db.String(200), nullable=False)
    developer_email = db.Column(db.String(200), nullable=False)
    developer_phone = db.Column(db.String(20))
    developer_company = db.Column(db.String(200))
    developer_website = db.Column(db.String(500))
    
    # App files
    app_logo = db.Column(db.String(500))  # file path
    app_screenshots = db.Column(db.Text)  # JSON array of file paths
    app_apk_file = db.Column(db.String(500))  # APK file path
    app_documentation = db.Column(db.String(500))  # documentation file path
    
    # App features and details
    app_features = db.Column(db.Text)  # JSON array of features
    target_audience = db.Column(db.String(200))
    app_size = db.Column(db.String(50))  # e.g., "25 MB"
    minimum_os_version = db.Column(db.String(50))
    permissions_required = db.Column(db.Text)  # JSON array
    
    # Pricing and monetization
    app_price = db.Column(db.String(50))  # "Free", "$2.99", etc.
    monetization_model = db.Column(db.String(100))  # "Free", "Paid", "Freemium", "Ad-supported"
    
    # Submission status
    status = db.Column(db.String(20), default='pending')  # pending, approved, rejected, needs_revision
    admin_notes = db.Column(db.Text)  # Admin feedback
    submission_date = db.Column(db.DateTime, default=datetime.utcnow)
    review_date = db.Column(db.DateTime)
    
    def get_features_list(self):
        if not self.app_features:
            return []
        try:
            return json.loads(self.app_features)
        except (json.JSONDecodeError, ValueError):
            return self.app_features.split('\n') if self.app_features else []
    
    def set_features_list(self, features_list):
        self.app_features = json.dumps(features_list)
    
    def get_screenshots_list(self):
        if not self.app_screenshots:
            return []
        try:
            return json.loads(self.app_screenshots)
        except (json.JSONDecodeError, ValueError):
            return []
    
    def set_screenshots_list(self, screenshots_list):
        self.app_screenshots = json.dumps(screenshots_list)
    
    def get_permissions_list(self):
        if not self.permissions_required:
            return []
        try:
            return json.loads(self.permissions_required)
        except (json.JSONDecodeError, ValueError):
            return self.permissions_required.split('\n') if self.permissions_required else []
    
    def set_permissions_list(self, permissions_list):
        self.permissions_required = json.dumps(permissions_list)

class MatrimonyFollow(db.Model):
    __tablename__ = 'matrimony_follows'
    
    id = db.Column(db.Integer, primary_key=True)
    follower_id = db.Column(db.Integer, db.ForeignKey('matrimony_profiles.id'), nullable=False)
    followed_id = db.Column(db.Integer, db.ForeignKey('matrimony_profiles.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    follower = db.relationship('MatrimonyProfile', foreign_keys=[follower_id], backref='following')
    followed = db.relationship('MatrimonyProfile', foreign_keys=[followed_id], backref='followers')

class AdminSection(db.Model):
    __tablename__ = 'admin_sections'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    slug = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text)
    icon = db.Column(db.String(50))
    is_active = db.Column(db.Boolean, default=True)
    sort_order = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class BlogPost(db.Model):
    __tablename__ = 'blog_posts'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    slug = db.Column(db.String(200), unique=True, nullable=False)
    content = db.Column(db.Text, nullable=False)
    excerpt = db.Column(db.Text)
    featured_image = db.Column(db.String(500))
    category = db.Column(db.String(100))
    tags = db.Column(db.Text)  # JSON array
    author_name = db.Column(db.String(100))
    author_email = db.Column(db.String(120))
    status = db.Column(db.String(20), default='draft')  # draft, published, archived
    views = db.Column(db.Integer, default=0)
    likes = db.Column(db.Integer, default=0)
    published_at = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class AdCampaign(db.Model):
    __tablename__ = 'ad_campaigns'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    image_url = db.Column(db.String(500))
    link_url = db.Column(db.String(500))
    position = db.Column(db.String(50))  # header, sidebar, footer, content
    is_active = db.Column(db.Boolean, default=True)
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    clicks = db.Column(db.Integer, default=0)
    impressions = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class SEOSetting(db.Model):
    __tablename__ = 'seo_settings'
    
    id = db.Column(db.Integer, primary_key=True)
    page_slug = db.Column(db.String(100), unique=True, nullable=False)
    meta_title = db.Column(db.String(200))
    meta_description = db.Column(db.Text)
    meta_keywords = db.Column(db.Text)
    og_title = db.Column(db.String(200))
    og_description = db.Column(db.Text)
    og_image = db.Column(db.String(500))
    schema_markup = db.Column(db.Text)
    canonical_url = db.Column(db.String(500))
    robots_meta = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    reviewed_by = db.Column(db.String(200))  # Admin who reviewed
    
    # Agreement and terms
    terms_accepted = db.Column(db.Boolean, default=False)
    privacy_policy_url = db.Column(db.String(500))
    terms_of_service_url = db.Column(db.String(500))
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def get_features_list(self):
        return json.loads(self.app_features) if self.app_features else []
    
    def set_features_list(self, features):
        self.app_features = json.dumps(features)
    
    def get_screenshots_list(self):
        return json.loads(self.app_screenshots) if self.app_screenshots else []
    
    def set_screenshots_list(self, screenshots):
        self.app_screenshots = json.dumps(screenshots)
    
    def get_permissions_list(self):
        return json.loads(self.permissions_required) if self.permissions_required else []
    
    def set_permissions_list(self, permissions):
        self.permissions_required = json.dumps(permissions)

# Matrimony App Models
class MatrimonyProfile(db.Model):
    __tablename__ = 'matrimony_profiles'
    
    id = db.Column(db.Integer, primary_key=True)
    
    # Basic Information
    full_name = db.Column(db.String(200), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)  # Male, Female, Other
    marital_status = db.Column(db.String(20), nullable=False)  # single, divorced, widowed
    relationship_type = db.Column(db.String(30), nullable=False)  # marriage, open, livein
    
    # Profile Details
    height = db.Column(db.String(10))  # e.g., "5'8\""
    weight = db.Column(db.String(10))  # e.g., "65kg"
    body_type = db.Column(db.String(20))  # slim, average, athletic, etc.
    complexion = db.Column(db.String(20))  # fair, medium, dark
    physical_status = db.Column(db.String(20))  # normal, differently_abled
    
    # Location
    city = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), default='India')
    
    # Education & Career
    education = db.Column(db.String(200))
    occupation = db.Column(db.String(200))
    annual_income = db.Column(db.String(50))  # e.g., "5-10 Lakhs"
    company_name = db.Column(db.String(200))
    
    # Family
    family_type = db.Column(db.String(20))  # nuclear, joint
    father_occupation = db.Column(db.String(100))
    mother_occupation = db.Column(db.String(100))
    siblings = db.Column(db.String(100))  # e.g., "1 brother, 1 sister"
    
    # Lifestyle & Preferences
    religion = db.Column(db.String(50))
    caste = db.Column(db.String(100))
    sub_caste = db.Column(db.String(100))
    mother_tongue = db.Column(db.String(50))
    diet = db.Column(db.String(20))  # vegetarian, non_vegetarian, vegan
    smoking = db.Column(db.String(20))  # never, occasionally, regularly
    drinking = db.Column(db.String(20))  # never, occasionally, regularly
    
    # About & Bio
    bio = db.Column(db.Text)
    hobbies = db.Column(db.Text)  # JSON array
    interests = db.Column(db.Text)  # JSON array
    
    # Partner Preferences
    partner_age_min = db.Column(db.Integer)
    partner_age_max = db.Column(db.Integer)
    partner_height_min = db.Column(db.String(10))
    partner_height_max = db.Column(db.String(10))
    partner_education = db.Column(db.Text)  # JSON array of preferred education levels
    partner_occupation = db.Column(db.Text)  # JSON array of preferred occupations
    partner_income_min = db.Column(db.String(50))
    partner_location = db.Column(db.Text)  # JSON array of preferred locations
    partner_caste = db.Column(db.Text)  # JSON array of acceptable castes
    
    # Contact Information
    email = db.Column(db.String(200), unique=True, nullable=False)
    phone = db.Column(db.String(20))
    whatsapp = db.Column(db.String(20))
    
    # Profile Images (up to 5)
    profile_images = db.Column(db.Text)  # JSON array of image URLs
    profile_photo = db.Column(db.String(500))  # main profile photo
    
    # Account Status
    is_verified = db.Column(db.Boolean, default=False)
    verification_documents = db.Column(db.Text)  # JSON array of document paths
    premium_member = db.Column(db.Boolean, default=False)
    membership_badge = db.Column(db.String(20), default='basic')  # basic, silver, gold, platinum
    membership_expires = db.Column(db.DateTime)
    
    # Privacy Settings
    contact_visible = db.Column(db.Boolean, default=False)
    photo_visible = db.Column(db.Boolean, default=True)
    profile_visible = db.Column(db.Boolean, default=True)
    photo_blurred = db.Column(db.Boolean, default=False)
    photo_blur_date = db.Column(db.DateTime)
    
    # Activity
    last_active = db.Column(db.DateTime, default=datetime.utcnow)
    profile_views = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Follow/Share functionality
    followers_count = db.Column(db.Integer, default=0)
    following_count = db.Column(db.Integer, default=0)
    shares_count = db.Column(db.Integer, default=0)
    
    # Password for login
    password_hash = db.Column(db.String(256))
    
    def set_password(self, password):
        """Set password hash"""
        from werkzeug.security import generate_password_hash
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        """Check password"""
        from werkzeug.security import check_password_hash
        return check_password_hash(self.password_hash, password)
    
    def get_profile_images(self):
        if not self.profile_images:
            return []
        try:
            return json.loads(self.profile_images)
        except (json.JSONDecodeError, ValueError):
            return []
    
    def check_photo_blur_status(self):
        """Check if basic member photos should be blurred after 10 days"""
        if self.membership_badge == 'basic' and self.created_at:
            days_since_creation = (datetime.utcnow() - self.created_at).days
            if days_since_creation > 10:
                self.photo_blurred = True
                if not self.photo_blur_date:
                    self.photo_blur_date = datetime.utcnow()
                return True
        return False
    
    def set_profile_images(self, images_list):
        self.profile_images = json.dumps(images_list)
    
    def get_hobbies(self):
        return json.loads(self.hobbies) if self.hobbies else []
    
    def set_hobbies(self, hobbies_list):
        self.hobbies = json.dumps(hobbies_list)
    
    def get_interests(self):
        return json.loads(self.interests) if self.interests else []
    
    def set_interests(self, interests_list):
        self.interests = json.dumps(interests_list)

class MatrimonyInteraction(db.Model):
    __tablename__ = 'matrimony_interactions'
    
    id = db.Column(db.Integer, primary_key=True)
    from_profile_id = db.Column(db.Integer, db.ForeignKey('matrimony_profiles.id'), nullable=False)
    to_profile_id = db.Column(db.Integer, db.ForeignKey('matrimony_profiles.id'), nullable=False)
    interaction_type = db.Column(db.String(20), nullable=False)  # like, dislike, view, shortlist, block
    message = db.Column(db.Text)  # optional message with interest
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    from_profile = db.relationship('MatrimonyProfile', foreign_keys=[from_profile_id], backref='sent_interactions')
    to_profile = db.relationship('MatrimonyProfile', foreign_keys=[to_profile_id], backref='received_interactions')
