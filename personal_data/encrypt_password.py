#!/usr/bin/env python3
"""encrypt password.py for task 5"""
import bcrypt

def is_valid(hashed_password: bytes, password:str) -> bool:
    """Checks if a plaintext password matches the hashed password."""
    return bcrypt.checkpw(password.encode(), hashed_password)


def hash_password(password: str) -> bytes:
    """Returns the hashed password in bytes"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
