import re

def validate_field(field_name, value):
    """
    Validates a single field based on predefined rules.
    Returns the valid value or False if invalid.
    """
    if field_name in ["first_name", "last_name"]:
        return value if re.match(r"^[A-Z][a-z]{2,}$", value.title()) else False

    elif field_name == "mail":
        # Updated email regex for stricter validation
        return value if re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", value) else False

    elif field_name == "zip_code":
        return value if re.match(r"^\d{5,6}$", value) else False

    elif field_name == "phone_number":
        return value if re.match(r"^\d{10}$", value) else False

    return value  # No validation needed for other fields

def validate_data(data_dict):
    """ Validates all fields in a dictionary before storing in Address Book. """
    validated_data = {key: validate_field(key, value) for key, value in data_dict.items()}
    
    if False in validated_data.values():
        return {key: False if val is False else val for key, val in validated_data.items()}
    
    return validated_data

def validation_wrapper(func):
    """ Decorator that validates input before executing function. """
    def wrapper(contact_data):
        validated_data = validate_data(contact_data)
        if False in validated_data.values():
            print("\nValidation failed! One or more fields are incorrect.")
            return
        return func(validated_data)
    return wrapper
