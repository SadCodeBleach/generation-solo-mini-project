couriers = ["jack", "sue"]

with open("couriers.txt", "w") as f:
    for courier in couriers:
        f.write(courier) 


def write_list_to_file(file_name, list_of_items):
    with open(file_name, "w") as f:
        for item in list_of_items:
            f.write(item) 

with open("couriers.txt", "w") as couriers_file:
    for courier in couriers:
        couriers_file.write(courier)
        couriers_file.write("\n")
        
