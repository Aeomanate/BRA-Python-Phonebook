# {("first_name", "last_name"): ("phone_number", "sity", "state")  }
phonebook = {}

def add_entry(): # Nazar
    print("Add new entry - stub")

def search_by_first_name(): # Артем Ніколаєв
    print("Search by first name - stub")

def search_by_last_name(): # Андрій
    print("Search by last name - stub")

def search_by_full_name():
    while True:
        full_name = input("\nEnter full name or type 'back' to return to Phonebook Menu: ").strip()

        if full_name.lower() == "back":
            return

        if " " not in full_name:
            print("Please enter both first and last name separated by space.")
            continue

        first_name, last_name = full_name.split(" ", 1)
        found = False
        for (fn, ln), (phone, city, state) in phonebook.items():
            if fn.lower() == first_name.lower() and ln.lower() == last_name.lower():
                print(f"\nFound contact:")
                print(f"Name: {fn} {ln}")
                print(f"Phone number: {phone}")
                print(f"City: {city}")
                print(f"State: {state}")
                found = True
                break

        if not found:
            print("No matching contact found.")

def search_by_phone_number(): # Михайло
    print("Search by telephone number - stub")

def search_by_city_or_state(): # Ростислав
    print("Search by city or state - stub")

def delete_by_phone_number(): # Дмитро
    print("Delete a record by telephone number - stub")

def update_by_phone_number(phone_number, new_person): # Юлія
    print("Update a record by telephone number - stub")

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
                update_by_phone_number()
            case 9:
                is_working = exit_program()
            case _:
                print("Invalid choice. Please select a number from 1 to 9.")

def main():
    application_loop()

main()