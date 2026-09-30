"""
billing.py
Calculates the final amount and prints the bill.
"""

from discount import calculate_discount


def calculate_bill(subtotal, tax_rate=5):
    discount = calculate_discount(subtotal)
    taxable_amount = subtotal - discount
    tax = taxable_amount * tax_rate / 100
    final_amount = taxable_amount + tax

    return discount, tax, final_amount


def print_bill(cart, customer_name):
    subtotal = cart.get_subtotal()
    discount, tax, final_amount = calculate_bill(subtotal)

    print("\n==========================================")
    print("          CONVENIENCE STORE BILL")
    print("==========================================")
    print(f"Customer: {customer_name}")
    print("------------------------------------------")
    print(f"{'Item':<22} {'Qty':<5} Amount")
    print("------------------------------------------")

    for item in cart.items:
        print(
            f"{item.product.name:<22} "
            f"{item.quantity:<5} "
            f"₹{item.total():.2f}"
        )

    print("------------------------------------------")
    print(f"Subtotal:                 ₹{subtotal:.2f}")
    print(f"Discount:                -₹{discount:.2f}")
    print(f"Tax (5%):                 ₹{tax:.2f}")
    print("------------------------------------------")
    print(f"FINAL AMOUNT:             ₹{final_amount:.2f}")
    print("==========================================")
    print("Thank you for shopping with us!")
    print("==========================================")

    return final_amount
