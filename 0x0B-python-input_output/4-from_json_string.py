#!/usr/bin/python3
"""Defines from_json_strings function"""
import json


def from_json_string(my_str):
    """Returns object represented by JSON string"""
    return(json.loads(my_str))
