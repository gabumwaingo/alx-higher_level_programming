#!/usr/bin/python3
"""
Script that adds all argument to a list and saves it to a file
"""
import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

args = sys.argv
with open(add_item.json, 'a+', encoding='utf-8') as f:
    mylist = []
    mylist = args[1:]
    save_to_json_file(my_list, add_item.json)
    load_from_json_file(my_list, add_item.json)
