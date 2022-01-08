#!/usr/bin/python3
income = float(input("Enter the annual income: "))
threshold = 85528

if income < threshold:
    tax = (income * 0.18) - 556.2
else:
    tax = 14839.2 + ((income - 85528) * 0.32)

if tax < 0:
    tax = 0

tax = round(tax, 0)
print("The tax is:", tax, "thalers")

