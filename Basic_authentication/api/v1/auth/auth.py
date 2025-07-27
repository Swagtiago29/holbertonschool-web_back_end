#!/usr/bin/env python3
"""DocDocDocDocDoc"""
from flask import request
from typing import List, TypeVar

class Auth:

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """to be implemented"""
        return False


    def authorization_header(self, request=None) -> str:
        """to be implemented"""
        return None


    def current_user(self, request=None) -> TypeVar('User'):
        """to be implemented"""
        return None
