#!/usr/bin/env python3
"""Task 0"""
import re


def filter_datum(fields, redaction, message, separator):
    """ comments fpr filter_datum """
    return re.sub(rf"({'|'.join(fields)})=[^{separator}]*", 
                  rf"\1={redaction}", message)
