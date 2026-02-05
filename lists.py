#names in a list and accessing them
friends = ['Vandit', 'Rishabh', 'Sagar']
#print("how are you " + friends[0] + " ?")

vehicles = ['bike', 'car', 'scooty']
#print("I would like to buy a " + vehicles[1] + " one day")

#Operations on a list
people = ['alex', 'jordi', 'dave']
print("You are invitd to our party " + people[0].title())
print("You are invitd to our party " + people[1].title())
print("You are invitd to our party " + people[2].title())

#not_attending = people.pop(1) # I was thinking of doing this and printing it but the issue is if it pop it here then i won't be able to insert elmet here as the place is already blank using 'remove'
print(people[1].title() + " is not attending the party")

del people[1]
print(people)

people.insert(1, 'brandy')
print(people)

print("You are invited to our house-party " + people[0].title())
print("You are invited to our house-party " + people[1].title())
print("You are invited to our house-party " + people[2].title())



#found a bigger dinner table so more people are invited
print("Just got a bigger dinner table so we will be inviting more people")

people.insert(0, "richard")
people.insert(2, 'john')
people.append('bruce')

print(people)

print("Hello, Welcome to the party " + people[0].title())
print("Hello, Welcome to the party " + people[1].title())
print("Hello, Welcome to the party " + people[2].title())
print("Hello, Welcome to the party " + people[3].title())
print("Hello, Welcome to the party " + people[4].title())
print("Hello, Welcome to the party " + people[5].title())


print("There's been an issue so we will be able to invite only two people for the dinner")
first_pop = people.pop()
print("Sorry for the trouble " + first_pop.title())
second_pop = people.pop()
print("Sorry for the trouble " + second_pop.title())
third_pop = people.pop()
print("Sorry for the trouble " + third_pop.title())
fourth_pop = people.pop()
print("Sorry for the trouble " + fourth_pop.title())

print("You are still invited " + people[0].title())
print("You are still invited " + people[1].title())

print("We are inviting " + str(len(people)) + " people")

del people[0]
del people[0]
print(people)

