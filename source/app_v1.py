product_menu_options = {
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

orders_menu_options = [{
    "customer_name:": "John",
    "customer_address:": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
    "customer_phone:": "0789887334",
    "status:": "Preparing"
}]

def main_menu():
    menu_option = int(input("Welcome to Our Cafe! \n\nMain Menu Options: \n0: Exit \n1: Product Menu \n2: Orders Menu \n\nSelect an Option: "))
    if menu_option == 0:
        exit
    elif menu_option == 1:
        product_menu_option = int(input("Product Menu Options: \n\n0: Return to Main Menu \n1: Product List \n2: Create New Product \n3: Update Existing Product \n4: Delete Product \n\nSelect an Option: "))
        if product_menu_option == 0:
            main_menu()
        elif product_menu_option == 1:
            print(product_menu_options)
            main_menu() 
        elif product_menu_option == 2:
            new_product_name = input("Enter New Product: ")
            new_product_price = float(input("Enter New Product Price: "))
            new_product = {new_product_name: new_product_price}
            product_menu_options.update(new_product)
            print(product_menu_options)
            main_menu()
        elif product_menu_option == 3:
            for product, price in product_menu_options.items():
                print(product, price)
            current_product_name = (input("Select Product Name: "))
            new_product_name = input("Enter New Product Name: ")
            new_product_price = float(input("Enter New Product Price: "))
            del product_menu_options[current_product_name]
            new_product = {new_product_name: new_product_price}
            product_menu_options.update(new_product)
            print(product_menu_options)
            main_menu()
        elif product_menu_option == 4:
            for product, price in product_menu_options.items():
                print(product, price)
            current_product_name = (input("Select Product To Delete: "))
            del product_menu_options[current_product_name]
            print(product_menu_options)
            main_menu()
        else:
            print("Incorrect menu option, try again.")
            main_menu()
    elif menu_option == 2:
        def orders():
            orders_menu_option = int(input("Orders Menu Options: \n\n0: Return To Main Menu \n1: Orders List \n2: Add New Order Details \n3: Update Existing Order Status \n4: Update Existing Order Details \n5: Delete Order \n\nSelect an Option: "))
            if orders_menu_option == 0:
                main_menu()
            elif orders_menu_option == 1:
                print(orders_menu_options)
                orders()
            elif orders_menu_option == 2:
                new_customer_name = str(input("Enter New Customer Name: "))
                new_customer_address = str(input("Enter New Customer Address: "))
                new_customer_number = int(input("Enter New Customer Number: "))
                status = "Preparing"
                new_order = {"customer_name:": new_customer_name, "customer_address:": new_customer_address, "customer_phone:": new_customer_number, "status:": status}
                orders_menu_options.append(new_order)
                for order in orders_menu_options:
                    print(order)
                orders()
            elif orders_menu_option == 3:
                for index, order in enumerate(orders_menu_options):
                    print(index, order)
                order_index = int(input("Select Order Index: "))
                status_update = str(input("Update Order Status: "))
                if order_index == index:
                    orders_menu_options[index]["status:"] = status_update
                    print(orders_menu_options)
                orders()
            elif orders_menu_option == 4:
                for index, order in enumerate(orders_menu_options):
                    print(index, order)
                order_index = int(input("Select Order Index: "))
                if order_index == index:
                    for key, value in orders_menu_options[index].items():
                        print(key, value)
                    customer_name_update = str(input("Update customer name: "))
                    if customer_name_update == "":
                        print("Customer name has not been updated.")    
                    else:   
                        orders_menu_options[index]["customer_name:"] = customer_name_update
                    customer_address_update = str(input("Update customer address: "))
                    if customer_address_update == "":
                        print("Customer address has not been updated.")    
                    else:   
                        orders_menu_options[index]["customer_address:"] = customer_address_update
                    customer_phone_update = int(input("Update customer phone number: "))
                    if customer_phone_update == "":
                        print("Customer phone number has not been updated.")    
                    else:   
                        orders_menu_options[index]["customer_phone:"] = customer_phone_update
                    status_update = str(input("Update Order Status: "))
                    if status_update == "":
                        print("Order status has not been updated.")    
                    else:   
                        orders_menu_options[index]["status:"] = status_update
                print(orders_menu_options)
                orders() 
            elif orders_menu_option == 5:
                for index, order in enumerate(orders_menu_options):
                    print(index, order)
                order_index = int(input("Select Order Index: "))
                if order_index == index:
                    del orders_menu_options[index]
                    print(orders_menu_options)
                    orders()
                else:
                    print("Incorrect index selection.")
                    orders()
    
            
        
        orders()         
                
main_menu()