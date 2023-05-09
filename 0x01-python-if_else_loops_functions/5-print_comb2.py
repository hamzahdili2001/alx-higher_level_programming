#!/usr/bin/python3
for i in range(100):
    if i < 10:
        print("{:02d}".format(i), end=', ')
    elif i != 99 and i >= 10:
        print("{:d}".format(i), end=", ")
    else:
        print("{:d}".format(i))
