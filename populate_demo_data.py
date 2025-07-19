#!/usr/bin/env python3
"""
Comprehensive Demo Data Population Script
Populates all tables with realistic demo data for immediate showcase
"""

import os
import sys
from datetime import datetime, timedelta
import random
from werkzeug.security import generate_password_hash

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import app, db
from models import *

def populate_demo_data():
    """Populate database with comprehensive demo data"""
    
    with app.app_context():
        # Clear existing data
        print("Clearing existing data...")
        
        # Create all tables first
        db.create_all()
        
        # Only clear demo data if it doesn't exist, to avoid conflicts
        if Category.query.count() == 0:
            print("Adding Categories...")
            categories_data = [
                {'name': 'Electronics', 'description': 'Mobile phones, laptops, gadgets'},
                {'name': 'Fashion', 'description': 'Clothing, accessories, footwear'},
                {'name': 'Home & Garden', 'description': 'Furniture, decor, gardening'},
                {'name': 'Sports', 'description': 'Sports equipment and fitness gear'},
                {'name': 'Books', 'description': 'Educational and entertainment books'},
                {'name': 'Health', 'description': 'Health and wellness products'},
                {'name': 'Automotive', 'description': 'Car accessories and parts'},
                {'name': 'Food', 'description': 'Food delivery and catering'},
            ]
            
            for cat_data in categories_data:
                category = Category(**cat_data)
                db.session.add(category)
            db.session.commit()
        
        # Add Demo Businesses
        if Business.query.count() == 0:
            print("Adding Demo Businesses...")
            businesses_data = [
                {
                    'business_name': 'TechMart Electronics',
                    'email': 'contact@techmart.com',
                    'contact_number': '+91-9876543210',
                    'business_type': 'Electronics Store',
                    'address': '123 Tech Street, Mumbai, Maharashtra',
                    'verification_status': 'verified',
                    'gpay_enabled': True,
                    'paytm_enabled': True,
                    'brainlo_enabled': False
                },
                {
                    'business_name': 'Fashion Hub',
                    'email': 'hello@fashionhub.com',
                    'contact_number': '+91-9876543211',
                    'business_type': 'Fashion Store',
                    'address': '456 Fashion Avenue, Delhi, Delhi',
                    'verification_status': 'verified',
                    'gpay_enabled': True,
                    'paytm_enabled': True,
                    'brainlo_enabled': True
                },
                {
                    'business_name': 'HomeDecor Plus',
                    'email': 'info@homedecor.com',
                    'contact_number': '+91-9876543212',
                    'business_type': 'Home & Garden',
                    'address': '789 Home Street, Bangalore, Karnataka',
                    'verification_status': 'verified',
                    'gpay_enabled': True,
                    'paytm_enabled': False,
                    'brainlo_enabled': True
                },
                {
                    'business_name': 'SportZone',
                    'email': 'contact@sportzone.com',
                    'contact_number': '+91-9876543213',
                    'business_type': 'Sports Store',
                    'address': '321 Sports Complex, Chennai, Tamil Nadu',
                    'verification_status': 'verified',
                    'gpay_enabled': True,
                    'paytm_enabled': True,
                    'brainlo_enabled': True
                },
                {
                    'business_name': 'BookWorm Library',
                    'email': 'books@bookworm.com',
                    'contact_number': '+91-9876543214',
                    'business_type': 'Bookstore',
                    'address': '654 Knowledge Street, Pune, Maharashtra',
                    'verification_status': 'verified',
                    'gpay_enabled': False,
                    'paytm_enabled': True,
                    'brainlo_enabled': True
                }
            ]
            
            for bus_data in businesses_data:
                business = Business(**bus_data)
                business.set_password('demo123')
                db.session.add(business)
            db.session.commit()
        
        # Add Demo Products
        if Product.query.count() == 0:
            print("Adding Demo Products...")
            categories = Category.query.all()
            businesses = Business.query.all()
            
            products_data = [
                # Electronics
                {'product_name': 'iPhone 15 Pro', 'description': 'Latest Apple smartphone with advanced features', 'price': 999.99, 'quantity': 50, 'category_id': 1, 'business_id': 1},
                {'product_name': 'Samsung Galaxy S24', 'description': 'Premium Android smartphone', 'price': 899.99, 'quantity': 30, 'category_id': 1, 'business_id': 1},
                {'product_name': 'MacBook Air M3', 'description': 'Ultra-portable laptop with M3 chip', 'price': 1299.99, 'quantity': 20, 'category_id': 1, 'business_id': 1},
                {'product_name': 'Sony WH-1000XM5', 'description': 'Wireless noise-canceling headphones', 'price': 399.99, 'quantity': 75, 'category_id': 1, 'business_id': 1},
                
                # Fashion
                {'product_name': 'Designer Jeans', 'description': 'Premium denim jeans with modern fit', 'price': 129.99, 'quantity': 100, 'category_id': 2, 'business_id': 2},
                {'product_name': 'Cotton T-Shirt', 'description': 'Comfortable cotton t-shirt in multiple colors', 'price': 29.99, 'quantity': 200, 'category_id': 2, 'business_id': 2},
                {'product_name': 'Leather Jacket', 'description': 'Genuine leather jacket for style and comfort', 'price': 299.99, 'quantity': 25, 'category_id': 2, 'business_id': 2},
                {'product_name': 'Running Shoes', 'description': 'Professional running shoes with cushioning', 'price': 159.99, 'quantity': 80, 'category_id': 2, 'business_id': 2},
                
                # Home & Garden
                {'product_name': 'Sofa Set', 'description': '3-piece comfortable sofa set for living room', 'price': 899.99, 'quantity': 15, 'category_id': 3, 'business_id': 3},
                {'product_name': 'Dining Table', 'description': '6-seater wooden dining table', 'price': 499.99, 'quantity': 10, 'category_id': 3, 'business_id': 3},
                {'product_name': 'Garden Plant Set', 'description': 'Collection of indoor plants for home decoration', 'price': 79.99, 'quantity': 50, 'category_id': 3, 'business_id': 3},
                
                # Sports
                {'product_name': 'Cricket Bat', 'description': 'Professional cricket bat made from English willow', 'price': 199.99, 'quantity': 40, 'category_id': 4, 'business_id': 4},
                {'product_name': 'Football', 'description': 'FIFA approved football for professional matches', 'price': 49.99, 'quantity': 60, 'category_id': 4, 'business_id': 4},
                {'product_name': 'Yoga Mat', 'description': 'Premium yoga mat for fitness and meditation', 'price': 39.99, 'quantity': 100, 'category_id': 4, 'business_id': 4},
                
                # Books
                {'product_name': 'Python Programming Guide', 'description': 'Comprehensive guide to Python programming', 'price': 59.99, 'quantity': 75, 'category_id': 5, 'business_id': 5},
                {'product_name': 'Web Development Handbook', 'description': 'Complete handbook for modern web development', 'price': 79.99, 'quantity': 50, 'category_id': 5, 'business_id': 5},
            ]
            
            for prod_data in products_data:
                product = Product(**prod_data)
                db.session.add(product)
            db.session.commit()
        
        # Add Demo Users
        if User.query.count() == 0:
            print("Adding Demo Users...")
            users_data = [
                {
                    'username': 'john_doe',
                    'email': 'john@example.com',
                    'full_name': 'John Doe',
                    'mobile': '+91-9876543220',
                    'phone_number': '+91-9876543220',
                    'address': '123 Main Street, Mumbai',
                    'user_type': 'subscriber',
                    'role': 'user',
                    'subscription_plan': 'free',
                    'verification_status': 'verified'
                },
                {
                    'username': 'jane_smith',
                    'email': 'jane@example.com',
                    'full_name': 'Jane Smith',
                    'mobile': '+91-9876543221',
                    'phone_number': '+91-9876543221',
                    'address': '456 Oak Avenue, Delhi',
                    'user_type': 'subscriber',
                    'role': 'user',
                    'subscription_plan': 'silver',
                    'verification_status': 'verified'
                },
                {
                    'username': 'admin_user',
                    'email': 'admin@mobileshop.com',
                    'full_name': 'Admin User',
                    'mobile': '+91-9876543222',
                    'phone_number': '+91-9876543222',
                    'address': 'Admin Office',
                    'user_type': 'admin',
                    'role': 'super_admin',
                    'subscription_plan': 'platinum',
                    'verification_status': 'verified'
                }
            ]
            
            for user_data in users_data:
                user = User(**user_data)
                user.set_password('demo123')
                db.session.add(user)
            db.session.commit()
        
        # Add Demo Apps
        if db.session.execute(db.text("SELECT COUNT(*) FROM apps")).scalar() == 0:
            print("Adding Demo Apps...")
            apps_data = [
                {
                    'name': 'Food Delivery Pro',
                    'slug': 'food-delivery-pro',
                    'short_description': 'Professional food delivery application with real-time tracking',
                    'long_description': 'Complete food delivery solution with GPS tracking, multiple payment options, and restaurant partnerships',
                    'category': 'Food & Dining',
                    'author_name': 'FoodTech Solutions',
                    'author_email': 'contact@foodtech.com',
                    'rating': 4.8,
                    'downloads': 15000,
                    'logo_url': '/static/images/food-app.png',
                    'status': 'active',
                    'featured': True
                },
                {
                    'name': 'Fitness Tracker',
                    'slug': 'fitness-tracker',
                    'short_description': 'Complete fitness tracking app with workout plans and nutrition',
                    'long_description': 'Advanced fitness tracking with personalized workouts, nutrition plans, and progress analytics',
                    'category': 'Health & Fitness',
                    'author_name': 'HealthTech Inc',
                    'author_email': 'info@healthtech.com',
                    'rating': 4.6,
                    'downloads': 25000,
                    'logo_url': '/static/images/fitness-app.png',
                    'status': 'active',
                    'featured': True
                },
                {
                    'name': 'Shopping Assistant',
                    'slug': 'shopping-assistant',
                    'short_description': 'AI-powered shopping assistant for best deals and recommendations',
                    'long_description': 'Smart shopping companion with price comparison, deal alerts, and personalized recommendations',
                    'category': 'Shopping',
                    'author_name': 'ShopSmart Technologies',
                    'author_email': 'support@shopsmart.com',
                    'rating': 4.7,
                    'downloads': 30000,
                    'logo_url': '/static/images/shopping-app.png',
                    'status': 'active',
                    'featured': False
                },
                {
                    'name': 'Learning Hub',
                    'slug': 'learning-hub',
                    'short_description': 'Educational platform with courses and certifications',
                    'long_description': 'Comprehensive learning platform with video courses, quizzes, and professional certifications',
                    'category': 'Education',
                    'author_name': 'EduTech Solutions',
                    'author_email': 'hello@edutech.com',
                    'rating': 4.9,
                    'downloads': 45000,
                    'logo_url': '/static/images/education-app.png',
                    'status': 'active',
                    'featured': True
                },
                {
                    'name': 'Travel Planner',
                    'slug': 'travel-planner',
                    'short_description': 'Complete travel planning app with booking and itinerary management',
                    'long_description': 'All-in-one travel solution with flight booking, hotel reservations, and trip planning',
                    'category': 'Travel',
                    'author_name': 'TravelTech Pro',
                    'author_email': 'booking@traveltech.com',
                    'rating': 4.5,
                    'downloads': 20000,
                    'logo_url': '/static/images/travel-app.png',
                    'status': 'active',
                    'featured': False
                }
            ]
            
            for app_data in apps_data:
                app = App(**app_data)
                db.session.add(app)
            db.session.commit()
        
        # Add Demo Delivery Profiles
        users = User.query.filter_by(user_type='subscriber').all()
        if DeliveryProfile.query.count() == 0 and users:
            print("Adding Demo Delivery Profiles...")
            delivery_data = [
                {
                    'user_id': users[0].id,
                    'driving_license': 'DL001234567890',
                    'aadhar_number': '1234-5678-9012',
                    'emergency_contact': '+91-9876543225',
                    'delivery_zone': 'local',
                    'is_available': True,
                    'rating': 4.8,
                    'total_deliveries': 150,
                    'status': 'active',
                    'verification_status': 'verified',
                    'registration_fee_paid': True
                },
                {
                    'user_id': users[1].id if len(users) > 1 else users[0].id,
                    'driving_license': 'DL001234567891',
                    'aadhar_number': '1234-5678-9013',
                    'emergency_contact': '+91-9876543226',
                    'delivery_zone': 'outdoor',
                    'is_available': True,
                    'rating': 4.9,
                    'total_deliveries': 200,
                    'status': 'active',
                    'verification_status': 'verified',
                    'registration_fee_paid': True
                }
            ]
            
            for del_data in delivery_data:
                delivery = DeliveryProfile(**del_data)
                db.session.add(delivery)
            db.session.commit()
        
        # Add Demo Matrimony Profiles
        if MatrimonyProfile.query.count() == 0:
            print("Adding Demo Matrimony Profiles...")
            matrimony_data = [
                {
                    'first_name': 'Priya',
                    'last_name': 'Sharma',
                    'email': 'priya@example.com',
                    'phone_number': '+91-9876543230',
                    'date_of_birth': datetime(1995, 5, 15),
                    'gender': 'Female',
                    'location': 'Mumbai',
                    'height': '5.4 ft',
                    'weight': '55 kg',
                    'education': 'MBA',
                    'occupation': 'Software Engineer',
                    'income': '8 LPA',
                    'religion': 'Hindu',
                    'caste': 'Brahmin',
                    'mother_tongue': 'Hindi',
                    'marital_status': 'Never Married',
                    'about_me': 'Looking for a caring and understanding life partner',
                    'looking_for': 'Well-educated and family-oriented person',
                    'interests': '["Reading", "Traveling", "Cooking", "Movies"]',
                    'status': 'active',
                    'membership_type': 'premium',
                    'photo_privacy': 'public'
                },
                {
                    'first_name': 'Rahul',
                    'last_name': 'Kumar',
                    'email': 'rahul@example.com',
                    'phone_number': '+91-9876543231',
                    'date_of_birth': datetime(1992, 8, 20),
                    'gender': 'Male',
                    'location': 'Delhi',
                    'height': '5.8 ft',
                    'weight': '70 kg',
                    'education': 'B.Tech',
                    'occupation': 'Data Scientist',
                    'income': '12 LPA',
                    'religion': 'Hindu',
                    'caste': 'Kshatriya',
                    'mother_tongue': 'Hindi',
                    'marital_status': 'Never Married',
                    'about_me': 'Technology enthusiast with traditional values',
                    'looking_for': 'Independent and career-oriented partner',
                    'interests': '["Technology", "Sports", "Music", "Photography"]',
                    'status': 'active',
                    'membership_type': 'basic',
                    'photo_privacy': 'public'
                },
                {
                    'first_name': 'Anita',
                    'last_name': 'Patel',
                    'email': 'anita@example.com',
                    'phone_number': '+91-9876543232',
                    'date_of_birth': datetime(1994, 12, 10),
                    'gender': 'Female',
                    'location': 'Bangalore',
                    'height': '5.3 ft',
                    'weight': '52 kg',
                    'education': 'M.Sc',
                    'occupation': 'Research Scientist',
                    'income': '10 LPA',
                    'religion': 'Hindu',
                    'caste': 'Patel',
                    'mother_tongue': 'Gujarati',
                    'marital_status': 'Never Married',
                    'about_me': 'Science enthusiast with creative mindset',
                    'looking_for': 'Intellectual and supportive life partner',
                    'interests': '["Science", "Art", "Dancing", "Yoga"]',
                    'status': 'active',
                    'membership_type': 'premium',
                    'photo_privacy': 'blurred'
                },
                {
                    'first_name': 'Vikram',
                    'last_name': 'Singh',
                    'email': 'vikram@example.com',
                    'phone_number': '+91-9876543233',
                    'date_of_birth': datetime(1990, 3, 25),
                    'gender': 'Male',
                    'location': 'Chennai',
                    'height': '6.0 ft',
                    'weight': '75 kg',
                    'education': 'CA',
                    'occupation': 'Chartered Accountant',
                    'income': '15 LPA',
                    'religion': 'Hindu',
                    'caste': 'Rajput',
                    'mother_tongue': 'Hindi',
                    'marital_status': 'Never Married',
                    'about_me': 'Finance professional with adventurous spirit',
                    'looking_for': 'Understanding and ambitious partner',
                    'interests': '["Finance", "Adventure Sports", "Travel", "Books"]',
                    'status': 'active',
                    'membership_type': 'gold',
                    'photo_privacy': 'public'
                },
                {
                    'first_name': 'Meera',
                    'last_name': 'Joshi',
                    'email': 'meera@example.com',
                    'phone_number': '+91-9876543234',
                    'date_of_birth': datetime(1996, 7, 8),
                    'gender': 'Female',
                    'location': 'Pune',
                    'height': '5.2 ft',
                    'weight': '50 kg',
                    'education': 'BDS',
                    'occupation': 'Dentist',
                    'income': '6 LPA',
                    'religion': 'Hindu',
                    'caste': 'Brahmin',
                    'mother_tongue': 'Marathi',
                    'marital_status': 'Never Married',
                    'about_me': 'Healthcare professional with caring nature',
                    'looking_for': 'Kind-hearted and responsible person',
                    'interests': '["Healthcare", "Classical Music", "Gardening", "Volunteering"]',
                    'status': 'active',
                    'membership_type': 'basic',
                    'photo_privacy': 'public'
                }
            ]
            
            for mat_data in matrimony_data:
                # Calculate age
                age = datetime.now().year - mat_data['date_of_birth'].year
                mat_data['age'] = age
                
                matrimony = MatrimonyProfile(**mat_data)
                db.session.add(matrimony)
            db.session.commit()
        
        # Add Demo Customers
        businesses = Business.query.all()
        if Customer.query.count() == 0 and businesses:
            print("Adding Demo Customers...")
            customers_data = [
                {
                    'business_id': businesses[0].id,
                    'name': 'Alice Johnson',
                    'phone_number': '+91-9876543240',
                    'email': 'alice@example.com',
                    'address': '789 Customer Street, Mumbai'
                },
                {
                    'business_id': businesses[1].id if len(businesses) > 1 else businesses[0].id,
                    'name': 'Bob Wilson',
                    'phone_number': '+91-9876543241',
                    'email': 'bob@example.com',
                    'address': '321 Client Avenue, Delhi'
                },
                {
                    'business_id': businesses[2].id if len(businesses) > 2 else businesses[0].id,
                    'name': 'Carol Brown',
                    'phone_number': '+91-9876543242',
                    'email': 'carol@example.com',
                    'address': '654 Buyer Lane, Bangalore'
                }
            ]
            
            for cust_data in customers_data:
                customer = Customer(**cust_data)
                db.session.add(customer)
            db.session.commit()
        
        print("✅ Demo data population completed successfully!")
        print(f"Categories: {Category.query.count()}")
        print(f"Businesses: {Business.query.count()}")
        print(f"Products: {Product.query.count()}")
        print(f"Users: {User.query.count()}")
        print(f"Matrimony Profiles: {MatrimonyProfile.query.count()}")
        print(f"Delivery Profiles: {DeliveryProfile.query.count()}")
        print(f"Customers: {Customer.query.count()}")

if __name__ == "__main__":
    populate_demo_data()