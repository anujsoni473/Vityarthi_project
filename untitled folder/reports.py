"""
reports.py
Small reporting functions used by the main program.
"""


def show_summary(cart):
    print("\n----------- ORDER SUMMARY -----------")

    if cart.is_empty():
        print("No items have been added yet.")
        return

    print(f"Different products: {len(cart.items)}")
    print(f"Total items: {sum(item.quantity for item in cart.items)}")
    print(f"Current subtotal: ₹{cart.get_subtotal():.2f}")


def show_help():
    print("\n----------- HELP -----------")
    print("1. View Products - shows the available store items.")
    print("2. Add Item - adds a product and quantity to the cart.")
    print("3. Remove Item - removes a complete product from the cart.")
    print("4. View Cart - shows the current shopping cart.")
    print("5. Order Summary - shows basic order information.")
    print("6. Generate Bill - calculates discount, tax and final amount.")
    print("7. Exit - closes the program.")
