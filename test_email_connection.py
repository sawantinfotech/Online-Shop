#!/usr/bin/env python3
"""
Email Connection Test Script
This script tests the email configuration and sends a test email.
"""

import os
import sys
from email_service import test_email_connection, send_test_email, get_email_settings

def main():
    print("=== Mobile Shop Email System Test ===\n")
    
    # Get email settings
    settings = get_email_settings()
    
    print("Email Configuration:")
    print(f"  SMTP Server: {settings['smtp_server']}")
    print(f"  SMTP Port: {settings['smtp_port']}")
    print(f"  Email Address: {settings['email_address'] or 'Not configured'}")
    print(f"  Status: {'Configured' if settings['email_configured'] else 'Not Configured'}")
    print()
    
    if not settings['email_configured']:
        print("❌ Email not configured!")
        print("\nTo configure email, set these environment variables:")
        print("  EMAIL_ADDRESS=your_email@gmail.com")
        print("  EMAIL_PASSWORD=your_app_password")
        print("  SMTP_SERVER=smtp.gmail.com (optional)")
        print("  SMTP_PORT=587 (optional)")
        print("\nFor Gmail, use an App Password instead of your regular password.")
        print("Generate one at: https://myaccount.google.com/apppasswords")
        return
    
    print("Testing email connection...")
    
    # Test connection
    if test_email_connection():
        print("✅ Email connection successful!")
        
        # Ask for test email
        test_email = input("\nEnter email address to send test email (or press Enter to skip): ").strip()
        
        if test_email:
            print(f"Sending test email to {test_email}...")
            if send_test_email(test_email):
                print("✅ Test email sent successfully!")
                print("\nCheck your inbox for the test email.")
            else:
                print("❌ Failed to send test email.")
        else:
            print("Skipping test email.")
    else:
        print("❌ Email connection failed!")
        print("\nPlease check your email configuration:")
        print("- Verify EMAIL_ADDRESS and EMAIL_PASSWORD are correct")
        print("- For Gmail, make sure you're using an App Password")
        print("- Check that 'Less secure app access' is enabled (if not using App Password)")
        print("- Verify SMTP server and port settings")

if __name__ == "__main__":
    main()