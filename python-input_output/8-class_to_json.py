#!/usr/bin/python3
""" A function that returns an object (Python data structure)
    represented by a JSON string.
"""
import json


def class_to_json(obj):
    """Returns a JSON representation of the given object."""
    return json.dumps(obj.__dict__)
