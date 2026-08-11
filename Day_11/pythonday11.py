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

##Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
def sum_of_even(num):
    even = 0
    for i in range(num+1):
        if i%2==0:
            even +=i
    return even

print(sum_of_even(5))

##