class User: 
    def __init__(self,name,balance=0):
        self.name = name 
        self.balance = balance
    

    def  make_deposit(self, amount):
        self.balance = self.balance + amount 
        return self
    
    def make_withdrawal(self, amount):
        if(self.balance - amount > 0):
            self.balance = self.balance - amount
        else:
            print(f"Error: {self.name} does not have enough money {self.balance}")  
        return self     

    def display_user_balance(self):
        print("User name: ",self.name,"   Balance: ",self.balance)
        return self
    
    def transfer_money(self, other, amount):
        self.make_withdrawal(amount)
        other.make_deposit(amount)
        return self

user1 = User("user1",1000)        
user2 = User("user2")
user3 = User("user3",200)



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


