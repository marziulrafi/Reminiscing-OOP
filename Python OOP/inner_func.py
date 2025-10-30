# Outer function
def double_decker():
    print('Starting the double_decker')

    # Inner function (defined inside outer)
    def inner_fun():
        print('Inside the inner function')
        return 3000  # returning a value from inner

    return inner_fun  # returning the function itself (not calling it)



# Example usage:
# Step 1: double_decker() returns the inner function
# Step 2: Then we call that inner function using another pair of parentheses ()
result = double_decker()()  # double call
print(result)  # Output: 3000