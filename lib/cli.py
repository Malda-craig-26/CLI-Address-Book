from models.contact import Contact
from models.address import Address
from helpers import get_int_input, get_non_empty_input
from db.connection import setup_db

def main_menu():
    print("""
--- Address Book CLI ---
1. Create Contact
2. Delete Contact
3. View All Contacts
4. Find Contact by Name
5. View Contact's Addresses
6. Add Address to Contact
7. Delete Address
8. View All Addresses
9. Exit
""")

def main():
    setup_db()  

    while True:
        main_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            name = get_non_empty_input("Enter contact name: ")
            email = get_non_empty_input("Enter contact email: ")
            contact = Contact.create(name, email)
            print(f"Created contact: {contact}")

        elif choice == "2":
            contact_id = get_int_input("Enter contact ID to delete: ")
            if Contact.delete(contact_id):
                print(f"Deleted contact with ID {contact_id}")
            else:
                print("Contact not found.")

        elif choice == "3":
            contacts = Contact.get_all()
            for c in contacts:
                print(c)

        elif choice == "4":
            name = get_non_empty_input("Enter contact name: ")
            contact = Contact.find_by_name(name)
            if contact:
                print(contact)
            else:
                print("Contact not found.")

        elif choice == "5":
            contact_id = get_int_input("Enter contact ID: ")
            addresses = Address.get_by_contact(contact_id)
            if addresses:
                for a in addresses:
                    print(a)
            else:
                print("No addresses found or contact does not exist.")

        elif choice == "6":
            contact_id = get_int_input("Enter contact ID: ")
            location = get_non_empty_input("Enter address: ")
            address = Address.create(location, contact_id)
            if address:
                print(f"Address added: {address}")
            else:
                print("Failed to add address. Check contact ID.")

        elif choice == "7":
            address_id = get_int_input("Enter address ID to delete: ")
            if Address.delete(address_id):
                print(f"Deleted address with ID {address_id}")
            else:
                print("Address not found.")

        elif choice == "8":
            addresses = Address.get_all()
            for a in addresses:
                print(a)

        elif choice == "9":
            print("Exiting Address Book. Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
