class AddressBook:
    def __init__(self, name):
        """Initialize AddressBook with a unique name and empty contact list."""
        self.name = name
        self.contacts = []

    def add_contact(self, contact):
        """Adds a new contact to the address book."""
        self.contacts.append(contact)


    def is_duplicate(self, first_name, last_name):
        """Checks if a contact with the same name already exists."""
        return any(contact.first_name == first_name and contact.last_name == last_name for contact in self.contacts)


    def view_contacts(self):
        """Displays all contacts in the address book."""
        if not self.contacts:
            print("No contacts found in this address book.")
        else:
            for contact in self.contacts:
                print(contact)

    def get_contact(self, first_name, last_name):
        """Finds and returns a contact by first and last name (case insensitive)."""
        first_name = first_name.strip().lower()  # Convert input to lowercase
        last_name = last_name.strip().lower()

        """Finds and returns a contact by first and last name."""
        for contact in self.contacts:
            if contact.first_name.lower() == first_name and contact.last_name.lower() == last_name:
                return contact
        return None

    def delete_contact(self, first_name, last_name):
        """Deletes a contact from the address book."""
        first_name = first_name.capitalize()  # Ensure stored format is matched
        last_name = last_name.capitalize()

        for contact in self.contacts:
            if contact.first_name == first_name and contact.last_name == last_name:
                self.contacts.remove(contact)
                print(f" Contact '{first_name} {last_name}' deleted successfully!")
                return

    print(" Contact not found! Make sure you entered the correct name.")
