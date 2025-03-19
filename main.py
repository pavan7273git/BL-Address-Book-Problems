from address_book import AddressBookMain  # Import AddressBookMain class
from validate import validate_data  # Import validation functions
from contact import Contact  # Import Contact class

# Take address book name from user
address_book_name = input("Enter the name of your Address Book: ").strip()
address_book = AddressBookMain(address_book_name)  # Initialize with user-defined name

def add_contact():
    """ Collects user input and adds a contact after validation. """
    contact_data = {
        "first_name": input("Enter First Name (Starts with a capital letter, min 3 chars): ").strip(),
        "last_name": input("Enter Last Name (Starts with a capital letter, min 3 chars): ").strip(),
        "address": input("Enter Address: ").strip(),
        "city": input("Enter City: ").strip(),
        "state": input("Enter State: ").strip(),
        "zip_code": input("Enter ZIP Code (5-6 digits): ").strip(),
        "phone_number": input("Enter Phone Number (10 digits): ").strip(),
        "mail": input("Enter Email: ").strip()
    }

    validated_data = validate_data(contact_data)
    if any(value is False for value in validated_data.values()):
        print("\nValidation failed! Contact not added.")
        return
    
    contact = Contact(
        validated_data["first_name"],
        validated_data["last_name"],
        validated_data["address"],
        validated_data["state"],  
        validated_data["city"],   
        validated_data["zip_code"],
        validated_data["phone_number"],
        validated_data["mail"]
    )

    address_book.addContact(contact)
    print("\nContact added successfully!")

def edit_contact():
    """ Edits an existing contact based on first name and last name. """
    first_name = input("Enter First Name of the contact to edit: ").strip()
    last_name = input("Enter Last Name of the contact to edit: ").strip()
    
    for phone, contact in address_book.contacts.items():
        if contact.first_name.lower() == first_name.lower() and contact.last_name.lower() == last_name.lower():
            print(f"\nFound Contact: {contact}")

            updated_data = {
                "address": input(f"Enter new Address (Leave blank to keep '{contact.address}'): ").strip() or contact.address,
                "city": input(f"Enter new City (Leave blank to keep '{contact.city}'): ").strip() or contact.city,
                "state": input(f"Enter new State (Leave blank to keep '{contact.state}'): ").strip() or contact.state,
                "zip_code": input(f"Enter new ZIP Code (Leave blank to keep '{contact.zip_code}'): ").strip() or contact.zip_code,
                "phone_number": input(f"Enter new Phone Number (Leave blank to keep '{contact.phone_number}'): ").strip() or contact.phone_number,
                "mail": input(f"Enter new Email (Leave blank to keep '{contact.mail}'): ").strip() or contact.mail
            }

            validated_data = validate_data(updated_data)
            if any(value is False for value in validated_data.values()):
                print("\nValidation failed! Edit operation canceled.")
                return

            contact.address = validated_data["address"]
            contact.city = validated_data["city"]
            contact.state = validated_data["state"]
            contact.zip_code = validated_data["zip_code"]
            contact.phone_number = validated_data["phone_number"]
            contact.mail = validated_data["mail"]
            
            print("\nContact updated successfully!")
            return
    
    print("\nContact not found!")

def delete_contact():
    """ Deletes a contact using the first name and last name. """
    first_name = input("Enter First Name of the contact to delete: ").strip()
    last_name = input("Enter Last Name of the contact to delete: ").strip()

    for phone, contact in list(address_book.contacts.items()):
        if contact.first_name.lower() == first_name.lower() and contact.last_name.lower() == last_name.lower():
            del address_book.contacts[phone]
            print("\nContact deleted successfully!")
            return
    
    print("\nContact not found!")

if __name__ == "__main__":
    print(f"\nWELCOME TO {address_book_name.upper()} ADDRESS BOOK\n")  
    
    while True:
        print("\n1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            address_book.getContacts()
        elif choice == "3":
            edit_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print(f"Exiting {address_book_name} Address Book. Goodbye!")
            break
        else:
            print("Invalid choice, please select again.")
