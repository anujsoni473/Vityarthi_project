"""
Convenience Store Bill Calculator
A simple first-year BTech Python project.

This program uses:
- input and output
- variables and data types
- operators
- if/elif/else
- loops
- lists
- functions
- modules
- classes and objects
- error handling
"""

from products import show_products, find_product
from cart import Cart
from billing import print_bill
from validation import get_positive_integer, get_product_code, get_customer_name
from reports import show_summary, show_help


def add_product_to_cart(cart):
    show_products()

    code = get_product_code("\nEnter product code: ")
    product = find_product(code)

    if product is None:
        print("Sorry, that product code was not found.")
        return

    quantity = get_positive_integer("Enter quantity: ")
    cart.add_item(product, quantity)

    print(f"{quantity} x {product.name} added to the cart.")


def remove_product_from_cart(cart):
    if cart.is_empty():
        print("\nCart is already empty.")
        return

    cart.show_cart()
    code = get_product_code("\nEnter product code to remove: ")

    if cart.remove_item(code):
        print("Item removed from the cart.")
    else:
        print("That product is not in the cart.")


def main():
    print("==========================================")
    print("     CONVENIENCE STORE BILL CALCULATOR")
    print("==========================================")

    customer_name = get_customer_name()
    cart = Cart()

    while True:
        print("\n--------------- MENU ---------------")
        print("1. View Products")
        print("2. Add Item")
        print("3. Remove Item")
        print("4. View Cart")
        print("5. Order Summary")
        print("6. Generate Bill")
        print("7. Help")
        print("8. Exit")
        print("-------------------------------------")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            show_products()

        elif choice == "2":
            add_product_to_cart(cart)

        elif choice == "3":
            remove_product_from_cart(cart)

        elif choice == "4":
            cart.show_cart()

        elif choice == "5":
            show_summary(cart)

        elif choice == "6":
            if cart.is_empty():
                print("\nPlease add at least one item before generating a bill.")
            else:
                print_bill(cart, customer_name)

        elif choice == "7":
            show_help()

        elif choice == "8":
            print("\nThank you for using the Convenience Store Bill Calculator.")
            break

        else:
            print("Invalid choice. Please select a number from 1 to 8.")


if __name__ == "__main__":
    main()
