## INSTANCE METHOD
# Method that access instance variables
# Self should be the first parameter
# Accessed by using self inside the class and by using object name outside of the class

class Student:
    __school_name = "Sunway"
    __school_address = "Maitidevi"
    def __init__(self, fn, ln):
        self.__first_name = fn
        self.__last_name = ln
    def get_full_name(self):
        return f"{self.__first_name} {self.__last_name}"
    def set_first_name(self, new_fn):
        self.__first_name = new_fn
    
## CLASS METHOD
# Method that access static variables
# Cls should be the first parameter
# accessed by using class name inside the class and outside of the class    

    @classmethod # Decorater
    def get_school_name(cls):
        return Student.__school_name
    
    @classmethod
    def set_school_name(cls, new_scname):
        cls.__school_name = new_scname
        
## STATIC METHOD
# Method that does not depend on class or object
# Can be parameterless
# @staticmethod decorator is required
        
    @staticmethod #Decorator
    def add():
        print(1 + 1)
    
    @staticmethod
    def mult(a, b):
        print(a * b)

s = Student('Ram', "Hari")
print(s.get_full_name())
s.set_first_name("Ayush")
print(s.get_full_name())
print(Student.get_school_name())
Student.set_school_name("Bro School")
print(Student.get_school_name())
Student.add()
Student.mult(4, 5)
