from flask import Blueprint

# Create a blueprint object for the 'admin' module
admin_bp = Blueprint('admin', __name__, template_folder='templates')

# Import the views from the 'views.py' file to associate with this blueprint
from . import views