#Iterate 0 to 10 using for loop, do the same using while loop.

print("Count 0 to 10")
print("FOR")
for i in range(0,11):
    print(i)

i = 0
print("WHIILE")
while i <= 10:
    print(i)
    i += 1

#Iterate 10 to 0 using for loop, do the same using while loop.

print("Count 10 to 0")
print("FOR")
for i in range(10,-1,-1):
    print(i)

i = 10
print("WHIILE")
while i >= 0:
    print(i)
    i -= 1

#Write a loop that makes seven calls to print(), so we get on the output the following triangle:
  #
  ##
  ###
  ####
  #####
  ######
  #######

print("FOR")
a = "#"
for i in range(1,8):
    print(a)
    a = a + "#"
print("WHILE")
n = 0
a = "#"
while n <=7:
    print(a)
    a = a + "#"
    n += 1



#Use nested loops to create the following:
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #






#Print the following pattern:
"""
0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100
"""

print("FOR")
for n in range(0,11):
    print(f"{n} x {n} = {n*n}")

print("WHILE")
n = 0
while n <= 10:
    print(f"{n} x {n} = {n*n}")
    n += 1



#Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.

l = ['Python', 'Numpy','Pandas','Django', 'Flask']

print("List --> ", l)
for skill  in l:
    print(skill)

#Use for loop to iterate from 0 to 100 and print only even numbers

PRINT("EVEN NUMBERS")
print("FOR")
for i in range(2,101,2):
    print(i)

print("WHILE")
n = 1
while n <= 100:
    if  n % 2 == 0:
        print(n)
    n +=1

#Use for loop to iterate from 0 to 100 and print only odd numbers

print("ODD NUMBERS")
print("FOR")
for i in range(1,100,2):
    print(i)

print("WHILE")
n = 1
while n <= 100:
    if  n % 2 != 0:
        print(n)
    n +=1

#Use for loop to iterate from 0 to 100 and print the sum of all numbers.

a = 0
for i in range(0,101):
    a = a + i
print(a)        #The sum of all numbers is 5050.



#Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
e = 0
o = 0
for i in range(0,101,1):
    if i % 2 == 0:
        e = e + i
    else:
        o = o + i
print(e)                    #The sum of all evens is 2550.
print(o)                    #The sum of all odds is 2500.

#Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.



#This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.

fruits = ['banana', 'orange', 'mango', 'lemon']


#Go to the data folder and use the countries_data.py file.
#What are the total number of languages in the data



#Find the ten most spoken languages from the data



#Find the 10 most populated countries in the world


