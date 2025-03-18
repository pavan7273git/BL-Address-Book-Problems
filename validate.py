import re

def validate_field(field_name, value):
    """
    Validates a single field based on predefined rules.
    Returns True if valid, otherwise False.
    """
    if field_name in ["first_name", "last_name"]:
        return bool(re.match(r"^[A-Z][a-z]{2,}$", value.title()))

    elif field_name == "mail":
        return bool(re.match(r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$", value))

    elif field_name == "zip_code":
        return bool(re.match(r"^\d{5,6}$", value))

    elif field_name == "phone_number":
        return bool(re.match(r"^\d{10}$", value))

    else:
        return True  # No validation needed for other fields

def validate_data(data_dict):
    """
    Validates all fields in a dictionary.
    If any field is invalid, prints "Validation failed" and asks for all inputs again.
    """
    while True:
        invalid_fields = [key for key, value in data_dict.items() if not validate_field(key, value)]
        
        if not invalid_fields:
            return data_dict  # Return validated data if everything is valid
        
        print("\n Validation failed. Please enter all details again.\n")
        
        # Re-collect all fields
        data_dict = {
            "first_name": input("Enter First Name (Starts with a capital letter, min 3 chars): "),
            "last_name": input("Enter Last Name (Starts with a capital letter, min 3 chars): "),
            "address": input("Enter Address: "),
            "city": input("Enter City: "),
            "state": input("Enter State: "),
            "zip_code": input("Enter ZIP Code (5-6 digits): "),
            "phone_number": input("Enter Phone Number (10 digits): "),
            "mail": input("Enter Email: ")
        }

def validation_wrapper(func):
    """ Decorator that validates input before executing function. """
    def wrapper(contact_data):
        validated_data = validate_data(contact_data)
        return func(validated_data)
    return wrapper
