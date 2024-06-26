def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def add_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return f"Phone number updated for {name}."
    else:
        contacts[name] = phone
        return "Contact added."

def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return f"Phone number updated for {name} to {phone}."
    else:
        return f"Contact {name} does not exist."

def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return f"{name} phone number is {contacts[name]}."
    else:
        return f"Contact {name} does not exist."

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
        elif command == "all":
            print(contacts)
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "show":
            print(show_phone(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
