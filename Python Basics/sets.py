# Empty set (⚠️ not {} because {} = empty dictionary)
s1 = set()

# Set with values
s2 = {1, 2, 3, 4}

# Duplicate values automatically removed
s3 = {1, 2, 2, 3, 3, 3}
print(s3)  # {1, 2, 3}

# Mixed data types allowed
s4 = {10, "hello", 3.14, True}



s = {1, 2, 3}

# Add single element
s.add(4)    
print(s)  # {1, 2, 3, 4}

# Add multiple elements
s.update([5, 6, 7])
print(s)  # {1, 2, 3, 4, 5, 6, 7}

# Remove specific element (error if not found)
s.remove(3)
print(s)  # {1, 2, 4, 5, 6, 7}

# Discard element (no error if not found)
s.discard(10)  # no error
print(s)

# Pop → removes a random element
popped = s.pop()
print("Removed:", popped, "Remaining:", s)

# Clear all elements
s.clear()
print(s)  # set()





# Set Operations

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}


# Union (all unique elements from both sets)
print(a | b)         # {1, 2, 3, 4, 5, 6}
print(a.union(b))    # same

# Intersection (common elements)
print(a & b)         # {3, 4}
print(a.intersection(b))

# Difference (elements in a but not in b)
print(a - b)         # {1, 2}
print(a.difference(b))

# Symmetric Difference (elements in either set, but not both)
print(a ^ b)         # {1, 2, 5, 6}
print(a.symmetric_difference(b))





# Set Membership

fruits = {"apple", "banana", "mango"}

print("apple" in fruits)   # True
print("grape" in fruits)   # False



# Frozen Sets

fs = frozenset([1, 2, 3, 4])
print(fs)  # frozenset({1, 2, 3, 4})

# fs.add(5) ❌ (error, because frozen)




# Removing duplicates from a list
nums = [1, 2, 2, 3, 3, 4, 5, 5]
unique_nums = list(set(nums))
print(unique_nums)  # [1, 2, 3, 4, 5]

# Checking common skills
skills_a = {"Python", "SQL", "C++"}
skills_b = {"Java", "Python", "HTML"}

print(skills_a & skills_b)  # {'Python'} → common skill



# Visit for more (https://www.freecodecamp.org/news/python-set-how-to-create-sets-in-python/)