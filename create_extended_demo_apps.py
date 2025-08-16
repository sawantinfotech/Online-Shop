#!/usr/bin/env python3
"""
Extended Demo Apps Generator for Mobile Shop Management System
Creates additional 10 demo apps including Buddhistan and other specialized apps
"""

import os
import sys
from datetime import datetime
import random

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import app, db
from models import App, Category

def generate_chakra_logo_svg():
    """Generate chakra logo SVG for Buddhistan app"""
    return '''<svg width="48" height="48" viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg">
        <circle cx="24" cy="24" r="20" fill="#FF6B35" stroke="#2E5266" stroke-width="2"/>
        <circle cx="24" cy="24" r="15" fill="none" stroke="#2E5266" stroke-width="1"/>
        <circle cx="24" cy="24" r="10" fill="none" stroke="#2E5266" stroke-width="1"/>
        <circle cx="24" cy="24" r="5" fill="none" stroke="#2E5266" stroke-width="1"/>
        <path d="M24 4 L26 12 L24 20 L22 12 Z" fill="#2E5266"/>
        <path d="M44 24 L36 26 L28 24 L36 22 Z" fill="#2E5266"/>
        <path d="M24 44 L22 36 L24 28 L26 36 Z" fill="#2E5266"/>
        <path d="M4 24 L12 22 L20 24 L12 26 Z" fill="#2E5266"/>
        <circle cx="24" cy="24" r="3" fill="#FFD60A"/>
    </svg>'''

def generate_app_logo_svg(app_name, primary_color, secondary_color="#FFFFFF"):
    """Generate SVG logo for app with custom colors"""
    icons = {
        'Mobile Shop Hub': '<path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z" fill="white"/>',
        'Matrimony': '<path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z" fill="white"/>',
        'Property': '<path d="M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8z" fill="white"/>',
        'Finance': '<path d="M11.8 10.9c-2.27-.59-3-1.2-3-2.15 0-1.09 1.01-1.85 2.7-1.85 1.78 0 2.44.85 2.5 2.1h2.21c-.07-1.72-1.12-3.3-3.21-3.81V3h-3v2.16c-1.94.42-3.5 1.68-3.5 3.61 0 2.31 1.91 3.46 4.7 4.13 2.5.6 3 1.48 3 2.41 0 .69-.49 1.79-2.7 1.79-2.06 0-2.87-.92-2.98-2.1h-2.2c.12 2.19 1.76 3.42 3.68 3.83V21h3v-2.15c1.95-.37 3.5-1.5 3.5-3.55 0-2.84-2.43-3.81-4.7-4.4z" fill="white"/>',
        'Placement': '<path d="M20 6h-2l-2-2H8l-2 2H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V8c0-1.1-.9-2-2-2zm-8 13c-2.76 0-5-2.24-5-5s2.24-5 5-5 5 2.24 5 5-2.24 5-5 5zm0-8c-1.65 0-3 1.35-3 3s1.35 3 3 3 3-1.35 3-3-1.35-3-3-3z" fill="white"/>',
        'Chat': '<path d="M20 2H4c-1.1 0-1.99.9-1.99 2L2 22l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zm-2 12H6v-2h12v2zm0-3H6V9h12v2zm0-3H6V6h12v2z" fill="white"/>',
        'Business': '<path d="M12 7V3H2v18h20V7H12zM6 19H4v-2h2v2zm0-4H4v-2h2v2zm0-4H4V9h2v2zm0-4H4V5h2v2zm4 12H8v-2h2v2zm0-4H8v-2h2v2zm0-4H8V9h2v2zm0-4H8V5h2v2zm10 12h-8v-2h2v-2h-2v-2h2v-2h-2V9h8v10zm-2-8h-2v2h2v-2zm0 4h-2v2h2v-2z" fill="white"/>',
        'Trust': '<path d="M12,1L3,5V11C3,16.55 6.84,21.74 12,23C17.16,21.74 21,16.55 21,11V5L12,1M10,17L6,13L7.41,11.59L10,14.17L16.59,7.58L18,9L10,17Z" fill="white"/>',
        'Legal': '<path d="M9 3v2H7v2h2v14c0 1.1.9 2 2 2h2c1.1 0 2-.9 2-2V7h2V5h-2V3H9zm2 2h2v2h-2V5zm0 4h2v2h-2V9zm0 4h2v2h-2v-2z" fill="white"/>'
    }
    
    icon = icons.get(app_name, '<circle cx="24" cy="24" r="8" fill="white"/>')
    
    return f'''<svg width="48" height="48" viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg">
        <rect width="48" height="48" rx="12" fill="{primary_color}"/>
        <g transform="translate(12, 12) scale(1)">
            {icon}
        </g>
    </svg>'''

def create_extended_demo_apps():
    """Create additional 10 demo apps with specialized features"""
    
    # Define the new apps with detailed information
    new_apps = [
        {
            'name': 'Buddhistan',
            'slug': 'buddhistan',
            'category': 'Public Services',
            'short_description': 'Public Services & Business Network platform for community development',
            'long_description': 'Buddhistan is a comprehensive platform designed to connect public services with business networks, facilitating community development and social progress. Our platform serves as a bridge between government services, local businesses, and citizens.',
            'features': [
                'Government Service Integration',
                'Business Directory & Networking',
                'Community Forum & Discussions', 
                'Service Request Management',
                'Digital Document Processing',
                'Multi-language Support',
                'Real-time Notifications',
                'Secure Data Protection'
            ],
            'author_name': 'Buddhistan Research & Development Organisation',
            'author_bio': 'Leading organization in digital governance and community development solutions',
            'website': 'https://www.buddhistan.org',
            'support_email': 'support@buddhistan.org',
            'version': '2.1.0',
            'downloads': '50000+',
            'rating': 4.8,
            'reviews_count': 1250,
            'logo_color': '#FF6B35',
            'featured': True,
            'social_links': {
                'buddhistan': 'https://buddhistan.org',
                'facebook': 'https://facebook.com/buddhistan',
                'twitter': 'https://twitter.com/buddhistan'
            }
        },
        {
            'name': 'Mobile Shop Hub',
            'slug': 'mobile-shop-hub',
            'category': 'Business',
            'short_description': 'Complete mobile shop management and e-commerce solution',
            'long_description': 'Mobile Shop Hub is the ultimate business management platform for mobile retailers, offering comprehensive tools for inventory management, customer relations, and online sales.',
            'features': [
                'Inventory Management',
                'Customer Relationship Management',
                'Point of Sale System',
                'Online Store Builder',
                'Payment Gateway Integration',
                'Analytics & Reporting',
                'Multi-location Support',
                'SEO Optimization Tools'
            ],
            'author_name': 'Mobile Shop Hub Team',
            'author_bio': 'Experts in retail technology and e-commerce solutions',
            'website': 'https://buddhistan.com',
            'support_email': 'support@buddhistan.com',
            'version': '3.2.1',
            'downloads': '75000+',
            'rating': 4.9,
            'reviews_count': 2100,
            'logo_color': '#007BFF',
            'featured': True
        },
        {
            'name': 'Matrimony',
            'slug': 'matrimony',
            'category': 'Social',
            'short_description': 'Find your perfect life partner with advanced matching algorithms',
            'long_description': 'Matrimony app connects hearts with our advanced matching system. Find compatible partners based on preferences, values, and lifestyle choices.',
            'features': [
                'Advanced Profile Matching',
                'Secure Messaging System',
                'Photo & Video Sharing',
                'Verification Services',
                'Privacy Controls',
                'Family Tree Integration',
                'Astrology Compatibility',
                'Multi-language Support'
            ],
            'author_name': 'Love Connect Solutions',
            'author_bio': 'Specialists in relationship technology and matchmaking services',
            'website': 'https://matrimony.buddhistan.com',
            'support_email': 'help@matrimony.com',
            'version': '4.5.2',
            'downloads': '120000+',
            'rating': 4.7,
            'reviews_count': 5600,
            'logo_color': '#E91E63',
            'featured': True
        },
        {
            'name': 'Property Hub',
            'slug': 'property-hub',
            'category': 'Real Estate',
            'short_description': 'Buy, sell, and rent properties with ease and transparency',
            'long_description': 'Property Hub revolutionizes real estate transactions with transparent pricing, virtual tours, and direct owner connections.',
            'features': [
                'Property Listings',
                'Virtual Property Tours',
                'Mortgage Calculator',
                'Price Analytics',
                'Legal Documentation',
                'Agent Directory',
                'Investment Analysis',
                'Location Insights'
            ],
            'author_name': 'PropTech Innovations',
            'author_bio': 'Leading real estate technology solutions provider',
            'website': 'https://property.buddhistan.com',
            'support_email': 'support@propertyhub.com',
            'version': '2.8.0',
            'downloads': '85000+',
            'rating': 4.6,
            'reviews_count': 3200,
            'logo_color': '#4CAF50',
            'featured': True
        },
        {
            'name': 'Finance Pro',
            'slug': 'finance-pro',
            'category': 'Finance',
            'short_description': 'Complete personal and business financial management solution',
            'long_description': 'Finance Pro offers comprehensive financial management tools for individuals and businesses, including budgeting, investments, and tax planning.',
            'features': [
                'Expense Tracking',
                'Investment Portfolio',
                'Tax Planning Tools',
                'Bill Reminders',
                'Financial Goals',
                'Market Analysis',
                'Crypto Tracking',
                'Business Accounting'
            ],
            'author_name': 'FinTech Solutions Ltd',
            'author_bio': 'Financial technology experts with 10+ years experience',
            'website': 'https://finance.buddhistan.com',
            'support_email': 'help@financepro.com',
            'version': '5.1.3',
            'downloads': '95000+',
            'rating': 4.8,
            'reviews_count': 4100,
            'logo_color': '#FF9800',
            'featured': True
        },
        {
            'name': 'Placement Portal',
            'slug': 'placement-portal',
            'category': 'Career',
            'short_description': 'Connect job seekers with employers for perfect career matches',
            'long_description': 'Placement Portal bridges the gap between talented job seekers and forward-thinking employers with AI-powered matching and career development tools.',
            'features': [
                'Job Matching Algorithm',
                'Resume Builder',
                'Interview Scheduler',
                'Skill Assessment',
                'Company Reviews',
                'Salary Insights',
                'Career Guidance',
                'Networking Events'
            ],
            'author_name': 'Career Connect Inc',
            'author_bio': 'Career development and recruitment technology specialists',
            'website': 'https://placement.buddhistan.com',
            'support_email': 'jobs@placementportal.com',
            'version': '3.7.1',
            'downloads': '110000+',
            'rating': 4.5,
            'reviews_count': 6800,
            'logo_color': '#9C27B0',
            'featured': True
        },
        {
            'name': 'ChatConnect',
            'slug': 'chatconnect',
            'category': 'Communication',
            'short_description': 'Secure and feature-rich messaging platform for all your communication needs',
            'long_description': 'ChatConnect provides secure, encrypted messaging with advanced features for personal and business communication.',
            'features': [
                'End-to-End Encryption',
                'Group Chats',
                'File Sharing',
                'Video Calls',
                'Screen Sharing',
                'Message Scheduling',
                'Auto-translate',
                'Business Integration'
            ],
            'author_name': 'SecureComm Technologies',
            'author_bio': 'Security-focused communication platform developers',
            'website': 'https://chat.buddhistan.com',
            'support_email': 'support@chatconnect.com',
            'version': '6.2.4',
            'downloads': '200000+',
            'rating': 4.7,
            'reviews_count': 8900,
            'logo_color': '#2196F3',
            'featured': False
        },
        {
            'name': 'Business Suite',
            'slug': 'business-suite',
            'category': 'Business',
            'short_description': 'All-in-one business management platform for modern enterprises',
            'long_description': 'Business Suite combines CRM, project management, accounting, and team collaboration tools in one powerful platform.',
            'features': [
                'Customer Relationship Management',
                'Project Management',
                'Team Collaboration',
                'Financial Management',
                'Document Management',
                'Time Tracking',
                'Analytics Dashboard',
                'API Integration'
            ],
            'author_name': 'Enterprise Solutions Group',
            'author_bio': 'Business software development and consulting experts',
            'website': 'https://business.buddhistan.com',
            'support_email': 'enterprise@businesssuite.com',
            'version': '4.3.2',
            'downloads': '65000+',
            'rating': 4.6,
            'reviews_count': 2800,
            'logo_color': '#607D8B',
            'featured': False
        },
        {
            'name': 'TrustGuard',
            'slug': 'trustguard',
            'category': 'Security',
            'short_description': 'Digital identity verification and trust management platform',
            'long_description': 'TrustGuard provides comprehensive digital identity verification and trust scoring for secure online transactions and interactions.',
            'features': [
                'Identity Verification',
                'Trust Scoring',
                'Document Authentication',
                'Background Checks',
                'Fraud Detection',
                'Compliance Management',
                'Risk Assessment',
                'Secure Storage'
            ],
            'author_name': 'CyberTrust Security',
            'author_bio': 'Cybersecurity and digital identity verification specialists',
            'website': 'https://trust.buddhistan.com',
            'support_email': 'security@trustguard.com',
            'version': '2.5.1',
            'downloads': '45000+',
            'rating': 4.9,
            'reviews_count': 1900,
            'logo_color': '#4CAF50',
            'featured': False
        },
        {
            'name': 'Legal Advisor',
            'slug': 'legal-advisor',
            'category': 'Legal',
            'short_description': 'Professional legal consultation and document management platform',
            'long_description': 'Legal Advisor connects users with qualified legal professionals and provides tools for legal document management and consultation.',
            'features': [
                'Lawyer Directory',
                'Legal Consultation',
                'Document Templates',
                'Case Management',
                'Legal Research',
                'Court Scheduling',
                'Contract Review',
                'Compliance Tracking'
            ],
            'author_name': 'LegalTech Innovations',
            'author_bio': 'Legal technology and consultation platform developers',
            'website': 'https://legal.buddhistan.com',
            'support_email': 'help@legaladvisor.com',
            'version': '3.1.0',
            'downloads': '38000+',
            'rating': 4.4,
            'reviews_count': 1500,
            'logo_color': '#795548',
            'featured': False
        }
    ]
    
    # Create apps in database
    for app_data in new_apps:
        existing_app = App.query.filter_by(slug=app_data['slug']).first()
        if existing_app:
            print(f"App {app_data['name']} already exists, skipping...")
            continue
            
        # Generate logo SVG
        if app_data['name'] == 'Buddhistan':
            logo_svg = generate_chakra_logo_svg()
        else:
            logo_svg = generate_app_logo_svg(app_data['name'], app_data['logo_color'])
        
        app = App(
            name=app_data['name'],
            slug=app_data['slug'],
            category=app_data['category'],
            short_description=app_data['short_description'],
            long_description=app_data['long_description'],
            features='\n'.join(app_data['features']),
            author_name=app_data['author_name'],
            author_bio=app_data['author_bio'],
            author_website=app_data['website'],
            support_email=app_data['support_email'],
            version=app_data['version'],
            downloads=app_data['downloads'],
            rating=app_data['rating'],
            reviews_count=app_data['reviews_count'],
            logo_url=logo_svg,
            featured=app_data.get('featured', False),
            status='active',
            created_at=datetime.now()
        )
        
        # Add social links if available
        if 'social_links' in app_data:
            app.social_links = str(app_data['social_links'])
        
        db.session.add(app)
    
    try:
        db.session.commit()
        print("✓ Extended demo apps created successfully!")
        
        # Display summary
        total_apps = App.query.count()
        featured_apps = App.query.filter_by(featured=True).count()
        
        print(f"\n=== EXTENDED DEMO APPS CREATED ===")
        print(f"Total Apps: {total_apps}")
        print(f"Featured Apps: {featured_apps}")
        
        print(f"\n=== NEW APPS ADDED ===")
        for app_data in new_apps:
            print(f"- {app_data['name']} ({app_data['category']}) - {app_data['downloads']} downloads, {app_data['rating']}★")
            
    except Exception as e:
        db.session.rollback()
        print(f"Error creating extended demo apps: {str(e)}")

def main():
    """Main function to create extended demo apps"""
    with app.app_context():
        create_extended_demo_apps()

if __name__ == '__main__':
    main()