#!/usr/bin/python3
def uppercase(str):
    upper = ""
    for i in str:
        if ord('a') <= ord(i) <= ord('z'):
            upper += chr(ord(i) - 32)
        else:
            upper += i
    print("{:s}".format(upper))
