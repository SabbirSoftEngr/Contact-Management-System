import csv

filename = "all_contacts.csv"

def load_contacts_from_file(filename):
    all_contacts = []

    try:
        with open(filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                all_contacts.append(row)
        print("Contacts loaded successfully.")

    except FileNotFoundError:
        print("No previous contacts found. Starting fresh.")
    return all_contacts
