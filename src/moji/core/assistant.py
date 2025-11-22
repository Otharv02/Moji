"""
For special command and chat
"""

def handle_commad(command):
    parts = command.split(" ")
    cmd   = parts[0].lower()
    args  = parts[1:]

    if cmd == "/help":
        return "Commands:\n/mood <name>\n/clear\n/help"

    else:
        return "Unknown command. Type /help"

def handle_chat(text):
    return text

