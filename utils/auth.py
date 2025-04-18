from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from models.user import Users
from functools import wraps
from flask import jsonify


def generate_token(user_id):
    return create_access_token(identity=str(user_id))


def token_required(f):
    @wraps(f)
    @jwt_required()
    def decorated_function(*args, **kwargs):
        user_id = get_jwt_identity()
        user = Users.query.get(int(user_id))
        if not user:
            return jsonify({"error": "User not found"}), 404
        return f(user, *args, **kwargs)

    return decorated_function
