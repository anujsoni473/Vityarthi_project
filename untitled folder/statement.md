Project Statement

Project Title

Convenience Store Bill Calculator

Problem Statement

In a small convenience store, calculating the bill manually can take time and can also lead to mistakes, especially when there are several products and different quantities.

The purpose of this project is to make a simple Python-based billing system that can take the customer's items, calculate their cost, apply a basic discount, add tax and display the final amount.

The project is intentionally kept simple because it is designed as a first-year BTech Python project.

Scope of the Project

The project covers the basic billing process inside a small convenience store.

The system can:

display products

accept product selection

accept quantity

maintain a shopping cart

remove products

calculate subtotal

apply a discount

calculate tax

generate a final bill

The project does not cover online payments, a real database, barcode hardware or cloud services.

Target Users

The main target users are:

small convenience store staff

students learning programming

beginners who want to understand how a billing system works

High-Level Features

Product catalogue

Shopping cart

Billing and discount calculation

Input validation

Order summary

Basic testing

Expected Input

The user provides:

customer name

menu choice

product code

quantity

Expected Output

The program provides:

product list

cart details

subtotal

discount

tax

final payable amount

simple help and order summary

Major Functional Modules

1. Product Management

Shows the available products and finds a product from its code.

2. Cart Management

Adds and removes products and calculates the current subtotal.

3. Billing and Reporting

Calculates discount and tax, generates the final bill and shows a basic order summary.

Non-Functional Requirements

Usability

The menu should be easy for a beginner to understand.

Reliability

Wrong product codes and invalid numbers should be handled without crashing the program.

Maintainability

The program is divided into separate Python modules so that individual parts can be changed more easily.

Resource Efficiency

The program uses only simple Python data structures and does not need an external database or heavy software.

Error Handling

The program checks important user inputs and shows a useful message when the input is invalid.

Project Objective

The main objective is to apply the Python concepts learned in the course to a small real-world problem. The project also helps us understand how a bigger program can be divided into smaller files and functions.