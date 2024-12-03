

def search_contact(contacts):
    
    # Search for a contact.
    
    query = input("Enter Name, Email, Phone Number, or Address to search: ").strip().lower()
    
    results = [
        contact for contact in contacts.values()
        if query in contact['Name'].lower() or
           query in contact['Email'].lower() or
           query in contact['Phone Number'].lower() or
           query in contact['Address'].lower()
    ]
    if results:
        print("\nSearch Results:")
        print("-" * 50)
        for contact in results:
            print(f"Name       : {contact['Name']}")
            print(f"Email      : {contact['Email']}")
            print(f"Phone      : {contact['Phone Number']}")
            print(f"Address    : {contact['Address']}")
            print("-" * 50)
    else:
        print("\nNo matching contacts found.\n")
    