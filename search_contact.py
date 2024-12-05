"""
def Search_a_contact(all_contacts):
    contact = int(input("Enter a phone number to search: "))
    found = False
    for contact in all_contacts:
        if contact["phone_number"] == phone_number:
            print(f"contact Found - Name: {Search_a_contact['name']}, Phone: {Search_a_contact['phone']}, Email: {Search_a_contact['email']}, Address: {Search_a_contact['address']}, Nationality: {Search_a_contact['nationality']}, Religion: {Search_a_contact['religion']}")
            print(contact)
            found = True
            break
    if not found:
        print("No contact found with the given phone number.")
"""



def SearchContact(all_contacts):
    Phone_number = int(input("Enter a phone number to search: "))
    found = False
    for contact_search in all_contacts:
        if contact_search["Phone_Number"] == Phone_number:
            print("Contact found:")
            print(contact_search)
            found = True
            break
    if not found:
        print("No contact found with the given phone number.")