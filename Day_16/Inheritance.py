#Inheritance = Allows a class(Child Class) to acquire properties and methods of another class (parent class)
#-- Inheritance is good for code reusability and Hierarchical Classification.

#example 1

class Animal:

    def __init__(self):
        print("This is an Animal")

    def eating(self):
        print("Animal is Eating")

    def sound(self):
        print("Animal is making a Sound")

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("This is a Dog")

    def sound(self):
        print("Bark")

    def eating(self):
        print("Dog eats")

d = Dog()
d.eating()
d.sound()

#EXAMPLE 2
