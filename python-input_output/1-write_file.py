#!/usr/bin/python3
def write_file(filename="", text=""):
    """Write a string to a text file in UTF-8 encoding and return the number of characters written."""
    with open(filename, 'w', encoding='utf-8') as file:
        num_chars_written = file.write(text)
    return num_chars_written
