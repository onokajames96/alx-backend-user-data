#!/usr/bin/env python3
"""Authentication"""
from flask import abort, jsonify, request
from api.v1.views import app_views
from models.user import User


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def view_all_users() -> str:
    """GET / view all users"""
    all_users = [user.to_json() for user in User.all()]
    return jsonify(all_users)

@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def view_one_user(user_id: str = None) -> str:
    """views the user"""
    if user_id == 'me':
        user = request.current_user
        if not user:
            abort(404)
        return jsonify(user.to_json())

    user = User.get(user_id)
    if not user:
        abort(404)
    return jsonify(user.to_json())

@app_views.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
def delete_user(user_id: str = None) -> str:
    """DELete """
    user = User.get(user_id)
    if not user:
        abort(404)
    user.remove()
    return jsonify({})

@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_user() -> str:
    """Creates users"""
    data = request.get_json()
    if not data or not data.get('email') or not data.get('password'):
        return jsonify({'error': 'email and password are required'}), 400

    try:
        user = User(email=data['email'], password=data['password'],
                    first_name=data.get('first_name'), last_name=data.get('last_name'))
        user.save()
        return jsonify(user.to_json()), 201
    except Exception as e:
        return jsonify({'error': f'Unable to create User: {e}'}), 400

@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def update_user(user_id: str = None) -> str:
    """PUT / updates users
    """
    user = User.get(user_id)
    if not user:
        abort(404)

    data = request.get_json()
    if data:
        user.first_name = data.get('first_name', user.first_name)
        user.last_name = data.get('last_name', user.last_name)

    try:
        user.save()
        return jsonify(user.to_json()), 200
    except Exception as e:
        return jsonify({'error': f'Unable to update User: {e}'}), 400
