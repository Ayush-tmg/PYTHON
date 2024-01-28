class Student:
    school_name = "Sunway"
    school_address = "Maitidevi"
    def __init__(self, fn, ln):
        self.__first_name = fn
        self.__last_name = ln
    def get_full_name(self):
        return f"{self.__first_name} {self.__last_name}"

s = Student('Ram', "Hari")
print(s.get_full_name())