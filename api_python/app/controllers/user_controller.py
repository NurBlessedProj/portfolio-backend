from app.models.user import User
from app import db
from flask import request, jsonify


def create_user():
    data = request.json
    new_user = User(username=data["username"], email=data["email"])
    db.session.add(new_user)
    db.session.commit()

    return jsonify([{"id": new_user.id}])


def get_users():
    users = User.query.all()
    return jsonify(
        [
            {"id": user.id, "username": user.username, "email": user.email}
            for user in users
        ]
    )
