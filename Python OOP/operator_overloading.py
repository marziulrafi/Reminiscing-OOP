class Book:
    def __init__(self, pages):
        self.pages = pages

    # Overloading the + operator
    def __add__(self, other):
        return self.pages + other.pages

    # Overloading the > operator
    def __gt__(self, other):
        return self.pages > other.pages

    # Overloading the str() method
    def __str__(self):
        return f"Book with {self.pages} pages"

book1 = Book(100)
book2 = Book(200)

print(book1 + book2)     # Calls __add__ → 300
print(book1 > book2)     # Calls __gt__  → False
print(book2 > book1)     # True
print(book1)             # Calls __str__ → Book with 100 pages
