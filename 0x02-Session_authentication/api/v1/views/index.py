#!/usr/bin/env python3
"""AUthentication"""
from flask import jsonify, abort
from api.v1.views import app_views
from models.user import User


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> str:
    """GET /api/v1/status."""
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stats() -> str:
    """GET /api/v1/stats"""
    stats = {
        'users': User.count()
    }
    return jsonify(stats)


@app_views.route('/unauthorized', methods=['GET'], strict_slashes=False)
def unauthorized() -> None:
    """GET /api/v1/unauthorized"""
    abort(401)


@app_views.route('/forbidden', methods=['GET'], strict_slashes=False)
def forbidden() -> None:
    """GET /api/v1/forbidden"""
    abort(403)
