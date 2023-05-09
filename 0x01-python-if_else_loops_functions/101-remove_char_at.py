#!/usr/bin/python3
def remove_char_at(str, n):
    string = ""
    i = 0
    for j in str:
        if i != n:
            string += str[i]
        i += 1
    return string
