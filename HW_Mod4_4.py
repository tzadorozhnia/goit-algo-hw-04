def parse_input(user_input: str):
    """Парсить введений рядок у команду та аргументи."""
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def add_contact(args, contacts: dict) -> str:
    """Додає новий контакт у словник."""
    if len(args) != 2:
        return "Usage: add <name> <phone>"
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts: dict) -> str:
    """Змінює телефон існуючого контакту."""
    if len(args) != 2:
        return "Usage: change <name> <new_phone>"
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    return f"Contact '{name}' not found."

def show_phone(args, contacts: dict) -> str:
    """Показує телефон за ім’ям."""
    if len(args) != 1:
        return "Usage: phone <name>"
    name = args[0]
    if name in contacts:
        return contacts[name]
    return f"Contact '{name}' not found."

def show_all(contacts: dict) -> str:
    """Виводить усі збережені контакти."""
    if not contacts:
        return "No contacts saved."
    result = []
    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")
    return "\n".join(result)

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()