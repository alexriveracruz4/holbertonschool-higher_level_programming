#!/usr/bin/python3
"""Defines save_to_json_file function"""
import json


def save_to_json_file(my_obj, filename):
    """Write object to text file using Json representation"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
