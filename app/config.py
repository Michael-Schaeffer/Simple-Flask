import os
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite://:memory:'
    SECRET_KEY = os.urandom(32)
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=5)
    
class ProductionConfig(Config):
    DEBUG = False
 
class DevelopmentConfig(Config):
    DEBUG = True
    # Database configuration
    # SQLALCHEMY_DATABASE_URI = "mysql://username:password@localhost/db_name"

    # Turn off the Flask-SQLAlchemy event system and warning
    # SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestingConfig(Config):
    TESTING = True