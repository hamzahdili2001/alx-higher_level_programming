#!/usr/bin/python3
for i in range(100):
    if i < 10:
        print(f"{i:02d}", end=', ')
    elif i != 99 and i >= 10:
        print(f"{i:d}", end=", ")
    else:
        print(f"{i:d}")
