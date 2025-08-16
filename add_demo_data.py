from app import app, db
from models import Business, User, DeliveryProfile, Product, Category
import random

with app.app_context():
    # Create demo businesses
    businesses_data = [
        {'business_name': 'TechMart Electronics', 'email': 'admin@techmart.com', 'contact_number': '+1234567890', 'address': '123 Tech Street, Silicon Valley, CA', 'business_type': 'retail', 'license_number': 'TM2024001', 'verification_status': 'verified'},
        {'business_name': 'Fashion Hub', 'email': 'contact@fashionhub.com', 'contact_number': '+1234567891', 'address': '456 Fashion Ave, New York, NY', 'business_type': 'retail', 'license_number': 'FH2024002', 'verification_status': 'verified'},
        {'business_name': 'Home Essentials Store', 'email': 'info@homeessentials.com', 'contact_number': '+1234567892', 'address': '789 Home Blvd, Austin, TX', 'business_type': 'retail', 'license_number': 'HE2024003', 'verification_status': 'verified'},
        {'business_name': 'Sports Central', 'email': 'sales@sportscentral.com', 'contact_number': '+1234567893', 'address': '321 Sports Drive, Miami, FL', 'business_type': 'retail', 'license_number': 'SC2024004', 'verification_status': 'verified'},
        {'business_name': 'BookWorm Library', 'email': 'books@bookworm.com', 'contact_number': '+1234567894', 'address': '654 Knowledge Lane, Boston, MA', 'business_type': 'retail', 'license_number': 'BW2024005', 'verification_status': 'verified'},
        {'business_name': 'Beauty Palace', 'email': 'beauty@palace.com', 'contact_number': '+1234567895', 'address': '987 Beauty Street, Los Angeles, CA', 'business_type': 'retail', 'license_number': 'BP2024006', 'verification_status': 'verified'},
        {'business_name': 'Gourmet Foods', 'email': 'gourmet@foods.com', 'contact_number': '+1234567896', 'address': '147 Taste Avenue, Chicago, IL', 'business_type': 'retail', 'license_number': 'GF2024007', 'verification_status': 'verified'},
        {'business_name': 'Mobile Accessories Plus', 'email': 'mobile@accessories.com', 'contact_number': '+1234567897', 'address': '258 Mobile Street, Seattle, WA', 'business_type': 'retail', 'license_number': 'MA2024008', 'verification_status': 'verified'},
        {'business_name': 'Gadget Galaxy', 'email': 'gadgets@galaxy.com', 'contact_number': '+1234567898', 'address': '369 Galaxy Road, Denver, CO', 'business_type': 'retail', 'license_number': 'GG2024009', 'verification_status': 'verified'},
        {'business_name': 'Office Supplies Co', 'email': 'office@supplies.com', 'contact_number': '+1234567899', 'address': '741 Office Park, Phoenix, AZ', 'business_type': 'wholesale', 'license_number': 'OS2024010', 'verification_status': 'verified'},
        {'business_name': 'Pet Paradise', 'email': 'pets@paradise.com', 'contact_number': '+1234567800', 'address': '852 Pet Lane, Portland, OR', 'business_type': 'retail', 'license_number': 'PP2024011', 'verification_status': 'verified'},
        {'business_name': 'Auto Parts Direct', 'email': 'auto@parts.com', 'contact_number': '+1234567801', 'address': '963 Auto Street, Detroit, MI', 'business_type': 'wholesale', 'license_number': 'AP2024012', 'verification_status': 'verified'},
        {'business_name': 'Jewelry Junction', 'email': 'jewelry@junction.com', 'contact_number': '+1234567802', 'address': '159 Jewelry Ave, Las Vegas, NV', 'business_type': 'retail', 'license_number': 'JJ2024013', 'verification_status': 'verified'},
        {'business_name': 'Toy Kingdom', 'email': 'toys@kingdom.com', 'contact_number': '+1234567803', 'address': '753 Toy Street, Orlando, FL', 'business_type': 'retail', 'license_number': 'TK2024014', 'verification_status': 'verified'},
        {'business_name': 'Music Instruments Store', 'email': 'music@instruments.com', 'contact_number': '+1234567804', 'address': '357 Music Boulevard, Nashville, TN', 'business_type': 'retail', 'license_number': 'MI2024015', 'verification_status': 'verified'},
        {'business_name': 'Garden Center', 'email': 'garden@center.com', 'contact_number': '+1234567805', 'address': '951 Garden Way, San Diego, CA', 'business_type': 'retail', 'license_number': 'GC2024016', 'verification_status': 'verified'},
        {'business_name': 'Hardware Solutions', 'email': 'hardware@solutions.com', 'contact_number': '+1234567806', 'address': '624 Hardware Street, Houston, TX', 'business_type': 'wholesale', 'license_number': 'HS2024017', 'verification_status': 'verified'},
        {'business_name': 'Craft Supplies Hub', 'email': 'craft@supplies.com', 'contact_number': '+1234567807', 'address': '486 Craft Avenue, Minneapolis, MN', 'business_type': 'retail', 'license_number': 'CS2024018', 'verification_status': 'verified'},
        {'business_name': 'Electronics Wholesale', 'email': 'wholesale@electronics.com', 'contact_number': '+1234567808', 'address': '735 Wholesale Drive, Atlanta, GA', 'business_type': 'wholesale', 'license_number': 'EW2024019', 'verification_status': 'verified'},
        {'business_name': 'Vintage Collectibles', 'email': 'vintage@collectibles.com', 'contact_number': '+1234567809', 'address': '824 Vintage Road, San Francisco, CA', 'business_type': 'retail', 'license_number': 'VC2024020', 'verification_status': 'verified'}
    ]
    
    print("Adding demo businesses...")
    for biz_data in businesses_data:
        existing = Business.query.filter_by(email=biz_data['email']).first()
        if not existing:
            business = Business(**biz_data)
            business.set_password('password123')
            db.session.add(business)
    
    # Create demo delivery partners
    delivery_data = [
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
    
    print("Adding demo delivery partners...")
    for partner_data in delivery_data:
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
            db.session.flush()
            
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
    
    db.session.commit()
    
    # Print summary
    print("\n=== DEMO DATA SUMMARY ===")
    print(f"Businesses: {Business.query.count()}")
    print(f"Delivery Partners: {User.query.filter_by(role='delivery').count()}")
    print(f"Products: {Product.query.count()}")
    print(f"Categories: {Category.query.count()}")
    print("\nDemo data created successfully!")
    print("Password for all demo accounts: password123")