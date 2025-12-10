#POLYMORPHISM- method overriding
class Employee:
    def get_desgn(self):
        print("employee")

class Teacher(Employee):
    def get_desgn(self):
        print("teacher")
        Employee.get_desgn(self)

t1=Teacher()
t1.get_desgn()    

#POLYMORPHISM- Duck Typing
class Cow:
    def make_sound(self):
        print("moo")

class Lion:
    def make_sound(self):
        print("roar")

c=Cow()
L=Lion()
L.make_sound()
c.make_sound()
        
