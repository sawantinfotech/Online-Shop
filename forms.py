from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import (
    StringField, TextAreaField, FloatField, IntegerField,
    SelectField, BooleanField, PasswordField, SelectMultipleField
)
from wtforms.validators import (
    DataRequired, Email, NumberRange, Optional, Length, EqualTo
)
# ---------------- Business Form DISCONNECTED ----------------
# BUSINESS SERVICE ISOLATED - Form disabled
# class BusinessRegistrationForm(FlaskForm):
#     business_name = StringField('Business Name', validators=[DataRequired(), Length(min=2, max=200)])
#     service_id = SelectField('Service', coerce=int, validators=[Optional()])
#     category_id = SelectField('Category', coerce=int, validators=[Optional()])
#     contact_number = StringField('Contact Number', validators=[DataRequired(), Length(min=10, max=15)])
#     email = StringField('Email', validators=[DataRequired(), Email()])
#     address = TextAreaField('Address', validators=[DataRequired()])
#     business_type = SelectField('Business Type', choices=[
#         ('', 'Select Business Type'),
#         ('retail', 'Retail'),
#         ('wholesale', 'Wholesale'),
#         ('service', 'Service'),
#         ('manufacturing', 'Manufacturing'),
#         ('other', 'Other')
#     ], validators=[DataRequired()])
#     license_number = StringField('License Number', validators=[Optional()])
#     password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
#     confirm_password = PasswordField('Confirm Password', validators=[
#         DataRequired(), EqualTo('password', message='Passwords must match')
#     ])
#     logo = FileField('Business Logo', validators=[FileAllowed(['jpg', 'png', 'jpeg', 'gif'])])
#     business_card = FileField('Business Card', validators=[FileAllowed(['jpg', 'png', 'jpeg', 'pdf'])])
#     id_proof = FileField('ID Proof', validators=[FileAllowed(['jpg', 'png', 'jpeg', 'pdf'])])
#     business_proof = FileField('Business Proof/Registration', validators=[FileAllowed(['jpg', 'png', 'jpeg', 'pdf'])])

# BUSINESS SERVICE DISCONNECTED - ProductForm moved to business folder
# class ProductForm - REMOVED (business-dependent)

# BUSINESS SERVICE DISCONNECTED - CustomerForm moved to business folder
# class CustomerForm - REMOVED (business-dependent)

# BUSINESS SERVICE DISCONNECTED - OrderForm moved to business folder
# class OrderForm - REMOVED (business-dependent)

# ---------------- Payment Settings ----------------

class PaymentSettingsForm(FlaskForm):
    # service_id = SelectField('Service', coerce=int, validators=[DataRequired()])  # BUSINESS SERVICE DISCONNECTED
    gpay_enabled = BooleanField('Enable GPay')
    paytm_enabled = BooleanField('Enable Paytm')
    brainlo_enabled = BooleanField('Enable Brainlo')

# ---------------- Login Form ----------------

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    mobile = StringField('Mobile', validators=[DataRequired(), Length(min=10, max=15)])
    password = PasswordField('Password', validators=[DataRequired()])

# BUSINESS SERVICE DISCONNECTED - SMSTemplateForm moved to business folder  
# class SMSTemplateForm - REMOVED (business-dependent)

# ---------------- App Submission Form ----------------

class AppSubmissionForm(FlaskForm):
    app_name = StringField('App Name', validators=[DataRequired(), Length(min=2, max=200)])
    app_description = TextAreaField('App Description', validators=[DataRequired(), Length(min=50, max=1000)])
    app_service = SelectField('App Service', choices=[
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
        ('Job', 'Job'),
        ('Other', 'Other')
    ], validators=[DataRequired()])
    app_category = SelectField('App Category', choices=[
        ('', 'Select Category'),
        ('Business', 'Business'),
        ('Education', 'Education'),
        ('Entertainment', 'Entertainment'),
        ('Social', 'Social'),
        ('Medical', 'Medical'),
        ('Other', 'Other')
    ], validators=[DataRequired()])
    app_version = StringField('App Version', validators=[DataRequired(), Length(min=1, max=20)])
    app_website = StringField('App Website', validators=[Optional(), Length(max=500)])
    app_download_url = StringField('Download URL', validators=[Optional(), Length(max=500)])

    developer_name = StringField('Developer Name', validators=[DataRequired(), Length(min=2, max=200)])
    developer_email = StringField('Developer Email', validators=[DataRequired(), Email()])
    developer_phone = StringField('Phone Number', validators=[Optional(), Length(max=20)])
    developer_company = StringField('Company/Organization', validators=[Optional(), Length(max=200)])
    developer_website = StringField('Developer Website', validators=[Optional(), Length(max=500)])

    app_logo = FileField('App Logo', validators=[
        FileAllowed(['jpg', 'jpeg', 'png', 'gif'], 'Images only!'),
        DataRequired('Please upload an app logo')
    ])
    app_screenshots = FileField('App Screenshots (up to 5)', validators=[
        FileAllowed(['jpg', 'jpeg', 'png', 'gif'], 'Images only!')
    ])
    app_apk_file = FileField('APK File (max 20MB)', validators=[
        Optional(), FileAllowed(['apk', 'ipa', 'exe', 'dmg', 'deb', 'rpm'], 'App files only!')
    ])
    app_documentation = FileField('Documentation', validators=[
        Optional(), FileAllowed(['pdf', 'doc', 'docx'], 'Docs only!')
    ])
    
    # Authentication Options for App Files
    github_repo_url = StringField('GitHub Repository URL', validators=[Optional(), Length(max=500)])
    google_play_url = StringField('Google Play Store URL', validators=[Optional(), Length(max=500)])
    apple_store_url = StringField('Apple App Store URL', validators=[Optional(), Length(max=500)])
    official_website_url = StringField('Official Download URL', validators=[Optional(), Length(max=500)])
    
    # File verification method
    verification_method = SelectField('File Verification Method', choices=[
        ('upload', 'Upload File Directly (up to 20MB)'),
        ('github', 'GitHub Repository Link'),
        ('store', 'App Store Link (Google Play/Apple Store)'),
        ('website', 'Official Website Download Link')
    ], validators=[DataRequired()], default='upload')

    app_features = TextAreaField('Key Features', validators=[DataRequired()])
    target_audience = StringField('Target Audience', validators=[DataRequired(), Length(max=200)])
    app_size = StringField('App Size', validators=[DataRequired(), Length(max=50)])
    minimum_os_version = StringField('Minimum OS Version', validators=[DataRequired(), Length(max=50)])
    permissions_required = TextAreaField('Permissions Required', validators=[Optional()])

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

    privacy_policy_url = StringField('Privacy Policy URL', validators=[Optional(), Length(max=500)])
    terms_of_service_url = StringField('Terms of Service URL', validators=[Optional(), Length(max=500)])
    terms_accepted = BooleanField('Accept Terms', validators=[DataRequired()])
    
    # Plan Selection  
    plan_type = SelectField('Select Plan', choices=[
        ('', 'Choose Your Plan'),
        ('basic', 'Basic Plan - Free (Limited features)'),
        ('standard', 'Standard Plan - $9.99/month (Full features)'),
        ('premium', 'Premium Plan - $19.99/month (Priority support + Advanced analytics)'),
        ('enterprise', 'Enterprise Plan - $49.99/month (Custom integrations + Dedicated support)')
    ], validators=[DataRequired()])
    # --- Matrimony Registration Form --------

class MatrimonyRegistrationForm(FlaskForm):
    # service_id = SelectField('Service', coerce=int, validators=[DataRequired()])  # BUSINESS SERVICE DISCONNECTED
    # Personal Details 
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=200)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=200)])
    date_of_birth = StringField('Date Of Birth', validators=[DataRequired(), Length(min=10, max=10)])
    age = IntegerField('Age', validators=[DataRequired(), NumberRange(min=15, max=80)])
    gender = SelectField('Gender', choices=[
        ('', 'Select Gender'),
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Threemale', 'Threemale'),
        ('Transgender', 'Transgender')
    ], validators=[DataRequired()])
    language = SelectField('Language', choices=[
        ('', 'Select Language'),
        ('boudh', 'boudh'),
        ('pali', 'Pali'),
        ('english', 'English'),
        ('hindi', 'Hindi')
    ], validators=[DataRequired()])
                           
    marital_status = SelectField('Marital Status', choices=[
        ('', 'Select Marital Status'),
        ('single', 'Single'),
        ('divorced', 'Divorced'),
        ('widowed', 'Widowed'),
        ('separated', 'Separated')
    ], validators=[DataRequired()])
    
    relationship_interest = SelectField('Relationship Interrest', choices=[
        ('', 'Select Relationship Interest'),
        ('friend', 'Friend'),
        ('party', 'For Party'),
        ('dating', 'Dating'),
        ('contract', 'Contract'),
        ('marriage', 'Marriage'),
        ('open', 'Open'),
        ('livein', 'Live In'),
        ('travel', 'Travel'),
        ('enjoyment', 'Enjoyment'),
        ('work', 'Work'),
        ('family', 'Family'),
        ('volunteer', 'Volunteer'),
        ('sex4baby', 'Sex 4 Baby')
    ], validators=[DataRequired()])
    
    
    # Contact Information
    email = StringField('Email', validators=[DataRequired(), Email()])
    mobile = StringField('Mobile Number', validators=[DataRequired(), Length(min=10, max=15)])
    phone = StringField('Phone Number', validators=[DataRequired(), Length(min=10, max=15)])
    
    # User Physical Details
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
    
    eye_color = SelectField('Eye Color', choices=[
        ('', 'Select Eye Color'),
        ('black', 'Black'),
        ('brown', 'Brown'),
        ('gray', 'Gray'),
        ('blue', 'Blue')
    ], validators=[Optional()])
    hair_color = SelectField('Hair Color', choices=[
        ('', 'Select Hair Color'),
        ('black', 'Black'),
        ('brown', 'Brown'),
        ('gray', 'Gray'),
        ('golden', 'Golden')
    ], validators=[Optional()])
    skin_tone = SelectField('Skin Tone', choices=[
        ('', 'Select Skin Tone'),
        ('black', 'Black'),
        ('brown', 'Brown'),
        ('white', 'White'),
        ('fair', 'Fair')
    ], validators=[Optional()])
    physical_disability = SelectField('Physical Disability', choices=[
        ('', 'Select Physical Disability'),
        ('blind', 'Blind'),
        ('dum', 'Dum'),
        ('deaf', 'Deaf'),
        ('spinalcord', 'Spinalcord')
    ], validators=[Optional()])
    mental_disability = SelectField('Mental Disability', choices=[
        ('', 'Select Mental Disability'),
        ('mental', 'Mental'),
        ('depression', 'Depression'),
        ('neuro', 'Neuro'),
        ('bipolar', 'Bipolar')
    ], validators=[Optional()])
    blood_group = SelectField('Blood Group', choices=[
        ('', 'Select Blood Group'),
        ('a+', 'A+'),
        ('a-', 'A-'),
        ('b+', 'B+'),
        ('b-', 'B-'),
        ('ab+', 'AB+'),
        ('ab-', 'AB-'),
        ('o+', 'O+')
        ('o-', 'O-')
    ], validators=[Optional()])
 

    # User Family Details
    
    father_name = StringField('Father Name', validators=[DataRequired(), Length(min=2, max=200)])
    mother_name = StringField('Mother Name', validators=[DataRequired(), Length(min=2, max=200)])
    brothers = StringField('Brothers Name', validators=[DataRequired(), Length(min=2, max=200)])
    sisters = StringField('Sisters Name', validators=[DataRequired(), Length(min=2, max=200)])
    family_type = StringField('Family Type', validators=[DataRequired(), Length(min=2, max=200)])
    family_status = StringField('Family Status', validators=[DataRequired(), Length(min=2, max=200)])
    family_values = StringField('Family Values', validators=[DataRequired(), Length(min=2, max=200)])
    ancestral_origin = StringField('Ancestral Origin', validators=[DataRequired(), Length(min=2, max=200)])
    social_group = SelectField('Social Group', choices=[
        ('', 'Select Social Group'),
        ('lower', 'Lower'),
        ('middle', 'Middle'),
        ('higher', 'Higher')
    ], validators=[Optional()])

    # User Horoscope Details
        
    religion = StringField('religion', validators=[DataRequired(), Length(min=2, max=200)])
    caste = StringField('caste', validators=[DataRequired(), Length(min=2, max=200)])
    subcaste = StringField('subcaste', validators=[DataRequired(), Length(min=2, max=200)])
    gothra = StringField('gothra', validators=[DataRequired(), Length(min=2, max=200)])
    dosham = StringField('dosham', validators=[DataRequired(), Length(min=2, max=200)])
    star = StringField('star', validators=[DataRequired(), Length(min=2, max=200)])
    raasi = StringField('raasi', validators=[DataRequired(), Length(min=2, max=200)])
    horoscope = StringField('horoscope', validators=[DataRequired(), Length(min=2, max=200)])
    
    # User Location
    address = StringField('Address', validators=[DataRequired(), Length(max=100)])
    city = StringField('City', validators=[DataRequired(), Length(max=100)])
    district = StringField('District', validators=[DataRequired(), Length(max=100)])
    pincode = StringField('Pincode', validators=[DataRequired(), Length(max=20)])
    state = StringField('State', validators=[DataRequired(), Length(max=100)])
    country = StringField('Country', validators=[DataRequired(), Length(max=100)], default='Buddhitan', 'India')
    nationality = StringField('nationality', validators=[DataRequired(), Length(max=100)], default='Buddhitan', 'India') 
    lives_in = StringField('Lives_in', validators=[DataRequired(), Length(max=100)], default='Buddhistan', 'India', 'UK')
    resident_status = StringField('Rresident_Status', validators=[DataRequired(), Length(max=100)], SelectField('resident_status', choices=[( 'Permanent'), ('Temporary'), ('Not Specified')])
    future_lives_in = StringField(' future_lives_in', validators=[DataRequired(), Length(max=100)], default='Buddhitan', 'India')
    # User Education & Career
    education = StringField('Education', validators=[DataRequired(), Length(max=200)])
    occupation = StringField('Occupation', validators=[DataRequired(), Length(max=200)])
    annual_income = SelectField('Annual Income', choices=[
        ('', 'Select Income Range'),
        ('Below 3 Lakhs', 'Below 3 Lakhs'),       
        ('5-10 Lakhs', '5-10 Lakhs'),
        ('10-15 Lakhs', '10-15 Lakhs'),        
        ('25-50 Lakhs', '25-50 Lakhs'),
        ('50+ Lakhs', '50+ Lakhs'),
        ('1+ Cr', '1+ Cr'),
        ('10-500 Cr', '10-500 Cr'),
        ('Not Employed', 'Not Employed')
    ], validators=[Optional()])
    company_name = StringField('Company Name', validators=[Optional(), Length(max=200)])
    
    # About You
    about_yourself = TextAreaField('About Yourself', validators=[DataRequired(), Length(min=50, max=1000)])
    
    # User Life Style
    hobbies = StringField('Hobbies', validators=[Optional(), Length(max=300)], default='Travel')
    smoking = StringField('Smoking', validators=[Optional(), Length(max=300)], default='Smoking','Occasionally', 'No', 'Not specified', '')
    drinking = StringField('Drinding', validators=[Optional(), Length(max=300)], default='Drinking', 'Occasionally', 'No', 'Not Specified', '')
    food = StringField('Food', validators=[Optional(), Length(max=300)], default='Food', 'Vegetarian', 'Non-Vegetarian', 'Not Specified', '')


    # Profile Images
    profile_images = FileField('Profile Images (up to 4)', validators=[
        FileAllowed(['jpg', 'jpeg', 'png', 'gif'], 'Images only!')
    ])
    family_images = FileField('Family Images (up to 1)', validators=[FileAllowed(['jpg', 'jpeg', 'png', 'gif'], 'Images only!')]) 
    
    # Membership
    membership_type = SelectField('Membership Type', choices=[
        ('basic', 'Basic (₹500/month)'),
        ('silver', 'Silver (₹999/month)'),
        ('gold', 'Gold (₹1999/month)'),
        ('platinum', 'Platinum (₹2999/month)')
    ], validators=[DataRequired()])
    
    # VIP-Documents Verification 
    document = FileField('Document (Optional)', validators=[FileAllowed(['jpg', 'jpeg', 'png', 'gif'], 'Images only!')])
    document = SelectField('Document', choices=[
        ('', 'Select Doc Status'),
        ('gov_id', 'Gov_ID'),
        ('family_photo', 'Family Photo'),
        ('birth', 'Birth Certificate'),
        ('educational', 'Educational Certificate'),
        ('occupation', 'Occupation Appointment Letter'),
        ('voter_id', 'Voter ID'),
        ('passport', 'Passport'),
        ('driving', 'Driving License'),
        ('bank_passbook', 'Bank Passbook'),
        ('address_proof', 'Address Proof'),
        ('work_permit', 'Work Permit'),
        ('income', 'Income Certificate'),
        ('marriage', 'Marriage Certificate'),
        ('divorce', 'Divorce Certificate'),
        ('children', 'Children_Certificate'),
        ('caste', 'Caste Certificate'),
        ('property', 'Property Certificate'),
        ('medical', 'Medical Proof'),
        ('sexual', 'Sexual Certificate'),
        ('mental', 'Mental Certificate'),
        ('physical', 'Physical Certificate'),
        ('criminal', 'Criminal Certificate'),
        ('police_noc', 'Police NOC'),
        ('medical_certificate ', 'Medical Certificate'),
        ('biometric_certificate', 'Biometric Certificate'),
        ('horoscope', 'Horoscope Certificate')
    ], validators=[DataRequired()])

    # Biometric Test Details 
    biometric_test = FileField('Biometric Test (Optional)', validators=[FileAllowed(['jpg', 'jpeg', 'png', 'gif'], 'Images only!')])
    document = SelectField('Documet', choices=[
        ('', 'Select Biometric Recognition Status'),
        
        ('finger_print', 'Finger Print Recognition'),
        ('voice_recognition', 'Voice Recognition'),
        ('faceial_recognition', 'Facial Recognition Recognition'),
        ('palm_recognition', 'Palm Print Recognition'),
        ('eye_recognition', 'Eye (IRIS/Retina) Recognition'),
        ('ear_recognition', 'Ear Recognition'),
        ('heartbeat', 'Heartbeat Recognition'),
        ('bone_marrow', 'Bone Marrow Recognition'),
        ('hla_tissue', 'HLA Tissue Recognition'),
        ('blood_stem_cell', 'Blood Stem Cell Recognition'),
        ('dna', 'DNA Recognition')
    ], validators=[DataRequired()])
    
    # Partner Preferences ()
    # Profile Matching- Personal Details
    partner_age_min = IntegerField('Partner Age (Min)', validators=[Optional(), NumberRange(min=15, max=80)])
    partner_age_max = IntegerField('Partner Age (Max)', validators=[Optional(), NumberRange(min=15, max=80)])
    partner_height_min = StringField('Partner Height (Min)', validators=[Optional(), Length(max=10)])
    partner_height_max = StringField('Partner Height (Max)', validators=[Optional(), Length(max=10)])
    partner_gender = StringField('Partner Gender', validators=[Optional(), Length(max=200)])
    partner_marital_status = StringField('Partner Marital Status ', validators=[Optional(), Length(max=200)])
    partner_relationship_interest = SelectField('Partner Relationship Interest', choices=[
        ('', 'Not Specified'),
        ('marriage', 'marriage'),
        ('relationship', 'relationship'),
        ('friendship', 'friendship'),
        ('for party', 'for party'),        
        ('open', 'open'),
        ('dating', 'dating'),
        ('contract', 'contract'),
        ('livein', 'livein'),
        ('enjoyment', 'enjoyment'),
        ('travel', 'travel'),
        ('work', 'work'),
        ('family', 'family'),
        ('sex for baby', 'sex for baby'),
        ('volunteer', 'volunteer')
    ], validators=[Optional()]) 
    
    # Partner Religious Preferences
    partner_religion = StringField('Partner Religion', validators=[Optional(), Length(max=200)]),
    partner_language = StringField('Partner Language', validators=[Optional(), Length(max=200)]),
    partner_cast = StringField('Partner Cast', validators=[Optional(), Length(max=200)]),

     # Partner Professional Preferences
        partner_education = StringField('Partner Education', validators=[Optional(), Length(max=200)]),
    partner_occupation = StringField('Partner Occupation', validators=[Optional(), Length(max=200)]),
    partner_income = SelectField('Partner Income Range', choices=[
        ('', 'No Preference'),
        ('Below 3 Lakhs', 'Below 3 Lakhs'),
        ('3-5 Lakhs', '3-5 Lakhs'),
        ('5-10 Lakhs', '5-10 Lakhs'),
        ('10-15 Lakhs', '10-15 Lakhs'),        
        ('25-50 Lakhs', '25-50 Lakhs'),
        ('50+ Lakhs', '50+ Lakhs'),
        ('1+ Cr', '1+ Cr'),
        ('10-500 Cr', '10-500 Cr'),
        ('Not Employed', 'Not Employed')
    ], validators=[Optional()])
        # Parner Location Preferences
address = StringField('Address', validators=[DataRequired(), Length(max=100)])
city = StringField('City', validators=[DataRequired(), Length(max=100)])
district = StringField('District', validators=[DataRequired(), Length(max=100)])
pincode = StringField('Pincode', validators=[DataRequired(), Length(max=20)])
state = StringField('State', validators=[DataRequired(), Length(max=100)])
country = StringField('Country', validators=[DataRequired(), Length(max=100)], default='Buddhitan', 'India')
nationality = StringField('nationality', validators=[DataRequired(), Length(max=100)], default='Buddhitan', 'India') 
lives_in = StringField('Lives_in', validators=[DataRequired(), Length(max=100)], default='Buddhistan', 'India', 'UK')
resident_status = StringField('Rresident_Status', validators=[DataRequired(), Length(max=100)], SelectField('resident_status', choices=[( 'Permanent'), ('Temporary'), ('Not Specified')])
future_lives_in = StringField(' future_lives_in', validators=[DataRequired(), Length(max=100)], default='Buddhitan', 'India')
      
    # Legal
    privacy_policy_url = StringField('Privacy Policy URL (Optional)', validators=[Optional(), Length(max=500)])
    terms_of_service_url = StringField('Terms of Service URL (Optional)', validators=[Optional(), Length(max=500)])
    terms_accepted = BooleanField('I accept the Terms and Conditions', validators=[DataRequired()])


