from flask import send_file, abort, flash, redirect, url_for, session
from models import App, AppSubmission
import os

def download_app_file(app_id):
    """Handle app file downloads"""
    try:
        # Check if user is logged in
        if 'user_id' not in session and 'business_id' not in session:
            flash('Please log in to download files.', 'error')
            return redirect(url_for('user_login'))
        
        # First try to find in App table
        app = App.query.get(app_id)
        if app and app.app_file_path:
            file_path = app.app_file_path
            if os.path.exists(file_path):
                # Increment download count
                app.downloads = (app.downloads or 0) + 1
                db.session.commit()
                return send_file(file_path, as_attachment=True)
        
        # Then try AppSubmission table
        submission = AppSubmission.query.get(app_id)
        if submission and submission.app_apk_file:
            file_path = submission.app_apk_file
            if os.path.exists(file_path):
                return send_file(file_path, as_attachment=True)
        
        # If verification method is not upload, redirect to external link
        if submission:
            if submission.verification_method == 'github' and submission.github_repo_url:
                return redirect(submission.github_repo_url)
            elif submission.verification_method == 'store':
                if submission.google_play_url:
                    return redirect(submission.google_play_url)
                elif submission.apple_store_url:
                    return redirect(submission.apple_store_url)
            elif submission.verification_method == 'website' and submission.official_website_url:
                return redirect(submission.official_website_url)
        
        flash('File not found or download link unavailable.', 'error')
        return redirect(url_for('app_home'))
        
    except Exception as e:
        flash(f'Error downloading file: {str(e)}', 'error')
        return redirect(url_for('app_home'))