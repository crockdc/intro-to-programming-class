# PROGRAMMER: Daniel Crocker
# PROGRAM NAME: Total Purchases
# DATE WRITTEN: January 25, 2022
# PURPOSE: Ask for the price of five items being purchased, then display the subtotal, sales tax, and the total sale.
# Declare variables in alphabetical order
# Initialize variables used to store calculations or results
subtotal = 0.0
salesTaxDefined = 0.0
total = 0.0

# Input Operations
print("Enter the price of item #01:")
item1 = float(input())
print("Enter the price of item #02:")
item2 = float(input())
print("Enter the price of item #03:")
item3 = float(input())
print("Enter the price of item #04:")
item4 = float(input())
print("Enter the price of item #05:")
item5 = float(input())
print("Enter the sales tax: [enter decimal value i.e. 0.04, .0.07]")
salesTaxDefined = float(input())

# Calculate the subtotal of the items.
subtotal = item1 + item2 + item3 + item4 + item5

# Calculate the amount of sales tax.
salesTax = subtotal * salesTaxDefined

# Calculate the total of the sale, including sales tax.
total = subtotal + salesTax

# OUTPUT OPERATIONS
# REPORT HEADING AND COLUMN HEADINGS
print("=" * 60)
print("TOTAL PURCHASE RECEIPT         /        INFORMATION")
print("=" * 60)

# Display the price for each item number.
print(f"PRICE FOR ITEM #01:                      ${item1:>,.2f}")
print(f"PRICE FOR ITEM #02:                      ${item2:>,.2f}")
print(f"PRICE FOR ITEM #03:                      ${item3:>,.2f}")
print(f"PRICE FOR ITEM #04:                      ${item4:>,.2f}")
print(f"PRICE FOR ITEM #05:                      ${item5:>,.2f}")
print("=" * 60)

# Display the subtotal, the sales tax, and the combined total.
print(f"SUBTOTAL:                                ${subtotal:>,.2f}")
print(f"SALES TAX:                               ${salesTax:>,.2f}")
print(f"TOTAL SALES:                             ${total:>,.2f}")
print("=" * 60)

# END PROGRAM
