from flask import Blueprint, render_template, request, redirect, url_for, flash, session, jsonify, send_from_directory
from werkzeug.utils import secure_filename
from product.product_models import (
    ProductItem, ProductCategory, ProductImage, ProductReview, 
    ProductFavorite, ProductView, ProductSearch, ProductInventoryLog
)
from product.cart_models import ProductCart, ProductCartItem, ProductOrder, ProductOrderItem
from product.product_forms import (
    ProductAddForm, ProductEditForm, ProductSearchForm, 
    ProductReviewForm, ProductCategoryForm, BulkProductUpdateForm
)
from app import db
import os
import json
from datetime import datetime
import uuid
from sqlalchemy import or_, and_, desc, asc, func

# PRODUCT SERVICE ROUTES - COMPLETELY ISOLATED
# These routes handle all product-related operations without affecting other services

# Create product blueprint (will be registered with main app)
product_bp = Blueprint('product', __name__, url_prefix='/product')

def product_login_required(f):
    """Decorator to require user login for product operations"""
    from functools import wraps
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in to access this page.', 'error')
            return redirect(url_for('user_login'))
        return f(*args, **kwargs)
    return decorated_function

def get_current_user():
    """Get current logged-in user from main app's User model"""
    if 'user_id' in session:
        from models import User
        return User.query.get(session['user_id'])
    return None

def save_uploaded_file(file, folder='products'):
    """Save uploaded file and return the file path"""
    if file and file.filename:
        # Generate unique filename
        filename = secure_filename(file.filename)
        name, ext = os.path.splitext(filename)
        unique_filename = f"{name}_{uuid.uuid4().hex[:8]}{ext}"
        
        # Create upload directory if it doesn't exist
        upload_dir = os.path.join('uploads', folder)
        os.makedirs(upload_dir, exist_ok=True)
        
        # Save file
        file_path = os.path.join(upload_dir, unique_filename)
        file.save(file_path)
        return file_path
    return None

@product_bp.route('/')
def product_home():
    """Product service main page - displays featured products and categories"""
    try:
        # Get featured products
        featured_products = ProductItem.query.filter_by(
            status='active', featured=True
        ).order_by(ProductItem.created_at.desc()).limit(8).all()
        
        # Get recent products
        recent_products = ProductItem.query.filter_by(
            status='active'
        ).order_by(ProductItem.created_at.desc()).limit(12).all()
        
        # Get categories with product counts
        categories = db.session.query(
            ProductCategory.name,
            ProductCategory.slug,
            ProductCategory.icon,
            ProductCategory.image_url,
            func.count(ProductItem.id).label('product_count')
        ).outerjoin(
            ProductItem, and_(
                ProductItem.category_id == ProductCategory.id,
                ProductItem.status == 'active'
            )
        ).filter(ProductCategory.is_active == True).group_by(
            ProductCategory.id
        ).order_by(ProductCategory.sort_order, ProductCategory.name).all()
        
        # Get statistics
        total_products = ProductItem.query.filter_by(status='active').count()
        total_categories = ProductCategory.query.filter_by(is_active=True).count()
        
        # Get user favorites if logged in
        user_favorites = []
        current_user = get_current_user()
        if current_user:
            favorites = ProductFavorite.query.filter_by(user_id=current_user.id).all()
            user_favorites = [fav.product_id for fav in favorites]
        
        return render_template('product/product_home.html',
                             featured_products=featured_products,
                             recent_products=recent_products,
                             categories=categories,
                             total_products=total_products,
                             total_categories=total_categories,
                             user_favorites=user_favorites,
                             current_user=current_user)
        
    except Exception as e:
        flash(f'Error loading product page: {str(e)}', 'error')
        return render_template('product/product_home.html',
                             featured_products=[],
                             recent_products=[],
                             categories=[],
                             total_products=0,
                             total_categories=0,
                             user_favorites=[])

@product_bp.route('/add', methods=['GET', 'POST'])
@product_login_required
def add_product():
    """Add new product - only for logged-in subscribers"""
    current_user = get_current_user()
    if not current_user or current_user.user_type != 'subscriber':
        flash('Only subscribers can add products.', 'error')
        return redirect(url_for('product.product_home'))
    
    form = ProductAddForm()
    
    if form.validate_on_submit():
        try:
            # Create new product
            product = ProductItem()
            
            # Basic information
            product.name = form.name.data
            product.description = form.description.data
            product.short_description = form.short_description.data
            product.sku = form.sku.data
            product.barcode = form.barcode.data
            
            # Pricing
            product.price = float(form.price.data)
            product.original_price = float(form.original_price.data) if form.original_price.data else None
            product.cost_price = float(form.cost_price.data) if form.cost_price.data else None
            product.discount_percentage = form.discount_percentage.data or 0.0
            
            # Inventory
            product.quantity = form.quantity.data
            product.minimum_stock = form.minimum_stock.data or 5
            product.maximum_stock = form.maximum_stock.data or 1000
            
            # Physical properties
            product.weight = form.weight.data
            product.dimensions = form.dimensions.data
            product.color = form.color.data
            product.size = form.size.data
            product.material = form.material.data
            
            # Category and brand
            if form.category.data:
                # Find or create category
                category = ProductCategory.query.filter_by(slug=form.category.data).first()
                if category:
                    product.category_id = category.id
            
            product.brand = form.brand.data
            product.manufacturer = form.manufacturer.data
            product.country_of_origin = form.country_of_origin.data
            
            # Handle main image upload
            if form.main_image.data:
                main_image_path = save_uploaded_file(form.main_image.data, 'products')
                if main_image_path:
                    product.main_image = main_image_path
            
            # Handle additional images
            additional_images = []
            if form.additional_images.data:
                for image_file in form.additional_images.data:
                    if image_file and image_file.filename:
                        image_path = save_uploaded_file(image_file, 'products')
                        if image_path:
                            additional_images.append(image_path)
            
            if additional_images:
                product.set_images(additional_images)
            
            product.video_url = form.video_url.data
            
            # Product settings
            product.status = form.status.data or 'active'  # Default to active if not specified
            product.featured = form.featured.data
            product.is_digital = form.is_digital.data
            product.requires_shipping = form.requires_shipping.data
            
            # SEO
            product.meta_title = form.meta_title.data
            product.meta_description = form.meta_description.data
            
            # Tags
            if form.tags.data:
                tags = [tag.strip() for tag in form.tags.data.split(',') if tag.strip()]
                product.set_tags(tags)
            
            # User information
            product.added_by = current_user.id
            
            # Save to database
            db.session.add(product)
            db.session.commit()
            
            # Log inventory addition
            if product.quantity > 0:
                inventory_log = ProductInventoryLog(
                    product_id=product.id,
                    change_type='add',
                    quantity_before=0,
                    quantity_changed=product.quantity,
                    quantity_after=product.quantity,
                    reason='Initial stock',
                    user_id=current_user.id
                )
                db.session.add(inventory_log)
                db.session.commit()
            
            flash(f'Product "{product.name}" added successfully!', 'success')
            return redirect(url_for('product.view_product', product_id=product.id))
            
        except Exception as e:
            db.session.rollback()
            flash(f'Error adding product: {str(e)}', 'error')
    
    return render_template('product/product_form.html', form=form, action='Add')

@product_bp.route('/all')
def all_products():
    """Display all active products with search and filtering"""
    # Get search parameters
    search_form = ProductSearchForm(request.args)
    page = request.args.get('page', 1, type=int)
    per_page = 12
    
    # Build query
    query = ProductItem.query.filter_by(status='active')
    
    # Apply search filters
    if search_form.search_term.data:
        search_term = f"%{search_form.search_term.data}%"
        query = query.filter(
            or_(
                ProductItem.name.ilike(search_term),
                ProductItem.description.ilike(search_term),
                ProductItem.brand.ilike(search_term),
                ProductItem.tags.ilike(search_term)
            )
        )
        
        # Log search
        try:
            current_user = get_current_user()
            search_log = ProductSearch(
                search_term=search_form.search_term.data,
                user_id=current_user.id if current_user else None,
                results_count=query.count(),
                ip_address=request.remote_addr
            )
            db.session.add(search_log)
            db.session.commit()
        except:
            pass  # Don't fail if search logging fails
    
    if search_form.category.data:
        category = ProductCategory.query.filter_by(slug=search_form.category.data).first()
        if category:
            query = query.filter_by(category_id=category.id)
    
    if search_form.min_price.data:
        query = query.filter(ProductItem.price >= search_form.min_price.data)
    
    if search_form.max_price.data:
        query = query.filter(ProductItem.price <= search_form.max_price.data)
    
    if search_form.in_stock_only.data:
        query = query.filter(ProductItem.quantity > 0)
    
    if search_form.featured_only.data:
        query = query.filter_by(featured=True)
    
    # Apply sorting
    sort_by = search_form.sort_by.data or 'newest'
    if sort_by == 'newest':
        query = query.order_by(desc(ProductItem.created_at))
    elif sort_by == 'oldest':
        query = query.order_by(asc(ProductItem.created_at))
    elif sort_by == 'price_low':
        query = query.order_by(asc(ProductItem.price))
    elif sort_by == 'price_high':
        query = query.order_by(desc(ProductItem.price))
    elif sort_by == 'name_asc':
        query = query.order_by(asc(ProductItem.name))
    elif sort_by == 'name_desc':
        query = query.order_by(desc(ProductItem.name))
    elif sort_by == 'rating':
        query = query.order_by(desc(ProductItem.rating_average))
    elif sort_by == 'popular':
        query = query.order_by(desc(ProductItem.view_count))
    
    # Paginate results
    products = query.paginate(
        page=page, per_page=per_page, error_out=False
    )
    
    # Get categories for filter dropdown
    categories = ProductCategory.query.filter_by(is_active=True).order_by(ProductCategory.name).all()
    
    # Get user favorites if logged in
    user_favorites = []
    current_user = get_current_user()
    if current_user:
        favorites = ProductFavorite.query.filter_by(user_id=current_user.id).all()
        user_favorites = [fav.product_id for fav in favorites]
    
    return render_template('product/all_product.html',
                         products=products,
                         search_form=search_form,
                         categories=categories,
                         user_favorites=user_favorites,
                         current_user=current_user)

@product_bp.route('/view/<int:product_id>')
def view_product(product_id):
    """View individual product details"""
    product = ProductItem.query.get_or_404(product_id)
    
    # Only show active products to public, or any status to the owner
    current_user = get_current_user()
    if product.status != 'active' and (not current_user or current_user.id != product.added_by):
        flash('Product not found or not available.', 'error')
        return redirect(url_for('product.product_home'))
    
    try:
        # Increment view count
        product.view_count += 1
        
        # Log product view
        view_log = ProductView(
            product_id=product.id,
            user_id=current_user.id if current_user else None,
            ip_address=request.remote_addr,
            user_agent=request.user_agent.string,
            referrer=request.referrer
        )
        db.session.add(view_log)
        db.session.commit()
        
    except Exception as e:
        db.session.rollback()
        # Continue even if view logging fails
        pass
    
    # Get product images
    product_images = product.get_images()
    
    # Get product reviews
    reviews = ProductReview.query.filter_by(
        product_id=product.id, status='approved'
    ).order_by(desc(ProductReview.created_at)).limit(10).all()
    
    # Get related products (same category)
    related_products = []
    if product.category_id:
        related_products = ProductItem.query.filter(
            and_(
                ProductItem.category_id == product.category_id,
                ProductItem.id != product.id,
                ProductItem.status == 'active'
            )
        ).limit(4).all()
    
    # Check if user has favorited this product
    is_favorited = False
    if current_user:
        favorite = ProductFavorite.query.filter_by(
            user_id=current_user.id, product_id=product.id
        ).first()
        is_favorited = favorite is not None
    
    # Get product category
    category = None
    if product.category_id:
        category = ProductCategory.query.get(product.category_id)
    
    # Review form for logged-in users
    review_form = ProductReviewForm() if current_user else None
    
    # Get user's cart info if logged in
    cart_quantity = 0
    if current_user:
        try:
            from product.cart_models import ProductCart, ProductCartItem
            user_cart = ProductCart.query.filter_by(user_id=current_user.id, status='active').first()
            if user_cart:
                cart_item = ProductCartItem.query.filter_by(cart_id=user_cart.id, product_id=product.id).first()
                if cart_item:
                    cart_quantity = cart_item.quantity
        except Exception as e:
            # Cart tables may not exist yet
            cart_quantity = 0
    
    return render_template('product/enhanced_product_details.html',
                         product=product,
                         product_images=product_images,
                         reviews=reviews,
                         related_products=related_products,
                         is_favorited=is_favorited,
                         category=category,
                         review_form=review_form,
                         current_user=current_user,
                         cart_quantity=cart_quantity)

@product_bp.route('/edit/<int:product_id>', methods=['GET', 'POST'])
@product_login_required
def edit_product(product_id):
    """Edit existing product - only for product owner or admin"""
    product = ProductItem.query.get_or_404(product_id)
    current_user = get_current_user()
    
    # Check permissions
    if current_user.id != product.added_by and current_user.role != 'admin':
        flash('You can only edit your own products.', 'error')
        return redirect(url_for('product.view_product', product_id=product_id))
    
    form = ProductEditForm(obj=product)
    form.product_id.data = product_id
    
    if form.validate_on_submit():
        try:
            # Update basic information
            product.name = form.name.data
            product.description = form.description.data
            product.short_description = form.short_description.data
            product.sku = form.sku.data
            product.barcode = form.barcode.data
            
            # Update pricing
            old_price = product.price
            product.price = float(form.price.data)
            product.original_price = float(form.original_price.data) if form.original_price.data else None
            product.cost_price = float(form.cost_price.data) if form.cost_price.data else None
            product.discount_percentage = form.discount_percentage.data or 0.0
            
            # Update inventory
            old_quantity = product.quantity
            product.quantity = form.quantity.data
            product.minimum_stock = form.minimum_stock.data or 5
            product.maximum_stock = form.maximum_stock.data or 1000
            
            # Log inventory change if quantity changed
            if old_quantity != product.quantity:
                change_type = 'add' if product.quantity > old_quantity else 'remove'
                quantity_changed = abs(product.quantity - old_quantity)
                
                inventory_log = ProductInventoryLog(
                    product_id=product.id,
                    change_type=change_type,
                    quantity_before=old_quantity,
                    quantity_changed=quantity_changed,
                    quantity_after=product.quantity,
                    reason='Manual update via edit form',
                    user_id=current_user.id
                )
                db.session.add(inventory_log)
            
            # Update physical properties
            product.weight = form.weight.data
            product.dimensions = form.dimensions.data
            product.color = form.color.data
            product.size = form.size.data
            product.material = form.material.data
            
            # Update category and brand
            if form.category.data:
                category = ProductCategory.query.filter_by(slug=form.category.data).first()
                if category:
                    product.category_id = category.id
            
            product.brand = form.brand.data
            product.manufacturer = form.manufacturer.data
            product.country_of_origin = form.country_of_origin.data
            
            # Handle image updates
            if form.main_image.data:
                main_image_path = save_uploaded_file(form.main_image.data, 'products')
                if main_image_path:
                    product.main_image = main_image_path
            
            # Handle additional images
            if form.additional_images.data:
                existing_images = product.get_images()
                new_images = []
                
                for image_file in form.additional_images.data:
                    if image_file and image_file.filename:
                        image_path = save_uploaded_file(image_file, 'products')
                        if image_path:
                            new_images.append(image_path)
                
                if new_images:
                    all_images = existing_images + new_images
                    product.set_images(all_images)
            
            if form.video_url.data:
                product.video_url = form.video_url.data
            
            # Update product settings
            product.status = form.status.data
            product.featured = form.featured.data
            product.is_digital = form.is_digital.data
            product.requires_shipping = form.requires_shipping.data
            
            # Update SEO
            product.meta_title = form.meta_title.data
            product.meta_description = form.meta_description.data
            
            # Update tags
            if form.tags.data:
                tags = [tag.strip() for tag in form.tags.data.split(',') if tag.strip()]
                product.set_tags(tags)
            
            # Update timestamp
            product.updated_at = datetime.utcnow()
            
            db.session.commit()
            flash(f'Product "{product.name}" updated successfully!', 'success')
            return redirect(url_for('product.view_product', product_id=product.id))
            
        except Exception as e:
            db.session.rollback()
            flash(f'Failed to update product: {str(e)}', 'error')
    
    # Get categories for the form
    categories = ProductCategory.query.filter_by(is_active=True).order_by(ProductCategory.name).all()
    return render_template('product/product_form.html',
                         form=form,
                         product=product,
                         categories=categories,
                         is_edit=True)

# ADD TO CART AND CART MANAGEMENT ROUTES

@product_bp.route('/add_to_cart/<int:product_id>', methods=['POST'])
@product_login_required
def add_to_cart(product_id):
    """Add product to user's cart"""
    from product.cart_models import ProductCart, ProductCartItem
    
    product = ProductItem.query.get_or_404(product_id)
    current_user = get_current_user()
    
    if product.status != 'active':
        return jsonify({'error': 'Product is not available'}), 400
    
    quantity = int(request.form.get('quantity', 1))
    
    if quantity > product.quantity:
        return jsonify({'error': 'Not enough stock available'}), 400
    
    try:
        # Get or create user's cart
        cart = ProductCart.query.filter_by(user_id=current_user.id, status='active').first()
        if not cart:
            cart = ProductCart(user_id=current_user.id, status='active')
            db.session.add(cart)
            db.session.flush()  # Get cart ID
        
        # Check if product already in cart
        cart_item = ProductCartItem.query.filter_by(cart_id=cart.id, product_id=product_id).first()
        
        if cart_item:
            # Update existing item
            new_quantity = cart_item.quantity + quantity
            if new_quantity > product.quantity:
                return jsonify({'error': 'Not enough stock available'}), 400
            cart_item.quantity = new_quantity
            cart_item.updated_at = datetime.utcnow()
            message = f'Updated {product.name} quantity in cart'
        else:
            # Add new item
            cart_item = ProductCartItem(
                cart_id=cart.id,
                product_id=product_id,
                quantity=quantity,
                unit_price=product.price
            )
            db.session.add(cart_item)
            message = f'Added {product.name} to cart'
        
        db.session.commit()
        
        # Return JSON response for AJAX calls
        if request.is_json or request.form.get('ajax'):
            return jsonify({
                'success': True,
                'message': message,
                'cart_total': cart.get_total_items(),
                'cart_price': cart.get_total_price(),
                'product_quantity': cart_item.quantity
            })
        
        flash(message, 'success')
        return redirect(url_for('product.view_product', product_id=product_id))
        
    except Exception as e:
        db.session.rollback()
        if request.is_json or request.form.get('ajax'):
            return jsonify({'error': 'Failed to add to cart'}), 500
        flash('Failed to add product to cart', 'error')
        return redirect(url_for('product.view_product', product_id=product_id))

@product_bp.route('/cart')
@product_login_required  
def view_cart():
    """View user's shopping cart"""
    from product.cart_models import ProductCart, ProductCartItem
    
    current_user = get_current_user()
    cart = ProductCart.query.filter_by(user_id=current_user.id, status='active').first()
    
    cart_items = []
    if cart:
        cart_items = cart.items.all()
    
    return render_template('product/cart.html',
                         cart=cart,
                         cart_items=cart_items,
                         current_user=current_user)

@product_bp.route('/update_cart/<int:item_id>', methods=['POST'])
@product_login_required
def update_cart_item(item_id):
    """Update quantity of item in cart"""
    from product.cart_models import ProductCartItem
    
    current_user = get_current_user()
    cart_item = ProductCartItem.query.get_or_404(item_id)
    
    # Verify ownership
    if cart_item.cart.user_id != current_user.id:
        return jsonify({'error': 'Unauthorized'}), 403
    
    new_quantity = int(request.form.get('quantity', 1))
    
    if new_quantity <= 0:
        # Remove item if quantity is 0 or negative
        db.session.delete(cart_item)
        message = 'Item removed from cart'
    else:
        # Check stock
        if new_quantity > cart_item.product.quantity:
            return jsonify({'error': 'Not enough stock available'}), 400
        
        cart_item.update_quantity(new_quantity)
        message = 'Cart updated'
    
    try:
        db.session.commit()
        
        if request.is_json or request.form.get('ajax'):
            return jsonify({
                'success': True,
                'message': message,
                'cart_total': cart_item.cart.get_total_items(),
                'cart_price': cart_item.cart.get_total_price()
            })
        
        flash(message, 'success')
        return redirect(url_for('product.view_cart'))
        
    except Exception as cart_update_error:
        db.session.rollback()
        if request.is_json or request.form.get('ajax'):
            return jsonify({'error': 'Failed to update cart'}), 500
        flash('Failed to update cart', 'error')
        return redirect(url_for('product.view_cart'))

@product_bp.route('/remove_from_cart/<int:item_id>', methods=['POST'])
@product_login_required
def remove_from_cart(item_id):
    """Remove item from cart"""
    from product.cart_models import ProductCartItem
    
    current_user = get_current_user()
    cart_item = ProductCartItem.query.get_or_404(item_id)
    
    # Verify ownership
    if cart_item.cart.user_id != current_user.id:
        return jsonify({'error': 'Unauthorized'}), 403
    
    try:
        product_name = cart_item.product.name
        db.session.delete(cart_item)
        db.session.commit()
        
        message = f'Removed {product_name} from cart'
        
        if request.is_json or request.form.get('ajax'):
            return jsonify({
                'success': True,
                'message': message,
                'cart_total': cart_item.cart.get_total_items(),
                'cart_price': cart_item.cart.get_total_price()
            })
        
        flash(message, 'success')
        return redirect(url_for('product.view_cart'))
        
    except Exception as e:
        db.session.rollback()
        if request.is_json or request.form.get('ajax'):
            return jsonify({'error': 'Failed to remove from cart'}), 500
        flash('Failed to remove item from cart', 'error')
        return redirect(url_for('product.view_cart'))

@product_bp.route('/edit/<int:product_id>', methods=['GET', 'POST'])
@product_login_required
def edit_product_duplicate_fix(product_id):
    """Edit existing product - fixed duplicate issue"""
    product = ProductItem.query.get_or_404(product_id)
    current_user = get_current_user()
    
    # Check permissions
    if current_user.id != product.added_by and current_user.role != 'admin':
        flash('You can only edit your own products.', 'error')
        return redirect(url_for('product.view_product', product_id=product_id))
    
    form = ProductEditForm(obj=product)
    form.product_id.data = product_id
    
    if form.validate_on_submit():
        try:
            # Update product fields here
            product.name = form.name.data
            product.description = form.description.data
            product.price = float(form.price.data)
            product.quantity = form.quantity.data
            product.updated_at = datetime.utcnow()
            
            db.session.commit()
            flash(f'Product "{product.name}" updated successfully!', 'success')
            return redirect(url_for('product.view_product', product_id=product.id))
            
        except Exception as e:
            db.session.rollback()
            flash(f'Failed to update product: {str(e)}', 'error')
    
    # Pre-populate form with existing data
    if request.method == 'GET':
        # Set tags for form display
        tags = product.get_tags()
        if tags:
            form.tags.data = ', '.join(tags)
    
    return render_template('product/product_form.html',
                         form=form,
                         product=product,
                         is_edit=True)

@product_bp.route('/delete/<int:product_id>', methods=['POST'])
@product_login_required
def delete_product(product_id):
    """Delete product - only for product owner or admin"""
    product = ProductItem.query.get_or_404(product_id)
    current_user = get_current_user()
    
    # Check permissions
    if current_user.id != product.added_by and current_user.role != 'admin':
        if request.is_json:
            return jsonify({'success': False, 'message': 'Permission denied'}), 403
        flash('You can only delete your own products.', 'error')
        return redirect(url_for('product.view_product', product_id=product_id))
    
    try:
        product_name = product.name
        
        # Delete related records first (to maintain data integrity)
        ProductReview.query.filter_by(product_id=product_id).delete()
        ProductFavorite.query.filter_by(product_id=product_id).delete()
        ProductView.query.filter_by(product_id=product_id).delete()
        ProductImage.query.filter_by(product_id=product_id).delete()
        ProductInventoryLog.query.filter_by(product_id=product_id).delete()
        
        # Delete the product
        db.session.delete(product)
        db.session.commit()
        
        if request.is_json:
            return jsonify({'success': True, 'message': f'Product "{product_name}" deleted successfully!'})
        
        flash(f'Product "{product_name}" deleted successfully!', 'success')
        return redirect(url_for('product.all_product'))
        
    except Exception as e:
        db.session.rollback()
        if request.is_json:
            return jsonify({'success': False, 'message': str(e)}), 500
        flash(f'Error deleting product: {str(e)}', 'error')
        return redirect(url_for('product.view_product', product_id=product_id))

@product_bp.route('/bulk-action', methods=['POST'])
@product_login_required
def bulk_action():
    """Handle bulk actions on products"""
    try:
        data = request.get_json()
        action = data.get('action')
        product_ids = data.get('product_ids', [])
        current_user = get_current_user()
        
        if not product_ids:
            return jsonify({'success': False, 'message': 'No products selected'}), 400
        
        # Get products that belong to current user or if admin
        query = ProductItem.query.filter(ProductItem.id.in_(product_ids))
        if current_user.role != 'admin':
            query = query.filter(ProductItem.added_by == current_user.id)
        
        products = query.all()
        
        if not products:
            return jsonify({'success': False, 'message': 'No valid products found'}), 404
        
        if action == 'delete':
            for product in products:
                # Delete related records first
                ProductReview.query.filter_by(product_id=product.id).delete()
                ProductFavorite.query.filter_by(product_id=product.id).delete()
                ProductView.query.filter_by(product_id=product.id).delete()
                ProductImage.query.filter_by(product_id=product.id).delete()
                ProductInventoryLog.query.filter_by(product_id=product.id).delete()
                db.session.delete(product)
            
            db.session.commit()
            return jsonify({'success': True, 'message': f'{len(products)} products deleted successfully'})
            
        elif action == 'activate':
            for product in products:
                product.status = 'active'
                product.updated_at = datetime.utcnow()
            
            db.session.commit()
            return jsonify({'success': True, 'message': f'{len(products)} products activated'})
            
        elif action == 'deactivate':
            for product in products:
                product.status = 'draft'
                product.updated_at = datetime.utcnow()
            
            db.session.commit()
            return jsonify({'success': True, 'message': f'{len(products)} products deactivated'})
        
        else:
            return jsonify({'success': False, 'message': 'Invalid action'}), 400
            
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)}), 500

@product_bp.route('/export', methods=['POST'])
@product_login_required
def export_products():
    """Export selected products to CSV"""
    try:
        product_ids = request.form.getlist('product_ids')
        current_user = get_current_user()
        
        if not product_ids:
            flash('No products selected for export', 'error')
            return redirect(url_for('subscriber_dashboard'))
        
        # Get products that belong to current user or if admin
        query = ProductItem.query.filter(ProductItem.id.in_(product_ids))
        if current_user.role != 'admin':
            query = query.filter(ProductItem.added_by == current_user.id)
        
        products = query.all()
        
        # Create CSV data
        import io
        import csv
        output = io.StringIO()
        writer = csv.writer(output)
        
        # Write headers
        writer.writerow(['ID', 'Name', 'Description', 'Price', 'Quantity', 'Status', 'Views', 'Created'])
        
        # Write product data
        for product in products:
            writer.writerow([
                product.id,
                product.name,
                product.description or '',
                product.price,
                product.quantity,
                product.status,
                product.view_count or 0,
                product.created_at.strftime('%Y-%m-%d %H:%M:%S') if product.created_at else ''
            ])
        
        # Create response
        output_str = output.getvalue()
        output.close()
        
        response = make_response(output_str)
        response.headers["Content-Disposition"] = f"attachment; filename=products_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        response.headers["Content-type"] = "text/csv"
        
        return response
        
    except Exception as e:
        flash(f'Export failed: {str(e)}', 'error')
        return redirect(url_for('subscriber_dashboard'))

@product_bp.route('/favorite/<int:product_id>', methods=['POST'])
@product_login_required
def toggle_favorite(product_id):
    """Add or remove product from user favorites"""
    current_user = get_current_user()
    product = ProductItem.query.get_or_404(product_id)
    
    try:
        # Check if already favorited
        favorite = ProductFavorite.query.filter_by(
            user_id=current_user.id, product_id=product_id
        ).first()
        
        if favorite:
            # Remove from favorites
            db.session.delete(favorite)
            is_favorited = False
            message = f'"{product.name}" removed from favorites'
        else:
            # Add to favorites
            favorite = ProductFavorite(
                user_id=current_user.id,
                product_id=product_id
            )
            db.session.add(favorite)
            is_favorited = True
            message = f'"{product.name}" added to favorites'
        
        db.session.commit()
        
        if request.is_json:
            return jsonify({
                'success': True,
                'is_favorited': is_favorited,
                'message': message
            })
        else:
            flash(message, 'success')
            return redirect(url_for('product.view_product', product_id=product_id))
            
    except Exception as e:
        db.session.rollback()
        error_msg = f'Error updating favorites: {str(e)}'
        
        if request.is_json:
            return jsonify({'success': False, 'message': error_msg})
        else:
            flash(error_msg, 'error')
            return redirect(url_for('product.view_product', product_id=product_id))

# ENHANCED CART FUNCTIONALITY ROUTES

@product_bp.route('/add-to-cart', methods=['POST'])
@product_login_required
def add_to_cart_json():
    """Add product to user's shopping cart via JSON API"""
    try:
        current_user = get_current_user()
        data = request.get_json()
        product_id = data.get('product_id')
        quantity = data.get('quantity', 1)
        
        if not product_id:
            return jsonify({'success': False, 'message': 'Product ID is required'})
        
        product = ProductItem.query.get(product_id)
        if not product:
            return jsonify({'success': False, 'message': 'Product not found'})
        
        if product.quantity < quantity:
            return jsonify({'success': False, 'message': 'Insufficient stock'})
        
        # Get or create user's cart
        from product.cart_models import ProductCart, ProductCartItem
        user_cart = ProductCart.query.filter_by(user_id=current_user.id, status='active').first()
        if not user_cart:
            user_cart = ProductCart(
                user_id=current_user.id,
                status='active'
            )
            db.session.add(user_cart)
            db.session.commit()
        
        # Check if product already in cart
        cart_item = ProductCartItem.query.filter_by(cart_id=user_cart.id, product_id=product_id).first()
        if cart_item:
            cart_item.quantity += quantity
        else:
            cart_item = ProductCartItem(
                cart_id=user_cart.id,
                product_id=product_id,
                quantity=quantity,
                unit_price=product.price
            )
            db.session.add(cart_item)
        
        db.session.commit()
        
        # Get cart count
        cart_count = ProductCartItem.query.filter_by(cart_id=user_cart.id).count()
        
        return jsonify({
            'success': True, 
            'message': 'Product added to cart successfully',
            'cart_count': cart_count
        })
        
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

@product_bp.route('/review/<int:product_id>', methods=['POST'])
@product_login_required
def add_review(product_id):
    """Add product review"""
    current_user = get_current_user()
    product = ProductItem.query.get_or_404(product_id)
    form = ProductReviewForm()
    
    if form.validate_on_submit():
        try:
            # Check if user already reviewed this product
            existing_review = ProductReview.query.filter_by(
                user_id=current_user.id, product_id=product_id
            ).first()
            
            if existing_review:
                flash('You have already reviewed this product.', 'warning')
                return redirect(url_for('product.view_product', product_id=product_id))
            
            # Create new review
            review = ProductReview(
                product_id=product_id,
                user_id=current_user.id,
                rating=int(form.rating.data),
                title=form.title.data,
                comment=form.comment.data,
                pros=form.pros.data,
                cons=form.cons.data,
                status='pending'  # Reviews need approval
            )
            
            db.session.add(review)
            db.session.commit()
            
            flash('Thank you for your review! It will be published after approval.', 'success')
            return redirect(url_for('product.view_product', product_id=product_id))
            
        except Exception as e:
            db.session.rollback()
            flash(f'Error adding review: {str(e)}', 'error')
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f'{field}: {error}', 'error')
    
    return redirect(url_for('product.view_product', product_id=product_id))

@product_bp.route('/category/<slug>')
def category_products(slug):
    """View products in a specific category"""
    category = ProductCategory.query.filter_by(slug=slug, is_active=True).first_or_404()
    
    page = request.args.get('page', 1, type=int)
    per_page = 12
    
    # Get products in this category
    products = ProductItem.query.filter_by(
        category_id=category.id, status='active'
    ).order_by(desc(ProductItem.created_at)).paginate(
        page=page, per_page=per_page, error_out=False
    )
    
    # Get user favorites if logged in
    user_favorites = []
    current_user = get_current_user()
    if current_user:
        favorites = ProductFavorite.query.filter_by(user_id=current_user.id).all()
        user_favorites = [fav.product_id for fav in favorites]
    
    return render_template('product/category_products.html',
                         category=category,
                         products=products,
                         user_favorites=user_favorites,
                         current_user=current_user)

@product_bp.route('/my-products')
@product_login_required
def my_products():
    """View current user's products"""
    current_user = get_current_user()
    
    page = request.args.get('page', 1, type=int)
    per_page = 12
    status_filter = request.args.get('status', 'all')
    
    # Build query for user's products
    query = ProductItem.query.filter_by(added_by=current_user.id)
    
    if status_filter != 'all':
        query = query.filter_by(status=status_filter)
    
    products = query.order_by(desc(ProductItem.created_at)).paginate(
        page=page, per_page=per_page, error_out=False
    )
    
    # Get statistics
    stats = {
        'total': ProductItem.query.filter_by(added_by=current_user.id).count(),
        'active': ProductItem.query.filter_by(added_by=current_user.id, status='active').count(),
        'draft': ProductItem.query.filter_by(added_by=current_user.id, status='draft').count(),
        'inactive': ProductItem.query.filter_by(added_by=current_user.id, status='inactive').count(),
    }
    
    return render_template('product/my_products.html',
                         products=products,
                         stats=stats,
                         status_filter=status_filter,
                         current_user=current_user)

@product_bp.route('/favorites')
@product_login_required
def my_favorites():
    """View current user's favorite products"""
    current_user = get_current_user()
    
    page = request.args.get('page', 1, type=int)
    per_page = 12
    
    # Get user's favorites with product details
    favorites = db.session.query(ProductItem).join(
        ProductFavorite, ProductItem.id == ProductFavorite.product_id
    ).filter(
        ProductFavorite.user_id == current_user.id,
        ProductItem.status == 'active'
    ).order_by(desc(ProductFavorite.created_at)).paginate(
        page=page, per_page=per_page, error_out=False
    )
    
    return render_template('product/favorites.html',
                         favorites=favorites,
                         current_user=current_user)

# API endpoints for AJAX requests

@product_bp.route('/api/search')
def api_search():
    """API endpoint for product search (for autocomplete, etc.)"""
    query = request.args.get('q', '').strip()
    limit = request.args.get('limit', 10, type=int)
    
    if not query or len(query) < 2:
        return jsonify([])
    
    search_term = f"%{query}%"
    products = ProductItem.query.filter(
        and_(
            ProductItem.status == 'active',
            or_(
                ProductItem.name.ilike(search_term),
                ProductItem.brand.ilike(search_term)
            )
        )
    ).limit(limit).all()
    
    results = []
    for product in products:
        results.append({
            'id': product.id,
            'name': product.name,
            'price': float(product.price),
            'image': product.main_image,
            'url': url_for('product.view_product', product_id=product.id)
        })
    
    return jsonify(results)

@product_bp.route('/plan')
def product_plan():
    """Product service plan page"""
    current_user = get_current_user()
    
    # Get user's product statistics if logged in
    user_stats = {}
    if current_user:
        user_stats = {
            'total_products': ProductItem.query.filter_by(added_by=current_user.id).count(),
            'active_products': ProductItem.query.filter_by(added_by=current_user.id, status='active').count(),
            'draft_products': ProductItem.query.filter_by(added_by=current_user.id, status='draft').count(),
            'total_views': db.session.query(func.sum(ProductItem.view_count)).filter_by(added_by=current_user.id).scalar() or 0,
            'total_favorites': db.session.query(func.count(ProductFavorite.id)).join(
                ProductItem, ProductFavorite.product_id == ProductItem.id
            ).filter(ProductItem.added_by == current_user.id).scalar() or 0
        }
    
    # Product service plans
    plans = [
        {
            'name': 'Basic Plan',
            'price': 'Free',
            'features': [
                'Add up to 10 products',
                'Basic product listing',
                'Image uploads (5MB max)',
                'Basic analytics',
                'Community support'
            ],
            'limitations': [
                'Limited to 10 products',
                'Basic features only',
                'No premium support'
            ]
        },
        {
            'name': 'Pro Plan',
            'price': '₹299/month',
            'features': [
                'Unlimited products',
                'Advanced product management',
                'Multiple images per product',
                'Detailed analytics',
                'SEO optimization',
                'Priority support',
                'Bulk operations',
                'Advanced search features'
            ],
            'popular': True
        },
        {
            'name': 'Enterprise Plan',
            'price': '₹999/month',
            'features': [
                'Everything in Pro',
                'API access',
                'Custom integrations',
                'White-label options',
                'Dedicated support',
                'Custom features',
                'Advanced reporting',
                'Multi-user access'
            ]
        }
    ]
    
    return render_template('product/product_plan.html',
                         plans=plans,
                         user_stats=user_stats,
                         current_user=current_user)

@product_bp.route('/api/stats')
def api_stats():
    """API endpoint for product statistics"""
    stats = {
        'total_products': ProductItem.query.filter_by(status='active').count(),
        'total_categories': ProductCategory.query.filter_by(is_active=True).count(),
        'featured_products': ProductItem.query.filter_by(status='active', featured=True).count(),
        'out_of_stock': ProductItem.query.filter_by(status='active', quantity=0).count(),
        'low_stock': ProductItem.query.filter(
            and_(ProductItem.status == 'active', ProductItem.quantity <= ProductItem.minimum_stock)
        ).count()
    }
    
    return jsonify(stats)

# File serving route
@product_bp.route('/uploads/<path:filename>')
def uploaded_file(filename):
    """Serve uploaded product files"""
    return send_from_directory('uploads/products', filename)

# Note: Cart routes are defined above in the main cart management section

# End of product routes - Cart routes are already defined above