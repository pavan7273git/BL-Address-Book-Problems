import os
import csv

# Define the CSV folder path
DATA_FOLDER = "data"
CSV_FOLDER = os.path.join(DATA_FOLDER, "csv")

class Contact:
    """Class representing a contact in the address book."""
    def __init__(self, first_name, last_name, address, city, state, zip_code, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.address}, {self.city}, {self.state}, {self.zip_code}, {self.phone_number}, {self.email}"

class AddressBook:
    """Class representing an Address Book."""
    def __init__(self, name):
        self.name = name
        self.contacts = []
        self.csv_file = os.path.join(CSV_FOLDER, f"{self.name}.csv")

        self.load_contacts()  # Load contacts on initialization

    def add_contact(self, contact):
        """Adds a new contact and saves it to CSV."""
        self.contacts.append(contact)
        self.save_contacts()  # Save contacts after adding

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
        first_name = first_name.strip().lower()
        last_name = last_name.strip().lower()
        for contact in self.contacts:
            if contact.first_name.lower() == first_name and contact.last_name.lower() == last_name:
                return contact
        return None


    def delete_contact(self, first_name, last_name):
        """Deletes a contact and updates the CSV file."""
        contact = self.get_contact(first_name, last_name)
        if contact:
            self.contacts.remove(contact)
            self.save_contacts()  # Save after deletion
            print(f" Contact '{first_name} {last_name}' deleted successfully!")
        else:
            print(f" Contact '{first_name} {last_name}' not found!")

    def save_contacts(self):
        """Saves all contacts to a CSV file."""
        os.makedirs(CSV_FOLDER, exist_ok=True)  # Ensure the directory exists

        with open(self.csv_file, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["First Name", "Last Name", "Address", "City", "State", "ZIP", "Phone", "Email"])

            for contact in self.contacts:
                writer.writerow([
                    contact.first_name, contact.last_name, contact.address,
                    contact.city, contact.state, contact.zip_code,
                    contact.phone_number, contact.email
                ])

    def load_contacts(self):
        """Loads contacts from a CSV file if it exists."""
        if os.path.exists(self.csv_file):
            with open(self.csv_file, mode="r", newline="") as file:
                reader = csv.reader(file)
                next(reader, None)  # Skip the header row

                for row in reader:
                    if len(row) == 8:  # Ensure correct format
                        contact = Contact(*row)
                        self.contacts.append(contact)
