#!/usr/bin/python3

from abc import ABC, abstractmethod

class Animal(ABC):
    """
    Abstract class representing an Animal.
    """
    @abstractmethod
    def sound(self):
        """
        Abstract method that must be implemented by all subclasses.
        This method should return the sound made by the animal.
        """
        pass

class Dog(Animal):
    """
    Class representing a Dog.
    Inherits from the Animal class and implements the sound method.
    """
    def sound(self):
        """
        Returns the sound made by a dog.
        """
        return "Bark"

class Cat(Animal):
    """
    Class representing a Cat.
    Inherits from the Animal class and implements the sound method.
    """
    def sound(self):
        """
        Returns the sound made by a cat.
        """
        return "Meow"
