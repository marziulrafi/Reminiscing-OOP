"""
Demonstrates use of @classmethod — a method that receives the class (cls)
and can access/modify class state. Frequently used for alternate constructors
or operations that affect the class as a whole.
"""

class User:
    # class attribute to track number of users
    user_count = 0

    def __init__(self, username, role="member"):
        self.username = username
        self.role = role
        User.user_count += 1

    # class method as an alternate constructor
    @classmethod
    def from_string(cls, data_string):
        """Create a User from a string like 'username:role'"""
        username, role = data_string.split(":")
        # cls() calls the constructor of the class on which the method was called
        return cls(username, role)

    # class method to get class-level info
    @classmethod
    def get_user_count(cls):
        return cls.user_count

    def __repr__(self):
        return f"User(username={self.username!r}, role={self.role!r})"


# Usage
u1 = User("alice")
u2 = User.from_string("bob:admin")  # alternate constructor
print(u1)
print(u2)
print("Total users:", User.get_user_count())



"""
classmethod vs staticmethod:
- classmethod receives the class (cls) and can modify class state or return instances.
- staticmethod receives neither self nor cls — it's just a regular function namespaced
  inside the class.
"""