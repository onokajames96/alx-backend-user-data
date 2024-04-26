#!/usr/bin/env python3
"""MOdule for user session"""
from models.base import Base


class UserSession(Base):
    """Class user session"""

    def __init__(self, *args: list, **kwargs: dict):
        """Initialization of user session"""
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
