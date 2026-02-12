#ccreate a program that simulates
#how websites ensure that everyone has a unique username

current_users = ['blake57', 'admin', '', 'jaDeHaRPer', 'bitchSluttyGaaaall']

new_users = ['ADMIN' , 'samuel8889', 'inminq00', 'jaDeHaRPer', 'samuel34']

usernames = [users.lower() for users in current_users]   #assigning current users to their lowercase versions

for users in new_users:
    if not users:   #check for empty username
        print("Username cannot be empty!")
        continue
    if users.lower() in usernames:     #case-insensitive comparison
        print(users + " already exists , try using a different username")
    else:
        print(users + " is available")
        