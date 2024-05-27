#!/usr/bin/python3

def read_file(filename=""):
    """
    This function reads the content of a text file encoded in UTF-8
    and prints the content to the standard output (stdout).

    Parameters:
    filename (str): the path to the file to read. If no path is provided, 
                    an empty string will be used by default.
    """
    # Using the 'with' statement to manage the file
    with open(filename, 'r', encoding='utf-8') as file:
        # Read the file content and print it
        print(file.read())
