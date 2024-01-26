######## EXERCISE 2 ########

guest = []

def add_guest():
    add_name = input("Enter the name of the guest to add: ")
    guest.append(add_name)
    print(f"{add_name} has been added to the guest list.")

def remove_guest():
    remove_name = input("Enter the name of the guest to remove: ")
    if remove_name in guest:
        guest.remove(remove_name)
        print(f"{remove_name} has been removed from the guest list.")
    else:
        print(f"{remove_name} is not on the guest list.")

def print_guest():
    print_name = sorted(guest)
    print("Guest List (sorted alphabetically ascending): \n", print_name)

print("""Options:
A. Add a guest
R. Remove a guest
P. Print guest list
Q. Quit""")

while True:
    option = input("Enter your choice: ")
    if option == "A":
        add_guest()
    elif option == "R":
        remove_guest()
    elif option == "P":
        print_guest()
    elif option == "Q":
        num = len(guest)
        print(f"Total number of guest: {num} \nGoodbye! See you in the party!")
        break
    else:
        print("Invalid choice. Please choose a valid option (A, R, P or Q).")