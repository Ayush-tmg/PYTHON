######## EXERCISE 2 ########

def menu(): 
    print("""
v. view contacts
a. add contact 
d. delete contact 
q. quit""")
    choice = input("Enter choice (v/a/d/q- to quit): ").lower()
    return choice

def view_contacts(contacts):
    hyphen = '-'
    print(f'\n{hyphen * 6} View_Contacts {hyphen * 6}')
    for i, (name, number) in enumerate(contacts):
        print(f"{i + 1 : > 5}. {name: >4} {number: >4}", end =' \n')

def add_contacts(contacts): 
    name = input("Enter Contact Name : ")
    number = int(input("Enter Contact Number: "))
    contacts.append((name, number))
    print(f'{name} - {number} has been added to the contact list ')
    return contacts

def delete_contacts(contacts): 
    id_val = int(input("Enter the ID of the contact you want to delete: "))
    if id_val < 0 or id_val > len(contacts):
        print("Invalid ID!! please enter a valid one.")
        return contacts
    else:
        name, number = contacts.pop(id_val-1)
        print(f'Deleting: Record {id_val} {name} {number}')
        return contacts

contacts=[("Ayush", "98123"), ("Ishan", "98453")]

def main(contacts):
    hyphen = '-'
    while True:
        op = menu()
        if op == 'v':
            view_contacts(contacts)
        elif op == 'a':
            add_contacts(contacts)
        elif op == 'd':
            delete_contacts(contacts)
        elif op == 'q':
            print(f'\n{hyphen*6}Goodbye{hyphen*6}')
            break
        else:
            print(f'\n{hyphen*6}Invalid choice {hyphen*6}')

if __name__ == "__main__":
    main(contacts)