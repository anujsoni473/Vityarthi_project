"""
validation.py
Input validation functions.
"""


def get_positive_integer(message):
    while True:
        try:
            value = int(input(message))

            if value > 0:
                return value

            print("Please enter a number greater than 0.")

        except ValueError:
            print("Please enter a valid whole number.")


def get_product_code(message):
    while True:
        code = input(message).strip().upper()

        if code:
            return code

        print("Product code cannot be empty.")


def get_customer_name():
    while True:
        name = input("Enter customer name: ").strip()

        if name:
            return name

        print("Customer name cannot be empty.")
