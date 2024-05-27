#!/usr/bin/python3
def append_write(filename="", text=""):
    """Append a string to the end of a text file (UTF-8) and return the number of characters added."""
    with open(filename, 'a', encoding='utf-8') as file:
        num_chars_added = file.write(text)
    return num_chars_added
