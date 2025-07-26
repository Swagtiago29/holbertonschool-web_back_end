#!/usr/bin/env python3
"""Task 1 - Log formatter"""
import re
from typing import List
import logging
import os
import mysql.connector
from mysql.connector.connection import MySQLConnection
import bcrypt

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str],
                 redaction: str, message: str, separator: str) -> str:
    """Redacts values of specified fields in a log message."""
    return re.sub(
        rf"({'|'.join(map(re.escape, fields))})=.*?{re.escape(separator)}",
        rf"\1={redaction}{separator}", message)


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Formats the LogRecord"""
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.getMessage(), self.SEPARATOR)
        return super().format(record)


def get_logger() -> logging.Logger:
    """Creates and configures a logger for user data"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(fields=PII_FIELDS))
    logger.addHandler(stream_handler)
    return logger


def get_db() -> MySQLConnection:
    """
    Establishes and returns a connection to the MySQL database using
    environment variables.

    Environment Variables:
        PERSONAL_DATA_DB_USERNAME: Database username (default: 'root').
        PERSONAL_DATA_DB_PASSWORD: Database password (default: '').
        PERSONAL_DATA_DB_HOST: Database host (default: 'localhost').
        PERSONAL_DATA_DB_NAME: Name of the database (no default — must be set)

    Returns:
        A MySQLConnection object. The caller is responsible for closing the
        connection using db.close() when done.
    """
    return mysql.connector.connect(
        user=os.getenv("PERSONAL_DATA_DB_USERNAME", "root"),
        password=os.getenv("PERSONAL_DATA_DB_PASSWORD", ""),
        host=os.getenv("PERSONAL_DATA_DB_HOST", "localhost"),
        database=os.getenv("PERSONAL_DATA_DB_NAME"),
    )


def main():
    """Main function that retrieves user data and logs it with sensitive
    fields redacted."""
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")

    field_names = [i[0] for i in cursor.description]
    logger = get_logger()

    for row in cursor:
        message = "; ".join(f"{field}={value}" for field,
                            value in zip(field_names, row)) + ";"
        logger.info(message)

    cursor.close()
    db.close()
def hash_password(password: str) -> bytes:
    """Returns the hashed password in bytes"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
if __name__ == "__main__":
    main()
