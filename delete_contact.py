import save_all_contacts

def delete_contact(contacts):
    """Delete a contact."""
    phone = input("Enter the phone number of the contact to delete: ").strip()
    if phone in contacts:
        del contacts[phone]
    
        save_all_contacts.save_contacts(contacts)
        print("\nContact deleted successfully!\n")
    
    else:
        print("\nError: No contact found with that phone number.\n")
                