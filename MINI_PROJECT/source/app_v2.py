
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
orders_menu = [{
    "customer_name:": "John",
    "customer_address:": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
    "customer_phone:": "0789887334",
    "status:": "Preparing"
}]

while True:
    try:
        main_menu_option = int(input(""" 
Welcome to our cafe! 
                                 
    Main Menu Options:
    0: Exit
    1: Product Menu
    2: Orders Menu
    3: Couriers Menu
                                 
Please Select an Option: """)) 
        
        if main_menu_option == 0:
            print("See you again soon!")
            exit
            break
        
#-------------Product Menu-------------------------------------------------    
   
        elif main_menu_option == 1:
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
                    print("!Incorrect Option, Try Again!")
                    
                if product_menu_option == 0:
                    break
                
                elif product_menu_option == 1:
                    print("[PRODUCT ITEM LIST:]")                
                    for item, price in product_items.items():
                        print(item, price)
                
                elif product_menu_option == 2:
                    try:
                        new_product_name = str(input("Enter New Product Item: "))
                        new_product_price = float(input("Enter New Product Price: "))
                        new_item = {new_product_name: new_product_price}
                        product_items.update(new_item)
                        print("\n")
                        print("[PRODUCT ITEM LIST:]")
                        for item, price in product_items.items():
                            print(item, price)
                    except Exception:
                        print("""!Incorrect Item Name or Price!
!No Changes Have Been Made!""")
                
                elif product_menu_option == 3:
                    print("\n")
                    print("[PRODUCT ITEM LIST:]")                
                    for item, price in product_items.items():
                        print(item, price)
                    print("\n")
                    
                    try:
                        current_product_item = str(input("Insert Current Product Item: "))
                        new_product_name = str(input("Enter New Product Item: "))
                        new_product_price = float(input("Enter New Product Price: "))
                        new_item = {new_product_name: new_product_price}
                        del product_items[current_product_item]
                        product_items.update(new_item)
                        print("[PRODUCT ITEM LIST:]")                
                        for item, price in product_items.items():
                            print(item, price)
                    except Exception:
                        print("""!Incorrect Item Name or Price!
!No Changes Have Been Made!""")
                
                elif product_menu_option == 4:
                    print("[PRODUCT ITEM LIST:]")                
                    for item, price in product_items.items():
                        print(item, price)
                    print("\n")
                    try:
                        current_product_item = str(input("Select Product to Delete: "))
                        del product_items[current_product_item]
                        for item, price in product_items.items():
                            print(item, price)
                        print("\n")
                    except NameError:
                        print("""!Item Does Not Exist!
!No Changes Have Been Made!""")
                        
#----------------Orders Menu------------------------------------------- 
      
        elif main_menu_option == 2:
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
                    break
                
                elif orders_menu_option == 1:
                    print("[ORDERS LIST:]")                
                    print(orders_menu)
                
                elif orders_menu_option == 2:
                    try:
                        new_customer_name = str(input("Enter New Customer Name: "))
                        new_customer_address = str(input("Enter New Customer Address: "))
                        new_customer_number = int(input("Enter New Customer Number: "))
                        status = "Preparing"
                        new_order = {"customer_name:": new_customer_name, "customer_address:": new_customer_address, "customer_phone:": new_customer_number, "status:": status}
                        orders_menu.append(new_order)
                        for order in orders_menu:
                            print(order)
                    except Exception as e:
                        print(f"You have made a(n) {e} error.")
                
                elif orders_menu_option == 3:
                    for index, order in enumerate(orders_menu):
                        print(index, order)
                    try:
                        order_index = int(input("Select Order Index: "))
                        if order_index == index:
                            order_index_2 = int(input("""Choose Update Status:
                                                      
1: Preparing
2: Out for Delivery
3: Delivered

Please Select an Update Option: """))
                            if order_index_2 == 1:
                                status_update = "Preparing"
                            elif order_index_2 == 2:
                                status_update = "Out for Delivery"
                            elif order_index_2 == 3:
                                status_update = "Delivered"
                            else:
                                print("!Incorrect Choice!")
                            orders_menu[index]["status:"] = status_update
                            print(orders_menu)
                        else:
                            print("!Invalid Index!")
                    except Exception:
                        print("""!Index Does Not Exist!
!No Changes Have Been Made!""")
                
                elif orders_menu_option == 4:
                    for index, order in enumerate(orders_menu):
                        print(index, order)
                    try:
                        order_index = int(input("Select Order Index: "))
                        if order_index == index:
                            for key, value in orders_menu[index].items():
                                print(key, value)
                            customer_name_update = str(input("Update customer name: "))
                            if customer_name_update == "":
                                print("Customer name has not been updated.")    
                            else:   
                                orders_menu[index]["customer_name:"] = customer_name_update
                            customer_address_update = str(input("Update customer address: "))
                            if customer_address_update == "":
                                print("Customer address has not been updated.")    
                            else:   
                                orders_menu[index]["customer_address:"] = customer_address_update
                            customer_phone_update = int(input("Update customer phone number: "))
                            if customer_phone_update == "":
                                print("Customer phone number has not been updated.")    
                            else:   
                                orders_menu[index]["customer_phone:"] = customer_phone_update
                            order_index_2 = int(input("""Choose Update Status:
                                                      
1: Preparing
2: Out for Delivery
3: Delivered

Please Select an Update Option: """))
                            if order_index_2 == 1:
                                status_update = "Preparing"
                            elif order_index_2 == 2:
                                status_update = "Out for Delivery"
                            elif order_index_2 == 3:
                                status_update = "Delivered"
                            else:
                                print("!Incorrect Choice!")
                            orders_menu[index]["status:"] = status_update
                        print(orders_menu)
                    except Exception as e:
                        print(f"Oh no! a(n) {e} has occured!")
                
                elif orders_menu_option == 5:
                    try:
                        for index, order in enumerate(orders_menu):
                            print(index, order)
                        order_index = int(input("Select Order Index: "))
                        if order_index == index:
                            del orders_menu[index]
                            print(orders_menu)      
                        else:
                            print("Incorrect index selection.")
                    except Exception:
                        print("""!Index Does Not Exist!
!No Changes Have Been Made!""")
                           
                    
               
                        
                    
                        
                    
                
                            
                        
                        
                    
                
                
    except Exception:
        print("!Incorrect Option, Try Again!")
        
    
