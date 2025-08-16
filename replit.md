# Online Shop Management System

## Overview
This project is a comprehensive multi-service business management platform built with Flask, designed to be a central hub for various professional services. It offers a unified interface for businesses across sectors like mobile shops, matrimony, and healthcare to manage operations, including user authentication, business registration, product management, payment processing, and administrative controls. The system aims to foster local business growth and enhance customer interaction.

## User Preferences
Preferred communication style: Simple, everyday language.

## Recent Changes (August 2025)
- **Product Add Form Fixed (August 13, 2025)**: Fixed product addition form to default to 'active' status instead of 'draft', ensuring newly added products appear immediately on all pages (home, product listing, details). Updated form defaults and database handling.
- **Product Service Dashboard Integration (August 13, 2025)**: Added complete Product Service section to subscriber dashboard with product statistics, quick actions, and detailed product management table showing status, views, stock levels.
- **Product Service Working - Database Fixed (August 13, 2025)**: Fixed product display issues across all pages by updating draft products to active status, creating product categories, and ensuring proper database relationships. All product routes working with products showing on home, product home, all products, and detail pages.
- **Product Service Complete Fix (August 13, 2025)**: Fixed all template errors, route imports, featured products display on all home pages, product view pages working without 500 errors, and Product service fully integrated with subscriber dashboard
- **Migration to Standard Replit Completed (August 13, 2025)**: Successfully migrated project from Replit Agent to standard Replit environment, fixed all template URLs, form field mismatches, and routing issues
- **Product Service Template Fixes (August 13, 2025)**: Fixed all Product service template URL routing and form field name conflicts
- **Product Service Implementation (August 13, 2025)**: Created complete Product service with full isolation following Business service pattern
- **Migration Completed (August 12, 2025)**: Successfully migrated from Replit Agent to standard Replit environment with full PostgreSQL integration
- **Business Service Disconnection (August 12, 2025)**: Systematically disconnected all Business service components while preserving files in business folder for future use
- **Code Cleanup (August 12, 2025)**: Reduced LSP errors from 137 to near zero by removing business dependencies from main application
- **August 12, 2025**: Fixed critical database schema issues, app registration form errors, routing problems, and improved app card spacing
- **Route Import Fixes (August 12, 2025)**: Fixed app registration and app detail route import errors by removing business-dependent model imports
- **Database Setup**: Created and configured PostgreSQL database with proper environment variables
- **Package Installation**: Installed all required dependencies including gunicorn for production deployment
- **Security Enhancements**: Implemented proper client/server separation and robust security practices
- **Template Fixes**: Resolved URL routing issues for better user navigation
- **Enhanced App Carousel**: Added missing buttons (View, Download, Follow, Share) to featured apps carousel
- **App Detail Page**: Created comprehensive app detail page with full functionality
- **Admin Login Fixed**: Resolved 404 errors and missing route issues for admin functionality
- **Database Schema**: Fixed database compatibility issues and recreated proper schema
- **Interactive Features**: Implemented app download tracking, developer following, and app sharing
- **Service Registration System**: Verified and improved service registration functionality for subscribers
- **Code Quality**: Fixed LSP diagnostics and duplicate method issues in models

## KEY POINT CONCEPT - CORE ARCHITECTURE (NEVER CHANGE)

**This is the fundamental architectural pattern that must be followed for ALL services forever:**

1. **User/Subscriber Routes**: Only in main.py, forms.py, models.py
2. **Individual Services**: Each service has TWO folders:
   - One HTML templates folder (e.g., `templates/product/`)  
   - One Python code folder (e.g., `product/`)
3. **Service Route Generation**: Each service generates routes ONLY in its own Python folder, NOT in main files
4. **Public Home Page**: Common page for all services, connects to main.py
5. **Service Home Pages**: Every service has its own `service_home` page and folders
6. **Subscriber Dashboard**: Has individual sections for each service
7. **Admin/Super Admin**: Separate routing system
8. **Route Isolation**: Routes/functions for each service generate ONLY in its own folder (html & py)

**This prevents routing conflicts between services and ensures clean separation.**

## System Architecture

### Backend Architecture
- **Framework**: Flask (Python web framework).
- **Database ORM**: SQLAlchemy, supporting both SQLite (development) and PostgreSQL (production).
- **Session Management**: Flask session-based authentication with distinct user types (businesses, customers, admins).
- **File Upload**: Werkzeug for secure file handling and organized uploads.
- **Email Service**: SMTP integration, including Gmail support, for template-based notifications.
- **SMS Service**: Twilio integration with a fallback simulation for demo purposes.

### Database Design
- **Multi-tenant Structure**: Separate models for different service types (Business, User, DeliveryProfile, MatrimonyProfile, App).
- **Relationship Management**: Foreign key relationships linking businesses, products, customers, and orders.
- **Document Storage**: JSON-based storage for business verification file URLs.
- **Flexible Schema**: Designed to support multiple business types and service categories.

### Authentication & Authorization
- **Multi-level Access**: Distinct login systems for customers, businesses, and administrators.
- **Password Security**: Werkzeug for secure password hashing with salt generation.
- **Session-based Auth**: Flask session management with role-based access control.
- **Password Recovery**: Email-based functionality for password resets.

### Payment Integration
- **Multiple Gateways**: Support for GPay, Paytm, and Brainlo payment systems.
- **Transaction Tracking**: Comprehensive management of payment history and status.
- **Invoice Generation**: Automated PDF invoice creation using ReportLab.

### Communication Systems
- **Email Templates**: Automated email notifications for orders, payments, and account updates.
- **SMS Notifications**: Updates on order status and promotional messages.
- **Template Management**: Customizable message templates for diverse business needs.

### Frontend Architecture
- **Responsive Design**: Bootstrap 5 with a mobile-first approach.
- **Multi-service Interface**: Dedicated home pages for each service type (e.g., apps, matrimony, hospital).
- **Dynamic Content**: JavaScript for enhanced user interactions and form validation.
- **Service-specific Styling**: Custom CSS tailored for different service categories.

### File Management
- **Organized Storage**: Directories segmented by file type (e.g., business documents, product images, user profiles).
- **Security**: Validation of file types and secure filename handling.
- **Scalability**: Designed to support migration to cloud storage.

### Core System Features
- **Comprehensive Service Directory**: Expanded to 50+ services with organized categories and dedicated home pages.
- **Service Management System**: Includes subscriber and admin functionalities, service registration, approval workflows, and detailed service tracking.
- **Admin Panel Enhancement**: Unified admin routes, user management, detailed service analytics, and new sections for customers, plans, accounts, offers, SMS, Email, notifications, office, and contact management.
- **App Service Implementation**: Full marketplace system with app registration, filtering, search, dynamic display, and integration with existing models.
- **Product Service Implementation**: Complete isolated product management system with categories, reviews, favorites, inventory tracking, and advanced search capabilities.

## External Dependencies

### Core Framework Dependencies
- **Flask**: Web application framework.
- **SQLAlchemy**: Database ORM.
- **Werkzeug**: WSGI utilities and security.
- **WTForms**: Form handling and validation.

### Payment Gateways
- **GPay**: Google Pay.
- **Paytm**: Indian digital wallet and payment system.
- **Brainlo**: Custom payment processing solution.

### Communication Services
- **Twilio**: SMS messaging service.
- **SMTP**: For email delivery.

### Frontend Libraries
- **Bootstrap 5**: CSS framework.
- **Font Awesome**: Icon library.
- **JavaScript**: For client-side interactions.

### Development Tools
- **ReportLab**: For PDF generation.

### Database Support
- **PostgreSQL**: Production database.
- **SQLite**: Development database.