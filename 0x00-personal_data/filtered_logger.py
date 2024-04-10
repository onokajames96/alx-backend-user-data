#!/usr/bin/env python3
"""Regex Authentification"""
import re


def filter_datum(fields, redaction, message, separator):
    """Define filter datum function"""
    for field in fields:
        message = re.sub(f'{field}=(.*?){separator}',
                        f'{field}={redaction}{separator}', message)

        return message
