#Iterate 0 to 10 using for loop, do the same using while loop.

#for loop

for i in range(0,11):
    print(i, end = ' ') 
print() #moves the cursor to the next line

#while loop 
count =0
while count < 11:
    print(count , end=' ')
    count = count +1
print()

#Iterate 10 to 0 using for loop, do the same using while loop.

#for loop 

for i in range(10, -1 , -1):
    print(i , end = ' ')
print()

#while loop 
count = 10
while count >= 0:
    print(count, end = ' ')
    count -=1
print()

#Write a loop that makes seven calls to print(), so we get on the output the following triangle:

  #
  ##
  ###
  ####
  #####
  ######
  #######

a = "*"
for rows in range(1,8):
    for cols in range(rows):
        print(a, end ='')
    print()

#Use nested loops to create the following:

# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #

#outer loop 8 number of rows 
for i in range(8): 

    #inner loop 8 number of colums
    for j in range(8):

        # print the symbol next to each other 
        print("#", end =' ')

    #moves the cursor next line and prints the inner loop
    print() 

##Print the following pattern:
for i in range(0,11):
        mul = i * i
        print(f"{i} * {i} = {mul}")

#Iterate through the list using a for loop and print out the items.
lst = ['Python', 'Numpy','Pandas','Django', 'Flask']
for i in range(0,5):
    print(lst[i])

#Use for loop to iterate from 0 to 100 and print only even numbers

# this is the method 1 where u can use the range(start, end, step) to print even number
for i in range(0,101,2):
    #Print each number with a space, don't go to the next line
    print(i, end = " ")   
#Move to the next line
print()


#method 2 would require the conditionals (if statement)
for i in range(0,101):
    if i%2==0:
        print(i, end=" ")
print()

#Use for loop to iterate from 0 to 100 and print only odd numbers##

#generate the odd number(method 1)
for i in range(1,101,2):
    #prints each number witha space, dont go next line
    print(i, end= " ")
#move to the next line
print()

#Method 2 (Conditionals)- if statement 
for i in range(0,101):
    if i%2!=0:
        print(i, end =" ")
print()

###Exercises: Level 2
#Use for loop to iterate from 0 to 100 and print the sum of all numbers.
#The sum of all numbers is 5050.

total = 0
for i in range(0,101):
    total = total + i
print(f"the sum of all Numbers {total}")


##Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
#The sum of all evens is 2550. And the sum of all odds is 2500.

even = 0
odd = 0
for i in range(0,101):
    if i%2 ==0:
        even += i
    if i%2!= 0:
        odd += i
print(f"The sum of all evens {even}. The sum of all odds {odd}")


###Exercises: Level 3
#Go to the data folder and use the countries.py file. Loop through the countries 
#and extract all the countries containing the word land.

from countries import countries
for country in countries:
    if "land" in country:
        print(country)

#####################################################################################################
#This is a fruit list, reverse the order using loop.
#method 1
fruit = ['banana', 'orange', 'mango', 'lemon']

for i in range(len(fruit)-1, -1, -1): #Start from the last index and move backwards until index 0
    print(fruit[i]) #prints each index from the fruit list


#Method 2
my_fruit = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = [] #set a empty list

for i in range(len(my_fruit)-1,-1,-1):
    reversed_fruits.append(my_fruit[i]) 
#insert list items from my_fruit to the reversed_fruits new list backwards

print(reversed_fruits)
#################################################################################################

#Go to the data folder and use the countries_data.py file.

#What are the total number of languages in the data
from countries_data import countries_data

for country in countries_data:
    if "lanuages" in country:
        print(country)


#Find the ten most spoken languages from the data
#Find the 10 most populated countries in the world

