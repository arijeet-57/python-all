#propgram to check odd Even
a = input("Enter a number: ")

if (int(a) % 2 == 0) :
    print("The number " + str(a) + " is even")
else : 
    print("The number " + str(a) + " is odd")

#program to check divisibility by 5
b = input("Enter a number: ")
if (int(b) % 5 == 0) :
    print("The number " + str(b) + " is divisible y 5")
else :
    print("The number " + str(b) + " is not divisible by 5")

#program to check if the entered number is a multiple of 7
c = input("Enter a number: ")
if (int(c) % 7 == 0) :
    print("The number " + str(c) + " is a multiple of 7")
else :
    print("The number " + str(c) + " is not a multiple of 7")
