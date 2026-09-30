"""
test_project.py
Basic validation tests for the project.

These tests use only Python's built-in assert statement.
"""

from products import find_product
from cart import Cart
from discount import calculate_discount
from billing import calculate_bill


def test_product_search():
    product = find_product("P01")

    assert product is not None
    assert product.name == "Milk"


def test_cart_total():
    cart = Cart()
    product = find_product("P05")

    cart.add_item(product, 3)

    assert cart.get_subtotal() == 60


def test_discount():
    assert calculate_discount(400) == 0
    assert calculate_discount(600) == 30
    assert calculate_discount(1000) == 100


def test_bill():
    discount, tax, final_amount = calculate_bill(600)

    assert discount == 30
    assert tax == 28.5
    assert final_amount == 598.5


def run_tests():
    test_product_search()
    test_cart_total()
    test_discount()
    test_bill()

    print("All tests passed successfully.")


if __name__ == "__main__":
    run_tests()
