#Create an empty tuple

tup = tuple()

#Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)

tpl_bro = ('Kevi','Lalito')
print(tpl_bro)
tpl_sis = ('Lety', 'Dany')
print(tpl_sis)

#Join brothers and sisters tuples and assign it to siblings

siblings = tpl_bro + tpl_sis

#How many siblings do you have?

print(siblings)
print("How many siblings do you have?")
print(len(siblings))

#Modify the siblings tuple and add the name of your father and mother and assign it to family_members

family_members = siblings + ('Margaret','Cirilo')

#Unpack siblings and parents from family_members

(br1, br2, sis1, sis2, mother, father) = family_members
print(br1)
print(br2)
print(sis1)
print(sis2)
print(mother)
print(father)

#Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.

fruits = ('Grape','Banana','Orange')
vegetables = ('Carrot','Potatoe','Corn')
animal_products = ('Milk','Egg','Honey')
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

#Change the about food_stuff_tp tuple to a food_stuff_lt list

food_stuff_lt = list(food_stuff_tp)

#Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.

print("Slice middle items")
print(food_stuff_tp[3], food_stuff_tp[4])
print(food_stuff_lt[3], food_stuff_lt[4])


#Slice out the first three items and the last three items from food_staff_lt list

print("Slice 3 first items")
print(food_stuff_tp[0:3])
print("Slice 3 last items")
print(food_stuff_tp[-3:])

#Delete the food_staff_tp tuple completely

del food_stuff_tp

#Check if an item exists in next tuple:

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Nordic countries:",nordic_countries)

#Check if 'Estonia' is a nordic country

print("word in tpl")
print("Estonia")
print('Estonia' in nordic_countries)

#Check if 'Iceland' is a nordic country

print("word in tpl")
print("Iceland")
print('Iceland' in nordic_countries)
