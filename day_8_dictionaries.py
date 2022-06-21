#Create an empty dictionary called dog

dog = {}

#Add name, color, breed, legs, age to the dog dictionary

dog["Name"] = "Bruno"
dog["Color"] = "White with brown"
dog["Breed"] = "English Pitbull"
dog["Legs"] = "Shorts white legs"
dog["Age"] = "4 years"
print("Dog with values:", dog)


#Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary

student_dict = {"first_name":"", "last_name":"", "gender":"", "age":"", "marital status":"", "skills":"", "country":"", "city":"", "address":""}

#Get the length of the student dictionary

print(student_dict)
print("Length:", len(student_dict))

#Get the value of skills and check the data type, it should be a list

student_dict["first_name"] = "Luis"
student_dict["last_name"] = "Acosta"
student_dict["gender"] = "M"
student_dict["age"] = 28
student_dict["marital status"] = "Single"
student_dict["skills"] = "Python, Microsoft Ofice, SQL"
student_dict["country"] = "México"
student_dict["city"] = "CDMX"
student_dict["adress"] = "J B Sepulveda 40, 07058"

print(student_dict)

#Modify the skills values by adding one or two skills

a = student_dict["skills"]
a = a + " R Studio" + " Git"
student_dict["skills"] = a
print("Adding two skills: ", student_dict)

#Get the dictionary keys as a list

keys = student_dict.keys()
print("Keys list: ", keys)

#Get the dictionary values as a list

values = student_dict.values()
print("Values list",values)

#Change the dictionary to a list of tuples using items() method

print("List of tuples")
print(student_dict.items())

#Delete one of the items in the dictionary

print("Remove one of the items")
student_dict.pop("city")    #It delete key and value, you must to specify the key as argument 
student_dict.popitem()  #Only delete the value
print(student_dict)

#Delete one of the dictionaries

del student_dict

#print(student_dict)     #student_dict doesn't exist, this is why the program returns error
