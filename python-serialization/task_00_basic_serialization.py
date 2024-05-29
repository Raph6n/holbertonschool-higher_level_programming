#!/usr/bin/python3
"""
Module for basic serialization and deserialization of Python dictionaries
"""

import json

def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary to a JSON file.

    Args:
        data (dict): The Python dictionary to serialize.
        filename (str): The filename of the output JSON file.
                        If the file already exists, it will be replaced.
    """
    # Open the file in write mode. If it exists, it will be overwritten.
    with open(filename, 'w') as file:
        # Serialize the dictionary to the file in JSON format.
        json.dump(data, file)

def load_and_deserialize(filename):
    """
    Loads and deserializes JSON data from a file to a Python dictionary.

    Args:
        filename (str): The filename of the input JSON file.

    Returns:
        dict: The deserialized Python dictionary.
    """
    # Open the file in read mode.
    with open(filename, 'r') as file:
        # Load and deserialize the JSON data from the file to a dictionary.
        return json.load(file)

