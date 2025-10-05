class Bank:
    # Constructor: initializes balance and withdrawal limits
    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 100000

    # Method to check current balance
    def get_balance(self):
        return self.balance

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:  # Only positive deposits allowed
            self.balance += amount

    # Method to withdraw money
    def withdraw(self, amount):
        if amount < self.min_withdraw:
            print(f"Fokira! You cannot withdraw below {self.min_withdraw}.")
        elif amount > self.max_withdraw:
            print(f"Bank fokir hoye jabe! You cannot withdraw more than {self.max_withdraw}.")
        else:
            self.balance -= amount
            print(f"Here is your money: {amount}")
            print(f"Your balance after withdrawal: {self.get_balance()}")



# Create a bank account for BRAC
brac = Bank(15000)
brac.withdraw(25)          # Too low
brac.withdraw(50000000)    # Too high
brac.withdraw(1000)        # Valid withdrawal



# Create another account for DBBL
dbbl = Bank(5000)
dbbl.deposit(2000)         # Deposit 2000
dbbl.deposit(2000)         # Deposit another 2000
print(dbbl.get_balance())  # Check final balance
