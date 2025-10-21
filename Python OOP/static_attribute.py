class Product:
    # class attribute (shared by all instances)
    tax_rate = 0.05  # 5% VAT (example) — this is shared among all products

    def __init__(self, name, price):
        # instance attributes (unique to each object)
        self.name = name
        self.price = price

    def price_with_tax(self):
        # uses the class attribute tax_rate to compute final price
        return self.price * (1 + Product.tax_rate)


# Usage examples
p1 = Product("Pen", 10.0)
p2 = Product("Notebook", 50.0)

# Both instances see the same tax_rate (class attribute)
print("Initial tax rate (class attribute):", Product.tax_rate)
print(p1.name, "price with tax:", p1.price_with_tax())
print(p2.name, "price with tax:", p2.price_with_tax())

# Change the class attribute; this affects all instances that rely on it
Product.tax_rate = 0.10  # change to 10%
print("\nAfter updating Product.tax_rate = 0.10")
print(p1.name, "price with tax:", p1.price_with_tax())
print(p2.name, "price with tax:", p2.price_with_tax())

# If you assign tax_rate on an instance, you create an instance attribute
p1.tax_rate = 0.20  # only p1 now has its own tax_rate attribute
print("\nAfter setting p1.tax_rate = 0.20 (instance attribute)")
print("p1.tax_rate (instance) =>", p1.tax_rate)
print("p2.tax_rate (from class) =>", p2.tax_rate)
print("Product.tax_rate (class) =>", Product.tax_rate)

# Note: Access lookup order: instance attribute -> class attribute