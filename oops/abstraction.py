# Abstraction in Python is the process of hiding the real implementation of an application from the user and emphasizing only on usage of it

# In Python, an abstraction is used to hide the irrelevant data/class in order to reduce the complexity.
# It also enhances the application efficiency
# In Python, abstraction can be achieved by using abstract classes and interfaces.
# Python provides the abc module to use the abstraction in the Python program

from abc import ABC, abstractclassmethod, abstractmethod


class Animal(ABC):
    @abstractmethod
    def move(self):
        pass


class Human(Animal):
    def move(self):
        print("I can walk and run")


class Snake(Animal):
    def move(self):
        print("I can crawl")


class Dog(Animal):
    def move(self):
        print("I can bark")


class Lion(Animal):
    def move(self):
        print("I can roar")


# Driver code
R = Human()
R.move()

K = Snake()
K.move()

R = Dog()
R.move()

K = Lion()
K.move()
