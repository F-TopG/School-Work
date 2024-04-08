#Extra points: Alternate Project

import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Can't be zero"
    else:
        return x / y

def calculate_sqrt(x):
    if x < 0:
        return "Can't be less than zero"
    elif x == 0:
        return "Can't be zero"
    else:
        return math.sqrt(x)
    
def calculator():
    print("Welcome to calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square Root")
    choice = input("Please choose the operation (1/2/3/4/5): ")

    if choice in ['1', '2', '3', '4']:
        number1 = int(input("Enter number 1: "))
        number2 = int(input("Enter number 2: "))

        if choice == '1':
            print("Result:", add(number1, number2))
        elif choice == '2':
            print("Result:", subtract(number1, number2))
        elif choice == '3':
            print("Result:", multiply(number1, number2))
        elif choice == '4':
            print("Result:", divide(number1, number2))
        
    elif choice == '5':
        number = int(input("Enter number for square root: "))
        print("Result:", calculate_sqrt(number))

    else:
        print("Invalid choice")

calculator()
