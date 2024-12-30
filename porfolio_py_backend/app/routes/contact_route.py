from flask import Blueprint, request
from flask_mail import Mail
from app.controllers.contact_controller import contact_handler
import logging


contact_bp = Blueprint("contact", __name__)
mail = Mail()


@contact_bp.route("/contact", methods=["POST"])
def send_contact():
    return contact_handler()
