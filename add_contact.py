from save_contact import save_contact

def add_contact(all_contacts):
    name = input("Enter Contact Name: ")
    email = input("Please Enter A Valid Email Address: ")
    Phone_number = int(input("Please Enter A Valid unique Phone Number: "))
    address = input("Please Enter Contact Address: ")
    nationality = input("Enter Contact Nationality: ")
    religion = input("Enter Contact Religion: ")

    if Phone_number in all_contacts:
        print('This Phone number is alreay exist in the system')

    else:
        all_contacts.append({
            'Name': name,
            'Email': email,
            'Phone_Number': Phone_number,
            'Address': address,
            'Nationality': nationality,
            'Religion': religion
        })

    save_contact(all_contacts)
    print("Contact added Successfully")
    return all_contacts