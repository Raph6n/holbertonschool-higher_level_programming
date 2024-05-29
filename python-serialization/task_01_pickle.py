#!/usr/bin/python3
import pickle

class CustomObject:
    def __init__(self, name, age, is_student):
        """Initialize the CustomObject with name, age, and is_student attributes."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the attributes of the CustomObject."""
        print("Name:", self.name)
        print("Age:", self.age)
        print("Is Student:", self.is_student)

    def serialize(self, filename):
        """Serialize the CustomObject instance to a file using pickle."""
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
            print("Serialization successful.")
        except Exception as e:
            print("Serialization failed:", e)

    @classmethod
    def deserialize(cls, filename):
        """Deserialize a CustomObject instance from a file using pickle."""
        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
            print("Deserialization successful.")
            return obj
        except FileNotFoundError:
            print("File not found.")
        except pickle.UnpicklingError as e:
            print("Deserialization failed:", e)
        return None
