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




# Visit for more (https://docs.python.org/3/tutorial/datastructures.html)