def toFixed(value, digits):
    return "%.*f" % (digits, value)

# NAME: Daniel Crocker
# PROGRAM NAME: Software Sales
# PURPOSE: To calculate software sales based off of the discount received depending on the quantity sold.
# DATE: February 1, 2022
# Declare Variables.
# Initialize variables for calculating.
discountTotal = 0.0
transactionPreTotal = 0.0
finalTransactionPrice = 0.0
discountRate = 0.00

# Input operations.
print("What is the price of the Software?")
softwarePrice = float(input())
print("How many software packages are to be purchased?")
softwareQuantity = int(input())

# Initial output operations.
print("")
print("")
print("=" * 80)
print(format("The cost per software package = ", ">60") + "$" + format(softwarePrice, ">10,.2f"))
print(format("The total number of software packages purchased = ", ">60") + format(softwareQuantity, ">8,"))
print("=" * 80)

# If statement to determine if and how much the discount will be.
if softwareQuantity <= 9:
    discountRate = 0.00
else:
    if softwareQuantity <= 19 and softwareQuantity >= 10:
        discountRate = 0.10
    else:
        if softwareQuantity <= 49 and softwareQuantity >= 20:
            discountRate = 0.20
        else:
            if softwareQuantity <= 99 and softwareQuantity >= 50:
                discountRate = 0.30
            else:
                discountRate = 0.40

# Calculate the discount amount.
discountTotal = discountRate * softwareQuantity * softwarePrice

# Calculate the total amount of software purchase prior to any discount.
transactionPreTotal = softwarePrice * softwareQuantity

# Calculate the final purchase price combining the discount and software price.
finalTransactionPrice = transactionPreTotal - discountTotal

# Output final results aligning decimal points vertically.
print("=" * 80)
print(format("The discount % rate = ", ">60") + format(discountRate * 100, ">11,.2f") + "%")
print(format("The calculated discount amount = ", ">60") + "$" + format(discountTotal, ">10,.2f"))
print(format("Total amount of software purchase prior to discount = ", ">60") + "$" + format(transactionPreTotal, ">10,.2f"))
print(format("Final software purchase price after applying discount = ", ">60") + "$" + format(finalTransactionPrice, ">10,.2f"))
print("=" * 80)

# End Program.
