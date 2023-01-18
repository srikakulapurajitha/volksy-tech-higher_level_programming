#!/usr/bin/python3
"""read"""


def append_write(filename="", text=""):
    """appending"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
