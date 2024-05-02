class BankAccount:

     def __init__(self, rate=0.01, balance=0):
          self.rate = rate
          self.balance = balance
          return self
         
     def deposit_amount(self,amount):
          self.balance+=amount
          return self

     def withdraw_amount(self,amount):
          if self.balance>=amount:
               self.balance-=amount
          return self
     
     def yield_insert(self,amount):
          print(self.balance)
          return self

            


     