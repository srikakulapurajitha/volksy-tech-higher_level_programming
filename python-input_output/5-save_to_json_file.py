#!/usr/bin/python3
"""read"""


import json


def save_to_json_file(my_obj, filename):
    """file open"""
    with open(filename, "w", encoding="UTF-8") as f:
        json.dump(my_obj, f)
