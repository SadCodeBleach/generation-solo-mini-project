import sys
import time
from db_funcs import *
from app_funcs2 import *
from input_funcs import *

clear_screen()
while True: # Display Main Menu Options
    try:
        main_menu_option = int(input(""" 
Welcome to our cafe! 
                                 
    Main Menu Options:
    0: Exit
    1: Product Menu
    2: Couriers Menu
    3: Orders Menu
                                 
Please Select an Option: """)) 
        
        if main_menu_option == 0:   # Exits App
            clear_screen()
            print("\nSee you again soon!\n")
            time.sleep(1.5)
            sys.exit()

#-------------Product Menu-------------------------------------------------    
   
        elif main_menu_option == 1: # Shows Product Menu Options
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
                    
                if product_menu_option == 0: # Back to Main Menu
                    clear_screen()
                    break
                
                elif product_menu_option == 1: # Displays Product Items
                    clear_screen()
                    select_from_products_db()
                    time.sleep(1.5)
                
                elif product_menu_option == 2: # Adds New Products
                    clear_screen()
                    
                    try:
                        insert_into_product_db(get_name_input("Enter New Product Item: "), get_price_input("Enter New Product Price: "))
                        select_from_products_db()
                        time.sleep(1.5)    
                    except Exception:
                        print("""!Incorrect Item Name or Price!
!No Changes Have Been Made!""")
                
                elif product_menu_option == 3: # Update Existing Products
                    clear_screen()
                    select_from_products_db()
                    time.sleep(1.5)
                    
                    try:
                        update_product_db(get_id_input("\nSelect Product ID: "), get_name_input("Enter New Product Item: "), get_price_input("Enter New Product Price: "))
                        select_from_products_db()        
                        time.sleep(1.5)
                    except Exception as e:
                            print(f"""!Incorrect Item Name or Price!
!No Changes Have Been Made! 
Ex: {e}""")
                        
                
                elif product_menu_option == 4: # Deletes Products
                    clear_screen()
                    select_from_products_db()
                    remove_from_product_db(get_id_input("\nSelect Product ID: "))
                    
                    clear_screen()
                    select_from_products_db()
                    time.sleep(1.5)
                
                else: # Error Handling to Catch Invalid Menu Index
                    clear_screen()
                    print("!Incorrect Menu Choice!")
                    time.sleep(1)

#---------Couriers Menu---------------------------------------------------

        elif main_menu_option == 2: # Display Courier Menu Options
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
                
                if courier_menu_option == 0: # Back to Main Menu
                    clear_screen()
                    break
            
                elif courier_menu_option == 1: # Displays Couriers
                    clear_screen()
                    select_from_couriers_db()
                    time.sleep(1.5)
                
                elif courier_menu_option == 2: # Adds New Couriers
                    clear_screen()
                    
                    try:
                        insert_into_courier_db(get_name_input("Enter New Courier Name: "), get_phone_input("Enter New Courier Phone: "))
                        clear_screen()
                        select_from_couriers_db()
                        time.sleep(1.5)   
                    except Exception:
                        print("""!Incorrect Courier Name or Phone!
!No Changes Have Been Made!""")
                    
                elif courier_menu_option == 3: # Updates Existing Couriers
                    clear_screen()
                    select_from_couriers_db()
                    time.sleep(1.5)
                    
                    try:
                        update_courier_db(get_id_input("\nSelect Courier ID: "), get_name_input("Enter New Courier Name: "), get_phone_input("Enter New Courier Phone: "))
                        clear_screen()
                        select_from_couriers_db()
                        time.sleep(1.5)                      
                    except Exception as e:
                            print(f"""!Incorrect Item Name or Price!
!No Changes Have Been Made! {e}""")    
                    
                elif courier_menu_option == 4: # Deletes a Courier
                    clear_screen()
                    select_from_couriers_db()
                    remove_from_couriers_db(get_id_input("\nSelect Courier ID: "))
                    
                    clear_screen()
                    select_from_couriers_db()
                    time.sleep(1.5)
            
                else: # Error Handling to Catch Invalid Menu Index
                    clear_screen()
                    print("!Incorrect Menu Choice!")
                    time.sleep(1)    
    
#----------------Orders Menu------------------------------------------- 
      
        elif main_menu_option == 3: # Displays Orders Menu Options
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
                           
                if orders_menu_option == 0: # Back to Main Menu
                    clear_screen()
                    break
                
                elif orders_menu_option == 1: # Displays Current Orders
                    clear_screen()
                    select_from_orders_db()
                    time.sleep(1.5)  
                
                elif orders_menu_option == 2: # Adds New Order
                    clear_screen()
                    try:
                        new_customer_name = str(input("Enter New Customer Name: "))
                        new_customer_address = str(input("Enter New Customer Address: "))
                        new_customer_phone = str(input("Enter New Customer Number: "))
                        status = 1
                        select_from_couriers_db()
                        courier_id = int(input("Select Courier: "))
                        select_from_products_db()
                        
                        # Issue where multiple product inputs overwrites previous rather than adds to
                        while True:
                            product_item = int(input("\nSelect Product to Add: "))
                            should_continue = str(input("\nAdd More Items? (y/n): "))
                            if should_continue == "y":
                                insert_into_orders_db(new_customer_name, new_customer_address, new_customer_phone, courier_id, status, product_item)                 
                                continue
                            elif should_continue == "n":
                                insert_into_orders_db(new_customer_name, new_customer_address, new_customer_phone, courier_id, status, product_item)
                                break
                            else:
                                print("Incorrect choice!")
                        select_from_orders_db()
                        time.sleep(1.5)
                    
                    except Exception as e:
                        print(f"!A(n) error has occured: {e}")
                        
                    
                elif orders_menu_option == 3: # Update Order Status
                    clear_screen()
                    select_from_orders_db()
                    time.sleep(0.5) 
                    
                    try:
                        get_order_id = int(input("\nSelect Order ID: "))
                        select_from_status_db()
                        status_id = int(input("\nSelect Status: "))
                        update_order_status_db(get_order_id, status_id)
                        select_from_orders_db()
                        time.sleep(1.5)                     
                        
                    except Exception as e:
                        print(f"You have made a(n) {e} error.")                 
                    
                    
                elif orders_menu_option == 4: # Update Order Details
                    clear_screen()
                    select_from_orders_db()
                    time.sleep(0.5)
                    
                    try:
                        get_order_id = int(input("\nSelect Order Index: "))
                        new_customer_name = str(input("Enter New Customer Name: "))
                        new_customer_address = str(input("Enter New Customer Address: "))
                        new_customer_phone = str(input("Enter New Customer Number: ")) 
                        select_from_couriers_db()
                        new_courier_id = int(input("Select Courier: "))
                        select_from_products_db()
                        new_product_item = int(input("\nSelect Product to Add: "))
    
                        if new_customer_name == "":
                            print('Entry empty, no updates made.')
                            continue
                        else:
                            customer_name = new_customer_name
                        if new_customer_address == "":
                            print('Entry empty, no updates made.')
                            continue
                        else:
                            customer_address = new_customer_address
                        if new_customer_phone == "":
                            print('Entry empty, no updates made.')
                            continue
                        else:
                            customer_phone = new_customer_phone
                        if new_courier_id == "":
                            print('Entry empty, no updates made.')
                            continue
                        else:
                            courier_id = new_courier_id
                        if new_product_item == "":
                            print('Entry empty, no updates made.')
                            continue
                        else:
                            product_item = new_product_item
                        
                        update_orders_db(customer_name, customer_address, customer_phone, courier_id, product_item, get_order_id)
                        
                        clear_screen()
                        select_from_orders_db()
                        time.sleep(1.5)
                    
                    except Exception as e:
                        print(f"You have made a(n) {e} error.")
                
                elif orders_menu_option == 5: # Delete an Order
                    clear_screen()
                    select_from_orders_db()
                    time.sleep(0.5)
                    
                    try:
                        remove_from_orders_db(get_id_input("\nSelect Order ID: "))
                        clear_screen()
                        select_from_orders_db()
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
        