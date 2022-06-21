it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

print(it_companies)
#Find the length of the set it_companies

print("set",it_companies)
print(len(it_companies))

#Add 'Twitter' to it_companies

it_companies.add('Twitter')

#Insert multiple IT companies at once to the set it_companies

list1 = ["SIEMENS","Intel","HP","ADOBE"]
it_companies.update(list1)
print(it_companies)

#Remove one of the companies from the set it_companies

it_companies.remove('Oracle')
it_companies.pop()

#What is the difference between remove and discard

"""the remove() method will raise an error if the specified item does not exist, and the discard() method will not"""

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

#Join A and B

print(A)
print(B)
print("Join A-B")
a = A.union(B)
print(A)

#Find A intersection B

b = A.intersection(B)
print(b)

#Is A subset of B

print("A Is subset of B")
print(A.issubset(B))

#Are A and B disjoint sets

print("A Is disjoint of B")
print(A.isdisjoint(B))

#Join A with B and B with A


a = A.union(B)
b = B.union(A)
print("AunionB:",a)
print("BunionA:",b)

# is the symmetric difference between A and B

print("Simetric difference")
print(A.symmetric_difference(B))

#Delete the sets completely

del A
del B
del it_companies

age = [22, 19, 24, 25, 26, 24, 25, 24]

#Convert the ages to a set and compare the length of the list and the set, which one is bigger?

print("Age", age)
age_set = set(age)
print(age_set)
print("Direcence between length set and length list")
print("List:", len(age))
print("Set:", len(age_set))

#Explain the difference between the following data types: string, list, tuple and set

"""
STRING
- Strings in python are surrounded by either single quotation marks, or double quotation marks.
- strings in Python are arrays of bytes representing unicode characters
SOME STRING FUNCTIONS
* capitalize( ) function
* lower( ) function
* title( ) function
* casefold( ) function
* upper( ) function
* count( ) function
* find( ) function
* replace( ) function
* swapcase( ) function
* join( ) function
https://www.w3schools.com/python/python_ref_string.asp

List
- Lists are used to store multiple items in a single variable.
- Lists are one of 4 built-in data types in Python used to store collections of data
- Lists are created using square 
- List items are ordered, changeable, and allow duplicate values. 
  When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
- If you add new items to a list, the new items will be placed at the end of the list.

SOME LIST FUNCTIONS
* insert()
* append()
* remove()
* extend()
* count()
* index()
* copy()
* sort()
* reverse()
* clear()
* pop()

Tuple
- Tuples are used to store multiple items in a single variable.
- A tuple is a collection which is ordered and unchangeable.
- Tuples are written with round brackets.
- When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
- Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
- Since tuples are indexed, they can have items with the same value

SOME TUPLE FUNCTIONS
* len()
* join tpl = tpl1 + tpl2
* count()
* index()

Set
- Sets are used to store multiple items in a single variable.
- A set is a collection which is unordered, unchangeable*, and unindexed.
- Sets are written with curly brackets.
- Set items are unordered, unchangeable, and do not allow duplicate valu
- Unordered means that the items in a set do not have a defined order.

  Set items can appear in a different order every time you use them, and cannot be referred to by index or key.
- Set items are unchangeable, meaning that we cannot change the items after the set has been created.

- Sets cannot have two items with the same value.

SOME SET FUNCTIONS

* add()
* clear()
* copy()
* difference()
* diference_update()
* discard()
* intersection()
* intersection_update()
* isdisjoint()
* issubset()
* issuperset()
* pop()
* remove()
* symmetric_difference()
* symmetric_difference_update()
* union()
* update()

"""
#I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.

sentence = "I am a teacher and I love to inspire and teach people"
list1 = sentence.split(" ")
print("Len list: ", len(list1))
set1 = set(sentence.split(" "))
print("Len set: ", len(set1))
print(set1)