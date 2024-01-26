##### OOP #####

## Class: Blueprint of an object
## It defines how an object should look like
## Object: An instantiation of class (Perfect Example)

class Student:
    def __init__(self, fn, ln, a): # Dunder method or magic method
        self.firstname = fn
        self.lastname = ln
        self.age = a
        print(f"Hello! {self.firstname} {self.lastname}. You are {self.age} years old.")

s = Student("Ayush", "Tamang", 19) # "Student" is object while "s" is reference variable
a = Student(fn = "Sam", ln = "Hari", a = 20)