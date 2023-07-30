from flask import render_template
from . import main_bp
from models import User


# Define some routes for the main module using the 'main_bp' blueprint
@main_bp.route('/')
def index():
    return render_template(
        'index.html',
        header = "Home"
        )

@main_bp.route('/about')
def about():
    return render_template(
        'index.html',
        header = "About",
        )

@main_bp.route('/users')
def list_users():
    users = User.fetch_all_user_data()
    # users = User.add_user_data()
    # users = User.delete_user_data(1)
    return render_template(
        'index.html',
        header = "Users",
        users = users
        )
