class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}\nPhone: {self.phone}\nEmail: {self.email}"


class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"Contact {contact.name} added successfully.")

    def display_contacts(self):
        if not self.contacts:
            print("No contacts in the book.")
        else:
            print("\nContact Book:")
            for contact in self.contacts:
                print(contact)

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Manager Menu:")
        print("1. Add Contact")
        print("2. Display Contacts")
        print("3. Exit")

        choice = input("Enter your choice (1,2,3): ")

        if choice == "1":
            name = input("Enter contact name: ")
            phone = input("Enter contact phone number: ")
            email = input("Enter contact email address: ")

            new_contact = Contact(name, phone, email)
            contact_book.add_contact(new_contact)

        elif choice == "2":
            contact_book.display_contacts()

        elif choice == "3":
            print("Exiting the Contact Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()