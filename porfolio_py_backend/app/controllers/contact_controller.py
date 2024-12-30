from flask import request, jsonify, current_app
from flask_mail import Message
from datetime import datetime
from app import mail
import traceback



def contact_handler():
    try:
        data = request.get_json()

        required_fields = ["name", "email", "subject", "message"]
        for field in required_fields:
            if not data.get(field):
                return jsonify({"error": f"Missing required field: {field}"}), 400

        

        msg = Message(
            subject=f"Contact Form: {data['subject']}",
            sender=current_app.config["MAIL_DEFAULT_SENDER"], 
            recipients=[current_app.config["MAIL_RECIPIENT"]],
            body=f"""
New contact form submission:

From: {data['name']} ({data['email']})
Subject: {data['subject']}

Message:
{data['message']}

            """,
        )

        mail.send(msg)

        return (
            jsonify(
                {
                    "message": "Message sent successfully",
                    "timestamp": datetime.now().isoformat(),
                }
            ),
            200,
        )

    except Exception as e:
        error_details = traceback.format_exc()
        return (
            jsonify(
                {
                    "error": str(e),
                    "message": "Failed to send message",
                    "details": error_details,
                }
            ),
            500,
        )
