"""
products.py
Product catalog for the Convenience Store Bill Calculator.
"""

class Product:
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.price = price

    def display(self):
        return f"{self.code:<6} {self.name:<25} ₹{self.price:.2f}"


PRODUCTS = [
    Product("P01", "Milk", 32.00),
    Product("P02", "Bread", 40.00),
    Product("P03", "Eggs (6)", 48.00),
    Product("P04", "Biscuits", 30.00),
    Product("P05", "Chips", 20.00),
    Product("P06", "Cold Drink", 45.00),
    Product("P07", "Chocolate", 35.00),
    Product("P08", "Noodles", 25.00),
    Product("P09", "Soap", 38.00),
    Product("P10", "Shampoo Sachet", 10.00)
]


def show_products():
    print("\n----------- PRODUCT LIST -----------")
    print(f"{'Code':<6} {'Product':<25} Price")
    print("-" * 45)

    for product in PRODUCTS:
        print(product.display())


def find_product(code):
    code = code.upper()

    for product in PRODUCTS:
        if product.code == code:
            return product

    return None