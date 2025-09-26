"""
1. A special method that runs automatically when object is created.
2. Used to initialize attributes.
"""

class Student:
    def __init__(self, name, age):   # constructor
        self.name = name   # instance attribute
        self.age = age

    def introduce(self):
        print(f"My name is {self.name}, and I am {self.age} years old.")

s1 = Student("Marziul", 22)  # __init__ is called here
s2 = Student("Rafi", 24)

s1.introduce()
s2.introduce()




class Phone:
   def __init__(self, brand, price):
      self.brand = brand
      self.price = price
      
def call(self):
    pass         # pass is a placeholder statement. It means “do nothing here”

 

samsung = Phone("Samsung", "90000")
iphone = Phone('Apple', '150000')

print(samsung.brand) # Samsung
print(iphone.brand) # Apple
