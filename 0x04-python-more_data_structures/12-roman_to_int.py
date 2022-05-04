#!/usr/bin/python3
def roman_to_int(roman_string):
    Rnumber = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500}
    Rnumber["M"] = 1000
    num = 0

    if roman_string is not None and type(roman_string) == str:
        for i in range(len(roman_string)):
            if i < len(roman_string) - 1:
                if Rnumber[roman_string[i]] >= Rnumber[roman_string[i + 1]]:
                    num += Rnumber[roman_string[i]]
                else:
                    num -= Rnumber[roman_string[i]]
            else:
                num += Rnumber[roman_string[i]]
    return num
