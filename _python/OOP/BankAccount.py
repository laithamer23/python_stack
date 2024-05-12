class BankAccount:

     def __init__(self, rate, balance):
          self.rate = rate
          self.balance = balance
          
         
     def deposit_amount(self,amount):
          self.balance+=amount
          return self

     def withdraw_amount(self,amount):
          if self.balance>=amount:
               self.balance-=amount
          return self
     
     def yield_insert(self):
          self.balance= self.balance*self.rate+self.balance
          print(self.balance)
          return self
            
Account1 =BankAccount(0.01,100)
Account2  =BankAccount(0.02,200)

user=BankAccount(0.08,300)
user.deposit_amount(100)
user.yield_insert()


Account1.deposit_amount(1000)
print(Account1.balance)
     