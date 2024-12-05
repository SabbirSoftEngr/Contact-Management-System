def SearchContact(all_contacts):
    Phone_number = input("Enter a phone number to search: ").strip()
    found = False
    for contact_search in all_contacts:
        if contact_search["Phone_Number"] == Phone_number:
            print("Contact found:")
            print(contact_search)
            found = True
            break
        else:
            print("No contact found with the given phone number.")
