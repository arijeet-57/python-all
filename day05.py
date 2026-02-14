# number = int(input("Enter a number: "))

# def sum_of_digits(num):
#     sum = 0 #intially assigning sum = 0
#     while num > 0:  #this loop will onyl work till the number is greater than 0, 
#         rem = num % 10 #here the remainder is stored for the number
#         sum += rem      #the sum now holds the number eg, 456%10 so sum is now equal to 6 and will add the other upcoming number
#         num = num//10      #now divide number (int division // not float /) so 456 //10 = 45
#     return sum #here sum = 6

# print("The sum of the digits is : " + str(sum_of_digits(number))  )



# Suppose user enters:
# Enter a number: 4729


# We trace the loop:

# Iteration 1
# num = 4729
# rem = 4729 % 10 = 9
# sum = 9
# num = 4729 // 10 = 472

# Iteration 2
# num = 472
# rem = 472 % 10 = 2
# sum = 11
# num = 472 // 10 = 47

# Iteration 3
# num = 47
# rem = 47 % 10 = 7
# sum = 18
# num = 47 // 10 = 4

# Iteration 4
# num = 4
# rem = 4 % 10 = 4
# sum = 22
# num = 4 // 10 = 0


# Loop stops because:

# while num > 0   → False


# Output:

# The sum of the digits is : 22


#vowel finder
# def vowel_finder():
#     character = input("Enter an alphabet: ")

#     match character:
#         case 'a':
#             print(f"{character} is a vowel")
#         case 'e':
#             print(f"{character} is a vowel")
#         case 'i':
#             print(f"{character} is a vowel")
#         case 'o':
#             print(f"{character} is a vowel")
#         case 'u':
#             print(f"{character} is a vowel")
#         case default:
#             print(f"{character} is a consonant")


# vowel_finder()

def ascii_finder():
    a = input("Enter a character: ")
    
    if a == " " or len(a) != 1:
        print("Enter a value !!")
    else:
        print(ord(a))
    
ascii_finder()

