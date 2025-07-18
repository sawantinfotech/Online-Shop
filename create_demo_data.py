#!/usr/bin/env python3
"""
Demo Data Generator for Mobile Shop Management System
Creates sample businesses and delivery partners for testing
"""

from app import app, db
from models import Business, Customer, Product, Category, User, DeliveryProfile
from datetime import datetime, timedelta
import random

def create_demo_businesses():
    """Create 20 demo businesses"""
    demo_businesses = [
        {
            'business_name': 'TechMart Electronics',
            'email': 'admin@techmart.com',
            'contact_number': '+1234567890',
            'address': '123 Tech Street, Silicon Valley, CA',
            'business_type': 'retail',
            'license_number': 'TM2024001',
            'verification_status': 'verified'
        },
        {
            'business_name': 'Fashion Hub',
            'email': 'contact@fashionhub.com',
            'contact_number': '+1234567891',
            'address': '456 Fashion Ave, New York, NY',
            'business_type': 'retail',
            'license_number': 'FH2024002',
            'verification_status': 'verified'
        },
        {
            'business_name': 'Home Essentials Store',
            'email': 'info@homeessentials.com',
            'contact_number': '+1234567892',
            'address': '789 Home Blvd, Austin, TX',
            'business_type': 'retail',
            'license_number': 'HE2024003',
            'verification_status': 'verified'
        },
        {
            'business_name': 'Sports Central',
            'email': 'sales@sportscentral.com',
            'contact_number': '+1234567893',
            'address': '321 Sports Drive, Miami, FL',
            'business_type': 'retail',
            'license_number': 'SC2024004',
            'verification_status': 'verified'
        },
        {
            'business_name': 'BookWorm Library',
            'email': 'books@bookworm.com',
            'contact_number': '+1234567894',
            'address': '654 Knowledge Lane, Boston, MA',
            'business_type': 'retail',
            'license_number': 'BW2024005',
            'verification_status': 'verified'
        },
        {
            'business_name': 'Beauty Palace',
            'email': 'beauty@palace.com',
            'contact_number': '+1234567895',
            'address': '987 Beauty Street, Los Angeles, CA',
            'business_type': 'retail',
            'license_number': 'BP2024006',
            'verification_status': 'verified'
        },
        {
            'business_name': 'Gourmet Foods',
            'email': 'gourmet@foods.com',
            'contact_number': '+1234567896',
            'address': '147 Taste Avenue, Chicago, IL',
            'business_type': 'retail',
            'license_number': 'GF2024007',
            'verification_status': 'verified'
        },
        {
            'business_name': 'Mobile Accessories Plus',
            'email': 'mobile@accessories.com',
            'contact_number': '+1234567897',
            'address': '258 Mobile Street, Seattle, WA',
            'business_type': 'retail',
            'license_number': 'MA2024008',
            'verification_status': 'verified'
        },
        {
            'business_name': 'Gadget Galaxy',
            'email': 'gadgets@galaxy.com',
            'contact_number': '+1234567898',
            'address': '369 Galaxy Road, Denver, CO',
            'business_type': 'retail',
            'license_number': 'GG2024009',
            'verification_status': 'verified'
        },
        {
            'business_name': 'Office Supplies Co',
            'email': 'office@supplies.com',
            'contact_number': '+1234567899',
            'address': '741 Office Park, Phoenix, AZ',
            'business_type': 'wholesale',
            'license_number': 'OS2024010',
            'verification_status': 'verified'
        },
        {
            'business_name': 'Pet Paradise',
            'email': 'pets@paradise.com',
            'contact_number': '+1234567800',
            'address': '852 Pet Lane, Portland, OR',
            'business_type': 'retail',
            'license_number': 'PP2024011',
            'verification_status': 'verified'
        },
        {
            'business_name': 'Auto Parts Direct',
            'email': 'auto@parts.com',
            'contact_number': '+1234567801',
            'address': '963 Auto Street, Detroit, MI',
            'business_type': 'wholesale',
            'license_number': 'AP2024012',
            'verification_status': 'verified'
        },
        {
            'business_name': 'Jewelry Junction',
            'email': 'jewelry@junction.com',
            'contact_number': '+1234567802',
            'address': '159 Jewelry Ave, Las Vegas, NV',
            'business_type': 'retail',
            'license_number': 'JJ2024013',
            'verification_status': 'verified'
        },
        {
            'business_name': 'Toy Kingdom',
            'email': 'toys@kingdom.com',
            'contact_number': '+1234567803',
            'address': '753 Toy Street, Orlando, FL',
            'business_type': 'retail',
            'license_number': 'TK2024014',
            'verification_status': 'verified'
        },
        {
            'business_name': 'Music Instruments Store',
            'email': 'music@instruments.com',
            'contact_number': '+1234567804',
            'address': '357 Music Boulevard, Nashville, TN',
            'business_type': 'retail',
            'license_number': 'MI2024015',
            'verification_status': 'verified'
        },
        {
            'business_name': 'Garden Center',
            'email': 'garden@center.com',
            'contact_number': '+1234567805',
            'address': '951 Garden Way, San Diego, CA',
            'business_type': 'retail',
            'license_number': 'GC2024016',
            'verification_status': 'verified'
        },
        {
            'business_name': 'Hardware Solutions',
            'email': 'hardware@solutions.com',
            'contact_number': '+1234567806',
            'address': '624 Hardware Street, Houston, TX',
            'business_type': 'wholesale',
            'license_number': 'HS2024017',
            'verification_status': 'verified'
        },
        {
            'business_name': 'Craft Supplies Hub',
            'email': 'craft@supplies.com',
            'contact_number': '+1234567807',
            'address': '486 Craft Avenue, Minneapolis, MN',
            'business_type': 'retail',
            'license_number': 'CS2024018',
            'verification_status': 'verified'
        },
        {
            'business_name': 'Electronics Wholesale',
            'email': 'wholesale@electronics.com',
            'contact_number': '+1234567808',
            'address': '735 Wholesale Drive, Atlanta, GA',
            'business_type': 'wholesale',
            'license_number': 'EW2024019',
            'verification_status': 'verified'
        },
        {
            'business_name': 'Vintage Collectibles',
            'email': 'vintage@collectibles.com',
            'contact_number': '+1234567809',
            'address': '824 Vintage Road, San Francisco, CA',
            'business_type': 'retail',
            'license_number': 'VC2024020',
            'verification_status': 'verified'
        }
    ]
    
    businesses_created = []
    for biz_data in demo_businesses:
        # Check if business already exists
        existing = Business.query.filter_by(email=biz_data['email']).first()
        if not existing:
            business = Business(**biz_data)
            business.set_password('password123')  # Default password for demo
            db.session.add(business)
            businesses_created.append(business)
    
    return businesses_created

def create_demo_delivery_partners():
    """Create 20 demo delivery partners"""
    demo_partners = [
        {'full_name': 'John Smith', 'email': 'john.smith@delivery.com', 'phone_number': '+1234567890', 'driving_license': 'DL001', 'rating': 4.8, 'total_deliveries': 245},
        {'full_name': 'Sarah Johnson', 'email': 'sarah.johnson@delivery.com', 'phone_number': '+1234567891', 'driving_license': 'DL002', 'rating': 4.9, 'total_deliveries': 178},
        {'full_name': 'Mike Davis', 'email': 'mike.davis@delivery.com', 'phone_number': '+1234567892', 'driving_license': 'DL003', 'rating': 4.7, 'total_deliveries': 312},
        {'full_name': 'Lisa Chen', 'email': 'lisa.chen@delivery.com', 'phone_number': '+1234567893', 'driving_license': 'DL004', 'rating': 4.8, 'total_deliveries': 189},
        {'full_name': 'Robert Wilson', 'email': 'robert.wilson@delivery.com', 'phone_number': '+1234567894', 'driving_license': 'DL005', 'rating': 4.6, 'total_deliveries': 203},
        {'full_name': 'Amanda Brown', 'email': 'amanda.brown@delivery.com', 'phone_number': '+1234567895', 'driving_license': 'DL006', 'rating': 4.9, 'total_deliveries': 267},
        {'full_name': 'David Miller', 'email': 'david.miller@delivery.com', 'phone_number': '+1234567896', 'driving_license': 'DL007', 'rating': 4.5, 'total_deliveries': 156},
        {'full_name': 'Emily Garcia', 'email': 'emily.garcia@delivery.com', 'phone_number': '+1234567897', 'driving_license': 'DL008', 'rating': 4.8, 'total_deliveries': 234},
        {'full_name': 'James Rodriguez', 'email': 'james.rodriguez@delivery.com', 'phone_number': '+1234567898', 'driving_license': 'DL009', 'rating': 4.7, 'total_deliveries': 198},
        {'full_name': 'Jennifer Martinez', 'email': 'jennifer.martinez@delivery.com', 'phone_number': '+1234567899', 'driving_license': 'DL010', 'rating': 4.9, 'total_deliveries': 289},
        {'full_name': 'Kevin Anderson', 'email': 'kevin.anderson@delivery.com', 'phone_number': '+1234567800', 'driving_license': 'DL011', 'rating': 4.6, 'total_deliveries': 145},
        {'full_name': 'Michelle Taylor', 'email': 'michelle.taylor@delivery.com', 'phone_number': '+1234567801', 'driving_license': 'DL012', 'rating': 4.8, 'total_deliveries': 221},
        {'full_name': 'Daniel Thomas', 'email': 'daniel.thomas@delivery.com', 'phone_number': '+1234567802', 'driving_license': 'DL013', 'rating': 4.7, 'total_deliveries': 167},
        {'full_name': 'Jessica White', 'email': 'jessica.white@delivery.com', 'phone_number': '+1234567803', 'driving_license': 'DL014', 'rating': 4.9, 'total_deliveries': 298},
        {'full_name': 'Christopher Lee', 'email': 'christopher.lee@delivery.com', 'phone_number': '+1234567804', 'driving_license': 'DL015', 'rating': 4.5, 'total_deliveries': 134},
        {'full_name': 'Ashley Harris', 'email': 'ashley.harris@delivery.com', 'phone_number': '+1234567805', 'driving_license': 'DL016', 'rating': 4.8, 'total_deliveries': 256},
        {'full_name': 'Matthew Clark', 'email': 'matthew.clark@delivery.com', 'phone_number': '+1234567806', 'driving_license': 'DL017', 'rating': 4.6, 'total_deliveries': 187},
        {'full_name': 'Stephanie Lewis', 'email': 'stephanie.lewis@delivery.com', 'phone_number': '+1234567807', 'driving_license': 'DL018', 'rating': 4.9, 'total_deliveries': 276},
        {'full_name': 'Ryan Walker', 'email': 'ryan.walker@delivery.com', 'phone_number': '+1234567808', 'driving_license': 'DL019', 'rating': 4.7, 'total_deliveries': 158},
        {'full_name': 'Nicole Hall', 'email': 'nicole.hall@delivery.com', 'phone_number': '+1234567809', 'driving_license': 'DL020', 'rating': 4.8, 'total_deliveries': 243}
    ]
    
    partners_created = []
    for partner_data in demo_partners:
        # Check if user already exists
        existing_user = User.query.filter_by(email=partner_data['email']).first()
        if not existing_user:
            # Create user first
            user = User(
                username=partner_data['email'].split('@')[0],
                email=partner_data['email'],
                full_name=partner_data['full_name'],
                phone_number=partner_data['phone_number'],
                role='delivery'
            )
            user.set_password('password123')
            db.session.add(user)
            db.session.flush()  # Get the ID
            
            # Create delivery profile
            delivery_profile = DeliveryProfile(
                user_id=user.id,
                driving_license=partner_data['driving_license'],
                rating=partner_data['rating'],
                total_deliveries=partner_data['total_deliveries'],
                status='active',
                verification_status='verified',
                is_available=True,
                registration_fee_paid=True
            )
            db.session.add(delivery_profile)
            partners_created.append(user)
    
    return partners_created

def create_demo_products():
    """Create sample products for demo businesses"""
    categories = Category.query.all()
    businesses = Business.query.all()
    
    if not categories or not businesses:
        print("No categories or businesses found. Create them first.")
        return []
    
    products_created = []
    
    # Sample products for each category
    sample_products = {
        'Electronics': [
            {'name': 'Smartphone X1', 'price': 599.99, 'description': 'Latest smartphone with advanced features'},
            {'name': 'Laptop Pro', 'price': 1299.99, 'description': 'High-performance laptop for professionals'},
            {'name': 'Wireless Headphones', 'price': 199.99, 'description': 'Premium wireless headphones'},
        ],
        'Clothing': [
            {'name': 'Cotton T-Shirt', 'price': 24.99, 'description': 'Comfortable cotton t-shirt'},
            {'name': 'Denim Jeans', 'price': 79.99, 'description': 'Classic denim jeans'},
            {'name': 'Winter Jacket', 'price': 149.99, 'description': 'Warm winter jacket'},
        ],
        'Home & Garden': [
            {'name': 'Garden Tools Set', 'price': 89.99, 'description': 'Complete garden tools set'},
            {'name': 'LED Desk Lamp', 'price': 45.99, 'description': 'Modern LED desk lamp'},
            {'name': 'Flower Pot Set', 'price': 29.99, 'description': 'Decorative flower pot set'},
        ]
    }
    
    for category in categories[:3]:  # Only create products for first 3 categories
        if category.name in sample_products:
            for product_data in sample_products[category.name]:
                # Assign to random business
                business = random.choice(businesses)
                
                product = Product(
                    business_id=business.id,
                    category_id=category.id,
                    product_name=product_data['name'],
                    price=product_data['price'],
                    description=product_data['description'],
                    quantity=random.randint(10, 100),
                    weight=random.uniform(0.1, 5.0)
                )
                
                db.session.add(product)
                products_created.append(product)
    
    return products_created

def main():
    """Main function to create all demo data"""
    print("Creating demo data for Mobile Shop Management System...")
    
    with app.app_context():
        try:
            # Create demo businesses
            print("Creating demo businesses...")
            businesses = create_demo_businesses()
            print(f"Created {len(businesses)} demo businesses")
            
            # Create demo delivery partners
            print("Creating demo delivery partners...")
            partners = create_demo_delivery_partners()
            print(f"Created {len(partners)} demo delivery partners")
            
            # Create demo products
            print("Creating demo products...")
            products = create_demo_products()
            print(f"Created {len(products)} demo products")
            
            # Commit all changes
            db.session.commit()
            print("✓ All demo data created successfully!")
            
            # Print summary
            print("\n=== DEMO DATA SUMMARY ===")
            print(f"Businesses: {Business.query.count()}")
            print(f"Delivery Partners: {User.query.filter_by(role='delivery').count()}")
            print(f"Products: {Product.query.count()}")
            print(f"Categories: {Category.query.count()}")
            
            print("\n=== LOGIN CREDENTIALS ===")
            print("All demo accounts use password: password123")
            print("\nSample Business Logins:")
            for i, business in enumerate(Business.query.limit(5).all()):
                print(f"  {i+1}. {business.email} - {business.business_name}")
            
            print("\nSample Delivery Partner Logins:")
            for i, partner in enumerate(User.query.filter_by(role='delivery').limit(5).all()):
                print(f"  {i+1}. {partner.email} - {partner.full_name}")
            
        except Exception as e:
            print(f"Error creating demo data: {e}")
            db.session.rollback()

if __name__ == "__main__":
    main()