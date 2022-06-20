#Declare an empty list

list1 = []
print(list1)

#Declare a list with more than 5 items

dogs = ['schnauzer', 'bobtail', 'golden retriever', 'Scottish terrier', 'chihuahua', 'bulldog']

#Find the length of your list

print(dogs)
print("length of dogs")
print(len(dogs))

#Get the first item, the middle item and the last item of the list

print("First element of dogs")
print(dogs[0])
print("Middle element of dogs")
print(round(len(dogs))/2)
print("Last element of dogs")
print(dogs[-1])

#Declare a list called mixed_data_types, put your(name, age, height, marital status, address)


mixed_data_types = ['Luis',28,1.63,'Single', 'J. B. Sepulveda 40']
print(mixed_data_types)


#Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

#Print the list using print()

print(it_companies)

#Print the number of companies in the list

print("Length")
print(len(it_companies))

#Print the first, middle and last company

print("First company")
print(it_companies[0])
print("Middle company")
print(it_companies[round(len(it_companies))//2])
print("Last company")
print(it_companies[-1])

#Print the list after modifying one of the companies

print("Midifying the list")
it_companies[0] = 'Meta'
print(it_companies)

#Add an IT company to it_companies

print("append")
it_companies.append("Xiaomi")
print(it_companies)

#Insert an IT company in the middle of the companies list

print("insert")
it_companies.insert(round(round(len(it_companies))/2), 'Siemens')
print(it_companies)

#Change one of the it_companies names to uppercase (IBM excluded!)

print("Upper")
it_companies[4] = it_companies[4].upper()

#Join the it_companies with a string '#;  '

print("Join")
result = '#; '.join(it_companies)
print(result)

#Check if a certain company exists in the it_companies list.

print("word in list")
print('Facebook' in it_companies)
print('Oracle' in it_companies)

#Sort the list using sort() method

print("sort")
print(it_companies.sort())

#Reverse the list in descending order using reverse() method

print("reverse")
print(it_companies.sort(reverse=True))
print(it_companies.reverse())

#Slice out the first 3 companies from the list

print("Slice first 3 companies")
print(it_companies[0:3])

#Slice out the last 3 companies from the list

print("Slice last 3 companies")
print(it_companies[-1:-3])

#Slice out the middle IT company or companies from the list

print("Middle company")
print(it_companies[round(round(len(it_companies))/2)])

#Remove the first IT company from the list

print("Remove first item of the list with del")
del it_companies[0]
print(it_companies)

#Remove the middle IT company or companies from the list

print("Remove the middle item of the list with del")
del it_companies[round(round(len(it_companies))//2)]
print(it_companies)

#Remove the last IT company from the list

print("Remove the last item of the list with pop")
it_companies.pop()

#Remove all IT companies from the list

print("Clear all elements in the list")
it_companies.clear()
print(it_companies)

#Destroy the IT companies list

del it_companies
#print(it_companies)         #ERROR

#Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

print(front_end + back_end)


#After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.

print("Insert python and sql after Redux")
full_stack = front_end + back_end
full_stack.insert(5, 'SQL')
full_stack.insert(5, 'Python')
print(full_stack)


#The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
#Sort the list and find the min and max age

print(ages)
ages.sort()
print(ages)

print("min: ",ages[0])
min = ages[0]
print("max: ",ages[-1])
max = ages[-1]
#Add the min age and the max age again to the list

ages.append(min)
ages.append(max)
print(ages)

#Find the median age (one middle item or two middle items divided by two)

ages.sort()
print(ages)
print("Median")


#Find the average age (sum of all items divided by their number )

average = sum(ages)/len(ages)
print("Average: ", average)

#Find the range of the ages (max minus min)

print("Range", max-min)

#Compare the value of (min - average) and (max - average), use abs() method

print(min - average)
print(max-average)
print("min-average == max-average?")
print(min - average == max-average)

"""
#Find the middle country(ies) in the countries list
#https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries.py
print(countries[len(countries)/2])


#Divide the countries list into two equal lists if it is even if not one more country for the first half.
['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
list1 = countries[:len(countries)/2] 
list2 = countries[len(countries)/2:]


#Unpack the first three countries and the rest as scandic countries.

print(countries[0:3]])
print(countries[3:])
"""