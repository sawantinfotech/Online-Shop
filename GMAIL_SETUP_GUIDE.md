# Gmail App Password Setup Guide

## Current Issue
Your email system shows:
- ✅ Email Address: sawantinfotech@gmail.com
- ❌ Password: Only 11 characters (App Password needs 16)
- ❌ Authentication: Failed - requires App Password

## Step-by-Step Solution

### Step 1: Enable 2-Step Verification
1. Go to [myaccount.google.com](https://myaccount.google.com)
2. Click **Security** in the left sidebar
3. Under "Signing in to Google", click **2-Step Verification**
4. Follow the setup process (usually requires phone verification)

### Step 2: Generate App Password
1. After 2-Step Verification is enabled, go to [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
2. Sign in with sawantinfotech@gmail.com
3. Select **Mail** from the "Select app" dropdown
4. Click **Generate**
5. Copy the 16-character password (format: "abcd efgh ijkl mnop")

### Step 3: Update in Replit
1. In Replit, click the **lock icon** (🔒) in the left sidebar
2. Find **EMAIL_PASSWORD** in the secrets list
3. Click on it to edit
4. Replace with the 16-character App Password
5. Click **Save**

### Step 4: Test Email System
After updating, the system will automatically:
- Send order confirmations
- Send payment receipts
- Send delivery updates
- Send business notifications

## Alternative: Use Different Email Provider

If Gmail setup is complex, you can use other providers:

### Option 1: Outlook/Hotmail
```
EMAIL_ADDRESS=your_email@outlook.com
EMAIL_PASSWORD=your_regular_password
SMTP_SERVER=smtp-mail.outlook.com
SMTP_PORT=587
```

### Option 2: Yahoo Mail
```
EMAIL_ADDRESS=your_email@yahoo.com
EMAIL_PASSWORD=your_app_password
SMTP_SERVER=smtp.mail.yahoo.com
SMTP_PORT=587
```

## Email System Features Ready
Once configured, your customers will receive:
- Professional order confirmations
- Payment receipts
- Shipping notifications
- Invoice PDFs
- Business updates

The entire email system is built and ready - just needs the correct authentication.