def display_menu():
    print("\n=== CONTACT MANAGER ===")
    print("1. Add contact")
    print("2. View all contacts")
    print("3. Search contact by name")
    print("4. Exit")

def add_contact(filename):
    name = input("Enter contact name: ").strip()
    phone = input("Enter phone number: ").strip()

    if name and phone:
        with open(filename, "a") as f:
            f.write(f"{name},{phone}\n")
        print("Contact added.")
    else:
        print("Name and phone number cannot be empty.")

def view_contacts(filename):
    print("\n--- All Contacts ---")
    try:
        with open(filename, "r") as f:
            content = f.read()
            if content.strip():
                print(content.strip())
            else:
                print("No contacts found.")
    except FileNotFoundError:
        print("No contact file found.")

def search_contact(filename):
    name_to_search = input("Enter name to search: ").strip().lower()
    found = False

    try:
        with open(filename, "r") as f:
            for line in f:
                name, phone = line.strip().split(",", 1)
                if name.lower() == name_to_search:
                    print(f"Found: {name} - {phone}")
                    found = True
                    break
        if not found:
            print("Contact not found.")
    except FileNotFoundError:
        print("No contact file found.")

def main():
    filename = "contacts.txt"
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()
        if choice == "1":
            add_contact(filename)
        elif choice == "2":
            view_contacts(filename)
        elif choice == "3":
            search_contact(filename)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 to 4.")

if __name__ == "__main__":
    main()
