#!/usr/bin/python3
"""
function that returns an object represented by a JSON string
"""


def from_json_string(my_str):
    """
    function that returns an object represented by a JSON string
    """
    import json
    return json.loads(my_str)
