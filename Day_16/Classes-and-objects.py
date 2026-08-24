### OOP -- Object Oriented Programming (Python)
# In OPP we basically use it to write code in Structured, Resuable, and manageable way 
## in Object oriented programming we have two core concepts Class and Object

##  A class is like an object constructor, or a "blueprint" for creating objects. We instantiate a class to create an object. 
# The class defines attributes and the behavior of the object, while the object, on the other hand, represents the class.
## lets take an example to understand these concepts


## lets take a House as an example 
#1 Class = Blueprint of House (defines Structure)
#2 Object = Actual House built (real thing created)

## House has Doors, Windows and a Gate 
#--> Attributes (Properties of the house)/(What House HAS)
#--> Methods (Things The house can do)/(What the house CAN DOw)


#class Attribute is Shared by all 
#Instance Attribute is differenct for each one 

##__init__(): automatically runs when an object is initialized, and is commonly used to give that object its initial attributes.



#Example 1
## Class
class Dog:
    species = "Canine" #Class Attribute

    def __init__(self,name,age):
        self.name = name #Instance Attribute
        self.age = age #Instance Attribute

#Creates an Object of the Class
Dog1 = Dog("Johnny",7)
print(Dog1.name) ## Accesses the Instance Attribute
print(Dog1.species) ## Accesses the Class Attibute

#Example 2
class Monster:

    #Attributes
    def __init__(self,health,energy):
        self.health = health
        self.energy = energy 

    def __str__(self):
        return f"A Monster with health {self.health} and energy {self.energy} "
        
    #methods
    def attack(self ,amount):
        print("The Monster has Attacked!")
        print(f"{amount} damage was dealt")
        self.energy -= 20
        print(self.energy)

    def move(self,speed):
        print(f"the monster has moved with the speed of {speed}kmph")

monster1 = Monster(health=50,energy=90)
print(monster1.health)
print(monster1)





# Example 3

class House: #(class keyword used to define the bluprint name) 

    # Instance Atrributes 
    #Attributes --> Properties every house has
    def __init__(self,doors,windows,gate,color): #self refers to the current object,allowing each object to store and access its own data 
        self.doors = doors  #how many doors
        self.windows = windows  #how many windows
        self.gate = gate  #has a gate or not
        self.color = color  #Color of the house

    #methods --> things house can do
    def describe(self):
        print(f"This House has {self.doors} doors")
        print(f"this house has {self.windows} windows ")
        print(f"Gate: {self.gate}")
        print(f"Color:{self.color}")

    def open_gate(self):
        if self.gate == "Open":
            print("The gate is open")
        else:
            print("The gate is closed")

#Building Actual House from Blueprint 
#Object  / instances of class
house1 = House(doors=2,windows=5,gate="Open",color= "Beige")
house2 = House(doors=4,windows=8,gate="Closed",color= "Blue")

house1.describe() ## Calling a method
house2.describe()
print("--------------")
house1.open_gate()
house2.open_gate()

# Example 3 
#this Question below is from Hackerrank Classes (Medium) problem 
## It covers Operator Overloading, Dunder methods
import math
class Complex:
    def __init__(self,real,imag):
        self.real = real
        self.imag = imag

    def __add__(self,other):
        return Complex(self.real + other.real, self.imag + other.imag )

    def __sub__(self, other):
        return Complex(self.real - other.real,
                       self.imag - other.imag)

    def __mul__(self, other):
        #multiplication for Complex Numbers (a*b -c*d),(a*d + c*b)
        return Complex(
            self.real * other.real - self.imag * other.imag,
            self.real * other.imag + self.imag * other.real
        )

    def __truediv__(self, other):
        #division for complex numbers is different 
        #Denominator = c^2 + d^2
        denominator = other.real**2 + other.imag**2
        #(ac + bd)/denominator
        Real_part = (self.real * other.real + self.imag * other.imag)/denominator
        #(bc - ad)/denominator
        Imaginary_part = (self.imag * other.real - self.real * other.imag)
        return Complex(Real_part,Imaginary_part)/denominator

    def mod(self):
        return Complex(math.sqrt(self.real**2 + self.imag**2),0)

    def __str__(self):
        if self.imag == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imag >= 0:
                result = "0.00+%.2fi" %(self.imag)
            else:
                result = "0.00-%.2fi" % (abs(self.imag))
        elif self.imag > 0:
            result = "%.2f+%.2fi" % (self.real,self.imag)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imag))
        return result

c1 =Complex(2,1)
c2 =Complex(5,6)

print(c1+c2)
print(c1-c2)
print(c1*c2)
print(c1.mod())
print(c2.mod())

##SELF TEST
# Create a Student class with:
# - class attribute: school_name
# - instance attributes: name, grade, marks
# - methods:
#   → describe() prints student info
#   → is_passing() returns True if marks > 40
#   → get_grade() returns A/B/C based on marks

class Student:
    school_name = "Python High School"

    def __init__(self, name, grade, marks):
        self.name = name
        self.grade = grade
        self.marks= marks

    def describe(self):
        print(f"School:{self.school_name}")
        print(f"{self.name},Grade:{self.grade}, Marks:{self.marks}")

    def is_passing(self):
        if self.marks> 40:
            return "True"
        else:
            return "False"

    def get_grade(self):
        if self.marks >= 90:
            return "A"
        elif 90 > self.marks >= 60:
            return "B"
        elif 60 > self.marks >=50:
            return "C"
        else:
            return "F"

s1 = Student("Krishna", 10, 95)
s2 = Student("Varun",   11, 38)

s1.describe()       # Krishna, Grade 10, Marks: 95
print(s1.is_passing())    # True
print(s1.get_grade())      # A
print("-----------------------------------------------")
s2.describe()       # Varun, Grade 11, Marks: 38
print(s2.is_passing())     # False
print(s2.get_grade())      # F



