def display_contacts(contacts):
    
    #Display all contacts in a neat format.
    
    if not contacts:
        print("\nNo contacts available.\n")
        return
    
    print("\nSaved Contacts:")
    print("-" * 50)
    
    for contact in contacts.values():
        print(f"Name       : {contact['Name']}")
        print(f"Email      : {contact['Email']}")
        print(f"Phone      : {contact['Phone Number']}")
        print(f"Address    : {contact['Address']}")
        print("-" * 50)