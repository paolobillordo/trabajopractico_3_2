from flask import Flask
from config import Config
from .routes.customer_bp import customer_bp

def init_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(customer_bp)

    @app.route('/')
    def home():
        return "BIKESHOP"
    
    
    return app
