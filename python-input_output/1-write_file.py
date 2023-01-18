#!/usr/bin/python3
"""read"""


def write_file(filename="", text=""):
    """documents"""
    with open(filename, "w", encoding="UTF-8") as f:
        return f.write(text)
