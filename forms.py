from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, TextAreaField, FloatField, IntegerField, SelectField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Email, NumberRange, Optional, Length

class BusinessRegistrationForm(FlaskForm):
    business_name = StringField('Business Name', validators=[DataRequired(), Length(min=2, max=200)])
    contact_number = StringField('Contact Number', validators=[DataRequired(), Length(min=10, max=15)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    address = TextAreaField('Address', validators=[DataRequired()])
    business_type = SelectField('Business Type', choices=[
        ('', 'Select Business Type'),
        ('retail', 'Retail'),
        ('wholesale', 'Wholesale'),
        ('service', 'Service'),
        ('manufacturing', 'Manufacturing'),
        ('other', 'Other')
    ], validators=[DataRequired()])
    license_number = StringField('License Number', validators=[Optional()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    logo = FileField('Business Logo', validators=[FileAllowed(['jpg', 'png', 'jpeg', 'gif'])])
    business_card = FileField('Business Card', validators=[FileAllowed(['jpg', 'png', 'jpeg', 'pdf'])])
    id_proof = FileField('ID Proof', validators=[FileAllowed(['jpg', 'png', 'jpeg', 'pdf'])])
    business_proof = FileField('Business Proof/Registration', validators=[FileAllowed(['jpg', 'png', 'jpeg', 'pdf'])])

class ProductForm(FlaskForm):
    product_name = StringField('Product Name', validators=[DataRequired(), Length(min=2, max=200)])
    category_id = SelectField('Category', coerce=int, validators=[Optional()])
    description = TextAreaField('Description', validators=[Optional()])
    price = FloatField('Price', validators=[DataRequired(), NumberRange(min=0)])
    quantity = IntegerField('Quantity', validators=[DataRequired(), NumberRange(min=0)])
    weight = FloatField('Weight (kg)', validators=[Optional(), NumberRange(min=0)])
    dimensions = StringField('Dimensions (LxWxH)', validators=[Optional()])
    images = FileField('Product Images', validators=[FileAllowed(['jpg', 'png', 'jpeg', 'gif'])])
    is_active = BooleanField('Active', default=True)

class CustomerForm(FlaskForm):
    name = StringField('Customer Name', validators=[DataRequired(), Length(min=2, max=200)])
    phone_number = StringField('Phone Number', validators=[DataRequired(), Length(min=10, max=15)])
    email = StringField('Email', validators=[Optional(), Email()])
    address = TextAreaField('Address', validators=[Optional()])
    groups = StringField('Groups (comma-separated)', validators=[Optional()])

class OrderForm(FlaskForm):
    customer_id = SelectField('Customer', coerce=int, validators=[DataRequired()])
    delivery_address = TextAreaField('Delivery Address', validators=[DataRequired()])
    delivery_type = SelectField('Delivery Type', choices=[
        ('standard', 'Standard'),
        ('express', 'Express'),
        ('scheduled', 'Scheduled')
    ], validators=[DataRequired()])

class PaymentSettingsForm(FlaskForm):
    gpay_enabled = BooleanField('Enable GPay')
    paytm_enabled = BooleanField('Enable Paytm')
    brainlo_enabled = BooleanField('Enable Brainlo')
    
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])

class SMSTemplateForm(FlaskForm):
    template_name = StringField('Template Name', validators=[DataRequired(), Length(min=2, max=100)])
    template_content = TextAreaField('Template Content', validators=[DataRequired()])
    template_type = SelectField('Template Type', choices=[
        ('order_confirmation', 'Order Confirmation'),
        ('payment_confirmation', 'Payment Confirmation'),
        ('delivery_update', 'Delivery Update'),
        ('promotional', 'Promotional'),
        ('reminder', 'Reminder')
    ], validators=[DataRequired()])
    is_active = BooleanField('Active', default=True)

class AppSubmissionForm(FlaskForm):
    # Basic App Information
    app_name = StringField('App Name', validators=[DataRequired(), Length(min=2, max=200)])
    app_description = TextAreaField('App Description', validators=[DataRequired(), Length(min=50, max=1000)])
    app_category = SelectField('App Category', choices=[
        ('', 'Select Category'),
        ('Business', 'Business'),
        ('Communication', 'Communication'),
        ('Education', 'Education'),
        ('Entertainment', 'Entertainment'),
        ('Finance', 'Finance'),
        ('Health & Fitness', 'Health & Fitness'),
        ('Lifestyle', 'Lifestyle'),
        ('Productivity', 'Productivity'),
        ('Shopping', 'Shopping'),
        ('Social', 'Social'),
        ('Travel', 'Travel'),
        ('Utilities', 'Utilities'),
        ('Games', 'Games'),
        ('News', 'News'),
        ('Photography', 'Photography'),
        ('Music', 'Music'),
        ('Sports', 'Sports'),
        ('Weather', 'Weather'),
        ('Books', 'Books'),
        ('Food & Drink', 'Food & Drink'),
        ('Medical', 'Medical'),
        ('Navigation', 'Navigation'),
        ('Real Estate', 'Real Estate'),
        ('Reference', 'Reference'),
        ('Legal', 'Legal'),
        ('Security', 'Security'),
        ('Public Services', 'Public Services'),
        ('Career', 'Career'),
        ('Other', 'Other')
    ], validators=[DataRequired()])
    app_version = StringField('App Version', validators=[DataRequired(), Length(min=1, max=20)])
    app_website = StringField('App Website (Optional)', validators=[Optional(), Length(max=500)])
    app_download_url = StringField('Download URL (Optional)', validators=[Optional(), Length(max=500)])
    
    # Developer Information
    developer_name = StringField('Developer Name', validators=[DataRequired(), Length(min=2, max=200)])
    developer_email = StringField('Developer Email', validators=[DataRequired(), Email(), Length(max=200)])
    developer_phone = StringField('Phone Number (Optional)', validators=[Optional(), Length(max=20)])
    developer_company = StringField('Company/Organization (Optional)', validators=[Optional(), Length(max=200)])
    developer_website = StringField('Developer Website (Optional)', validators=[Optional(), Length(max=500)])
    
    # App Files
    app_logo = FileField('App Logo', validators=[
        FileAllowed(['jpg', 'jpeg', 'png', 'gif'], 'Images only!'),
        DataRequired('Please upload an app logo')
    ])
    app_screenshots = FileField('App Screenshots (up to 5)', validators=[
        FileAllowed(['jpg', 'jpeg', 'png', 'gif'], 'Images only!')
    ])
    app_apk_file = FileField('APK File (Optional)', validators=[
        Optional(),
        FileAllowed(['apk'], 'APK files only!')
    ])
    app_documentation = FileField('Documentation (Optional)', validators=[
        Optional(),
        FileAllowed(['pdf', 'doc', 'docx'], 'Documents only!')
    ])
    
    # App Details
    app_features = TextAreaField('Key Features (one per line)', validators=[DataRequired()])
    target_audience = StringField('Target Audience', validators=[DataRequired(), Length(max=200)])
    app_size = StringField('App Size (e.g., 25 MB)', validators=[DataRequired(), Length(max=50)])
    minimum_os_version = StringField('Minimum OS Version', validators=[DataRequired(), Length(max=50)])
    permissions_required = TextAreaField('Permissions Required (one per line)', validators=[Optional()])
    
    # Pricing
    app_price = SelectField('App Price', choices=[
        ('Free', 'Free'),
        ('$0.99', '$0.99'),
        ('$1.99', '$1.99'),
        ('$2.99', '$2.99'),
        ('$4.99', '$4.99'),
        ('$9.99', '$9.99'),
        ('$19.99', '$19.99'),
        ('$49.99', '$49.99'),
        ('Custom', 'Custom Price')
    ], validators=[DataRequired()])
    
    monetization_model = SelectField('Monetization Model', choices=[
        ('Free', 'Free'),
        ('Paid', 'Paid'),
        ('Freemium', 'Freemium'),
        ('Ad-supported', 'Ad-supported'),
        ('In-app purchases', 'In-app purchases'),
        ('Subscription', 'Subscription')
    ], validators=[DataRequired()])
    
    # Legal
    privacy_policy_url = StringField('Privacy Policy URL (Optional)', validators=[Optional(), Length(max=500)])
    terms_of_service_url = StringField('Terms of Service URL (Optional)', validators=[Optional(), Length(max=500)])
    terms_accepted = BooleanField('I accept the App Store Terms and Conditions', validators=[DataRequired()])

class MatrimonyRegistrationForm(FlaskForm):
    # Basic Information
    full_name = StringField('Full Name', validators=[DataRequired(), Length(min=2, max=200)])
    age = IntegerField('Age', validators=[DataRequired(), NumberRange(min=18, max=80)])
    gender = SelectField('Gender', choices=[
        ('', 'Select Gender'),
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    ], validators=[DataRequired()])
    marital_status = SelectField('Marital Status', choices=[
        ('', 'Select Marital Status'),
        ('single', 'Single'),
        ('divorced', 'Divorced'),
        ('widowed', 'Widowed')
    ], validators=[DataRequired()])
    
    # Contact Information
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone Number', validators=[DataRequired(), Length(min=10, max=15)])
    
    # Physical Details
    height = StringField('Height (e.g., 5\'8")', validators=[DataRequired(), Length(max=10)])
    weight = StringField('Weight (e.g., 65kg)', validators=[Optional(), Length(max=10)])
    body_type = SelectField('Body Type', choices=[
        ('', 'Select Body Type'),
        ('slim', 'Slim'),
        ('average', 'Average'),
        ('athletic', 'Athletic'),
        ('heavy', 'Heavy')
    ], validators=[Optional()])
    complexion = SelectField('Complexion', choices=[
        ('', 'Select Complexion'),
        ('fair', 'Fair'),
        ('medium', 'Medium'),
        ('dark', 'Dark')
    ], validators=[Optional()])
    
    # Location
    city = StringField('City', validators=[DataRequired(), Length(max=100)])
    state = StringField('State', validators=[DataRequired(), Length(max=100)])
    country = StringField('Country', validators=[DataRequired(), Length(max=100)], default='India')
    
    # Education & Career
    education = StringField('Education', validators=[DataRequired(), Length(max=200)])
    occupation = StringField('Occupation', validators=[DataRequired(), Length(max=200)])
    annual_income = SelectField('Annual Income', choices=[
        ('', 'Select Income Range'),
        ('Below 3 Lakhs', 'Below 3 Lakhs'),
        ('3-5 Lakhs', '3-5 Lakhs'),
        ('5-10 Lakhs', '5-10 Lakhs'),
        ('10-15 Lakhs', '10-15 Lakhs'),
        ('15-25 Lakhs', '15-25 Lakhs'),
        ('25-50 Lakhs', '25-50 Lakhs'),
        ('50+ Lakhs', '50+ Lakhs')
    ], validators=[Optional()])
    company_name = StringField('Company Name', validators=[Optional(), Length(max=200)])
    
    # About You
    about_yourself = TextAreaField('About Yourself', validators=[DataRequired(), Length(min=50, max=1000)])
    hobbies = StringField('Hobbies & Interests', validators=[Optional(), Length(max=300)])
    
    # Partner Preferences
    preferred_age_min = IntegerField('Preferred Partner Age (Min)', validators=[Optional(), NumberRange(min=18, max=80)])
    preferred_age_max = IntegerField('Preferred Partner Age (Max)', validators=[Optional(), NumberRange(min=18, max=80)])
    preferred_height_min = StringField('Preferred Height (Min)', validators=[Optional(), Length(max=10)])
    preferred_height_max = StringField('Preferred Height (Max)', validators=[Optional(), Length(max=10)])
    preferred_education = StringField('Preferred Education', validators=[Optional(), Length(max=200)])
    preferred_occupation = StringField('Preferred Occupation', validators=[Optional(), Length(max=200)])
    preferred_income = SelectField('Preferred Income Range', choices=[
        ('', 'No Preference'),
        ('Below 3 Lakhs', 'Below 3 Lakhs'),
        ('3-5 Lakhs', '3-5 Lakhs'),
        ('5-10 Lakhs', '5-10 Lakhs'),
        ('10-15 Lakhs', '10-15 Lakhs'),
        ('15-25 Lakhs', '15-25 Lakhs'),
        ('25-50 Lakhs', '25-50 Lakhs'),
        ('50+ Lakhs', '50+ Lakhs')
    ], validators=[Optional()])
    
    # Profile Images
    profile_images = FileField('Profile Images (up to 5)', validators=[
        FileAllowed(['jpg', 'jpeg', 'png', 'gif'], 'Images only!')
    ])
    
    # Membership
    membership_type = SelectField('Membership Type', choices=[
        ('basic', 'Basic (Free)'),
        ('silver', 'Silver (₹999/month)'),
        ('gold', 'Gold (₹1999/month)'),
        ('platinum', 'Platinum (₹2999/month)')
    ], validators=[DataRequired()])
    
    # Terms
    terms_accepted = BooleanField('I accept the Terms and Conditions', validators=[DataRequired()])
