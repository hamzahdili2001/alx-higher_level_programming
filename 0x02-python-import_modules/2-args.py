#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    num_args = len(args)

    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        print("1 argument:")
    else:
        print("{:d} arguments:".format(num_args))
    for i, a in enumerate(args):
        print("{:d}: {:s}".format(i + 1, a))
