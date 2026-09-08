#Error and Exceptional handling
# there are three keywords:
# -try: 
#     (block of code that may or may not have an error)
# -except: 
#     (if error does occur this will be executed)
# -finally: 
#     (block of code that gets executed regarless of any error)


#example 1:
while True:
    try: #a risky code which may or may not have an error
        result = int(input("Enter a Number: "))
        break
    except ValueError: # runs when an Error ("ValueError") occurs from the try block of code the except is executed
        print("This is not a valid Number, Try Again....")

#example 2 
num = 10 
try:
    res = num/0
except ZeroDivisionError:
    print("You cannot divide a number with Zero")
    print("As the result is always zero")

#example 3
try:
    f = open("Day_18/testfile.txt",'r')
    f.write("This is a test file")
except TypeError:
    print("There is a type error")
except OSError:
    print("there is an OS Error")
finally:
    print("this is the End of try/except/finally block")

#example 4

def ask_for_int():
    while True:
        try:
            value = int(input("Enter a valid Number:"))
        except ValueError:
            print("this is not a valid number try again...")
            continue
        else:
            print(value)
            print("Thank You")
            break
ask_for_int()


#1
try:
    for i in ['a','b','c']:
        print(i**2)
except TypeError:
    print("there is a type error")

#2

x = 5
y = 0
try:
    z = x/y
except ZeroDivisionError:
    print("you cannot divide the value with zero")
finally:
    print("All Done")

#3
def ask():
    while True:
        try:
            num = int(input("Enter an Integer: "))
        except ValueError:
            print("A ValueError has occured Try Again..")
            continue   
        else:
            print("Thank you, your squared number:",num**2) 
            break

ask()
