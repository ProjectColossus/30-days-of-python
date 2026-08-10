#Practicing Loops Concepts to Understand better(Chai aur code) 

#1 Counting Positive Numbers
#Given a list of Numbers Count How many Positive

lst =[1,-2,3,-4,5,6,-7,-8,9,10]
Postive_Numbers = 0

for Num in lst:
    if Num > 0:
        Postive_Numbers += 1
print(f"Postive Numbers: {Postive_Numbers}")

#2 Sum of Even Numbers
n = 10
Sum_Even_Numbers = 0
for Num in range(1,n+1):
    if Num % 2 == 0:
        Sum_Even_Numbers += Num
print("Sum of Even Numbers:",Sum_Even_Numbers)

#3 Multiplication Table Printer
#Print a multiplication table for a given number n. Skip the fifth iteration

n = 5

for i in range(1,11):
    if i ==5:
        continue  #continue lets you skip a particular iteration in the loop and continues 
    print( n, "X" ,i ,"=",n*i )

#4 Reverse a String
input_str = "Python"
reversed_string =""

for i in input_str:
    reversed_string = i + reversed_string

print(reversed_string)

#5 Find the First Non-repeated Character
# given a String find the non repeated character

input_str = "teteeracabac"

for char in input_str:
    print(char)
    if input_str.count(char) == 1:
        print("Non-Repeated Character: ",char)
        break
#break lets you to exit the loop once the work is completed 

#6 factorial Calculator
#Problem: Compute the Factorial of a Number Using While Loop 

Number = 5
Factorial = 1

while Number > 0:
    Factorial *=  Number
    Number -= 1
print(f"Factorial : {Factorial}")

#7 Validate Input
#Problem: Keep Asking the User Input Until They Enter A Number Between 1 to 10

while True:
    num = int(input("Enter a Number b/w 1 to 10: "))
    if 1<=num<=10:
        print("Thanks")
        break
    else:
        print("Invalid Number")

#8 Prime Number Checker
#Problem: Check if Number is Prime

n =1
is_prime = True

if n > 1:
    for i in range(2,n):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print(n,"is a Prime Number")
    else:
        print(n,"Not a prime Number")

#9 List Unique Checker
#Problem: Check is all the elements ina list are unique. if duplicate is found, exit the loop and print the duplicate

items = ["apple", "orange", "banana", "apple", "mango"]
unique_item = set()
# set() only stores unique items no duplicates 
for item in items:
    if item in unique_item:
        print("Duplicate:",item)
    else:
        unique_item.add(item)

#10 Exponential Backoff
#Problem: Implement an Exponential backoff strategy that doubles wait time between retries, starting from 1 second, but stops after 5 retries

import time

attempts = 0
max_retries = 5
wait_time = 1

while attempts < max_retries:
    print("attempts",attempts+1, "-wait_time",wait_time)
    time.sleep(wait_time)
    wait_time *= 2 #wait_time doubles as attempts increase by 1
    attempts += 1


#Nested Loops: a Loop within Another Loop (Outer Loop, Inner Loop )

#1 Rectangle

for x in range(4):
    for y in range(10):
        print("x" , end ="")
    print()