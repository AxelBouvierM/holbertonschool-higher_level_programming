#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    for count in range(0, x):
        try:
            print(f"{my_list[count]}", end="")
            i += 1
        except (ValueError, TypeError, IndexError):
            break
    print()
    return (i)
