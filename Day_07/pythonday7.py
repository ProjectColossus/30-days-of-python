#DAY 7 (SET)

# Exercises:1

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]


#Exercises: Level 1

#Find the length of the set it_companies.
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(len(it_companies))

#Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)

#Insert multiple IT companies at once to the set it_companies
it_companies.update(['JPMorgan', 'GoldmanSachs', 'BCG', 'Pepsico'])
print(it_companies)

#Remove one of the companies from the set it_companies
it_companies.remove('BCG')
print(it_companies)

#What is the difference between remove and discard
it_companies.discard('Google')
print(it_companies)
it_companies.remove('Facebook')
print(it_companies)
# remove and discard items from the collection of Set

#---------------------------------------------------------
#Exercises: Level 2
#-----------------------------------------------------------
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
#Join A and B
print(A.union(B))

#Find A intersection B
print(A.intersection(B))

#Is A subset of B
print(A.issubset(B))

#Are A and B disjoint sets
print(A.isdisjoint(B))

#Join A with B and B with A
print(A.union(B))
print(B.union(A))

#What is the symmetric difference between A and B 
print(A.symmetric_difference(B))

# Delete the sets completely
del A , B

#-----------------------------------------------------------------
#Exercises: Level 3
#-----------------------------------------------------------------

#Convert the ages to a set and compare the length of the list and the set, 
#which one is bigger?
age = [22, 19, 24, 25, 26, 24, 25, 24]
age1 = set(age)
print(len(age))
print(len(age1) >= len(age)) #list age is bigger

#Explain the difference between the following data types: string, list, tuple and set
# String - A string is a data type 
#list - a collection of data type which is ordered and mutable
#Tuple - A collection of data type which is ordered and immutable
#set - a collection of data type which is unordered and un-indexed 

 
#How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
text = "I am a teacher and I love to inspire and teach people."
word_list = text.split()
unique = set(word_list)
print(unique)