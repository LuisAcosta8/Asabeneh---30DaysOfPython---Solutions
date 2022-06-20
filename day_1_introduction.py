Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Open the python interactive shell and do the following operations. The operands are 3 and 4.
#addition

3+4
7
#substraction
3-4
-1
#multiplication
3*4
12
#modulus
3%4
3
#division
3/4
0.75
#exponential
3**4
81
#floor division operator
3//4
0
#Check the data types of the following data
#10
type(10)
<class 'int'>
#9.8
type(9.8)
<class 'float'>
#3.14
type(3.14)
<class 'float'>
#4-4j
type(4-4j)
<class 'complex'>
#['Asabeneh', 'Python', 'Finland']
type(['Asabeneh', 'Python', 'Finland'])
<class 'list'>
#Your name
type('Luis')
<class 'str'>
#Your family name
type('Acosta')
<class 'str'>
#Your country
type('México')
<class 'str'>
#Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.
#integer
8
8
#float
15.368
15.368
#complex
9-18j
(9-18j)
#string
'Hello'
'Hello'
#boolean
True
True
#list
['Hello','world','!']
['Hello', 'world', '!']
#tuple
('Luis',8)
('Luis', 8)
#set
{15,8,8,16,9,75}
{16, 8, 9, 75, 15}
#dictionary
{'Name':'Luis','Last name':'Acosta','Age':28}
{'Name': 'Luis', 'Last name': 'Acosta', 'Age': 28}
#Find an Euclidian distance between (2, 3) and (10, 8)
from math import sqrt
sqrt((10-2)**2 + (8-3)**2)
9.433981132056603
