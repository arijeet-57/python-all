import sys #needed for the gesize function

#user input basic validation and output
number = input("Enter an integer: ")
print("Your integer is: " + number)

#size of datatypes
print(sys.getsizeof(True))
print(sys.getsizeof(5))
print(sys.getsizeof(5.6))
print(sys.getsizeof("hello"))

#Number comparison
numberOne = input("Enter first number: ")
numberTwo = input("Enter second number: ")

if(numberOne > numberTwo) :
    print("The larger number is: " + numberOne)
elif(numberOne == numberTwo) :
    print("Both the numbers are equal")
else :
    print("The larger number is: " + numberTwo)