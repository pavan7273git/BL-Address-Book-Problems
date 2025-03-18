from address_book import AddressBookMain  # Import AddressBookMain
from validate import validate_data       # Import validation
from contact import Contact              # Import Contact class

# Initialize Address Book
address_book = AddressBookMain("Personal Address Book")

def add_contact():
    """ Collects input, validates it, and adds a contact. """
    while True:
        contact_data = {
            "first_name": input("Enter First Name (Starts with a capital letter, min 3 chars): "),
            "last_name": input("Enter Last Name (Starts with a capital letter, min 3 chars): "),
            "address": input("Enter Address: "),
            "city": input("Enter City: "),
            "state": input("Enter State: "),
            "zip_code": input("Enter ZIP Code (5-6 digits): "),
            "phone_number": input("Enter Phone Number (10 digits): "),
            "mail": input("Enter Email: ")
        }

        validated_data = validate_data(contact_data)
        if validated_data:  # Proceed only if all fields are valid
            contact = Contact(**validated_data)
            address_book.addContact(contact)
            print("\nContact added successfully!")
            break  # Exit loop after successful addition
        else:
            print("\nValidation failed. Please re-enter details.")

def edit_contact():
    """ Edits an existing contact based on first & last name. """
    first_name = input("Enter First Name of the contact to edit: ").strip().title()
    last_name = input("Enter Last Name of the contact to edit: ").strip().title()
    
    for phone, contact in address_book.contacts.items():
        if contact.first_name == first_name and contact.last_name == last_name:
            print(f"\nFound Contact: {contact}")

            while True:
                new_data = {
                    "address": input(f"Enter new Address (Leave blank to keep '{contact.address}'): ") or contact.address,
                    "city": input(f"Enter new City (Leave blank to keep '{contact.city}'): ") or contact.city,
                    "state": input(f"Enter new State (Leave blank to keep '{contact.state}'): ") or contact.state,
                    "zip_code": input(f"Enter new ZIP Code (Leave blank to keep '{contact.zip_code}'): ") or contact.zip_code,
                    "phone_number": input(f"Enter new Phone Number (Leave blank to keep '{contact.phone_number}'): ") or contact.phone_number,
                    "mail": input(f"Enter new Email (Leave blank to keep '{contact.mail}'): ") or contact.mail
                }

                validated_data = validate_data(new_data)
                if validated_data:
                    contact.address = validated_data["address"]
                    contact.city = validated_data["city"]
                    contact.state = validated_data["state"]
                    contact.zip_code = validated_data["zip_code"]
                    contact.phone_number = validated_data["phone_number"]
                    contact.mail = validated_data["mail"]
                    
                    print("\n Contact updated successfully!")
                    return
                else:
                    print("\n Validation failed. Please re-enter details.")

    print("\n Contact not found!")

def view_contacts():
    """ Displays all contacts. """
    address_book.getContacts()

def exit_program():
    """ Exits the program. """
    print(" Exiting Address Book. Goodbye!")
    exit()

# Menu options mapping (Switch case alternative in Python)
menu_options = {
    "1": add_contact,
    "2": view_contacts,
    "3": edit_contact,
    "4": exit_program
}

if __name__ == "__main__":
    while True:
        print("\n ADDRESS BOOK MENU")
        print("1 Add Contact")
        print("2 View Contacts")
        print("3 Edit Contact")
        print("4 Exit")

        choice = input("Choose an option: ").strip()
        action = menu_options.get(choice)

        if action:
            action()
        else:
            print(" Invalid choice, please select again.")
