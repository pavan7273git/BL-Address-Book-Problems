from address_book import AddressBook  #  Import AddressBook

class AddressBookMain:
    def __init__(self):
        """Initialize the AddressBook system with multiple address books."""
        self.address_books = {}

    def add_address_book(self, name):
        """Creates a new address book with a unique name."""
        if name in self.address_books:
            print(f"Address Book '{name}' already exists!")
        else:
            self.address_books[name] = AddressBook(name)  
            print(f"Address Book '{name}' created successfully.")

    def get_address_book(self, name):
        """Retrieves an existing address book by name."""
        return self.address_books.get(name, None)

    def display_address_books(self):
        """Displays all available address books."""
        if not self.address_books:
            print("No address books available.")
        else:
            print("Existing Address Books:")
            for name in self.address_books:
                print(f"- {name}")

    def delete_address_book(self, name):
        """Deletes an address book if it exists."""
        if name in self.address_books:
            del self.address_books[name]
            print(f"Address Book '{name}' deleted successfully.")
        else:
            print(f"Address Book '{name}' not found.")


class SearchByCity(AddressBookMain):
    def search(self, address_book_system, city_name):
        """Searches contacts by city name and returns a dictionary."""
        city_dict = {}
        for book_name, address_book in address_book_system.address_books.items():
            for contact in address_book.contacts:
                if contact.city.lower() == city_name.lower():
                    if city_name not in city_dict:
                        city_dict[city_name] = []
                    city_dict[city_name].append((contact, book_name))
        return city_dict  
        

class SearchByState(AddressBookMain):
    def search(self, address_book_system, state_name):
        """Searches contacts by state name and returns a dictionary."""
        state_dict = {}
        for book_name, address_book in address_book_system.address_books.items():
            for contact in address_book.contacts:
                if contact.state.lower() == state_name.lower():
                    if state_name not in state_dict:
                        state_dict[state_name] = []
                    state_dict[state_name].append((contact, book_name))
        return state_dict  



