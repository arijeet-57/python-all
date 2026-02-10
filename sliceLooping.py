flowers = ['hibiscus', 'rose', ' lotus', 'lavendar', 'marigold']

def first_three_elements():
    print("The first three elements in this list are: " + str(flowers[:3]))

def middle_three():
    print("The middle three elements in this list are: " +  str(flowers[1:4]))

def last_three():
    print("The last three elements in this list are: " + str(flowers[-3:]))

# first_three_elements()
# middle_three()
# last_three()


#pizza slicing yeahhh !!
def pizza_party():
    my_pizzas = ['margherita','pepperoni', 'barbecue']
    friend_pizzas = my_pizzas[:]

    my_pizzas.append('chicken')
    friend_pizzas.append('paneer')

    print("My favorite pizzas are: ")
    for pizza in my_pizzas:
        print(pizza)

    print("My friend's favorite pizzas are: ")
    for pizza in friend_pizzas:
        print(pizza)

pizza_party()