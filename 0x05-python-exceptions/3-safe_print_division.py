#!/usr/bin/python3
def safe_print_division(a, b):
    div = 0
    try:
        div = a / b
        return div
    except (ValueError, ZeroDivisionError):
        return None
    finally:
        if div != 0:
            print("Inside result: {}".format(div))
        else:
            print("Inside result: None")
