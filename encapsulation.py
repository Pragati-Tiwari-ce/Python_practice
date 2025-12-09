#Implemented encapsulation using protected and private variables with getter and setter methods.
class Bank:
    def __init__(self,name,balance):
        self.name=name
        self._balance=balance   #protected


acc1=Bank("pragati",20)
print(acc1.name,acc1._balance) # in python its just a convention, not enforcement



class Salary:
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance

    def get_balance(self): #getter func
        return self.__balance
    
    def set_balance(self,newBalance):  #setter func
        self.__balance=newBalance

s1=Salary("amit",20000)
#print(s1.__salary)  #this will give an error (no attr)

#to access private var we use "getters"
print(s1.get_balance())

#to modify private var we use "setters"
s1.set_balance(30000)
print(s1.get_balance())


#however priv var are also not completely restricted
print(s1._Salary__balance)