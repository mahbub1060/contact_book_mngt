import add_contacts
import display_all_contacts
import delete_contact
import search_contact
import load_contacts

   
contacts = load_contacts.load_contacts()
    
while True:
    print("\nContact Book Management System")
    print("1. Display All Contacts")
    print("2. Add New Contact")
    print("3. Delete Contact")
    print("4. Search Contact")
    print("5. Exit")
        
    choice = input("Choose an option: ").strip()
        
    if choice == '1':
        display_all_contacts.display_contacts(contacts)
    elif choice == '2':
        add_contacts.add_contact(contacts)
    elif choice == '3':
        delete_contact.delete_contact(contacts)
    elif choice == '4':
        search_contact.search_contact(contacts)
    elif choice == '5':
        print("\nExiting... Goodbye!")
        break
    else:
         print("\nInvalid option. Please choose again.\n")
