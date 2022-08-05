def toFixed(value, digits):
    return "%.*f" % (digits, value)

# PROGRAMMER:   Daniel Crocker
# PROGRAM NAME:  Customer Information Program using a While Loop
# DATE WRITTEN:  February 10, 2022
# PURPOSE: DEMONSTRATE BASIC WHILE LOOP CONCEPT
# Declare variables in alpha order
# answer is the lcv
# Initialize variable(s) where calculated results are stored.
averagePurchase = 0.0
count = 0
totalAmount = 0.0

# Main Column Heading
print('=' * 62)
print("CUSTOMER PURCHASE INFORMATION")
print('=' * 62)
print("CUSTOMER NAME                       PURCHASE AMOUNT")
print('=' * 62)

# Initialize lcv "answer"
print("Do you wish to process a customer's information? [type 'y' or 'Y' otherwise enter 'no'] ")
answer = input()

# Display a blank line
print(" ")

# While Loop
# testing the lcv To enter more than one customer name and purchase amount
while answer == "y" or answer == "Y": 
    # Input Operations
    print("Enter customer's name ")
    customerName = input()
    print("How much did the customer spend on this item? ")
    purchaseAmount = float(input())
    
    # keep a running total of the purchase amounts per customer
    totalAmount = totalAmount + purchaseAmount
    
    # count or tally the number of customers / purchases
    count = count + 1
    
    # Output each customer name and their purchase amount as a column
    print(f'{customerName:30s}{" ":10s}{"$":2s}{purchaseAmount:12,.2f}')
    
    # update lcv answer
    print("Do you wish to process a customer's information? [type 'y' or 'Y' otherwise enter 'no'] ")
    answer = input()
    print(" ")
    
    # end while loop
# calculate the average purchase amount
averagePurchase = totalAmount / count

# Output operations
print('=' * 62)

# Displays the total amount of purchases for all the customers
print(f'{"Customer Total Purchases = ":30s}{" ":10s}{"$":2s}{totalAmount:12,.2f}')
print('=' * 62)

# Displays the Average of purchases for all the customers
print(f'{"THE AVERAGE PURCHASE PRICE = ":30s}{" ":10s}{"$":2s}{averagePurchase:12,.2f}')
print('=' * 62)
print("THIS PROGRAM IS COMPLETE - EDITED BY DANIEL CROCKER")
print('=' * 62)

# END PROGRAM
