#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    print(str(a) + " + " + str(b) + " = " + str(add(a, b)))
    print(str(a) + " - " + str(b) + " = " + str(sub(a, b)))
    print(str(a) + " * " + str(b) + " = " + str(mul(a, b)))
    print(str(a) + " / " + str(b) + " = " + str(round(div(a, b))))
