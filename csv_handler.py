"""
CSV Import/Export Handler for Mobile Shop Management System
Handles bulk data operations for all sections with proper validation and demo data generation
"""

import csv
import io
import json
import logging
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash
from flask import Response, request, flash
from models import *
from app import db
import random
import uuid


class CSVHandler:
    """Handles CSV import/export operations for all data models"""
    
    @staticmethod
    def export_to_csv(data, columns, filename):
        """Export data to CSV format"""
        output = io.StringIO()
        writer = csv.DictWriter(output, fieldnames=columns)
        writer.writeheader()
        
        for item in data:
            row = {}
            for col in columns:
                value = getattr(item, col, '')
                if isinstance(value, datetime):
                    value = value.strftime('%Y-%m-%d %H:%M:%S')
                elif isinstance(value, bool):
                    value = 'Yes' if value else 'No'
                elif value is None:
                    value = ''
                row[col] = str(value)
            writer.writerow(row)
        
        output.seek(0)
        return Response(
            output.getvalue(),
            mimetype='text/csv',
            headers={"Content-disposition": f"attachment; filename={filename}.csv"}
        )
    
    @staticmethod
    def import_from_csv(file_data, model_class, required_fields, user_id=None):
        """Import data from CSV file"""
        try:
            csv_data = file_data.read().decode('utf-8')
            reader = csv.DictReader(io.StringIO(csv_data))
            
            imported_count = 0
            errors = []
            
            for row_num, row in enumerate(reader, 1):
                try:
                    # Validate required fields
                    for field in required_fields:
                        if not row.get(field):
                            errors.append(f"Row {row_num}: Missing required field '{field}'")
                            continue
                    
                    # Create model instance based on class
                    if model_class == Business:
                        obj = CSVHandler._create_business(row, user_id)
                    elif model_class == Product:
                        obj = CSVHandler._create_product(row, user_id)
                    elif model_class == Customer:
                        obj = CSVHandler._create_customer(row, user_id)
                    elif model_class == App:
                        obj = CSVHandler._create_app(row)
                    elif model_class == MatrimonyProfile:
                        obj = CSVHandler._create_matrimony_profile(row)
                    elif model_class == Category:
                        obj = CSVHandler._create_category(row)
                    elif model_class == User:
                        obj = CSVHandler._create_user(row)
                    else:
                        continue
                    
                    if obj:
                        db.session.add(obj)
                        imported_count += 1
                        
                except Exception as e:
                    errors.append(f"Row {row_num}: {str(e)}")
            
            db.session.commit()
            return imported_count, errors
            
        except Exception as e:
            db.session.rollback()
            return 0, [f"File processing error: {str(e)}"]
    
    @staticmethod
    def _create_business(row, user_id):
        """Create business from CSV row"""
        return Business(
            user_id=user_id,
            name=row['name'],
            description=row.get('description', ''),
            email=row['email'],
            phone=row.get('phone', ''),
            address=row.get('address', ''),
            business_type=row.get('business_type', 'retail'),
            verification_status='pending',
            created_at=datetime.utcnow()
        )
    
    @staticmethod
    def _create_product(row, user_id):
        """Create product from CSV row"""
        business_id = row.get('business_id') or Business.query.filter_by(user_id=user_id).first().id
        return Product(
            business_id=business_id,
            name=row['name'],
            description=row.get('description', ''),
            price=float(row.get('price', 0)),
            quantity=int(row.get('quantity', 0)),
            category=row.get('category', 'General'),
            is_active=True,
            created_at=datetime.utcnow()
        )
    
    @staticmethod
    def _create_customer(row, user_id):
        """Create customer from CSV row"""
        business_id = row.get('business_id') or Business.query.filter_by(user_id=user_id).first().id
        return Customer(
            business_id=business_id,
            name=row['name'],
            email=row['email'],
            phone=row.get('phone', ''),
            address=row.get('address', ''),
            customer_group=row.get('customer_group', 'Regular'),
            created_at=datetime.utcnow()
        )
    
    @staticmethod
    def _create_app(row):
        """Create app from CSV row"""
        return App(
            name=row['name'],
            slug=row['name'].lower().replace(' ', '-'),
            short_description=row.get('short_description', ''),
            category=row.get('category', 'General'),
            author_name=row.get('author_name', 'Developer'),
            rating=float(row.get('rating', 4.0)),
            downloads=int(row.get('downloads', 0)),
            status='active',
            created_at=datetime.utcnow()
        )
    
    @staticmethod
    def _create_matrimony_profile(row):
        """Create matrimony profile from CSV row"""
        return MatrimonyProfile(
            full_name=row['full_name'],
            age=int(row['age']),
            gender=row['gender'],
            marital_status=row.get('marital_status', 'single'),
            relationship_type=row.get('relationship_type', 'marriage'),
            city=row['city'],
            state=row['state'],
            education=row.get('education', ''),
            occupation=row.get('occupation', ''),
            email=row['email'],
            phone=row.get('phone', ''),
            is_verified=False,
            created_at=datetime.utcnow()
        )
    
    @staticmethod
    def _create_category(row):
        """Create category from CSV row"""
        return Category(
            name=row['name'],
            description=row.get('description', ''),
            created_at=datetime.utcnow()
        )
    
    @staticmethod
    def _create_user(row):
        """Create user from CSV row"""
        return User(
            full_name=row['full_name'],
            email=row['email'],
            mobile=row.get('mobile', ''),
            password_hash=generate_password_hash('password123'),
            user_type=row.get('user_type', 'subscriber'),
            is_verified=True,
            created_at=datetime.utcnow()
        )


class DemoDataGenerator:
    """Generates demo CSV files for all sections"""
    
    @staticmethod
    def generate_demo_businesses():
        """Generate demo businesses CSV data"""
        businesses = [
            {'name': 'Tech Solutions Pro', 'description': 'Advanced technology solutions', 'email': 'contact@techsolutions.com', 'phone': '+1-555-0101', 'address': '123 Tech Street, Silicon Valley', 'business_type': 'technology'},
            {'name': 'Fashion Forward Store', 'description': 'Latest fashion trends', 'email': 'info@fashionforward.com', 'phone': '+1-555-0102', 'address': '456 Fashion Ave, New York', 'business_type': 'retail'},
            {'name': 'Green Garden Center', 'description': 'Plants and gardening supplies', 'email': 'hello@greengarden.com', 'phone': '+1-555-0103', 'address': '789 Garden Blvd, Portland', 'business_type': 'gardening'},
            {'name': 'Sports Excellence', 'description': 'Premium sports equipment', 'email': 'sales@sportsexcellence.com', 'phone': '+1-555-0104', 'address': '321 Sports Way, Denver', 'business_type': 'sports'},
            {'name': 'BookWorm Paradise', 'description': 'Books for every reader', 'email': 'books@bookworm.com', 'phone': '+1-555-0105', 'address': '654 Library St, Boston', 'business_type': 'bookstore'},
            {'name': 'Beauty Bliss Salon', 'description': 'Complete beauty services', 'email': 'appointments@beautybliss.com', 'phone': '+1-555-0106', 'address': '987 Beauty Lane, Miami', 'business_type': 'beauty'},
            {'name': 'Food Fusion Restaurant', 'description': 'International cuisine', 'email': 'orders@foodfusion.com', 'phone': '+1-555-0107', 'address': '147 Cuisine Ave, Chicago', 'business_type': 'restaurant'},
            {'name': 'Auto Care Plus', 'description': 'Complete automotive services', 'email': 'service@autocare.com', 'phone': '+1-555-0108', 'address': '258 Auto Street, Detroit', 'business_type': 'automotive'},
            {'name': 'Home Decor Emporium', 'description': 'Beautiful home decorations', 'email': 'design@homedecor.com', 'phone': '+1-555-0109', 'address': '369 Decor Drive, Atlanta', 'business_type': 'home_decor'},
            {'name': 'Electronics Galaxy', 'description': 'Latest electronic gadgets', 'email': 'support@electronicsgalaxy.com', 'phone': '+1-555-0110', 'address': '741 Electronics Plaza, Seattle', 'business_type': 'electronics'}
        ]
        return businesses
    
    @staticmethod
    def generate_demo_products():
        """Generate demo products CSV data"""
        products = [
            {'name': 'Smartphone Pro Max', 'description': 'Latest flagship smartphone', 'price': '999.99', 'quantity': '50', 'category': 'Electronics'},
            {'name': 'Wireless Earbuds', 'description': 'Premium wireless earbuds', 'price': '199.99', 'quantity': '100', 'category': 'Electronics'},
            {'name': 'Designer T-Shirt', 'description': 'Premium cotton t-shirt', 'price': '49.99', 'quantity': '75', 'category': 'Fashion'},
            {'name': 'Running Shoes', 'description': 'Professional running shoes', 'price': '129.99', 'quantity': '60', 'category': 'Sports'},
            {'name': 'Organic Plant Food', 'description': 'Natural plant nutrients', 'price': '24.99', 'quantity': '200', 'category': 'Gardening'},
            {'name': 'Programming Book', 'description': 'Learn Python programming', 'price': '39.99', 'quantity': '30', 'category': 'Books'},
            {'name': 'Face Moisturizer', 'description': 'Anti-aging face cream', 'price': '34.99', 'quantity': '80', 'category': 'Beauty'},
            {'name': 'Protein Shake', 'description': 'Vanilla protein powder', 'price': '59.99', 'quantity': '40', 'category': 'Health'},
            {'name': 'Car Phone Holder', 'description': 'Universal car mount', 'price': '19.99', 'quantity': '150', 'category': 'Automotive'},
            {'name': 'LED Desk Lamp', 'description': 'Adjustable LED lamp', 'price': '79.99', 'quantity': '25', 'category': 'Home'}
        ]
        return products
    
    @staticmethod
    def generate_demo_customers():
        """Generate demo customers CSV data"""
        customers = [
            {'name': 'John Smith', 'email': 'john.smith@email.com', 'phone': '+1-555-1001', 'address': '123 Main St, Anytown', 'customer_group': 'Premium'},
            {'name': 'Sarah Johnson', 'email': 'sarah.j@email.com', 'phone': '+1-555-1002', 'address': '456 Oak Ave, Springfield', 'customer_group': 'Regular'},
            {'name': 'Mike Davis', 'email': 'mike.davis@email.com', 'phone': '+1-555-1003', 'address': '789 Pine Rd, Riverside', 'customer_group': 'VIP'},
            {'name': 'Emily Brown', 'email': 'emily.brown@email.com', 'phone': '+1-555-1004', 'address': '321 Elm St, Lakewood', 'customer_group': 'Regular'},
            {'name': 'David Wilson', 'email': 'david.w@email.com', 'phone': '+1-555-1005', 'address': '654 Maple Dr, Hillview', 'customer_group': 'Premium'},
            {'name': 'Lisa Anderson', 'email': 'lisa.anderson@email.com', 'phone': '+1-555-1006', 'address': '987 Cedar Ln, Parkside', 'customer_group': 'Regular'},
            {'name': 'Robert Taylor', 'email': 'robert.t@email.com', 'phone': '+1-555-1007', 'address': '147 Birch Way, Greenfield', 'customer_group': 'VIP'},
            {'name': 'Jennifer Martinez', 'email': 'jennifer.m@email.com', 'phone': '+1-555-1008', 'address': '258 Spruce St, Fairview', 'customer_group': 'Premium'},
            {'name': 'Christopher Lee', 'email': 'chris.lee@email.com', 'phone': '+1-555-1009', 'address': '369 Walnut Ave, Westside', 'customer_group': 'Regular'},
            {'name': 'Amanda Garcia', 'email': 'amanda.g@email.com', 'phone': '+1-555-1010', 'address': '741 Cherry Blvd, Eastview', 'customer_group': 'VIP'}
        ]
        return customers
    
    @staticmethod
    def generate_demo_apps():
        """Generate demo apps CSV data"""
        apps = [
            {'name': 'TaskMaster Pro', 'short_description': 'Advanced task management', 'category': 'Productivity', 'author_name': 'ProductivityTech', 'rating': '4.8', 'downloads': '15000'},
            {'name': 'FitTracker Plus', 'short_description': 'Comprehensive fitness tracking', 'category': 'Health', 'author_name': 'FitnessTech', 'rating': '4.7', 'downloads': '25000'},
            {'name': 'BudgetWise', 'short_description': 'Smart financial management', 'category': 'Finance', 'author_name': 'FinanceTech', 'rating': '4.6', 'downloads': '18000'},
            {'name': 'LearnFast', 'short_description': 'Accelerated learning platform', 'category': 'Education', 'author_name': 'EduTech', 'rating': '4.9', 'downloads': '30000'},
            {'name': 'PhotoEdit Master', 'short_description': 'Professional photo editing', 'category': 'Photography', 'author_name': 'PhotoTech', 'rating': '4.5', 'downloads': '22000'},
            {'name': 'MusicMix Studio', 'short_description': 'Digital music creation', 'category': 'Music', 'author_name': 'AudioTech', 'rating': '4.4', 'downloads': '12000'},
            {'name': 'TravelGuide Pro', 'short_description': 'Complete travel companion', 'category': 'Travel', 'author_name': 'TravelTech', 'rating': '4.7', 'downloads': '28000'},
            {'name': 'RecipeBook Plus', 'short_description': 'Digital recipe collection', 'category': 'Food', 'author_name': 'CookingTech', 'rating': '4.6', 'downloads': '20000'},
            {'name': 'HomeDesign 3D', 'short_description': '3D home design tool', 'category': 'Design', 'author_name': 'DesignTech', 'rating': '4.5', 'downloads': '16000'},
            {'name': 'PetCare Assistant', 'short_description': 'Complete pet care management', 'category': 'Lifestyle', 'author_name': 'PetTech', 'rating': '4.8', 'downloads': '14000'}
        ]
        return apps
    
    @staticmethod
    def generate_demo_matrimony_profiles():
        """Generate demo matrimony profiles CSV data"""
        profiles = [
            {'full_name': 'Arjun Sharma', 'age': '28', 'gender': 'Male', 'marital_status': 'single', 'relationship_type': 'marriage', 'city': 'Mumbai', 'state': 'Maharashtra', 'education': 'B.Tech', 'occupation': 'Software Engineer', 'email': 'arjun.s@email.com', 'phone': '+91-9876543210'},
            {'full_name': 'Priya Patel', 'age': '26', 'gender': 'Female', 'marital_status': 'single', 'relationship_type': 'marriage', 'city': 'Delhi', 'state': 'Delhi', 'education': 'MBA', 'occupation': 'Marketing Manager', 'email': 'priya.p@email.com', 'phone': '+91-9876543211'},
            {'full_name': 'Rohit Kumar', 'age': '30', 'gender': 'Male', 'marital_status': 'single', 'relationship_type': 'marriage', 'city': 'Bangalore', 'state': 'Karnataka', 'education': 'M.Tech', 'occupation': 'Data Scientist', 'email': 'rohit.k@email.com', 'phone': '+91-9876543212'},
            {'full_name': 'Sneha Gupta', 'age': '25', 'gender': 'Female', 'marital_status': 'single', 'relationship_type': 'marriage', 'city': 'Pune', 'state': 'Maharashtra', 'education': 'BDS', 'occupation': 'Dentist', 'email': 'sneha.g@email.com', 'phone': '+91-9876543213'},
            {'full_name': 'Vikash Singh', 'age': '32', 'gender': 'Male', 'marital_status': 'single', 'relationship_type': 'marriage', 'city': 'Chennai', 'state': 'Tamil Nadu', 'education': 'CA', 'occupation': 'Chartered Accountant', 'email': 'vikash.s@email.com', 'phone': '+91-9876543214'},
            {'full_name': 'Anjali Verma', 'age': '27', 'gender': 'Female', 'marital_status': 'single', 'relationship_type': 'marriage', 'city': 'Hyderabad', 'state': 'Telangana', 'education': 'M.Sc', 'occupation': 'Research Scientist', 'email': 'anjali.v@email.com', 'phone': '+91-9876543215'},
            {'full_name': 'Amit Joshi', 'age': '29', 'gender': 'Male', 'marital_status': 'single', 'relationship_type': 'marriage', 'city': 'Kolkata', 'state': 'West Bengal', 'education': 'M.Com', 'occupation': 'Business Analyst', 'email': 'amit.j@email.com', 'phone': '+91-9876543216'},
            {'full_name': 'Kavya Reddy', 'age': '24', 'gender': 'Female', 'marital_status': 'single', 'relationship_type': 'marriage', 'city': 'Ahmedabad', 'state': 'Gujarat', 'education': 'B.Pharma', 'occupation': 'Pharmacist', 'email': 'kavya.r@email.com', 'phone': '+91-9876543217'},
            {'full_name': 'Rajesh Agarwal', 'age': '31', 'gender': 'Male', 'marital_status': 'single', 'relationship_type': 'marriage', 'city': 'Jaipur', 'state': 'Rajasthan', 'education': 'LLB', 'occupation': 'Lawyer', 'email': 'rajesh.a@email.com', 'phone': '+91-9876543218'},
            {'full_name': 'Neha Kapoor', 'age': '26', 'gender': 'Female', 'marital_status': 'single', 'relationship_type': 'marriage', 'city': 'Lucknow', 'state': 'Uttar Pradesh', 'education': 'M.A', 'occupation': 'Teacher', 'email': 'neha.k@email.com', 'phone': '+91-9876543219'}
        ]
        return profiles
    
    @staticmethod
    def generate_demo_categories():
        """Generate demo categories CSV data"""
        categories = [
            {'name': 'Smart Electronics', 'description': 'Latest smart electronic devices and gadgets'},
            {'name': 'Sustainable Fashion', 'description': 'Eco-friendly and sustainable fashion items'},
            {'name': 'Organic Home & Garden', 'description': 'Organic products for home and garden care'},
            {'name': 'Professional Sports', 'description': 'Professional-grade sports equipment and gear'},
            {'name': 'Digital Books & Media', 'description': 'Digital books, audiobooks, and educational content'},
            {'name': 'Natural Health & Beauty', 'description': 'Natural and organic health and beauty products'},
            {'name': 'Gourmet Food & Beverages', 'description': 'Premium gourmet food items and specialty beverages'},
            {'name': 'Luxury Automotive', 'description': 'Luxury automotive accessories and services'},
            {'name': 'Smart Home Solutions', 'description': 'Intelligent home automation and IoT devices'},
            {'name': 'Artisan Crafts', 'description': 'Handmade artisan crafts and unique creations'}
        ]
        return categories
    
    @staticmethod
    def generate_demo_users():
        """Generate demo users CSV data"""
        users = [
            {'full_name': 'Alex Thompson', 'email': 'alex.thompson@demo.com', 'mobile': '+1-555-2001', 'user_type': 'subscriber'},
            {'full_name': 'Maria Rodriguez', 'email': 'maria.rodriguez@demo.com', 'mobile': '+1-555-2002', 'user_type': 'subscriber'},
            {'full_name': 'James Wilson', 'email': 'james.wilson@demo.com', 'mobile': '+1-555-2003', 'user_type': 'business_owner'},
            {'full_name': 'Emma Davis', 'email': 'emma.davis@demo.com', 'mobile': '+1-555-2004', 'user_type': 'subscriber'},
            {'full_name': 'Michael Brown', 'email': 'michael.brown@demo.com', 'mobile': '+1-555-2005', 'user_type': 'delivery_partner'},
            {'full_name': 'Sophie Anderson', 'email': 'sophie.anderson@demo.com', 'mobile': '+1-555-2006', 'user_type': 'subscriber'},
            {'full_name': 'Daniel Martinez', 'email': 'daniel.martinez@demo.com', 'mobile': '+1-555-2007', 'user_type': 'business_owner'},
            {'full_name': 'Olivia Taylor', 'email': 'olivia.taylor@demo.com', 'mobile': '+1-555-2008', 'user_type': 'subscriber'},
            {'full_name': 'Ryan Johnson', 'email': 'ryan.johnson@demo.com', 'mobile': '+1-555-2009', 'user_type': 'delivery_partner'},
            {'full_name': 'Isabella Garcia', 'email': 'isabella.garcia@demo.com', 'mobile': '+1-555-2010', 'user_type': 'subscriber'}
        ]
        return users
    
    @staticmethod
    def create_demo_csv_files():
        """Create all demo CSV files in the uploads directory"""
        import os
        demo_dir = 'uploads/demo_csv'
        os.makedirs(demo_dir, exist_ok=True)
        
        # Generate all demo CSV files
        datasets = {
            'businesses.csv': DemoDataGenerator.generate_demo_businesses(),
            'products.csv': DemoDataGenerator.generate_demo_products(),
            'customers.csv': DemoDataGenerator.generate_demo_customers(),
            'apps.csv': DemoDataGenerator.generate_demo_apps(),
            'matrimony_profiles.csv': DemoDataGenerator.generate_demo_matrimony_profiles(),
            'categories.csv': DemoDataGenerator.generate_demo_categories(),
            'users.csv': DemoDataGenerator.generate_demo_users()
        }
        
        for filename, data in datasets.items():
            filepath = os.path.join(demo_dir, filename)
            with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
                if data:
                    writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
                    writer.writeheader()
                    writer.writerows(data)
        
        logging.info(f"Demo CSV files created in {demo_dir}")
        return demo_dir