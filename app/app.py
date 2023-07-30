from flask import Flask
from main import main_bp
from admin import admin_bp

app = Flask(__name__)
app.config.from_object("config.DevelopmentConfig")  # Configure from python files

app.register_blueprint(main_bp)
app.register_blueprint(admin_bp)

if __name__ == "__main__":
    app.run()
