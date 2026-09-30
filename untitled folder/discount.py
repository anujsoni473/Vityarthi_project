"""
discount.py
Simple discount rules for the store.
"""


def calculate_discount(subtotal):
    # The discount is kept simple so that it is easy to understand
    # and change later.
    if subtotal >= 1000:
        return subtotal * 0.10
    elif subtotal >= 500:
        return subtotal * 0.05
    else:
        return 0


def discount_message(subtotal):
    discount = calculate_discount(subtotal)

    if discount > 0:
        return f"You saved ₹{discount:.2f} with the store discount."

    return "No discount applied. Add more items to unlock a discount."
