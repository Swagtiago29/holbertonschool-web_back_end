#!/usr/bin/env python3
import re

def filter_datum(fields: list, redaction: str, message:str, separator: str) -> str:
    