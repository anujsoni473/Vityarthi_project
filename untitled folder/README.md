Convenience Store Bill Calculator

1. Project Overview

This is a small Python project made for the VITyarthi Build Your Own Project activity.

The idea is simple: a customer selects items from a convenience store, enters the required quantity, and the program prepares a bill. The program also applies a basic discount and adds 5% tax.

We kept the project at a level that is realistic for first-year BTech students. Instead of using a database or any external library, we used Python concepts that we have learned in the course.

2. Main Features

Display the available products and prices.

Add products and quantities to a shopping cart.

Remove a product from the cart.

View the current cart.

Show a simple order summary.

Apply discount rules.

Calculate 5% tax.

Generate a final bill.

Handle incorrect inputs without immediately stopping the program.

Run a few basic validation tests.

3. Technologies Used

Python 3

Python standard features only

No external libraries are required.

The project uses concepts such as variables, input/output, operators, conditions, loops, lists, functions, modules, classes, objects and basic error handling.

4. Project Files

main.py - starts the program and handles the menu.

products.py - contains the product class and product list.

cart.py - manages cart items and calculations.

discount.py - contains the discount rules.

billing.py - calculates tax and creates the bill.

validation.py - checks user input.

reports.py - displays order information and help.

test_project.py - contains simple tests.

5. How to Run

Make sure Python 3 is installed.

Open a terminal in the project folder and run:

python main.py

Then follow the menu shown on the screen.

6. How to Test

Run:

python test_project.py

If everything is working correctly, the program prints:

All tests passed successfully.

7. Basic Discount Rule

Below ₹500: no discount

₹500 to ₹999.99: 5% discount

₹1000 and above: 10% discount

After the discount, 5% tax is calculated on the reduced amount.

8. Limitations

This is an educational project, so it does not have online payment, a database, barcode scanning or a real inventory system.

9. Future Improvements

In the future, we could add:

stock/inventory management

saving bills to a file

barcode input

different tax categories

a customer purchase history

a graphical interface

10. Learning Outcome

While making this project, we got practice in breaking one problem into smaller Python modules. We also understood why functions and classes make a program easier to manage than putting everything in one large file.