import json
#----------------------------------------------------------------------------------
product_items = {
    "Americano": 3.00,
    "Latte": 4.20,
    "Mocha": 4.50,
    "Iced Coffee": 4.25,
    "English Breakfast": 4.50,
    "Green Tea": 4.50,
    "Croissant": 2.20,
    "Muffin": 2.50,
    "Pastry": 3.50
}

# Used to open product.json file and print to screen:
def print_products_json():
    print("[PRODUCT ITEM LIST:]")
    try:    
        with open('products.json', 'r') as f:
            product_data = json.load(f)
            print(product_data)
    except FileNotFoundError as fnfe:
        print(f"Cannot find file: {fnfe}")

# # Used to overwrite product.json file and print to screen:
def write_products_json(product_items):
    print("[PRODUCT ITEM LIST:]")
    try:
        with open('products.json', 'w+') as f:
            json.dump(product_items, f)
            print(product_items)
    except FileNotFoundError as fnfe:
        print(f"Cannot find file: {fnfe}")


    

#--------------------------------------------------------------------------------
orders_menu = [
    {
    "customer_name:": "John",
    "customer_address:": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
    "customer_phone:": "0789887334",
    "courier:": 2,
    "status:": "Preparing"
    }
        ]

def print_orders_json():
    try:    
        with open('orders.json', 'r') as f:
            orders_data = json.load(f)
            print(orders_data)
    except FileNotFoundError as fnfe:
        print(f"Cannot find file: {fnfe}")
        

def write_orders_json(orders_menu):
    try:
        with open('orders.json', 'w+') as f:
            json.dump(orders_menu, f)
            print(orders_menu)
    except FileNotFoundError as fnfe:
        print(f"Cannot find file: {fnfe}")

# #----------------------------------------------------------------------------------
couriers_list = {
    "Jack": "07700127577",
    "Claire": "07545739553",
    "Maddie": "07265650318"
}

def write_couriers_list():
    try:
        with open('couriers.json', 'w+') as f:
            json.dump(couriers_list, f)
    except FileNotFoundError as fnfe:
        print(f"Cannot find file: {fnfe}")

def print_couriers_list():
    try:    
        with open('couriers.json', 'r') as f:
            couriers_data = json.load(f)
            print(couriers_data)
    except FileNotFoundError as fnfe:
        print(f"Cannot find file: {fnfe}")