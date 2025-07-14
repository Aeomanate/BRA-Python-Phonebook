import copy
import json
import os

# {("first_name", "last_name"): ("phone_number", "sity", "state")  }
phonebook = {
    # ("Alice", "Johnson"): ("555-2468", "Chicago", "IL"),
    # ("Bob", "Williams"): ("555-1357", "Houston", "TX"),
    # ("Charlie", "Brown"): ("555-9876", "Phoenix", "AZ"),
    # ("Diana", "Miller"): ("555-1122", "Philadelphia", "PA"),
    # ("Ethan", "Davis"): ("555-3344", "San Antonio", "TX"),
    # ("Fiona", "Wilson"): ("555-5566", "San Diego", "CA")
}


def add_entry():
    try:
        while True:
            first_name = input("Enter first name: ").strip().capitalize()
            last_name = input("Enter last name: ").strip().capitalize()
            for key in phonebook.keys():
                if first_name == key[0] and last_name == key[1]:
                    print('This fullname is already in our list')
                    raise ValueError
            break
        while True:
            phone_number = input("Enter phone number: ").strip().capitalize()
            for num in phonebook.values():
                if phone_number == num[0]:
                    print('This number is already in our list')
                    raise ValueError
            break

        city = input("Enter city: ").strip().capitalize()
        state = input("Enter state: ").strip().upper()

        phonebook[(first_name, last_name)] = (phone_number, city, state)
        print(f"\n {first_name} {last_name} added to the phonebook!")
        return True
    except ValueError:
        add_entry()
    except Exception as e:
        print(f"Error adding entry: {str(e)}")
        return False


def search_by_first_name():
    found = False
    name_to_search = input("Enter first name: ").lower()
    for (first_name, last_name), (phone_number, city, state) in phonebook.items():
        if first_name.lower() == name_to_search:
            print(f'Found person: {first_name} {last_name}, phone number: {phone_number}, city: {city}, state: {state}')
            found = True
    if not found:
        print("A person by that name has not been found")


def search_by_last_name():  # Андрій
    results = []

    l_name = input("Enter last name: ").strip()

    for (first_name, last_name), (phone_number, city, state) in phonebook.items():
        if last_name.lower() == l_name.lower():
            results.append((first_name, last_name, phone_number, city, state))
            found = True
    print(f"Found entries: {results}") if results else print(f"No entries found for entered last name '{l_name}'.")


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


def search_by_phone_number():
    phone = input("Enter the phone number to search: ")
    found = False
    for (first_name, last_name), (phone_number, city, state) in phonebook.items():
        if phone_number == phone:
            print(f"Found: {first_name} {last_name} | Phone: {phone_number} | City: {city} | State: {state}")
            found = True
            break
    if not found:
        print("No entry found with that phone number.")


def search_by_city_or_state():  # Ростислав
    query = input("Enter city or state to search: ").strip().lower()
    results = []
    for (first_name, last_name), (phone_number, city, state) in phonebook.items():
        if query == city.lower() or query == state.lower():
            results.append(f"{first_name} {last_name}: {phone_number}, {city}, {state}")
    if results:
        print("\n".join(results))
    else:
        print("No entries found for the given city or state.")


def delete_by_phone_number():  # Дмитро
    print("Delete a record by telephone number")
    phone = input("Enter the phone number to search: ")
    print("Current phonebook:", phonebook)
    for key, value in list(phonebook.items()):
        if value[0] == phone:
            del phonebook[key]
            print(f"Record with phone number {phone} deleted.")
            break
    else:
        print("Phone number not found.")

    print("Updated phonebook:\n")
    phonebook_info()


def update_by_phone_number():
    phone = input("Enter the phone number to update: ")
    for key, value in phonebook.items():
        if phone == value[0]:
            print(f"Current info for this phone: {key} {phonebook[key]}.\n"
                  f"Enter new information in the fields or press 'enter' to leave them as they were\n\n")
            update_logic(phone, key, value)
            break
    else:
        print("There is no such phone number in our list!\n"
              "Please try again")
        update_by_phone_number()


def update_logic(phone, key, value):
    try:
        while True:
            first_name = input("Enter new first name: ").strip().capitalize()
            last_name = input("Enter new last name: ").strip().capitalize()

            for key in phonebook.keys():
                if first_name == key[0] and last_name == key[1]:
                    print('This fullname is already in our list')
                    raise ValueError

            if first_name.strip() == '':
                fn = key[0]
            if last_name.strip() == '':
                ln = key[1]
            break

        while True:
            phone_number = input("Enter phone number: ").strip().capitalize()
            for num in phonebook.values():
                if phone_number == num[0]:
                    print('This number is already in our list')
                    raise ValueError

            if phone_number.strip() == '':
                phone_number = value[0]
            break

        city = input("Enter new city: ")
        if city.strip() == '':
            city = value[1]

        state = input("Enter new state: ")
        if state.strip() == '':
            state = value[2]

        del phonebook[key]
        phonebook[(first_name, last_name)] = (phone_number, city, state)
        print(f"New info for this phone: {(first_name, last_name)} {phonebook[(phone_number, city, state)]}.\n")
    except ValueError:
        update_logic()
    # else:
    #     print("There is no such phone number in our list!\n"
    #           "Please try again")
    #     update_by_phone_number()


def exit_program():
    try:
        file = open("phonebook.json", 'w', encoding='utf-8')
        data_to_save = {f"{key[0]} {key[1]}": value for key, value in phonebook.items()}
        json.dump(data_to_save, file)

        print("Exiting program.")
    except Exception as e:
        print(f"Error saving phonebook: {str(e)}")
    return False


def load_phonebook():
    global phonebook
    try:
        file = open("phonebook.json", 'r', encoding='utf-8')
        data = json.load(file)

        for key, value in data.items():
            first_name, last_name = key.split(" ", 1)
            phonebook[(first_name, last_name)] = tuple(value)

        print("Phonebook loaded.")
        phonebook_info()
    except FileNotFoundError:
        print("Phonebook file not found. It will be new book")


def phonebook_info():
    print("\nPhonebook:")
    for key, value in phonebook.items():
        print(f"{key} : {value}")


def application_loop():
    load_phonebook()

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
9) See phonebook
10) Exit the program""")
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
                phonebook_info()
            case 10:
                is_working = exit_program()
            case _:
                print("Invalid choice. Please select a number from 1 to 9.")


def main():
    application_loop()


main()
