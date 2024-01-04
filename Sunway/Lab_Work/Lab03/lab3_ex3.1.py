######## EXERCISE 1 ########

import math

def find_prime(n):
    if n == 1:
        return True
    if n == 2:
        return False
    
    s = int(math.sqrt(n))

    for i in range(2, s + 1):
        if n % i == 0:
            return False
    return True

def find_divisor(n):
    divisors = []

    for i in range(1, n + 1):
        if n % i  == 0:
            divisors.append(i)
    return divisors

num = int(input("Enter a whole number: "))  
result = find_prime(num)

if result == True:
    print(f"The number {num} is prime.")
else:
    divisor = find_divisor(num)
    print(f"The divisor of {num} is {divisor}")