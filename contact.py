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
        all_contacts = remove_contact(all_contacts)
    elif menu == "0":
        print('Thanks For Using Contact Management Application')
        

else:
    print('Please Select A Valid Number.')
