#!/usr/bin/env python3
"""Auth """

import bcrypt


def _hash_password(password: str) -> bytes:
    """
    Hash the password using bcrypt.hashpw with the generated salt
    """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
