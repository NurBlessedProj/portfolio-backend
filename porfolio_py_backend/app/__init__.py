from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import Config
import pymysql
from flask_mail import Mail
import logging

# Install PyMySQL as MySQLdb
pymysql.install_as_MySQLdb()

mail = Mail()
db = SQLAlchemy()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Setup logging
    logging.basicConfig(level=logging.DEBUG)

    # Initialize extensions
    db.init_app(app)
    mail.init_app(app)

    # Configure CORS properly
    CORS(
        app,
        resources={
            r"/api/*": {
                "origins": "*",
                "methods": ["GET", "POST", "OPTIONS"],
                "allow_headers": ["Content-Type", "Authorization"],
            }
        },
    )

    @app.after_request
    def after_request(response):
        response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type,Authorization"
        )
        response.headers.add(
            "Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS"
        )
        return response

    from app.routes.project_route import project_routes
    from app.routes.contact_route import contact_bp

    app.register_blueprint(project_routes, url_prefix="/api")
    app.register_blueprint(contact_bp, url_prefix="/api")

    with app.app_context():
        db.create_all()

    return app
