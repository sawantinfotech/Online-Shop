#!/usr/bin/env python3
"""
Create simple demo data for testing
"""

from app import app, db
from models import Business, Product, Category, User, App
from werkzeug.security import generate_password_hash
import random

def create_simple_demo_data():
    """Create basic demo data for testing"""
    
    with app.app_context():
        # Create demo businesses
        businesses_data = [
            {
                'name': 'TechGadget Store',
                'email': 'info@techgadget.com',
                'phone': '9876543210',
                'address': '123 Tech Street, Silicon Valley',
                'business_type': 'electronics',
                'verification_status': 'verified'
            },
            {
                'name': 'Fashion Hub',
                'email': 'contact@fashionhub.com',
                'phone': '9876543211',
                'address': '456 Fashion Ave, Mumbai',
                'business_type': 'clothing',
                'verification_status': 'verified'
            },
            {
                'name': 'Home Essentials',
                'email': 'hello@homeessentials.com',
                'phone': '9876543212',
                'address': '789 Home Lane, Delhi',
                'business_type': 'home_garden',
                'verification_status': 'verified'
            }
        ]
        
        for business_data in businesses_data:
            existing = Business.query.filter_by(email=business_data['email']).first()
            if not existing:
                business = Business(
                    name=business_data['name'],
                    email=business_data['email'],
                    phone=business_data['phone'],
                    address=business_data['address'],
                    business_type=business_data['business_type'],
                    verification_status=business_data['verification_status'],
                    password_hash=generate_password_hash('password123')
                )
                db.session.add(business)
        
        db.session.commit()
        print("✓ Created demo businesses")
        
        # Create demo products
        categories = Category.query.all()
        businesses = Business.query.all()
        
        products_data = [
            {'name': 'iPhone 15 Pro', 'price': 999.99, 'category': 'Electronics'},
            {'name': 'Samsung Galaxy S24', 'price': 899.99, 'category': 'Electronics'},
            {'name': 'MacBook Pro M3', 'price': 1999.99, 'category': 'Electronics'},
            {'name': 'Designer Jeans', 'price': 79.99, 'category': 'Clothing'},
            {'name': 'Cotton T-Shirt', 'price': 19.99, 'category': 'Clothing'},
            {'name': 'Running Shoes', 'price': 129.99, 'category': 'Sports'},
            {'name': 'Yoga Mat', 'price': 29.99, 'category': 'Sports'},
            {'name': 'Garden Plants', 'price': 15.99, 'category': 'Home & Garden'},
            {'name': 'Cook Book', 'price': 24.99, 'category': 'Books'},
            {'name': 'Face Cream', 'price': 39.99, 'category': 'Health & Beauty'}
        ]
        
        for product_data in products_data:
            # Find category
            category = Category.query.filter_by(name=product_data['category']).first()
            if not category:
                continue
                
            # Random business
            business = random.choice(businesses)
            
            existing = Product.query.filter_by(name=product_data['name']).first()
            if not existing:
                product = Product(
                    name=product_data['name'],
                    price=product_data['price'],
                    category_id=category.id,
                    business_id=business.id,
                    description=f"High quality {product_data['name']} available now",
                    stock_quantity=random.randint(10, 100),
                    is_active=True
                )
                db.session.add(product)
        
        db.session.commit()
        print("✓ Created demo products")
        
        # Create demo apps
        apps_data = [
            {
                'name': 'Mobile Shop Hub',
                'category': 'Business',
                'description': 'Complete mobile shop management system',
                'price': 0.0,
                'status': 'active'
            },
            {
                'name': 'E-Commerce Pro',
                'category': 'Business',
                'description': 'Professional e-commerce platform',
                'price': 49.99,
                'status': 'active'
            },
            {
                'name': 'Inventory Manager',
                'category': 'Business',
                'description': 'Smart inventory management tool',
                'price': 29.99,
                'status': 'active'
            }
        ]
        
        for app_data in apps_data:
            existing = App.query.filter_by(name=app_data['name']).first()
            if not existing:
                app = App(
                    name=app_data['name'],
                    category=app_data['category'],
                    description=app_data['description'],
                    price=app_data['price'],
                    status=app_data['status'],
                    downloads=random.randint(100, 10000),
                    rating=random.uniform(4.0, 5.0)
                )
                db.session.add(app)
        
        db.session.commit()
        print("✓ Created demo apps")
        
        # Create demo users
        users_data = [
            {
                'full_name': 'John Subscriber',
                'email': 'john@subscriber.com',
                'mobile': '9876543213',
                'user_type': 'subscriber'
            },
            {
                'full_name': 'Jane Business',
                'email': 'jane@business.com',
                'mobile': '9876543214',
                'user_type': 'business'
            }
        ]
        
        for user_data in users_data:
            existing = User.query.filter_by(email=user_data['email']).first()
            if not existing:
                user = User(
                    full_name=user_data['full_name'],
                    email=user_data['email'],
                    mobile=user_data['mobile'],
                    user_type=user_data['user_type'],
                    password_hash=generate_password_hash('password123')
                )
                db.session.add(user)
        
        db.session.commit()
        print("✓ Created demo users")
        
        # Print summary
        print("\n=== DEMO DATA SUMMARY ===")
        print(f"Businesses: {Business.query.count()}")
        print(f"Products: {Product.query.count()}")
        print(f"Apps: {App.query.count()}")
        print(f"Users: {User.query.count()}")
        print(f"Categories: {Category.query.count()}")
        print(f"Pricing Plans: {db.session.query(db.text('SELECT COUNT(*) FROM pricing_plans')).scalar()}")

if __name__ == "__main__":
    create_simple_demo_data()