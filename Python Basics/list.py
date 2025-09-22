"""
1. A list is a built-in Python data structure that stores an ordered, mutable collection of items.
2. Items can be of any type (integers, strings, floats, booleans, even other lists).
3. Lists are written with square brackets []. 
"""


numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]
mixed = [1, "hello", 3.14, True]



print(fruits[0])   # apple (first element)
print(fruits[1])   # banana
print(fruits[-1])  # cherry (last element)
print(fruits[-2])  # banana
print(fruits[-3])  # apple



# Slicing

fruits = ["apple", "banana", "cherry", "mango"]

print(fruits[1:3])   # ['banana', 'cherry'] (from index 1 to 2)
print(fruits[:2])    # ['apple', 'banana']
print(fruits[2:])    # ['cherry', 'mango']
print(fruits[::-1])  # ['mango', 'cherry', 'banana', 'apple'] (reverse list)


# [start : end : step]

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(numbers[0:8:2]) # [1, 3, 5, 7]

numbers2 = [1, 2, 3, 4, 5, 6, 7, 8]
print(numbers2[:5]) #[1, 2, 3, 4, 5]

numbers3 = [1, 2, 3, 4, 5, 6, 7, 8]
print(numbers3[3:]) # [4, 5, 6, 7, 8]


nums = [10, 20, 30, 40, 50]

print(nums[-3:])    # [30, 40, 50] → last 3 elements
print(nums[:-2])    # [10, 20, 30] → everything except last 2




# Visit for more (https://docs.python.org/3/tutorial/datastructures.html)