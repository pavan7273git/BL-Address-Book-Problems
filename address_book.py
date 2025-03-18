class AddressBookMain:
    def __init__(self, address_book_name):
        self.address_book_name = address_book_name
        self.contacts = {}  

    def addContact(self, contact_obj):
        self.contacts[contact_obj.phone_number] = contact_obj 

    def getContacts(self):
        print(f"\nWELCOME TO {self.address_book_name} ADDRESS BOOK\n")
        for phone, contact in self.contacts.items():
            print(contact) 

   