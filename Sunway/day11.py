##### OOP #####

## Class: Blueprint of an object
## It defines how an object should look like
## Object: An instantiation of class (Perfect Example)

class Student:
    def __init__(self, fn, ln, a): # Dunder method or magic method
        self.firstname = "Ayush"
        self.lastname = "Tamang"
        self.age = 19
        print("Hello")

s = Student() # "Student" is object while "s" is reference variable
a = Student()