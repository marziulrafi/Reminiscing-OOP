fruits = ["apple", "banana", "cherry"]
fruits[1] = "mango"
print(fruits)  # ['apple', 'mango', 'cherry']

fruits2 = ["apple", "banana"]

fruits2.append("cherry")   # add at end
fruits2.insert(1, "mango") # insert at index 1
fruits2.extend(["kiwi", "orange"])  # add multiple items

print(fruits2)  # ['apple', 'mango', 'banana', 'cherry', 'kiwi', 'orange']



fruits2.remove("banana")  # remove by value
popped = fruits2.pop(1)   # remove by index (returns the item)
del fruits2[0]            # delete by index
fruits2.clear()           # remove all items

print(fruits2)  # []


numbers = [10, 20, 30, 40]

print(len(numbers))    # 4
print(max(numbers))    # 40
print(min(numbers))    # 10
print(sum(numbers))    # 100
print(sorted(numbers, reverse=True))  # [40, 30, 20, 10]



fruit = ["apple", "banana", "cherry", "banana"]

print(fruit.index("banana"))   # 1 (first occurrence)
print(fruit.count("banana"))   # 2 (count duplicates)

fruit.sort()                   # sort alphabetically
print(fruit)                   # ['apple', 'banana', 'banana', 'cherry']

fruit.reverse()                # reverse order
print(fruit)                   # ['cherry', 'banana', 'banana', 'apple']



grades = [85, 90, 78]
average = sum(grades) / len(grades)
print("Average :", average)  # Average: 84.3333



# Visit for more (https://docs.python.org/3/tutorial/datastructures.html)