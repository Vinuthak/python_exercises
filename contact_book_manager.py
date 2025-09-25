# Add new contacts (stores in dictionary).

# View all saved contacts.

# Search for a contact by name.

# Delete a contact.

# Exit option to stop the program.

contacts = {}

# View all saved contacts.
def view_contacts():
    if  not contacts:
        print("No contacts yet")
    else:
        for name, number in contacts.items():
            print(f"{name} : {number}")

# Add new contacts (stores in dictionary).
def add_contact(name,number):
    contacts[name] = number
    print(f"Contact {name} with {number} is added.")

# Search for a contact by name.
def search_contact(name):
    if name in contacts:
        print(f"{name} :{ contacts[name]}")
    else:
        print("Contact not found.")

# update a contact
def update_contact(name):
    # contacts => { 'a': 11, 'b': 22 }
    # contacts['a'] => 11
    if contacts[name]:
        new_contact_number = input("Enter a new contact number: ")
        contacts[name] = new_contact_number
        print(f"Updated {name} with {new_contact_number}")
    else:
        print("No contact with that name.")
# Delete a contact.

def delete_contact(name):
    if name in contacts:
        contacts.pop(name)
        print(f"Removed : {name} from contacts.")
    else:
        print("THere is no contact with that name.")

while True:
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update number")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        contact = input("Enter number: ")
        add_contact(name,contact)
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        name = input("Enter a name to search: ")
        search_contact(name)
    elif choice == "4":
         name = input("Enter the name of the contact to update: ")
         update_contact(name)
    elif choice == "5":
        input("Enter a name to delete: ")
        delete_contact(name)
    elif choice =="6":
        break
    else:
        print("Invalid input!")