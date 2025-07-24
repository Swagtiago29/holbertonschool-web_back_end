#!/usr/bin/env python3
"""Task 0"""
import re


def filter_datum(fields, redaction, message, separator):
    """Redacts values of specified fields in a log message."""
    return re.sub(rf"({'|'.join(fields)})=[^{separator}]*", rf"\1={redaction}", message)
