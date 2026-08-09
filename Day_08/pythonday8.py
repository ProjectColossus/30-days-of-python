#Dictionaries
# Exercises: Day 8

#Create an empty dictionary called dog
dog = {}

#Add name, color, breed, legs, age to the dog dictionary
dog = { 'name':'Max', 'Color': 'black','breed':'dobermann','Legs':4 , 'age': 6}
print(dog)

#Create a student dictionary and add first_name, last_name, gender, age, marital status,
# skills, country, city and address as keys for the dictionary
student ={'first_name':'Krishna', 
          'Last_name':'M',
          'gender': 'Male',
          'age':19,
          'marital_status':'Single',
          'Skills':['Python','Java'],
          'Country': 'India',
          'City':'Bangalore',
          'Address':{
              'Street':'HSR',
              'Zipcode': 560102
          }
          }

#Get the length of the student dictionary
print(len(student))

#Get the value of skills and check the data type, it should be a list
print(student.get('Skills'))
print(type(student['Skills']))

#Modify the skills values by adding one or two skills
student['Skills'].append('AI')
student['Skills'].append('ML')
print(student['Skills'])

#Get the dictionary keys as a list
keys_ = student.keys()
print(keys_)

#Get the dictionary values as a list
values_ = student.values()
print(values_)

#Change the dictionary to a list of tuples using items() method
std_items = student.items()
print(std_items)

#Delete one of the items in the dictionary
del student['marital_status']
print(student)

#Delete one of the dictionaries
del dog