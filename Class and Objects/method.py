class Student:
    # Attribute
    school = "ABC University"

    # Method
    def say_hello(self):
        print("Hello, I am a student of", self.school)


s1 = Student()
s1.say_hello()



# Self keyword

class Student2:
    def greet(self, name):
        print(f"Hello {name}, I am inside {self}")

s2 = Student2()
s2.greet("Rafi")  # self = s2





class Phone:
    price = 19000
    color = 'blue'
    brand = 'samsung'

    # Methods must be inside the class and indented properly
    def call(self):
        print('Calling one person')

    def send_message(self, message):
        return f"Sending message : {message}"


# Create an object
myphone = Phone()

# Call methods
myphone.call()  
print(myphone.send_message("Hello World"))
