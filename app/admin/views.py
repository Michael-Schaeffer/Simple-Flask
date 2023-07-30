from flask import render_template
from . import admin_bp

# Define some routes for the admin module using the 'admin_bp' blueprint
@admin_bp.route('/admin')
def admin():
    return render_template(
        'index.html',
        header = "Admin"
        )

@admin_bp.route('/dashboard')
def dashboard():
    return render_template(
        'index.html',
        header = "This is admin dashboard"
    )