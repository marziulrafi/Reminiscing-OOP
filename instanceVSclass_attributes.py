# Use class attributes for values that are the same for everyone.
# Use instance attributes for values unique to each object.



class Student:
    school = "ABC University"  # class attribute

    def __init__(self, name):
        self.name = name       # instance attribute

s1 = Student("Marziul")
s2 = Student("Rafi")

print(s1.name)   # Marziul
print(s2.name)   # Rafi
print(s1.school) # ABC University
print(s2.school) # ABC University






# cart as Class Attribute


class Shop:
    cart = []   # class attribute (shared by all objects)

    def __init__(self, buyer):
        self.buyer = buyer

    def add_to_cart(self, product):
        self.cart.append(product)  # modifies the shared class list


mamun = Shop("Mamun")
mamun.add_to_cart("Shoes")
mamun.add_to_cart("Shirt")
print("After mamun added:", mamun.cart) # After mamun added: ['Shoes', 'Shirt']

mahmud = Shop("Mahmud")
mahmud.add_to_cart('Cap')
mahmud.add_to_cart("Watch")
print("After mahmud added:", mahmud.cart) # After mahmud added: ['Shoes', 'Shirt', 'Cap', 'Watch']


# Problem: Both buyers are using the same cart. Not realistic.




# cart as Instance Attribute


class Shop:
    def __init__(self, buyer):
        self.buyer = buyer
        self.cart = []   # instance attribute (unique per object)

    def add_to_cart(self, product):
        self.cart.append(product)  # modifies this buyer’s own list


mamun = Shop("Mamun")
mamun.add_to_cart("Shoes")
mamun.add_to_cart("Shirt")
print("After mamun added:", mamun.cart) # After mamun added: ['Shoes', 'Shirt']

mahmud = Shop("Mahmud")
mahmud.add_to_cart('Cap')
mahmud.add_to_cart("Watch")
print("After mahmud added:", mahmud.cart) # After mahmud added: ['Cap', 'Watch']
