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
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "sqlite:///mobile_shop.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    "pool_recycle": 300,
    "pool_pre_ping": True,
}

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
