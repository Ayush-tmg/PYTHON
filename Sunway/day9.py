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

# odd_even = lambda n : True if n % 2 == 0 else False
# n = int(input("Enter a num: "))
# if odd_even(n) == True:
#     print(f"The given number {n} is even.")
# else:
#     print(f"The given number {n} is odd.")

# OR
    
# odd_even = lambda n : print(f"The given number {n} is even.") if n % 2 == 0 else print(f"The given number {n} is odd.")
# n = int(input("Enter a num: "))
# odd_even(n)

## Write a lambda function that takes a string and returns the last letter of that string.

# a = lambda x : x[-1]
# x = input("Enter a word: ")
# print(a(x))

## Write a lambda function that takes a string and returns the reberse of that string.

# a = lambda x : x[::-1]
# x = input("Enter a word: ")
# print(a(x))

## Write a lambda function that takes a string and checks whether that string is a palindrome or not.

# a = lambda x : print(f"{x} is a palindrome.") if x in x[::-1] else print(f"{x} is not a palindrome.")
# x = input("Enter a word: ").lower()
# a(x)

## Write a lambda function that takes a string and checks whether letter "u" is present in that string or not disregarding the case sensitivity.

a = lambda x : print(f"The letter u is present in {x}") if "u" in x else print(f"The letter u is not present in {x}")
x = input("Enter a word: ").lower()
a(x)

## MAke a keyword detector in python ##
## like True and False
# import keyword module use it or not
# check whether the input keyword is pyhton keyword or not

### Matplotlib in python study
# graph and pychart
## ENter your monthly rent(expenditure on monthly rent, on lunch, fuel/Travel and grocerie)
# Represent it in pie chart in prercentage upto round(2) place like 12.12
# pirchart must be saved on laptop
# title of piechart should be monthly expenditure
# file must be saved as january_expenditure.png or any other extensions
# monthly expenditure on jan/feb/mar
