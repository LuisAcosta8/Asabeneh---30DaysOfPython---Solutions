


#Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.

print('Thirty', 'Days', 'Of', 'Python')


#Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.

print('Coding', 'For' , 'All')

#Declare a variable named company and assign it to an initial value "Coding For All".

company = "Coding For All"

#Print the variable company using print().

print("company = 'Coding For All'")
print(company)

#Print the length of the company string using len() method and print().

print("len")
print(len(company))

#Change all the characters to uppercase letters using upper() method.

print("upper")
print(company.upper())

#Change all the characters to lowercase letters using lower() method.

print("lower")
print(company.lower())

#Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.

print("capitalize")
print(company.capitalize())
print("title")
print(company.title())
print("swapcase")
print(company.swapcase())

#Cut(slice) out the first word of Coding For All string.

print("Slice the first word of Coding For All")
print(company[0:6])

#Check if Coding For All string contains a word Coding using the method index, find or other methods.

print("Find")
print(company.find('Coding'))
print("Rfind")
print(company.rfind('Coding'))
print("index")
word = "Coding"
print(company.index(word))
print("rindex")
print(company.rindex(word))


#Replace the word coding in the string 'Coding For All' to Python.

print("Replace")
print(company.replace('Coding', 'Python'))

#Change Python for Everyone to Python for All using the replace method or other methods.

print(company.replace('All', 'Everyone'))

#Split the string 'Coding For All' using space as the separator (split()) .

print("Split")
print(company.split(' '))

#"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.

companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies)
print(companies.split(","))

#What is the character at index 0 in the string Coding For All.

company = "Coding For All"
print("Coding for all [0]")
print(company[0])

#What is the last index of the string Coding For All.

print("Coding for all [-1]")
print(company[-1])

#What character is at index 10 in "Coding For All" string.

print("Coding for all [10]")
print(company[10])

#Create an acronym or an abbreviation for the name 'Python For Everyone'.

print("Acronym for 'Python For Everyone'")
print("PFE")

#Create an acronym or an abbreviation for the name 'Coding For All'.

print("Acronym for 'Coding For All'")
print("CFA")

#Use index to determine the position of the first occurrence of C in Coding For All.

char = "C"
print("Index C in Coding For All")
print(company.index(char))

#Use index to determine the position of the first occurrence of F in Coding For All.

char = "F"
print("Index C in Coding For All")
print(company.index(char))

#Use rfind to determine the position of the last occurrence of l in Coding For All People.

company = "Coding For All People"
char = "l"
print("Rfind last l in Coding For All People")
print(company.rfind(char))

#Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You  cannot end a sentence with because because because is a conjunction'

sentence = 'You  cannot end a sentence with because because because is a conjunction'
word = 'because'
print("Index first because in 'You  cannot end a sentence with because because because is a conjunction'")
print(sentence.index(word))
print("Find first because in 'You  cannot end a sentence with because because because is a conjunction'")
print(sentence.find(word))

#Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

print('last because in sentence')
print(sentence.rindex(word))

#Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because  because because is a conjunction'

print(sentence[0:39],sentence[56:])

#Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence  with because because because is a conjunction'

print(sentence.find('because'))

#Does ''Coding For All' start with a substring Coding?

"""Yes, ' is a substring """

#Does 'Coding For All' end with a substring coding?

"""No, the sentence starts with C"""

#'   Coding For All      '  , remove the left and right trailing spaces in the given string.

sentence = '   Coding For All      '
print(sentence.replace(' ', ''))
print(sentence.strip(' '))      #This line solved the problem

#Which one of the following variables return True when we use the method isidentifier(): 


a = '30DaysOfPython'
b = 'thirty_days_of_python'
print("30DaysOfPython isidentifier?")
print(a.isidentifier())
print("thirty_days_of_python isidentifier?")
print(b.isidentifier())



"""The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. """
#Join the list with a hash with space string.

libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result = ' #'.join(libraries)
print(result)

#Use the new line escape sequence to separate the following sentences.
# I am enjoying this challenge. I just wonder what is next.

print("I am enjoying this challenge.\nI just wonder what is next.")

#Use a tab escape sequence to write the following lines.
"""Name      Age     Country   City
   Asabeneh  250     Finland   Helsinki"""

print("NAME\t\tAGE\tCOUNTRY\t\tCITY\nAsabeneh\t250\tFinland\t\tHelsinki")
#Use the string formatting method to display the following:
"""radius = 10
   area = 3.14 * radius ** 2
   The area of a circle with radius 10 is 314 meters square."""

print("Radius = 10\narea = 3.14 * radius **2\nThe area of a circle with radius 10 is 314 meters square.")

#Make the following using string formatting methods:
"""
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144
"""

a = 8
b = 6

print("{} + {} = {}".format(a, b, a+b))
print("{} - {} = {}".format(a, b, a-b))
print("{} * {} = {}".format(a, b, a*b))
print("{} / {} = {}".format(a, b, a/b))
print("{} % {} = {}".format(a, b, a%b))
print("{} // {} = {}".format(a, b, a//b))
print("{} ** {} = {}".format(a, b, a**b))
