#!/usr/bin/python3
"""Module for loading an object from a JSON file."""
import json

def load_from_json_file(file_name):
    """Load an object from a JSON file.
    
    Args:
        file_name (str): The name of the JSON file.

    Returns:
        object: The object loaded from the JSON file.
    """
    # Open the file in read mode and specify UTF-8 encoding
    with open(file_name, 'r', encoding='utf-8') as file:
        # Load the object from the JSON file
        return json.load(file)
