from flask import Blueprint, request, jsonify
from models.user import Users
from instance.database import db
from shared import crono
from werkzeug.security import generate_password_hash, check_password_hash
from pydantic import BaseModel, ValidationError
from repo.user import create_user
from utils.auth import generate_token, token_required
from flask_jwt_extended import create_access_token, create_refresh_token


class UserRegisterSchema(BaseModel):
    username: str
    first_name: str
    last_name: str
    email: str
    phone: str
    password: str
    date_of_birth: str
    address: str
    city: str
    state: str
    country: str
    zip_code: str
    image_url: str
    role: str
    bank_account: str
    bank_name: str


user_router = Blueprint("user", __name__, url_prefix="/users")


@user_router.route("", methods=["POST"])
def register_user():
    """Register a new user using schema validation & repo logic."""
    data = request.json
    try:
        user = UserRegisterSchema.model_validate(data)
    except ValidationError as e:
        return jsonify({"error": "Validation failed", "details": e.errors()}), 400

    if Users.query.filter_by(username=user.username).first():
        return jsonify({"error": "Username already exists"}), 400
    if Users.query.filter_by(email=user.email).first():
        return jsonify({"error": "Email already exists"}), 400
    if Users.query.filter_by(phone=user.phone).first():
        return jsonify({"error": "Phone already exists"}), 400

    hashed_password = generate_password_hash(user.password)
    created_user = create_user(user, hashed_password)

    return (
        jsonify(
            {
                "message": "User registered successfully",
                "user": {
                    "id": created_user.id,
                    "username": created_user.username,
                    "email": created_user.email,
                    "role": created_user.role.value,
                    "is_active": created_user.is_active,
                },
            }
        ),
        201,
    )


@user_router.route("/login", methods=["POST"])
def login_user():
    data = request.json
    if not data or "username" not in data or "password" not in data:
        return jsonify({"error": "Username and password required"}), 400

    user = Users.query.filter_by(username=data["username"]).first()
    if not user or not check_password_hash(user.password_hash, data["password"]):
        return jsonify({"error": "Invalid credentials"}), 401

    access_token = create_access_token(identity=str(user.id))
    refresh_token = create_refresh_token(identity=str(user.id))

    return (
        jsonify(
            {
                "access_token": access_token,
                "refresh_token": refresh_token,
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                    "role": user.role.value,
                },
            }
        ),
        200,
    )


@user_router.route("/me", methods=["GET"])
@token_required
def get_profile(current_user):
    return jsonify(
        {
            "id": current_user.id,
            "username": current_user.username,
            "first_name": current_user.first_name,
            "last_name": current_user.last_name,
            "email": current_user.email,
            "phone": current_user.phone,
            "address": current_user.address,
            "city": current_user.city,
            "state": current_user.state,
            "country": current_user.country,
            "zip_code": current_user.zip_code,
            "image_url": current_user.image_url,
            "role": current_user.role.value,
            "bank_account": current_user.bank_account,
            "bank_name": current_user.bank_name,
            "created_at": current_user.created_at.isoformat(),
            "updated_at": current_user.updated_at.isoformat(),
        }
    )


@user_router.route("/me", methods=["PUT"])
@token_required
def update_profile(current_user):
    data = request.json
    if not data:
        return jsonify({"error": "No data provided"}), 400

    fields = [
        "username",
        "email",
        "first_name",
        "last_name",
        "phone",
        "address",
        "city",
        "state",
        "country",
        "zip_code",
        "image_url",
        "bank_account",
        "bank_name",
    ]

    for field in fields:
        if field in data:
            setattr(current_user, field, data[field])

    if "password" in data:
        current_user.password_hash = generate_password_hash(data["password"])

    current_user.updated_at = crono.now()
    db.session.commit()

    return jsonify(
        {
            "message": "Profile updated successfully",
            "user": {
                "id": current_user.id,
                "username": current_user.username,
                "email": current_user.email,
            },
        }
    )
