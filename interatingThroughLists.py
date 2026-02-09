# #we can iterate throught the elements of a list using for loop
# #below is an example of how we can do so
# magicians = ['alice', 'bob', 'emily', 'dave']
# for m in magicians:
#     print(m)


# #printing a message for each
#     print("How are you " + m.title() + " ?")

# #exercise
# pizzas = ['margherita', 'pepperoni', 'sausage']
# for p in pizzas:
#     print("I love "+ p.title() + " pizza !")

# print("I love pizza and all of its types !!")

#exercise 2
# animals = ['pangolin', 'platypus', 'penguin']
# for a in animals:
#     print("The "+ a.title() + " is a great animal !")
# print("I love animal and all of its types !!")

#printing the squares of numbers
# squares = [] #null list
# for i in range(1,11):
#     squares.append(i**2)
# print(squares)

#from here onwards i will be writing in list comprehenstions
#1. Counting to twenty
# count = [i for i in range(1,21)]
# print(count)

# #2. One Million
# millionCount = [i for i in range(1, 1000001)]
# print(millionCount)

# #3. Summing a Million
# #using the previous answer
# maximum = max(millionCount)
# print(maximum)
# minimum = min(millionCount)
# print(minimum)
# sumOf = sum(millionCount)
# print(sumOf)

#4. Odd numbers from 1 to 20
# oddNumbers = [odd for odd in range(1,21,2)]
# print(oddNumbers)

#5. Multiples for 3 from 3 to 30
# multiples = [num*3 for num in range(1,11)]
# print(multiples)

#6. Cube of numbers
# cube = [num**3 for num in range(1,11)]
# print(cube)

cube = []
for i in range(1,11):
    numbers = i**3
    cube.append(numbers)
print(cube)





