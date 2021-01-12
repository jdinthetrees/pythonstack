
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    
    
    
    
    
    
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    
    
    
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"{self.name} has {self.account_balance} dollars.")
        return self

john = User("John", "johndoe@email.com")
mary = User("Mary", "marydoes@email.com")
paul = User("Paul", "pauldoe@email.com")

# john.make_deposit(300)
# john.make_deposit(100)
# john.make_deposit(100)
# john.display_user_balance()
john.make_deposit(300).make_deposit(100).make_deposit(100).display_user_balance()

# mary.make_deposit(600)
# mary.make_deposit(200)
# mary.display_user_balance()
mary.make_deposit(600).make_deposit(200).display_user_balance()

# paul.make_deposit(1000)
# paul.make_withdrawal(100)
# paul.make_withdrawal(100)
# paul.display_user_balance()
paul.make_deposit(1000).make_withdrawal(100).make_withdrawal(100).display_user_balance()

