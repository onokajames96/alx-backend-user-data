#!/usr/bin/env python3
import re


def filter_datum(fields, redaction, message, separator):
    reg_pattern = (
        r'(?<=^|{})'
        '(?:{})'
        '(?={}|$)'
    ).format(separator, '|'.join(fields), separator)
    return re.sub(reg_pattern, redaction, message)
