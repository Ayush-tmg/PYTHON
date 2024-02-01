"""
4 pillars of OOP:
    Encapsulation
    Inheritance
    Abstraction
    Polymerphism

Encapsulation:
    It is defined as warrping up data into a single unit
    It ensures data integrety 

Abstraction:
    Displaying only necessary infromation

Inheritance:
    Children gains property from the parent
    It creates reusable code    

"""

## File Handling tell and seek

# class Employee:
#     def __init__(self, fn, ln, age):
#         self.first_name = fn
#         self.last_name = ln
#         self.age = age

#     def get_full_name(self):
#         return f"{self.first_name} {self.last_name}"
    
# class Student:
#     def __init__(self, fn, ln, age):
#         self.first_name = fn
#         self.last_name = ln
#         self.age = age

#     def get_full_name(self):
#         return f"{self.first_name} {self.last_name}"
    
# class Teacher:
#     def __init__(self, fn, ln, age):
#         self.first_name = fn
#         self.last_name = ln
#         self.age = age

#     def get_full_name(self):
#         return f"{self.first_name} {self.last_name}"
    
## USING INHERITANCE ##

class Person:
    def __init__(self, fn, ln, age, addr, salary):
        self.first_name = fn
        self.last_name = ln
        self.age = age
        self.address = addr
        self.salary = salary

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_salary(self):
        return f"{self.salary}"

class Student(Person):
    def __init__(self, fn, ln, age, addr, salary):
        super().__init__(fn, ln, age, addr, salary)
        
    
class Teacher(Person):
    def __init__(self, fn, ln, age, addr, salary):
        super().__init__(fn, ln, age, addr, salary)

class Admin(Person):
    def __init__(self, fn, ln, age, addr, salary):
        super().__init__(fn, ln, age, addr, salary)
    
s = Student("Ayush", "Tamang", 19, "Samakhusi", 20000)
print(f"Hello! {s.get_full_name()}. You are {s.age} years old. You live in {s.address} and your fee is {s.get_salary()}.")

t = Teacher("Ayush", "Tamang", 25, "Samakhusi", 300000)
print(f"Hello! {t.get_full_name()}. You are {t.age} years old. You live in {t.address} and your salary is {t.get_salary()}.")

a = Admin("Ayush", "Tamang", 30, "Samakhusi", 500000)
print(f"Hello! {a.get_full_name()}. You are {a.age} years old. You live in {a.address} and your salary is {a.get_salary()}.")