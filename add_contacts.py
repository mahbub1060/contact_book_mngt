import validate_contact
import save_all_contacts

def add_contact(contacts):
    
  #  """Add a new contact."""
    try:
        name = input("Enter Name: ").strip()
        email = input("Enter Email: ").strip()
        phone = input("Enter Phone Number: ").strip()
        address = input("Enter Address: ").strip()
        
        validate_contact.validate_contact(name, email, phone, address)       
        if phone in contacts:
            print("\nError: This phone number is already assigned to another contact.\n")
            return
        
        contacts[phone] = {'Name': name, 'Email': email, 'Phone Number': phone, 'Address': address}
        save_all_contacts.save_contacts(contacts)
        print("\nContact added successfully!\n")
    
    except ValueError as e:
        print(f"\nError: {e}\n")
    
    
    
    