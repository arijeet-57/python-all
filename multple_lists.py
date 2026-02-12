# eg: 
# available_toppings = ['mushrooms', 'olives', 'green peppers',
#  'pepperoni', 'pineapple', 'extra cheese']

# requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

# for requested_topping in requested_toppings:
#     if requested_topping in available_toppings:
#         print("Adding " + requested_topping + ".")
#     else:
#         print("Sorry, we don't have " + requested_topping + ".")

# print("\nFinished making your pizza!")


usernames = ['admin', 'user1', 'sam5858', 'danielsdani', 'harper']

if not usernames:     #if the list is empty this gets printed
    print("We need to find some users !") 

for username in usernames:
    if username == 'admin': #custom message for admin
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello " + username + ", thank yo for loggin in again !")