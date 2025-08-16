from datetime import datetime
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
import json

# BUSINESS SERVICE MODELS - ISOLATED
# These models are disconnected from the main application
# but preserved for future reintegration

class Business(db.Model):
    __tablename__ = 'businesses_isolated'  # Renamed to avoid conflicts
    
    id = db.Column(db.Integer, primary_key=True)
    business_name = db.Column(db.String(200), nullable=False)
    logo_url = db.Column(db.String(500))
    license_number = db.Column(db.String(100))
    contact_number = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    address = db.Column(db.Text)
    business_type = db.Column(db.String(100))
    verification_status = db.Column(db.String(20), default='pending')
    documents = db.Column(db.Text)  # JSON string of document URLs
    gpay_enabled = db.Column(db.Boolean, default=False)
    paytm_enabled = db.Column(db.Boolean, default=False)
    brainlo_enabled = db.Column(db.Boolean, default=False)
    password_hash = db.Column(db.String(256))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def get_documents(self):
        return json.loads(self.documents) if self.documents else []
    
    def set_documents(self, documents_list):
        self.documents = json.dumps(documents_list)

# Additional business-related models would go here
class BusinessProduct(db.Model):
    __tablename__ = 'business_products_isolated'
    
    id = db.Column(db.Integer, primary_key=True)
    business_id = db.Column(db.Integer, nullable=False)  # No foreign key constraint
    product_name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, default=0)
    images = db.Column(db.Text)  # JSON string of image URLs
    weight = db.Column(db.Float)  # in kg
    dimensions = db.Column(db.String(100))  # LxWxH format
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class BusinessCustomer(db.Model):
    __tablename__ = 'business_customers_isolated'
    
    id = db.Column(db.Integer, primary_key=True)
    business_id = db.Column(db.Integer, nullable=False)  # No foreign key constraint
    name = db.Column(db.String(200), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(120))
    address = db.Column(db.Text)
    social_media = db.Column(db.Text)  # JSON string
    groups = db.Column(db.Text)  # JSON string of group names
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)