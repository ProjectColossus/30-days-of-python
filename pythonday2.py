#Day 2 (level 1)
first_name = 'Krishna'
last_name = 'Nanda'
country = 'india'
city = 'Bangalore'
age = 19
year = 2026
is_married = False
is_true = True
is_light_on = True
first_name,last_name,country,city,age,year,is_married,is_true,is_light_on = 'Krishna','Nanda','India','Bangalore',19,2026,False,True,True


#level 2
print(len(first_name))
print(len(last_name))
print(f"Are first_name and last_name equal? {first_name == last_name}")
num1 = 5
num2 = 4
total = num1 + num2
print(total)
diff = num1 - num2
print(diff)
product = num1 * num2
print(product)
division = num1 / num2
print(division)
remainder = num1 % num2
print(remainder)
exp = num1 ** num2
print(exp)
floor_division = num1 // num2
print(floor_division)

#calculation of circle
import math
r = int(input("Enter the radius of the circle: "))
area_of_circle = math.pi * (r**2)
print(f"Area of the circel is {area_of_circle:.2f}")
circum_of_circle = 2 * math.pi * r
print(f"circumference of the circle is {circum_of_circle:.2f}")