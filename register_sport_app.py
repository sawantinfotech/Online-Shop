#!/usr/bin/env python3
"""
Script to register a sport app for testing the approval workflow
"""

import os
import sys
from datetime import datetime, timedelta
sys.path.append('.')

from app import app, db
from models import App

def register_sport_app():
    """Register a sport app for testing"""
    with app.app_context():
        # Check if sport app already exists
        existing_app = App.query.filter_by(name="SportTracker Pro").first()
        if existing_app:
            print("Sport app already exists!")
            return existing_app

        # Create new sport app
        sport_app = App(
            name="SportTracker Pro",
            slug="sporttracker-pro",
            short_description="Track your fitness goals and sports activities with advanced analytics",
            long_description="SportTracker Pro is a comprehensive fitness and sports tracking application that helps you monitor your workouts, set goals, and analyze your performance. Features include GPS tracking, workout planning, social challenges, and detailed analytics.",
            category="Sports",
            author_name="FitTech Solutions",
            author_email="admin@fittech.com",
            version="1.2.3",
            downloads=0,
            rating=4.5,
            status="pending",  # This will trigger approval pending workflow
            logo_url="https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=64&h=64&fit=crop&crop=center",
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        
        db.session.add(sport_app)
        db.session.commit()
        
        print(f"✅ Sport app registered successfully!")
        print(f"   ID: {sport_app.id}")
        print(f"   Name: {sport_app.name}")
        print(f"   Status: {sport_app.status}")
        print(f"   Created: {sport_app.created_at}")
        
        return sport_app

if __name__ == "__main__":
    app_data = register_sport_app()
    print("\n🏃‍♂️ SportTracker Pro is now ready for testing!")
    print("   - It will show as 'Approval Pending' on app cards")
    print("   - It will be highlighted with warning colors")
    print("   - Admin can approve it from the admin panel")