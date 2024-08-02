#!/usr/bin/env python3
"""
    Password encryption module
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Hashes the provided password using bcrypt and returns the salted,
    hashed password.

    Args:
        password (str): The password to be hashed.

    Returns:
        bytes: The salted, hashed password.
    """
    if password:
        return bcrypt.hashpw(str.encode(password), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Validates the provided password against the hashed password.

    Args:
        hashed_password (bytes): The hashed password to check against.
        password (str): The password to be validated.

    Returns:
        bool: True if the password matches the hash, False otherwise.
    """
    if hashed_password and password:
        return bcrypt.checkpw(str.encode(password), hashed_password)
