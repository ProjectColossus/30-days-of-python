#Lambda Functions

#lambda functions is a small anonymous function 
#which can take any number of arguements but can only have one expression 

#Syntax:  lambda Arguements: Expression

#1
x = lambda a: a+10
print(x(5))

#2 Using Lambda function inside a another function
def myfunction(n):
    return lambda a: a*n

doubler = myfunction(2)
tripler = myfunction(3)
print(doubler(11))
print(tripler(11))

## Use lambda functions when an anonymous function is required for a short period of time.

#Lambda functions are commonly used with Built in functions ike Map(),filter() nd sorted()

#3 map()- function applies to every item in a iterable
num = [1,2,3,4]
doubled = lambda a: a*2
print(list(map(doubled,num)))

#4 filter()- function creates a list of items for which a function returns boolean

numbers = [1,2,3,4,5,6,7,8,9]
odd_numbers = lambda x: x % 2 != 0
print(list(filter(odd_numbers,numbers)))

#alternative way
odd = list(filter( lambda x: x%2 != 0,numbers))
print(odd)

#sorted() -funcction that uses lambda as a key for custom sorting 

# Sort a list of tuples by the second element
student =[('Emily',25),('Tobey',22),('Linus',28)] #each tuple has a x[0]and x[1]
sorted_student_name = sorted(student, key = lambda x : x[0])
sorted_student_age = sorted(student, key = lambda x: x[1])
#sorted student based on x[0] it sorts them based on alphabets
#sorted students based on x[1] it sorts them based on age(22,25,28)
print(sorted_student_name)
print(sorted_student_age)


#sort strings by length
words = ["apple", "banana","pie","Cherry"]

sorted_words=sorted(words, key= lambda x: len(x) )
print(sorted_words)

fruits = ["banana", "apple","kiwi","mango"]
print(sorted(fruits))#to sort them alphabetically 

#sort by nuumber of vowels
def count_vowels(x):
    count = 0
    for ch in x:
        if ch in "aeiou":
            count += 1
    return count

print(sorted(fruits, key=count_vowels))

#reverse 
print(sorted(fruits, reverse = True))

#sort by number of a's
words = ['banana', 'apple', 'avocado', 'kiwi']
def sort_numofchar():
    count = sorted(words, key=lambda x: x.count('a'))
    return count
print(sort_numofchar())



#cool way to end 
numberss = [1,2,3,4,5]
even_num =list(map(lambda x: x*2, filter(lambda x: x%2==0, numberss)))
print(even_num)

#By this, you totally understand that:
#1. It takes the numbers.
#2. It filters out the even numbers from the numbers and then maps them.
#3. It gives it out as a list.
#numbers → filter → map → list reads it from rigth to left