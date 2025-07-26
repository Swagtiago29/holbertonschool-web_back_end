#bin/usr/env python3
"""encrypt password.py for task 5"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Returns the hashed password in bytes"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())