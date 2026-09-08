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
## in this One Ill Talk About the super().__init__() method
#super() function is used to call methods from the Parent class(Super Class)
#__init__ is used after the super() called the inherited attributs from the parent class

class Animal:

    def __init__(self,name,sound):
        self.name = name
        self.sound = sound

    def info(self):
        print("Animal Name:",self.name)
        print("Animal Makes a Sound:",self.sound)

class Dog(Animal):

    def __init__(self,name,breed,sound):
        super().__init__(name, sound)
        self.breed = breed

    def details(self):
        print(f"Dog name:{self.name}")

    def show_breed(self):
        print(f"Dog breed:{self.breed}")

    def Dog_sound(self):
        print("Woof!",self.sound)

d = Dog(name="Johnny",breed= "Husky", sound= "Woof!")
d.info()
d.show_breed()
d.Dog_sound()




