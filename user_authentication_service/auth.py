#!/usr/bin/env python3
"""
Auth module for handling user authentication, session management,
and password hashing for the User Authentication Service.
"""
from bcrypt import hashpw, checkpw, gensalt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> bytes:
    """Return a salted hash of the input password."""
    encoded = password.encode('utf-8')
    salt = gensalt()
    return hashpw(encoded, salt)


def _generate_uuid() -> str:
    """Return a new string UUID."""
    new_uuid = uuid.uuid4()
    return str(new_uuid)


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self):
        """Initialize the Auth instance with a database connection."""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a new user with an email and password."""
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = _hash_password(password)
            self._db.add_user(email, hashed_password)
            return self._db.find_user_by(email=email)

    def valid_login(self, email: str, password: str) -> bool:
        """Check if provided login credentials are valid."""
        try:
            user = self._db.find_user_by(email=email)
            return checkpw(password.encode('utf-8'), user.hashed_password)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """Create a new session for the user and return the session ID."""
        try:
            curent_user = self._db.find_user_by(email=email)
            user_uuid = _generate_uuid()
            curent_user.session_id = user_uuid
            return user_uuid
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """Return the user corresponding to a given session ID."""
        try:
            if not session_id:
                return None
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """Destroy the session for the given user ID."""
        try:
            user = self._db.find_user_by(id=user_id)
            user.session_id = None
            self._db._session.commit()
            return None
        except NoResultFound:
            return None

    def get_reset_password_token(self, email: str) -> str:
        """Generate and return a password reset token for the user."""
        try:
            user = self._db.find_user_by(email=email)
            new_uuid = self.create_session(email)
            user.reset_token = new_uuid
            self._db._session.commit()
            return new_uuid
        except NoResultFound:
            raise ValueError

    def update_password(self, reset_token: str, password: str) -> None:
        """Update the user's password using the provided reset token."""
        try:
            user = self._db.find_user_by(reset_token=reset_token)
            hashed = _hash_password(password)
            user.hashed_password = hashed
            user.reset_token = None
            self._db._session.commit()
            return None
        except NoResultFound:
            raise ValueError
