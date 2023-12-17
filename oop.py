# Incapsilation
    # The properties of binding and hooking a class within a class
    # It makes searching process easier
    # It makes bug finding easier

# Abstraction
    # Displaying only essentual information and hiding unnecessary details
    # It reduces the complexity of the system

# Inheritance
    # The process of inheriting properties and behaviour from a parent class

# Polymorphism
    # Two types of method overwriting and overloading
    # Overloading method is not possible in python
    # It is the exploitation of Inheritance

##main class (super class)
# class Employee:
#     def __init__(self, fn, ln, age):
#         self.first_name = fn 
#         self.last_name = ln
#         self.age = age      
#     def get_name(self):
#         print("I am base class.")
# ##inheritance class
# class FullTimeEmployee(Employee):
#     def __init__(self, fn, ln, age, addr, sal):
#         super().__init__(fn, ln, age) #super class called here
#         self.address = addr
#         self.sal = sal
#     def get_name(self):
#         print("I am Full Time.")
        
# f = FullTimeEmployee('Ayush', 'Tamang', '18', 'Samakhusi', '10000')
# f.get_name()

