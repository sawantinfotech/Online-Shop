# Mobile Shop Management System

## Overview

This is a comprehensive mobile shop management system built with Flask and SQLAlchemy. The application enables business owners to manage their mobile shop operations including product management, customer relationships, order processing, inventory tracking, and payment gateway integrations. It features a web-based interface for business registration, product catalog management, order fulfillment, and customer communication through SMS services.

## System Architecture

### Frontend Architecture
- **Template Engine**: Jinja2 templates with Bootstrap 5 for responsive UI
- **Static Assets**: CSS and JavaScript files for styling and client-side functionality
- **Forms**: FlaskWTF forms for secure form handling and validation
- **Authentication**: Session-based authentication with login/logout functionality

### Backend Architecture
- **Framework**: Flask web framework with Python
- **Database ORM**: SQLAlchemy with support for multiple database backends
- **Session Management**: Flask sessions for user authentication state
- **File Handling**: Werkzeug for secure file uploads and processing
- **Form Validation**: WTForms for server-side form validation

### Database Design
- **Primary Models**: Business, Product, Customer, Order, OrderItem, Payment, Delivery, Category, SMSTemplate
- **Relationships**: One-to-many relationships between Business-Products, Business-Customers, Business-Orders
- **Authentication**: Password hashing using Werkzeug security utilities
- **Document Storage**: JSON field for storing business verification documents

## Key Components

### Business Management
- Business registration with document verification
- Business profile management with logo and business card uploads
- Multi-business support architecture
- Verification status tracking (pending, verified, rejected)

### Product Management
- Product catalog with categories
- Image upload and management
- Inventory tracking with quantity management
- Product search and filtering capabilities
- CSV import/export functionality

### Customer Relationship Management
- Customer profile management
- Contact information storage
- Customer grouping for targeted marketing
- Order history tracking per customer

### Order Processing
- Order creation and management
- Order status tracking (pending, confirmed, processing, shipped, delivered, cancelled)
- Invoice generation with PDF export
- Delivery management with charge calculation

### Payment Integration
- Multiple payment gateway support (GPay, Paytm, Brainlo)
- Payment processing abstraction layer
- Payment status tracking
- Gateway-specific configuration management

### Communication System
- SMS service integration using Twilio
- Automated notifications for order updates
- Template-based SMS messaging
- Customer communication tracking

## Data Flow

1. **Business Registration**: Business owner registers with documents → Verification process → Account activation
2. **Product Management**: Add products → Upload images → Set pricing → Manage inventory
3. **Customer Management**: Add customers → Group customers → Track interactions
4. **Order Processing**: Create order → Process payment → Update status → Send notifications → Generate invoice
5. **Communication**: Template-based SMS → Customer notifications → Order updates

## External Dependencies

### Payment Gateways
- **Google Pay**: Integration for UPI payments
- **Paytm**: Digital wallet and payment processing
- **Brainlo**: Alternative payment solution

### Communication Services
- **Twilio**: SMS service provider for customer notifications
- **Email**: SMTP configuration for email notifications (future implementation)

### File Storage
- **Local Storage**: File uploads stored in `uploads/` directory
- **Image Processing**: Support for JPG, PNG, JPEG, GIF formats
- **Document Storage**: PDF support for business documents

### Frontend Libraries
- **Bootstrap 5**: CSS framework for responsive design
- **Font Awesome**: Icon library for UI elements
- **jQuery**: JavaScript library for DOM manipulation (implied by templates)

## Deployment Strategy

### Environment Configuration
- **Database**: Configurable via `DATABASE_URL` environment variable (defaults to SQLite)
- **Session Secret**: Configurable via `SESSION_SECRET` environment variable
- **Upload Directory**: Configurable upload folder with size limits (16MB max)
- **Payment Gateway Keys**: Environment-based configuration for API keys

### Production Considerations
- **Database**: Production deployment should use PostgreSQL instead of SQLite
- **File Storage**: Consider cloud storage solutions for production file uploads
- **Security**: Implement HTTPS, secure session configuration, and environment-specific secrets
- **Monitoring**: Add logging and monitoring for production deployments

### Scalability
- **Database Connection Pooling**: Configured with pool recycling and pre-ping
- **Static File Serving**: Consider CDN for static assets in production
- **Session Management**: Consider Redis for session storage in multi-instance deployments

## Changelog

```
Changelog:
- July 06, 2025. Initial setup
- July 06, 2025. Added comprehensive admin panel with business verification, system monitoring, and analytics
- July 06, 2025. Implemented working email system with Gmail SMTP integration
- July 06, 2025. Enhanced system with SMS notifications via Twilio
- July 06, 2025. Created complete documentation and testing tools
- July 07, 2025. Migrated to Replit environment with PostgreSQL database integration
- July 07, 2025. Added PostgreSQL database for improved performance and scalability
- July 07, 2025. Implemented complete delivery system with career page, registration, and management
- July 07, 2025. Added password reset functionality for all user types
- July 07, 2025. Enhanced pricing plans with Silver/Gold/Platinum badges
- July 07, 2025. Created comprehensive demo data (15 products, 10 users, 6 delivery partners)
- July 07, 2025. Added delivery partner carousel with live status tracking
- July 07, 2025. Implemented subject-related images and improved UI/UX
- July 15, 2025. Fixed database connection issues with PostgreSQL fallback to SQLite
- July 15, 2025. Added 20 demo businesses and 20 delivery partners for testing
- July 15, 2025. Enhanced navigation with Account dropdown menu featuring separate login options
- July 15, 2025. Created delivery partner login system with dedicated routes
- July 15, 2025. Updated main menu to include Admin, Business, and Delivery login options
- July 15, 2025. Created comprehensive Apps showcase section with 30+ demo apps
- July 15, 2025. Added horizontal scrolling carousel on homepage for featured apps
- July 15, 2025. Implemented detailed app pages with 6 sections (logo, intro, features, author, support, social)
- July 15, 2025. Added special Buddhistan app with chakra logo and public services integration
- July 15, 2025. Created Mobile Shop Hub app entry with SEO functionality for admin
- July 15, 2025. Enhanced social sharing to include Buddhistan platform option
- July 15, 2025. Built multi-step app registration system for developers
- July 15, 2025. Added comprehensive matrimony platform with profile management
- July 15, 2025. Implemented swipe functionality and premium membership tiers
- July 15, 2025. Created complete database schema for all specialized apps
- July 15, 2025. Generated comprehensive final project report with deployment guide
- July 17, 2025. **MIGRATION COMPLETED**: Successfully migrated from Replit Agent to standard Replit environment
- July 17, 2025. Enhanced matrimonial system with multi-step registration (4 steps)
- July 17, 2025. Added comprehensive profile carousel with 5 photos per member and photo navigation
- July 17, 2025. Implemented follow/share functionality for matrimonial profiles  
- July 17, 2025. Created 17 diverse demo profiles (10 girls, 10 boys, 5 widowed women, 5 divorced men)
- July 17, 2025. Added relationship types: marriage, open relationship, live-in relationship
- July 17, 2025. Implemented photo blur feature for basic members after 10 days validity
- July 17, 2025. Created 15 comprehensive admin sections for super admin control
- July 17, 2025. Enhanced security with proper client/server separation and robust practices
- July 17, 2025. **DATABASE UPGRADE**: Added PostgreSQL database for production-ready performance
- July 17, 2025. **COMPREHENSIVE TESTING**: Completed full system testing and created final deployment report
- July 17, 2025. **PRODUCTION READY**: All features working, 17 matrimonial profiles, 15 admin sections active
- July 18, 2025. **REPLIT MIGRATION COMPLETED**: Successfully migrated from Replit Agent to standard Replit environment
- July 18, 2025. **SUBSCRIBER SYSTEM ADDED**: New unified subscriber login/signup system with category-based registration
- July 18, 2025. **PRICING PLANS CREATED**: 32 pricing plans across 8 categories (Free, Silver, Gold, Platinum)
- July 18, 2025. **PAYMENT SYSTEM INTEGRATED**: Complete payment processing with status tracking and notifications
- July 18, 2025. **POSTGRESQL INTEGRATION**: Database upgraded to PostgreSQL for production performance
- July 19, 2025. **PRODUCTION MIGRATION**: Successfully migrated from Replit Agent to standard Replit environment
- July 19, 2025. **AUTOMATIC DEMO DATA**: Implemented permanent demo data auto-population system
- July 19, 2025. **SCHEMA OPTIMIZATION**: Fixed all database schema issues and template rendering errors
- July 19, 2025. **SECURITY ENHANCEMENT**: Enhanced client/server separation with robust security practices
- July 19, 2025. **DEPLOYMENT READY**: All systems working with PostgreSQL database and comprehensive demo data
```

## User Preferences

```
Preferred communication style: Simple, everyday language.
```