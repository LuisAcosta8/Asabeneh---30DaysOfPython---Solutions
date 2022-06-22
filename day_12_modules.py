import string
import random
#Write a function which generates a six digit/character random_user_id.
"""
  print(random_user_id());
  '1ee33d'
"""

def random_user_id():
    l1 = []
    for dig in string.digits:
        l1.append(dig)
    for st in string.ascii_letters:
        l1.append(st)
    user = ""
    for i in range(0,6):
        user = user + random.choice(l1)
    print(user)

#Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
"""
print(user_id_gen_by_user()) # user input: 5 5
#output:
#kcsy2
#SMFYb
#bWmeq
#ZXOYh
#2Rgxf 
print(user_id_gen_by_user()) # 16 5
#1GCSgPLMaBAVQZ26
#YD7eFwNQKNs7qXaT
#ycArC5yrRupyG00S
#UbGxOFI7UXSWAyKN
#dIV0SSUTgAdKwStr
"""

def user_id_gen_by_user():
    list1 = []
    for strings in string.ascii_letters:
        list1.append(strings)
    for num in string.digits:
        list1.append(num)
    characters = int(input("How many characters must have your user?: "))
    users = int(input("How many users do you want to create?: "))
    n = 1
    a = ""
    while n <= users:
        for i in range(characters):
            a = a + random.choice(list1)
        print(f"'{a}'")
        a = ""
        n+=1

def gen_ids(quantity,characters):
    l =[]
    for strings in string.ascii_letters:
        l.append(strings)
    for num in string.digits:
        l.append(num)
    n = 1
    id = ""
    while n <= quantity:
        for i in range (characters):
            id = id + random.choice(l)
        print(f"{id}")
        id = ""
        n+=1 

#Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
"""
print(rgb_color_gen())
# rgb(125,244,255) - the output should be in this form
"""

def rgb_color_gen():
    a = random.randint(0,255)
    b = random.randint(0,255)
    c = random.randint(0,255)
    print(f"rgb({a},{b},{c})")

#Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).

def list_of_hexa_colors(quantity):
    list = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
    n = 1
    hexa = "#"
    while n <= quantity:
        for i in range(6):
            hexa = hexa + random.choice(list)
        print(hexa)
        hexa = "#"
        n += 1

#Write a function list_of_rgb_colors which returns any number of RGB colors in an array.

def list_of_rgb_colors(quantity):
    a, b, c = 0, 0, 0
    n = 1
    color = ""
    l = []
    while n <= quantity:
        a, b, c = random.randint(0,255), random.randint(0,255), random.randint(0,255)
        color = f"rgb({a},{b},{c})"
        l.append(color)
        n+=1
    print(l)

#Write a function generate_colors which can generate any number of hexa or rgb colors.
"""
   generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b'] 
   generate_colors('hexa', 1) # ['#b334ef']
   generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
   generate_colors('rgb', 1)  # ['rgb(33,79, 176)']
"""

def generate_colors(kind, quantity):
    n = 1
    hexa = "#"
    color = ""
    l = []
    if kind == "hexa":
        list = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
        n = 1
        hexa = "#"
        while n <= quantity:
            for i in range(6):
                hexa = hexa + random.choice(list)
            l.append(hexa)
            hexa = "#"
            n += 1
        print(l)
    elif kind == "rgb":
        a, b, c = 0, 0, 0
        l = []
        while n <= quantity:
            a, b, c = random.randint(0,255), random.randint(0,255), random.randint(0,255)
            color = f"rgb({a},{b},{c})"
            l.append(color)
            n+=1
        print(l)
    else:
        print("Incorrect type")

#Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list

def shuffle_list(name_list):
    l = []
    for it in range(len(name_list)):
        a = random.choice(name_list)
        l.append(a)
    name_list = l
    print(name_list)

#Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.

def array():
    l = []
    for i in range(7):
        a = random.randint(0,9)
        l.append(a)
    print(l)
