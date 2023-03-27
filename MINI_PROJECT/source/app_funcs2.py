import json
from typing import List,Dict
import os

# Used to clear screen:
def clear_screen():
    os.system("cls")

# Generic function to load json files into useable variable:
def load_list_from_json(filename: str) -> List[Dict]:
    try:
        with open(filename, 'r') as f:
            file_data = json.loads(f.read())
        return file_data
    except FileNotFoundError as fnfe:
        print(f"Cannot find file: {fnfe}")

# orders = load_list_from_json('products.json')
# print(orders)

# Generic function to save edited variable into json file:
def save_list_to_json(list_to_save, filename):
    try:
        with open(filename, 'w') as f:
            json.dump(list_to_save, f, indent=4)
    except FileNotFoundError as fnfe:
        print(f"Cannot find file: {fnfe}")
        
def enumerate_list(some_list):
    for index, key in enumerate(some_list):
        print(index, key)