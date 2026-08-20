# JSON is a syntax for storing and exchanging Data.
# JSON is text, written in JavaScript Object Notation 

## In Python JSON Exists as a String 
import json

person = '{"name": "Bob", "languages": ["English", "French"]}'
person_dict = json.loads(person)
## json.loads() - this method is used to convert a python jSON  to dictionary
print( person_dict)
print(person_dict['languages'])

## Python Read JSON File

#first we a save a json file named as 'person.json'

import json 

with open('Day_15/person.json','r') as f: #we use open() function to read the json file
    data = json.load(f) #the file is prased using json.load() method

print(data)

##vConvert Dict to JSON

import json 

person_dict = {'name': 'bob',
               'age':'18',
               'children':None}

person_json =json.dumps(person_dict) #json.dumps() method is used to convert  dictionary to json string

print(person_json) 


## Writing JSON to a file

import json 

person = {'name':'Bob',
          'age':20,
          "Married": True,
          "languages":["English","French"]}

# with open('person.txt','w') as json_file:
#    json.dump(person,json_file)


## Python Pretty print json 

import json 

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x,indent=4,sort_keys=True))
#indent - parameter to define the numbers of indents
#sort_keys - parameter to specify the result should be sorted or not
