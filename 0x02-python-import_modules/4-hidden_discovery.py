#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    dir = dir()
    for i in range(len(dir)):
        if dir[i][:2] != "__":
            print("{}".format(dir[i]))
