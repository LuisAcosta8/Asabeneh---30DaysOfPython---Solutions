#Declare a function add_two_numbers. It takes two parameters and it returns a sum.

def add_two_numbers(a, b):
    return a + b

#Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.

from math import pi
from tkinter import N
def area_of_circle(radius):
    return pi * radius**2

#Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.

def add_all_nums(*numbers):
    total = 0
    for n in numbers:
        total = total + n
    return total

def add_all_nums_2(*nums):
    return sum(nums)

#Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to_fahrenheit.

def convert_celsius_to_fahrenheit(celsius):
    F = (celsius * 9/5) + 32
    print("°Farenheit:", F)
    return F

#Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.

def check_season(month):
    month = input("Enter a month: ")
    if month == "September" or month == "October" or month == "November":
        print("The season is Autumn")
    elif month == "December" or month == "January" or month == "February":
        print("The season is Winter")
    elif month == "March" or month == "April" or month == "May":
        print("The season is Spring")
    elif month == "June" or month == "July" or month == "August":
        print("The season is Summer")
    else:
        print("ERROR")

#Write a function called calculate_slope which return the slope of a linear equation

def calculate_slope(x1, x2, y1, y2):
    m = (y2 - y1) / (x2 - x1)
    return m

#Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.

from math import sqrt
def solve_quadratic_eqn(a,b,c):
    x1 = (-b+sqrt(b**2 - 4*a*c))/2*a
    x2 = (-b-sqrt(b**2 - 4*a*c))/2*a
    return (f"x1 = {x1}    x2 = {x2}")

#Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.

def print_list(*args):
    l = []
    for word in args:
        l.append(word)
    print(l)

#Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
"""
print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
print(reverse_list1(["A", "B", "C"]))
# ["C", "B", "A"]
"""

def reverse_list(*args):
    l = []
    for i in args:
        l.append(i)

#Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items

def capitalize_list_items(*args):
    l = []
    for arg in args:
        l.append(arg.capitalize())
    print(l)


#Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
"""
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
numbers = [2, 3, 7, 9];
print(add_item(numbers, 5))      [2, 3, 7, 9, 5]
"""

def add_item(name_list, item):
    name_list.append(item)

#Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
"""
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9];
print(remove_item(numbers, 3))  # [2, 7, 9]
"""

def remove_item(name_list, item):
    name_list.remove(item)
    print(name_list)

#Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
"""
print(sum_of_numbers(5))  # 15
print(sum_all_numbers(10)) # 55
print(sum_all_numbers(100)) # 5050
"""

def sum_of_numbers(num):
    n = 0
    sum = 0
    while n <= num:
         sum = sum + n
         n += 1
    print(sum)

#Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.

def sum_of_odds(initial,end):
    sum = 0
    for i in range(initial,end):
        if i % 2 != 0:
            sum = sum + i
    print(sum)

#Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.

def sum_of_even(initial,end):
    sum = 0
    for i in range(initial,end):
        if i % 2 == 0:
            sum = sum + i
    print(sum)

#Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
"""
print(evens_and_odds(100))
# The number of odds are 50.
# The number of evens are 51.
"""

def evens_and_odds(number):
    odds = 0
    evens = 0
    for n in range(0, number+1):
        if n % 2 == 0:
            evens = evens + 1
        elif n % 2 != 0:
            odds = odds + 1
    print(f"The number of odds are {odds}")
    print(f"The number of evens are {evens}")

#Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number

def factorial(num):
    fact = 1
    for i in range(fac + 1):
        fact *= i
    return fact
    
    
    """
    if num == 1:
        return 1
    else:
        return (num * factorial(num-1))
    """
#Call your function is_empty, it takes a parameter and it checks if it is empty or not

def is_empty(parameter=0):
    parameter = bool(parameter)
    if parameter is True:
        print("Is not empty")
    else:
        print("Is empty")

#Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range calculate_variance, calculate_std (standard deviation).

def mean(name_list):
    return sum(name_list) / len(name_list)


def median(name_list):
    data = sorted(name_list)
    index = len(data) // 2

    if len(name_list) % 2 != 0:
        return data[index]

    return (data[index - 1] + data[index]) / 2


def mode(name_list):
    frequency = {}

    for value in name_list:
        frequency[value] = frequency.get(value, 0) + 1

    most_frequent = max(frequency.values())

    modes = [key for key, value in frequency.items() if value == most_frequent]

    return modes


def variance(name_list):
    n = len(name_list)
    mean = sum(name_list) / n
    deviations = [(x - mean) ** 2 for x in name_list]
    variance = sum(deviations) / n
    return variance


def stdev(name_list):
    var = variance(name_list)
    std_dev = var ** 0.5
    return std_dev

#Write a function called is_prime, which checks if a number is prime.

def is_prime(number):
    for n in range(2, number):
        if number % n == 0:
            continue
    print("Is prime")


#Write a functions which checks if all items are unique in the list.

l = ["Luis","luis","Luis","Alberto","Kevi"]

def unique_item(name_list):
    set1 = set(name_list)
    for it in set1:
        if it in name_list:
                if name_list.count(it) > 1:
                    print(f"{it} is not unique")
                else:
                    print(f"{it} is unique")
            

#Write a function which checks if all the items of the list are of the same data type.

def same_data_type(*args):
    list1 = list(args)
    for item in list1:
        print(f"{item} is {type(item)} type")
        for it in list1:
            if type(item) != type(it):
                print("Not all data is of the same type")

#Write a function which check if provided variable is a valid python variable

def variable_valid(variable):
    return re.match(r"[_a-z]\w*$", variable, flags=re.I)

#Go to the data folder and access the countries-data.py file.
"""
list_data = countries_data.data
total_languages_initial = []
for i in list_data:
    total_languages_initial.extend(i["languages"])
print("Languages = ", len(set(total_languages_initial)))
counts = {}
for i in total_languages_initial:
    counts[i] = counts.get(i, 0) + 1
"""
#Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
"""
def sort_dict_by_value(d, reverse=False):
    return dict(sorted(d.items(), key=lambda x: x[1], reverse=reverse))
"""
#Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.
"""
counts = sort_dict_by_value(counts, True)
for i in list(counts.items())[:20]:
    print(i)
populations = {}
for i in list_data:
    populations[i["name"]] = i["population"]
populations = sort_dict_by_value(populations, True)
for i in list(populations.items())[:20]:
    print(i)
"""