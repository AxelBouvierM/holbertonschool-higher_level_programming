#!/usr/bin/python3
"""
script that adds all arguments to a Python list, and then save them to a file
"""
import sys
import os.path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

obj = []
for arg in sys.argv:
    if arg is not sys.argv[0]:
        obj.append(arg)
if os.path.exists("add_item.json") is False:
    save_to_json_file(obj, "add_item.json")
else:
    data = load_from_json_file("add_item.json")
    for i in obj:
        data.append(i)
    save_to_json_file(data, "add_item.json")
