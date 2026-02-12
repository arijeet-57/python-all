# foods in a buffet
foods = ('curry' , 'fried eggs', 'salad' , 'beans' , 'hotdog')
for f in foods: 
    print(f)         #printing all the elements of the tuple 

# foods[0] = "study" python rejects this line as tupe is immutable

foods = ('curry' , 'fried eggs', 'salad', 'fries', 'burger')
for f in foods:
    print(f)


animals = ['lion', 'cow', 'buffalo']

if 'donkey' not in animals:
    print("How are you?")


# Write a series of conditional tests. Print a statement describing each test and your prediction for the results of each test

age = 14 
print("Is age = 14 ?  True")
print(age == 14)

age = 15 
print("Is age = 14 ?  False")
print(age == 14)


name = 'sam' 
print("Is name = 'sam' ?  True")
print(name == 'sam')

name = 'mike'
print("Is name = 'sam' ?  False")
print(name == 'sam')


name = 'Sam' 
print("Is name = 'sam' ?  True")
print(name.lower() == 'sam')

name = 'mike' 
print("Is name = 'sam' ?  True")
print(name.lower() == 'sam')


name = 'Sam' 
print(name.lower() == 'sam' and name.upper() == 'SAM')

name = 'Sam' 
print(name.lower() == 'sam' or name.upper() == 'mike')

lists = ['shop', 'carry']
print('dog' in lists)

lists = ['shop', 'carry']
print('dog' not in lists)


