#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) == 1:
        print("0")
    else:
        num = 0
        for i in range(1, len(argv)):
            num += int(argv[i])
        print(num)
