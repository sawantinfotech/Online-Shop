import os
from werkzeug.utils import secure_filename
from flask import current_app
import uuid
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from datetime import datetime
import io

def allowed_file(filename, extensions):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in extensions

def save_uploaded_file(file, subfolder):
    if file and allowed_file(file.filename, ['png', 'jpg', 'jpeg', 'gif', 'pdf']):
        filename = secure_filename(file.filename)
        # Add unique identifier to prevent filename conflicts
        filename = f"{uuid.uuid4()}_{filename}"
        
        # Create subfolder if it doesn't exist
        folder_path = os.path.join(current_app.config['UPLOAD_FOLDER'], subfolder)
        os.makedirs(folder_path, exist_ok=True)
        
        file_path = os.path.join(folder_path, filename)
        file.save(file_path)
        
        return f"{subfolder}/{filename}"
    return None

def calculate_delivery_charges(weight, dimensions, location, delivery_type='standard'):
    """
    Calculate delivery charges based on weight, size, location, and delivery type
    """
    base_charge = 50.0  # Base delivery charge
    
    # Weight-based charges (per kg)
    weight_charge = weight * 10.0 if weight else 0
    
    # Size-based charges
    size_charge = 0
    if dimensions:
        try:
            # Parse dimensions (LxWxH)
            parts = dimensions.split('x')
            if len(parts) == 3:
                volume = float(parts[0]) * float(parts[1]) * float(parts[2])
                if volume > 1000:  # Large item
                    size_charge = 30.0
                elif volume > 500:  # Medium item
                    size_charge = 20.0
        except ValueError:
            pass
    
    # Location-based charges
    location_charge = 0
    if location:
        location_lower = location.lower()
        if 'express' in location_lower or 'premium' in location_lower:
            location_charge = 25.0
        elif 'remote' in location_lower or 'rural' in location_lower:
            location_charge = 40.0
    
    # Delivery type charges
    type_charge = 0
    if delivery_type == 'express':
        type_charge = 50.0
    elif delivery_type == 'scheduled':
        type_charge = 25.0
    
    total_charge = base_charge + weight_charge + size_charge + location_charge + type_charge
    
    return round(total_charge, 2)

def generate_invoice_pdf(order):
    """
    Generate PDF invoice for an order
    """
    # Create filename
    filename = f"invoice_{order.id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], 'invoices', filename)
    
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    
    # Create PDF
    doc = SimpleDocTemplate(filepath, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []
    
    # Title
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        spaceAfter=30,
        textColor=colors.HexColor('#2c3e50')
    )
    story.append(Paragraph("INVOICE", title_style))
    story.append(Spacer(1, 20))
    
    # Business Information
    business_info = f"""
    <b>{order.business.business_name}</b><br/>
    {order.business.address}<br/>
    Phone: {order.business.contact_number}<br/>
    Email: {order.business.email}
    """
    story.append(Paragraph(business_info, styles['Normal']))
    story.append(Spacer(1, 20))
    
    # Invoice Details
    invoice_details = f"""
    <b>Invoice #:</b> {order.id}<br/>
    <b>Date:</b> {order.order_date.strftime('%B %d, %Y')}<br/>
    <b>Customer:</b> {order.customer.name}<br/>
    <b>Phone:</b> {order.customer.phone_number}<br/>
    <b>Delivery Address:</b> {order.delivery_address}
    """
    story.append(Paragraph(invoice_details, styles['Normal']))
    story.append(Spacer(1, 30))
    
    # Order Items Table
    data = [['Product', 'Quantity', 'Price', 'Total']]
    for item in order.order_items:
        data.append([
            item.product.product_name,
            str(item.quantity),
            f"₹{item.price:.2f}",
            f"₹{item.total:.2f}"
        ])
    
    # Add totals
    data.append(['', '', 'Subtotal:', f"₹{order.total_amount:.2f}"])
    data.append(['', '', 'Delivery Charges:', f"₹{order.delivery_charges:.2f}"])
    data.append(['', '', 'Total:', f"₹{order.total_amount + order.delivery_charges:.2f}"])
    
    table = Table(data, colWidths=[3*inch, 1*inch, 1*inch, 1*inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#3498db')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTNAME', (0, -3), (-1, -1), 'Helvetica-Bold'),
        ('BACKGROUND', (0, -1), (-1, -1), colors.HexColor('#e8f4f8')),
    ]))
    
    story.append(table)
    story.append(Spacer(1, 30))
    
    # Payment Information
    payment_info = f"""
    <b>Payment Status:</b> {order.payment_status.title()}<br/>
    <b>Payment Method:</b> {order.payment_method.title() if order.payment_method else 'Not specified'}
    """
    story.append(Paragraph(payment_info, styles['Normal']))
    story.append(Spacer(1, 20))
    
    # Footer
    footer_text = "Thank you for your business!"
    story.append(Paragraph(footer_text, styles['Heading2']))
    
    # Build PDF
    doc.build(story)
    
    return filepath

def format_currency(amount):
    """Format currency for display"""
    return f"₹{amount:.2f}"

def truncate_text(text, max_length=50):
    """Truncate text to specified length"""
    if len(text) <= max_length:
        return text
    return text[:max_length] + "..."

def get_order_status_color(status):
    """Get Bootstrap color class for order status"""
    status_colors = {
        'pending': 'warning',
        'confirmed': 'info',
        'processing': 'primary',
        'shipped': 'success',
        'delivered': 'success',
        'cancelled': 'danger'
    }
    return status_colors.get(status, 'secondary')

def get_payment_status_color(status):
    """Get Bootstrap color class for payment status"""
    status_colors = {
        'pending': 'warning',
        'processing': 'info',
        'completed': 'success',
        'failed': 'danger',
        'refunded': 'secondary'
    }
    return status_colors.get(status, 'secondary')
