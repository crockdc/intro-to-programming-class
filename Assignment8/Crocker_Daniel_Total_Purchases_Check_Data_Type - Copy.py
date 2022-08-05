# PROGRAMMER: Daniel Crocker
# PROGRAM NAME: Total Purchases (revised for Assignment 8)
# DATE WRITTEN: January 25, 2022 (revised on March 21, 2022)
# PURPOSE: Ask for the price of five items being purchased, then display the subtotal, sales tax, and the total sale.
# Declare variables in alphabetical order
# Initialize variables used to store calculations or results
fileName = ''
outFile = ''
subtotal = 0.0
salesTaxDefined = 0.0
total = 0.0

# Create file name where results will be stored (ask user for the file name)
fileName = input("Enter the file name where you wish to write the output/results\n")
outFile = open(fileName + ".txt", "w")

# Input Operations utilizing TRY/EXCEPT within WHILE loops
print("Enter the price of item #01:")
while True: # Loop is used to check the data type, negative values or values greater than 100000000
    try:
        item1 = float(input())
    except ValueError:
        print("You entered the wrong data type\n" \
              "Re-enter a positive value [decimals are acceptable]")
        continue
    else:
        if (item1 < 0) or (item1 > 100000000):
            print("You entered a negative value or a value > 100,000,000\n" \
                  "Re-enter a positive value [decimals are acceptable]")
            continue
        else:
            break
        
print("Enter the price of item #02:")
while True: # Loop is used to check the data type, negative values or values greater than 100000000
    try:
        item2 = float(input())
    except ValueError:
        print("You entered the wrong data type\n" \
              "Re-enter a positive value [decimals are acceptable]")
        continue
    else:
        if (item2 < 0) or (item2 > 100000000):
            print("You entered a negative value or a value > 100,000,000\n" \
                  "Re-enter a positive value [decimals are acceptable]")
            continue
        else:
            break

print("Enter the price of item #03:")
while True: # Loop is used to check the data type, negative values or values greater than 100000000
    try:
        item3 = float(input())
    except ValueError:
        print("You entered the wrong data type\n" \
              "Re-enter a positive value [decimals are acceptable]")
        continue
    else:
        if (item3 < 0) or (item3 > 100000000):
            print("You entered a negative value or a value > 100,000,000\n" \
                  "Re-enter a positive value [decimals are acceptable]")
            continue
        else:
            break

print("Enter the price of item #04:")
while True: # Loop is used to check the data type, negative values or values greater than 100000000
    try:
        item4 = float(input())
    except ValueError:
        print("You entered the wrong data type\n" \
              "Re-enter a positive value [decimals are acceptable]")
        continue
    else:
        if (item4 < 0) or (item4 > 100000000):
            print("You entered a negative value or a value > 100,000,000\n" \
                  "Re-enter a positive value [decimals are acceptable]")
            continue
        else:
            break

print("Enter the price of item #05:")
while True: # Loop is used to check the data type, negative values or values greater than 100000000
    try:
        item5 = float(input())
    except ValueError:
        print("You entered the wrong data type\n" \
              "Re-enter a positive value [decimals are acceptable]")
        continue
    else:
        if (item5 < 0) or (item5 > 100000000):
            print("You entered a negative value or a value > 100,000,000\n" \
                  "Re-enter a positive value [decimals are acceptable]")
            continue
        else:
            break

print("Enter the sales tax: [enter decimal value i.e. 0.04, .0.07]")
while True: # Loop is used to check the data type, negative values or values greater than 100000
    try:
        salesTaxDefined = float(input())
    except ValueError:
        print("You entered the wrong data type\n" \
              "Re-enter a positive value [decimals are acceptable]")
        continue
    else:
        if (salesTaxDefined < 0) or (salesTaxDefined > 100000):
            print("You entered a negative value or a value > 100,000\n" \
                  "Re-enter a positive value [decimals are acceptable]")
            continue
        else:
            break

# Calculate the subtotal of the items
subtotal = item1 + item2 + item3 + item4 + item5

# Calculate the amount of sales tax.
salesTax = subtotal * salesTaxDefined

# Calculate the total of the sale, including sales tax
total = subtotal + salesTax

# OUTPUT OPERATIONS
# REPORT HEADING AND COLUMN HEADINGS
outFile.write("=" * 60 + "\n")
outFile.write("TOTAL PURCHASE RECEIPT         /        INFORMATION\n")
outFile.write("=" * 60 + "\n")

# Display the price for each item number
outFile.write(f"PRICE FOR ITEM #01:                      ${item1:10,.2f}\n")
outFile.write(f"PRICE FOR ITEM #02:                      ${item2:10,.2f}\n")
outFile.write(f"PRICE FOR ITEM #03:                      ${item3:10,.2f}\n")
outFile.write(f"PRICE FOR ITEM #04:                      ${item4:10,.2f}\n")
outFile.write(f"PRICE FOR ITEM #05:                      ${item5:10,.2f}\n")
outFile.write("=" * 60 + "\n")

# Display the subtotal, the sales tax, and the combined total
outFile.write(f"SUBTOTAL:                                ${subtotal:10,.2f}\n")
outFile.write(f"SALES TAX:                               ${salesTax:10,.2f}\n")
outFile.write(f"TOTAL SALES:                             ${total:10,.2f}\n")
outFile.write("=" * 60 + "\n")

# Close the newly formed external file where output will be written
outFile.close()

# END PROGRAM
