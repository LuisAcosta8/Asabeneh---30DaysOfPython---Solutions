#Variables, builtin functions

#Write a python comment saying 'Day 2: 30 Days of python programming'

#Day 2: 30 Days of python programming

#Declare a first name variable and assign a value to it

from itertools import count


first_name = 'Luis'

#Declare a last name variable and assign a value to it

last_name = 'Acosta'

#Declare a full name variable and assign a value to it

full_name = 'Luis Acosta'

#Declare a country variable and assign a value to it

country = 'México'

#Declare a city variable and assign a value to it

city = 'CDMX'

#Declare an age variable and assign a value to it

age = 28

#Declare a year variable and assign a value to it

year = 2022

#Declare a variable is_married and assign a value to it

is_married = 'No'

#Declare a variable is_true and assign a value to it

is_true = True

#Declare a variable is_light_on and assign a value to it

is_light = False

#Declare multiple variable on one line

a, b, c = 8, 12.5, 4-16j

#Check the data type of all your variables using type() built-in function

print(first_name)
print(type(first_name))

print(last_name)
print(type(last_name))

print(full_name)
print(type(full_name))

print(country)
print(type(country))

print(city)
print(type(city))

print(age)
print(type(age))

print(year)
print(type(year))

print(is_married)
print(type(is_married))

print(is_true)
print(type(is_true))

print(is_light)
print(type(is_light))

print(a)
print(type(a))

print(b)
print(type(b))

print(c)
print(type(c))

#Using the len() built-in function, find the length of your first name

print(first_name)
print(len(first_name))

#Compare the length of your first name and your last name

print(last_name)
print(len(last_name))
print("first_name > last_name ?")
print(len(first_name) > len(last_name))


#Declare 5 as num_one and 4 as num_two

num_one = 5
num_two = 4
print("num_one:",num_one)
print("num_two:",num_two)

#Add num_one and num_two and assign the value to a variable total

print("addition")
total = num_one + num_two
print(total)

#Subtract num_two from num_one and assign the value to a variable diff

print("substraction")
diff = num_one - num_two
print(diff)

#Multiply num_two and num_one and assign the value to a variable product

print("multiplication")
product = num_one * num_two
print(product)

#Divide num_one by num_two and assign the value to a variable division

print("division")
division = num_one / num_two
print(division)

#Use modulus division to find num_two divided by num_one and assign the value to a variable remainder

print("modulus")
remainder = num_two % num_one
print(remainder)

#Calculate num_one to the power of num_two and assign the value to a variable exp

print("power")
exp = num_one ** num_two
print(exp)

#Find floor division of num_one by num_two and assign the value to a variable floor_division

print("floor division")
floor_division = num_one // num_two
print(floor_division)

#The radius of a circle is 30 meters.

radious = 30
print("Radious:",radious)


#Calculate the area of a circle and assign the value to a variable name of area_of_circle
from math import pi

area_of_circle = pi * radious**2
print("Area:",area_of_circle)

#Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle

circum_of_circle = 2 * pi * radious
print("Circumference:",circum_of_circle)

#Take radius as user input and calculate the area.

radious = float(input("Enter the radious: "))
area_of_circle = pi * radious**2
print("Area: ",area_of_circle)

#Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names

first_name = input("Enter your name: ")
last_name = input("Enter your last name: ")
country = input("Enter your country: ")
age = int(input("Enter your age: "))

print("Hi,", first_name, last_name, "you live in", country, "and you are", age, "years old")



