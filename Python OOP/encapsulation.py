"""
Encapsulation means keeping data (attributes) and methods (functions)
together inside a class and controlling access to them.
Python uses conventions for access control:
  - public (normal)
  - _protected (convention)
  - __private (name-mangling)
"""



# Public, Protected, and Private

class Example:
    def __init__(self):
        self.public = "I am public"          # accessible directly
        self._protected = "Use with care"    # internal use (convention)
        self.__private = "Hidden"            # name-mangled, hard to access

obj = Example()
print(obj.public)          # ✅ OK
print(obj._protected)      # ⚠️ Works, but signals “internal use”
# print(obj.__private)     # ❌ AttributeError
print(obj._Example__private)  # ⚠️ Not recommended (uses name-mangling)
print("\n")



# Encapsulation using Getter & Setter

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age    # private attribute

    # Getter
    def get_age(self):
        return self.__age

    # Setter with validation
    def set_age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self.__age = value

p = Person("Rafi", 22)
print("Getter/Setter Example:")
print(p.get_age())   # 22
p.set_age(25)
print(p.get_age())   # 25
# p.__age = -100     # ❌ Won’t change real private variable
print("\n")




# Encapsulation using @property (Recommended)

class Student:
    def __init__(self, name, age):
        self.name = name
        self._age = age   # protected by convention

    # getter
    @property
    def age(self):
        return self._age

    # setter with validation
    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value

    # optional deleter
    @age.deleter
    def age(self):
        del self._age

student = Student("Marziul", 21)
print("Property Example:")
print(student.age)    # uses getter
student.age = 23      # uses setter
print(student.age)
# student.age = -5    # ❌ raises ValueError
print("\n")




# Real-World Example — BankAccount

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance           # protected attribute
        self.__transactions = []          # private list

    # read-only property for balance
    @property
    def balance(self):
        return self._balance

    # deposit method
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self._balance += amount
        self.__record_transaction("deposit", amount)

    # withdraw method
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount
        self.__record_transaction("withdraw", amount)

    # private helper method
    def __record_transaction(self, kind, amount):
        self.__transactions.append((kind, amount))

    # public method to get transaction list safely
    def get_transactions(self):
        return list(self.__transactions)  # returns a copy (read-only)

acct = BankAccount("Mamun", 15000)
acct.deposit(2000)
acct.withdraw(1000)
print("BankAccount Example:")
print("Balance:", acct.balance)
print("Transactions:", acct.get_transactions())
print("\n")




# Private / Protected helper methods

class TextProcessor:
    def __init__(self, text):
        self.text = text

    def process(self):
        # Public method that uses an internal helper
        t = self._normalize(self.text)
        return t.upper()

    def _normalize(self, s):
        # Protected helper method
        return s.strip()

tp = TextProcessor("   hello world   ")
print("Private/Protected Helper Example:")
print(tp.process())  # HELLO WORLD
print("\n")



"""
Public: normal attributes (e.g., self.name)
Protected: single underscore prefix (e.g., self._data)
Private: double underscore prefix (e.g., self.__secret)

Use @property when you want to control access or validation
while keeping natural syntax (obj.attr instead of obj.get_attr()).
"""