#Recursions

# Recusrion is when a function call itself
# this has a Benefit of meaning that you can loop through a data to reach result

# Example 1
def countdown(n):
    if n <= 0: ## Base Case (Stopping Condition)
        print("Done") 
    else:
        print(n) ## Recursive Case (Calls itself)
        countdown(n-1) ## Calls itself with a smaller value

countdown(5)

#there are two parts for every recursive function 
#  Base case == When To Stop 
# Recursive Case == Call itself with smaller input

#Example 2

def factorial(n):
    #Base Case
    if n==0 or n==1:
        return 1 #tells you to stop Or else infinity Loop  
    # Recursive Case
    else:
        return n*factorial(n-1)

print(factorial(5))

# some Question to build LogicBuilding in  Recursion and get a better handle with it

## Level 1

#1 Print NUmber from 1 to n using recursions

def count_up(num):
    if num <= 0:
        return
    else:
        count_up(num -1) #Recursive case where it decreases to first
        print(num) # then calls itself
count_up(5)

print()

#2 print Numbers from n to 1 recursively

def count_down(n):
    if n <= 0:
        return
    else:
        print(n) #Recursive case (calls itself)
        count_down(n-1) #calls itself with a smaller value
count_down(5)

print()


#3 Print Only Even Numbers using Recursion 
def even_numbers(n):
    if n==0:
        return
    even_numbers(n-1)
    if n%2==0:
        print(n)

even_numbers(10)

print()

#4 Print only Odd Numbers using Recursion 

def odd_numbers(num):
    if num == 0:
        return
    odd_numbers(num-1)
    if num % 2 !=0:
        print(num)

odd_numbers(10)

print() ## to skip one line thats it 

#5 print the sum of n no of digits

def sum_num(num):
    if num <=0:
        return 0
    else:
        return num + sum_num(num-1)
print(sum_num(5))