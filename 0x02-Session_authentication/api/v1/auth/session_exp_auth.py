#!/usr/bin/env python3
"""AUthentication"""
import os
from flask import request
from datetime import datetime, timedelta
from .session_auth import SessionAuth


class SessionExpAuth(SessionAuth):
    """Class for SessionExpAuth"""

    def __init__(self) -> None:
        """initialization"""
        super().__init__()
        try:
            self.session_duration = int(os.getenv('SESSION_DURATION', '0'))
        except ValueError:
            self.session_duration = 0

    def create_session(self, user_id=None) -> str:
        """Creates a session"""
        session_id = super().create_session(user_id)
        if not isinstance(session_id, str):
            return None
        
        self.user_id_by_session_id[session_id] = {
            'user_id': user_id,
            'created_at': datetime.now()
        }
        return session_id

    def user_id_for_session_id(self, session_id=None) -> str:
        """Retrieves."""
        if session_id in self.user_id_by_session_id:
            session_dict = self.user_id_by_session_id[session_id]
            if self.session_duration <= 0:
                return session_dict.get('user_id')
            
            created_at = session_dict.get('created_at')
            if not created_at:
                return None
            
            expiration_time = created_at + timedelta(seconds=self.session_duration)
            if datetime.now() > expiration_time:
                del self.user_id_by_session_id[session_id]
                return None
            
            return session_dict.get('user_id')
        
        return None
