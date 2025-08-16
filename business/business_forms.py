from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import (
    StringField, TextAreaField, FloatField, IntegerField,
    SelectField, BooleanField, PasswordField, SelectMultipleField
)
from wtforms.validators import (
    DataRequired, Email, NumberRange, Optional, Length, EqualTo
)

# BUSINESS SERVICE FORMS - ISOLATED
# These forms are disconnected from the main application
# but preserved for future reintegration

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
    confirm_password = PasswordField('Confirm Password', validators=[
        DataRequired(), EqualTo('password', message='Passwords must match')
    ])
    logo = FileField('Business Logo', validators=[FileAllowed(['jpg', 'png', 'jpeg', 'gif'])])
    business_card = FileField('Business Card', validators=[FileAllowed(['jpg', 'png', 'jpeg', 'pdf'])])
    id_proof = FileField('ID Proof', validators=[FileAllowed(['jpg', 'png', 'jpeg', 'pdf'])])
    business_proof = FileField('Business Proof/Registration', validators=[FileAllowed(['jpg', 'png', 'jpeg', 'pdf'])])

class BusinessProductForm(FlaskForm):
    product_name = StringField('Product Name', validators=[DataRequired(), Length(min=2, max=200)])
    description = TextAreaField('Description', validators=[Optional()])
    price = FloatField('Price', validators=[DataRequired(), NumberRange(min=0)])
    quantity = IntegerField('Quantity', validators=[DataRequired(), NumberRange(min=0)])
    weight = FloatField('Weight (kg)', validators=[Optional(), NumberRange(min=0)])
    dimensions = StringField('Dimensions (LxWxH)', validators=[Optional()])
    images = FileField('Product Images', validators=[FileAllowed(['jpg', 'png', 'jpeg', 'gif'])])
    is_active = BooleanField('Active', default=True)

class BusinessCustomerForm(FlaskForm):
    name = StringField('Customer Name', validators=[DataRequired(), Length(min=2, max=200)])
    phone_number = StringField('Phone Number', validators=[DataRequired(), Length(min=10, max=15)])
    email = StringField('Email', validators=[Optional(), Email()])
    address = TextAreaField('Address', validators=[Optional()])
    groups = StringField('Groups (comma-separated)', validators=[Optional()])