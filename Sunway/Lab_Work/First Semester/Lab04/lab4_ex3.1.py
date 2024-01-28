######## EXERCISE 1 ########

def add(num1, num2):
    return f"{num1} added by {num2} is {num1 + num2}"

def subtract (num1, num2):
    return f"{num1} subtracted by {num2} is {num1 - num2}"

def multiply(num1, num2):
    return f"{num1} multiplied by {num2} is {num1 * num2}"

def divide (num1, num2):
    return f"{num1} divided by {num2} is {num1 / num2}"

def calculator(num1, num2, operator):
    if operator == "+":
        print(add(num1, num2))
    if operator == "-":
        print(subtract(num1, num2))
    if operator == "*":
        print(multiply(num1, num2))
    if operator == "/":
        print(divide(num1, num2))

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
op = input("Enter an operator: ")

if op not in ['+', '-', '*', '/']:
    print("Invalid operator.")
else:
    calculator(num1, num2, op)