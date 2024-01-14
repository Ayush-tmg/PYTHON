##### LIST COMPREHENSION #####

# without list comprehension
# a = list(range(20))
# even = []
# for item in a:
#     if item % 2 == 0:
#         even.append(item)
# print(even)

# with list comprehension
# a = list(range(20))
# even = [item for item in a if item % 2 == 0]
# print(even)

# names = ["ram", "shyam", "hari", "rita", "gita"]
# new_names = []
# for item in names:
#     new_names.append(item.upper())
# print(new_names)

# names = ["ram", "shyam", "hari", "rita", "gita"]
# new_names = [item.upper() for item in names]
# print(new_names)

import keyword
keyword_list = keyword.kwlist
user_choice = input("Enter a word: ")
if user_choice in keyword_list:
    print(f"{user_choice} is a keyword.")