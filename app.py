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
database_url = os.environ.get("DATABASE_URL", "sqlite:///mobile_shop.db")

# Check if the database URL is accessible
try:
    import psycopg2
    from urllib.parse import urlparse
    
    if database_url.startswith("postgresql://"):
        # Test PostgreSQL connection
        conn = psycopg2.connect(database_url)
        conn.close()
        app.config["SQLALCHEMY_DATABASE_URI"] = database_url
        app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
            "pool_recycle": 300,
            "pool_pre_ping": True,
        }
        logging.info("Using PostgreSQL database")
    else:
        app.config["SQLALCHEMY_DATABASE_URI"] = database_url
        logging.info("Using SQLite database")
except Exception as e:
    logging.warning(f"PostgreSQL connection failed: {e}")
    logging.info("Falling back to SQLite database")
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mobile_shop.db"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# File upload configuration
app.config["UPLOAD_FOLDER"] = "uploads"
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024  # 16MB max file size

# Initialize database
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Create upload directory if it doesn't exist
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

with app.app_context():
    # Import models to create tables
    import models  # noqa: F401
    db.create_all()
    logging.info("Database tables created")
    
    # Register admin blueprint
    from admin import admin_bp
    app.register_blueprint(admin_bp)
    
    # Initialize default categories
    from models import Category
    if Category.query.count() == 0:
        categories = [
            Category(name='Electronics', description='Electronic devices and accessories'),
            Category(name='Clothing', description='Apparel and fashion items'),
            Category(name='Home & Garden', description='Home improvement and gardening'),
            Category(name='Sports', description='Sports equipment and accessories'),
            Category(name='Books', description='Books and educational materials'),
            Category(name='Health & Beauty', description='Health and beauty products'),
            Category(name='Food & Beverages', description='Food items and beverages'),
            Category(name='Other', description='Other products')
        ]
        
        for category in categories:
            db.session.add(category)
        
        db.session.commit()
        logging.info("Default categories created")
