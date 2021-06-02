#!/usr/bin/python3
"""Defines to_json_string function"""
import json


def to_json_string(my_obj):
    """Return the JSON representation of my_obj"""
    return(json.dumps(my_obj))
