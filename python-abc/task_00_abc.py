#!/usr/bin/python3
"""Abstract class Animal with Dog and Cat subclasses."""


from abc import ABC, abstractmethod

class Animal(ABC):
    """Abstract base class."""

    @abstractmethod
    def sound(self):
        """Must be implemented by subclasses."""
        pass


class Dog(Animal):
    """Dog class, implements sound()."""
    def sound(self):
        """Returns dog sound."""
        return ("Bark")


class Cat(Animal):
    """Cat class, implements sound()."""
    def sound(self):
        """Returns cat sound."""
        return ("Meow")
