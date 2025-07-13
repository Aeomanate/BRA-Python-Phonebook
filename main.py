phonebook = {}
def add_entry(): # Nazar
    print("Add new entry - stub")

def search_by_first_name(): # Артем Ніколаєв
    print("Search by first name - stub")

def search_by_last_name(): # Андрій
    print("Search by last name - stub")

def search_by_full_name(): # Віталіна
    print("Search by full name - stub")

def search_by_phone_number(): # Михайло
    print("Search by telephone number - stub")

def search_by_city_or_state(): # Ростислав
    print("Search by city or state - stub")

def delete_by_phone_number(): # Дмитро
    print("Delete a record by telephone number - stub")

def update_by_phone_number(phonebook_dic,phone_number=""):
    found_person=None
    phone_number=str(input("Enter phone number: "))
    for key_name, data_value in phonebook_dic.items():
        if data_value[0] == phone_number:
            found_person=(key_name, data_value)
            break
    if found_person:
        name, data=found_person
        print(f"""Person with phone number {phone_number} was found.
                Full name: {name[0]} {name[1]}
                City: {data[1]}, {data[2]}""")
    else:
        print(f"Person with phone number {phone_number} was not found. Create new record.")
        first_name=input("First name: ")
        last_name=input("Last name: ")
        city=input("City: ")
        state=input("State: ")
        new_key_name=(first_name, last_name)
        new_data_value=(phone_number, city, state)
        phonebook_dic[new_key_name] = new_data_value
        print(f"Record for person {new_key_name[0]} {new_key_name[1]} with phone number {phone_number} was updated.")
    return phonebook_dic

def exit_program():
    print("Exiting program.")
    return False

def application_loop():
    is_working = True
    while is_working:
        print("""\nPhonebook Menu:
1) Add new entries 
2) Search by first name 
3) Search by last name 
4) Search by full name
5) Search by telephone number
6) Search by city or state
7) Delete a record for a given telephone number
8) Update a record for a given telephone number
9) Exit the program""")
        try:
            choice = int(input('Your choice: '))
        except ValueError:
            print("Please enter a valid number from 1 to 9.")
            continue

        match choice:
            case 1:
                add_entry()
            case 2:
                search_by_first_name()
            case 3:
                search_by_last_name()
            case 4:
                search_by_full_name()
            case 5:
                search_by_phone_number()
            case 6:
                search_by_city_or_state()
            case 7:
                delete_by_phone_number()
            case 8:
                update_by_phone_number(phonebook)
            case 9:
                is_working = exit_program()
            case _:
                print("Invalid choice. Please select a number from 1 to 9.")

def main():
    application_loop()

main()