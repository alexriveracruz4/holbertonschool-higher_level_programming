#!/usr/bin/python3
"""Defines write_file function"""


def write_file(filename="", text=""):
    """Write string to a text file  and return num of chars"""
    with open(filename, "w", encoding="utf-8") as f:
        return(f.write(text))
