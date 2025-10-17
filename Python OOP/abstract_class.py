from abc import ABC, abstractmethod


# 1. Abstract Class Example


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        return "Woof!"


class Cat(Animal):
    def make_sound(self):
        return "Meow!"


# d = Animal()  # ❌ Error: cannot instantiate abstract class
dog = Dog()
cat = Cat()

print(dog.make_sound())
print(cat.make_sound())
print("\n")





# 2. Abstract Class + Concrete Method


class Vehicle(ABC):
    def start_engine(self):
        print("Engine started...")

    @abstractmethod
    def drive(self):
        pass


class Car(Vehicle):
    def drive(self):
        print("Car is driving on the road!")


class Boat(Vehicle):
    def drive(self):
        print("Boat is sailing in water!")


car = Car()
boat = Boat()

car.start_engine()
car.drive()
boat.start_engine()
boat.drive()
print("\n")




# 3. Real-world Example: Payment System


class Payment(ABC):
    @abstractmethod
    def make_payment(self, amount):
        pass

    def transaction_summary(self, amount):
        print(f"Transaction completed for amount: {amount}")


class CreditCardPayment(Payment):
    def make_payment(self, amount):
        print(f"Processing Credit Card payment of ${amount}")
        self.transaction_summary(amount)


class PayPalPayment(Payment):
    def make_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}")
        self.transaction_summary(amount)


credit = CreditCardPayment()
paypal = PayPalPayment()

credit.make_payment(500)
paypal.make_payment(200)