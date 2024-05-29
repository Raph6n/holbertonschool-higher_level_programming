#!/usr/bin/python3
""" 
A class Student that defines a student with public instance attributes: 
first_name, last_name, and age.
"""

class Student:
    """ Initializes the attributes. """
    def __init__(self, first_name, last_name, age):
        """ Initializes the student with first_name, last_name, and age. """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    """ A public method that retrieves a dictionary representation
        of a Student instance.
    """
    def to_json(self, attrs=None):
        """ Returns a dictionary representation of the instance. """
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for attribute_name in attrs:
                if attribute_name in self.__dict__:
                    new_dict[attribute_name] = self.__dict__[attribute_name]
            return new_dict

    def reload_from_json(self, json):
        """ Replaces all attributes of the Student instance from a JSON dictionary. """
        for key, value in json.items():
            setattr(self, key, value)
