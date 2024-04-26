#!/usr/bin/env python3
"""SESSION AUTHENTICATION"""
import os
from typing import Tuple
from flask import abort, jsonify, request
from models.user import User
from api.v1.views import app_views
from api.v1.app import auth


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> Tuple[str, int]:
    """POST session login"""
    email = request.form.get('email')
    password = request.form.get('password')

    if not email or not email.strip():
        return jsonify({"error": "email missing"}), 400
    if not password or not password.strip():
        return jsonify({"error": "password missing"}), 400

    try:
        users = User.search({'email': email})
    except Exception:
        return jsonify({"error": "user search failed"}), 404

    if not users:
        return jsonify({"error": "no user found for this email"}), 404

    user = users[0]
    if user.is_valid_password(password):
        session_id = auth.create_session(user.id)
        response = jsonify(user.to_json())
        response.set_cookie(os.getenv("SESSION_NAME"), session_id)
        return response

    return jsonify({"error": "wrong password"}), 401

@app_views.route('/auth_session/logout', methods=['DELETE'], strict_slashes=False)
def logout() -> Tuple[str, int]:
    """session logout."""
    if not auth.destroy_session(request):
        abort(404)
    return jsonify({}), 200
