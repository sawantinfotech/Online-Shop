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
