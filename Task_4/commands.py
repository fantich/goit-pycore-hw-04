from storage import contacts

def hello():
    return "How can I help you?"

def add_contact(args):
    try:
        name, phone = args.split(maxsplit=1)
        contacts[name] = phone
        return f"Contact {name} added."
    except ValueError:
        return "Invalid format. Use: add username phone"

def change_contact(args):
    try:
        name, phone = args.split(maxsplit=1)
        if name in contacts:
            contacts[name] = phone
            return f"Contact {name} updated."
        return f"Contact {name} not found."
    except ValueError:
        return "Invalid format. Use: change username phone"

def get_phone(args):
    name = args.strip()
    return contacts.get(name, "Contact not found.")

def all_contacts():
    if contacts:
        return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
    return "No contacts found."

def process_command(user_input):
    command, *args = user_input.split(maxsplit=1)
    args = args[0] if args else ""

    commands = {
        "hello": hello,
        "add": add_contact,
        "change": change_contact,
        "phone": get_phone,
        "all": all_contacts,
    }
    
    return commands.get(command, lambda: "Unknown command")(args)
