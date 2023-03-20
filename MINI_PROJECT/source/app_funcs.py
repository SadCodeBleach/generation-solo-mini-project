import os

# Used to clear the screen:
def clear_screen():
    os.system("cls")

# Used to print tupled list from the product dictionary:    
def print_products_dict(product_items):
    print("\n")
    print("[PRODUCT ITEM LIST:]")
    for item, price in product_items.items():
        print(item, price)

# Used to enumerate and print orders dictionary:
def enumerate_orders_dict(orders_menu):
    print("[ORDERS LIST:]")
    for index, order in enumerate(orders_menu):
        print(index, order)

# Used to print couriers.txt file:   
def print_couriers_list():
    print("\n[COURIERS LIST:]")
    courier_file = open('couriers.txt', 'r')
    print(courier_file.read())  
    courier_file.close() 

# Used to append new couriers to couriers.txt:    
def write_couriers_list(new_courier):
    courier_file = open('couriers.txt', 'a+')
    courier_file.write("\n")
    courier_file.write(new_courier)
    courier_file.close() 

# Used to enumerate through couriers.txt file and show index of each courier:    
def enumerate_courier_file():
    print("\n[COURIERS LIST:]")
    courier_file = open('couriers.txt', 'r')
    courier_list = courier_file.readlines()
    for index, courier in enumerate(courier_list):
        print(index, courier)



