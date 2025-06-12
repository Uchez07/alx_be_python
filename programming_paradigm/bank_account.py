class BankAccount:
    def __init__(self, initial_balance=100.0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            

    def withdraw(self, amount):
        self.amount = account_balance

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance}")
