class Shopping:
    def __init__(self, name):
        # Each customer has a name and their own shopping cart (a list)
        self.name = name
        self.cart = []

    def add_to_cart(self, item, price, quantity):
        # Add a product (dictionary) to the customer's cart
        product = {'item': item, 'price': price, 'quantity': quantity}
        self.cart.append(product)

    # Homework: remove an item from the cart
    def remove_item(self, item):
        # Loop through the cart and find the matching item
        for product in self.cart:
            if product['item'] == item:
                self.cart.remove(product)
                print(f"{item} removed from cart.")
                return
        print(f"{item} not found in cart.")  # If item doesn’t exist

    def checkout(self, amount):
        # Calculate the total price of items in the cart
        total = 0
        for item in self.cart:
            total += item['price'] * item['quantity']

        print('Total price:', total)

        # Check if the given amount is enough
        if amount < total:
            print(f'Please provide {total - amount} more.')
        else:
            extra = amount - total
            print(f'Here are your items and your extra money: {extra}')


# Create a customer named "Alan Swapon"
swapan = Shopping('Alan Swapon')

# Add items to cart
swapan.add_to_cart('alu', 50, 6)   # 50 * 6 = 300
swapan.add_to_cart('dim', 12, 24)  # 12 * 24 = 288
swapan.add_to_cart('rice', 50, 5)  # 50 * 5 = 250

# Show the cart items
print(swapan.cart)

# Try removing an item (optional)
# swapan.remove_item('dim')

# Checkout with given amount
swapan.checkout(1600)
