import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import logging

# Email configuration
SMTP_SERVER = os.environ.get('SMTP_SERVER', 'smtp.gmail.com')
SMTP_PORT = int(os.environ.get('SMTP_PORT', '587'))
EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

def send_email(to_email, subject, body, attachment_path=None):
    """
    Send email with optional attachment
    """
    try:
        # Create message
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = to_email
        msg['Subject'] = subject
        
        # Add body to email
        msg.attach(MIMEText(body, 'plain'))
        
        # Add attachment if provided
        if attachment_path and os.path.exists(attachment_path):
            with open(attachment_path, "rb") as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header(
                    'Content-Disposition',
                    f'attachment; filename= {os.path.basename(attachment_path)}'
                )
                msg.attach(part)
        
        # Create SMTP session
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # Enable security
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        
        # Send email
        text = msg.as_string()
        server.sendmail(EMAIL_ADDRESS, to_email, text)
        server.quit()
        
        logging.info(f"Email sent successfully to {to_email}")
        return True
        
    except Exception as e:
        logging.error(f"Failed to send email to {to_email}: {str(e)}")
        return False

def send_order_confirmation_email(order):
    """
    Send order confirmation email
    """
    subject = f"Order Confirmation - Order #{order.id}"
    body = f"""
Dear {order.customer.name},

Thank you for your order! Here are the details:

Order ID: {order.id}
Order Date: {order.order_date.strftime('%B %d, %Y')}
Total Amount: ₹{order.total_amount:.2f}
Delivery Address: {order.delivery_address}

Order Items:
"""
    
    for item in order.order_items:
        body += f"- {item.product.product_name} x {item.quantity} = ₹{item.total:.2f}\n"
    
    body += f"""
Payment Status: {order.payment_status.title()}
Order Status: {order.order_status.title()}

We will keep you updated on your order status.

Best regards,
{order.business.business_name}
Contact: {order.business.contact_number}
"""
    
    return send_email(order.customer.email, subject, body)

def send_payment_confirmation_email(order, payment):
    """
    Send payment confirmation email
    """
    subject = f"Payment Confirmation - Order #{order.id}"
    body = f"""
Dear {order.customer.name},

Your payment has been successfully processed!

Payment Details:
- Order ID: {order.id}
- Amount Paid: ₹{payment.amount:.2f}
- Payment Method: {payment.payment_method.title()}
- Transaction ID: {payment.transaction_id}
- Payment Status: {payment.status.title()}

Your order is now being processed and will be shipped soon.

Best regards,
{order.business.business_name}
Contact: {order.business.contact_number}
"""
    
    return send_email(order.customer.email, subject, body)

def send_order_status_update_email(order, old_status, new_status):
    """
    Send order status update email
    """
    subject = f"Order Status Update - Order #{order.id}"
    body = f"""
Dear {order.customer.name},

Your order status has been updated:

Order ID: {order.id}
Previous Status: {old_status.title()}
New Status: {new_status.title()}

"""
    
    if new_status == 'shipped':
        body += "Your order has been shipped and is on its way!\n"
    elif new_status == 'delivered':
        body += "Your order has been delivered. Thank you for shopping with us!\n"
    elif new_status == 'cancelled':
        body += "Your order has been cancelled. If you have any questions, please contact us.\n"
    
    body += f"""
Best regards,
{order.business.business_name}
Contact: {order.business.contact_number}
"""
    
    return send_email(order.customer.email, subject, body)

def send_invoice_email(order, invoice_path):
    """
    Send invoice email with PDF attachment
    """
    subject = f"Invoice for Order #{order.id}"
    body = f"""
Dear {order.customer.name},

Please find attached the invoice for your recent order.

Order Details:
- Order ID: {order.id}
- Order Date: {order.order_date.strftime('%B %d, %Y')}
- Total Amount: ₹{order.total_amount:.2f}

Thank you for your business!

Best regards,
{order.business.business_name}
Contact: {order.business.contact_number}
"""
    
    return send_email(order.customer.email, subject, body, invoice_path)

def send_business_verification_email(business):
    """
    Send business verification status email
    """
    subject = f"Business Verification Status - {business.business_name}"
    
    if business.verification_status == 'verified':
        body = f"""
Dear {business.business_name},

Congratulations! Your business registration has been verified and approved.

You can now access all features of our mobile shop management system:
- Add unlimited products
- Process orders
- Accept payments through multiple gateways
- Send SMS notifications to customers

Welcome to our platform!

Best regards,
Mobile Shop Management Team
"""
    else:
        body = f"""
Dear {business.business_name},

Thank you for registering your business with us.

Your business verification is currently: {business.verification_status.title()}

We will review your submitted documents and notify you once the verification is complete.

Best regards,
Mobile Shop Management Team
"""
    
    return send_email(business.email, subject, body)

def test_email_connection():
    """
    Test email connection and send a test email
    """
    try:
        # Test SMTP connection
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.quit()
        
        logging.info("Email connection test successful")
        return True
        
    except Exception as e:
        logging.error(f"Email connection test failed: {str(e)}")
        return False

def send_test_email(to_email):
    """
    Send a test email to verify email functionality
    """
    subject = "Test Email from Mobile Shop Management System"
    body = """
This is a test email from your Mobile Shop Management System.

If you receive this email, the email configuration is working correctly.

Features that will use email:
- Order confirmations
- Payment confirmations
- Order status updates
- Invoice delivery
- Business verification notifications

Best regards,
Mobile Shop Management System
"""
    
    return send_email(to_email, subject, body)

def get_email_settings():
    """
    Get current email configuration settings
    """
    return {
        'smtp_server': SMTP_SERVER,
        'smtp_port': SMTP_PORT,
        'email_address': EMAIL_ADDRESS,
        'email_configured': bool(EMAIL_ADDRESS and EMAIL_PASSWORD)
    }