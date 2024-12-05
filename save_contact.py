import csv

def save_contact(all_contact):
    with open('all_contacts.csv', 'w') as file:
        for contact in all_contact:
            line = f"{contact['Name']}, {contact['Email']}, {contact['Phone_Number']}, {contact['Address']}, {contact['Nationality']}, {contact['Religion']}\n"
            file.write(line)