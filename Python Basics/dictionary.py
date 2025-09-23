# Empty dictionary
d1 = {}

# With values
d2 = {"name": "Alice", "age": 25, "city": "Dhaka"}

# Using dict() function
d3 = dict(name="Bob", age=30, city="Chittagong")

# Mixed keys
d4 = {1: "one", "pi": 3.1416, (2, 3): "tuple key"}




person = {"name": "Alice", "age": 25, "city": "Dhaka"}

# Using key
print(person["name"])   # Alice

# Using get() (safe, avoids KeyError)
print(person.get("age"))       # 25
print(person.get("gender"))    # None
print(person.get("gender", "Not found"))  # Not found


# Adding & Updating

person["gender"] = "Female"  # Add new key
person["age"] = 26           # Update existing key
print(person)
# {'name': 'Alice', 'age': 26, 'city': 'Dhaka', 'gender': 'Female'}



# Removing Elements

person = {"name": "Alice", "age": 25, "city": "Dhaka"}

# pop() → remove by key
age = person.pop("age")
print(age)      # 25
print(person)   # {'name': 'Alice', 'city': 'Dhaka'}

# popitem() → remove last inserted pair
item = person.popitem()
print(item)     # ('city', 'Dhaka')

# del → delete specific key
del person["name"]

# clear() → remove everything
person.clear()
print(person)   # {}



# Iterating through Dictionary

student = {"name": "Ahmed", "dept": "CSE", "cgpa": 3.5}

# Keys only
for key in student:
    print(key)

# Values only
for value in student.values():
    print(value)

# Keys + Values
for key, value in student.items():
    print(key, ":", value)




# Nested Dictionaries

students = {
    "101": {"name": "Tanzim", "cgpa": 3.8},
    "102": {"name": "Tahsin", "cgpa": 3.6},
}

print(students["101"]["name"])  # Tanzim