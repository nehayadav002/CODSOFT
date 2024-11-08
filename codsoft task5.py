class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added successfully!")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print("Contact deleted successfully!")
                return
        print("Contact not found.")

    def display_contacts(self):
        if self.contacts:
            print("Contacts:")
            for contact in self.contacts:
                print(f"Name: {contact.name}, Phone: {contact.phone_number}, Email: {contact.email}")
        else:
            print("Contact book is empty.")

def main():
    contact_book = ContactBook()

    while True:
        print("\n1. Add Contact\n2. Delete Contact\n3. Display Contacts\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            contact = Contact(name, phone_number, email)
            contact_book.add_contact(contact)
        elif choice == '2':
            name = input("Enter the name of contact to delete: ")
            contact_book.delete_contact(name)
        elif choice == '3':
            contact_book.display_contacts()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
