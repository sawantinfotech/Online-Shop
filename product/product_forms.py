from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, MultipleFileField
from wtforms import (
    StringField, TextAreaField, FloatField, IntegerField,
    SelectField, BooleanField, HiddenField, DecimalField
)
from wtforms.validators import (
    DataRequired, NumberRange, Optional, Length, ValidationError
)
import re

# PRODUCT SERVICE FORMS - COMPLETELY ISOLATED
# These forms handle all product-related operations

class ProductAddForm(FlaskForm):
    # Basic Product Information
    name = StringField('Product Name', validators=[
        DataRequired(message="Product name is required"),
        Length(min=2, max=200, message="Product name must be between 2 and 200 characters")
    ])
    
    description = TextAreaField('Full Description', validators=[
        Optional(),
        Length(max=5000, message="Description cannot exceed 5000 characters")
    ])
    
    short_description = StringField('Short Description', validators=[
        Optional(),
        Length(max=500, message="Short description cannot exceed 500 characters")
    ])
    
    # Product Identification
    sku = StringField('SKU (Stock Keeping Unit)', validators=[
        Optional(),
        Length(max=100, message="SKU cannot exceed 100 characters")
    ])
    
    barcode = StringField('Barcode', validators=[
        Optional(),
        Length(max=100, message="Barcode cannot exceed 100 characters")
    ])
    
    # Pricing Information
    price = DecimalField('Selling Price', validators=[
        DataRequired(message="Price is required"),
        NumberRange(min=0.01, message="Price must be greater than 0")
    ], places=2)
    
    original_price = DecimalField('Original Price (for discounts)', validators=[
        Optional(),
        NumberRange(min=0, message="Original price must be positive")
    ], places=2)
    
    cost_price = DecimalField('Cost Price', validators=[
        Optional(),
        NumberRange(min=0, message="Cost price must be positive")
    ], places=2)
    
    discount_percentage = FloatField('Discount Percentage', validators=[
        Optional(),
        NumberRange(min=0, max=100, message="Discount must be between 0 and 100")
    ])
    
    # Inventory Management
    quantity = IntegerField('Current Stock Quantity', validators=[
        DataRequired(message="Quantity is required"),
        NumberRange(min=0, message="Quantity cannot be negative")
    ])
    
    minimum_stock = IntegerField('Minimum Stock Alert', validators=[
        Optional(),
        NumberRange(min=0, message="Minimum stock cannot be negative")
    ])
    
    maximum_stock = IntegerField('Maximum Stock Capacity', validators=[
        Optional(),
        NumberRange(min=1, message="Maximum stock must be at least 1")
    ])
    
    # Physical Properties
    weight = FloatField('Weight (kg)', validators=[
        Optional(),
        NumberRange(min=0, message="Weight cannot be negative")
    ])
    
    dimensions = StringField('Dimensions (L x W x H)', validators=[
        Optional(),
        Length(max=100, message="Dimensions cannot exceed 100 characters")
    ])
    
    color = StringField('Color', validators=[
        Optional(),
        Length(max=50, message="Color cannot exceed 50 characters")
    ])
    
    size = StringField('Size', validators=[
        Optional(),
        Length(max=50, message="Size cannot exceed 50 characters")
    ])
    
    material = StringField('Material', validators=[
        Optional(),
        Length(max=100, message="Material cannot exceed 100 characters")
    ])
    
    # Category and Brand
    category = SelectField('Category', choices=[
        ('', 'Select Category'),
        ('electronics', 'Electronics'),
        ('clothing', 'Clothing & Fashion'),
        ('home_garden', 'Home & Garden'),
        ('books', 'Books & Media'),
        ('sports', 'Sports & Recreation'),
        ('toys', 'Toys & Games'),
        ('health', 'Health & Beauty'),
        ('automotive', 'Automotive'),
        ('food', 'Food & Beverages'),
        ('jewelry', 'Jewelry & Accessories'),
        ('other', 'Other')
    ], validators=[Optional()])
    
    brand = StringField('Brand', validators=[
        Optional(),
        Length(max=100, message="Brand cannot exceed 100 characters")
    ])
    
    manufacturer = StringField('Manufacturer', validators=[
        Optional(),
        Length(max=200, message="Manufacturer cannot exceed 200 characters")
    ])
    
    country_of_origin = StringField('Country of Origin', validators=[
        Optional(),
        Length(max=100, message="Country cannot exceed 100 characters")
    ])
    
    # Product Images
    main_image = FileField('Main Product Image', validators=[
        FileAllowed(['jpg', 'jpeg', 'png', 'gif'], 'Only image files allowed')
    ])
    
    additional_images = MultipleFileField('Additional Images (Optional)', validators=[
        FileAllowed(['jpg', 'jpeg', 'png', 'gif'], 'Only image files allowed')
    ])
    
    video_url = StringField('Product Video URL (YouTube, Vimeo, etc.)', validators=[
        Optional(),
        Length(max=500, message="Video URL cannot exceed 500 characters")
    ])
    
    # Product Settings
    status = SelectField('Product Status', choices=[
        ('active', 'Active (Published)'),
        ('draft', 'Draft (Not Published)'),
        ('inactive', 'Inactive (Hidden)')
    ], default='active', validators=[DataRequired()])
    
    featured = BooleanField('Featured Product')
    is_digital = BooleanField('Digital Product (No Shipping Required)')
    requires_shipping = BooleanField('Requires Shipping', default=True)
    
    # SEO and Marketing
    meta_title = StringField('SEO Title', validators=[
        Optional(),
        Length(max=200, message="SEO title cannot exceed 200 characters")
    ])
    
    meta_description = TextAreaField('SEO Description', validators=[
        Optional(),
        Length(max=500, message="SEO description cannot exceed 500 characters")
    ])
    
    tags = StringField('Tags (comma-separated)', validators=[
        Optional(),
        Length(max=500, message="Tags cannot exceed 500 characters")
    ])
    
    def validate_sku(self, field):
        if field.data:
            # SKU should contain only alphanumeric characters, hyphens, and underscores
            if not re.match(r'^[a-zA-Z0-9_-]+$', field.data):
                raise ValidationError('SKU can only contain letters, numbers, hyphens, and underscores')
    
    def validate_original_price(self, field):
        if field.data and self.price.data:
            if field.data < self.price.data:
                raise ValidationError('Original price should be greater than or equal to selling price')
    
    def validate_maximum_stock(self, field):
        if field.data and self.minimum_stock.data:
            if field.data <= self.minimum_stock.data:
                raise ValidationError('Maximum stock should be greater than minimum stock')

class ProductEditForm(ProductAddForm):
    # Inherits all fields from ProductAddForm
    # Additional field to track the product being edited
    product_id = HiddenField()

class ProductSearchForm(FlaskForm):
    search_term = StringField('Search Products', validators=[
        Optional(),
        Length(max=500, message="Search term cannot exceed 500 characters")
    ])
    
    category = SelectField('Category', choices=[
        ('', 'All Categories'),
        ('electronics', 'Electronics'),
        ('clothing', 'Clothing & Fashion'),
        ('home_garden', 'Home & Garden'),
        ('books', 'Books & Media'),
        ('sports', 'Sports & Recreation'),
        ('toys', 'Toys & Games'),
        ('health', 'Health & Beauty'),
        ('automotive', 'Automotive'),
        ('food', 'Food & Beverages'),
        ('jewelry', 'Jewelry & Accessories'),
        ('other', 'Other')
    ], validators=[Optional()])
    
    min_price = DecimalField('Minimum Price', validators=[
        Optional(),
        NumberRange(min=0, message="Minimum price cannot be negative")
    ], places=2)
    
    max_price = DecimalField('Maximum Price', validators=[
        Optional(),
        NumberRange(min=0, message="Maximum price cannot be negative")
    ], places=2)
    
    sort_by = SelectField('Sort By', choices=[
        ('newest', 'Newest First'),
        ('oldest', 'Oldest First'),
        ('price_low', 'Price: Low to High'),
        ('price_high', 'Price: High to Low'),
        ('name_asc', 'Name: A to Z'),
        ('name_desc', 'Name: Z to A'),
        ('rating', 'Highest Rated'),
        ('popular', 'Most Popular')
    ], default='newest', validators=[Optional()])
    
    in_stock_only = BooleanField('In Stock Only')
    featured_only = BooleanField('Featured Products Only')
    
    def validate_max_price(self, field):
        if field.data and self.min_price.data:
            if field.data <= self.min_price.data:
                raise ValidationError('Maximum price should be greater than minimum price')

class ProductReviewForm(FlaskForm):
    rating = SelectField('Rating', choices=[
        ('', 'Select Rating'),
        ('5', '5 Stars - Excellent'),
        ('4', '4 Stars - Very Good'),
        ('3', '3 Stars - Good'),
        ('2', '2 Stars - Fair'),
        ('1', '1 Star - Poor')
    ], validators=[DataRequired(message="Rating is required")])
    
    title = StringField('Review Title', validators=[
        Optional(),
        Length(max=200, message="Review title cannot exceed 200 characters")
    ])
    
    comment = TextAreaField('Your Review', validators=[
        DataRequired(message="Review comment is required"),
        Length(min=10, max=2000, message="Review must be between 10 and 2000 characters")
    ])
    
    pros = TextAreaField('What you liked (Optional)', validators=[
        Optional(),
        Length(max=1000, message="Pros cannot exceed 1000 characters")
    ])
    
    cons = TextAreaField('What could be improved (Optional)', validators=[
        Optional(),
        Length(max=1000, message="Cons cannot exceed 1000 characters")
    ])

class ProductCategoryForm(FlaskForm):
    name = StringField('Category Name', validators=[
        DataRequired(message="Category name is required"),
        Length(min=2, max=100, message="Category name must be between 2 and 100 characters")
    ])
    
    slug = StringField('URL Slug', validators=[
        DataRequired(message="URL slug is required"),
        Length(min=2, max=100, message="URL slug must be between 2 and 100 characters")
    ])
    
    description = TextAreaField('Description', validators=[
        Optional(),
        Length(max=1000, message="Description cannot exceed 1000 characters")
    ])
    
    icon = StringField('Icon Class (Font Awesome)', validators=[
        Optional(),
        Length(max=100, message="Icon class cannot exceed 100 characters")
    ])
    
    parent_category = SelectField('Parent Category', choices=[
        ('', 'No Parent (Top Level)')
    ], validators=[Optional()])
    
    sort_order = IntegerField('Sort Order', validators=[
        Optional(),
        NumberRange(min=0, message="Sort order cannot be negative")
    ])
    
    is_active = BooleanField('Active Category', default=True)
    
    meta_title = StringField('SEO Title', validators=[
        Optional(),
        Length(max=200, message="SEO title cannot exceed 200 characters")
    ])
    
    meta_description = TextAreaField('SEO Description', validators=[
        Optional(),
        Length(max=500, message="SEO description cannot exceed 500 characters")
    ])
    
    def validate_slug(self, field):
        if field.data:
            # Slug should contain only lowercase letters, numbers, and hyphens
            if not re.match(r'^[a-z0-9-]+$', field.data):
                raise ValidationError('URL slug can only contain lowercase letters, numbers, and hyphens')

class BulkProductUpdateForm(FlaskForm):
    action = SelectField('Bulk Action', choices=[
        ('', 'Select Action'),
        ('activate', 'Activate Selected'),
        ('deactivate', 'Deactivate Selected'),
        ('feature', 'Mark as Featured'),
        ('unfeature', 'Remove from Featured'),
        ('delete', 'Delete Selected')
    ], validators=[DataRequired(message="Please select an action")])
    
    selected_products = HiddenField('Selected Product IDs')
    
    # Additional fields for specific actions
    new_category = SelectField('New Category', choices=[], validators=[Optional()])
    price_adjustment = DecimalField('Price Adjustment (%)', validators=[
        Optional(),
        NumberRange(min=-100, max=1000, message="Price adjustment must be between -100% and 1000%")
    ], places=2)