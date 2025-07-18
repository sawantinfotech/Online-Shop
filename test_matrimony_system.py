#!/usr/bin/env python3
"""
Comprehensive test script for matrimony system functionality
"""
import sys
import os

# Add the project root to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import app, db
from models import MatrimonyProfile
import requests
from datetime import datetime
import json

def test_matrimony_system():
    """Test the complete matrimony system"""
    
    with app.app_context():
        print("=== MATRIMONY SYSTEM TEST ===")
        print(f"Test started at: {datetime.now()}")
        
        # Test 1: Database connection and models
        print("\n1. Testing Database Connection...")
        try:
            total_profiles = MatrimonyProfile.query.count()
            print(f"✓ Database connected successfully")
            print(f"✓ Total matrimony profiles: {total_profiles}")
        except Exception as e:
            print(f"✗ Database connection failed: {e}")
            return False
        
        # Test 2: Sample profiles exist
        print("\n2. Testing Sample Profiles...")
        try:
            verified_profiles = MatrimonyProfile.query.filter_by(is_verified=True).count()
            visible_profiles = MatrimonyProfile.query.filter_by(profile_visible=True).count()
            
            print(f"✓ Verified profiles: {verified_profiles}")
            print(f"✓ Visible profiles: {visible_profiles}")
            
            # Test membership distribution
            for membership in ['basic', 'silver', 'gold', 'platinum']:
                count = MatrimonyProfile.query.filter_by(membership_badge=membership).count()
                print(f"✓ {membership.title()} members: {count}")
                
        except Exception as e:
            print(f"✗ Sample profiles test failed: {e}")
            return False
        
        # Test 3: Individual profile data
        print("\n3. Testing Individual Profile Data...")
        try:
            sample_profile = MatrimonyProfile.query.first()
            if sample_profile:
                print(f"✓ Sample profile: {sample_profile.full_name}")
                print(f"  - Age: {sample_profile.age}")
                print(f"  - City: {sample_profile.city}")
                print(f"  - Occupation: {sample_profile.occupation}")
                print(f"  - Membership: {sample_profile.membership_badge}")
                print(f"  - Verified: {sample_profile.is_verified}")
                print(f"  - Profile views: {sample_profile.profile_views}")
            else:
                print("✗ No sample profiles found")
                return False
        except Exception as e:
            print(f"✗ Individual profile test failed: {e}")
            return False
        
        print("\n=== ALL TESTS PASSED ===")
        return True

def test_matrimony_routes():
    """Test matrimony routes via HTTP requests"""
    
    base_url = "http://localhost:5000"
    
    print("\n=== MATRIMONY ROUTES TEST ===")
    
    routes_to_test = [
        ("/", "Homepage"),
        ("/matrimony", "Matrimony Platform"),
        ("/matrimony/register", "Matrimony Registration"),
        ("/matrimony/profiles", "Browse Profiles"),
        ("/matrimony/profile/1", "Individual Profile"),
        ("/apps", "Apps Showcase"),
        ("/apps/matrimony", "Matrimony App Detail")
    ]
    
    all_passed = True
    
    for route, description in routes_to_test:
        try:
            response = requests.get(f"{base_url}{route}", timeout=5)
            status = "✓" if response.status_code == 200 else "✗"
            print(f"{status} {description} ({route}): {response.status_code}")
            
            if response.status_code != 200:
                all_passed = False
                
        except requests.exceptions.RequestException as e:
            print(f"✗ {description} ({route}): Connection failed - {e}")
            all_passed = False
    
    return all_passed

def main():
    """Main test function"""
    
    print("Starting comprehensive matrimony system test...")
    
    # Test database and models
    db_test_passed = test_matrimony_system()
    
    # Test HTTP routes
    routes_test_passed = test_matrimony_routes()
    
    print("\n" + "="*50)
    print("FINAL TEST RESULTS:")
    print(f"Database & Models Test: {'PASSED' if db_test_passed else 'FAILED'}")
    print(f"HTTP Routes Test: {'PASSED' if routes_test_passed else 'FAILED'}")
    
    if db_test_passed and routes_test_passed:
        print("\n🎉 ALL TESTS PASSED! Matrimony system is fully functional.")
        return True
    else:
        print("\n❌ Some tests failed. Please check the issues above.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)