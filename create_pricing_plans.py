#!/usr/bin/env python3
"""
Create demo pricing plans for subscriber categories
"""

from app import app, db
from models import PricingPlan, Category
import json

def create_demo_pricing_plans():
    """Create demo pricing plans for each category"""
    
    with app.app_context():
        # Clear existing pricing plans
        PricingPlan.query.delete()
        
        # Get all categories
        categories = Category.query.all()
        
        for category in categories:
            # Free Plan
            free_plan = PricingPlan(
                category_id=category.id,
                name='Free',
                description='Perfect for getting started',
                price=0.0,
                billing_cycle='monthly',
                duration='monthly',
                features=json.dumps([
                    'Basic product listing',
                    'Up to 10 products',
                    'Basic order management', 
                    'Customer support',
                    'Mobile-friendly design'
                ]),
                max_products=10,
                max_orders=50,
                max_customers=25,
                custom_homepage=False,
                advanced_analytics=False,
                priority_support=False,
                is_featured=False,
                is_active=True
            )
            db.session.add(free_plan)
            
            # Silver Plan
            silver_plan = PricingPlan(
                category_id=category.id,
                name='Silver',
                description='Great for growing businesses',
                price=29.99,
                billing_cycle='monthly',
                duration='monthly',
                features=json.dumps([
                    'Advanced product management',
                    'Up to 100 products',
                    'Order tracking & notifications',
                    'Customer management',
                    'Basic analytics',
                    'Email support',
                    'Custom branding'
                ]),
                max_products=100,
                max_orders=500,
                max_customers=200,
                custom_homepage=True,
                advanced_analytics=False,
                priority_support=False,
                is_featured=True,
                is_active=True
            )
            db.session.add(silver_plan)
            
            # Gold Plan
            gold_plan = PricingPlan(
                category_id=category.id,
                name='Gold',
                description='Best for established businesses',
                price=59.99,
                billing_cycle='monthly',
                duration='monthly',
                features=json.dumps([
                    'Unlimited products',
                    'Advanced order management',
                    'Customer segmentation',
                    'Advanced analytics & reports',
                    'Priority email support',
                    'Custom homepage design',
                    'Integration with payment gateways',
                    'SMS notifications'
                ]),
                max_products=-1,
                max_orders=-1,
                max_customers=-1,
                custom_homepage=True,
                advanced_analytics=True,
                priority_support=True,
                is_featured=False,
                is_active=True
            )
            db.session.add(gold_plan)
            
            # Platinum Plan
            platinum_plan = PricingPlan(
                category_id=category.id,
                name='Platinum',
                description='Enterprise solution with all features',
                price=99.99,
                billing_cycle='monthly',
                duration='monthly',
                features=json.dumps([
                    'Everything in Gold',
                    'Multi-store management',
                    'Advanced inventory tracking',
                    'Custom integrations',
                    'Dedicated account manager',
                    '24/7 phone support',
                    'Advanced security features',
                    'Custom reporting',
                    'API access'
                ]),
                max_products=-1,
                max_orders=-1,
                max_customers=-1,
                custom_homepage=True,
                advanced_analytics=True,
                priority_support=True,
                is_featured=False,
                is_active=True
            )
            db.session.add(platinum_plan)
        
        db.session.commit()
        
        total_plans = PricingPlan.query.count()
        print(f"✓ Created {total_plans} pricing plans successfully!")
        
        # Show sample plans
        print("\n=== SAMPLE PRICING PLANS ===")
        for category in categories[:3]:  # Show first 3 categories
            print(f"\n{category.name} Plans:")
            plans = PricingPlan.query.filter_by(category_id=category.id).all()
            for plan in plans:
                print(f"  - {plan.name}: ${plan.price}/month")

if __name__ == "__main__":
    create_demo_pricing_plans()