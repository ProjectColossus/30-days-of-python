#Modules
# A Modules is basically a set of codes or set of functions which can be included to an application

#we are gonna create a Module to write our code in a python script ex: "mymodule.py"
#Exercises: Level 1

#1 Write a function which generates a six digit/character random_user_id.

import random #import 2 modules one is random and string
import string

def random_user_id():
    characters = string.ascii_lowercase + string.digits
    result = ""
    for i in range(6):
        result += random.choice(characters)
    return result



#2 Modify the previous task. Declare a function named user_id_gen_by_user. 
# It doesn’t take any parameters but it takes two inputs using input().
#  One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
import random #import 2 modules one is random and string
import string

def user_id_gen_by_user():
    user_num_charcters = 5
    user_num_ids = 5
    characters = string.ascii_lowercase + string.digits
    for i in range(user_num_ids):
        result = ""
        for j in range(user_num_charcters):
            result += random.choice(characters)
        print(result)



#3 Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).

import random

def rgb_color_gen():
    rgb = []
    for i in range(3):
        rgb.append(random.randint(0,255))
    print(rgb)



#4 Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array.
# (six hexadecimal numbers written after #.)
#  Hexadecimal numeral system is made out of 16 symbols,
#  0-9 and first 6 letters of the alphabet, a-f. 
# Check the task 6 for output examples).

import random 
import string 
def list_of_hexa_colors(name, num):
    hexa =[]
    hexa_chars = "abcdef" + string.digits 
    for i in range(num): #controls how many colors this basically builds one color at a time
        color = "#"
        for j in range(6): #builds one character at a time | character runs 6 times, 6 character each color
            color += random.choice(hexa_chars)
        hexa.append(color)
    return hexa


#5 Write a function list_of_rgb_colors which returns any number of RGB colors in an array.

import random 

def list_of_rgb_colors(num):
    rgb = []
    for i in range(num):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        color = f"rgb({r},{g},{b})"
        rgb.append(color)
    return rgb



#6Write a function generate_colors which can generate any number of hexa or rgb colors

def generate_colors(name, num):
    if name == 'Hexa':
        hexa =[]
        hexa_chars = "abcdef" + string.digits 
        for i in range(num): #controls how many colors this basically builds one color at a time
            color = "#"
            for j in range(6): #builds one character at a time | character runs 6 times, 6 character each color
                color += random.choice(hexa_chars)
            hexa.append(color)
        return hexa
    elif name=='rgb':
        rgb =[]
        for i in range(num):
            r = random.randint(0,255)
            g = random.randint(0,255)
            b = random.randint(0,255)
            color = f"rgb({r},{g},{b})"
            rgb.append(color)
        return rgb


##Modules types
# Math for math utilities
# re for regular expression 
# json to work with JSON
# datetime to work with dates
# sqlite to use SQLite
# sqlite3 to use SQLite
# os for Operation System Utilities
# random for random Number Generation
# statistics for statistics utilities
# requests to perform HTTP network requests
# http to create http servers 
# urllib to manage urls

