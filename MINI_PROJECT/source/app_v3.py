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
                    try:
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
                        
                        save_list_to_json(product_dict, 'products.json')
                                
                        print("[PRODUCTS MENU]\n")
                        enumerate_list(product_dict)
                        time.sleep(1.5)
                    except Exception:
                            print("""!Incorrect Item Name or Price!
!No Changes Have Been Made!""")
                        
                
                elif product_menu_option == 4:
                    clear_screen()
                    print("[PRODUCTS MENU]\n")
                    enumerate_list(product_dict)
                    get_product_index = int(input("\nSelect Product Index: "))
                    product_dict.remove(product_dict[get_product_index])
                    
                    save_list_to_json(product_dict, 'products.json')
                    
                    clear_screen()
                    print("[PRODUCTS MENU]\n")
                    enumerate_list(product_dict)
                    time.sleep(1.5)
                
                else:
                    clear_screen()
                    print("!Incorrect Menu Choice!")
                    time.sleep(1)

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
                    print("[COURIERS LIST]\n")
                    enumerate_list(couriers_dict)
                    time.sleep(1.5)
                
                elif courier_menu_option == 2:
                    clear_screen()
                    try:
                        new_courier_name = str(input("Enter New Courier Name: "))
                        new_courier_phone = str(input("Enter New Courier Phone: "))
                        new_courier = {"name": new_courier_name, "phone": new_courier_phone}
                        couriers_dict.append(new_courier)
                        save_list_to_json(couriers_dict, 'couriers.json')
                        
                        clear_screen()
                        print("[COURIERS LIST]\n")
                        enumerate_list(couriers_dict)
                        time.sleep(1.5)
                        
                    except Exception:
                        print("""!Incorrect Courier Name or Phone!
!No Changes Have Been Made!""")
                    
                elif courier_menu_option == 3:
                    clear_screen()
                    print("[COURIERS LIST]\n")
                    enumerate_list(couriers_dict)
                    time.sleep(1.5)
                    try:
                        get_courier_index = int(input("\nSelect Courier Index: "))
                        new_courier_name = str(input("Enter New Courier Name: "))
                        new_courier_phone = str(input("Enter New Courier Phone: "))
                        for courier in couriers_dict[get_courier_index]:
                            if new_courier_name == "":
                                continue
                            else:
                                couriers_dict[get_courier_index]["name"] = new_courier_name
                            if new_courier_phone == "":
                                continue
                            else:
                                couriers_dict[get_courier_index]["phone"] = new_courier_phone
                        
                        save_list_to_json(couriers_dict, 'couriers.json')
                        
                        clear_screen()        
                        print("[COURIERS LIST]\n")
                        enumerate_list(couriers_dict)
                        time.sleep(1.5)
                    except Exception:
                            print("""!Incorrect Item Name or Price!
!No Changes Have Been Made!""")    
                    
                elif courier_menu_option == 4:
                    clear_screen()
                    print("[COURIERS LIST]\n")
                    enumerate_list(couriers_dict)
                    get_courier_index = int(input("\nSelect Courier Index: "))
                    couriers_dict.remove(couriers_dict[get_courier_index])
                    
                    save_list_to_json(couriers_dict, 'couriers.json')
                    
                    clear_screen()
                    print("[COURIERS LIST]\n")
                    enumerate_list(couriers_dict)
                    time.sleep(1.5)
                
                else:
                    clear_screen()
                    print("!Incorrect Menu Choice!")
                    time.sleep(1)    
    
#----------------Orders Menu------------------------------------------- 
      
        elif main_menu_option == 3:
            clear_screen()
            while True:    
                try:    
                    orders_menu_option = int(input("""
Orders Menu Options:

    0: Return to Main Menu
    1: Orders List
    2: Add New Order Details
    3: Update Existing Order Status
    4: Update Existing Order Details
    5: Delete Order

Please Select an Option: """))
                except Exception:
                    print("!Incorrect Option, Try Again!")
                           
                if orders_menu_option == 0:
                    clear_screen()
                    break
                
                elif orders_menu_option == 1:
                    clear_screen()
                    print("[ORDERS LIST]\n")
                    enumerate_list(orders_dict)
                    time.sleep(1.5)  
                
                elif orders_menu_option == 2:
                    clear_screen()
                    try:
                        new_customer_name = str(input("Enter New Customer Name: "))
                        new_customer_address = str(input("Enter New Customer Address: "))
                        new_customer_number = int(input("Enter New Customer Number: "))   
                        status = "Preparing"
                        items = ""
                        courier = ""
                        new_order = {"customer_name": new_customer_name,
                                     "customer_address": new_customer_address,
                                     "customer_phone": new_customer_number,
                                     "courier": courier,
                                     "status": status,
                                     "items": items
                                     }
                        orders_dict.append(new_order)
                        save_list_to_json(orders_dict, 'orders.json')
                        
                        # Adding multiple items code below only adds 1 even after multiple inputs:
                        clear_screen()
                        enumerate_list(product_dict)
                        for product in enumerate(product_dict):
                            get_product_index = int(input("\nSelect Products to Add: "))

                            should_continue = str(input("\nAdd More Items? (Y/N): "))
                            if should_continue == "Y":
                                items = ','.join(str(get_product_index))
                                continue
                            else:
                                break
                        
                        orders_dict[-1]["items"] = items
                        
                        enumerate_list(couriers_dict)
                        get_courier_index = int(input("Select Courier: "))
                        orders_dict[-1]["courier"] = get_courier_index
                        
                        save_list_to_json(orders_dict, 'orders.json')
                        
                        print("[ORDERS LIST]\n")
                        enumerate_list(orders_dict)
                        time.sleep(1.5)
                    
                    except Exception as e:
                        print(f"!A(n) error has occured: {e}")
                        
                    
                elif orders_menu_option == 3:
                    clear_screen()
                    print("[ORDERS LIST]\n")
                    enumerate_list(orders_dict)
                    time.sleep(0.5) 
                    
                    try:
                        get_order_index = int(input("\nSelect Order Index: "))
                        
                        enumerate_list(orders_status_list)
                        get_status_index = int(input("\nSelect Status: "))
                        
                        orders_dict[get_order_index]["status"] = orders_status_list[get_status_index]
                        
                        save_list_to_json(orders_dict, 'orders.json')
                        
                        print("[ORDERS LIST]\n")
                        enumerate_list(orders_dict)
                        time.sleep(1.5)                     
                        
                    except Exception as e:
                        print(f"You have made a(n) {e} error.")                 
                    
                    
                elif orders_menu_option == 4:
                    clear_screen()
                    print("[ORDERS LIST]\n")
                    enumerate_list(orders_dict)
                    time.sleep(0.5)
                    
                    try:
                        get_order_index = int(input("\nSelect Order Index: "))
                        new_customer_name = str(input("\nEnter New Customer Name: "))
                        new_customer_address = str(input("\nEnter New Customer Address: "))
                        new_customer_number = int(input("\nEnter New Customer Number: "))
                        enumerate_list(couriers_dict)
                        get_courier_index = int(input("\nSelect Courier: "))
                        enumerate_list(orders_status_list)
                        get_status_index = int(input("\nSelect Status: "))
                        enumerate_list(product_dict)
                        get_product_index = int(input("\nSelect Products to Add: "))
                         
                        for details in orders_dict[get_order_index]:
                            if new_customer_name == "":
                                continue
                            else:
                                orders_dict[get_order_index]["customer_name"] = new_customer_name
                            if new_customer_address == "":
                                continue
                            else:
                                orders_dict[get_order_index]["customer_address"] = new_customer_address
                            if new_customer_number == "":
                                continue
                            else:
                                orders_dict[get_order_index]["customer_phone"] = new_customer_number
                            if get_courier_index == "":
                                continue
                            else:
                                orders_dict[get_order_index]["courier"] = get_courier_index
                            if get_status_index == "":
                                continue
                            else:
                                orders_dict[get_order_index]["status"] = orders_status_list[get_status_index]
                            if get_product_index == "":
                                continue
                            else:
                                orders_dict[get_order_index]["items"] = get_product_index
                        
                        save_list_to_json(orders_dict, 'orders.json')
                        clear_screen()
                        print("[ORDERS LIST]\n")
                        enumerate_list(orders_dict)
                        time.sleep(1.5)
                    
                    except Exception as e:
                        print(f"You have made a(n) {e} error.")
                
                elif orders_menu_option == 5:
                    clear_screen()
                    print("[ORDERS LIST]\n")
                    enumerate_list(orders_dict)
                    time.sleep(0.5)
                    
                    try:
                        
                        get_order_index = int(input("Select Order to Delete: "))
                        orders_dict.remove(orders_dict[get_order_index])
                        save_list_to_json(orders_dict, 'orders.json')
                        
                        clear_screen()
                        print("[ORDERS LIST]\n")
                        enumerate_list(orders_dict)
                        time.sleep(1.5)
                        
                    except Exception:
                       print("""!Incorrect Index!
#!No Changes Have Been Made!""") 
                
                else:
                    clear_screen()
                    print("!Incorrect Menu Choice!")
                    time.sleep(1)
    
        else:
            clear_screen()
            print("!Incorrect Menu Choice!")
            time.sleep(1)
    
    
    
    
    
    
    
    
    
    
    
    except Exception as e:
        clear_screen()
        print(f"Theres an {e} error")
        time.sleep(1.5) 
        