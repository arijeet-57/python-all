#Multiplication table
def multiplication_table():
    num = int(input("Enter a number: "))    #taking the input as int
    for i in range(1,11):
        print(f"{num} x {i} = {num*i}") #using formatted string by using f


#calculator
def calculator_function():
    numOne = int(input("Enter a number: "))
    numTwo = int(input("Enter another number: "))
    choice = input("Choose operation : '+', '-', 'x' , '%' : ")

    match choice:
        case '+' :
            print(f"{numOne} + {numTwo} = {numOne+numTwo}")
        case '-' :
            print(f"{numOne} - {numTwo} = {numOne-numTwo}")
        case 'x':
            print(f"{numOne} x {numTwo} = {numOne*numTwo}")
        case '%':
            print(f"{numOne} % {numTwo} = {numOne/numTwo}")
        case _:
            print("Choose your choice")


#Printing a number in reverse order
def number_vice_versa():
    num_str = input("Enter a number: ")

    reversed_str = ""

    for i in num_str:
        reversed_str = i + reversed_str

    print(reversed_str)

        
# number_vice_versa()
# calculator_function() 
# multiplication_table()