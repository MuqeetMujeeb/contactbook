class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}\nPhone: {self.phone_number}\nEmail: {self.email}\nAddress: {self.address}\n"


class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone_number, email, address):
        contact = Contact(name, phone_number, email, address)
        self.contacts.append(contact)
        print("Contact added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            print("Contact List:")
            for i, contact in enumerate(self.contacts, start=1):
                print(f"{i}. {contact.name} - {contact.phone_number}")

    def search_contact(self, search_term):
        results = [contact for contact in self.contacts if search_term.lower() in contact.name.lower() or search_term in contact.phone_number]
        if results:
            for contact in results:
                print(contact)
        else:
            print("No contacts found.")

    def update_contact(self, search_term):
        contact = self.find_contact(search_term)
        if contact:
            print("Updating contact details. Press Enter to skip updating a field.")
            name = input(f"New name ({contact.name}): ") or contact.name
            phone_number = input(f"New phone number ({contact.phone_number}): ") or contact.phone_number
            email = input(f"New email ({contact.email}): ") or contact.email
            address = input(f"New address ({contact.address}): ") or contact.address

            contact.name = name
            contact.phone_number = phone_number
            contact.email = email
            contact.address = address

            print("Contact updated successfully!")
        else:
            print("Contact not found.")

    def delete_contact(self, search_term):
        contact = self.find_contact(search_term)
        if contact:
            self.contacts.remove(contact)
            print("Contact deleted successfully!")
        else:
            print("Contact not found.")

    def find_contact(self, search_term):
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term == contact.phone_number:
                return contact
        return None


def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_book.add_contact(name, phone_number, email, address)

        elif choice == '2':
            contact_book.view_contacts()

        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            contact_book.search_contact(search_term)

        elif choice == '4':
            search_term = input("Enter name or phone number to update: ")
            contact_book.update_contact(search_term)

        elif choice == '5':
            search_term = input("Enter name or phone number to delete: ")
            contact_book.delete_contact(search_term)

        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
