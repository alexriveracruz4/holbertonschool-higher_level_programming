#!/usr/bin/python3
"""Defines append_write function"""


def append_write(filename="", text=""):
    """Appends a string to text file and return num of char"""
    with open(filename, "a", encoding="utf-8") as f:
        return(f.write(text))
