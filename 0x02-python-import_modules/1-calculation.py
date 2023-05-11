#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    a = 10
    b = 5

    add_ = add(a, b)
    sub_ = sub(a, b)
    mul_ = mul(a, b)
    div_ = div(a, b)

    print("{:d} + {:d} = {:d}".format(a, b, add_))
    print("{:d} - {:d} = {:d}".format(a, b, sub_))
    print("{:d} * {:d} = {:d}".format(a, b, mul_))
    print("{:d} / {:d} = {:d}".format(a, b, div_))
