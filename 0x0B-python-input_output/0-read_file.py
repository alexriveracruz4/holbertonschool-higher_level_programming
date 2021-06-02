#!/usr/bin/python3
"""Defines read_file function"""


def read_file(filename=""):
    """Function to read file"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
