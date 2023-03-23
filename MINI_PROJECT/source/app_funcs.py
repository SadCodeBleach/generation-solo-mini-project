import os
import json


# Used to clear the screen:
def clear_screen():
    os.system("cls")

#-----------------Product List Funcs----------------------------------------------------    
# Used to open product.json file and print to screen:
def print_products_json():
    clear_screen()
    print("[PRODUCT ITEM LIST]")
    try:    
        with open('products.json', 'r') as f:
            product_data = json.load(f)
            print(product_data)
    except FileNotFoundError as fnfe:
        print(f"Cannot find file: {fnfe}")

# Used to overwrite product.json file and print to screen:
def write_products_json(product_items):
    clear_screen()
    print("[PRODUCT ITEM LIST]")
    try:
        with open('products.json', 'w+') as f:
            json.dump(product_items, f, indent=4)
            print(product_items)
    except FileNotFoundError as fnfe:
        print(f"Cannot find file: {fnfe}")
        
        
 #-----------------Order List Funcs----------------------------------------------------         
 # Used to open orders.json file and print to screen:   
def print_orders_json():
    try:    
        with open('orders.json', 'r') as f:
            orders_data = json.load(f)
        print("[ORDERS LIST]")
        for index, order in enumerate(orders_data):
            print(index, order)
    except FileNotFoundError as fnfe:
        print(f"Cannot find file: {fnfe}")
        
# Used to overwrite orders.json file and print to screen:
def write_orders_json(orders_menu):
    try:
        with open('orders.json', 'w') as f:
            json.dump(orders_menu, f, indent=4)
        print("[ORDERS LIST]")
        for index, order in enumerate(orders_menu):
            print(index, order)
    except FileNotFoundError as fnfe:
        print(f"Cannot find file: {fnfe}")
 
        
def enum_orders_json():
    try:    
        with open('orders.json', 'r') as f:
            orders_data = json.load(f)
        print("[ORDERS LIST]")
        for index, order in enumerate(orders_data):
            print(index, order)
    except FileNotFoundError as fnfe:
        print(f"Cannot find file: {fnfe}")
    
        
#-------------------------------------------------------------------------------------

def enum_couriers_json():
    try:    
        with open('couriers.json', 'r') as f:
            couriers_data = json.load(f)
        print("[COURIERS LIST]")
        for index, courier in enumerate(couriers_data):
            print(index, courier)
    except FileNotFoundError as fnfe:
        print(f"Cannot find file: {fnfe}")

def print_couriers_json():
    clear_screen()
    try:    
        with open('couriers.json', 'r') as f:
            couriers_data = json.load(f)
        print("[COURIERS LIST]")
        print(couriers_data)
    except FileNotFoundError as fnfe:
        print(f"Cannot find file: {fnfe}")
        

def write_couriers_json(couriers_list):
    try:
        with open('couriers.json', 'w+') as f:
            json.dump(couriers_list, f, indent=4)
    except FileNotFoundError as fnfe:
        print(f"Cannot find file: {fnfe}")



#-----------------------------------------------------------------------------------
# # Used to print tupled list from the product dictionary:    
# def print_products_dict(product_items):
#     print("\n")
#     print("[PRODUCT ITEM LIST:]")
#     for item, price in product_items.items():
#         print(item, price)

# # Used to enumerate and print orders dictionary:
# def enumerate_orders_dict(orders_menu):
#     print("[ORDERS LIST:]")
#     for index, order in enumerate(orders_menu):
#         print(index, order)

# # Used to print couriers.txt file:   
# def print_couriers_list():
#     print("\n[COURIERS LIST:]")
#     courier_file = open('couriers.txt', 'r')
#     print(courier_file.read())  
#     courier_file.close() 

# # Used to append new couriers to couriers.txt:    
# def write_couriers_list(new_courier):
#     courier_file = open('couriers.txt', 'a+')
#     courier_file.write("\n")
#     courier_file.write(new_courier)
#     courier_file.close() 

# # Used to enumerate through couriers.txt file and show index of each courier:    
# def enumerate_courier_file():
#     print("\n[COURIERS LIST:]")
#     courier_file = open('couriers.txt', 'r')
#     courier_list = courier_file.readlines()
#     for index, courier in enumerate(courier_list):
#         print(index, courier)



