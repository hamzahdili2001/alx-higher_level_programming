#!/usr/bin/python3
"""a script that adds all arguments
to a Python list, and then save them to a file:"""


import sys
import os.path as op


saving = __import__('5-save_to_json_file').save_to_json_file
loading = __import__('6-load_from_json_file').load_from_json_file

lst = []

item = "add_item.json"
if op.exists(item):
    lst = loading(item)

for i in sys.argv[1:]:
    lst.append(i)

saving(lst, item)
