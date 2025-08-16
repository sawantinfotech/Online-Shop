from datetime import datetime
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
import json

# BUSINESS SERVICE DISCONNECTED
# Business model moved to business/business_models.py for isolation
# All business-related functionality has been disconnected from main application

class Service(db.Model):
    __tablename__ = 'services'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    category = db.Column(db.String(50))  # Technology, Healthcare, Finance, etc.
    status = db.Column(db.String(20), default='pending')  # pending, approved, rejected, active, inactive
    service_type = db.Column(db.String(20), default='standard')  # standard, premium, enterprise
    requested_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    pricing_type = db.Column(db.String(20), default='freemium')  # free, freemium, paid
    free_trial_days = db.Column(db.Integer, default=7)
    monthly_price = db.Column(db.Float, default=0.0)
    yearly_price = db.Column(db.Float, default=0.0)
    features = db.Column(db.Text)  # JSON string of features
    icon = db.Column(db.String(200))  # Font Awesome icon class
    image_url = db.Column(db.String(500))  # Service image
    is_featured = db.Column(db.Boolean, default=False)
    usage_count = db.Column(db.Integer, default=0)
    rating = db.Column(db.Float, default=0.0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    # products = db.relationship('Product', backref='service', lazy=True)
    # service_usages = db.relationship('ServiceUsage', backref='service', lazy=True)
    
    def get_features(self):
        return json.loads(self.features) if self.features else []
    
    def set_features(self, features_list):
        self.features = json.dumps(features_list)
  
# BUSINESS SERVICE DISCONNECTED - Product model moved to business folder
# Stub models for compatibility
class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, default=0.0)
    status = db.Column(db.String(20), default='active')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(20), default='pending')
    total_amount = db.Column(db.Float, default=0.0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Payment(db.Model):
    __tablename__ = 'payments'
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, default=0.0)
    status = db.Column(db.String(20), default='pending')
    payment_method = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


# BUSINESS SERVICE DISCONNECTED - SMSTemplate model moved to business folder
# class SMSTemplate - REMOVED (business-dependent)

# New models for enhanced features

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256))
    full_name = db.Column(db.String(200))
    mobile = db.Column(db.String(15))
    profile_photo = db.Column(db.String(500))
    phone_number = db.Column(db.String(15))
    address = db.Column(db.Text)
    gender = db.Column(db.String(10))  # male, female, other
    user_type = db.Column(db.String(20), default='subscriber')  # subscriber, admin
    is_online = db.Column(db.Boolean, default=False)
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    role = db.Column(db.String(20), default='user')  # user, manager, admin, super_admin
    # business_id = db.Column(db.Integer, db.ForeignKey('businesses.id'))  # BUSINESS SERVICE DISCONNECTED
    credit_points = db.Column(db.Integer, default=0)
    subscription_plan = db.Column(db.String(50), default='free')
    custom_homepage = db.Column(db.Boolean, default=False)
    verification_status = db.Column(db.String(20), default='pending')
    verification_token = db.Column(db.String(100), unique=True)
    is_active = db.Column(db.Boolean, default=True)  # Added for admin panel compatibility
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    # reviews = db.relationship('Review', backref='user', lazy=True)
    # likes = db.relationship('Like', backref='user', lazy=True)
    # comments = db.relationship('Comment', backref='user', lazy=True)
    # followers = db.relationship('Follow', foreign_keys='Follow.followed_id', backref='followed', lazy='dynamic')
    # following = db.relationship('Follow', foreign_keys='Follow.follower_id', backref='follower', lazy='dynamic')
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def get_followers_count(self):
        # return self.followers.count()
        return 0  # Placeholder until Follow model is properly configured
    
    def get_following_count(self):
        # return self.following.count()
        return 0  # Placeholder until Follow model is properly configured

class Follow(db.Model):
    __tablename__ = 'follows'
    
    id = db.Column(db.Integer, primary_key=True)
    follower_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    followed_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# BUSINESS SERVICE DISCONNECTED - Like model moved to business folder
# class Like - REMOVED (business-dependent)

# BUSINESS SERVICE DISCONNECTED - Comment model moved to business folder
# class Comment - REMOVED (business-dependent)

# BUSINESS SERVICE DISCONNECTED - Review model moved to business folder
# class Review - REMOVED (business-dependent)

# BUSINESS SERVICE DISCONNECTED - Favorite model moved to business folder
# class Favorite - REMOVED (business-dependent)

# BUSINESS SERVICE DISCONNECTED - Advertisement model moved to business folder
# class Advertisement - REMOVED (business-dependent)

class PricingPlan(db.Model):
    __tablename__ = 'pricing_plans'
    
    id = db.Column(db.Integer, primary_key=True)
    service_id = db.Column(db.Integer, db.ForeignKey('services.id'), nullable=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    billing_cycle = db.Column(db.String(20))  # monthly, yearly
    duration = db.Column(db.String(50), default='monthly')  # monthly, yearly, lifetime
    features = db.Column(db.Text)  # JSON array of features
    max_products = db.Column(db.Integer, default=-1)  # -1 for unlimited
    max_orders = db.Column(db.Integer, default=-1)
    max_customers = db.Column(db.Integer, default=-1)
    custom_homepage = db.Column(db.Boolean, default=False)
    advanced_analytics = db.Column(db.Boolean, default=False)
    priority_support = db.Column(db.Boolean, default=False)
    is_featured = db.Column(db.Boolean, default=False)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    # service = db.relationship('Service', backref='pricing_plans')
    
    def get_features(self):
        return json.loads(self.features) if self.features else []
    
    def set_features(self, features_list):
        self.features = json.dumps(features_list)

class UserSubscription(db.Model):
    __tablename__ = 'user_subscriptions'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    # BUSINESS SERVICE DISCONNECTED - business_id reference removed
    # business_id = db.Column(db.Integer, db.ForeignKey('businesses.id'), nullable=False)
    
    plan_id = db.Column(db.Integer, db.ForeignKey('pricing_plans.id'), nullable=False)
    additional_info = db.Column(db.Text)
    amount = db.Column(db.Float, nullable=False, default=0.0)
    start_date = db.Column(db.DateTime, default=datetime.utcnow)
    end_date = db.Column(db.DateTime)
    status = db.Column(db.String(20), default='pending')  # pending, active, expired, cancelled
    payment_status = db.Column(db.String(20), default='pending')  # pending, completed, failed
    payment_method = db.Column(db.String(50))
    transaction_id = db.Column(db.String(100))
    started_at = db.Column(db.DateTime)
    expires_at = db.Column(db.DateTime)
    approved_at = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    # user = db.relationship('User', backref='subscriptions')
    # service = db.relationship('Service', backref='subscriptions')
    # plan = db.relationship('PricingPlan', backref='subscriptions')

class ServiceManager(db.Model):
    __tablename__ = 'service_managers'
    
    id = db.Column(db.Integer, primary_key=True)
    # BUSINESS SERVICE DISCONNECTED - business_id reference removed
    # business_id = db.Column(db.Integer, db.ForeignKey('businesses.id'), nullable=False)
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
    service_id = db.Column(db.Integer, db.ForeignKey('services.id'), nullable=True)  # If assigned to specific service
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
    # user = db.relationship('User', foreign_keys=[user_id], backref='delivery_profile')
    # service = db.relationship('service', backref='delivery_staff')
    # vehicles = db.relationship('DeliveryVehicle', backref='delivery_profile', lazy=True, foreign_keys='DeliveryVehicle.delivery_profile_id')
    # deliveries = db.relationship('DeliveryAssignment', backref='delivery_profile', lazy=True, foreign_keys='DeliveryAssignment.delivery_profile_id')

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
    # BUSINESS SERVICE DISCONNECTED - order_id reference removed
    # order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
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
    user_type = db.Column(db.String(20), nullable=False)  # service, user, delivery
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
    
    # App status and tracking
    status = db.Column(db.String(20), default='pending')  # active, inactive, pending
    featured = db.Column(db.Boolean, default=False)
    submitted_by = db.Column(db.Integer, db.ForeignKey('users.id'))  # Track who submitted the app
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
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # BUSINESS SERVICE DISCONNECTED - Changed from business_id to user_id
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
    
    # File verification method and authentication URLs
    verification_method = db.Column(db.String(50), default='upload')  # upload, github, store, website
    github_repo_url = db.Column(db.String(500))  # GitHub repository URL
    google_play_url = db.Column(db.String(500))  # Google Play Store URL
    apple_store_url = db.Column(db.String(500))  # Apple App Store URL
    official_website_url = db.Column(db.String(500))  # Official website download URL
    
    # App features and details
    app_features = db.Column(db.Text)  # JSON array of features
    target_audience = db.Column(db.String(200))
    app_size = db.Column(db.String(50))  # e.g., "25 MB"
    minimum_os_version = db.Column(db.String(50))
    permissions_required = db.Column(db.Text)  # JSON array
    
    # Pricing and monetization
    app_price = db.Column(db.String(50))  # "Free", "$2.99", etc.
    monetization_model = db.Column(db.String(100))  # "Free", "Paid", "Freemium", "Ad-supported"
    plan_type = db.Column(db.String(50), default='basic')  # "basic", "standard", "premium", "enterprise"
    
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

# App interaction models for favorites, follows, and shares
class AppFavorite(db.Model):
    __tablename__ = 'app_favorites'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    app_id = db.Column(db.Integer, db.ForeignKey('apps.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Ensure unique user-app combination
    __table_args__ = (db.UniqueConstraint('user_id', 'app_id', name='unique_user_app_favorite'),)

class DeveloperFollow(db.Model):
    __tablename__ = 'developer_follows'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    developer_email = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Ensure unique user-developer combination
    __table_args__ = (db.UniqueConstraint('user_id', 'developer_email', name='unique_user_developer_follow'),)

class AppShare(db.Model):
    __tablename__ = 'app_shares'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    app_id = db.Column(db.Integer, db.ForeignKey('apps.id'), nullable=False)
    platform = db.Column(db.String(50), nullable=False)  # facebook, twitter, whatsapp, email, etc.
    shared_at = db.Column(db.DateTime, default=datetime.utcnow)

class MatrimonyFollow(db.Model):
    __tablename__ = 'matrimony_follows'
    
    id = db.Column(db.Integer, primary_key=True)
    # BUSINESS SERVICE DISCONNECTED - business_id reference removed
    # business_id = db.Column(db.Integer, db.ForeignKey('businesses.id'), nullable=False)
    follower_id = db.Column(db.Integer, db.ForeignKey('matrimony_profiles.id'), nullable=False)
    followed_id = db.Column(db.Integer, db.ForeignKey('matrimony_profiles.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    # follower = db.relationship('MatrimonyProfile', foreign_keys=[follower_id], backref='following')
    # followed = db.relationship('MatrimonyProfile', foreign_keys=[followed_id], backref='followers')

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
    # BUSINESS SERVICE DISCONNECTED - business_id reference removed
    # business_id = db.Column(db.Integer, db.ForeignKey('businesses.id'), nullable=False)
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
    # BUSINESS SERVICE DISCONNECTED - business_id reference removed
    # business_id = db.Column(db.Integer, db.ForeignKey('businesses.id'), nullable=False)
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
    # BUSINESS SERVICE DISCONNECTED - business_id reference removed  
    # business_id = db.Column(db.Integer, db.ForeignKey('businesses.id'), nullable=False)
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

class ServiceUsage(db.Model):
    __tablename__ = 'service_usage'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey('services.id'), nullable=False)
    plan_type = db.Column(db.String(20), default='free_trial')  # free_trial, monthly, yearly
    status = db.Column(db.String(20), default='active')  # active, expired, cancelled
    started_at = db.Column(db.DateTime, default=datetime.utcnow)
    expires_at = db.Column(db.DateTime)
    usage_count = db.Column(db.Integer, default=0)
    last_used_at = db.Column(db.DateTime, default=datetime.utcnow)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)



# Matrimony App Models
class MatrimonyProfile(db.Model):
    __tablename__ = 'matrimony_profiles'
    
    id = db.Column(db.Integer, primary_key=True)
    # BUSINESS SERVICE DISCONNECTED - business_id reference removed
    # business_id = db.Column(db.Integer, db.ForeignKey('businesses.id'), nullable=False)
    # Basic Information
    first_name = db.Column(db.String(200), nullable=False)
    last_name = db.Column(db.String(200), nullable=False)
    date_of_birth = db.Column(db.String(200), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)  # Male, Female, Other
    language = db.Column(db.String(20), nullable=False)
    marital_status = db.Column(db.String(20), nullable=False)  # single, divorced, widowed, separated
    relationship_interest = db.Column(db.String(20), nullable=False)  # marriage, open, livein, party, dating, contract, sex4baby    
      
    # User Profile Details
    height = db.Column(db.String(10))  # e.g., "5'8\""
    weight = db.Column(db.String(10))  # e.g., "65kg"
    body_type = db.Column(db.String(20))  # slim, average, athletic, etc.
    complexion = db.Column(db.String(20))  # fair, medium, dark
    eye_color = db.Column(db.String(20)) # black, brown, gray, blue, green, hazelnut,
    hair_color = db.Column(db.String(20)) # black, brown, gray, blonde, red, white,
    skin_tone = db.Column(db.String(20)) # fair, light, medium, olive, dark, ebony,
    physical_disability = db.Column(db.String(20)) # blind, dum, deaf, spinalcord.
    mental_disability = db.Column(db.String(20)) # mental, depression, neuro, bipolar.
    blood_group = db.Column(db.String(20)) #  'A-', 'A+',  'B+', 'B-',  'AB+',   'AB-',  'O+' 'O-'.
    
    physical_status = db.Column(db.String(20))  # normal, differently_abled
    
    # User Location Details
    address = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    district = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(100), nullable=False)
    pincode = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), default='India')
    nationality = db.Column(db.String(100), nullable=False) # Buddhistan, Indian, American, British, Chinese, Rassian, Japanese.
    lives_in = db.Column(db.String(100), nullable=False)
    resident_status = db.Column(db.String(100), nullable=False)
    future_lives_in = db.Column(db.String(100), nullable=False)
    
    # User Education & Career
    education = db.Column(db.String(200))
    occupation = db.Column(db.String(200))
    annual_income = db.Column(db.String(50))  # e.g., "5-10 Lakhs"
    company_name = db.Column(db.String(200))
    
    # User Family Details
    family_type = db.Column(db.String(20))  # nuclear, joint
    father_occupation = db.Column(db.String(100))
    mother_occupation = db.Column(db.String(100))
    siblings = db.Column(db.String(100))  # e.g., "1 brother, 1 sister"
    social_group = db.Column(db.String(20))  # lower, middle, higher

    # Religious Preferences
    religion = db.Column(db.String(50))
    caste = db.Column(db.String(100))
    sub_caste = db.Column(db.String(100))
    gothra = db.Column(db.String(100))
    dosham = db.Column(db.String(100))
    star = db.Column(db.String(100))
    raasi = db.Column(db.String(100))
    horoscope = db.Column(db.String(100))

    # Lifestyle
    hobbies = db.Column(db.Text)  # JSON array
    diet = db.Column(db.String(20))  # vegetarian, non_vegetarian, vegan
    smoking = db.Column(db.String(20))  # never, occasionally, regularly
    drinking = db.Column(db.String(20))  # never, occasionally, regularly
    
    # About & Bio
    bio = db.Column(db.Text)
      
    # Partner Basic Preferences
    partner_age_min = db.Column(db.Integer)
    partner_age_max = db.Column(db.Integer)
    partner_height_min = db.Column(db.String(10))
    partner_height_max = db.Column(db.String(10))
    partner_gender = db.Column(db.String(10))
    partner_marital_status = db.Column(db.Text)
    partner_relationship_interest = db.Column(db.String(20))
    # Professional Preferences
    partner_education = db.Column(db.Text)  # JSON array of preferred education levels
    partner_occupation = db.Column(db.Text)  # JSON array of preferred occupations
    partner_income_min = db.Column(db.String(50))
    partner_location = db.Column(db.Text)  # JSON array of preferred locations
    # Religious Preferences
    partner_religion = db.Column(db.Text)
    partner_language = db.Column(db.Text)
    partner_caste = db.Column(db.Text)  # JSON array of acceptable castes
    
    # Contact Information
    email = db.Column(db.String(200), unique=True, nullable=False)
    mobile = db.Column(db.String(20), unique=True, nullable=False)
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
    # BUSINESS SERVICE DISCONNECTED - business_id reference removed
    # business_id = db.Column(db.Integer, db.ForeignKey('businesses.id'), nullable=False)
    from_profile_id = db.Column(db.Integer, db.ForeignKey('matrimony_profiles.id'), nullable=False)
    to_profile_id = db.Column(db.Integer, db.ForeignKey('matrimony_profiles.id'), nullable=False)
    interaction_type = db.Column(db.String(20), nullable=False)  # like, dislike, view, shortlist, block
    message = db.Column(db.Text)  # optional message with interest
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    # from_profile = db.relationship('MatrimonyProfile', foreign_keys=[from_profile_id], backref='sent_interactions')
    # to_profile = db.relationship('MatrimonyProfile', foreign_keys=[to_profile_id], backref='received_interactions')
