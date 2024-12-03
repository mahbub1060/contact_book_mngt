import csv
import os

# Constants
FILE_NAME = "contacts.csv"

def load_contacts():
    # """Load contacts from the file into a dictionary."""
    contacts = {}
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                contacts[row['Phone Number']] = row
    return contacts