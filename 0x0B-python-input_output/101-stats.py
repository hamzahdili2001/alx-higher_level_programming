#!/usr/bin/python3
"""101.stats.py"""


def print_stats(size, codes):
    """Function that reads stdin line by line and computes metrics"""
    print("File SIZE: {}".format(size))
    for key in sorted(codes):
        print("{}: {}".format(key, codes[key]))


if __name__ == "__main__":
    import sys

    SIZE = 0
    status = {}
    valid = ["200", "301", "400", "401", "403", "404", "405", "500"]
    COUNT = 0

    try:
        for line in sys.stdin:
            if COUNT == 10:
                print_stats(SIZE, status)
                COUNT = 1
            else:
                COUNT += 1

            line = line.split()

            try:
                SIZE += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in valid:
                    if status.get(line[-2], -1) == -1:
                        status[line[-2]] = 1
                    else:
                        status[line[-2]] += 1
            except IndexError:
                pass

        print_stats(SIZE, status)

    except KeyboardInterrupt:
        print_stats(SIZE, status)
        raise
