#!/usr/bin/python3
"""Defines pascal_triangle function"""


def pascal_triangle(n):
    """returns a list of lists of integers representing
    the Pascal’s triangle of n"""

    if n <= 0:
        return([])

    listTriangle = [[1]]
    while len(listTriangle) < n:
        last = listTriangle[-1]
        add = [1]
        for i in range(len(last) - 1):
            add.append(last[i] + last[i + 1])
        add.append(1)
        listTriangle.append(add)
    return(listTriangle)
