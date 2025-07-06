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
```

## User Preferences

```
Preferred communication style: Simple, everyday language.
```