def validate_contact(name, email, phone, address):
    
    #"""Validate contact details."""
    
    if not name.isalpha():
        raise ValueError("The contact's name must only contain alphabetic characters.")
    if not phone.isdigit():
        raise ValueError("The phone number must be a numeric value.")
    if '@' not in email or '.' not in email.split('@')[-1]:
        raise ValueError("The email address is invalid.")
    if not address.strip():
        raise ValueError("The address cannot be empty.")