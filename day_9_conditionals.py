#Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
"""
Enter your age: 30
You are old enough to learn to drive.
Output:
Enter your age: 15
You need 3 more years to learn to drive.
"""

print("Age")
age = int(input("Enter your age: "))
if age >= 18 and age < 112:
    print("You are old enough to drive.")
elif age >=0 and age < 18:
    print(f"You need {18 - age} more years to learn to drive.")
else:
    print("Enter a correctly age")


#Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
"""
Enter your age: 30
You are 5 years older than me.
"""

print("younger, older")
my_age = 28
your_age = int(input("Enter your age: "))
if my_age > your_age:
    diference = my_age - your_age
    if diference == 1:
        print(f"You are {diference} year younger than me.")
    else:
        print(f"You are {diference} years younger than me.")
elif your_age > my_age:
    diference =  your_age -my_age
    if diference == 1:
        print(f"You are {diference} year older than me.")
    else:
        print(f"You are {diference} years older than me.")
else:
    print("We're both just as old")

#Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
"""
Enter number one: 4
Enter number two: 3
4 is greater than 3
"""

print("Comparing two numbers")
a = int(input("Enter number one: "))
b = int(input("Enter number two: "))

if a > b:
    print("a is greater than b")
elif b > a:
    print("a is smaller than b")
else:
    print("a is equal to b")


#Write a code which gives grade to students according to theirs scores:
"""
90-100, A
80-89, B
70-79, C
60-69, D
50-59, E
0-49, F
"""

print("Score")
score = 80
print(score)

if score >= 90 and score <= 100:
    print(score, "A")
elif score >= 80 and score < 90:
    print(score, "B")
elif score >= 70 and score < 80:
    print(score, "C")
elif score >= 60 and score < 70:
    print(score, "D")
elif score >= 50 and score < 60:
    print(score, "E")
elif score >= 0 and score < 50:
    print(score, "F")
else:
    print("ERROR - Enter a correct number")

#Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer

print("SEASON")
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

#The following list contains some fruits:
fruits = ['banana', 'orange', 'mango', 'lemon']
#If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')

print("Fruits")
fruit = input("Enter a fruit: ")
if fruit in fruits:
    fruits.append(fruit)
    print(fruits)
else:
    print("That fruit already exist in the list")
    print(fruits)

#Here we have a person dictionary. Feel free to modify it!
    person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
 #Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
 
print(person)

print("Middle skills")

if "skills" in person.keys():
    if len(person["skills"]) % 2 == 0:
        print(person["skills"][((len(person["skills"])+1)//2)-1],person["skills"][len(person["skills"])//2])
    else:
        print(person["skills"][(len(person["skills"])+1)//2])
else:
    print("This person don't have skills")

 
 #Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
 
print("Python in dictionary")
if "skills" in person.keys():
    if "Python" in person["skills"]:
        print(person["skills"])
    else:
        print("Python isn't in skills")
else:
    print("This person don't have skills")
 
 #If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!

print("Front end, Backend or fullstack developer?")
if "skills" in person.keys():
    if len(person["skills"]) == 2 and "JavaScript" in person["skills"] and "React" in person["skills"]:
        print("He/She is a front end developer")
    elif "Node" in person["skills"] and "Python" in person["skills"] and "MongoDB" in person["skills"]:
        print("He is a backend developer")
    elif "React" in person["skills"] and "Node" in person["skills"] and "MongoDB" in person["skills"]:
        print("He is a fullstack developer")
    else:
        print("unknown title")
else:
    print("This person don't have skills")

 #If the person is married and if he lives in Finland, print the information in the following format:
 #Asabeneh Yetayeh lives in Finland. He is married.

if person["is_marred"] == True and person["country"] == "Finland":
    print(person["first_name"], person["last_name"], "lives in", person["country"]+".", "He is married.")
