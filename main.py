# ------------------------------------------
#   Contact Book - Python CLI App
#   Description:
#       A simple command-line contact manager
#       that lets users add, view, delete, and
#       search contacts. Data is stored in
#       contacts.txt
# ------------------------------------------

CONTACT_FILE = "contacts.txt"


def add_contact():
    """Add a new contact."""
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email (optional): ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    if not phone.isdigit():
        print("Phone must contain only numbers.")
        return

    with open(CONTACT_FILE, "a", encoding="utf-8") as file:
        file.write(f"{name},{phone},{email}\n")

    print("Contact added successfully.")


def show_contacts():
    """Show all saved contacts."""
    try:
        with open(CONTACT_FILE, "r", encoding="utf-8") as file:
            contacts = file.readlines()
    except FileNotFoundError:
        print("No contacts found.")
        return

    if not contacts:
        print("Contact list is empty.")
        return

    print("\n--- Contact List ---")
    for index, c in enumerate(contacts, start=1):
        name, phone, email = c.strip().split(",")
        print(f"{index}. {name} | {phone} | {email}")
    print("---------------------\n")


def search_contact():
    """Search for a contact by name."""
    keyword = input("Enter name to search: ").strip().lower()

    try:
        with open(CONTACT_FILE, "r", encoding="utf-8") as file:
            contacts = file.readlines()
    except FileNotFoundError:
        print("No contacts found.")
        return

    matches = [c.strip() for c in contacts if keyword in c.lower()]

    if not matches:
        print("No matching contacts.")
        return

    print("\n--- Search Results ---")
    for c in matches:
        print("- " + c)
    print("----------------------\n")


def delete_contact():
    """Delete a contact by number."""
    try:
        with open(CONTACT_FILE, "r", encoding="utf-8") as file:
            contacts = file.readlines()
    except FileNotFoundError:
        print("No contacts to delete.")
        return

    if not contacts:
        print("No contacts to delete.")
        return

    show_contacts()
    choice = input("Enter the number to delete: ")

    if not choice.isdigit():
        print("Invalid input.")
        return

    index = int(choice)

    if not (1 <= index <= len(contacts)):
        print("Index out of range.")
        return

    removed = contacts.pop(index - 1)

    with open(CONTACT_FILE, "w", encoding="utf-8") as file:
        file.writelines(contacts)

    print(f"Deleted: {removed.strip()}")


def main():
    while True:
        print("""
===== CONTACT BOOK =====
1. Add Contact
2. Show Contacts
3. Search Contact
4. Delete Contact
5. Exit
========================
        """)

        choice = input("Choose an option: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            show_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")
            

if __name__ == "__main__":
    main()
