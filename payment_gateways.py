import os
import requests
import json
import logging
from datetime import datetime

# Payment gateway configurations
GPAY_MERCHANT_ID = os.environ.get("GPAY_MERCHANT_ID", "default_gpay_merchant")
PAYTM_MERCHANT_ID = os.environ.get("PAYTM_MERCHANT_ID", "default_paytm_merchant")
BRAINLO_API_KEY = os.environ.get("BRAINLO_API_KEY", "default_brainlo_key")

def process_payment(amount, payment_method, customer_info, order_id=None):
    """
    Process payment through selected gateway
    """
    try:
        if payment_method == 'gpay':
            return process_gpay_payment(amount, customer_info, order_id)
        elif payment_method == 'paytm':
            return process_paytm_payment(amount, customer_info, order_id)
        elif payment_method == 'brainlo':
            return process_brainlo_payment(amount, customer_info, order_id)
        else:
            return {
                'success': False,
                'error': 'Invalid payment method'
            }
    except Exception as e:
        logging.error(f"Payment processing error: {str(e)}")
        return {
            'success': False,
            'error': 'Payment processing failed'
        }

def process_gpay_payment(amount, customer_info, order_id):
    """
    Process GPay payment
    """
    try:
        # GPay API integration
        payload = {
            'merchant_id': GPAY_MERCHANT_ID,
            'amount': amount,
            'currency': 'INR',
            'order_id': order_id,
            'customer_name': customer_info.get('name'),
            'customer_phone': customer_info.get('phone'),
            'customer_email': customer_info.get('email'),
            'callback_url': 'https://your-domain.com/payment-callback',
            'timestamp': datetime.now().isoformat()
        }
        
        # For demo purposes, simulate successful payment
        # In production, replace with actual GPay API call
        response = {
            'status': 'success',
            'transaction_id': f"gpay_{datetime.now().strftime('%Y%m%d%H%M%S')}",
            'amount': amount,
            'currency': 'INR'
        }
        
        return {
            'success': True,
            'transaction_id': response['transaction_id'],
            'amount': response['amount'],
            'gateway_response': json.dumps(response)
        }
        
    except Exception as e:
        logging.error(f"GPay payment error: {str(e)}")
        return {
            'success': False,
            'error': 'GPay payment failed'
        }

def process_paytm_payment(amount, customer_info, order_id):
    """
    Process Paytm payment
    """
    try:
        # Paytm API integration
        payload = {
            'merchant_id': PAYTM_MERCHANT_ID,
            'amount': amount,
            'currency': 'INR',
            'order_id': order_id,
            'customer_name': customer_info.get('name'),
            'customer_phone': customer_info.get('phone'),
            'customer_email': customer_info.get('email'),
            'callback_url': 'https://your-domain.com/payment-callback',
            'timestamp': datetime.now().isoformat()
        }
        
        # For demo purposes, simulate successful payment
        # In production, replace with actual Paytm API call
        response = {
            'status': 'success',
            'transaction_id': f"paytm_{datetime.now().strftime('%Y%m%d%H%M%S')}",
            'amount': amount,
            'currency': 'INR'
        }
        
        return {
            'success': True,
            'transaction_id': response['transaction_id'],
            'amount': response['amount'],
            'gateway_response': json.dumps(response)
        }
        
    except Exception as e:
        logging.error(f"Paytm payment error: {str(e)}")
        return {
            'success': False,
            'error': 'Paytm payment failed'
        }

def process_brainlo_payment(amount, customer_info, order_id):
    """
    Process Brainlo payment
    """
    try:
        # Brainlo API integration
        headers = {
            'Authorization': f'Bearer {BRAINLO_API_KEY}',
            'Content-Type': 'application/json'
        }
        
        payload = {
            'amount': amount,
            'currency': 'INR',
            'order_id': order_id,
            'customer_name': customer_info.get('name'),
            'customer_phone': customer_info.get('phone'),
            'customer_email': customer_info.get('email'),
            'callback_url': 'https://your-domain.com/payment-callback',
            'timestamp': datetime.now().isoformat()
        }
        
        # For demo purposes, simulate successful payment
        # In production, replace with actual Brainlo API call
        response = {
            'status': 'success',
            'transaction_id': f"brainlo_{datetime.now().strftime('%Y%m%d%H%M%S')}",
            'amount': amount,
            'currency': 'INR'
        }
        
        return {
            'success': True,
            'transaction_id': response['transaction_id'],
            'amount': response['amount'],
            'gateway_response': json.dumps(response)
        }
        
    except Exception as e:
        logging.error(f"Brainlo payment error: {str(e)}")
        return {
            'success': False,
            'error': 'Brainlo payment failed'
        }

def verify_payment(transaction_id, payment_method):
    """
    Verify payment status
    """
    try:
        if payment_method == 'gpay':
            return verify_gpay_payment(transaction_id)
        elif payment_method == 'paytm':
            return verify_paytm_payment(transaction_id)
        elif payment_method == 'brainlo':
            return verify_brainlo_payment(transaction_id)
        else:
            return {
                'success': False,
                'error': 'Invalid payment method'
            }
    except Exception as e:
        logging.error(f"Payment verification error: {str(e)}")
        return {
            'success': False,
            'error': 'Payment verification failed'
        }

def verify_gpay_payment(transaction_id):
    """
    Verify GPay payment
    """
    # For demo purposes, simulate successful verification
    return {
        'success': True,
        'status': 'completed',
        'transaction_id': transaction_id
    }

def verify_paytm_payment(transaction_id):
    """
    Verify Paytm payment
    """
    # For demo purposes, simulate successful verification
    return {
        'success': True,
        'status': 'completed',
        'transaction_id': transaction_id
    }

def verify_brainlo_payment(transaction_id):
    """
    Verify Brainlo payment
    """
    # For demo purposes, simulate successful verification
    return {
        'success': True,
        'status': 'completed',
        'transaction_id': transaction_id
    }

def get_payment_methods():
    """
    Get available payment methods
    """
    return [
        {'id': 'gpay', 'name': 'Google Pay', 'enabled': True},
        {'id': 'paytm', 'name': 'Paytm', 'enabled': True},
        {'id': 'brainlo', 'name': 'Brainlo', 'enabled': True}
    ]

def format_payment_response(response):
    """
    Format payment response for display
    """
    if response.get('success'):
        return {
            'success': True,
            'message': 'Payment processed successfully',
            'transaction_id': response.get('transaction_id'),
            'amount': response.get('amount')
        }
    else:
        return {
            'success': False,
            'message': response.get('error', 'Payment failed'),
            'error_code': response.get('error_code')
        }
