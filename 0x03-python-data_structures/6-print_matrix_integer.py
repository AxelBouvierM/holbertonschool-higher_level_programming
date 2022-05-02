#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for x in i:
            print(f"{x}", end="")
            if x != i[len(i) - 1]:
                print(" ", end="")
        print()
