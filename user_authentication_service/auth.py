#!/usr/bin/env python3
import bcrypt

def _hash_password(password:str) -> bytes:
    password.encode('utf-8')
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password, salt)
