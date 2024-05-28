#!/usr/bin/python3
import sys
import os

# Import the helper functions
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Load existing items from the file if it exists, otherwise start with an empty list
if os.path.exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

# Add new items from command-line arguments using extend
items.extend(sys.argv[1:])

# Save the updated list back to the file
save_to_json_file(items, filename)
