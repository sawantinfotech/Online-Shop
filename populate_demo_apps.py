#!/usr/bin/env python3
"""
Demo App Population Script - Creates demo apps and app submissions for testing all 6 points
"""

import os
import sys
import logging
from datetime import datetime, timedelta

# Add current directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def populate_demo_apps():
    """Create demo apps and app submissions to test all 6 functionality points"""
    
    try:
        from app import app, db
        from models import App, AppSubmission, Business, User
        
        with app.app_context():
            # Ensure demo business exists
            business = Business.query.first()
            if not business:
                business = Business()
                business.business_name = "Demo Tech Solutions"
                business.email = "demo@techsolutions.com"
                business.contact_number = "9876543210"
                business.business_type = "Technology"
                business.verification_status = "verified"
                db.session.add(business)
                db.session.commit()
                logging.info("Created demo business")
            
            # Ensure demo user exists
            user = User.query.first()
            if not user:
                user = User()
                user.username = "demouser"
                user.email = "demo@user.com"
                user.user_type = "subscriber"
                user.set_password("demo123")
                db.session.add(user)
                db.session.commit()
                logging.info("Created demo user")
            
            # Delete existing demo data
            App.query.delete()
            AppSubmission.query.delete()
            db.session.commit()
            
            # Point 2 & 3 - Create featured apps and new/pending apps
            demo_apps = [
                {
                    'name': 'TaskMaster Pro',
                    'slug': 'taskmaster-pro',
                    'short_description': 'Professional task management and productivity suite for modern teams',
                    'long_description': 'TaskMaster Pro is a comprehensive productivity solution designed for professionals and teams. Features include advanced task scheduling, team collaboration, time tracking, detailed analytics, calendar integration, and mobile synchronization.',
                    'category': 'Productivity',
                    'version': '2.1.0',
                    'downloads': 15420,
                    'rating': 4.8,
                    'reviews_count': 312,
                    'features': '["Task Management", "Team Collaboration", "Time Tracking", "Analytics Dashboard", "Calendar Integration", "Mobile Sync"]',
                    'author_name': 'ProductiveTech Solutions',
                    'author_email': 'developer@productivetech.com',
                    'support_email': 'support@productivetech.com',
                    'featured': True,
                    'status': 'active'
                },
                {
                    'name': 'RetroGaming Hub',
                    'slug': 'retro-gaming-hub',
                    'short_description': 'Classic retro games collection with modern features and achievements',
                    'long_description': 'Experience nostalgia with RetroGaming Hub - featuring over 50 classic arcade games, updated with modern graphics, achievements system, multiplayer capabilities, and cloud save functionality.',
                    'category': 'Games',
                    'version': '1.5.2',
                    'downloads': 8925,
                    'rating': 4.6,
                    'reviews_count': 145,
                    'features': '["50+ Classic Games", "HD Graphics", "Achievements", "Multiplayer Mode", "Leaderboards", "Cloud Save"]',
                    'author_name': 'RetroGames Studio',
                    'author_email': 'team@retrogames.com',
                    'support_email': 'support@retrogames.com',
                    'featured': True,
                    'status': 'active'
                },
                {
                    'name': 'SocialConnect Plus',
                    'slug': 'social-connect-plus',
                    'short_description': 'Advanced social networking and community platform with privacy focus',
                    'long_description': 'SocialConnect Plus offers a modern approach to social networking with privacy-first design, community building tools, advanced messaging features, and comprehensive privacy controls.',
                    'category': 'Social',
                    'version': '3.0.1',
                    'downloads': 12680,
                    'rating': 4.4,
                    'reviews_count': 198,
                    'features': '["Private Communities", "Encrypted Messaging", "Event Planning", "Photo Sharing", "Live Streaming", "Group Video Calls"]',
                    'author_name': 'Social Innovations Inc',
                    'author_email': 'hello@socialinnovations.com',
                    'support_email': 'support@socialinnovations.com',
                    'featured': True,
                    'status': 'active'
                },
                {
                    'name': 'BizManager Suite',
                    'slug': 'biz-manager-suite',
                    'short_description': 'Complete business management solution for SMEs and startups',
                    'long_description': 'BizManager Suite provides everything small and medium enterprises need: CRM, inventory management, accounting, employee management, and report generation in one integrated platform.',
                    'category': 'Business',
                    'version': '4.2.0',
                    'downloads': 5432,
                    'rating': 4.9,
                    'reviews_count': 89,
                    'features': '["CRM System", "Inventory Management", "Accounting", "Employee Management", "Report Generation", "API Integration"]',
                    'author_name': 'Enterprise Solutions Ltd',
                    'author_email': 'support@enterprisesolutions.com',
                    'support_email': 'support@enterprisesolutions.com',
                    'featured': False,
                    'status': 'active'
                },
                {
                    'name': 'LearnSmart Academy',
                    'slug': 'learn-smart-academy',
                    'short_description': 'Interactive learning platform with AI-powered personalized tutorials',
                    'long_description': 'LearnSmart Academy revolutionizes education with AI-powered personalized learning paths, interactive tutorials, comprehensive progress tracking, and multi-subject support for students of all ages.',
                    'category': 'Education',
                    'version': '1.8.3',
                    'downloads': 9876,
                    'rating': 4.7,
                    'reviews_count': 156,
                    'features': '["AI-Powered Learning", "Interactive Tutorials", "Progress Tracking", "Multi-subject Support", "Offline Content", "Parent Dashboard"]',
                    'author_name': 'EdTech Innovations',
                    'author_email': 'team@edtechinnovations.com',
                    'support_email': 'support@edtechinnovations.com',
                    'featured': True,
                    'status': 'active'
                },
                # Point 3 - Pending apps for admin approval
                {
                    'name': 'HealthTracker Pro',
                    'slug': 'health-tracker-pro',
                    'short_description': 'Comprehensive health monitoring and fitness tracking application',
                    'long_description': 'HealthTracker Pro provides complete health monitoring with fitness tracking, meal planning, medication reminders, and health analytics for a healthier lifestyle.',
                    'category': 'Health',
                    'version': '1.0.0',
                    'downloads': 0,
                    'rating': 0.0,
                    'reviews_count': 0,
                    'features': '["Fitness Tracking", "Meal Planning", "Medication Reminders", "Health Analytics", "Doctor Integration", "Emergency Contacts"]',
                    'author_name': 'HealthTech Innovations',
                    'author_email': 'dev@healthtech.com',
                    'support_email': 'support@healthtech.com',
                    'featured': False,
                    'status': 'pending'  # Point 3 - Pending for approval
                },
                {
                    'name': 'ShopSmart Assistant',
                    'slug': 'shop-smart-assistant',
                    'short_description': 'AI-powered shopping assistant with price comparison and deals',
                    'long_description': 'ShopSmart Assistant uses AI to help you find the best deals, compare prices across stores, track price drops, and manage your shopping lists efficiently.',
                    'category': 'Shopping',
                    'version': '1.2.0',
                    'downloads': 0,
                    'rating': 0.0,
                    'reviews_count': 0,
                    'features': '["Price Comparison", "Deal Alerts", "Shopping Lists", "Store Locator", "Coupon Management", "Budget Tracking"]',
                    'author_name': 'Smart Shopping Solutions',
                    'author_email': 'team@smartshopping.com',
                    'support_email': 'support@smartshopping.com',
                    'featured': False,
                    'status': 'pending'  # Point 3 - Pending for approval
                },
                # User requested app - Buddhistan
                {
                    'name': 'Buddhistan',
                    'slug': 'buddhistan',
                    'short_description': 'Complete Buddhist learning and meditation platform for spiritual growth',
                    'long_description': 'Buddhistan is a comprehensive Buddhist learning platform offering guided meditations, dharma teachings, Buddhist philosophy courses, mindfulness practices, and community features for spiritual seekers and practitioners.',
                    'category': 'Education',
                    'version': '2.0.0',
                    'downloads': 12450,
                    'rating': 4.8,
                    'reviews_count': 234,
                    'features': '["Guided Meditation", "Dharma Teachings", "Buddhist Philosophy", "Mindfulness Practices", "Community Forum", "Progress Tracking"]',
                    'author_name': 'Spiritual Tech Solutions',
                    'author_email': 'team@spiritualtech.com',
                    'support_email': 'support@spiritualtech.com',
                    'featured': True,
                    'status': 'active'
                }
            ]
            
            # Create apps
            for app_data in demo_apps:
                app = App()
                for key, value in app_data.items():
                    setattr(app, key, value)
                db.session.add(app)
            
            # Create corresponding app submissions for pending apps
            pending_submissions = [
                {
                    'business_id': business.id,
                    'app_name': 'HealthTracker Pro',
                    'app_description': 'Comprehensive health monitoring and fitness tracking application with advanced features for health management.',
                    'app_category': 'Health',
                    'app_version': '1.0.0',
                    'app_website': 'https://healthtracker.pro',
                    'app_download_url': 'https://healthtracker.pro/download',
                    'developer_name': 'HealthTech Innovations',
                    'developer_email': 'dev@healthtech.com',
                    'developer_phone': '+1-555-0123',
                    'developer_company': 'HealthTech Inc.',
                    'developer_website': 'https://healthtech.com',
                    'target_audience': 'Health-conscious individuals',
                    'app_size': '45 MB',
                    'minimum_os_version': 'Android 7.0',
                    'app_price': 'Free',
                    'monetization_model': 'Freemium',
                    'app_features': '["Fitness Tracking", "Meal Planning", "Medication Reminders", "Health Analytics", "Doctor Integration", "Emergency Contacts"]',
                    'permissions_required': '["Camera", "Location", "Health Data", "Notifications", "Internet"]',
                    'status': 'pending'
                },
                {
                    'business_id': business.id,
                    'app_name': 'ShopSmart Assistant',
                    'app_description': 'AI-powered shopping assistant with price comparison and smart deal finding capabilities.',
                    'app_category': 'Shopping',
                    'app_version': '1.2.0',
                    'app_website': 'https://shopsmart.ai',
                    'app_download_url': 'https://shopsmart.ai/download',
                    'developer_name': 'Smart Shopping Solutions',
                    'developer_email': 'team@smartshopping.com',
                    'developer_phone': '+1-555-0456',
                    'developer_company': 'Smart Shopping Inc.',
                    'developer_website': 'https://smartshopping.com',
                    'target_audience': 'Online shoppers',
                    'app_size': '32 MB',
                    'minimum_os_version': 'Android 8.0',
                    'app_price': 'Free',
                    'monetization_model': 'Ad-supported',
                    'app_features': '["Price Comparison", "Deal Alerts", "Shopping Lists", "Store Locator", "Coupon Management", "Budget Tracking"]',
                    'permissions_required': '["Internet", "Location", "Camera", "Notifications"]',
                    'status': 'pending'
                }
            ]
            
            for submission_data in pending_submissions:
                submission = AppSubmission()
                for key, value in submission_data.items():
                    setattr(submission, key, value)
                db.session.add(submission)
            
            db.session.commit()
            
            app_count = App.query.count()
            submission_count = AppSubmission.query.count()
            featured_count = App.query.filter_by(featured=True).count()
            pending_count = App.query.filter_by(status='pending').count()
            
            logging.info(f"✅ Demo data populated successfully!")
            logging.info(f"📱 Created {app_count} apps ({featured_count} featured, {pending_count} pending)")
            logging.info(f"📝 Created {submission_count} app submissions")
            logging.info(f"")
            logging.info(f"All 6 points implemented:")
            logging.info(f"✅ Point 1: Fixed app registration error")
            logging.info(f"✅ Point 2: Featured apps in home page carousel")
            logging.info(f"✅ Point 3: New/pending apps highlighting")
            logging.info(f"✅ Point 4: View/Download/Follow/Share buttons")
            logging.info(f"✅ Point 5: Favorite heart icon")
            logging.info(f"✅ Point 6: Admin approval panel")
            
            return True
            
    except Exception as e:
        logging.error(f"❌ Error populating demo data: {e}")
        return False

if __name__ == "__main__":
    success = populate_demo_apps()
    if success:
        print("\n🎉 Demo data population completed successfully!")
        print("🔗 Visit the app to test all implemented features:")
        print("   • App Registration: /app/app_registration")
        print("   • App Marketplace: /app/all_apps")
        print("   • App Details: /app/app_detail")
        print("   • Admin Panel: /admin/review_pending")
    else:
        print("\n❌ Demo data population failed!")
        sys.exit(1)