#!/usr/bin/env python3
import bcrypt
from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    encoded = password.encode('utf-8')
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(encoded, salt)

class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        try:
            self._db.find_user_by(email=email)
        except:   
           raise ValueError (f"User {email} already exists")
        hashed_password = _hash_password(password)
        self._db.add_user(self, email, hashed_password)
        return self._db.find_user_by(email=email)
