#!/usr/bin/env python3
"""Task 0 - log obfuscator"""
import re
from typing import List


def filter_datum(fields: List[str],
                 redaction: str, message: str, separator: str):
    """Redacts values of specified fields in a log message."""
    return re.sub(f"({'|'.join(fields)})=.*?{separator}",
                  f"\\1={redaction}{separator}", message)
