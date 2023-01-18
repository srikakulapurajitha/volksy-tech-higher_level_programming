#!/usr/bin/python3
"""read"""


def read_file(filename=""):
    """with"""
    with open(filename, "r", encoding="UTF-8") as f:
        print(f.read(), end="")
