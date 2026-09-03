#Polymorphism - it allows Functions or Methods with the same name ti work differently depending on the type of object they are acting upon 
# this makes the code reusable, maintainable and scalable code


#example 1
#Example 1

class Animal:

    def __init__(self):
        print("This is the Animal Kingdom")


class Dog(Animal):

    def speak(self):
        print("Woof Woof")

class Cat(Animal):

    def speak(self):
        print("Meow Meow!")

class Cow(Animal):

    def speak(self):
        print("Moo Moo!")

#Runtime Polymorphism
Dog().speak()
Cat().speak()
Cow().speak()

#Alternative
animals = [Dog(), Cat(),Cow()]
for animal in animals:
    animal.speak()


# this Solves the concept of Inheritence/Polymorphism Combined and Self test problem
class Animal:

    def __init__(self):
        self.species = "Mammals"

class Dog(Animal):

    def __init__(self):
        super().__init__()
        print(f"This is a part of {self.species}")

    def eating(self):
        print("Dog is Eating Dog food")

    def speak(self):
        print("Woof Woof")

class Cat(Animal):
     
    def __init__(self):
        super().__init__()
        print(f"This is a part of {self.species}")

    def eating(self):
        print("Cat is Drinking Milk")

    def speak(self):
        print("Meow Meow!")

class Cow(Animal):

    def __init__(self):
        super().__init__()
        print(f"This is a part of {self.species}")

    def eating(self):
        print("Cow is eating Hay")

    def speak(self):
        print("Moo Moo!")

dog = Dog()
dog.speak()
dog.eating()

cat = Cat()
cat.speak()
cat.eating()

