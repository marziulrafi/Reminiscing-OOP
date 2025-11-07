import math

# Decorator definition
def timer(func):
    # Inner function that wraps around the main function
    def inner(n):
        print('Time started')
        func(n)  # Call the actual function
        print('Time ended')
    return inner  # Return the inner function


# Applying the decorator using @
@timer
def get_factorial(n):
    print('Factorial calculation started...')
    result = math.factorial(n)
    print(f'Factorial of {n} is: {result}')


# Example usage
get_factorial(5)
