from search_contact import SearchContact
from add_contact import add_contact
from view_contact import view_contact
from save_contact import save_contact

all_contacts = []

while True:
    print("Welcome to Contact Management System")
    print("1. Add Contacts")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Remove Contact Using Phone Number")
    print("0. Exit to Home")


    menu = input('select any number: ')

    if menu == "1":
        all_contacts = add_contact(all_contacts)
    elif menu == "2":
            if len(all_contacts) == 0:
                print("No contacts found in the list.")
            else:
                view_contact(all_contacts)
    elif menu =="3":
        SearchContact(all_contacts)
    elif menu == "4":
        if len(all_contacts) == 0:
            print("No contacts to remove.")
        else:
            phone_number_to_remove = int(input("Enter phone number to remove: "))
            found = False
            for contact in all_contacts:
                if contact["Phone_Number"] == phone_number_to_remove:
                    all_contacts.remove(contact)
                    found = True
                    print("Contact removed successfully!")
                    break

                else:
                    print("Contact not found in the list")
    elif menu == "0":
        print('Thanks For Using Contact Management Application')
        

else:
    print('Please Select A Valid Number.')