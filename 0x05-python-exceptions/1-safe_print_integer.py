#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print(f"{value:d}")
    except (TypeError):
        return False
    else:
        return True
