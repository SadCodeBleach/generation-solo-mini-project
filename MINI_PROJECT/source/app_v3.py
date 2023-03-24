import sys
import time
from app_funcs2 import *

product_dict = load_list_from_json('products.json')
orders_dict = load_list_from_json('orders.json')
couriers_dict = load_list_from_json('couriers.json')

orders_status_list = ["Preparing", "Out for Delivery", "Delivered"]

clear_screen()
while True:
    try:
        main_menu_option = int(input(""" 
Welcome to our cafe! 
                                 
    Main Menu Options:
    0: Exit
    1: Product Menu
    2: Couriers Menu
    3: Orders Menu
                                 
Please Select an Option: """)) 
        
        if main_menu_option == 0:
            save_list_to_json(product_dict, 'products.json')
            save_list_to_json(orders_dict, 'orders.json')
            save_list_to_json(couriers_dict, 'couriers.json')
            clear_screen()
            print("\nSee you again soon!\n")
            sys.exit()

#-------------Product Menu-------------------------------------------------    
   
        elif main_menu_option == 1:
            clear_screen()
            while True:                  
                try:    
                    product_menu_option = int(input("""
Product Menu Options:

    0: Return to Main Menu
    1: List Products
    2: Add a New Product
    3: Update Existing Product
    4: Delete a Product

Please Select an Option: """))
                    
                except Exception:
                    print("\nIncorrect Option, Try Again!")
                    
                if product_menu_option == 0:
                    clear_screen()
                    break
                
                elif product_menu_option == 1:
                    clear_screen()
                    print("[PRODUCTS MENU]\n")
                    enumerate_list(product_dict)
                    time.sleep(1.5)
                
                elif product_menu_option == 2:
                    clear_screen()
                    try:
                        new_product_name = str(input("Enter New Product Item: "))
                        new_product_price = float(input("Enter New Product Price: "))
                        new_item = {"name": new_product_name, "price": new_product_price}
                        product_dict.append(new_item)
                        save_list_to_json(product_dict, 'products.json')
                        
                        print("[PRODUCTS MENU]\n")
                        enumerate_list(product_dict)
                        time.sleep(1.5)
                        
                    except Exception:
                        print("""!Incorrect Item Name or Price!
!No Changes Have Been Made!""")
                
                elif product_menu_option == 3:
                    clear_screen()
                    print("[PRODUCTS MENU]\n")
                    enumerate_list(product_dict)
                    time.sleep(1.5)
                    
                    get_product_index = int(input("Select Product Index: "))
                    new_product_name = str(input("Enter New Product Item: "))
                    new_product_price = float(input("Enter New Product Price: "))
                    for product in product_dict[get_product_index]:
                        if new_product_name == "":
                            continue
                        else:
                            product_dict[get_product_index]["name"] = new_product_name
                        if new_product_price == "":
                            continue
                        else:
                            product_dict[get_product_index]["price"] = new_product_price
                            
                    print("[PRODUCTS MENU]\n")
                    enumerate_list(product_dict)
                    time.sleep(1.5)
                
                elif product_menu_option == 4:
                    clear_screen()
                    print("[PRODUCTS MENU]\n")
                    enumerate_list(product_dict)
                    get_product_index = int(input("\nSelect Product Index: "))
                    product_dict.remove(product_dict[get_product_index])
                    
                    clear_screen()
                    print("[PRODUCTS MENU]\n")
                    enumerate_list(product_dict)
                    time.sleep(1.5)

#---------Couriers Menu---------------------------------------------------

        elif main_menu_option == 2:
            clear_screen()
            while True:
                try:
                    courier_menu_option = int(input("""
Courier Menu Options:

    0: Return to Main Menu
    1: View Couriers List
    2: Add New Courier
    3: Update Existing Courier
    4: Remove Courier

Please Select an Option: """))
                except Exception as e:
                    clear_screen()
                    print(f"Oh no! a(n) {e} has occured!")
                    time.sleep(1.5)
                
                if courier_menu_option == 0:
                    clear_screen()
                    break
            
                elif courier_menu_option == 1:
                    clear_screen()
                    print("[COURIERS MENU]\n")
                    enumerate_list(couriers_dict)
                    time.sleep(1.5)
                    
                    
    
                    
                    
                    
                    
                
    
    
    
    
    
    
    
    
    
    
    
    
    
    except Exception as e:
        clear_screen()
        print(f"Theres an {e} error")
        time.sleep(1.5) 
        