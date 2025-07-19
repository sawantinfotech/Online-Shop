"""
CSV Import/Export Routes for Mobile Shop Management System
"""

from flask import request, redirect, url_for, flash, render_template, session
from werkzeug.utils import secure_filename
from app import app, db
from models import *
from csv_handler import CSVHandler, DemoDataGenerator
import os

# Allow CSV file uploads
ALLOWED_EXTENSIONS = {'csv'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/csv/export/<model_type>')
def export_csv(model_type):
    """Export data to CSV"""
    try:
        if model_type == 'businesses':
            data = Business.query.all()
            columns = ['id', 'name', 'description', 'email', 'phone', 'address', 'business_type', 'verification_status', 'created_at']
            filename = 'businesses_export'
            
        elif model_type == 'products':
            data = Product.query.all()
            columns = ['id', 'name', 'description', 'price', 'quantity', 'category', 'is_active', 'created_at']
            filename = 'products_export'
            
        elif model_type == 'customers':
            data = Customer.query.all()
            columns = ['id', 'name', 'email', 'phone', 'address', 'customer_group', 'created_at']
            filename = 'customers_export'
            
        elif model_type == 'apps':
            data = App.query.all()
            columns = ['id', 'name', 'short_description', 'category', 'author_name', 'rating', 'downloads', 'status', 'created_at']
            filename = 'apps_export'
            
        elif model_type == 'matrimony':
            data = MatrimonyProfile.query.all()
            columns = ['id', 'full_name', 'age', 'gender', 'marital_status', 'city', 'state', 'education', 'occupation', 'email', 'phone', 'created_at']
            filename = 'matrimony_profiles_export'
            
        elif model_type == 'categories':
            data = Category.query.all()
            columns = ['id', 'name', 'description', 'created_at']
            filename = 'categories_export'
            
        elif model_type == 'users':
            data = User.query.all()
            columns = ['id', 'full_name', 'email', 'mobile', 'user_type', 'is_verified', 'created_at']
            filename = 'users_export'
            
        else:
            flash('Invalid export type', 'error')
            return redirect(request.referrer or url_for('index'))
        
        return CSVHandler.export_to_csv(data, columns, filename)
        
    except Exception as e:
        flash(f'Export failed: {str(e)}', 'error')
        return redirect(request.referrer or url_for('index'))

@app.route('/csv/import/<model_type>', methods=['POST'])
def import_csv(model_type):
    """Import data from CSV"""
    try:
        if 'csv_file' not in request.files:
            flash('No file selected', 'error')
            return redirect(request.referrer or url_for('index'))
        
        file = request.files['csv_file']
        if file.filename == '':
            flash('No file selected', 'error')
            return redirect(request.referrer or url_for('index'))
        
        if not allowed_file(file.filename):
            flash('Invalid file format. Please upload a CSV file.', 'error')
            return redirect(request.referrer or url_for('index'))
        
        # Determine model and required fields
        user_id = session.get('user_id') or session.get('subscriber_id')
        
        if model_type == 'businesses':
            model_class = Business
            required_fields = ['name', 'email']
            
        elif model_type == 'products':
            model_class = Product
            required_fields = ['name', 'price']
            
        elif model_type == 'customers':
            model_class = Customer
            required_fields = ['name', 'email']
            
        elif model_type == 'apps':
            model_class = App
            required_fields = ['name', 'category']
            
        elif model_type == 'matrimony':
            model_class = MatrimonyProfile
            required_fields = ['full_name', 'age', 'gender', 'city', 'state', 'email']
            
        elif model_type == 'categories':
            model_class = Category
            required_fields = ['name']
            
        elif model_type == 'users':
            model_class = User
            required_fields = ['full_name', 'email']
            
        else:
            flash('Invalid import type', 'error')
            return redirect(request.referrer or url_for('index'))
        
        # Process import
        imported_count, errors = CSVHandler.import_from_csv(file, model_class, required_fields, user_id)
        
        if imported_count > 0:
            flash(f'Successfully imported {imported_count} records', 'success')
        
        if errors:
            error_message = f"Import completed with {len(errors)} errors: " + "; ".join(errors[:3])
            if len(errors) > 3:
                error_message += f" and {len(errors) - 3} more..."
            flash(error_message, 'warning')
        
        return redirect(request.referrer or url_for('index'))
        
    except Exception as e:
        flash(f'Import failed: {str(e)}', 'error')
        return redirect(request.referrer or url_for('index'))

@app.route('/csv/demo/generate')
def generate_demo_csv():
    """Generate demo CSV files"""
    try:
        demo_dir = DemoDataGenerator.create_demo_csv_files()
        flash(f'Demo CSV files generated successfully in {demo_dir}', 'success')
        return redirect(request.referrer or url_for('index'))
    except Exception as e:
        flash(f'Failed to generate demo CSV files: {str(e)}', 'error')
        return redirect(request.referrer or url_for('index'))

@app.route('/csv/demo/download/<filename>')
def download_demo_csv(filename):
    """Download demo CSV file"""
    try:
        demo_dir = 'uploads/demo_csv'
        filepath = os.path.join(demo_dir, filename)
        
        if not os.path.exists(filepath):
            # Generate demo files if they don't exist
            DemoDataGenerator.create_demo_csv_files()
        
        from flask import send_file
        return send_file(filepath, as_attachment=True, download_name=filename)
        
    except Exception as e:
        flash(f'Failed to download demo file: {str(e)}', 'error')
        return redirect(request.referrer or url_for('index'))

@app.route('/csv/demo/populate/<model_type>')
def populate_demo_data(model_type):
    """Populate demo data from CSV files"""
    try:
        demo_dir = 'uploads/demo_csv'
        
        # Ensure demo CSV files exist
        if not os.path.exists(demo_dir):
            DemoDataGenerator.create_demo_csv_files()
        
        filename_map = {
            'businesses': 'businesses.csv',
            'products': 'products.csv',
            'customers': 'customers.csv',
            'apps': 'apps.csv',
            'matrimony': 'matrimony_profiles.csv',
            'categories': 'categories.csv',
            'users': 'users.csv'
        }
        
        if model_type not in filename_map:
            flash('Invalid demo data type', 'error')
            return redirect(request.referrer or url_for('index'))
        
        filepath = os.path.join(demo_dir, filename_map[model_type])
        
        # Read and import demo data
        with open(filepath, 'rb') as f:
            user_id = session.get('user_id') or session.get('subscriber_id') or 1
            
            if model_type == 'businesses':
                model_class = Business
                required_fields = ['name', 'email']
            elif model_type == 'products':
                model_class = Product
                required_fields = ['name', 'price']
            elif model_type == 'customers':
                model_class = Customer
                required_fields = ['name', 'email']
            elif model_type == 'apps':
                model_class = App
                required_fields = ['name', 'category']
            elif model_type == 'matrimony':
                model_class = MatrimonyProfile
                required_fields = ['full_name', 'age', 'gender', 'city', 'state', 'email']
            elif model_type == 'categories':
                model_class = Category
                required_fields = ['name']
            elif model_type == 'users':
                model_class = User
                required_fields = ['full_name', 'email']
            
            imported_count, errors = CSVHandler.import_from_csv(f, model_class, required_fields, user_id)
            
            if imported_count > 0:
                flash(f'Successfully populated {imported_count} demo {model_type}', 'success')
            
            if errors:
                flash(f'Demo population completed with some errors', 'warning')
        
        return redirect(request.referrer or url_for('index'))
        
    except Exception as e:
        flash(f'Failed to populate demo data: {str(e)}', 'error')
        return redirect(request.referrer or url_for('index'))