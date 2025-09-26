# Define a class (blueprint)
class Student:
    pass

# Create objects (instances)
s1 = Student()
s2 = Student()

print(type(s1))  # <class '__main__.Student'>
print(isinstance(s1, Student))  # True



class Phone:
    price = 19000
    color = 'Black'
    brand = 'Redmi'


myphone = Phone()

print(myphone.brand) # output: Redmi
print(Phone.price) # 19000