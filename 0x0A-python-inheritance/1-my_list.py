#!/usr/bin/python3
"""Define class MyList"""


class MyList(list):
    """Subclass of list"""
    def __init__(self):
        """Initialize object"""
        super().__init__()

    def print_sorted(self):
        """Prints sorted list"""
        print(sorted(self))
