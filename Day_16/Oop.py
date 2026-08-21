### OOP's -- Object Oriented Programming (Python)
# In OPPs we basically use it to write code in Structured, Resuable, and manageable way 
## in Object oriented programming we have two core concepts Class and Object

## lets take an example to understand these concepts


## lets take a House as an example 
#1 Class = Blueprint of House (defines Structure)
#2 Object = Actual House built (real thing created)

## House has Doors, Windows and a Gate 
#--> Attributes (Properties of the house)/(What House HAS)
#--> Methods (Things The house can do)/(What the house CAN DOw)

##__init__(): automatically runs when an object is initialized, and is commonly used to give that object its initial attributes.

class House: #(class keyword used to define the bluprint name)

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
house1 = House(doors=2,windows=5,gate="Open",color= "Beige")
house2 = House(doors=4,windows=8,gate="Closed",color= "Blue")

house1.describe()
house2.describe()
print("--------------")
house1.open_gate()
house2.open_gate()

#########################################