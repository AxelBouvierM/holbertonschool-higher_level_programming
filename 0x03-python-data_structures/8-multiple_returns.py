#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        sentence[0] = None
    lenght = len(sentence)
    first_letter = sentence[0]
    return (lenght, first_letter)
