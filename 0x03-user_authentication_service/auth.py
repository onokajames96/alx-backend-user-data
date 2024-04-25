#!/usr/bin/env python3
"""Auth """

import bcrypt
from db import DB


def _hash_password(password: str) -> bytes:
    """
    Hash the password using bcrypt.hashpw with the generated salt
    """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        try:
            self.db.find_user_by(email=email)

        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))
        raise ValueError(f"User {email} already exists")
