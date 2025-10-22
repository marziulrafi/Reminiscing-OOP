"""
Demonstrates use of @staticmethod — a method that belongs to the class
but does not receive either 'self' or 'cls'. Useful for utility functions
logically related to the class.

"""

class MathUtils:
    # Static method example: a small utility that does not use class or instance state
    @staticmethod
    def add(a, b):
        """Return sum of a and b. Can be called on the class or an instance."""
        return a + b

    @staticmethod
    def is_even(n):
        """Return True if n is even, False otherwise."""
        return n % 2 == 0


# Usage
print("MathUtils.add(2,3):", MathUtils.add(2, 3))
mu = MathUtils()
print("mu.add(10,20):", mu.add(10, 20))  # also callable via instance
print("MathUtils.is_even(4):", MathUtils.is_even(4))
print("MathUtils.is_even(5):", MathUtils.is_even(5))




# When to use staticmethod?
# - When a function is logically grouped with a class but doesn't need access
#   to instance (self) or class (cls) data.
# Example: small converters, validators, factory helpers that don't need class state.