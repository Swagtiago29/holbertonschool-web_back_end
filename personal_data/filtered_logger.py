#!/usr/bin/env python3
"""Task 0 - log obfuscator"""
import re
from typing import List


def filter_datum(fields: List[str],
                 redaction: str, message: str, separator: str) -> str:
    """Redacts values of specified fields in a log message."""
    return re.sub(
        rf"({'|'.join(map(re.escape, fields))})=.*?{re.escape(separator)}",
        rf"\1={redaction}{separator}", message)
