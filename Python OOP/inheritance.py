"""
Why use Inheritance?

1. Code Reusability - Avoid writing the same code multiple times.
2. Organized Code - Logical relationship between classes.
3. Extensibility - You can easily add new features by extending old classes.

"""




# Base class (Parent)
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn. Remaining balance: {self.balance}")


# Derived class (Child)
class SavingsAccount(BankAccount):
    def __init__(self, owner, balance, interest_rate):
        # Use super() to call parent constructor
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print(f"Interest added: {interest}. New balance: {self.balance}")


# Example usage
account1 = SavingsAccount("Marziul", 5000, 5)
account1.deposit(2000)        # Inherited from BankAccount
account1.add_interest()       # Defined in SavingsAccount
account1.withdraw(1000)       # Inherited from BankAccount
