######## EXERCISE 2 ########

import math

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
d = float(input("Enter fourth number: "))
e = float(input("Enter fifth number: "))

sum = a + b + c + d + e
μ = (sum) / 5

a -= μ
b -= μ
c -= μ
d -= μ
e -= μ

a = a ** 2
b = b ** 2
c = c ** 2
d = d ** 2
e = e ** 2

variance = a + b + c + d + e

sd = math.sqrt(variance / 5)

print(f"\nThe Sum is {sum}")
print(f"\nThe Average is {μ}")
print(f"\nThe Standard Deviation is {sd}")