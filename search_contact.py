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
