#!/usr/bin/env python3
"""
Create comprehensive admin sections for super admin control
"""

from app import app, db
from models import AdminSection

def create_admin_sections():
    """Create all admin sections for comprehensive control"""
    
    admin_sections = [
        {
            'name': 'App Management',
            'slug': 'apps',
            'description': 'Manage all applications, submissions, and app store content',
            'icon': 'fas fa-mobile-alt',
            'sort_order': 1
        },
        {
            'name': 'Blog & Content',
            'slug': 'blog',
            'description': 'Manage blog posts, articles, and content publishing',
            'icon': 'fas fa-blog',
            'sort_order': 2
        },
        {
            'name': 'Business Management',
            'slug': 'business',
            'description': 'Manage business registrations, verifications, and profiles',
            'icon': 'fas fa-building',
            'sort_order': 3
        },
        {
            'name': 'Delivery System',
            'slug': 'delivery',
            'description': 'Manage delivery partners, assignments, and logistics',
            'icon': 'fas fa-truck',
            'sort_order': 4
        },
        {
            'name': 'Matrimonial Platform',
            'slug': 'matrimony',
            'description': 'Manage matrimonial profiles, matching, and premium features',
            'icon': 'fas fa-heart',
            'sort_order': 5
        },
        {
            'name': 'Pricing & Plans',
            'slug': 'pricing',
            'description': 'Manage subscription plans, pricing, and billing',
            'icon': 'fas fa-tags',
            'sort_order': 6
        },
        {
            'name': 'User Profiles',
            'slug': 'users',
            'description': 'Edit and manage all user profiles and permissions',
            'icon': 'fas fa-users',
            'sort_order': 7
        },
        {
            'name': 'Advertising',
            'slug': 'advertising',
            'description': 'Manage ad campaigns, placements, and revenue',
            'icon': 'fas fa-ad',
            'sort_order': 8
        },
        {
            'name': 'Categories',
            'slug': 'categories',
            'description': 'Manage all system categories and classifications',
            'icon': 'fas fa-list',
            'sort_order': 9
        },
        {
            'name': 'SEO Management',
            'slug': 'seo',
            'description': 'Manage SEO settings, meta tags, and search optimization',
            'icon': 'fas fa-search',
            'sort_order': 10
        },
        {
            'name': 'Marketing Tools',
            'slug': 'marketing',
            'description': 'Email campaigns, SMS marketing, and promotional tools',
            'icon': 'fas fa-bullhorn',
            'sort_order': 11
        },
        {
            'name': 'Testing & QA',
            'slug': 'testing',
            'description': 'System testing, quality assurance, and debugging tools',
            'icon': 'fas fa-bug',
            'sort_order': 12
        },
        {
            'name': 'Analytics & Reports',
            'slug': 'analytics',
            'description': 'System analytics, performance reports, and insights',
            'icon': 'fas fa-chart-line',
            'sort_order': 13
        },
        {
            'name': 'Security & Permissions',
            'slug': 'security',
            'description': 'Manage user permissions, security settings, and access control',
            'icon': 'fas fa-shield-alt',
            'sort_order': 14
        },
        {
            'name': 'System Settings',
            'slug': 'system',
            'description': 'Core system configuration and administrative settings',
            'icon': 'fas fa-cogs',
            'sort_order': 15
        }
    ]
    
    with app.app_context():
        print("Creating admin sections...")
        
        sections_created = 0
        
        for section_data in admin_sections:
            # Check if section already exists
            existing = AdminSection.query.filter_by(slug=section_data['slug']).first()
            
            if existing:
                print(f"Section '{section_data['name']}' already exists, updating...")
                existing.description = section_data['description']
                existing.icon = section_data['icon']
                existing.sort_order = section_data['sort_order']
            else:
                section = AdminSection(
                    name=section_data['name'],
                    slug=section_data['slug'],
                    description=section_data['description'],
                    icon=section_data['icon'],
                    is_active=True,
                    sort_order=section_data['sort_order']
                )
                db.session.add(section)
                sections_created += 1
                print(f"Created section: {section_data['name']}")
        
        try:
            db.session.commit()
            print(f"\n✅ Successfully created/updated {len(admin_sections)} admin sections!")
            print("\nAdmin sections available:")
            for section in AdminSection.query.order_by(AdminSection.sort_order).all():
                print(f"- {section.name} ({section.slug})")
                
        except Exception as e:
            db.session.rollback()
            print(f"❌ Error creating admin sections: {str(e)}")

if __name__ == "__main__":
    create_admin_sections()