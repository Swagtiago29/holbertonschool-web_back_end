#!/usr/bin/env python3
from bcrypt import hashpw, checkpw, gensalt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> bytes:
    encoded = password.encode('utf-8')
    salt = gensalt()
    return hashpw(encoded, salt)


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = _hash_password(password)
            self._db.add_user(email, hashed_password)
            return self._db.find_user_by(email=email)

    def valid_login(self, email: str, password: str) -> bool:
        try:
            user = self._db.find_user_by(email=email)
            return checkpw(password.encode('utf-8'), user.hashed_password)
        except NoResultFound:
            return False

    def _generate_uuid(self) -> str:
        new_uuid = uuid4()
        return str(new_uuid)
