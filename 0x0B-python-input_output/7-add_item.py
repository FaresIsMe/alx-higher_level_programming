#!/usr/bin/python3
"""
7. Load, add, save
"""
import sys
import json
import os.path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

file_name = "add_item.json"
j_list = []

if os.path.exists(file_name):
    j_list = load_from_json_file(file_name)

for i in range(1, len(sys.argv)):
    j_list.append(sys.argv[i])

save_to_json_file(j_list, file_name)
