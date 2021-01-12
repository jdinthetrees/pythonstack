

class Bank_Account:
    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        if self.balance<0:
            print("Insufficent funds: Charging a $5 fee")
            self.balance -= 5
        return self
    
    def display_account_info(self):
        print(f"Balance: ${self.balance}")

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self

bankAccount1 = Bank_Account(balance = 800)
bankAccount1.deposit(50).deposit(100).deposit(20).display_account_info()


bankAccount2 = Bank_Account(balance = 500)
bankAccount2.deposit(30).deposit(30).withdraw(10).withdraw(30).withdraw(30).withdraw(20).yield_interest().display_account_info()