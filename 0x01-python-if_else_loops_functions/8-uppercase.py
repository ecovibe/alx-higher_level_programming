#!/usr/bin/python3
# Author - Malau Malau Monday

def uppercase(s):
    for char in s:
        if ord(char) >= 97 and ord(char) <= 122:
            char = chr(ord(char) - 32)
            print(char, end=" ")  # Print horizontally with a space separator
            print() # Print a new line
