#!/usr/bin/python3
"""read"""


import json


def load_from_json_file(filename):
    """opening file"""
    with open(filename, "r", encoding="UTF-8") as f:
        return json.load(f)
