from app import db
from datetime import datetime

# SHOPPING CART MODELS - ISOLATED IN PRODUCT SERVICE
# These models handle shopping cart functionality

class ProductCart(db.Model):
    __tablename__ = 'product_cart_isolated'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)  # Remove FK constraint for now
    session_id = db.Column(db.String(100))  # For guest users
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    status = db.Column(db.String(20), default='active')  # active, abandoned, converted
    
    # Relationships
    items = db.relationship('ProductCartItem', backref='cart', lazy='dynamic', cascade='all, delete-orphan')
    
    def get_total_items(self):
        """Get total quantity of items in cart"""
        return sum(item.quantity for item in self.items)
    
    def get_total_price(self):
        """Calculate total price of all items in cart"""
        return sum(item.get_total_price() for item in self.items)
    
    def get_items_count(self):
        """Get number of unique items in cart"""
        return self.items.count()

class ProductCartItem(db.Model):
    __tablename__ = 'product_cart_items_isolated'
    
    id = db.Column(db.Integer, primary_key=True)
    cart_id = db.Column(db.Integer, db.ForeignKey('product_cart_isolated.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product_items_isolated.id'), nullable=False)
    quantity = db.Column(db.Integer, default=1, nullable=False)
    unit_price = db.Column(db.Float, nullable=False)  # Price at time of adding to cart
    added_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    product = db.relationship('ProductItem', backref='cart_items')
    
    def get_total_price(self):
        """Get total price for this cart item"""
        return self.quantity * self.unit_price
    
    def update_quantity(self, new_quantity):
        """Update quantity and timestamp"""
        self.quantity = max(1, new_quantity)  # Minimum quantity is 1
        self.updated_at = datetime.utcnow()

class ProductOrder(db.Model):
    __tablename__ = 'product_orders_isolated'
    
    id = db.Column(db.Integer, primary_key=True)
    order_number = db.Column(db.String(100), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    # Order details
    total_amount = db.Column(db.Float, nullable=False)
    tax_amount = db.Column(db.Float, default=0.0)
    shipping_amount = db.Column(db.Float, default=0.0)
    discount_amount = db.Column(db.Float, default=0.0)
    final_amount = db.Column(db.Float, nullable=False)
    
    # Order status
    status = db.Column(db.String(20), default='pending')  # pending, confirmed, processing, shipped, delivered, cancelled
    payment_status = db.Column(db.String(20), default='pending')  # pending, paid, failed, refunded
    
    # Shipping details
    shipping_address = db.Column(db.Text)
    shipping_method = db.Column(db.String(50))
    tracking_number = db.Column(db.String(100))
    
    # Timestamps
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    estimated_delivery = db.Column(db.DateTime)
    delivered_at = db.Column(db.DateTime)
    
    # Relationships
    items = db.relationship('ProductOrderItem', backref='order', lazy='dynamic', cascade='all, delete-orphan')
    
    def generate_order_number(self):
        """Generate unique order number"""
        import uuid
        self.order_number = f"ORD-{datetime.utcnow().strftime('%Y%m%d')}-{str(uuid.uuid4())[:8].upper()}"

class ProductOrderItem(db.Model):
    __tablename__ = 'product_order_items_isolated'
    
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('product_orders_isolated.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product_items_isolated.id'), nullable=False)
    
    quantity = db.Column(db.Integer, nullable=False)
    unit_price = db.Column(db.Float, nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    
    # Product details at time of order (in case product is deleted)
    product_name = db.Column(db.String(200))
    product_sku = db.Column(db.String(100))
    
    # Relationships
    product = db.relationship('ProductItem', backref='order_items')