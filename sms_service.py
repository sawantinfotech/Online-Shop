import os
import logging
from datetime import datetime

# SMS service configuration
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID", "default_twilio_sid")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN", "default_twilio_token")
TWILIO_PHONE_NUMBER = os.environ.get("TWILIO_PHONE_NUMBER", "+1234567890")

try:
    from twilio.rest import Client
    TWILIO_AVAILABLE = True
except ImportError:
    TWILIO_AVAILABLE = False
    logging.warning("Twilio library not available. SMS functionality will be simulated.")

def send_sms(to_phone_number, message, template_type='general'):
    """
    Send SMS message
    """
    try:
        if TWILIO_AVAILABLE:
            # Use Twilio to send SMS
            client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
            
            message = client.messages.create(
                body=message,
                from_=TWILIO_PHONE_NUMBER,
                to=to_phone_number
            )
            
            logging.info(f"SMS sent with SID: {message.sid}")
            return {
                'success': True,
                'message_sid': message.sid,
                'status': 'sent'
            }
        else:
            # Simulate SMS sending for demo
            logging.info(f"SMS simulated - To: {to_phone_number}, Message: {message}")
            return {
                'success': True,
                'message_sid': f"sim_{datetime.now().strftime('%Y%m%d%H%M%S')}",
                'status': 'sent'
            }
            
    except Exception as e:
        logging.error(f"SMS sending error: {str(e)}")
        return {
            'success': False,
            'error': str(e)
        }

def send_order_confirmation_sms(order):
    """
    Send order confirmation SMS
    """
    message = f"""
Order Confirmation - {order.business.business_name}

Order ID: #{order.id}
Date: {order.order_date.strftime('%d/%m/%Y')}
Total: ₹{order.total_amount:.2f}

Your order has been received and is being processed.

Thank you for your business!
    """.strip()
    
    return send_sms(order.customer.phone_number, message, 'order_confirmation')

def send_payment_confirmation_sms(order, payment):
    """
    Send payment confirmation SMS
    """
    message = f"""
Payment Confirmed - {order.business.business_name}

Order ID: #{order.id}
Amount: ₹{payment.amount:.2f}
Payment Method: {payment.payment_method.title()}
Transaction ID: {payment.transaction_id}

Your payment has been successfully processed.

Thank you!
    """.strip()
    
    return send_sms(order.customer.phone_number, message, 'payment_confirmation')

def send_order_status_update_sms(order, old_status, new_status):
    """
    Send order status update SMS
    """
    status_messages = {
        'confirmed': 'Your order has been confirmed and is being prepared.',
        'processing': 'Your order is being processed.',
        'shipped': 'Your order has been shipped and is on its way.',
        'delivered': 'Your order has been delivered successfully.',
        'cancelled': 'Your order has been cancelled.'
    }
    
    status_message = status_messages.get(new_status, f'Order status updated to {new_status}')
    
    message = f"""
Order Update - {order.business.business_name}

Order ID: #{order.id}
Status: {new_status.title()}

{status_message}

For any queries, contact: {order.business.contact_number}
    """.strip()
    
    return send_sms(order.customer.phone_number, message, 'status_update')

def send_delivery_update_sms(order, delivery):
    """
    Send delivery update SMS
    """
    message = f"""
Delivery Update - {order.business.business_name}

Order ID: #{order.id}
Delivery Status: {delivery.status.title()}
Tracking Number: {delivery.tracking_number}

Estimated Delivery: {delivery.estimated_time.strftime('%d/%m/%Y %I:%M %p') if delivery.estimated_time else 'TBD'}

Track your order or contact us: {order.business.contact_number}
    """.strip()
    
    return send_sms(order.customer.phone_number, message, 'delivery_update')

def send_promotional_sms(customer, message, business):
    """
    Send promotional SMS
    """
    full_message = f"""
{business.business_name}

{message}

Contact: {business.contact_number}
    """.strip()
    
    return send_sms(customer.phone_number, full_message, 'promotional')

def send_bulk_sms(customers, message, business):
    """
    Send bulk SMS to multiple customers
    """
    results = []
    
    for customer in customers:
        result = send_promotional_sms(customer, message, business)
        results.append({
            'customer_id': customer.id,
            'customer_name': customer.name,
            'phone_number': customer.phone_number,
            'success': result['success'],
            'error': result.get('error') if not result['success'] else None
        })
    
    return results

def get_sms_templates():
    """
    Get predefined SMS templates
    """
    templates = {
        'order_confirmation': 'Hi {customer_name}, your order #{order_id} has been received. Total: ₹{total_amount}. Thank you!',
        'payment_confirmation': 'Hi {customer_name}, payment of ₹{amount} for order #{order_id} has been confirmed. Transaction ID: {transaction_id}',
        'order_shipped': 'Hi {customer_name}, your order #{order_id} has been shipped. Track with: {tracking_number}',
        'order_delivered': 'Hi {customer_name}, your order #{order_id} has been delivered successfully. Thank you for choosing us!',
        'promotional': 'Special offer! Get {discount}% off on your next purchase. Use code: {promo_code}. Valid till {expiry_date}.',
        'reminder': 'Hi {customer_name}, you have items in your cart. Complete your purchase now and get free delivery!',
        'welcome': 'Welcome to {business_name}! Thank you for joining us. Enjoy exclusive deals and offers.'
    }
    
    return templates

def format_sms_template(template, **kwargs):
    """
    Format SMS template with provided data
    """
    try:
        return template.format(**kwargs)
    except KeyError as e:
        logging.error(f"SMS template formatting error: Missing key {e}")
        return template

def validate_phone_number(phone_number):
    """
    Validate phone number format
    """
    # Remove spaces and special characters
    cleaned = ''.join(filter(str.isdigit, phone_number))
    
    # Check if it's a valid Indian mobile number
    if len(cleaned) == 10 and cleaned.startswith(('6', '7', '8', '9')):
        return f"+91{cleaned}"
    elif len(cleaned) == 12 and cleaned.startswith('91'):
        return f"+{cleaned}"
    elif len(cleaned) == 13 and cleaned.startswith('+91'):
        return cleaned
    else:
        return None

def get_sms_delivery_status(message_sid):
    """
    Get SMS delivery status
    """
    try:
        if TWILIO_AVAILABLE:
            client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
            message = client.messages(message_sid).fetch()
            
            return {
                'success': True,
                'status': message.status,
                'error_code': message.error_code,
                'error_message': message.error_message
            }
        else:
            # Simulate delivery status for demo
            return {
                'success': True,
                'status': 'delivered',
                'error_code': None,
                'error_message': None
            }
            
    except Exception as e:
        logging.error(f"SMS status check error: {str(e)}")
        return {
            'success': False,
            'error': str(e)
        }
