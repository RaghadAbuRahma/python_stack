
class BankAccount:
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount 
        return self
        
    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(self.balance)
        return self

    def yield_interest(self):
        if(self.balance < 0) :
            print("Error")
        else: self.balance +=(self.balance * self.int_rate)
        return self

	
		


account1 = BankAccount(0.02, 1500)
account2 = BankAccount(0.04, 10000)

account1.deposit(100).deposit(200).deposit(300).withdraw(100).yield_interest().display_account_info()

account2.deposit(40). deposit(50).withdraw(20).withdraw(30).withdraw(40).withdraw(50).yield_interest().display_account_info()
