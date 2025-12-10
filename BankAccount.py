'''Create a class with attributes account_number, owner_name, and balance.
Add methods to deposit, withdraw, and check balance.
'''
class BankAccount:
    def __init__(self,acc_number,owner_name,balance=0):
      self.acc_number=acc_number
      self.owner_name=owner_name
      self.balance=balance
    
    def deposit(self,value):
       self.balance+=value
       print(f"your balance after deposit is: {self.balance}")
    
    def withdraw(self,value):
        if value>self.balance:
          print("insufficient balance")
        else:
            self.balance-=value
            print(f"your remaining balance is :{self.balance}")
    
    def check_balance(self):
       print(f"Your account balance is :{self.balance}")

n=int(input("enter your account number"))
b=input("enter your name")
b1=BankAccount(n,b)
b1.deposit(4000)
b1.withdraw(2000)
b1.check_balance()
