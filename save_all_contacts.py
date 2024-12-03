import csv
import load_contacts

FILE_NAME = "contacts.csv"

def save_contacts(contacts):
    
    #Save all contacts to the file.
    
    with open(FILE_NAME, mode="w", newline='') as fp:
        fieldnames = ['Name', 'Email', 'Phone Number', 'Address']
        writer = csv.DictWriter(fp, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(contacts.values())
        