from datetime import datetime
from app import db
import json

# PRODUCT SERVICE MODELS - COMPLETELY ISOLATED
# These models are independent and don't conflict with any other service

class ProductItem(db.Model):
    __tablename__ = 'product_items_isolated'
    
    id = db.Column(db.Integer, primary_key=True)
    
    # Product Information
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    short_description = db.Column(db.String(500))
    sku = db.Column(db.String(100), unique=True)
    barcode = db.Column(db.String(100))
    
    # Pricing
    price = db.Column(db.Float, nullable=False)
    original_price = db.Column(db.Float)  # For discounts
    cost_price = db.Column(db.Float)  # For profit calculation
    discount_percentage = db.Column(db.Float, default=0.0)
    
    # Inventory
    quantity = db.Column(db.Integer, default=0)
    minimum_stock = db.Column(db.Integer, default=5)
    maximum_stock = db.Column(db.Integer, default=1000)
    
    # Physical Properties
    weight = db.Column(db.Float)  # in kg
    dimensions = db.Column(db.String(100))  # LxWxH format
    color = db.Column(db.String(50))
    size = db.Column(db.String(50))
    material = db.Column(db.String(100))
    
    # Category and Organization
    category_id = db.Column(db.Integer, nullable=True)  # No foreign key constraint for isolation
    brand = db.Column(db.String(100))
    manufacturer = db.Column(db.String(200))
    country_of_origin = db.Column(db.String(100))
    
    # Images and Media
    main_image = db.Column(db.String(500))  # Primary product image
    images = db.Column(db.Text)  # JSON array of additional image URLs
    video_url = db.Column(db.String(500))  # Product demo video
    
    # Product Status
    status = db.Column(db.String(20), default='active')  # active, inactive, discontinued, draft
    featured = db.Column(db.Boolean, default=False)
    is_digital = db.Column(db.Boolean, default=False)
    requires_shipping = db.Column(db.Boolean, default=True)
    
    # SEO and Marketing
    meta_title = db.Column(db.String(200))
    meta_description = db.Column(db.Text)
    tags = db.Column(db.Text)  # JSON array of tags
    
    # User Information (connected to main app's User system)
    added_by = db.Column(db.Integer, nullable=False)  # User ID from main app
    approved_by = db.Column(db.Integer)  # Admin user ID
    
    # Analytics
    view_count = db.Column(db.Integer, default=0)
    purchase_count = db.Column(db.Integer, default=0)
    rating_average = db.Column(db.Float, default=0.0)
    rating_count = db.Column(db.Integer, default=0)
    
    # Timestamps
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    published_at = db.Column(db.DateTime)
    
    def get_images(self):
        if not self.images:
            return []
        try:
            return json.loads(self.images)
        except (json.JSONDecodeError, ValueError):
            return []
    
    def set_images(self, images_list):
        self.images = json.dumps(images_list)
    
    def get_tags(self):
        if not self.tags:
            return []
        try:
            return json.loads(self.tags)
        except (json.JSONDecodeError, ValueError):
            return self.tags.split(',') if self.tags else []
    
    def set_tags(self, tags_list):
        self.tags = json.dumps(tags_list)
    
    def is_in_stock(self):
        return self.quantity > 0
    
    def is_low_stock(self):
        return self.quantity <= self.minimum_stock
    
    def get_discount_amount(self):
        if self.original_price and self.discount_percentage:
            return self.original_price * (self.discount_percentage / 100)
        return 0.0
    
    def get_final_price(self):
        return self.price

class ProductCategory(db.Model):
    __tablename__ = 'product_categories_isolated'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    slug = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text)
    icon = db.Column(db.String(100))  # Font Awesome icon class
    image_url = db.Column(db.String(500))
    parent_id = db.Column(db.Integer)  # For subcategories, no foreign key for isolation
    sort_order = db.Column(db.Integer, default=0)
    is_active = db.Column(db.Boolean, default=True)
    meta_title = db.Column(db.String(200))
    meta_description = db.Column(db.Text)
    product_count = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class ProductImage(db.Model):
    __tablename__ = 'product_images_isolated'
    
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, nullable=False)  # No foreign key for isolation
    image_url = db.Column(db.String(500), nullable=False)
    alt_text = db.Column(db.String(200))
    title = db.Column(db.String(200))
    sort_order = db.Column(db.Integer, default=0)
    is_primary = db.Column(db.Boolean, default=False)
    file_size = db.Column(db.Integer)  # in bytes
    file_type = db.Column(db.String(20))  # jpg, png, etc.
    uploaded_by = db.Column(db.Integer, nullable=False)  # User ID
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class ProductReview(db.Model):
    __tablename__ = 'product_reviews_isolated'
    
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, nullable=False)  # No foreign key for isolation
    user_id = db.Column(db.Integer, nullable=False)  # User ID from main app
    rating = db.Column(db.Integer, nullable=False)  # 1-5 stars
    title = db.Column(db.String(200))
    comment = db.Column(db.Text)
    pros = db.Column(db.Text)  # What user liked
    cons = db.Column(db.Text)  # What user didn't like
    verified_purchase = db.Column(db.Boolean, default=False)
    helpful_count = db.Column(db.Integer, default=0)
    status = db.Column(db.String(20), default='pending')  # pending, approved, rejected
    reviewed_by = db.Column(db.Integer)  # Admin who reviewed
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class ProductFavorite(db.Model):
    __tablename__ = 'product_favorites_isolated'
    
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, nullable=False)  # No foreign key for isolation
    user_id = db.Column(db.Integer, nullable=False)  # User ID from main app
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Ensure unique user-product combination
    __table_args__ = (db.UniqueConstraint('user_id', 'product_id', name='unique_user_product_favorite'),)

class ProductView(db.Model):
    __tablename__ = 'product_views_isolated'
    
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, nullable=False)  # No foreign key for isolation
    user_id = db.Column(db.Integer)  # User ID from main app (nullable for anonymous views)
    ip_address = db.Column(db.String(45))  # IPv4 or IPv6
    user_agent = db.Column(db.Text)
    referrer = db.Column(db.String(500))
    view_duration = db.Column(db.Integer)  # seconds spent viewing
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class ProductSearch(db.Model):
    __tablename__ = 'product_searches_isolated'
    
    id = db.Column(db.Integer, primary_key=True)
    search_term = db.Column(db.String(500), nullable=False)
    user_id = db.Column(db.Integer)  # User ID from main app (nullable for anonymous)
    results_count = db.Column(db.Integer, default=0)
    ip_address = db.Column(db.String(45))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class ProductInventoryLog(db.Model):
    __tablename__ = 'product_inventory_logs_isolated'
    
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, nullable=False)  # No foreign key for isolation
    change_type = db.Column(db.String(20), nullable=False)  # add, remove, sold, returned, damaged
    quantity_before = db.Column(db.Integer, nullable=False)
    quantity_changed = db.Column(db.Integer, nullable=False)
    quantity_after = db.Column(db.Integer, nullable=False)
    reason = db.Column(db.String(200))
    notes = db.Column(db.Text)
    user_id = db.Column(db.Integer, nullable=False)  # User who made the change
    created_at = db.Column(db.DateTime, default=datetime.utcnow)