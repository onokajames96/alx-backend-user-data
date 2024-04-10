#!/usr/bin/env python3
"""Regex Authentification"""
import re


def filter_datum(fields, redaction, message, separator):
    """Define filter datum function"""
    reg_pattern = (
        r'(?<=^|{})'
        '(?:{})'
        '(?={}|$)'
    ).format(separator, '|'.join(fields), separator)
    return re.sub(reg_pattern, redaction, message)
