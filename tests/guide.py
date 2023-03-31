import json
from typing import List,Dict

#Start of app/function:
# load orders from file into orders variable
def load_list_from_json(filename: str) -> List[Dict]:
    try:
        with open(filename, 'r') as f:
            file_data = json.loads(f.read())
        return file_data
    except FileNotFoundError as fnfe:
        print(f"Cannot fine file: {fnfe}")
    # open the file
    # read json contents into variable
    # return variable
orders = load_list_from_json('orders.json')

# during app
# make changes to orders within the variable

for idx, order in enumerate(orders):
    print(idx, order)
idx_input = int(input('pick an order: '))
orders[idx_input]['phone_number'] = '999'
for idx, order in enumerate(orders):
    print(idx, order)
    
# close app/function
# save and overwrite the orders file
#def save_list_to_json(list_to_save, filename):
    # open filename as write
    # save the list

# function to update order status
# 1. call load from file function
# 2. display list of data
# 3. get which item to update from user (index)
# 4. take input from user for what changes to make
# 5. update data in variable
# 6. save variable to file