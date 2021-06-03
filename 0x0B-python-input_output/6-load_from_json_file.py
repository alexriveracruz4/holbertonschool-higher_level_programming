#!/usr/bin/python3
"""Defines load_from_json_file function"""
import json


def load_from_json_file(filename):
    """Creates onject from JSON  file"""
    with open(filename, "r", encoding="utf-8") as f:
        return(json.loads(f.read()))
