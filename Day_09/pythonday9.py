#Conditionals

#💻 Exercises: Day 9

#EXCERCISE 1

#Get user input using input(“Enter your age: ”). If user is 18 or older,give feedback:You are old enough to drive.
#  If below 18 give feedback to wait for the missing amount of years
age = int(input("Enter your Age: "))
if age >= 18:
    print("You are old enough to drive")
else:
    years_left = 18 - age  
    print(f"Wait for {years_left} years to drive")

#Compare the values of my_age and your_age using if … else. Who is older (me or you)? 
# Use input(“Enter your age: ”) to get the age as input.
#  You can use a nested condition to print 'year' for 1 year difference in age, 
# 'years' for bigger differences, and a custom text if my_age = your_age. 
my_age = 30
your_age = 30

if my_age > your_age:
    diff = my_age - your_age
    if diff == 1:
        print("you are 1 year older than me")
    else:
        print(f"you are {diff} years older than me")

elif your_age > my_age:
    diff = your_age - my_age
    if diff == 1:
        print("you are 1 year older than me")
    else:
        print(f"your {diff} years older than me")

else:
    print("we are the same age")

#Get two numbers from the user using input prompt.
# If a is greater than b return a is greater than b, 
# if a is less b return a is smaller than b, else a is equal to b.
a = 4
b = 3
if a>b:
    print(f"{a} is greater than {b}")
elif a<b :
    print(f"{a} is less than {b}")
else:
    print(f"both {a} and {b} are same")

