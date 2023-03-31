def get_id_input(input_text):
    while True:
        try:
            id_option = int(input(input_text))
            if id_option == "":
                print('No index selected.')
                break
            else:
                return id_option
        except:
            print('This is not an index!')
            break


def get_name_input(input_text):
    while True:
        try:
            name = str(input(input_text))
            if name == "":
                print("No name inserted!")
                break
            else:
                return name
        except:
            print('This is not a name!')
            break
            

def get_phone_input(input_text):
    while True:
        try:
            phone = str(input(input_text))
            if phone == "":
                print("No phone numer inserted!")
                break
            else:
                return phone
        except:
            print('This is not a phone number!')
            break

        
def get_price_input(input_text):
    while True:
        try:
            price = float(input(input_text))
            if price == "":
                print("No price inserted!")
                break
            else:
                return price
        except:
            print('This is not a price!')
            break