class Contact:
    def __init__(info, name, phone_number, email, address):
        info.name = name
        info.phone_number = phone_number
        info.email = email
        info.address = address

class ContactBook:
    def __init__(info):
        info.contacts = []

    def add_contact(info, contact):
        info.contacts.append(contact)

    def view_contacts(info):
        if not info.contacts:
            print("No contacts found.")
        else:
            for i, contact in enumerate(info.contacts, start=1):
                print(f"{i}. Name: {contact.name}, Phone: {contact.phone_number}")

    def search_contacts(info, search_term):
        results = [contact for contact in info.contacts if search_term.lower() in contact.name.lower() or search_term in contact.phone_number]
        if results:
            info.view_contacts(results)
        else:
            print("No contacts found.")

    def update_contact(info, index, new_contact):
        if 0 <= index < len(info.contacts):
            info.contacts[index] = new_contact
            print("Contact updated successfully.")
        else:
            print("update failed.")

    def delete_contact(info, index):
        if 0 <= index < len(info.contacts):
            del info.contacts[index]
            print("Contact deleted successfully.")
        else:
            print("Invalid index.")

def add_contact(contact_book):
    name = input("Enter name: ")
    phone_number = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contact = Contact(name, phone_number, email, address)
    contact_book.add_contact(contact)
    print("Contact added successfully.")

def search_contacts(contact_book):
    search_term = input("Enter name or phone number to search: ")
    contact_book.search_contacts(search_term)

def update_contact(contact_book):
    index = int(input("Enter the index of the contact to update: ")) - 1
    if 0 <= index < len(contact_book.contacts):
        name = input("Enter name: ")
        phone_number = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        new_contact = Contact(name, phone_number, email, address)
        contact_book.update_contact(index, new_contact)
    else:
        print("update failed")

def delete_contact(contact_book):
    index = int(input("Enter the index of the contact to delete: ")) - 1
    contact_book.delete_contact(index)

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Organizer")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact(contact_book)

        elif choice == "2":
            contact_book.view_contacts()

        elif choice == "3":
            search_contacts(contact_book)

        elif choice == "4":
            update_contact(contact_book)

        elif choice == "5":
            delete_contact(contact_book)

        elif choice == "6":
            print("Program terminated. Goodbye!")
            break

        else:
            print("Invalid input. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
