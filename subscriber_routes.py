from flask import render_template, request, redirect, url_for, flash, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from app import app, db
from models import User, PricingPlan, UserSubscription, Category
from datetime import datetime, timedelta
import logging

# Session management for subscribers
def subscriber_login_required(f):
    from functools import wraps
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'subscriber_id' not in session:
            flash('Please log in to access this page.', 'error')
            return redirect(url_for('subscriber_login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/subscriber/login')
def subscriber_login():
    """Display subscriber login/signup page"""
    return render_template('subscriber_login.html')

@app.route('/subscriber/auth', methods=['POST'])
def subscriber_auth():
    """Handle subscriber login/signup"""
    action = request.form.get('action')
    email = request.form.get('email')
    password = request.form.get('password')
    
    if action == 'login':
        # Login existing subscriber
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password_hash, password):
            session['subscriber_id'] = user.id
            session['subscriber_email'] = user.email
            session['subscriber_name'] = user.full_name
            flash('Login successful!', 'success')
            return redirect(url_for('subscriber_dashboard'))
        else:
            flash('Invalid email or password.', 'error')
    
    elif action == 'signup':
        # Register new subscriber
        full_name = request.form.get('full_name')
        mobile = request.form.get('mobile')
        
        # Check if user already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email already registered. Please login instead.', 'error')
        else:
            # Create new subscriber
            user = User(
                full_name=full_name,
                email=email,
                mobile=mobile,
                password_hash=generate_password_hash(password),
                user_type='subscriber',
                created_at=datetime.utcnow()
            )
            db.session.add(user)
            db.session.commit()
            
            # Auto-login after signup
            session['subscriber_id'] = user.id
            session['subscriber_email'] = user.email
            session['subscriber_name'] = user.full_name
            
            flash('Registration successful! Welcome to Mobile Shop Hub!', 'success')
            return redirect(url_for('subscriber_dashboard'))
    
    return redirect(url_for('subscriber_login'))

@app.route('/subscriber/dashboard')
@subscriber_login_required
def subscriber_dashboard():
    """Subscriber dashboard showing available service categories"""
    user_id = session.get('subscriber_id')
    
    # Get all available categories
    categories = Category.query.all()
    
    # Get user's current subscriptions
    user_subscriptions = UserSubscription.query.filter_by(user_id=user_id).all()
    
    return render_template('subscriber_dashboard.html', 
                         categories=categories,
                         user_subscriptions=user_subscriptions)

@app.route('/subscriber/category/<int:category_id>')
@subscriber_login_required
def select_category(category_id):
    """Show category registration form with pricing plans"""
    category = Category.query.get_or_404(category_id)
    user_id = session.get('subscriber_id')
    user = User.query.get(user_id)
    
    # Get pricing plans for this category
    pricing_plans = PricingPlan.query.filter_by(category_id=category_id, is_active=True).all()
    
    return render_template('category_registration.html',
                         category=category,
                         pricing_plans=pricing_plans,
                         user=user)

@app.route('/subscriber/category/<int:category_id>/register', methods=['POST'])
@subscriber_login_required
def register_category(category_id):
    """Handle category registration with pricing plan"""
    category = Category.query.get_or_404(category_id)
    user_id = session.get('subscriber_id')
    user = User.query.get(user_id)
    
    # Get form data
    plan_id = request.form.get('plan_id')
    additional_info = request.form.get('additional_info', '')
    
    # Get selected pricing plan
    plan = PricingPlan.query.get_or_404(plan_id)
    
    # Create subscription record
    subscription = UserSubscription(
        user_id=user_id,
        category_id=category_id,
        plan_id=plan_id,
        additional_info=additional_info,
        amount=plan.price,
        status='pending',  # pending until payment
        created_at=datetime.utcnow()
    )
    
    db.session.add(subscription)
    db.session.commit()
    
    # If plan is free, approve immediately
    if plan.price == 0:
        subscription.status = 'active'
        subscription.approved_at = datetime.utcnow()
        db.session.commit()
        flash(f'Successfully registered for {category.name} - Free Plan!', 'success')
        return redirect(url_for('subscriber_dashboard'))
    
    # For paid plans, redirect to payment
    return redirect(url_for('process_payment', subscription_id=subscription.id))

@app.route('/subscriber/payment/<int:subscription_id>')
@subscriber_login_required
def process_payment(subscription_id):
    """Handle payment processing for subscription"""
    subscription = UserSubscription.query.get_or_404(subscription_id)
    
    # Verify subscription belongs to current user
    if subscription.user_id != session.get('subscriber_id'):
        flash('Access denied.', 'error')
        return redirect(url_for('subscriber_dashboard'))
    
    return render_template('payment_processing.html', subscription=subscription)

@app.route('/subscriber/payment/<int:subscription_id>/complete', methods=['POST'])
@subscriber_login_required
def complete_payment(subscription_id):
    """Complete payment and activate subscription"""
    subscription = UserSubscription.query.get_or_404(subscription_id)
    
    # Verify subscription belongs to current user
    if subscription.user_id != session.get('subscriber_id'):
        flash('Access denied.', 'error')
        return redirect(url_for('subscriber_dashboard'))
    
    # Simulate payment processing
    payment_success = request.form.get('payment_success') == 'true'
    
    if payment_success:
        subscription.status = 'active'
        subscription.approved_at = datetime.utcnow()
        subscription.payment_status = 'completed'
        flash('Payment successful! Your subscription is now active.', 'success')
    else:
        subscription.status = 'pending'
        subscription.payment_status = 'failed'
        flash('Payment failed. Please try again or contact support.', 'error')
    
    db.session.commit()
    return redirect(url_for('subscriber_dashboard'))

@app.route('/subscriber/logout')
def subscriber_logout():
    """Logout subscriber"""
    session.pop('subscriber_id', None)
    session.pop('subscriber_email', None) 
    session.pop('subscriber_name', None)
    flash('You have been logged out successfully.', 'success')
    return redirect(url_for('subscriber_login'))

@app.route('/subscriber/profile')
@subscriber_login_required
def subscriber_profile():
    """Show subscriber profile"""
    user_id = session.get('subscriber_id')
    user = User.query.get(user_id)
    subscriptions = UserSubscription.query.filter_by(user_id=user_id).all()
    
    return render_template('subscriber_profile.html', user=user, subscriptions=subscriptions)