#!/usr/bin/python3
def safe_print_division(a, b):
    result = 0.0
    r2 = None
    try:
        result = a / b
    except(ZeroDivisionError):
        result = None
    finally:
        print("Inside Result = {}".format(result))
        return result
