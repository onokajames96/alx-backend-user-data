#!/usr/bin/env python3
"""passwords ENncryption"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Hashes a password"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Checks if its a hashed password
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
