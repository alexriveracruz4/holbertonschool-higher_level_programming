#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        if ord(letter) >= 93 and ord(letter) <= 122:
            letter = chr(ord(letter) - 32)
        print(letter, end="")
    print("")
