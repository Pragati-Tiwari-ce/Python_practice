# Abstraction in Python OOP:
# - Animal is an abstract base class inheriting from ABC
# - make_sound() is an abstract method that must be implemented by child classes
# - Lion and Cow provide concrete implementations of make_sound()
# - Demonstrates how abstraction hides implementation details and enforces rules on subclassesfrom abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Lion(Animal):
    def make_sound(self):
        print("roar")

class Cow(Animal):
    def make_sound(self):
        print("moo")
lion=Lion()
cow=Cow()
lion.make_sound()
cow.make_sound()
#a=Animal() #not possible due to abstraction
    