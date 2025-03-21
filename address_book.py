import os
import json
from contact import Contact  

DATA_FOLDER = "data"
JSON_FOLDER = os.path.join(DATA_FOLDER, "json")

class AddressBook:
    def __init__(self, name):
        """Initialize AddressBook with a unique name and empty contact list."""
        self.name = name
        self.contacts = []
        self.json_file = os.path.join(JSON_FOLDER, f"{self.name}.json")
        self.load_contacts()  # Load existing contacts if the file exists

    def add_contact(self, contact):
        """Adds a new contact to the address book."""
        self.contacts.append(contact)
        self.save_contacts()

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
        """Finds and returns a contact by first and last name."""
        for contact in self.contacts:
            if contact.first_name.lower() == first_name.lower() and contact.last_name.lower() == last_name.lower():

                return contact
        return None

    def edit_contact(self, first_name, last_name, updated_data):
        """Edits an existing contact and saves changes."""
        for contact in self.contacts:
            if contact["first_name"].lower() == first_name.lower() and contact["last_name"].lower() == last_name.lower():
                contact.update(updated_data)  # Update contact details
                self.save_contacts()
                print(f"Contact '{first_name} {last_name}' updated successfully!")
                return
        print("Contact not found!")

    def delete_contact(self, first_name, last_name):
        """Deletes a contact from the address book."""
        for contact in self.contacts:
            if contact["first_name"].lower() == first_name.lower() and contact["last_name"].lower() == last_name.lower():
                self.contacts.remove(contact)
                self.save_contacts()
                print(f"Contact '{first_name} {last_name}' deleted successfully!")
                return
        print("Contact not found!")

    def save_contacts(self):
        """Saves all contacts to a JSON file."""
        os.makedirs(JSON_FOLDER, exist_ok=True)  # Ensure the directory exists
        with open(self.json_file, "w") as file:
            json.dump([contact.__dict__ for contact in self.contacts], file, indent=4)

    def load_contacts(self):
        """Loads contacts from a JSON file."""
        if os.path.exists(self.json_file):
            with open(self.json_file, mode="r") as file:
                try:
                    contacts_data = json.load(file)
                    self.contacts = [Contact(**data) for data in contacts_data]  # Convert back to Contact objects
                except json.JSONDecodeError:
                    self.contacts = []
        else:
            self.contacts = []

