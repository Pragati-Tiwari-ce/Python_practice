# Encapsulation example: Private attributes with validation using getters and setters.
class Student:
    def __init__(self,name,roll_no,marks):
        self.__name=None
        self.__roll_no=None
        self.__marks=None
        self.set_name(name)
        self.set_roll_no(roll_no)
        self.set_marks(marks)

    def get_name(self):
        return self.__name
        
    def get_roll_no(self):
        return self.__roll_no
    
    def get_marks(self):
        return self.__marks
    
    def set_name(self,name):
        if name.strip()!="":
            self.__name=name
        else:
            print("enter valid name")
    
    def set_roll_no(self,roll_no):
        if roll_no<1 or roll_no>100:
            print("enter between 1 to 100")
        else:
            self.__roll_no=roll_no
    
    def set_marks(self,marks):
        if marks>=0:
            self.__marks=marks
        else:
            print("marks cannot be negative")

a=Student("pragati",25,100)
print(a.get_name(),a.get_roll_no(),a.get_marks())