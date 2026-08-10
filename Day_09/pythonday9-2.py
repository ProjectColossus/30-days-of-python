#Exercises: Level 2

#Write a code which gives grade to students according to theirs scores
grade = 90

if grade >= 90 and grade <= 100:
    print("A")
elif grade >= 80 and grade < 90:
    print("B")
elif grade >= 70 and grade < 80:
    print("C")
elif grade >= 60 and grade < 70:
    print("D")
else:
    print("F")

#Get the month from user input then check if the season is Autumn, Winter, Spring or Summer.
#If the user input is: September, October or November, the season is Autumn.
#December, January or February, the season is Winter.
#March, April or May, the season is Spring. 
#June, July or August, the season is Summer.

month = 'May'

if month == 'September' or month == 'October' or month == 'November':
    print("Season is Autumn")
elif month == 'December' or month =='January' or month == 'February':
    print("Season is Winter")
elif month == 'March' or month =='April' or month =='May':
    print("Season is Spring")
elif month == 'June' or month == 'July' or month == 'August':
    print("Season is Summer")
else:
    print("Input is incorrect")


#The following list contains some fruits:
#If a fruit doesn't exist in the list add the fruit to the list and print the modified list.
# If the fruit exists print('That fruit already exist in the list')

fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits

if  not does_exist:
    fruits.append('apple')
    print(fruits)
else:
    print("fruit does exist in the list")

#Exercises: Level 3

#Here we have a person dictionary. Feel free to modify it!
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
 #Check if the person dictionary has skills key,
 #if so print out the middle skill in the skills list.
 
exist = 'skills' in person
if exist:
    print("skills in dictionary exist:",exist)
    skills = person['skills']
    middle_index = len(skills)//2
    print(skills[middle_index])
    
else:
    print("Does not exist")

 # Check if the person dictionary has skills key, 
 # if so check if the person has 'Python' skill and print out the result.

check = 'Python' in person['skills']
if exist and check:
    print("python skill does exist")
    print(person['skills'])
else:
    print("Does not exit")

 # If a person skills has only JavaScript and React,
 # print('He is a front end developer'), 
 # if the person skills has Node, Python, MongoDB, print('He is a backend developer'), 
 # if the person skills has , Print('He is a fullstack developer'),
 # else print('unknown title') - for more accurate results more conditions can be nested!

if person['skills'] == ['Javascript','React']:
    print("He is a front end developer")
elif person['skills'] == ['Node', 'Python', 'MongoDB']:
    print("he is a backend developer")
elif person['skills'] ==['JavaScript', 'React', 'Node', 'MongoDB', 'Python']:
    print("He is a FullStack Developer")
else:
    print("Unknown tile")



# If the person is married and if he lives in Finland,
# print the information in the following format:
lives = 'Finland'
is_married = True

if lives == 'Finland' and is_married:
    print(f"Asabeneh Yetayeh lives in {lives}. He is married")
else:
    print("Wrong format")
