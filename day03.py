#Program to Calculate the Square and Cube of a Number:
def square_cube():
    a = int(input("Enter a number: "))
    print("Square: " + str(a**2) + " , " + "Cube: " + str(a**3))

def area_circle_triangle():
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    radius = float(input("Enter the radius for the circle: "))

    print("Area of triangle: " + str(0.5*base*height) + "cm^2" + "\nArea of circle: " + str(2*3.14*radius) + "cm^2")

def quotient_divisor():
    a = int(input("Input a number: "))
    b = int(input("Input another number: "))

    print("Quotient: " + str(a/b) + "\nRemainder: " + str(a%b))

