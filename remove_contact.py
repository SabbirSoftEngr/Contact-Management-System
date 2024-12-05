def remove_contact(all_contacts):
    if len(all_contacts) == 0:
        print("No contacts to remove.")
    else:
        try:
            phone_number_to_remove = input("Enter phone number to remove: ").strip()
            found = False
            for contact in all_contacts:
                if contact["Phone_Number"] == phone_number_to_remove:
                    all_contacts.remove(contact)
                    found = True
                    print("Contact removed successfully!")
                    break
            if not found:
                print("Contact not found in the list.")
        except ValueError:
            print("Invalid phone number. Please enter a Valid Phone Number.")
    return all_contacts

