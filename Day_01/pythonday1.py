#exercise 1 (Day 1)
#level 1
#1
print(3+4) #addition
print(3-4) #subtraction
print(3*4) #multiplication
print(3/4) #divison
print(3%4) #modulus
print(3**4) #power
print(3//4) #floor division

#2 (Exercise 1)
print("Krishna M")
print("India")
print("Bangalore")
print("Billionaire")

#3 (Excercise 1)
print(type(10)) #integer    
print(type(99.99)) #float
print(type("Krishna")) #string
print(type(True)) #boolean
print(type(None)) #NoneType
print(type(4+4j)) #complex number
print(type(['krishna','apple','python'])) #list

#level 3
#Write an example for different Python data types such as Tuple, Set and Dictionary.
print(type({'name':'Krishna',
            'Age':19,
            'car':'porsche 911'}))
print(type({'apple','banana','fruit',56})) # order is not important in set
print(type(('apple','banana','cherry'))) #tuples are immutable

#Find an Euclidean distance between (2, 3) and (10, 8)
import math
x1,x2=2,10
y1,y2=3,8
x = x2-x1
y = y2-y1
result = math.sqrt(x**2+y**2)
print(f'result: {result:.2f}') #result to be printed in 2 floating point