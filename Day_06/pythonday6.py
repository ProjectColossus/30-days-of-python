#Day 6 (Tuple)

#Exercises: Level 1

#Create an empty tuple
tpl = () #this is an empty tuple

#Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
bro = ('John', 'King','Bob','Andrew')
sis = ('Sarah', 'Amanda', 'Emily',)

#Join brothers and sisters tuples and assign it to siblings
siblings = bro + sis
print(f"These are siblings: {siblings}")

#How many siblings do you have??
print(len(siblings))

#Modify the siblings tuple and add the name of your father and mother and assign it to family_member
family_member = list(siblings)
family_member.append('father')
family_member.append("Mother")         
family_member = tuple(family_member)
print("This is a family: ",family_member)

#Exercises: Level 2

#Unpack siblings and parents from family_members
siblings1 = family_member[0:7]
parents = family_member[7:]
print("Parents: ",parents)
print("Siblings: ", siblings1) 

#Create fruits, vegetables and animal products tuples. 
#Join the three tuples and assign it to a variable called food_stuff_tp.
fru = ('banana', 'orange', 'mango', 'lemon')
veg = ('tomato','potato','bringal','beans')
ani_pro = ('Milk','eggs','cheese','yogurt')
food_stuff = fru + veg + ani_pro
print(food_stuff)

#Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff)

#Slice out the middle item or items from the food_stuff tuple or food_stuff_lt list.
middle_item = food_stuff_lt[5:7]
print(middle_item)

#Slice out the first three items and the last three items from food_stuff_lt list
first_three_items = food_stuff_lt[0:3]
print(first_three_items)

#Delete the food_stuff_tp tuple completely
del food_stuff

#Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)