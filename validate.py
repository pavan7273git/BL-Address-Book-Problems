import re
from functools import wraps

def validate_field(field_name, value):
    """Validates input fields based on regex rules."""
    while True:
        if field_name in ["first_name", "last_name"]:
            if re.match(r"^[A-Z][a-zA-Z]{2,}$", value):
                return value
            else:
                print(f"Invalid {field_name}, must start with capital letter and have at least 3 characters.")
                return False

        elif field_name == "email":
            if re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", value):
                return value
            else:
                print("Invalid Email format.")
                return False

        elif field_name == "zip_code":
            if re.match(r"^\d{5,6}$", value):
                return value
            else:
                print("Invalid ZIP Code, must be 5-6 digits.")
                return False

        elif field_name == "phone_number":
            if re.match(r"^\d{10}$", value):
                return value
            else:
                print("Invalid Phone Number, must be 10 digits.")
                return False

        return value

def validate_data(data_dict):
    """Validates all fields in a dictionary before storing in Address Book."""
    validated_data = {key: validate_field(key, value) for key, value in data_dict.items()}
    
    if False in validated_data.values():
        print("\nValidation failed!")
        return False

    return validated_data

from functools import wraps

def validation_wrapper(func):
    @wraps(func)
    def wrapper(address_book, contact_data):
        validated_data = validate_data(contact_data)  # Validate contact data

        if not isinstance(validated_data, dict):  # Check if validation failed
            print("\nValidation failed! Contact not added.")
            return

        return func(address_book, validated_data)  # Call function with validated data

    return wrapper
