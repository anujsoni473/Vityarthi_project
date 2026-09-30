"""
cart.py
Shopping cart operations.
"""

class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def total(self):
        return self.product.price * self.quantity


class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        for item in self.items:
            if item.product.code == product.code:
                item.quantity += quantity
                return

        self.items.append(CartItem(product, quantity))

    def remove_item(self, code):
        for item in self.items:
            if item.product.code == code.upper():
                self.items.remove(item)
                return True

        return False

    def is_empty(self):
        return len(self.items) == 0

    def get_subtotal(self):
        subtotal = 0

        for item in self.items:
            subtotal += item.total()

        return subtotal

    def show_cart(self):
        if self.is_empty():
            print("\nCart is empty.")
            return

        print("\n------------- CART -------------")
        print(f"{'Product':<25} {'Qty':<5} {'Amount'}")
        print("-" * 45)

        for item in self.items:
            print(
                f"{item.product.name:<25} "
                f"{item.quantity:<5} "
                f"₹{item.total():.2f}"
            )

        print("-" * 45)
        print(f"Subtotal: ₹{self.get_subtotal():.2f}")
