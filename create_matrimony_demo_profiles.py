#!/usr/bin/env python3
"""
Create comprehensive matrimony demo profiles with diverse relationship types and membership levels
"""

import json
import random
from datetime import datetime, timedelta
from app import app, db
from models import MatrimonyProfile

# Sample profile data
profile_data = {
    'girls': [
        {
            'full_name': 'Priya Sharma', 'age': 25, 'city': 'Mumbai', 'state': 'Maharashtra',
            'education': 'MBA in Marketing', 'occupation': 'Digital Marketing Manager',
            'annual_income': '8-12 Lakhs', 'height': '5\'4"', 'complexion': 'fair',
            'bio': 'Passionate about digital marketing and travel. Love exploring new cultures and cuisines.',
            'hobbies': 'Travel, Photography, Cooking, Reading',
            'membership_badge': 'gold', 'relationship_type': 'marriage',
            'profile_images': ['https://images.unsplash.com/photo-1494790108755-2616b30d8c87?w=400&h=400&fit=crop&crop=face']
        },
        {
            'full_name': 'Ananya Reddy', 'age': 27, 'city': 'Bangalore', 'state': 'Karnataka',
            'education': 'B.Tech Computer Science', 'occupation': 'Software Engineer',
            'annual_income': '12-15 Lakhs', 'height': '5\'6"', 'complexion': 'medium',
            'bio': 'Tech enthusiast who loves coding and solving complex problems. Enjoy hiking and yoga.',
            'hobbies': 'Coding, Hiking, Yoga, Music',
            'membership_badge': 'platinum', 'relationship_type': 'marriage',
            'profile_images': ['https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=400&h=400&fit=crop&crop=face']
        },
        {
            'full_name': 'Kavya Patel', 'age': 24, 'city': 'Ahmedabad', 'state': 'Gujarat',
            'education': 'CA', 'occupation': 'Chartered Accountant',
            'annual_income': '6-8 Lakhs', 'height': '5\'3"', 'complexion': 'fair',
            'bio': 'Detail-oriented CA with a passion for financial planning and investment strategies.',
            'hobbies': 'Reading, Finance, Dancing, Traveling',
            'membership_badge': 'silver', 'relationship_type': 'marriage',
            'profile_images': ['https://images.unsplash.com/photo-1489424731084-a5d8b219a5bb?w=400&h=400&fit=crop&crop=face']
        },
        {
            'full_name': 'Sanya Singh', 'age': 26, 'city': 'Delhi', 'state': 'Delhi',
            'education': 'MBBS', 'occupation': 'Doctor',
            'annual_income': '10-15 Lakhs', 'height': '5\'5"', 'complexion': 'medium',
            'bio': 'Dedicated doctor working in pediatrics. Believe in helping others and making a difference.',
            'hobbies': 'Medicine, Volunteering, Reading, Swimming',
            'membership_badge': 'platinum', 'relationship_type': 'marriage',
            'profile_images': ['https://images.unsplash.com/photo-1487412720507-e7ab37603c6f?w=400&h=400&fit=crop&crop=face']
        },
        {
            'full_name': 'Rhea Kapoor', 'age': 23, 'city': 'Pune', 'state': 'Maharashtra',
            'education': 'BBA', 'occupation': 'Business Analyst',
            'annual_income': '5-8 Lakhs', 'height': '5\'2"', 'complexion': 'fair',
            'bio': 'Young professional passionate about business analytics and data visualization.',
            'hobbies': 'Data Analysis, Painting, Fitness, Movies',
            'membership_badge': 'basic', 'relationship_type': 'marriage',
            'profile_images': ['https://images.unsplash.com/photo-1517841905240-472988babdf9?w=400&h=400&fit=crop&crop=face']
        },
        # Open relationship girls
        {
            'full_name': 'Maya Joshi', 'age': 28, 'city': 'Goa', 'state': 'Goa',
            'education': 'MA Psychology', 'occupation': 'Therapist',
            'annual_income': '6-10 Lakhs', 'height': '5\'4"', 'complexion': 'medium',
            'bio': 'Open-minded therapist who believes in modern relationships and personal freedom.',
            'hobbies': 'Psychology, Beach walks, Meditation, Art',
            'membership_badge': 'gold', 'relationship_type': 'open',
            'profile_images': ['https://images.unsplash.com/photo-1494790108755-2616b30d8c87?w=400&h=400&fit=crop&crop=face']
        },
        {
            'full_name': 'Zara Khan', 'age': 29, 'city': 'Mumbai', 'state': 'Maharashtra',
            'education': 'Fashion Design', 'occupation': 'Fashion Designer',
            'annual_income': '8-12 Lakhs', 'height': '5\'7"', 'complexion': 'fair',
            'bio': 'Creative fashion designer exploring modern relationship dynamics.',
            'hobbies': 'Fashion, Designing, Photography, Travel',
            'membership_badge': 'platinum', 'relationship_type': 'open',
            'profile_images': ['https://images.unsplash.com/photo-1502823403499-6ccfcf4fb453?w=400&h=400&fit=crop&crop=face']
        }
    ],
    'boys': [
        {
            'full_name': 'Arjun Mehta', 'age': 28, 'city': 'Mumbai', 'state': 'Maharashtra',
            'education': 'MBA Finance', 'occupation': 'Investment Banker',
            'annual_income': '15-20 Lakhs', 'height': '6\'0"', 'complexion': 'medium',
            'bio': 'Ambitious investment banker who loves financial markets and strategic planning.',
            'hobbies': 'Finance, Cricket, Traveling, Reading',
            'membership_badge': 'platinum', 'relationship_type': 'marriage',
            'profile_images': ['https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400&h=400&fit=crop&crop=face']
        },
        {
            'full_name': 'Rohit Kumar', 'age': 30, 'city': 'Bangalore', 'state': 'Karnataka',
            'education': 'M.Tech', 'occupation': 'Senior Software Engineer',
            'annual_income': '18-25 Lakhs', 'height': '5\'10"', 'complexion': 'fair',
            'bio': 'Senior software engineer passionate about AI and machine learning technologies.',
            'hobbies': 'Technology, Gaming, Football, Cooking',
            'membership_badge': 'gold', 'relationship_type': 'marriage',
            'profile_images': ['https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=400&h=400&fit=crop&crop=face']
        },
        {
            'full_name': 'Vikram Singh', 'age': 32, 'city': 'Delhi', 'state': 'Delhi',
            'education': 'CA + MBA', 'occupation': 'Financial Consultant',
            'annual_income': '20-30 Lakhs', 'height': '6\'1"', 'complexion': 'medium',
            'bio': 'Experienced financial consultant helping businesses grow and prosper.',
            'hobbies': 'Finance, Golf, Reading, Traveling',
            'membership_badge': 'platinum', 'relationship_type': 'marriage',
            'profile_images': ['https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=400&h=400&fit=crop&crop=face']
        },
        {
            'full_name': 'Aditya Gupta', 'age': 27, 'city': 'Pune', 'state': 'Maharashtra',
            'education': 'B.Tech Mechanical', 'occupation': 'Project Manager',
            'annual_income': '10-15 Lakhs', 'height': '5\'9"', 'complexion': 'fair',
            'bio': 'Mechanical engineer turned project manager with a passion for innovation.',
            'hobbies': 'Engineering, Biking, Adventure Sports, Music',
            'membership_badge': 'silver', 'relationship_type': 'marriage',
            'profile_images': ['https://images.unsplash.com/photo-1519345182560-3f2917c472ef?w=400&h=400&fit=crop&crop=face']
        },
        {
            'full_name': 'Karan Shah', 'age': 25, 'city': 'Ahmedabad', 'state': 'Gujarat',
            'education': 'BBA', 'occupation': 'Marketing Executive',
            'annual_income': '6-8 Lakhs', 'height': '5\'8"', 'complexion': 'medium',
            'bio': 'Young marketing professional with creative ideas and entrepreneurial spirit.',
            'hobbies': 'Marketing, Photography, Sports, Movies',
            'membership_badge': 'basic', 'relationship_type': 'marriage',
            'profile_images': ['https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?w=400&h=400&fit=crop&crop=face']
        },
        # Live-in boys
        {
            'full_name': 'Dev Malhotra', 'age': 29, 'city': 'Mumbai', 'state': 'Maharashtra',
            'education': 'MS Computer Science', 'occupation': 'Tech Lead',
            'annual_income': '22-30 Lakhs', 'height': '5\'11"', 'complexion': 'fair',
            'bio': 'Tech lead who believes in modern relationship approaches and compatibility testing.',
            'hobbies': 'Technology, Travel, Music, Photography',
            'membership_badge': 'platinum', 'relationship_type': 'livein',
            'profile_images': ['https://images.unsplash.com/photo-1560250097-0b93528c311a?w=400&h=400&fit=crop&crop=face']
        }
    ],
    'widowed_women': [
        {
            'full_name': 'Sunita Agarwal', 'age': 35, 'city': 'Jaipur', 'state': 'Rajasthan',
            'education': 'M.Com', 'occupation': 'Accountant',
            'annual_income': '8-12 Lakhs', 'height': '5\'3"', 'complexion': 'fair',
            'marital_status': 'widowed',
            'bio': 'Strong and independent woman looking for companionship and emotional support.',
            'hobbies': 'Reading, Cooking, Gardening, Volunteering',
            'membership_badge': 'gold', 'relationship_type': 'marriage',
            'profile_images': ['https://images.unsplash.com/photo-1580489944761-15a19d654956?w=400&h=400&fit=crop&crop=face']
        },
        {
            'full_name': 'Meera Jain', 'age': 38, 'city': 'Indore', 'state': 'Madhya Pradesh',
            'education': 'B.Ed', 'occupation': 'School Teacher',
            'annual_income': '5-8 Lakhs', 'height': '5\'2"', 'complexion': 'medium',
            'marital_status': 'widowed',
            'bio': 'Dedicated teacher and mother seeking a caring partner for life\'s journey.',
            'hobbies': 'Teaching, Reading, Music, Social Work',
            'membership_badge': 'silver', 'relationship_type': 'marriage',
            'profile_images': ['https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=400&h=400&fit=crop&crop=face']
        }
    ],
    'divorced_men': [
        {
            'full_name': 'Rajesh Verma', 'age': 36, 'city': 'Chennai', 'state': 'Tamil Nadu',
            'education': 'MBA', 'occupation': 'Business Development Manager',
            'annual_income': '15-20 Lakhs', 'height': '5\'10"', 'complexion': 'medium',
            'marital_status': 'divorced',
            'bio': 'Experienced professional seeking a fresh start with understanding and compatibility.',
            'hobbies': 'Business, Sports, Cooking, Travel',
            'membership_badge': 'gold', 'relationship_type': 'marriage',
            'profile_images': ['https://images.unsplash.com/photo-1507591064344-4c6ce005b128?w=400&h=400&fit=crop&crop=face']
        },
        {
            'full_name': 'Amit Desai', 'age': 40, 'city': 'Surat', 'state': 'Gujarat',
            'education': 'B.Com', 'occupation': 'Textile Business Owner',
            'annual_income': '25-40 Lakhs', 'height': '6\'0"', 'complexion': 'fair',
            'marital_status': 'divorced',
            'bio': 'Successful businessman looking for a life partner who values family and togetherness.',
            'hobbies': 'Business, Cricket, Reading, Family time',
            'membership_badge': 'platinum', 'relationship_type': 'marriage',
            'profile_images': ['https://images.unsplash.com/photo-1552374196-c4e7ffc6e126?w=400&h=400&fit=crop&crop=face']
        }
    ]
}

def create_matrimony_profiles():
    """Create diverse matrimony profiles"""
    
    with app.app_context():
        print("Creating matrimony demo profiles...")
        
        # Clear existing profiles for demo
        existing_count = MatrimonyProfile.query.count()
        print(f"Found {existing_count} existing profiles")
        
        profiles_created = 0
        
        # Create profiles for each category
        for category, profiles in profile_data.items():
            print(f"\nCreating {category} profiles...")
            
            for profile_data_item in profiles:
                try:
                    # Check if profile with this email already exists
                    email = f"{profile_data_item['full_name'].lower().replace(' ', '.')}@example.com"
                    existing = MatrimonyProfile.query.filter_by(email=email).first()
                    
                    if existing:
                        print(f"Profile for {profile_data_item['full_name']} already exists, skipping...")
                        continue
                    
                    # Create new profile
                    profile = MatrimonyProfile()
                    
                    # Basic information
                    profile.full_name = profile_data_item['full_name']
                    profile.age = profile_data_item['age']
                    profile.gender = 'Female' if category in ['girls', 'widowed_women'] else 'Male'
                    profile.marital_status = profile_data_item.get('marital_status', 'single')
                    profile.relationship_type = profile_data_item['relationship_type']
                    profile.email = email
                    profile.phone = f"+91{random.randint(7000000000, 9999999999)}"
                    
                    # Physical details
                    profile.height = profile_data_item['height']
                    profile.weight = f"{random.randint(45, 80)}kg"
                    profile.body_type = random.choice(['slim', 'average', 'athletic'])
                    profile.complexion = profile_data_item['complexion']
                    
                    # Location
                    profile.city = profile_data_item['city']
                    profile.state = profile_data_item['state']
                    profile.country = 'India'
                    
                    # Education & Career
                    profile.education = profile_data_item['education']
                    profile.occupation = profile_data_item['occupation']
                    profile.annual_income = profile_data_item['annual_income']
                    profile.company_name = f"{profile_data_item['occupation']} Company"
                    
                    # Personal details
                    profile.bio = profile_data_item['bio']
                    profile.hobbies = profile_data_item['hobbies']
                    profile.religion = random.choice(['Hindu', 'Muslim', 'Christian', 'Sikh'])
                    profile.mother_tongue = random.choice(['Hindi', 'English', 'Tamil', 'Telugu', 'Bengali'])
                    
                    # Partner preferences
                    profile.partner_age_min = max(18, profile.age - 5)
                    profile.partner_age_max = profile.age + 10
                    profile.partner_height_min = "5'0\"" if profile.gender == 'Female' else "5'2\""
                    profile.partner_height_max = "6'2\""
                    profile.partner_education = json.dumps(['Graduate', 'Post Graduate'])
                    profile.partner_income_min = profile.annual_income
                    
                    # Profile images (5 images per profile)
                    base_images = profile_data_item['profile_images']
                    all_images = []
                    for i in range(5):
                        # Rotate through available images and add variations
                        img_index = i % len(base_images)
                        img_url = base_images[img_index]
                        # Add slight variations to make it look like different photos
                        variations = ['?v=1', '?v=2', '?v=3', '?v=4', '?v=5']
                        all_images.append(img_url + variations[i])
                    
                    profile.profile_images = json.dumps(all_images)
                    profile.profile_photo = all_images[0]
                    
                    # Membership and verification
                    profile.membership_badge = profile_data_item['membership_badge']
                    profile.premium_member = profile.membership_badge in ['gold', 'platinum']
                    profile.is_verified = True
                    profile.profile_visible = True
                    profile.photo_visible = True
                    profile.contact_visible = profile.premium_member
                    
                    # Photo blur logic for basic members
                    if profile.membership_badge == 'basic':
                        # Some basic profiles created 10+ days ago (for demo)
                        if random.choice([True, False]):
                            profile.created_at = datetime.utcnow() - timedelta(days=15)
                            profile.photo_blurred = True
                            profile.photo_blur_date = datetime.utcnow() - timedelta(days=5)
                        else:
                            profile.created_at = datetime.utcnow() - timedelta(days=random.randint(1, 9))
                    else:
                        profile.created_at = datetime.utcnow() - timedelta(days=random.randint(1, 30))
                    
                    # Activity metrics
                    profile.profile_views = random.randint(50, 500)
                    profile.followers_count = random.randint(10, 100)
                    profile.following_count = random.randint(5, 50)
                    profile.shares_count = random.randint(1, 20)
                    profile.last_active = datetime.utcnow() - timedelta(hours=random.randint(1, 24))
                    
                    # Set password for login (optional)
                    from werkzeug.security import generate_password_hash
                    profile.password_hash = generate_password_hash('password123')
                    
                    db.session.add(profile)
                    profiles_created += 1
                    print(f"Created profile: {profile.full_name} ({profile.relationship_type}, {profile.membership_badge})")
                    
                except Exception as e:
                    print(f"Error creating profile for {profile_data_item['full_name']}: {str(e)}")
                    continue
        
        # Commit all profiles
        try:
            db.session.commit()
            print(f"\n✅ Successfully created {profiles_created} matrimony profiles!")
            print("\nProfile Summary:")
            print(f"- Total profiles: {MatrimonyProfile.query.count()}")
            print(f"- Marriage seekers: {MatrimonyProfile.query.filter_by(relationship_type='marriage').count()}")
            print(f"- Open relationship: {MatrimonyProfile.query.filter_by(relationship_type='open').count()}")
            print(f"- Live-in relationship: {MatrimonyProfile.query.filter_by(relationship_type='livein').count()}")
            print(f"- Basic members: {MatrimonyProfile.query.filter_by(membership_badge='basic').count()}")
            print(f"- Silver members: {MatrimonyProfile.query.filter_by(membership_badge='silver').count()}")
            print(f"- Gold members: {MatrimonyProfile.query.filter_by(membership_badge='gold').count()}")
            print(f"- Platinum members: {MatrimonyProfile.query.filter_by(membership_badge='platinum').count()}")
            
        except Exception as e:
            db.session.rollback()
            print(f"❌ Error committing profiles: {str(e)}")

if __name__ == "__main__":
    create_matrimony_profiles()