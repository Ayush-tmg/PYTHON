######## EXERCISE 2 ########

n = 0

while n < 5:
    password = input("Enter password: ")
    if password == "test100":
        print("You are logged in.")
        break
    else:
        n += 1
        print("Incorrect! password. Please try again.")

    if n == 5:
        print("You've reached maximum login attempts.")        
        break