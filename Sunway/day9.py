##### LAMBDA FUNCTION #####

# A small anonymous function
# This function has no name

# Normal function:
# def is_even(n):
#   return True if n % 2 -- 0 else Fasle

# Lambda function:
# a = lambda n : True if n % 2 == 0 else False
# print(a(5))

## Write a lambda functino that takes 2 num and return the summation of those 2 function

# s = lambda a, b : a + b
# num1 = int(input("Enter first num: "))
# num2 = int(input("Enter second num: "))
# print(f"The sum of {num1} and {num2} is {s(num1, num2)}")

## Write a lambda function that takes a num and prints whether the num is odd or even

odd_even = lambda n : True if n % 2 == 0 else False
n = int(input("Enter a num: "))
if odd_even(n) == True:
    print(f"The given number {n} is even.")
else:
    print(f"The given number {n} is odd.")