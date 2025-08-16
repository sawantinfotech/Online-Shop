#!/usr/bin/env python3
"""
Create sample matrimony profiles for testing
"""
import sys
import os

# Add the project root to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import app, db
from models import MatrimonyProfile
from datetime import datetime
import json

def create_sample_profiles():
    """Create sample matrimony profiles"""
    
    sample_profiles = [
        {
            'full_name': 'Priya Sharma',
            'age': 28,
            'gender': 'Female',
            'marital_status': 'single',
            'email': 'priya.sharma@example.com',
            'phone': '+91-9876543210',
            'height': '5\'5"',
            'weight': '55kg',
            'body_type': 'slim',
            'complexion': 'fair',
            'city': 'Mumbai',
            'state': 'Maharashtra',
            'country': 'India',
            'education': 'MBA from IIM Bangalore',
            'occupation': 'Marketing Manager',
            'annual_income': '10-15 Lakhs',
            'company_name': 'Tech Solutions Ltd',
            'bio': 'I am a cheerful and ambitious person who loves traveling and reading. I believe in maintaining a work-life balance and enjoy spending time with family and friends. Looking for a caring and understanding life partner.',
            'relationship_type': 'marriage',
            'partner_age_min': 28,
            'partner_age_max': 35,
            'membership_badge': 'gold',
            'is_verified': True,
            'profile_views': 245
        },
        {
            'full_name': 'Rahul Patel',
            'age': 32,
            'gender': 'Male',
            'marital_status': 'single',
            'email': 'rahul.patel@example.com',
            'phone': '+91-9876543211',
            'height': '5\'10"',
            'weight': '75kg',
            'body_type': 'athletic',
            'complexion': 'medium',
            'city': 'Bangalore',
            'state': 'Karnataka',
            'country': 'India',
            'education': 'B.Tech Computer Science',
            'occupation': 'Software Engineer',
            'annual_income': '15-25 Lakhs',
            'company_name': 'Google India',
            'bio': 'I am a passionate software engineer who loves solving complex problems. I enjoy outdoor activities and believe in living life to the fullest. Looking for a partner who shares similar interests and values.',
            'relationship_type': 'marriage',
            'partner_age_min': 25,
            'partner_age_max': 30,
            'membership_badge': 'platinum',
            'is_verified': True,
            'profile_views': 320
        },
        {
            'full_name': 'Ananya Reddy',
            'age': 26,
            'gender': 'Female',
            'marital_status': 'single',
            'email': 'ananya.reddy@example.com',
            'phone': '+91-9876543212',
            'height': '5\'3"',
            'weight': '50kg',
            'body_type': 'slim',
            'complexion': 'fair',
            'city': 'Hyderabad',
            'state': 'Telangana',
            'country': 'India',
            'education': 'CA (Chartered Accountant)',
            'occupation': 'Financial Analyst',
            'annual_income': '8-12 Lakhs',
            'company_name': 'KPMG',
            'bio': 'I am a dedicated professional with strong family values. I love dancing and have been learning classical dance since childhood. Looking for a supportive and understanding partner.',
            'relationship_type': 'marriage',
            'partner_age_min': 26,
            'partner_age_max': 32,
            'membership_badge': 'silver',
            'is_verified': True,
            'profile_views': 180
        },
        {
            'full_name': 'Arjun Singh',
            'age': 29,
            'gender': 'Male',
            'marital_status': 'single',
            'email': 'arjun.singh@example.com',
            'phone': '+91-9876543213',
            'height': '6\'0"',
            'weight': '80kg',
            'body_type': 'athletic',
            'complexion': 'fair',
            'city': 'Delhi',
            'state': 'Delhi',
            'country': 'India',
            'education': 'MBBS, MD',
            'occupation': 'Doctor',
            'annual_income': '25-50 Lakhs',
            'company_name': 'AIIMS Delhi',
            'bio': 'I am a dedicated doctor who believes in serving humanity. I enjoy playing cricket and spending time with patients. Looking for a caring and compassionate life partner.',
            'relationship_type': 'marriage',
            'partner_age_min': 24,
            'partner_age_max': 28,
            'membership_badge': 'platinum',
            'is_verified': True,
            'profile_views': 415
        },
        {
            'full_name': 'Meera Joshi',
            'age': 25,
            'gender': 'Female',
            'marital_status': 'single',
            'email': 'meera.joshi@example.com',
            'phone': '+91-9876543214',
            'height': '5\'4"',
            'weight': '52kg',
            'body_type': 'slim',
            'complexion': 'medium',
            'city': 'Pune',
            'state': 'Maharashtra',
            'country': 'India',
            'education': 'B.Tech Electronics',
            'occupation': 'Software Developer',
            'annual_income': '8-12 Lakhs',
            'company_name': 'Infosys',
            'bio': 'I am a tech enthusiast who loves creating innovative solutions. I enjoy traveling and exploring different cultures. Looking for a partner who shares my passion for technology and adventure.',
            'relationship_type': 'marriage',
            'partner_age_min': 25,
            'partner_age_max': 30,
            'membership_badge': 'basic',
            'is_verified': False,
            'profile_views': 95
        }
    ]
    
    with app.app_context():
        for profile_data in sample_profiles:
            # Check if profile already exists
            existing = MatrimonyProfile.query.filter_by(email=profile_data['email']).first()
            if existing:
                print(f"Profile for {profile_data['full_name']} already exists, skipping...")
                continue
            
            # Create new profile
            profile = MatrimonyProfile(**profile_data)
            profile.created_at = datetime.utcnow()
            
            db.session.add(profile)
            print(f"✓ Created profile for {profile_data['full_name']}")
        
        db.session.commit()
        print("\n✅ Sample matrimony profiles created successfully!")
        
        # Display summary
        total_profiles = MatrimonyProfile.query.count()
        visible_profiles = MatrimonyProfile.query.filter_by(profile_visible=True).count()
        verified_profiles = MatrimonyProfile.query.filter_by(is_verified=True).count()
        
        print(f"\n=== MATRIMONY PROFILES SUMMARY ===")
        print(f"Total Profiles: {total_profiles}")
        print(f"Visible Profiles: {visible_profiles}")
        print(f"Verified Profiles: {verified_profiles}")
        
        # Display by membership type
        for membership in ['basic', 'silver', 'gold', 'platinum']:
            count = MatrimonyProfile.query.filter_by(membership_badge=membership).count()
            print(f"{membership.title()} Members: {count}")

if __name__ == "__main__":
    create_sample_profiles()