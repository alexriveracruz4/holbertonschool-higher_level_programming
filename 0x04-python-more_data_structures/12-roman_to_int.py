#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str) is False or roman_string is None:
        return(0)

    value = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    for i in roman_string:
        if i not in value.keys():
            return(0)

    list1 = [value[i] for i in roman_string]
    num = 0

    if len(list1) == 1:
        return(list1[0])

    for j in range(len(list1) - 1):
        if list1[j] >= list1[j + 1]:
            num += list1[j]
            if j is (len(list1) - 2):
                num += list1[j + 1]
        else:
            num += list1[j + 1] - list1[j]
    return(num)
