#Functions
# Level 1
#Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(num1,num2):
    return num1 + num2
print(add_two_numbers(8,20))
 
#Area of a circle is calculated as follows: area = π x r x r. 
# Write a function that calculates area_of_circle.
def area_of_circle(r):
    Area = 3.14 *r*r
    return Area
print(area_of_circle(2))

#Temperature in °C can be converted to °F using this formula: °F = (°C x. 9/5) + 32
# Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_celsius_to_fahrenheit(Celcius):
    Fahrenheit = (Celcius * 9/5) + 32
    return Fahrenheit
print(convert_celsius_to_fahrenheit(32))
        


##Write a function called check-season, 
# it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.

def check_season(month):
    if month == "December" or month == "January" or month == "February":
        return "Winter"
    elif month == "March" or month == "April" or month == "May":
        return "Spring"
    elif month == "June" or month == "July" or month == "August":
        return "Summer"
    elif month == "November" or month == "September" or month=="October":
        return "Autumn"
    
print(check_season("May"))
print(check_season("January"))
print(check_season("October"))


##Write a function called calculate_slope which return the slope of a linear equation

def calculate_scope(x2,x1,y2,y1):
    slope = (y2-y1) / (x2-x1)
    return round(slope, 2) 
print(calculate_scope(10,4,9,5))

##Quadratic equation is calculated as follows: ax² + bx + c = 0.
#Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.

import math 
def solve_quadratic_eqn(a,b,c):
    discriminant = b**2 - 4*a*c

    if discriminant >0 : #two solutions
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return round(x1,2), round(x2,2)
    
    elif discriminant == 0: #only one soluton 
        x1 = (-b) / (2*a)
        return round(x1,2)
    else:
        return "No real solution"
    
print(solve_quadratic_eqn(2,5,3))


##Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(lst):
    for i in range(len(lst)):
        print(lst[i])

print_list([5,6,4,8,2]) #just call tyhe function 

##Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).

def reversed_list(arr):
    rev_result=[]
    for i in range(len(arr),0,-1):
        rev_result.append(i)
    return rev_result

print(reversed_list([1, 2, 3, 4, 5]))
print(reversed_list(["A", "B", "C"]))

##Declare a function named capitalize_list_items. 
#It takes a list as a parameter and it returns a capitalized list of items

def capitalize_list_items(lst):
    capitalize_list =[]
    for i in lst:
        capitalize_list.append(i.capitalize())
    return capitalize_list
print(capitalize_list_items(["krishna","varun","John"]))


##Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
def add_item(lst, items):
    food_item = []
    for i in lst:
        food_item.append(i)
    food_item.append(items)
    return food_item
print(add_item(['Potato', 'Tomato', 'Mango', 'Milk'], "Meat"))
print(add_item([2, 3, 7, 9],5))

##Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
def remove_item(lst,item):
    my_list = []
    for i in lst:
        my_list.append(i)
    my_list.remove(item)
    return my_list
       
print(remove_item(['Potato', 'Tomato', 'Mango', 'Milk', 'Meat'],"Mango"))
print(remove_item([2, 3, 7, 9],3))


##Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(num):
    total = 0
    for i in range(num+1):
        total +=i
    return total
print(sum_of_numbers(5))
print(sum_of_numbers(10))
print(sum_of_numbers(100)) 


##Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(n):
    odd = 0
    for i in range(n+1):
        if i%2!=0:
            odd += i
    return odd
    
print(sum_of_odds(5))


##LEVEL 2

##Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
def sum_of_even(num):
    even = 0
    for i in range(num+1):
        if i%2==0:
            even +=i
    return even

print(sum_of_even(5))

#Declare a function named evens_and_odds .
# It takes a positive integer as parameter and it counts number of evens and odds in the number.

def evens_and_odds(num):
    odd_count = 0
    even_count = 0
    for i in range(num+1):
        if i % 2 ==0:
            even_count += 1
        elif i % 2!= 0:
            odd_count +=1
    return f"Evens: {even_count} , Odds: {odd_count}"
print(evens_and_odds(100))

#Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(num):
    result = 1
    for i in range(num, 0, -1):
        result *= i
    return result
print(factorial(5))

#Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(lst):
    if len(lst) == 0:
        return "empty"
    else:
        return "Not Empty"

print(is_empty([]))
print(is_empty([1,2,3]))

#Write different functions which take lists. 
#They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).

def calculate_mean(lst):
    sum_of_values = 0
    Number_of_values = 0
    for i in lst:
        sum_of_values += i
        Number_of_values+=1
    mean = sum_of_values / Number_of_values
    return round(mean,2)
print(calculate_mean([2, 4, 6, 8, 10]))

def calculate_median(lst):
    n = len(lst)
    middle_term = n//2
    if len(lst) % 2 !=0:
        median_odd = lst[middle_term]
        return f"median for odd Values are : {median_odd}"
    elif len(lst) % 2 ==0:
        median_even = (lst[middle_term-1] +lst[middle_term]) / 2
        return f"median for even values are: {median_even}"

print(calculate_median([2,4,6,8,10]))
print(calculate_median([2,4,6,8,10,12]))

def calculate_mode(lst):
    mode = lst[0]
    frequency = 0
    for i in lst:
        count = 0
        for j in lst:
            if i == j:
                count +=1
        if count>frequency:
            frequency = count
            mode = i
    return mode
print(calculate_mode([1,2,2,2,3,4]))

##Write a function called greet which takes a default argument, name. If no argument is supplied it should print "Hello, Guest!", 
# otherwise it should greet the person by name.

def greet(name= "Guest!"):
    print("Hello", name)

greet()
greet("Alice")

##Create a function called show_args to take an arbitrary number of named arguments and
#print their names and values.


def show_args(**kwargs):
 #**kwargs collect any number of named arguements into a dictionary 
    print(kwargs)

show_args(name="Alice", age=30, city="New York")
    
# *args - is for arbitary postional arguments 

def show_args(*args):
    for value in args:
        print(value)

show_args("Alice", 30,"New York")

##

def show_args(**kwargs):
    print(kwargs)

show_args(name="Bob", pet="Fluffy, the bunny")



##Write a function called is_prime, which checks if a number is prime.

n = int(input())

def is_prime():
    is_Prime = True
    if n > 1:
        for i in range(2,n):
            if n % i ==0:
                is_Prime = False
                break
        return is_Prime

print(is_prime())
##\end\
    

