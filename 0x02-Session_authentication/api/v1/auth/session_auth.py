#!/usr/bin/env python3
"""Authentication """
from uuid import uuid4
from flask import request
from .auth import Auth
from models.user import User


class SessionAuth(Auth):
    """class module"""

    def __init__(self):
        """initialization"""
        self.user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Seesion Created"""
        if isinstance(user_id, str):
            session_id = str(uuid4())
            self.user_id_by_session_id[session_id] = user_id
            return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Gets user by seesion id"""
        if isinstance(session_id, str):
            return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None) -> User:
        """Requests user upon request"""
        user_id = self.user_id_for_session_id(self.session_cookie(request))
        return User.get(user_id)

    def destroy_session(self, request=None):
        """destroy the session"""
        session_id = self.session_cookie(request)
        if session_id:
            user_id = self.user_id_for_session_id(session_id)
            if user_id:
                del self.user_id_by_session_id[session_id]
                return True
        return False
