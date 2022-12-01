#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as cal
    import sys

    ops = ["+", "-", "*", "/"]
    op_exist = False
    arg = sys.argv
    length = len(arg) - 1
    if length < 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if length == 3:
        a = int(arg[1])
        b = int(arg[3])
        op = arg[2]
        if op in ops:
            op_exist = True
        if not op_exist:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        if op == ops[0]:
            print("{0} + {1} = {2}".format(a, b, cal.add(a, b)))
        if op == ops[1]:
            print("{0} - {1} = {2}".format(a, b, cal.sub(a, b)))
        if op == ops[2]:
            print("{0} * {1} = {2}".format(a, b, cal.mul(a, b)))
        if op == ops[3]:
            print("{0} / {1} = {2}".format(a, b, cal.div(a, b)))
