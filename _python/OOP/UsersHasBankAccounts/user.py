from bankAccount import *

class User: 
    def __init__(self,name,bank_account=BankAccount(0,0)) -> None:
        self.name = name 
        self.bank_account = bank_account

    def  make_deposit(self, amount):
        self.bank_account.balance = self.bank_account.balance + amount 
    
    def make_withdrawal(self, amount):
        if(self.bank_account.balance - amount > 0):
            self.bank_account.balance = self.bank_account.balance - amount
        else:
            print(f"Error: {self.name} does not have enough money {self.bank_account.balance}")       

    def display_user_bank_account(self):
        print("User name: ",self.name,"   bank_account: ",self.bank_account.balance)
    
    def transfer_money(self, other, amount):
        self.make_withdrawal(amount)
        other.make_deposit(amount)


user1 = User("user1",BankAccount(0.02, 1500))        
user2 = User("user2")
user3 = User("user3",BankAccount(0.04, 10000))


user1.display_user_bank_account()
user1.make_deposit(200)
user1.make_deposit(300)
user1.make_deposit(50)
user1.make_withdrawal(1000)
user1.display_user_bank_account()


user2.display_user_bank_account()
user2.make_deposit(200)
user2.make_deposit(1500)
user2.make_withdrawal(700)
user2.make_withdrawal(400)
user2.display_user_bank_account()

user3.display_user_bank_account()
user3.make_deposit(500)
user3.make_withdrawal(100)
user3.make_withdrawal(400)
user3.make_withdrawal(1000)
user3.display_user_bank_account()


print("user1 transfer 100 to user3")

user1.transfer_money(user3,100)
user1.display_user_bank_account()
user3.display_user_bank_account()