from random_words import RandomWords
from core.responses import get_face
"""
For special command and chat
"""

rw = RandomWords()


def handle_commad(command):
    parts = command.split(" ")
    cmd   = parts[0].lower()
    args  = parts[1:]

    # help
    if cmd == "/help":
        return "Commands:\n/mood <name>\n/random\n/about\n/help\n/exit"
    
    # get random widget from the respomses.py
    elif cmd =="/mood":
        return get_face()

    # gives random word
    elif cmd =="/random":
        rw = RandomWords()
        return rw.random_word()
    
    # About Message
    elif cmd =="/about":
        return "Moji 1.0 ~ Created By Atharv Nawale..."
    
    # To exit using the command
    elif cmd =="/exit":
        return exit()

    else:
        return "Unknown command. Type /help"

def handle_chat(text):
    return text

# grnerates random word
def random_word():
    word = rw.random_word()
    return word

