#Application Using Functions

def greet():
    print("Hello! Welcome to the Arithmetic Operations Program.")

def add_numbers(a, b):
    result = a + b
    return result

def multiply_numbers(*numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def power_of_numbers(**kwargs):
    if 'base' in kwargs and 'exponent' in kwargs:
        result = kwargs['base'] ** kwargs['exponent']
        return result
    else:
        return "Please provide both base and exponent."

def divide_numbers(dividend, divisor=1):
    if divisor == 0:
        return "Cannot divide by zero."
    result = dividend / divisor
    return result

greet()

sum_result = add_numbers(5, 3)
print(f"Addition Result: {sum_result}")

product_result = multiply_numbers(2, 3, 4)
print(f"Multiplication Result: {product_result}")

power_result = power_of_numbers(base=2, exponent=3)
print(f"Power Result: {power_result}")

division_result = divide_numbers(10)
print(f"Division Result: {division_result}")
