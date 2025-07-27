#!/usr/bin/env python3
"""DocDocDocDoc"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Methods for Basic Base64 auth"""

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """Extracts base64 authorization from header"""
        if authorization_header is None:
            return None
        if type(authorization_header) != str:
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]
