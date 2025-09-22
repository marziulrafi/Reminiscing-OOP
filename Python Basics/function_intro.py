# for declaring function, we use "def" keyword
def add_two(a, b):
    return a + b
    
result = add_two(5, 4)
print(result)  # 9

def subtract(a, b):
    return a - b


# default parameter c=0
def add_default(a, b, c=0):
    return a + b + c

result = add_default(5, 4)       # output 5 + 4 + 0 = 9
result2 = add_default(5, 4, 3)   # output 5 + 4 + 3 = 12

print(result)
print(result2)



# Using *args when we don’t know how many positional arguments will be passed
def add_many(*args):
    total = 0
    for num in args:
        total += num
    return total

result = add_many(5, 4)          # output 5 + 4 = 9
result2 = add_many(1, 2, 3, 4)   # output 1+2+3+4 = 10

print(result)
print(result2)
