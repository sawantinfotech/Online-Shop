import os
import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from werkzeug.middleware.proxy_fix import ProxyFix

# Configure logging
logging.basicConfig(level=logging.DEBUG)

class Base(DeclarativeBase):
    pass

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "mobile-shop-secret-key")
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

# Database configuration
database_url = os.environ.get("DATABASE_URL")

if database_url:
    app.config["SQLALCHEMY_DATABASE_URI"] = database_url
    app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
        "pool_recycle": 300,
        "pool_pre_ping": True,
    }
    logging.info("Using PostgreSQL database")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mobile_shop.db"
    logging.info("Using SQLite database")

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# File upload configuration
app.config["UPLOAD_FOLDER"] = "uploads"
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024  # 16MB max file size

# Initialize database
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Create upload directory if it doesn't exist
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

with app.app_context():
    # Import models to create tables
    import models  # noqa: F401
    import json
    
    # Add JSON filter for templates
    app.jinja_env.filters['from_json'] = json.loads
    
    db.create_all()
    logging.info("Database tables created")
    
    # Register admin blueprint
    from admin import admin_bp
    app.register_blueprint(admin_bp)
    
    # Initialize default categories and demo data
    from models import *
    from datetime import datetime, timedelta
    import random
    
    # Auto-populate demo data on startup for immediate showcase
    if Category.query.count() == 0:
        logging.info("Populating demo data for immediate showcase...")
        
        # Categories
        categories = [
            Category(name='Electronics', description='Electronic devices and accessories'),
            Category(name='Fashion', description='Apparel and fashion items'), 
            Category(name='Home & Garden', description='Home improvement and gardening'),
            Category(name='Sports', description='Sports equipment and accessories'),
            Category(name='Books', description='Educational and entertainment books'),
            Category(name='Health', description='Health and wellness products'),
            Category(name='Automotive', description='Car accessories and parts'),
            Category(name='Food', description='Food delivery and catering'),
            Category(name='Books', description='Books and educational materials'),
            Category(name='Health & Beauty', description='Health and beauty products'),
            Category(name='Food & Beverages', description='Food items and beverages'),
            Category(name='Other', description='Other products')
        ]
        
        for category in categories:
            db.session.add(category)
        db.session.commit()
        
        # Demo Businesses
        businesses_data = [
            {'business_name': 'TechMart Electronics', 'email': 'contact@techmart.com', 'contact_number': '+91-9876543210', 'business_type': 'Electronics Store', 'address': '123 Tech Street, Mumbai', 'verification_status': 'verified', 'gpay_enabled': True, 'paytm_enabled': True},
            {'business_name': 'Fashion Hub', 'email': 'hello@fashionhub.com', 'contact_number': '+91-9876543211', 'business_type': 'Fashion Store', 'address': '456 Fashion Avenue, Delhi', 'verification_status': 'verified', 'gpay_enabled': True, 'paytm_enabled': True},
            {'business_name': 'HomeDecor Plus', 'email': 'info@homedecor.com', 'contact_number': '+91-9876543212', 'business_type': 'Home & Garden', 'address': '789 Home Street, Bangalore', 'verification_status': 'verified', 'gpay_enabled': True, 'paytm_enabled': False},
            {'business_name': 'SportZone', 'email': 'contact@sportzone.com', 'contact_number': '+91-9876543213', 'business_type': 'Sports Store', 'address': '321 Sports Complex, Chennai', 'verification_status': 'verified', 'gpay_enabled': True, 'paytm_enabled': True},
            {'business_name': 'BookWorm Library', 'email': 'books@bookworm.com', 'contact_number': '+91-9876543214', 'business_type': 'Bookstore', 'address': '654 Knowledge Street, Pune', 'verification_status': 'verified', 'gpay_enabled': False, 'paytm_enabled': True}
        ]
        
        for bus_data in businesses_data:
            business = Business(**bus_data)
            business.set_password('demo123')
            db.session.add(business)
        db.session.commit()
        
        # Demo Products
        products_data = [
            {'product_name': 'iPhone 15 Pro', 'description': 'Latest Apple smartphone', 'price': 999.99, 'quantity': 50, 'category_id': 1, 'business_id': 1},
            {'product_name': 'Samsung Galaxy S24', 'description': 'Premium Android smartphone', 'price': 899.99, 'quantity': 30, 'category_id': 1, 'business_id': 1},
            {'product_name': 'MacBook Air M3', 'description': 'Ultra-portable laptop', 'price': 1299.99, 'quantity': 20, 'category_id': 1, 'business_id': 1},
            {'product_name': 'Designer Jeans', 'description': 'Premium denim jeans', 'price': 129.99, 'quantity': 100, 'category_id': 2, 'business_id': 2},
            {'product_name': 'Cotton T-Shirt', 'description': 'Comfortable cotton t-shirt', 'price': 29.99, 'quantity': 200, 'category_id': 2, 'business_id': 2},
            {'product_name': 'Sofa Set', 'description': '3-piece comfortable sofa set', 'price': 899.99, 'quantity': 15, 'category_id': 3, 'business_id': 3},
            {'product_name': 'Cricket Bat', 'description': 'Professional cricket bat', 'price': 199.99, 'quantity': 40, 'category_id': 4, 'business_id': 4},
            {'product_name': 'Python Programming Guide', 'description': 'Comprehensive Python guide', 'price': 59.99, 'quantity': 75, 'category_id': 5, 'business_id': 5}
        ]
        
        for prod_data in products_data:
            product = Product(**prod_data)
            db.session.add(product)
        db.session.commit()
        
        # Demo Users
        users_data = [
            {'username': 'john_doe', 'email': 'john@example.com', 'full_name': 'John Doe', 'mobile': '+91-9876543220', 'phone_number': '+91-9876543220', 'address': '123 Main Street, Mumbai', 'user_type': 'subscriber', 'verification_status': 'verified'},
            {'username': 'jane_smith', 'email': 'jane@example.com', 'full_name': 'Jane Smith', 'mobile': '+91-9876543221', 'phone_number': '+91-9876543221', 'address': '456 Oak Avenue, Delhi', 'user_type': 'subscriber', 'verification_status': 'verified'},
            {'username': 'admin_user', 'email': 'admin@mobileshop.com', 'full_name': 'Admin User', 'mobile': '+91-9876543222', 'phone_number': '+91-9876543222', 'address': 'Admin Office', 'user_type': 'admin', 'role': 'super_admin', 'verification_status': 'verified'}
        ]
        
        for user_data in users_data:
            user = User(**user_data)
            user.set_password('demo123')
            db.session.add(user)
        db.session.commit()
        
        # Demo Apps
        apps_data = [
            {'name': 'Food Delivery Pro', 'slug': 'food-delivery-pro', 'short_description': 'Professional food delivery app', 'category': 'Food & Dining', 'author_name': 'FoodTech', 'rating': 4.8, 'downloads': 15000, 'status': 'active', 'featured': True},
            {'name': 'Fitness Tracker', 'slug': 'fitness-tracker', 'short_description': 'Complete fitness tracking app', 'category': 'Health & Fitness', 'author_name': 'HealthTech', 'rating': 4.6, 'downloads': 25000, 'status': 'active', 'featured': True},
            {'name': 'Shopping Assistant', 'slug': 'shopping-assistant', 'short_description': 'AI-powered shopping assistant', 'category': 'Shopping', 'author_name': 'ShopSmart', 'rating': 4.7, 'downloads': 30000, 'status': 'active'},
            {'name': 'Learning Hub', 'slug': 'learning-hub', 'short_description': 'Educational platform', 'category': 'Education', 'author_name': 'EduTech', 'rating': 4.9, 'downloads': 45000, 'status': 'active', 'featured': True},
            {'name': 'Travel Planner', 'slug': 'travel-planner', 'short_description': 'Travel planning app', 'category': 'Travel', 'author_name': 'TravelTech', 'rating': 4.5, 'downloads': 20000, 'status': 'active'}
        ]
        
        for app_data in apps_data:
            app_item = App(**app_data)
            db.session.add(app_item)
        db.session.commit()
        
        # Demo Delivery Profiles
        users = User.query.filter_by(user_type='subscriber').all()
        if users:
            delivery_data = [
                {'user_id': users[0].id, 'driving_license': 'DL001234567890', 'delivery_zone': 'local', 'is_available': True, 'rating': 4.8, 'total_deliveries': 150, 'status': 'active', 'verification_status': 'verified', 'registration_fee_paid': True},
                {'user_id': users[1].id if len(users) > 1 else users[0].id, 'driving_license': 'DL001234567891', 'delivery_zone': 'outdoor', 'is_available': True, 'rating': 4.9, 'total_deliveries': 200, 'status': 'active', 'verification_status': 'verified', 'registration_fee_paid': True}
            ]
            
            for del_data in delivery_data:
                delivery = DeliveryProfile(**del_data)
                db.session.add(delivery)
            db.session.commit()
        
        # Demo Matrimony Profiles
        matrimony_data = [
            {'first_name': 'Priya', 'last_name': 'Sharma', 'email': 'priya@example.com', 'phone_number': '+91-9876543230', 'date_of_birth': datetime(1995, 5, 15), 'age': 29, 'gender': 'Female', 'location': 'Mumbai', 'height': '5.4 ft', 'education': 'MBA', 'occupation': 'Software Engineer', 'status': 'active', 'membership_type': 'premium', 'profile_visible': True},
            {'first_name': 'Rahul', 'last_name': 'Kumar', 'email': 'rahul@example.com', 'phone_number': '+91-9876543231', 'date_of_birth': datetime(1992, 8, 20), 'age': 32, 'gender': 'Male', 'location': 'Delhi', 'height': '5.8 ft', 'education': 'B.Tech', 'occupation': 'Data Scientist', 'status': 'active', 'membership_type': 'basic', 'profile_visible': True},
            {'first_name': 'Anita', 'last_name': 'Patel', 'email': 'anita@example.com', 'phone_number': '+91-9876543232', 'date_of_birth': datetime(1994, 12, 10), 'age': 30, 'gender': 'Female', 'location': 'Bangalore', 'height': '5.3 ft', 'education': 'M.Sc', 'occupation': 'Research Scientist', 'status': 'active', 'membership_type': 'premium', 'profile_visible': True},
            {'first_name': 'Vikram', 'last_name': 'Singh', 'email': 'vikram@example.com', 'phone_number': '+91-9876543233', 'date_of_birth': datetime(1990, 3, 25), 'age': 34, 'gender': 'Male', 'location': 'Chennai', 'height': '6.0 ft', 'education': 'CA', 'occupation': 'Chartered Accountant', 'status': 'active', 'membership_type': 'gold', 'profile_visible': True},
            {'first_name': 'Meera', 'last_name': 'Joshi', 'email': 'meera@example.com', 'phone_number': '+91-9876543234', 'date_of_birth': datetime(1996, 7, 8), 'age': 28, 'gender': 'Female', 'location': 'Pune', 'height': '5.2 ft', 'education': 'BDS', 'occupation': 'Dentist', 'status': 'active', 'membership_type': 'basic', 'profile_visible': True}
        ]
        
        for mat_data in matrimony_data:
            matrimony = MatrimonyProfile(**mat_data)
            db.session.add(matrimony)
        db.session.commit()
        
        logging.info("✅ Demo data populated successfully!")
