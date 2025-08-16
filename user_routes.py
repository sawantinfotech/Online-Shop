    from flask import render_template, request, redirect, url_for, flash, session, jsonify
    from werkzeug.security import generate_password_hash, check_password_hash
    from app import app, db
    from models import User, PricingPlan, UserSubscription, Service, Category
    from datetime import datetime, timedelta
    import logging

    # Session management for subscribers
    def user_register_required(f):
        from functools import wraps
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if 'user_id' not in session:
                flash('Please log in to access this page.', 'error')
                return redirect(url_for('user_register'))
            return f(*args, **kwargs)
        return decorated_function

    @app.route('/user_register')
    def user_register():
        """Display user login/signup page"""
        return render_template('/user_register.html')

    @app.route('/auth', methods=['POST'])
    def user_auth():
        """Handle user login/signup"""
        action = request.form.get('action')
        email = request.form.get('email')
        mobile = request.form.get('mobile')
        dateofbirth = request.form.get('dateofbirth')
        first_name = request.form.get('first_name')
        user_type = request.form.get('user_type')
        password = request.form.get('password')

        if action == 'login':
            # Login existing subscriber
            user = User.query.filter_by(email=email).first(), (mobile=mobile).first(), (dateofbirth=dateofbirth).first(),(first_name=first_name).first(), (user_type=user_type).first()
            if user and check_password_hash(user.password_hash, password):
                # Update online status
                user.is_online = True
                user.last_seen = datetime.utcnow()
                db.session.commit()

                session['user_id'] = user.id
                session['user_email'] = user.email
                session['user_mobile'] = user.mobile
                session['user-dateofbirth'] = user.dateofbirth
                session['user_name'] = user.full_name
                session['user_type'] = user.user_type
                flash('Login successful!', 'success')
                return redirect(url_for('subscriber_dashboard'))
            else:
                flash('Invalid email or password.', 'error'),
                flash('Invalid mobile or password.', 'error'),
                flash('Invalid dateofbirth or password.', 'error')
                flash('Invalid first_name or password.', 'error')
                flash('Invalid user_type or password.', 'error')
        elif action == 'signup':
            # Register new subscriber
            first_name = request.form.get('first_name')
            mobile = request.form.get('mobile')
            dateofbirth = request.form.get('dateofbirth')
            user_type = request.form.get('user_type')
            # Check if user already exists
            existing_user = User.query.filter_by(email=email).first()
            existing_user =
    User.query.filter_by(mobile=mobile)
            existing_user =
    User.query.filter_by(dateofbirth=dateofbirth)
            if existing_user:
                flash('Email already registered. Please login instead.', 'error')
                flash('Mobile already registered. Please login instead.', 'error')
                flash('DOB already registered. Please login instead.', 'error')
            else:
                # Create new subscriber
                user = User(
                    first_name=first_name,
                    email=email,
                    mobile=mobile,
                    dateofbirth=dateofbirth,
                    password_hash=generate_password_hash(password),
                    user_type='subscriber', 'admin', 'staff', 'vendor', 'customer', 'guest', 'developer', 'manager', 'owner', 'partner', 'investor', 'employee', 'student', 'teacher', 'family', 'friend', 'leader', 'member', 'donor', 'volunteer', 'sponsor', 'rider',
                    is_online=True,
                    last_seen=datetime.utcnow(),
                    created_at=datetime.utcnow()
                )
                db.session.add(user)
                db.session.commit()

                # Auto-login after signup
                session['user_id'] = user.id
                session['user_email'] = user.email
                session['user_name'] = user.first_name
                session['user_mobile'] = user.mobile
                session['user-dateofbirth'] = user.dateofbirth
                session['user_type'] = user.user_type

                flash('Registration successful! Welcome to Mobile Shop Hub!', 'success')
                return redirect(url_for('subscriber_dashboard'))

        return redirect(url_for('user_register'))

    @app.route('/subscriber_dashboard')
    @subscriber_login_required
    def subscriber_dashboard():
        """Subscriber dashboard showing available services & categories"""
        user_id = session.get('user_id')

        # Get all available categories
        services = service.query.all()
        # Get all available categories
        categories = Category.query.all()

        # Get user's current subscriptions
        user_subscriptions = UserSubscription.query.filter_by(user_id=subscriber_id).all()

        return render_template('/user/subscriber_dashboard.html',
                             services=services,
                             categories=categories,
                             user_subscriptions=user_subscriptions)

    @app.route('/service/<int:service_id>','/category/<int:category_id>')
    @subscriber_login_required
    def select_service(service_id):
        """Show services registration form with pricing plans"""
        service = Service.query.get_or_404(service_id)
        user_id = session.get('subscriber_id')
        user = User.query.get(user_id)
    
        # Get pricing plans for this services, category
        pricing_plans =
    PricingPlan.query.filter_by(service_id=service_id,)
    is_active=True).all()   

        return 
    render_template('/services/services_registration.html',
                             service=service,
                             pricing_plans=pricing_plans,
                             user=user)
   @app.route('/subscriber/services/<int:services_id>/register', methods=['POST'])
    @subscriber_login_required
    def register_services(service_id):
        """Handle services registration with pricing plan"""
        service = Service.query.get_or_404(service_id)
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
            service_id=service_id,
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
            flash(f'Successfully registered for {service.name} - Free Plan!', 'success')
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

        return render_template('/payment/payment_processing.html', subscription=subscription)

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

    @app.route('/subscriber_logout')
    def subscriber_logout():
        """Logout subscriber"""
        session.pop('subscriber_id', None)
        session.pop('subscriber_email', None) 
        session.pop('subscriber_name', None)
        flash('You have been logged out successfully.', 'success')
        return redirect(url_for('subscriber_login'))

    @app.route('/subscriber_profile')
    @subscriber_login_required
    def subscriber_profile():
        """Display and edit subscriber profile"""
        user_id = session.get('subscriber_id')
        user = User.query.get(user_id)
        subscriptions = UserSubscription.query.filter_by(user_id=user_id).all()
        return render_template('/user/subscriber_profile.html', user=user, subscriptions=subscriptions)

    @app.route('/subscriber_profile/<int:user_id>')
    def public_subscriber_profile(user_id):
        """Display public subscriber profile"""
        from models import Follow
        user = User.query.get_or_404(user_id)

        # Get user's subscriptions
        subscriptions = UserSubscription.query.filter_by(user_id=user_id, status='active').all()

        # Get user's activity stats
        followers_count = Follow.query.filter_by(followed_id=user_id).count()
        following_count = Follow.query.filter_by(follower_id=user_id).count()

        return render_template('/user/subscriber_profile.html', 
                             user=user,
                             subscriptions=subscriptions,
                             followers_count=followers_count,
                             following_count=following_count,
                             is_public_view=True)

    @app.route('/subscriber_profile/update', methods=['POST'])
    @subscriber_login_required
    def update_subscriber_profile():
        """Update subscriber profile information"""
        user_id = session.get('subscriber_id')
        user = User.query.get(user_id)

        # Update profile fields
        user.first_name = request.form.get('first_name', user.first_name)
        user.mobile = request.form.get('mobile', user.mobile)
        user.phone_number = request.form.get('phone_number', user.phone_number)
        user.address = request.form.get('address', user.address)

        # Handle password update if provided
        new_password = request.form.get('new_password')
        if new_password:
            user.password_hash = generate_password_hash(new_password)

        db.session.commit()
        flash('Profile updated successfully!', 'success')
        return redirect(url_for('subscriber_profile'))