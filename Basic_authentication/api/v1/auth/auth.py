#!/usr/bin/env python3
"""DocDocDocDocDoc"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Auth Class methods"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Checks if path is authorized"""
        if path is None:
            return True
        if not excluded_paths:
            return True
        if not path.endswith("/"):
            path += '/'
        if path in excluded_paths:
            return False    
    def authorization_header(self, request=None) -> str:
        """to be implemented"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """to be implemented"""
        return None
