#!/usr/bin/python3
"""read"""


def number_of_lines(filename=""):
    """documents"""
    with open(filename, "r", encoding="UTF-8") as f:
        return len(list(f))
