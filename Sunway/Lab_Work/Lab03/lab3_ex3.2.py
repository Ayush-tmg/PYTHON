######## EXERCISE 2 ########

print("-------WELCOME TO OUR BANK-------")

user_name = input("Enter your name: ")
balance = 1000

while True: #student completes while loop
    print("\nChoose 1 for Deposit \nChoose 2 for Withdraw \nChoose 3 for Check Balance \nChoose Q or q to Exit: ")
    choice = input("\nPlease choose transactions: ")
    if choice == "1": 
        deposit_amount = int(input(f"Please! enter the amount {user_name}: "))
        balance += deposit_amount
        
    elif choice == "2":
       withdraw_amount = int(input(f"Please! enter the amount {user_name}: "))
       if withdraw_amount < balance:
           balance -= withdraw_amount
       else:
           print(f"{user_name} it is not possible to withdraw beyond the account balance.")
            
    elif choice == "3":
        print(f"{user_name}, you have a total of £{balance} in your account.")
      
    elif choice == "Q" or choice == "q":
        print("""
              -------------------------------------
              | Thanks for choosing us as your bank |
              | Visit us again!                     |
              -------------------------------------
              """)
        break
    else:
        print("Wrong transaction! Try again.")