from save_contact import save_contact  # Assuming this function is defined elsewhere.

def add_contact(all_contacts):
    while True:

        name = input("Enter Contact Name: ").strip()
        if name.isalpha(): 
            break
        else:
            print("Name must be written in letters. Please try again.")

    while True:

        email = input("Please Enter A Valid Email Address: ").strip()
        if "@" in email and "." in email:
            break
        else:
            print("Invalid email format. Please include '@' and a domain.")

    while True:

        phone_number = input("Please Enter A Valid Unique Phone Number: ").strip()
        if phone_number.isdigit() and phone_number not in all_contacts:
            break
        elif phone_number in all_contacts:
            print("This phone number already exists in the system.")
        else:
            print("Phone number should only contain digits. Please try again.")

    while True:

        address = input("Please Enter Contact Address: ").strip()
        if address.isalpha() or ',' or ' ' in address:
            break
        else:
            print("Address must be write in Alphabetically")

    while True:

        nationality = input("Enter Contact Nationality: ").strip()
        if nationality.isalpha():
            break
        else:
            print("Nationality name must be written in letters. Please try again.")

    while True:

        religion = input("Enter Contact Religion: ").strip()
        if religion.isalpha():
            break
        else:
            print("Religion name must be written in letters. Please try again.")

    all_contacts.append({
        'Name': name,
        'Email': email,
        'Phone_Number': phone_number,
        'Address': address,
        'Nationality': nationality,
        'Religion': religion
    })

    save_contact(all_contacts)
    print("Contact added successfully.")
    return all_contacts
