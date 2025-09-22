# Empty tuple
t1 = ()

# Single element tuple (must include a comma!)
t2 = (5,)  

# Multiple elements
t3 = (10, 20, 30)

# Without parentheses (packing)
t4 = 1, 2, 3, 4

print(t1, t2, t3, t4)


t = (10, 20, 30, 40)

print(t[0])   # 10
print(t[-1])  # 40
print(t[1:3]) # (20, 30)  → slicing also works


# Packing
student = ("Messi", 38, "Argentina")

# Unpacking
name, age, country = student
print(name)     # Messi
print(age)      # 38
print(country)  # Argentina



nested = (("a", "b"), (1, 2, 3))
print(nested[0])    # ('a', 'b')
print(nested[1][2]) # 3


# Tuple Operations

t1 = (1, 2, 3)
t2 = (4, 5)

# Concatenation
print(t1 + t2)  # (1, 2, 3, 4, 5)

# Repetition
print(t1 * 3)   # (1, 2, 3, 1, 2, 3, 1, 2, 3)

# Membership
print(2 in t1)  # True
print(10 in t1) # False




#Built-in

t = (5, 1, 5, 3, 5, 7)

print(len(t))     # 6
print(max(t))     # 7
print(min(t))     # 1
print(sum(t))     # 26
print(t.count(5)) # 3 (number of times 5 appears)
print(t.index(3)) # 3 (position of first 3)




# Visit for more (https://www.geeksforgeeks.org/python/python-tuple-methods/)