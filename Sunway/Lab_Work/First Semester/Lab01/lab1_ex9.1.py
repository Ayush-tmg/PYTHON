######## EXERCISE 1 ########

import math

A = float(input("Enter the coefficient A: "))

B = float(input("Enter the coefficient B: "))

C = float(input("Enter the coefficient C: "))

print("\nThe coefficients of the equation are:")
print("Coefficient A = ", A)
print("Coefficient B = ", B)
print("Coefficient C = ", C)

d = math.sqrt(B * B - 4 * A * C)

root1 = (- B + d ) / ( 2 * A)  
root2 = (- B - d ) / ( 2 * A)

print("\nThe roots of the equation:")
print("Root #1 = ", round(root1,2)) 
print("Root #2 = ", round(root2,2))

