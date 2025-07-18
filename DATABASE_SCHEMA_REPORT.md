# Mobile Shop Management System - Database Schema Report

## Database Information
- **Database Name**: neondb (PostgreSQL)
- **Schema**: public
- **Total Tables**: 19
- **Database Type**: PostgreSQL with full ACID compliance

## Complete Table Structure

### 1. **businesses** (Core Business Entity)
Primary table for storing business information and profiles.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | integer | PRIMARY KEY, AUTO INCREMENT | Unique business identifier |
| business_name | varchar(200) | NOT NULL | Business display name |
| logo_url | varchar(500) | NULLABLE | URL to business logo image |
| license_number | varchar(100) | NULLABLE | Business registration/license number |
| contact_number | varchar(15) | NOT NULL | Primary contact phone number |
| email | varchar(120) | NOT NULL, UNIQUE | Business email address |
| address | text | NULLABLE | Physical business address |
| business_type | varchar(100) | NULLABLE | Type of business (retail, wholesale, etc.) |
| verification_status | varchar(20) | DEFAULT 'pending' | Admin verification status |
| documents | text | NULLABLE | JSON array of uploaded document URLs |
| gpay_enabled | boolean | DEFAULT false | Google Pay integration status |
| paytm_enabled | boolean | DEFAULT false | Paytm payment integration status |
| brainlo_enabled | boolean | DEFAULT false | Brainlo payment integration status |
| password_hash | varchar(256) | NULLABLE | Encrypted password for business login |
| created_at | timestamp | DEFAULT now() | Account creation timestamp |
| updated_at | timestamp | DEFAULT now() | Last update timestamp |

### 2. **users** (Enhanced User Management)
Extended user system with social features and role management.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | integer | PRIMARY KEY, AUTO INCREMENT | Unique user identifier |
| username | varchar(80) | NOT NULL, UNIQUE | Unique username |
| email | varchar(120) | NOT NULL, UNIQUE | User email address |
| password_hash | varchar(256) | NULLABLE | Encrypted password |
| full_name | varchar(200) | NULLABLE | User's full name |
| profile_photo | varchar(500) | NULLABLE | Profile picture URL |
| phone_number | varchar(15) | NULLABLE | Contact phone number |
| address | text | NULLABLE | User address |
| is_online | boolean | DEFAULT false | Current online status |
| last_seen | timestamp | DEFAULT now() | Last activity timestamp |
| role | varchar(20) | DEFAULT 'user' | User role (user, manager, admin, super_admin) |
| business_id | integer | FOREIGN KEY → businesses.id | Associated business (if any) |
| credit_points | integer | DEFAULT 0 | Brainlo credit points balance |
| subscription_plan | varchar(50) | DEFAULT 'free' | Current subscription plan |
| custom_homepage | boolean | DEFAULT false | Custom homepage enabled flag |
| created_at | timestamp | DEFAULT now() | Registration timestamp |
| updated_at | timestamp | DEFAULT now() | Last update timestamp |

### 3. **categories** (Product Classification)
Product categorization system for better organization.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | integer | PRIMARY KEY, AUTO INCREMENT | Category identifier |
| name | varchar(100) | NOT NULL | Category name |
| description | text | NULLABLE | Category description |
| created_at | timestamp | DEFAULT now() | Creation timestamp |

### 4. **products** (Product Catalog)
Complete product information with inventory management.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | integer | PRIMARY KEY, AUTO INCREMENT | Product identifier |
| business_id | integer | NOT NULL, FOREIGN KEY → businesses.id | Owning business |
| category_id | integer | FOREIGN KEY → categories.id | Product category |
| product_name | varchar(200) | NOT NULL | Product title |
| description | text | NULLABLE | Product description |
| price | double precision | NOT NULL | Product price |
| quantity | integer | DEFAULT 0 | Available stock quantity |
| images | text | NULLABLE | JSON array of product image URLs |
| weight | double precision | NULLABLE | Product weight in kg |
| dimensions | varchar(100) | NULLABLE | Product dimensions (LxWxH) |
| is_active | boolean | DEFAULT true | Product visibility status |
| created_at | timestamp | DEFAULT now() | Product creation timestamp |
| updated_at | timestamp | DEFAULT now() | Last update timestamp |

### 5. **customers** (Customer Management)
Customer relationship management with grouping capabilities.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | integer | PRIMARY KEY, AUTO INCREMENT | Customer identifier |
| business_id | integer | NOT NULL, FOREIGN KEY → businesses.id | Associated business |
| name | varchar(200) | NOT NULL | Customer name |
| phone_number | varchar(15) | NOT NULL | Contact number |
| email | varchar(120) | NULLABLE | Email address |
| address | text | NULLABLE | Customer address |
| social_media | text | NULLABLE | JSON social media profiles |
| groups | text | NULLABLE | JSON customer group memberships |
| created_at | timestamp | DEFAULT now() | Registration timestamp |
| updated_at | timestamp | DEFAULT now() | Last update timestamp |

### 6. **orders** (Order Management)
Complete order processing with status tracking.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | integer | PRIMARY KEY, AUTO INCREMENT | Order identifier |
| business_id | integer | NOT NULL, FOREIGN KEY → businesses.id | Processing business |
| customer_id | integer | NOT NULL, FOREIGN KEY → customers.id | Ordering customer |
| order_status | varchar(20) | DEFAULT 'pending' | Order processing status |
| total_amount | double precision | NOT NULL | Total order value |
| delivery_charges | double precision | DEFAULT 0.0 | Delivery cost |
| payment_status | varchar(20) | DEFAULT 'pending' | Payment processing status |
| payment_method | varchar(20) | NULLABLE | Selected payment method |
| delivery_address | text | NULLABLE | Shipping address |
| order_date | timestamp | DEFAULT now() | Order placement timestamp |
| delivery_date | timestamp | NULLABLE | Scheduled/actual delivery |
| invoice_url | varchar(500) | NULLABLE | Generated invoice PDF URL |
| created_at | timestamp | DEFAULT now() | Record creation timestamp |
| updated_at | timestamp | DEFAULT now() | Last update timestamp |

### 7. **order_items** (Order Line Items)
Individual products within orders.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | integer | PRIMARY KEY, AUTO INCREMENT | Line item identifier |
| order_id | integer | NOT NULL, FOREIGN KEY → orders.id | Parent order |
| product_id | integer | NOT NULL, FOREIGN KEY → products.id | Ordered product |
| quantity | integer | NOT NULL | Quantity ordered |
| price | double precision | NOT NULL | Unit price at time of order |
| total | double precision | NOT NULL | Line total (quantity × price) |

### 8. **payments** (Payment Processing)
Payment transaction records with gateway integration.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | integer | PRIMARY KEY, AUTO INCREMENT | Payment identifier |
| order_id | integer | NOT NULL, FOREIGN KEY → orders.id | Associated order |
| amount | double precision | NOT NULL | Payment amount |
| payment_method | varchar(20) | NOT NULL | Payment gateway used |
| transaction_id | varchar(100) | NULLABLE | Gateway transaction ID |
| status | varchar(20) | DEFAULT 'pending' | Payment status |
| gateway_response | text | NULLABLE | Gateway response data |
| created_at | timestamp | DEFAULT now() | Payment timestamp |

### 9. **deliveries** (Delivery Management)
Shipping and delivery tracking information.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | integer | PRIMARY KEY, AUTO INCREMENT | Delivery identifier |
| order_id | integer | NOT NULL, FOREIGN KEY → orders.id | Associated order |
| delivery_type | varchar(20) | DEFAULT 'standard' | Delivery service type |
| charges | double precision | NOT NULL | Delivery cost |
| estimated_time | timestamp | NULLABLE | Estimated delivery time |
| actual_time | timestamp | NULLABLE | Actual delivery time |
| status | varchar(20) | DEFAULT 'pending' | Delivery status |
| tracking_number | varchar(100) | NULLABLE | Tracking reference |
| created_at | timestamp | DEFAULT now() | Record creation timestamp |

### 10. **sms_templates** (SMS Communication)
Template-based SMS messaging system.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | integer | PRIMARY KEY, AUTO INCREMENT | Template identifier |
| business_id | integer | NOT NULL, FOREIGN KEY → businesses.id | Template owner |
| template_name | varchar(100) | NOT NULL | Template name |
| template_content | text | NOT NULL | SMS message template |
| template_type | varchar(50) | NULLABLE | Template category |
| is_active | boolean | DEFAULT true | Template active status |
| created_at | timestamp | DEFAULT now() | Creation timestamp |

## Enhanced Social & Business Features

### 11. **follows** (Social Following System)
User-to-user following relationships.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | integer | PRIMARY KEY, AUTO INCREMENT | Relationship identifier |
| follower_id | integer | NOT NULL, FOREIGN KEY → users.id | User who follows |
| followed_id | integer | NOT NULL, FOREIGN KEY → users.id | User being followed |
| created_at | timestamp | DEFAULT now() | Follow timestamp |

### 12. **likes** (Like System)
Universal liking system for products and businesses.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | integer | PRIMARY KEY, AUTO INCREMENT | Like identifier |
| user_id | integer | NOT NULL, FOREIGN KEY → users.id | User who liked |
| target_type | varchar(20) | NOT NULL | Type (product/business) |
| target_id | integer | NOT NULL | Target entity ID |
| created_at | timestamp | DEFAULT now() | Like timestamp |

### 13. **comments** (Comment System)
Comment system for products and businesses.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | integer | PRIMARY KEY, AUTO INCREMENT | Comment identifier |
| user_id | integer | NOT NULL, FOREIGN KEY → users.id | Comment author |
| target_type | varchar(20) | NOT NULL | Type (product/business) |
| target_id | integer | NOT NULL | Target entity ID |
| content | text | NOT NULL | Comment content |
| created_at | timestamp | DEFAULT now() | Comment timestamp |

### 14. **reviews** (Review & Rating System)
Star rating and review system.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | integer | PRIMARY KEY, AUTO INCREMENT | Review identifier |
| user_id | integer | NOT NULL, FOREIGN KEY → users.id | Reviewer |
| target_type | varchar(20) | NOT NULL | Type (product/business) |
| target_id | integer | NOT NULL | Target entity ID |
| rating | integer | NOT NULL | Star rating (1-5) |
| review_text | text | NULLABLE | Review content |
| created_at | timestamp | DEFAULT now() | Review timestamp |

### 15. **favorites** (Favorites System)
User favorites for products and businesses.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | integer | PRIMARY KEY, AUTO INCREMENT | Favorite identifier |
| user_id | integer | NOT NULL, FOREIGN KEY → users.id | User |
| target_type | varchar(20) | NOT NULL | Type (product/business) |
| target_id | integer | NOT NULL | Target entity ID |
| created_at | timestamp | DEFAULT now() | Favorite timestamp |

## Business Features

### 16. **advertisements** (Advertisement System)
Business advertising and promotion management.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | integer | PRIMARY KEY, AUTO INCREMENT | Advertisement identifier |
| business_id | integer | NOT NULL, FOREIGN KEY → businesses.id | Advertising business |
| title | varchar(200) | NOT NULL | Advertisement title |
| content | text | NULLABLE | Advertisement content |
| media_url | varchar(500) | NULLABLE | Image/video URL |
| media_type | varchar(20) | NULLABLE | Media type (image/video) |
| duration | integer | DEFAULT 5 | Video duration (seconds) |
| target_audience | text | NULLABLE | JSON targeting criteria |
| status | varchar(20) | DEFAULT 'pending' | Approval status |
| start_date | timestamp | NULLABLE | Campaign start date |
| end_date | timestamp | NULLABLE | Campaign end date |
| budget | double precision | DEFAULT 0.0 | Advertisement budget |
| impressions | integer | DEFAULT 0 | View count |
| clicks | integer | DEFAULT 0 | Click count |
| created_at | timestamp | DEFAULT now() | Creation timestamp |

### 17. **pricing_plans** (Subscription Plans)
Service tier management for businesses.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | integer | PRIMARY KEY, AUTO INCREMENT | Plan identifier |
| name | varchar(100) | NOT NULL | Plan name |
| description | text | NULLABLE | Plan description |
| price | double precision | NOT NULL | Plan cost |
| billing_cycle | varchar(20) | NULLABLE | Billing frequency |
| features | text | NULLABLE | JSON feature list |
| max_products | integer | DEFAULT -1 | Product limit (-1 = unlimited) |
| max_orders | integer | DEFAULT -1 | Order limit (-1 = unlimited) |
| max_customers | integer | DEFAULT -1 | Customer limit (-1 = unlimited) |
| custom_homepage | boolean | DEFAULT false | Custom homepage access |
| advanced_analytics | boolean | DEFAULT false | Advanced analytics access |
| priority_support | boolean | DEFAULT false | Priority support access |
| is_active | boolean | DEFAULT true | Plan availability |
| created_at | timestamp | DEFAULT now() | Creation timestamp |

### 18. **user_subscriptions** (Subscription Management)
User subscription tracking and billing.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | integer | PRIMARY KEY, AUTO INCREMENT | Subscription identifier |
| user_id | integer | NOT NULL, FOREIGN KEY → users.id | Subscribed user |
| plan_id | integer | NOT NULL, FOREIGN KEY → pricing_plans.id | Selected plan |
| start_date | timestamp | DEFAULT now() | Subscription start |
| end_date | timestamp | NULLABLE | Subscription expiry |
| status | varchar(20) | DEFAULT 'active' | Subscription status |
| payment_method | varchar(50) | NULLABLE | Payment method used |
| transaction_id | varchar(100) | NULLABLE | Payment transaction ID |
| created_at | timestamp | DEFAULT now() | Creation timestamp |

### 19. **business_managers** (Business Management)
Manager role assignments for businesses.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | integer | PRIMARY KEY, AUTO INCREMENT | Assignment identifier |
| business_id | integer | NOT NULL, FOREIGN KEY → businesses.id | Managed business |
| user_id | integer | NOT NULL, FOREIGN KEY → users.id | Manager user |
| role | varchar(50) | DEFAULT 'manager' | Management role level |
| permissions | text | NULLABLE | JSON permission array |
| status | varchar(20) | DEFAULT 'active' | Assignment status |
| assigned_by | integer | FOREIGN KEY → users.id | Assigning user |
| created_at | timestamp | DEFAULT now() | Assignment timestamp |

## Database Relationships

### Primary Relationships
- **businesses** → **products** (1:Many) - Business owns multiple products
- **businesses** → **customers** (1:Many) - Business has multiple customers  
- **businesses** → **orders** (1:Many) - Business processes multiple orders
- **orders** → **order_items** (1:Many) - Order contains multiple items
- **orders** → **payments** (1:Many) - Order can have multiple payments
- **orders** → **deliveries** (1:Many) - Order can have multiple delivery attempts

### Enhanced Feature Relationships
- **users** → **reviews** (1:Many) - User can write multiple reviews
- **users** → **likes** (1:Many) - User can like multiple items
- **users** → **comments** (1:Many) - User can comment multiple times
- **users** → **follows** (Many:Many) - Users can follow each other
- **users** → **favorites** (1:Many) - User can favorite multiple items

### Business Feature Relationships
- **businesses** → **advertisements** (1:Many) - Business can run multiple ads
- **users** → **user_subscriptions** (1:Many) - User can have multiple subscriptions
- **pricing_plans** → **user_subscriptions** (1:Many) - Plan can have multiple subscribers
- **businesses** → **business_managers** (1:Many) - Business can have multiple managers

## Admin Credentials
- **Regular Admin**: username: `admin`, password: `admin123`
- **Super Admin**: username: `superadmin`, password: `super123`
- **Admin Panel URL**: `/admin/login`

## Key Features Implemented

### Core Business Features
✅ Business registration and verification
✅ Product catalog management
✅ Customer relationship management
✅ Order processing and tracking
✅ Payment gateway integration (GPay, Paytm, Brainlo)
✅ SMS notifications via Twilio
✅ Email system with Gmail SMTP
✅ Invoice generation (PDF)

### Enhanced Social Features
✅ User registration and profiles
✅ Follow/unfollow system
✅ Like/dislike functionality
✅ Comment system
✅ Review and rating system
✅ Favorites system
✅ Online/offline status tracking

### Business Management Features
✅ Advertisement management
✅ Pricing plans and subscriptions
✅ Business manager roles
✅ Custom homepages for businesses
✅ Credit points system (Brainlo integration)

### Admin Features
✅ Business verification workflow
✅ System monitoring dashboard
✅ Category management
✅ Order tracking across all businesses
✅ Revenue analytics and reporting
✅ System configuration management

### Public Features
✅ Public product catalog with search/filter
✅ Business directory
✅ Social sharing (WhatsApp, Facebook, Twitter)
✅ Grid/list view toggle
✅ Category filtering
✅ Price range filtering
✅ Location-based filtering
✅ User carousel with online status
✅ Featured products and businesses
✅ Testimonials and reviews display
✅ Pricing plans showcase

## Security Features
- Password hashing with Werkzeug
- Session-based authentication
- Admin role separation
- Business data isolation
- Secure file upload handling
- SQL injection prevention via ORM
- XSS protection through template escaping

## Integration Status
- ✅ PostgreSQL Database (Fully Operational)
- ✅ Email System (Gmail SMTP Configured)
- ✅ SMS System (Twilio Integration Ready)
- ✅ Payment Gateways (GPay, Paytm, Brainlo Ready)
- ✅ File Upload System (16MB Limit, Multiple Formats)
- ✅ PDF Generation (Invoice System)

This database schema supports a complete mobile shop management ecosystem with social features, business management tools, advertising capabilities, subscription management, and comprehensive admin controls.