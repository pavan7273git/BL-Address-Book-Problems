from contact import Contact
from address_book import AddressBookMain
from validate import validation_wrapper  # Import validation wrapper

print("Welcome to Address Book Program")
address_book = AddressBookMain("Personal Address Book")

@validation_wrapper
def add_contact(contact_data):
    """ Adds a contact after validation. """
    contact = Contact(
        contact_data["first_name"],
        contact_data["last_name"],
        contact_data["address"],
        contact_data["city"],
        contact_data["state"],
        contact_data["zip_code"],
        contact_data["phone_number"],
        contact_data["mail"]
    )
    address_book.addContact(contact)
    print("\nContact added successfully!")

def get_contact_input():
    """ Collects user input and stores it in a dictionary for validation. """
    return {
        "first_name": input("Enter First Name (Starts with a capital letter, min 3 chars): "),
        "last_name": input("Enter Last Name (Starts with a capital letter, min 3 chars): "),
        "address": input("Enter Address: "),
        "city": input("Enter City: "),
        "state": input("Enter State: "),
        "zip_code": input("Enter ZIP Code (5-6 digits): "),
        "phone_number": input("Enter Phone Number (10 digits): "),
        "mail": input("Enter Email: ")
    }

if __name__ == "__main__":
    while True:
        contact_data = get_contact_input()
        add_contact(contact_data)
        
        choice = input("Do you want to add another contact? (yes/no): ").strip().lower()
        if choice != "yes":
            break
    
    print("\nSaved Contacts:")
    address_book.getContacts()
