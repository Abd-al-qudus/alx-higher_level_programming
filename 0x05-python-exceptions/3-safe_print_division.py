#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = float(a / b)
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result if result else None))
    return result
