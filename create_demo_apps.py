#!/usr/bin/env python3
"""
Demo Apps Generator for Mobile Shop Management System
Creates 20 demo apps with detailed information for the apps showcase section
"""

from app import app as flask_app, db
from models import App
import json

def generate_app_logo_svg(app_name, color):
    """Generate SVG logo for app"""
    initials = ''.join([word[0] for word in app_name.split()[:2]]).upper()
    return f'''<svg width="64" height="64" viewBox="0 0 64 64" xmlns="http://www.w3.org/2000/svg">
        <rect width="64" height="64" rx="12" fill="{color}"/>
        <text x="32" y="40" font-family="Arial, sans-serif" font-size="20" font-weight="bold" 
              text-anchor="middle" fill="white">{initials}</text>
    </svg>'''

def create_demo_apps():
    """Create 20 demo apps with comprehensive information"""
    
    # Delete existing apps
    App.query.delete()
    
    apps_data = [
        {
            'name': 'TaskMaster Pro',
            'slug': 'taskmaster-pro',
            'category': 'Productivity',
            'short_description': 'Advanced task management and productivity tracking application',
            'long_description': 'TaskMaster Pro is a comprehensive task management solution designed for professionals and teams. It features advanced project tracking, deadline management, team collaboration tools, and detailed analytics to boost productivity.',
            'version': '2.1.0',
            'downloads': 15420,
            'rating': 4.8,
            'reviews_count': 892,
            'features': [
                'Advanced task scheduling and prioritization',
                'Team collaboration and real-time updates',
                'Time tracking and productivity analytics',
                'Calendar integration and deadline alerts',
                'Custom project templates and workflows',
                'Mobile and desktop synchronization'
            ],
            'screenshots': [
                'data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzAwIiBoZWlnaHQ9IjIwMCIgdmlld0JveD0iMCAwIDMwMCAyMDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgPHJlY3Qgd2lkdGg9IjMwMCIgaGVpZ2h0PSIyMDAiIGZpbGw9IiNmOGY5ZmEiLz4KICA8cmVjdCB4PSIyMCIgeT0iMjAiIHdpZHRoPSIyNjAiIGhlaWdodD0iMTYwIiBmaWxsPSJ3aGl0ZSIgc3Ryb2tlPSIjZTNlNmVhIiBzdHJva2Utd2lkdGg9IjIiIHJ4PSI4Ii8+CiAgPHRleHQgeD0iMTUwIiB5PSIxMDAiIGZvbnQtZmFtaWx5PSJBcmlhbCIgZm9udC1zaXplPSIxNiIgZmlsbD0iIzM3NDE0YiIgdGV4dC1hbmNob3I9Im1pZGRsZSI+VGFzayBEYXNoYm9hcmQ8L3RleHQ+Cjwvc3ZnPg==',
                'data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzAwIiBoZWlnaHQ9IjIwMCIgdmlld0JveD0iMCAwIDMwMCAyMDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgPHJlY3Qgd2lkdGg9IjMwMCIgaGVpZ2h0PSIyMDAiIGZpbGw9IiNmOGY5ZmEiLz4KICA8cmVjdCB4PSIyMCIgeT0iMjAiIHdpZHRoPSIyNjAiIGhlaWdodD0iMTYwIiBmaWxsPSJ3aGl0ZSIgc3Ryb2tlPSIjZTNlNmVhIiBzdHJva2Utd2lkdGg9IjIiIHJ4PSI4Ii8+CiAgPHRleHQgeD0iMTUwIiB5PSIxMDAiIGZvbnQtZmFtaWx5PSJBcmlhbCIgZm9udC1zaXplPSIxNiIgZmlsbD0iIzM3NDE0YiIgdGV4dC1hbmNob3I9Im1pZGRsZSI+QW5hbHl0aWNzIFZpZXc8L3RleHQ+Cjwvc3ZnPg=='
            ],
            'author_name': 'Alex Johnson',
            'author_email': 'alex@productivity.com',
            'author_website': 'https://productivity.com',
            'author_bio': 'Software engineer with 8 years of experience in productivity applications.',
            'author_avatar': 'data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjQiIGhlaWdodD0iNjQiIHZpZXdCb3g9IjAgMCA2NCA2NCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8Y2lyY2xlIGN4PSIzMiIgY3k9IjMyIiByPSIzMiIgZmlsbD0iIzM0OThhMyIvPgogIDx0ZXh0IHg9IjMyIiB5PSI0MCIgZm9udC1mYW1pbHk9IkFyaWFsIiBmb250LXNpemU9IjI0IiBmaWxsPSJ3aGl0ZSIgdGV4dC1hbmNob3I9Im1pZGRsZSI+QUo8L3RleHQ+Cjwvc3ZnPg==',
            'support_email': 'support@taskmaster.com',
            'support_phone': '+1-555-0123',
            'support_website': 'https://taskmaster.com/support',
            'documentation_url': 'https://taskmaster.com/docs',
            'social_links': {
                'website': 'https://taskmaster.com',
                'twitter': 'https://twitter.com/taskmaster',
                'facebook': 'https://facebook.com/taskmaster',
                'linkedin': 'https://linkedin.com/company/taskmaster'
            },
            'color': '#3498a3'
        },
        {
            'name': 'EcoTracker',
            'slug': 'ecotracker',
            'category': 'Environment',
            'short_description': 'Personal carbon footprint tracking and environmental impact monitor',
            'long_description': 'EcoTracker helps individuals and organizations monitor their environmental impact through detailed carbon footprint analysis, sustainability recommendations, and eco-friendly lifestyle tracking.',
            'version': '1.5.2',
            'downloads': 8730,
            'rating': 4.6,
            'reviews_count': 445,
            'features': [
                'Carbon footprint calculation and tracking',
                'Sustainability recommendations',
                'Eco-friendly product suggestions',
                'Environmental impact reports',
                'Community challenges and achievements',
                'Integration with smart home devices'
            ],
            'screenshots': [
                'data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzAwIiBoZWlnaHQ9IjIwMCIgdmlld0JveD0iMCAwIDMwMCAyMDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgPHJlY3Qgd2lkdGg9IjMwMCIgaGVpZ2h0PSIyMDAiIGZpbGw9IiNlOGY1ZTgiLz4KICA8cmVjdCB4PSIyMCIgeT0iMjAiIHdpZHRoPSIyNjAiIGhlaWdodD0iMTYwIiBmaWxsPSJ3aGl0ZSIgc3Ryb2tlPSIjNGNhZjUwIiBzdHJva2Utd2lkdGg9IjIiIHJ4PSI4Ii8+CiAgPHRleHQgeD0iMTUwIiB5PSIxMDAiIGZvbnQtZmFtaWx5PSJBcmlhbCIgZm9udC1zaXplPSIxNiIgZmlsbD0iIzJlN2QzMiIgdGV4dC1hbmNob3I9Im1pZGRsZSI+Q2FyYm9uIEZvb3RwcmludDwvdGV4dD4KPC9zdmc+',
                'data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzAwIiBoZWlnaHQ9IjIwMCIgdmlld0JveD0iMCAwIDMwMCAyMDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgPHJlY3Qgd2lkdGg9IjMwMCIgaGVpZ2h0PSIyMDAiIGZpbGw9IiNlOGY1ZTgiLz4KICA8cmVjdCB4PSIyMCIgeT0iMjAiIHdpZHRoPSIyNjAiIGhlaWdodD0iMTYwIiBmaWxsPSJ3aGl0ZSIgc3Ryb2tlPSIjNGNhZjUwIiBzdHJva2Utd2lkdGg9IjIiIHJ4PSI4Ii8+CiAgPHRleHQgeD0iMTUwIiB5PSIxMDAiIGZvbnQtZmFtaWx5PSJBcmlhbCIgZm9udC1zaXplPSIxNiIgZmlsbD0iIzJlN2QzMiIgdGV4dC1hbmNob3I9Im1pZGRsZSI+RWNvIENoYWxsZW5nZXM8L3RleHQ+Cjwvc3ZnPg=='
            ],
            'author_name': 'Maria Santos',
            'author_email': 'maria@greentech.com',
            'author_website': 'https://greentech.com',
            'author_bio': 'Environmental scientist and app developer passionate about sustainability.',
            'author_avatar': 'data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjQiIGhlaWdodD0iNjQiIHZpZXdCb3g9IjAgMCA2NCA2NCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8Y2lyY2xlIGN4PSIzMiIgY3k9IjMyIiByPSIzMiIgZmlsbD0iIzRjYWY1MCIvPgogIDx0ZXh0IHg9IjMyIiB5PSI0MCIgZm9udC1mYW1pbHk9IkFyaWFsIiBmb250LXNpemU9IjI0IiBmaWxsPSJ3aGl0ZSIgdGV4dC1hbmNob3I9Im1pZGRsZSI+TVM8L3RleHQ+Cjwvc3ZnPg==',
            'support_email': 'help@ecotracker.com',
            'support_phone': '+1-555-0234',
            'support_website': 'https://ecotracker.com/help',
            'documentation_url': 'https://ecotracker.com/guide',
            'social_links': {
                'website': 'https://ecotracker.com',
                'twitter': 'https://twitter.com/ecotracker',
                'instagram': 'https://instagram.com/ecotracker',
                'youtube': 'https://youtube.com/ecotracker'
            },
            'color': '#4caf50'
        },
        {
            'name': 'FitnessPal',
            'slug': 'fitnesspal',
            'category': 'Health & Fitness',
            'short_description': 'Comprehensive fitness tracking and workout planning application',
            'long_description': 'FitnessPal is your personal fitness companion that helps you track workouts, plan nutrition, monitor progress, and achieve your health goals with personalized training programs.',
            'version': '3.2.1',
            'downloads': 25600,
            'rating': 4.7,
            'reviews_count': 1250,
            'features': [
                'Workout tracking and exercise library',
                'Nutrition planning and calorie counter',
                'Progress monitoring and analytics',
                'Personal trainer recommendations',
                'Social fitness challenges',
                'Wearable device integration'
            ],
            'screenshots': [
                'data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzAwIiBoZWlnaHQ9IjIwMCIgdmlld0JveD0iMCAwIDMwMCAyMDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgPHJlY3Qgd2lkdGg9IjMwMCIgaGVpZ2h0PSIyMDAiIGZpbGw9IiNmZmU1ZTUiLz4KICA8cmVjdCB4PSIyMCIgeT0iMjAiIHdpZHRoPSIyNjAiIGhlaWdodD0iMTYwIiBmaWxsPSJ3aGl0ZSIgc3Ryb2tlPSIjZjU2NTY1IiBzdHJva2Utd2lkdGg9IjIiIHJ4PSI4Ii8+CiAgPHRleHQgeD0iMTUwIiB5PSIxMDAiIGZvbnQtZmFtaWx5PSJBcmlhbCIgZm9udC1zaXplPSIxNiIgZmlsbD0iI2Q1M2YzZiIgdGV4dC1hbmNob3I9Im1pZGRsZSI+V29ya291dCBUcmFja2VyPC90ZXh0Pgo8L3N2Zz4=',
                'data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzAwIiBoZWlnaHQ9IjIwMCIgdmlld0JveD0iMCAwIDMwMCAyMDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgPHJlY3Qgd2lkdGg9IjMwMCIgaGVpZ2h0PSIyMDAiIGZpbGw9IiNmZmU1ZTUiLz4KICA8cmVjdCB4PSIyMCIgeT0iMjAiIHdpZHRoPSIyNjAiIGhlaWdodD0iMTYwIiBmaWxsPSJ3aGl0ZSIgc3Ryb2tlPSIjZjU2NTY1IiBzdHJva2Utd2lkdGg9IjIiIHJ4PSI4Ii8+CiAgPHRleHQgeD0iMTUwIiB5PSIxMDAiIGZvbnQtZmFtaWx5PSJBcmlhbCIgZm9udC1zaXplPSIxNiIgZmlsbD0iI2Q1M2YzZiIgdGV4dC1hbmNob3I9Im1pZGRsZSI+TnV0cml0aW9uIFBsYW48L3RleHQ+Cjwvc3ZnPg=='
            ],
            'author_name': 'David Kim',
            'author_email': 'david@fitnesstech.com',
            'author_website': 'https://fitnesstech.com',
            'author_bio': 'Certified fitness trainer and mobile app developer with 5 years experience.',
            'author_avatar': 'data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjQiIGhlaWdodD0iNjQiIHZpZXdCb3g9IjAgMCA2NCA2NCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8Y2lyY2xlIGN4PSIzMiIgY3k9IjMyIiByPSIzMiIgZmlsbD0iI2Y1NjU2NSIvPgogIDx0ZXh0IHg9IjMyIiB5PSI0MCIgZm9udC1mYW1pbHk9IkFyaWFsIiBmb250LXNpemU9IjI0IiBmaWxsPSJ3aGl0ZSIgdGV4dC1hbmNob3I9Im1pZGRsZSI+REs8L3RleHQ+Cjwvc3ZnPg==',
            'support_email': 'support@fitnesspal.com',
            'support_phone': '+1-555-0345',
            'support_website': 'https://fitnesspal.com/support',
            'documentation_url': 'https://fitnesspal.com/help',
            'social_links': {
                'website': 'https://fitnesspal.com',
                'twitter': 'https://twitter.com/fitnesspal',
                'instagram': 'https://instagram.com/fitnesspal',
                'facebook': 'https://facebook.com/fitnesspal'
            },
            'color': '#f56565'
        },
        {
            'name': 'CryptoWallet Pro',
            'slug': 'cryptowallet-pro',
            'category': 'Finance',
            'short_description': 'Secure cryptocurrency wallet and portfolio management system',
            'long_description': 'CryptoWallet Pro provides a secure, user-friendly platform for managing cryptocurrency investments with advanced security features, portfolio tracking, and market analysis tools.',
            'version': '2.0.5',
            'downloads': 12300,
            'rating': 4.5,
            'reviews_count': 678,
            'features': [
                'Multi-currency wallet support',
                'Portfolio tracking and analytics',
                'Real-time market data and alerts',
                'Advanced security with biometric access',
                'DeFi integration and staking options',
                'Cross-platform synchronization'
            ],
            'screenshots': [
                'data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzAwIiBoZWlnaHQ9IjIwMCIgdmlld0JveD0iMCAwIDMwMCAyMDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgPHJlY3Qgd2lkdGg9IjMwMCIgaGVpZ2h0PSIyMDAiIGZpbGw9IiNmZmY5ZTciLz4KICA8cmVjdCB4PSIyMCIgeT0iMjAiIHdpZHRoPSIyNjAiIGhlaWdodD0iMTYwIiBmaWxsPSJ3aGl0ZSIgc3Ryb2tlPSIjZjU5ZTBiIiBzdHJva2Utd2lkdGg9IjIiIHJ4PSI4Ii8+CiAgPHRleHQgeD0iMTUwIiB5PSIxMDAiIGZvbnQtZmFtaWx5PSJBcmlhbCIgZm9udC1zaXplPSIxNiIgZmlsbD0iI2Q2OTYwNCIgdGV4dC1hbmNob3I9Im1pZGRsZSI+V2FsbGV0IERhc2hib2FyZDwvdGV4dD4KPC9zdmc+',
                'data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzAwIiBoZWlnaHQ9IjIwMCIgdmlld0JveD0iMCAwIDMwMCAyMDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgPHJlY3Qgd2lkdGg9IjMwMCIgaGVpZ2h0PSIyMDAiIGZpbGw9IiNmZmY5ZTciLz4KICA8cmVjdCB4PSIyMCIgeT0iMjAiIHdpZHRoPSIyNjAiIGhlaWdodD0iMTYwIiBmaWxsPSJ3aGl0ZSIgc3Ryb2tlPSIjZjU5ZTBiIiBzdHJva2Utd2lkdGg9IjIiIHJ4PSI4Ii8+CiAgPHRleHQgeD0iMTUwIiB5PSIxMDAiIGZvbnQtZmFtaWx5PSJBcmlhbCIgZm9udC1zaXplPSIxNiIgZmlsbD0iI2Q2OTYwNCIgdGV4dC1hbmNob3I9Im1pZGRsZSI+TWFya2V0IEFuYWx5c2lzPC90ZXh0Pgo8L3N2Zz4='
            ],
            'author_name': 'Sarah Chen',
            'author_email': 'sarah@cryptotech.com',
            'author_website': 'https://cryptotech.com',
            'author_bio': 'Blockchain developer and cybersecurity expert with 7 years in fintech.',
            'author_avatar': 'data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjQiIGhlaWdodD0iNjQiIHZpZXdCb3g9IjAgMCA2NCA2NCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8Y2lyY2xlIGN4PSIzMiIgY3k9IjMyIiByPSIzMiIgZmlsbD0iI2Y1OWUwYiIvPgogIDx0ZXh0IHg9IjMyIiB5PSI0MCIgZm9udC1mYW1pbHk9IkFyaWFsIiBmb250LXNpemU9IjI0IiBmaWxsPSJ3aGl0ZSIgdGV4dC1hbmNob3I9Im1pZGRsZSI+U0M8L3RleHQ+Cjwvc3ZnPg==',
            'support_email': 'support@cryptowallet.com',
            'support_phone': '+1-555-0456',
            'support_website': 'https://cryptowallet.com/support',
            'documentation_url': 'https://cryptowallet.com/docs',
            'social_links': {
                'website': 'https://cryptowallet.com',
                'twitter': 'https://twitter.com/cryptowallet',
                'telegram': 'https://t.me/cryptowallet',
                'reddit': 'https://reddit.com/r/cryptowallet'
            },
            'color': '#f59e0b'
        },
        {
            'name': 'StudyBuddy',
            'slug': 'studybuddy',
            'category': 'Education',
            'short_description': 'Interactive learning platform with AI-powered study assistance',
            'long_description': 'StudyBuddy revolutionizes learning with AI-powered study assistance, interactive flashcards, collaborative study groups, and personalized learning paths for students of all ages.',
            'version': '1.8.3',
            'downloads': 18900,
            'rating': 4.9,
            'reviews_count': 1045,
            'features': [
                'AI-powered study recommendations',
                'Interactive flashcards and quizzes',
                'Collaborative study groups',
                'Progress tracking and analytics',
                'Subject-specific learning paths',
                'Offline study mode'
            ],
            'screenshots': [
                'data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzAwIiBoZWlnaHQ9IjIwMCIgdmlld0JveD0iMCAwIDMwMCAyMDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgPHJlY3Qgd2lkdGg9IjMwMCIgaGVpZ2h0PSIyMDAiIGZpbGw9IiNlZGY0ZmYiLz4KICA8cmVjdCB4PSIyMCIgeT0iMjAiIHdpZHRoPSIyNjAiIGhlaWdodD0iMTYwIiBmaWxsPSJ3aGl0ZSIgc3Ryb2tlPSIjNjM2NmYxIiBzdHJva2Utd2lkdGg9IjIiIHJ4PSI4Ii8+CiAgPHRleHQgeD0iMTUwIiB5PSIxMDAiIGZvbnQtZmFtaWx5PSJBcmlhbCIgZm9udC1zaXplPSIxNiIgZmlsbD0iIzQ3NTJhNiIgdGV4dC1hbmNob3I9Im1pZGRsZSI+U3R1ZHkgRGFzaGJvYXJkPC90ZXh0Pgo8L3N2Zz4=',
                'data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzAwIiBoZWlnaHQ9IjIwMCIgdmlld0JveD0iMCAwIDMwMCAyMDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgPHJlY3Qgd2lkdGg9IjMwMCIgaGVpZ2h0PSIyMDAiIGZpbGw9IiNlZGY0ZmYiLz4KICA8cmVjdCB4PSIyMCIgeT0iMjAiIHdpZHRoPSIyNjAiIGhlaWdodD0iMTYwIiBmaWxsPSJ3aGl0ZSIgc3Ryb2tlPSIjNjM2NmYxIiBzdHJva2Utd2lkdGg9IjIiIHJ4PSI4Ii8+CiAgPHRleHQgeD0iMTUwIiB5PSIxMDAiIGZvbnQtZmFtaWx5PSJBcmlhbCIgZm9udC1zaXplPSIxNiIgZmlsbD0iIzQ3NTJhNiIgdGV4dC1hbmNob3I9Im1pZGRsZSI+QUkgVHV0b3I8L3RleHQ+Cjwvc3ZnPg=='
            ],
            'author_name': 'Michael Rodriguez',
            'author_email': 'michael@edutech.com',
            'author_website': 'https://edutech.com',
            'author_bio': 'Educational technology specialist and former teacher with passion for AI.',
            'author_avatar': 'data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjQiIGhlaWdodD0iNjQiIHZpZXdCb3g9IjAgMCA2NCA2NCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8Y2lyY2xlIGN4PSIzMiIgY3k9IjMyIiByPSIzMiIgZmlsbD0iIzYzNjZmMSIvPgogIDx0ZXh0IHg9IjMyIiB5PSI0MCIgZm9udC1mYW1pbHk9IkFyaWFsIiBmb250LXNpemU9IjI0IiBmaWxsPSJ3aGl0ZSIgdGV4dC1hbmNob3I9Im1pZGRsZSI+TVI8L3RleHQ+Cjwvc3ZnPg==',
            'support_email': 'help@studybuddy.com',
            'support_phone': '+1-555-0567',
            'support_website': 'https://studybuddy.com/help',
            'documentation_url': 'https://studybuddy.com/guide',
            'social_links': {
                'website': 'https://studybuddy.com',
                'twitter': 'https://twitter.com/studybuddy',
                'facebook': 'https://facebook.com/studybuddy',
                'youtube': 'https://youtube.com/studybuddy'
            },
            'color': '#6366f1'
        }
    ]
    
    # Add remaining 15 apps to make it 20 total
    additional_apps = [
        {
            'name': 'PhotoEdit Pro',
            'slug': 'photoedit-pro',
            'category': 'Photography',
            'short_description': 'Professional photo editing with AI-powered enhancements',
            'version': '4.1.0',
            'downloads': 32100,
            'rating': 4.8,
            'reviews_count': 1876,
            'author_name': 'Emma Wilson',
            'author_email': 'emma@phototech.com',
            'color': '#ec4899'
        },
        {
            'name': 'TravelGuide',
            'slug': 'travelguide',
            'category': 'Travel',
            'short_description': 'Comprehensive travel planning and navigation assistant',
            'version': '2.3.1',
            'downloads': 14500,
            'rating': 4.6,
            'reviews_count': 789,
            'author_name': 'Carlos Silva',
            'author_email': 'carlos@traveltech.com',
            'color': '#06b6d4'
        },
        {
            'name': 'MusicMaker',
            'slug': 'musicmaker',
            'category': 'Music',
            'short_description': 'Digital audio workstation for music production',
            'version': '3.0.2',
            'downloads': 21700,
            'rating': 4.7,
            'reviews_count': 1123,
            'author_name': 'James Thompson',
            'author_email': 'james@audiotech.com',
            'color': '#8b5cf6'
        },
        {
            'name': 'RecipeBook',
            'slug': 'recipebook',
            'category': 'Food & Drink',
            'short_description': 'Smart recipe management and meal planning app',
            'version': '1.6.4',
            'downloads': 19200,
            'rating': 4.5,
            'reviews_count': 945,
            'author_name': 'Sofia Martinez',
            'author_email': 'sofia@foodtech.com',
            'color': '#f97316'
        },
        {
            'name': 'WeatherPro',
            'slug': 'weatherpro',
            'category': 'Weather',
            'short_description': 'Advanced weather forecasting with radar and alerts',
            'version': '5.2.0',
            'downloads': 45600,
            'rating': 4.9,
            'reviews_count': 2341,
            'author_name': 'Robert Brown',
            'author_email': 'robert@weathertech.com',
            'color': '#3b82f6'
        },
        {
            'name': 'VoiceMemo',
            'slug': 'voicememo',
            'category': 'Utilities',
            'short_description': 'Advanced voice recording and transcription tool',
            'version': '2.1.3',
            'downloads': 11800,
            'rating': 4.4,
            'reviews_count': 567,
            'author_name': 'Lisa Chang',
            'author_email': 'lisa@voicetech.com',
            'color': '#10b981'
        },
        {
            'name': 'BudgetTracker',
            'slug': 'budgettracker',
            'category': 'Finance',
            'short_description': 'Personal finance management and expense tracking',
            'version': '1.9.0',
            'downloads': 16300,
            'rating': 4.6,
            'reviews_count': 821,
            'author_name': 'Daniel Lee',
            'author_email': 'daniel@fintech.com',
            'color': '#059669'
        },
        {
            'name': 'GameCenter',
            'slug': 'gamecenter',
            'category': 'Games',
            'short_description': 'Multiplayer gaming platform with tournaments',
            'version': '3.4.1',
            'downloads': 38900,
            'rating': 4.7,
            'reviews_count': 1965,
            'author_name': 'Ryan Park',
            'author_email': 'ryan@gametech.com',
            'color': '#dc2626'
        },
        {
            'name': 'NewsHub',
            'slug': 'newshub',
            'category': 'News',
            'short_description': 'Personalized news aggregation and reading app',
            'version': '2.5.2',
            'downloads': 27400,
            'rating': 4.5,
            'reviews_count': 1234,
            'author_name': 'Anna Johnson',
            'author_email': 'anna@newstech.com',
            'color': '#374151'
        },
        {
            'name': 'SocialConnect',
            'slug': 'socialconnect',
            'category': 'Social',
            'short_description': 'Advanced social networking with privacy controls',
            'version': '1.3.0',
            'downloads': 22100,
            'rating': 4.3,
            'reviews_count': 987,
            'author_name': 'Kevin Wu',
            'author_email': 'kevin@socialtech.com',
            'color': '#1f2937'
        },
        {
            'name': 'HealthMonitor',
            'slug': 'healthmonitor',
            'category': 'Health & Fitness',
            'short_description': 'Comprehensive health tracking and medical records',
            'version': '2.7.1',
            'downloads': 19700,
            'rating': 4.8,
            'reviews_count': 1076,
            'author_name': 'Dr. Sarah Kim',
            'author_email': 'sarah@healthtech.com',
            'color': '#ef4444'
        },
        {
            'name': 'ShoppingList',
            'slug': 'shoppinglist',
            'category': 'Shopping',
            'short_description': 'Smart shopping list with price comparison',
            'version': '1.4.2',
            'downloads': 13600,
            'rating': 4.4,
            'reviews_count': 675,
            'author_name': 'Michelle Davis',
            'author_email': 'michelle@shoptech.com',
            'color': '#f59e0b'
        },
        {
            'name': 'DocumentScan',
            'slug': 'documentscan',
            'category': 'Business',
            'short_description': 'Professional document scanning and OCR processing',
            'version': '3.1.0',
            'downloads': 24800,
            'rating': 4.7,
            'reviews_count': 1298,
            'author_name': 'Peter Zhang',
            'author_email': 'peter@doctech.com',
            'color': '#6b7280'
        },
        {
            'name': 'LanguageLearn',
            'slug': 'languagelearn',
            'category': 'Education',
            'short_description': 'Interactive language learning with AI conversation',
            'version': '2.0.4',
            'downloads': 31200,
            'rating': 4.9,
            'reviews_count': 1654,
            'author_name': 'Marie Dubois',
            'author_email': 'marie@langtech.com',
            'color': '#8b5cf6'
        },
        {
            'name': 'SmartHome',
            'slug': 'smarthome',
            'category': 'Utilities',
            'short_description': 'Complete home automation and IoT device control',
            'version': '4.3.0',
            'downloads': 18500,
            'rating': 4.6,
            'reviews_count': 923,
            'author_name': 'Thomas Anderson',
            'author_email': 'thomas@hometech.com',
            'color': '#059669'
        }
    ]
    
    # Process all apps
    all_apps = apps_data + additional_apps
    
    for i, app_data in enumerate(all_apps):
        # Fill in missing data for additional apps
        if len(app_data) < 20:  # Basic structure
            app_data.update({
                'long_description': f"{app_data['short_description']} This application provides advanced features and user-friendly interface designed for modern users. Built with cutting-edge technology and optimized for performance.",
                'features': [
                    'User-friendly interface',
                    'Advanced functionality',
                    'Cloud synchronization',
                    'Multi-platform support',
                    'Regular updates',
                    'Customer support'
                ],
                'screenshots': [
                    f'data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzAwIiBoZWlnaHQ9IjIwMCIgdmlld0JveD0iMCAwIDMwMCAyMDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgPHJlY3Qgd2lkdGg9IjMwMCIgaGVpZ2h0PSIyMDAiIGZpbGw9IiNmOGY5ZmEiLz4KICA8cmVjdCB4PSIyMCIgeT0iMjAiIHdpZHRoPSIyNjAiIGhlaWdodD0iMTYwIiBmaWxsPSJ3aGl0ZSIgc3Ryb2tlPSIjZTNlNmVhIiBzdHJva2Utd2lkdGg9IjIiIHJ4PSI4Ii8+CiAgPHRleHQgeD0iMTUwIiB5PSIxMDAiIGZvbnQtZmFtaWx5PSJBcmlhbCIgZm9udC1zaXplPSIxNiIgZmlsbD0iIzM3NDE0YiIgdGV4dC1hbmNob3I9Im1pZGRsZSI+U2NyZWVuc2hvdCAxPC90ZXh0Pgo8L3N2Zz4=',
                    f'data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzAwIiBoZWlnaHQ9IjIwMCIgdmlld0JveD0iMCAwIDMwMCAyMDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgPHJlY3Qgd2lkdGg9IjMwMCIgaGVpZ2h0PSIyMDAiIGZpbGw9IiNmOGY5ZmEiLz4KICA8cmVjdCB4PSIyMCIgeT0iMjAiIHdpZHRoPSIyNjAiIGhlaWdodD0iMTYwIiBmaWxsPSJ3aGl0ZSIgc3Ryb2tlPSIjZTNlNmVhIiBzdHJva2Utd2lkdGg9IjIiIHJ4PSI4Ii8+CiAgPHRleHQgeD0iMTUwIiB5PSIxMDAiIGZvbnQtZmFtaWx5PSJBcmlhbCIgZm9udC1zaXplPSIxNiIgZmlsbD0iIzM3NDE0YiIgdGV4dC1hbmNob3I9Im1pZGRsZSI+U2NyZWVuc2hvdCAyPC90ZXh0Pgo8L3N2Zz4='
                ],
                'author_website': f'https://{app_data["slug"]}.com',
                'author_bio': f'Experienced developer specializing in {app_data["category"].lower()} applications.',
                'author_avatar': f'data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjQiIGhlaWdodD0iNjQiIHZpZXdCb3g9IjAgMCA2NCA2NCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8Y2lyY2xlIGN4PSIzMiIgY3k9IjMyIiByPSIzMiIgZmlsbD0iJXtwcC1kYXRhW2NvbG9yXX0iLz4KICA8dGV4dCB4PSIzMiIgeT0iNDAiIGZvbnQtZmFtaWx5PSJBcmlhbCIgZm9udC1zaXplPSIyNCIgZmlsbD0id2hpdGUiIHRleHQtYW5jaG9yPSJtaWRkbGUiPntlWzBdLnVwcGVyKCl9e2VbMV0udXBwZXIoKX08L3RleHQ+Cjwvc3ZnPg==',
                'support_email': f'support@{app_data["slug"]}.com',
                'support_phone': f'+1-555-{1000 + i:04d}',
                'support_website': f'https://{app_data["slug"]}.com/support',
                'documentation_url': f'https://{app_data["slug"]}.com/docs',
                'social_links': {
                    'website': f'https://{app_data["slug"]}.com',
                    'twitter': f'https://twitter.com/{app_data["slug"]}',
                    'facebook': f'https://facebook.com/{app_data["slug"]}',
                    'linkedin': f'https://linkedin.com/company/{app_data["slug"]}'
                }
            })
        
        # Create app instance
        app = App(
            name=app_data['name'],
            slug=app_data['slug'],
            logo_url=generate_app_logo_svg(app_data['name'], app_data['color']),
            short_description=app_data['short_description'],
            long_description=app_data['long_description'],
            category=app_data['category'],
            version=app_data['version'],
            downloads=app_data['downloads'],
            rating=app_data['rating'],
            reviews_count=app_data['reviews_count'],
            author_name=app_data['author_name'],
            author_email=app_data['author_email'],
            author_website=app_data['author_website'],
            author_bio=app_data['author_bio'],
            author_avatar=app_data['author_avatar'],
            support_email=app_data['support_email'],
            support_phone=app_data['support_phone'],
            support_website=app_data['support_website'],
            documentation_url=app_data['documentation_url'],
            status='active',
            featured=True if i < 8 else False  # First 8 apps are featured
        )
        
        # Set JSON fields
        app.set_features(app_data['features'])
        app.set_screenshots(app_data['screenshots'])
        app.set_social_links(app_data['social_links'])
        
        db.session.add(app)
    
    db.session.commit()
    print(f"✓ Created {len(all_apps)} demo apps successfully!")

def main():
    """Main function to create demo apps"""
    with flask_app.app_context():
        create_demo_apps()
        print("\n=== DEMO APPS CREATED ===")
        total_apps = App.query.count()
        featured_apps = App.query.filter_by(featured=True).count()
        print(f"Total Apps: {total_apps}")
        print(f"Featured Apps: {featured_apps}")
        
        print("\n=== SAMPLE APPS ===")
        sample_apps = App.query.limit(5).all()
        for app in sample_apps:
            print(f"- {app.name} ({app.category}) - {app.downloads} downloads, {app.rating}★")

if __name__ == "__main__":
    main()