class Contact:
    def __init__(self, first_name, last_name, address, city, state, zip_code, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone_number = phone_number
        self.email = email

    def update(self, updated_data):
        """Updates the contact details with validated data."""
        for key, value in updated_data.items():
            setattr(self, key, value)  # Dynamically update attributes

    def __str__(self):
        """Return a string representation of the contact."""
        return (f"First Name: {self.first_name}\n Last Name: {self.last_name}\n Address: {self.address}\nCity: {self.city}\n State: {self.state}\n "
                f"Zip Code: {self.zip_code}\n Phone Number: {self.phone_number}\nEmail: {self.email}\n")
