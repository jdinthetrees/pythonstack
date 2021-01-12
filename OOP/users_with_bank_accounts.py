class Bank_Account:
    def __init__(self, int_rate=0.02, balance=0):
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




class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = Bank_Account()
    

    
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
        print(self.account.balance)
    
    
    
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        print(f"{self.name} has {self.account.balance} dollars.")
        return self

john = User("John", "johndoe@email.com")
mary = User("Mary", "marydoes@email.com")
paul = User("Paul", "pauldoe@email.com")

# john.make_deposit(300)
# john.make_deposit(100)
# john.make_deposit(100)
# john.display_user_balance()
# john.make_deposit(300).make_deposit(100).make_deposit(100).display_user_balance()

# mary.make_deposit(600)
# mary.make_deposit(200)
# mary.display_user_balance()
# mary.make_deposit(600).make_deposit(200).display_user_balance()

# paul.make_deposit(1000)
# paul.make_withdrawal(100)
# paul.make_withdrawal(100)
# paul.display_user_balance()
# paul.make_deposit(1000).make_withdrawal(100).make_withdrawal(100).display_user_balance()

# john.make_deposit(1000).display_user_balance()

