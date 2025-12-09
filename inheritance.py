#Added inheritance examples: single-level, multilevel, and multiple inheritance with constructor chaining
class Employee:  #PARENT CLASS
    start_time=10
    end_time=5
    def changeTime(self,new_endtime):
        self.end_time=new_endtime
    
class Teacher(Employee): #child class 
    def __init__(self,subject):
        self.subject=subject

t1=Teacher("english")  #object
t1.changeTime(6)
print(t1.subject,t1.start_time,t1.end_time)

#types of inheritance 1.Single-level 2.multilevel 3.multiple

#MULTILEVEL INHERITANCE
class Department:
    open_time=10
    close_time=8

class Business(Department):
    def __init__(self,profit,loss):
        self.profit=profit
        self.loss=loss

class sales(Business):
    def __init__(self,product,price,profit,loss):#from parent
        super().__init__(profit,loss)  #so that cons can understand previous init method
        self.product=product
        self.price=price

s1=sales("car",20000,1000,200)   
print(s1.product,s1.price,s1.profit,s1.loss)

#multiple inheritance
class Teachers:
    def __init__(self,salary):
        self.salary=salary
class Students:
    def __init__(self,gpa):
        self.gpa=gpa
class TA(Teachers,Students):
    def __init__(self,salary,gpa,name):
        super().__init__(salary)
        Students.__init__(self,gpa)
        self.name=name

ta1=TA(2000,9.4,"pragya")
print(ta1.gpa,ta1.salary,ta1.name)
