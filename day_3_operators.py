#Declare your age as integer variable

from email.mime import base
import string
from turtle import width


age = int(28)

#Declare your height as a float variable

height = float(1.63)

#Declare a variable that store a complex number

comp = 4-8j

#Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
"""
Enter base: 20
Enter height: 10
The area of the triangle is 100
"""

t_base = float(input("Enter base: "))
t_height = float(input("Enter height: "))
area = 0.5 * t_base * t_height
print("The area of the triangle is",area)


#Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
"""
Enter side a: 5
Enter side b: 4
Enter side c: 3
The perimeter of the triangle is 12
"""

side_a = float(input("Enter side a: "))
side_b = float(input("Enter side b: "))
side_c = float(input("Enter side c: "))
perimeter = side_a + side_b + side_c
print("The perimeter of the triangle is", perimeter)

#Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))

length = float(input("Enter the lenght ob the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width
perimeter = 2 * (length + width)

#Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
from math import pi

radious = float(input("Enter radious: "))
area = pi * radious * radious
c = 2 * pi* radious
print("Area:",area)
print("Circurference:",c)


#Calculate the slope, x-intercept and y-intercept of y = 2x -2




#Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
from math import sqrt
print("Punto 1 = (2,2) \t Punto 2 = (6,10)")
slope = (10-2)/(6-2)
Edistance = sqrt((10-2)**2/(6-2)**2)
print("Slope = ", slope)
print("Euclidean distance = ",Edistance)

#Compare the slopes in tasks 8 and 9.



#Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.

x = 0
y = x**2 + 6*x + 9
print("Y = ",y)

#Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print("Python and dragon")
a = len("python")
b = len("dragon")
print(a!=b)

#Use and operator to check if 'on' is found in both 'python' and 'dragon'

print("on in word")
print("on" in "python")
print("on" in "dragon")

#I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.

print("jargon in sentence")
print("jargon" in "I hope this course is not full of jargon")

#There is no 'on' in both dragon and python

print("there is no on in word")
print("on" not in "python")
print("on" not in "dragon")

#Find the length of the text python and convert the value to float and convert it to string

length = len("python")
print(float(length))
print(string(length))

#Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?

"""With module (%) module retunrs the remainder of a division if the result is 0 it will be an even number."""

#Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.

print("7//3 is equal to int(2.7)?")
print(7//3 == int(2.7))

#Check if type of '10' is equal to type of 10

print("type '10' is equal to type 10?")
print(type('10') == type(10))

#Check if int('9.8') is equal to 10

print("int(9.8) is equal to 10?")
print(int(9.8) == 10)

#Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
"""
Enter hours: 40
Enter rate per hour: 28
Your weekly earning is 1120
"""

hours = int(input("Enter hours: "))
rph = float(input("Enter rat per hour: "))
print("Your weekly earning is: ", hours * rph)

#Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
"""
Enter number of years you have lived: 100
You have lived for 3153600000 seconds.
"""

years = int(input("Enter number of years you have lived: "))
seconds = years * 31536000
print("You have lived for", seconds, "seconds")

#Write a Python script that displays the following table
"""
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
"""

print(1, 1//1, 1*1, 1**2, 1**3)
print(2, 2//2, 2*1, 2**2, 2**3)
print(3, 3//3, 3*3, 3**2, 3**3)
print(4, 4//4, 4*1, 4**2, 4**3)
print(5, 5//5, 5*1, 5**2, 5**3)