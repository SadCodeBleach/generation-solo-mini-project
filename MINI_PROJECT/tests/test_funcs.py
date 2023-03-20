#------------------------------------------------------

def print_products(product_items):
    print("[PRODUCT ITEM LIST:]")                
    for item, price in product_items.item():
        print(item, price)
    print("\n")
    

# Generic write to list function:
def write_list_to_file(file_name, list_of_items):
    with open(file_name, "w") as f:
        for item in list_of_items:
            f.write(item) 
            

# Generic function for opening files
def print_items_from_file(file):
    items = file.readlines()
    for item in items:
        print(item.strip())
 
# try/except to catch errors       
try:
    courier_file = open('couriers.txt', 'r')
    print_items_from_file(courier_file)
except FileNotFoundError as fnfe:
    print(f"Cannot find file: {fnfe}")
# finally statement to finish (file.close()):
finally:
    courier_file.close()
    print("The file was closed")
    
def enumerate_list_starting_from_index_1(my_list):
    for i, item in enumerate(my_list):
        print(f'{i + 1}: {item}')



def load_items_from_file(filename, file_list):
    file_list = []
    try:
        with open(filename, 'r') as f:
            content = f.readlines()
            for x in content:
                row = x.split()
                file_list.append(row[0])
    except FileNotFoundError as e:
        print(f'File not found: {e}')
    return enumerate_list_starting_from_index_1()
    


