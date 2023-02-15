class Bank_account:
    # Constructor
    def __init__(self, interest_rate, balance)
        self.interest_rate = interest_rate
        self.balance = balance
#methods

    def deposit(self, amount):
      self.balance += amount
      return self

    def withdraw(self, amount):
      if (self.balance - amount) > 0:
        self.balance -= amount
      else: 
        print(f'Sorry Your balance: {self.balance}')
        return self

    def display_account_info(self):
       print(self.balance)
       return self 

    def yield_interest(self):
      if self.balance > 0:
        self.balance += (self.balance * self.interest_rate)
      else: 
        print('Your account balance is negative')
      return self
    najwa = Bank_Account(2, 200)
    najwa1 = Bank_Account(5, 300)  
    najwa.deposit(100).deposit(100).deposit(100).withdraw(200).yield_interest().display_account_info()
    najwa1.deposit(200).deposit(200).withdraw(50).withdraw(50).withdraw(20).withdraw(20).yield_interest().display_account_info()
#assignment_users_with_bank_accounts
class User:
    def __init__(self, name, email,):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    # other methods
    @staticmethod
    def display_stats(self):
        print(f"name = {self.name}")
        print(f"email = {self.email}")
        print(f"account={self.account}")
       
        return self
    
    def make_deposit(self, cls,amount,new_deposit):
    	# your code here
      
        cls.deposit = new_deposit


   