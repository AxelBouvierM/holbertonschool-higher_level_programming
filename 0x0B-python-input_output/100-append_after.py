#!/usr/bin/python3
"""
function that inserts a line of text to a file
"""


def append_after(filename="", search_string="", new_string=""):
    """
    function that inserts a line of text to a file
    """
    string = ""
    with open(filename) as f:
        for i in f:
            string += i
            if search_string in i:
                string += new_string
    with open(filename, "w") as f:
        f.write(string)
