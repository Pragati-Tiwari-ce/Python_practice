#Creating class, object, and use of __init__ method
class Student:
    def __init__(self,name):
        self.name=name      
student1=Student("pragati")
print(student1.name)

#constructor
class ltce_student:
    def __init__(self,name,course,age,cgpa):
        self.name=name
        self.course=course
        self.age=age
        self.cgpa=cgpa

    def get_cgpa(self):  #method
        return self.cgpa
    
stu1=ltce_student("pragati","be",20,9.5)
print(f"name = {stu1.name}\ncourse= {stu1.course}\nage= {stu1.age}\ncgpa={stu1.get_cgpa()}")

#types of constructors- default and parameterized

#attributes-class attr and instance attr
class office:
    office_name="ABC cooperation" # class attr
    def __init__(self,name,age,profession):
        self.name=name       #instance attr
        self.age=age
        self.profession=profession
emp1=office("pragati",20,"engineer")
print(emp1.name) 
print(office.office_name) 

#methods- instance,class and static
#----static methods---
class laptop:
    storage="ssd"
    @staticmethod
    def calc_discount(price,discount):
        final_price=price-(discount*price/100)
        print(final_price)
l1=laptop()
l1.calc_discount(200,2)

       