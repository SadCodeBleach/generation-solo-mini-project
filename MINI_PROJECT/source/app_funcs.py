import os
import sys

def print_products(product_items):
    print("[PRODUCT ITEM LIST:]")                
    for item, price in product_items.item():
        print(item, price)
    print("\n")
    

# Generic write to list function:
def write_list_to_file(file_name, list_of_items):
    with open(file_name, "w") as f:
        for item in list_of_items:
            f.write(item) 
            

def clear_screen():
    os.system("cls")


