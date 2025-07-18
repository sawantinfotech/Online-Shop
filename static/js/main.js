// Mobile Shop Management System - Main JavaScript

// Global variables
let currentUser = null;
let notifications = [];

// Document ready
document.addEventListener('DOMContentLoaded', function() {
    initializeApp();
    setupEventListeners();
    loadNotifications();
});

// Initialize application
function initializeApp() {
    // Initialize tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function(tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Initialize popovers
    var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    var popoverList = popoverTriggerList.map(function(popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl);
    });

    // Auto-hide alerts after 5 seconds
    setTimeout(function() {
        const alerts = document.querySelectorAll('.alert');
        alerts.forEach(function(alert) {
            if (alert.classList.contains('fade')) {
                new bootstrap.Alert(alert).close();
            }
        });
    }, 5000);
}

// Setup event listeners
function setupEventListeners() {
    // Form validation
    setupFormValidation();
    
    // File upload handlers
    setupFileUpload();
    
    // Search functionality
    setupSearch();
    
    // Confirmation dialogs
    setupConfirmationDialogs();
    
    // Auto-refresh for orders page
    setupAutoRefresh();
}

// Form validation
function setupFormValidation() {
    const forms = document.querySelectorAll('form');
    forms.forEach(function(form) {
        form.addEventListener('submit', function(event) {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        });
    });
}

// File upload handling
function setupFileUpload() {
    const fileInputs = document.querySelectorAll('input[type="file"]');
    fileInputs.forEach(function(input) {
        input.addEventListener('change', function(event) {
            const file = event.target.files[0];
            if (file) {
                validateFile(file, input);
                previewFile(file, input);
            }
        });
    });
}

// File validation
function validateFile(file, input) {
    const maxSize = 5 * 1024 * 1024; // 5MB
    const allowedTypes = ['image/jpeg', 'image/png', 'image/gif', 'application/pdf'];
    
    if (file.size > maxSize) {
        showAlert('File size must be less than 5MB', 'error');
        input.value = '';
        return false;
    }
    
    if (!allowedTypes.includes(file.type)) {
        showAlert('Only JPEG, PNG, GIF, and PDF files are allowed', 'error');
        input.value = '';
        return false;
    }
    
    return true;
}

// File preview
function previewFile(file, input) {
    if (file.type.startsWith('image/')) {
        const reader = new FileReader();
        reader.onload = function(e) {
            const previewId = input.id + '_preview';
            let preview = document.getElementById(previewId);
            
            if (!preview) {
                preview = document.createElement('img');
                preview.id = previewId;
                preview.className = 'img-thumbnail mt-2';
                preview.style.maxWidth = '200px';
                preview.style.maxHeight = '200px';
                input.parentNode.appendChild(preview);
            }
            
            preview.src = e.target.result;
        };
        reader.readAsDataURL(file);
    }
}

// Search functionality
function setupSearch() {
    const searchInputs = document.querySelectorAll('input[name="search"]');
    searchInputs.forEach(function(input) {
        let timeout;
        input.addEventListener('input', function() {
            clearTimeout(timeout);
            timeout = setTimeout(function() {
                // Auto-submit search after 500ms delay
                const form = input.closest('form');
                if (form) {
                    form.submit();
                }
            }, 500);
        });
    });
}

// Confirmation dialogs
function setupConfirmationDialogs() {
    const deleteButtons = document.querySelectorAll('button[type="submit"], form[onsubmit*="confirm"]');
    deleteButtons.forEach(function(button) {
        const form = button.closest('form');
        if (form && form.action.includes('delete')) {
            button.addEventListener('click', function(event) {
                if (!confirm('Are you sure you want to delete this item?')) {
                    event.preventDefault();
                }
            });
        }
    });
}

// Auto-refresh for orders page
function setupAutoRefresh() {
    if (window.location.pathname.includes('/orders')) {
        setInterval(function() {
            // Refresh page every 5 minutes
            location.reload();
        }, 300000);
    }
}

// Utility functions
function showAlert(message, type = 'info') {
    const alertContainer = document.getElementById('alert-container') || createAlertContainer();
    const alertId = 'alert-' + Date.now();
    
    const alertHTML = `
        <div id="${alertId}" class="alert alert-${type} alert-dismissible fade show" role="alert">
            ${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        </div>
    `;
    
    alertContainer.insertAdjacentHTML('beforeend', alertHTML);
    
    // Auto-hide after 5 seconds
    setTimeout(function() {
        const alert = document.getElementById(alertId);
        if (alert) {
            new bootstrap.Alert(alert).close();
        }
    }, 5000);
}

function createAlertContainer() {
    const container = document.createElement('div');
    container.id = 'alert-container';
    container.className = 'position-fixed top-0 end-0 p-3';
    container.style.zIndex = '9999';
    document.body.appendChild(container);
    return container;
}

// Load notifications
function loadNotifications() {
    // Placeholder for notification loading
    // In a real app, this would fetch from an API
    notifications = [
        {
            id: 1,
            type: 'order',
            message: 'New order received',
            timestamp: new Date(),
            read: false
        }
    ];
}

// Format currency
function formatCurrency(amount) {
    return new Intl.NumberFormat('en-IN', {
        style: 'currency',
        currency: 'INR'
    }).format(amount);
}

// Format date
function formatDate(date, format = 'dd/mm/yyyy') {
    const d = new Date(date);
    const day = String(d.getDate()).padStart(2, '0');
    const month = String(d.getMonth() + 1).padStart(2, '0');
    const year = d.getFullYear();
    
    switch (format) {
        case 'dd/mm/yyyy':
            return `${day}/${month}/${year}`;
        case 'mm/dd/yyyy':
            return `${month}/${day}/${year}`;
        case 'yyyy-mm-dd':
            return `${year}-${month}-${day}`;
        default:
            return d.toLocaleDateString();
    }
}

// Delivery charge calculator
function calculateDeliveryCharges(weight, dimensions, location, deliveryType) {
    let baseCharge = 50.0;
    let weightCharge = weight * 10.0;
    let sizeCharge = 0;
    let locationCharge = 0;
    let typeCharge = 0;
    
    // Size-based charges
    if (dimensions) {
        const parts = dimensions.split('x');
        if (parts.length === 3) {
            const volume = parseFloat(parts[0]) * parseFloat(parts[1]) * parseFloat(parts[2]);
            if (volume > 1000) {
                sizeCharge = 30.0;
            } else if (volume > 500) {
                sizeCharge = 20.0;
            }
        }
    }
    
    // Location-based charges
    if (location) {
        const locationLower = location.toLowerCase();
        if (locationLower.includes('express') || locationLower.includes('premium')) {
            locationCharge = 25.0;
        } else if (locationLower.includes('remote') || locationLower.includes('rural')) {
            locationCharge = 40.0;
        }
    }
    
    // Delivery type charges
    switch (deliveryType) {
        case 'express':
            typeCharge = 50.0;
            break;
        case 'scheduled':
            typeCharge = 25.0;
            break;
        default:
            typeCharge = 0;
    }
    
    return Math.round((baseCharge + weightCharge + sizeCharge + locationCharge + typeCharge) * 100) / 100;
}

// SMS functionality
function sendSMS(phoneNumber, message) {
    return fetch('/api/sms/send', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            phone_number: phoneNumber,
            message: message
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            showAlert('SMS sent successfully!', 'success');
        } else {
            showAlert('Failed to send SMS: ' + data.error, 'error');
        }
        return data;
    })
    .catch(error => {
        showAlert('Error sending SMS: ' + error.message, 'error');
        throw error;
    });
}

// Payment processing
function processPayment(amount, paymentMethod, customerInfo) {
    return fetch('/api/process_payment', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            amount: amount,
            payment_method: paymentMethod,
            customer_info: customerInfo
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            showAlert('Payment processed successfully!', 'success');
        } else {
            showAlert('Payment failed: ' + data.error, 'error');
        }
        return data;
    })
    .catch(error => {
        showAlert('Error processing payment: ' + error.message, 'error');
        throw error;
    });
}

// Chart initialization (if Chart.js is loaded)
function initializeCharts() {
    // Sales Chart
    const salesChart = document.getElementById('salesChart');
    if (salesChart && typeof Chart !== 'undefined') {
        new Chart(salesChart, {
            type: 'line',
            data: {
                labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
                datasets: [{
                    label: 'Sales',
                    data: [1000, 1200, 1500, 1800, 2000, 2200],
                    borderColor: '#3498db',
                    backgroundColor: 'rgba(52, 152, 219, 0.1)',
                    tension: 0.4
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        display: false
                    }
                },
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    }
    
    // Orders Chart
    const ordersChart = document.getElementById('ordersChart');
    if (ordersChart && typeof Chart !== 'undefined') {
        new Chart(ordersChart, {
            type: 'doughnut',
            data: {
                labels: ['Pending', 'Processing', 'Shipped', 'Delivered'],
                datasets: [{
                    data: [10, 15, 8, 25],
                    backgroundColor: ['#f39c12', '#3498db', '#9b59b6', '#27ae60']
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        position: 'bottom'
                    }
                }
            }
        });
    }
}

// Export functions for global use
window.MobileShop = {
    showAlert,
    formatCurrency,
    formatDate,
    calculateDeliveryCharges,
    sendSMS,
    processPayment,
    initializeCharts
};

// Initialize charts when page loads
document.addEventListener('DOMContentLoaded', function() {
    setTimeout(initializeCharts, 100);
});
