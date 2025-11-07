# Decorator that can wrap any function with any number of arguments
def wrapper_function(func):
    def inner(*args, **kwargs):
        print("🚀 Function execution starts")
        result = func(*args, **kwargs)  # Call original function with arguments
        print("🏁 Function execution ends")
        return result  # Return the function's result
    return inner


# Applying decorator
@wrapper_function
def add(a, b):
    print(f"Adding {a} + {b}")
    return a + b


# Example usage
print("Result:", add(3, 5))
