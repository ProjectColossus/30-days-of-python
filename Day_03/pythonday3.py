#day3 (level 1)
#1
age = 19
height = 1.78
com = 4+3j

#Area of triangle
base_triangle = int(input("Enter the base of the triangle: "))
height_triangle = int(input("Enter the height of the triangle: "))
area_of_triangle = 0.5 * base_triangle * height_triangle
print(f"Area of triangle is {area_of_triangle}")

#perimeter of triangle
side_1 = int(input("Enter the first side of the triangle: "))
side_2 = int(input("Enter the second side of the triangle: "))
side_3 = int(input("Enter the third side of the triangle: "))
perimeter_of_triangle = side_1 + side_2 + side_3
print(f"Perimeter of triangle is {perimeter_of_triangle}")

#calculate the Area and perimeter of Rectangle
length = int(input("Enter the length of Rectangle: "))
width = int(input("Enter the Width of Rectangle: "))
Area_of_rect = length * width
perimeter_of_rect= 2 * (length + width)
print(f'Area of Rectangle is {Area_of_rect}')
print(f'Perimeter of Rectangle is {perimeter_of_rect}')

#calculate the Area and circumference of circle
import math
r = int(input("Enter the radius of circle: "))
area_pf_circle = math.pi *r*r
circumference_of_circle = 2 * math.pi *r
print(f'Area of circle is {area_pf_circle:.2f}')
print(f'Circumference of circle is {circumference_of_circle:.2f}')

#8
#Calculate the slope, x-intercept and y-intercept of y = 2x -2
# For y = mx + c, m is the slope and c is the y-intercept.
# For y = 2x - 2, the slope (m) = 2 and the y-intercept (c) = -2.
# The x-intercept is when y = 0. So, 0 = 2x - 2 => 2x = 2 => x = 1.
slope = 2
y_intercept = -2
x_intercept = 1

print(f'Slope is {slope}')
print(f'X-intercept is {x_intercept}')
print(f'Y-intercept is {y_intercept}')

#9
#calculate the slope (m = (y2-y1)/(x2-x1)) and Euclidean distance between (2,2) and (6,10)
import math 
x1, x2 = 2 , 6
y1 , y2 = 2 , 10
x = x2-x1
y = y2-y1
slope1 = int((y)/(x))
print(f"Slope1: {slope1}")

result = math.sqrt(x**2 + y**2)
print(f"the euclidean distance between (2,2) and (6,10): {result:.2f} ")

#10
#compare the slopes in tasks 8 and 9
print(slope == slope1)
print(slope != slope1)
print(slope > slope1)
print(slope < slope1)
print(slope >= slope1)
print(slope <= slope1)

#11
#Calculate the value of y (y = x^2 + 6x + 9). 
#Try to use different x values and figure out at what x value y is going to be 0
X = int(input("Enter the value of x"))
Y = X**2 + 6*X + 9 
print(Y)

#12 
# find the length od "Python and "dragon" and make a falsely comparison 
print(len('Python')>len("Dragon"))

#13 and 15
#Use "and" operator to check if 'on' is found in both 'python' and 'dragon'
#There is no 'on' in both dragon and python
print('on' in 'Python' and 'on' in 'Dragon')
print('on' not in 'python' and 'on' not in 'dragon') #False
#True
# and =  'and' operator return True if both the statements are true

#14
print('jargon' in 'I hope this course is not full of jargon')
#True

#16
#Find the length of the text python 
#and convert the value to float and convert it to string
print(str(float(len('python'))))

#17
#Even numbers are divisible by 2 and the remainder is zero
# How do you check if a number is even or not using python?(without conditionals)
a = 5
print(("even", "odd")[a % 2])

#18 
#Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print(7//3 == int(2.7)) #True
 
#19 
#  Check if type of '10' is equal to type of 10
print(type('10') == type(10)) #False

#20
#Check if int('9.8') is equal to 10
print(float('9.8') == 10) #false, because int('9.8') will give an error since
#'9.8' is a string representation of a float, not an integer

#21 
# Write a script that prompts the user to enter hours and rate per hour.
# Calculate pay of the person?
hours = float(input("Enter hours: "))
rate_per_hour = float(input("Enter rate per hour: "))
weekly_earning = hours * rate_per_hour
print(f"Your weekly earnings are: {weekly_earning}")

#22 
#Write a script that prompts the user to enter number of years.
#Calculate the number of seconds a person can live. 
years = int(input("Enter number of years you live: "))
seconds_in_year = 365 * 24 * 60 * 60
total_seconds = years * seconds_in_year
print(f"The number of seconds a person can live is: {total_seconds}")

#23
#Write a Python script that displays the following table
print("1 1 1 1 1")  
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")