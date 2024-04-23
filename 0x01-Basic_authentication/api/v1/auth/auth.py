#!/usr/bin/env python3
"""
Authentication for API mdule
"""
from typing import List, TypeVar
from flask import request


class Auth:
    """
    Authentication class module
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Check if authentication is required for the given path.
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Get the authorization header from the Flask request.

        Args:
            request: The Flask request object.

        Returns:
            None since we are not implementing authentication logic yet.
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Get the current user based on the Flask request.
        """
        return None
