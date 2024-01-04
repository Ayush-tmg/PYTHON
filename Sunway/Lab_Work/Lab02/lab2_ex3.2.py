######## EXERCISE 2 ########

import math

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

ab = a + b
bc = b + c
ca = c + a

if a != bc and not (a > bc):
    if b != ca and not (b > ca):
        if c != ab and not (c > ab):
            p = a + b + c
            s = (a + b + c) / 2
            h = math.sqrt(s * ((s - a) * (s - b) * (s - c)))
            print(f"{a}, {b}, and {c} can form the sides of a triangle.")
            print(f"The Perimeter of the formed triangle is {p}")
            print(f"The surface using Heron's formula is {h}")
        else:
            print(f"{a}, {b}, and {c} can't form the sides of a triangle.")
    else:
        print(f"{a}, {b}, and {c} can't form the sides of a triangle.")
else:
    print(f"{a}, {b}, and {c} can't form the sides of a triangle.")