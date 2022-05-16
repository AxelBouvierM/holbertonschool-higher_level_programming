#!/usr/bin/python3
def safe_print_division(a, b):
    div = 0
    try:
        div = a / b
        return div
    except (ValueError, TypeError, ZeroDivisionError):
        return None
    finally:
        if div != 0:
            print(f"Inside result: {div}")
        else:
            print("Inside result: None")
