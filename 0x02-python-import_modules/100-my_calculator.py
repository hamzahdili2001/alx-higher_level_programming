#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    ops = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div
    }
    argc = len(sys.argv)
    if argc != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    op = sys.argv[2]
    b = int(sys.argv[3])

    if op not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    result = ops[op](a, b)

    print("{:d} {:s} {:d} = {:d}".format(a, op, b, result))
