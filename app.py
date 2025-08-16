import os
import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from werkzeug.middleware.proxy_fix import ProxyFix

# Configure logging
logging.basicConfig(level=logging.DEBUG)

class Base(DeclarativeBase):
    pass

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "mobile-shop-secret-key")
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

# Database configuration
database_url = os.environ.get("DATABASE_URL")

if database_url:
    app.config["SQLALCHEMY_DATABASE_URI"] = database_url
    app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
        "pool_recycle": 300,
        "pool_pre_ping": True,
    }
    logging.info("Using PostgreSQL database")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mobile_shop.db"
    logging.info("Using SQLite database")

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# File upload configuration
app.config["UPLOAD_FOLDER"] = "uploads"
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024  # 16MB max file size

# Initialize database
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Create upload directory if it doesn't exist
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

# Import models to create tables
import models  # noqa: F401
# Import Product service models to create tables
import product.product_models  # noqa: F401
import json

# Add JSON filter for templates
app.jinja_env.filters['from_json'] = json.loads

# Function to initialize demo data
def init_demo_data():
    """Initialize demo data for the application"""
    try:
        # Import required models (only existing ones)  
        from models import User, Service, App, DeliveryProfile, Product, Order, Payment
        from datetime import datetime, timedelta
        import random
        
        db.create_all()
        logging.info("Database tables created")
        
        #Auto-populate demo data on startup for immediate showcase
        if Service.query.count() == 0:
            logging.info("Populating demo data for immediate showcase...")
            # Services
            services_data = [
                {'name': 'User', 'description': 'User platform'},
                {'name': 'Product', 'description': 'Product platform'},
                {'name': 'Delivery', 'description': 'Delivery service'},
                {'name': 'App', 'description': 'App marketplace'}
            ]
            
            for service_data in services_data:
                service = Service()
                service.name = service_data['name']
                service.description = service_data['description']
                db.session.add(service)
            
            try:
                db.session.commit()
                logging.info("Demo services created successfully")
            except Exception as e:
                logging.error(f"Error creating demo services: {e}")
                db.session.rollback()
            
            logging.info("✅ Demo data populated successfully!")
            
    except Exception as e:
        logging.error(f"Error initializing demo data: {e}")
        db.session.rollback()

# Initialize demo data with app context
with app.app_context():
    init_demo_data()
    
    # Register admin blueprint
    try:
        from admin import admin_bp
        app.register_blueprint(admin_bp)
        logging.info("Admin blueprint registered")
    except ImportError:
        logging.warning("Admin blueprint not found, skipping registration")