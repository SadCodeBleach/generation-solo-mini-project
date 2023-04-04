import pymysql
import os
from dotenv import load_dotenv

load_dotenv()
host_name = os.environ.get("mysql_host")
database_name = os.environ.get("mysql_db")
user_name = os.environ.get("mysql_user")
user_password = os.environ.get("mysql_pass")

# ---------Insert in DB funcs-----------------------------------

def insert_into_courier_db(courier_name, courier_phone):
    try:
        with pymysql.connect(
            host = host_name,
            database = database_name,
            user = user_name,
            password = user_password    
        ) as connection:
            cursor = connection.cursor()
            sql = "INSERT INTO couriers (courier_name, courier_phone) VALUES (%s,%s)"
            cursor.execute(sql, ({courier_name}, {courier_phone}))
            connection.commit()
            cursor.close()
    except Exception as e:
        print(f'Failed to open connection: {e}')


def insert_into_product_db(product_name, product_price):
    try:
        with pymysql.connect(
            host = host_name,
            database = database_name,
            user = user_name,
            password = user_password    
        ) as connection:
            cursor = connection.cursor()
            sql = "INSERT INTO products (product_name, product_price) VALUES (%s,%s)"
            cursor.execute(sql, ({product_name}, {product_price}))
            connection.commit()
            cursor.close()
    except Exception as e:
        print(f'Failed to open connection: {e}')

        
def insert_into_orders_db(new_customer_name, new_customer_address, new_customer_phone, courier_id, status_id, product_id):
    try:
        with pymysql.connect(
            host = host_name,
            database = database_name,
            user = user_name,
            password = user_password    
        ) as connection:
            cursor = connection.cursor()
            sql = "INSERT INTO orders (customer_name, customer_address, customer_phone, courier_id, status_id, product_id) VALUES (%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, ({new_customer_name}, {new_customer_address}, {new_customer_phone}, {courier_id}, {status_id}, {product_id}))
            connection.commit()
            cursor.close()
    except Exception as e:
        print(f'Failed to open connection: {e}')
        

#------------------UPDATE DB FUNCS----------------------------------------------------- 
def update_product_db(get_product_id: int, new_product_name: str, new_product_price: float):
    try:
        with pymysql.connect(
            host = host_name,
            database = database_name,
            user = user_name,
            password = user_password    
        ) as connection:
            cursor = connection.cursor()
            sql = "UPDATE products SET product_name = %s, product_price = %s WHERE product_id = %s"
            cursor.execute(sql, ({new_product_name}, {new_product_price}, {get_product_id}))
            connection.commit()
            cursor.close()
    except Exception as e:
        print(f'Failed to open connection: {e}')


def update_courier_db(get_courier_id: int, new_courier_name: str, new_courier_phone: str):
    try:
        with pymysql.connect(
            host = host_name,
            database = database_name,
            user = user_name,
            password = user_password    
        ) as connection:
            cursor = connection.cursor()
            sql = "UPDATE couriers SET courier_name = %s, courier_phone = %s WHERE courier_id = %s"
            cursor.execute(sql, ({new_courier_name}, {new_courier_phone}, {get_courier_id}))
            connection.commit()
            cursor.close()
    except Exception as e:
        print(f'Failed to open connection: {e}')
        
        
def update_order_status_db(get_order_id: int, get_status_id: int):
    try:
        with pymysql.connect(
            host = host_name,
            database = database_name,
            user = user_name,
            password = user_password    
        ) as connection:
            cursor = connection.cursor()
            sql = "UPDATE orders SET status_id = %s WHERE order_id = %s"
            cursor.execute(sql, ({get_status_id}, {get_order_id}))
            connection.commit()
            cursor.close()
    except Exception as e:
        print(f'Failed to open connection: {e}')
        
        
def update_orders_db(new_customer_name: str, new_customer_address: str, new_customer_phone, new_courier_id, new_product_id, get_order_id: int):
    try:
        with pymysql.connect(
            host = host_name,
            database = database_name,
            user = user_name,
            password = user_password    
        ) as connection:
            cursor = connection.cursor()
            sql = "UPDATE orders SET customer_name = %s, customer_address = %s, customer_phone = %s, courier_id = %s, product_id = %s WHERE order_id = %s"
            cursor.execute(sql, ({new_customer_name}, {new_customer_address}, {new_customer_phone}, {new_courier_id}, {new_product_id}, {get_order_id}))
            connection.commit()
            cursor.close()
    except Exception as e:
        print(f'Failed to open connection: {e}')


        
#-----------------Select from db funcs----------------------------------------------------------

def select_from_couriers_db():
    try:
        with pymysql.connect(
            host = host_name,
            database = database_name,
            user = user_name,
            password = user_password    
        ) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT courier_id, courier_name, courier_phone FROM couriers")
            rows = cursor.fetchall()
            print("\n[COURIERS MENU]")
            for row in rows:
                print(f"[Courier ID]: {row[0]}, [Name]: {row[1]}, [Phone]: {row[2]}")
            cursor.close()
    except Exception as e:
        print(f'Failed to open connection: {e}')

        
def select_from_products_db():
    try:
        with pymysql.connect(
            host = host_name,
            database = database_name,
            user = user_name,
            password = user_password    
        ) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT product_id, product_name, product_price FROM products")
            rows = cursor.fetchall()
            print("\n[PRODUCTS MENU]")
            for row in rows:
                print(f"[Product ID]: {row[0]}, [Name]: {row[1]}, [Price]: {row[2]}")
            cursor.close()
    except Exception as e:
        print(f'Failed to open connection: {e}')

def select_from_orders_db():
    try:
        with pymysql.connect(
            host = host_name,
            database = database_name,
            user = user_name,
            password = user_password    
        ) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT order_id, customer_name, customer_address, customer_phone, courier_id, status_id, product_id FROM orders")
            rows = cursor.fetchall()
            print("\n[ORDERS MENU]")
            for row in rows:
                print(f"[Order ID]: {row[0]}, [Name]: {row[1]}, [Address]: {row[2]}, [Phone]: {row[3]}, [Courier]: {row[4]}, [Status]: {row[5]}, [Product]: {row[6]}")
            cursor.close()
    except Exception as e:
        print(f'Failed to open connection: {e}')
        
def select_from_status_db():
    try:
        with pymysql.connect(
            host = host_name,
            database = database_name,
            user = user_name,
            password = user_password    
        ) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT status_id, status FROM order_status")
            rows = cursor.fetchall()
            print("\n[STATUS OPTIONS]")
            for row in rows:
                print(f"[Status ID]: {row[0]}, [Status]: {row[1]}")
            cursor.close()
    except Exception as e:
        print(f'Failed to open connection: {e}')

        

        
# -------------DELETE ROWS FROM DB FUNCS ---------------------------------------------------

def remove_from_product_db(get_product_id: int):
    try:
        with pymysql.connect(
            host = host_name,
            database = database_name,
            user = user_name,
            password = user_password    
        ) as connection:
            cursor = connection.cursor()
            sql = "DELETE FROM products WHERE product_id = %s"
            cursor.execute(sql, ({get_product_id}))
            connection.commit()
            cursor.close()
    except Exception as e:
        print(f'Failed to open connection: {e}')
        

def remove_from_couriers_db(get_courier_id: int):
    try:
        with pymysql.connect(
            host = host_name,
            database = database_name,
            user = user_name,
            password = user_password    
        ) as connection:
            cursor = connection.cursor()
            sql = "DELETE FROM couriers WHERE courier_id = %s"
            cursor.execute(sql, ({get_courier_id}))
            connection.commit()
            cursor.close()
    except Exception as e:
        print(f'Failed to open connection: {e}')


def remove_from_orders_db(get_order_id: int):
    try:
        with pymysql.connect(
            host = host_name,
            database = database_name,
            user = user_name,
            password = user_password    
        ) as connection:
            cursor = connection.cursor()
            sql = "DELETE FROM orders WHERE order_id = %s"
            cursor.execute(sql, ({get_order_id}))
            connection.commit()
            cursor.close()
    except Exception as e:
        print(f'Failed to open connection: {e}')