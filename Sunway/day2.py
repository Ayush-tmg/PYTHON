# -----> Dictionary <-----

# a = {'ram':50, 'shyam':60, 'hari':80}
# a['rita'] = 25
# print(a.keys)
# print(a.values)

# -------> IF ELSE <-------

##It is also called conditional statement.

## if (condition):
    ## (code)

# first_name = "ram"
# second_name = "hari"

# if first_name == "ram":
#     print("Your name is Ram.")
# elif first_name == "hari":
#     print("Your name is Hari.")
# elif first_name == "sita":
#     print("Your name is Sita.")
# else:
#     print("I am else.")

##if 2 > 3:
    ##pass ==> is used to pass the statement.

# first_name = 'ram'
# last_name = 'hari'

# if first_name == 'ram':
#     if last_name == 'khanal':
#         print('Ram Khanal')
#     elif last_name == 'regmi':
#         print('Ram Regmi')
#     else:
#         print("Ram I do not know your last name.")
# elif first_name == 'hari':
#     print('I am Hari.')
# else:
#     print('I am else.')

## -----> LOGICAL OPERATOR <----

## NOT, AND, OR

# print(True and True and False and not True and not False or not True)

## Assignment
## Take 2 num as input from user
## Enter a operator
## Allowed operation are +, *, -, /, //, %
## +: the sum of 10 and 20 is 30
## -: the difference of 10 and 20 is -10 (ask "Do you want to print absolute value Y/N?" if result is negative)
## if Y: print absolute value else: print negative value
## for division small num should divide bigger num

first_num = int(input("Enter first number: "))
second_num = int(input("Enter second number: "))
op = input("Enter operator from +, *, -, /, // and %: ")

if op == "+":
    print(first_num + second_num)

if op == "-":
    dif = first_num - second_num
    if dif < 0:
        a = input("Do you want to print absolute value Y/N? ").lower
        if a == "y":
            absolute_value = abs(dif)
            print(f"The absolute value of the difference {first_num} and {second_num} is {absolute_value}")
        else:
            pass
    else:
        print(dif)

if op == "*":
    print(first_num * second_num)

if op == "/":
    if first_num > second_num:
        print(first_num / second_num)
    else:
        print(second_num / first_num)

if op == "//":
    if first_num > second_num:
        print(first_num // second_num)
    else:
        print(second_num // first_num)

if op == "%":
    if first_num > second_num:
        print(first_num % second_num)
    else:
        print(second_num % first_num)