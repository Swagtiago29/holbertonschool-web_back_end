#!/usr/bin/env python3
import re

def filter_datum(fields: list, redaction: str, message:str, separator: str) -> str:
    return re.sub(rf"({'|'.join(fields)})=[^{separator}]*", rf"\1={redaction}", message)