from address_book_main import AddressBookMain
from validate import validation_wrapper, validate_data
from contact import Contact
from address_book_main import SearchByCity, SearchByState


# Initialize Address Book system
address_book_system = AddressBookMain()

@validation_wrapper
def add_contact_to_book(address_book, contact_data):
    """ Adds a validated contact to the selected address book. """
    first_name= contact_data["first_name"].capitalize()
    last_name = contact_data["last_name"].capitalize()
    
    # Check if the contact already exists
    if address_book.is_duplicate(first_name, last_name):
        print("\n Duplicate Entry: A contact with this name already exists in the Address Book!")
        return

    contact = Contact(**contact_data)  
    address_book.add_contact(contact)  
    print("\n Contact added successfully!")

def get_contact_input():
    """Collects user input for contact details with trimmed spaces."""
    return {
        "first_name": input("Enter First Name: ").strip(),
        "last_name": input("Enter Last Name: ").strip(),
        "address": input("Enter Address: ").strip(),
        "city": input("Enter City: ").strip(),
        "state": input("Enter State: ").strip(),
        "zip_code": input("Enter ZIP Code: ").strip(),
        "phone_number": input("Enter Phone Number: ").strip(),
        "email": input("Enter Email: ").strip()
    }

def edit_contact(address_book):
    """Edits an existing contact in the address book."""
    first_name = input("Enter First Name of the contact to edit: ").strip().lower()
    last_name = input("Enter Last Name of the contact to edit: ").strip().lower()
    
    contact = address_book.get_contact(first_name, last_name)
    if not contact:
        print("\n Contact not found!")
        return
    
    print(f"\nEditing Contact: {contact}")
    
    updated_data = {
        "first_name": contact.first_name,  # Keep original case
        "last_name": contact.last_name,  # Keep original case
        "address": input(f"Enter new Address (Leave blank to keep '{contact.address}'): ").strip() or contact.address,
        "city": input(f"Enter new City (Leave blank to keep '{contact.city}'): ").strip() or contact.city,
        "state": input(f"Enter new State (Leave blank to keep '{contact.state}'): ").strip() or contact.state,
        "zip_code": input(f"Enter new ZIP Code (Leave blank to keep '{contact.zip_code}'): ").strip() or contact.zip_code,
        "phone_number": input(f"Enter new Phone Number (Leave blank to keep '{contact.phone_number}'): ").strip() or contact.phone_number,
        "email": input(f"Enter new Email (Leave blank to keep '{contact.email}'): ").strip() or contact.email
    }

    validated_data = validate_data(updated_data)
    if not isinstance(validated_data, dict):  # Check if validation failed
        print("\nValidation failed! Edit operation canceled.")
        return
    
    contact.update(validated_data)  # Update contact details
    print("\nContact updated successfully!")


def search_contact():
    """Allows the user to search for a contact by city or state and displays results as a dictionary."""
    print("\n1. Search by City")
    print("2. Search by State")
    choice = input("Choose an option: ").strip()

    if choice == "1":
        city_name = input("Enter City Name to search: ").strip()
        search_instance = SearchByCity(city_name)
        results = search_instance.search(address_book_system)
    elif choice == "2":
        state_name = input("Enter State Name to search: ").strip()
        search_instance = SearchByState(state_name)
        results = search_instance.search(address_book_system)
    else:
        print("Invalid choice.")
        return
    
    if results:
        print("\nSearch Results:")
        for location, contacts in results.items():
            print(f"\nLocation: {location}")
            for contact, book_name in contacts:
                print(f"{contact} (Found in Address Book: {book_name})")
    else:
        print("\nNo contacts found in the given location.")



def manage_address_book():
    """Handles address book operations."""
    while True:
        print("\nAddress Book Menu")
        print("1. Add Address Book")
        print("2. Select Address Book")
        print("3. Display Address Books")
        print("4. Delete Address Book")
        print("5. Search Contact")
        print("6. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            book_name = input("Enter Address Book Name: ").strip()
            address_book_system.add_address_book(book_name)
        
        elif choice == "2":
            book_name = input("Enter Address Book Name to use: ").strip()
            address_book = address_book_system.get_address_book(book_name)

            if address_book is None:
                print("Address Book not found")
                continue
            
            while True:
                print(f"\nManaging '{book_name}' Address Book")
                print("1. Add Contact")
                print("2. View Contacts")
                print("3. Edit Contact")
                print("4. Delete Contact")
                print("5. Exit Address Book")

                sub_choice = input("Choose an option: ").strip()

                if sub_choice == "1":
                    contact_data = get_contact_input()
                    add_contact_to_book(address_book, contact_data)
                
                elif sub_choice == "2":
                    address_book.view_contacts()

                elif sub_choice == "3":
                    edit_contact(address_book)

                elif sub_choice == "4":
                    first_name = input("Enter First Name of contact to delete: ").strip()
                    last_name = input("Enter Last Name of contact to delete: ").strip()
                    address_book.delete_contact(first_name, last_name)

                elif sub_choice == "5":
                    print(f"Exiting '{book_name}' Address Book")
                    break
                
                else:
                    print("Invalid choice, please select again")

        elif choice == "3":
            address_book_system.display_address_books()

        elif choice == "4":
            book_name = input("Enter Address Book Name to delete: ").strip()
            address_book_system.delete_address_book(book_name)

        elif choice == "5":
            search_contact()

        elif choice == "6":
            print("Exiting Address Book System. Goodbye")
            break

        else:
            print("Invalid choice, please select again")

if __name__ == "__main__":
    manage_address_book()