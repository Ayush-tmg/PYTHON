# def find_max(l):
#     return max(l)

# print(find_max([1,2,3,4,5]))

#Write a function that takes list as an arguement and rounds up

# def find_avg(l):
#     # sum = 0
#     # for item in l:
#     #     sum = sum + item
#     # avg = sum / len(l)

#     return round(sum(l) / len(l), 2)
#     # return round(avg, 2)

# print(find_avg([1,2,3,4,5]))

#Write a function that takes a string and count the number of consonents in the string and return it.

# def count_consonants(string):
#     consonants = "bcdfghjklmnpqrstvwxyz"
#     count = 0

#     for char in string:
#         if char.lower() in consonants:
#             count += 1

#     return count


# str = input("Enter any words to find the consonants: ")
# result = count_consonants(str)
# print(f"The number of consonants in '{str}' is {result}")

#### OR ####

# def count_consonants(s):
#     count = 0
#     for item in s:
#         if item.lower() not in "aeiou":
#             count += 1
#     return count

# str = input("Enter any words to find the consonants: ")
# result = count_consonants(str)
# print(f"The number of consonants in '{str}' is {result}")

#Take a email and check whether that email address is a gmail address or not.

# def check_email(e):
#     check = "@gmail.com"
#     if check in e.lower():
#         print(f"The given email address {e} is a gmail address.")
#     else:
#         print(f"The given email address {e} is not a gmail address.")

# email = input("Enter your email: ")
# check_email(email)

#Write a function that takes email and returns wether that email belongs to edu.np or not.
#Write a function that takes multiple number of integers and separate the number into two different list even and odd.
#Write a funtion that takes a string and checks wether that string is a palindrone or not.
