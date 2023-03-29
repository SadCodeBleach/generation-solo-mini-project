import pymysql
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
host_name = os.environ.get("mysql_host")
database_name = os.environ.get("mysql_db")
user_name = os.environ.get("mysql_user")
user_password = os.environ.get("mysql_pass")


try:
    print('Opening connection...')
    # TODO Establish a database connection
    # Hint: use "with ..."
    
    with pymysql.connect(
        host = host_name,
        database = database_name,
        user = user_name,
        password = user_password    
    ) as connection:

        # This bit won't compile till the "with" is done...
        print('Opening cursor...')
        # TODO open a cursor

        cursor = connection.cursor()


        print('Inserting new record...')
        # TODO Add code here to insert a new record
        def insert_into_courier_db(courier_name, courier_phone):
            sql = "INSERT INTO couriers (courier_name, courier_phone) VALUES (%s,%s)"
            cursor.execute(sql, ({courier_name}, {courier_phone}))
            connection.commit()
            
        def insert_into_product_db(product_name, product_price):
            sql = "INSERT INTO products (product_name, product_price) VALUES (%s,%s)"
            cursor.execute(sql, ({product_name}, {product_price}))
            connection.commit()

        # insert_into_courier_db("Damien", "07661868088")
        
        print('Selecting all records...')
        # TODO Add code here to select all the records

        def select_from_couriers_db():
            cursor.execute("SELECT courier_name, courier_phone FROM couriers")
            rows = cursor.fetchall()
            print(rows)
        
        def select_from_products_db():
            cursor.execute("SELECT product_name, product_price FROM products")
            rows = cursor.fetchall()
            print(rows)
            
            
            

        print('Displaying all records...')
        # TODO Add code here to print out all the records
        



        print('Closing cursor...')
        # TODO close the cursor
        cursor.close()


    # The connection will automatically close here
except Exception as e:
    print(f'Failed to open connection: {e}')

# Leave this line here!
print('All done!')
