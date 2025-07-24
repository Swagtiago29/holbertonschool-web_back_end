#!/usr/bin/env python3
"""Task 0"""
from re import sub


def filter_datum(fields, redaction, message, separator):
    """ comments fpr filter_datum """
    return sub(rf"({'|'.join(fields)})=[^{separator}]*",
                  rf"\1={redaction}",
                  message)
