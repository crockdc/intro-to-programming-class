# Function to check the data type and for positive input
def checkFloatDataType():
    while True: # Loop is used to check the data type, negative values or values greater than 100000000
        try:
            floatDataType = float(input())
        except ValueError:
            print("You entered the wrong data type\n" \
                  "Re-enter a positive value [decimals are acceptable]")
            continue
        else:
            if (floatDataType < 0) or (floatDataType > 100000000):
                print("You entered a negative value or a value > 100,000,000\n" \
                      "Re-enter a positive value [decimals are acceptable]")
                continue
            else:
                break
            # end Try statement
        # end while True statement
    return floatDataType
    # End checkFloatDataType function

# Define a function to add all of the purchases
def addTotalPurchases(i1, i2, i3, i4, i5):
    totalPurchase = i1 + i2 + i3 + i4 + i5
    return totalPurchase
    # End addTotalPurchases function

# Define a function to calculate the sales tax total
def calcSalesTax(t1, t2):
    taxTotal = t1 * t2
    return taxTotal
    # End calcSalesTax function

# Define a function to calculate the final total
def finalTotal(f1, f2):
    final = f1 + f2
    return final
    #End finalTotal function

# Define a function to write the results and create a report
def writeResults(i1, i2, i3, i4, i5, sub, tax, tot):
    # REPORT HEADING AND COLUMN HEADINGS
    outFile.write("=" * 60 + "\n")
    outFile.write("TOTAL PURCHASE RECEIPT         /        INFORMATION\n")
    outFile.write("=" * 60 + "\n")

    # Display the price for each item number
    outFile.write(f"PRICE FOR ITEM #01:                      ${i1:10,.2f}\n")
    outFile.write(f"PRICE FOR ITEM #02:                      ${i2:10,.2f}\n")
    outFile.write(f"PRICE FOR ITEM #03:                      ${i3:10,.2f}\n")
    outFile.write(f"PRICE FOR ITEM #04:                      ${i4:10,.2f}\n")
    outFile.write(f"PRICE FOR ITEM #05:                      ${i5:10,.2f}\n")
    outFile.write("=" * 60 + "\n")

    # Display the subtotal, the sales tax, and the combined total
    outFile.write(f"SUBTOTAL:                                ${sub:10,.2f}\n")
    outFile.write(f"SALES TAX:                               ${tax:10,.2f}\n")
    outFile.write(f"TOTAL SALES:                             ${tot:10,.2f}\n")
    outFile.write("=" * 60 + "\n")
    # End of writeResults function
        
# PROGRAMMER: Daniel Crocker
# PROGRAM NAME: Total Purchases (revised for Assignment 8)
# DATE WRITTEN: January 25, 2022 (revised on March 27, 2022)
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
item1 = checkFloatDataType() # Call function to check data type and for negative values
        
print("Enter the price of item #02:")
item2 = checkFloatDataType() # Call function to check data type and for negative values

print("Enter the price of item #03:")
item3 = checkFloatDataType() # Call function to check data type and for negative values

print("Enter the price of item #04:")
item4 = checkFloatDataType() # Call function to check data type and for negative values

print("Enter the price of item #05:")
item5 = checkFloatDataType() # Call function to check data type and for negative values

print("Enter the sales tax: [enter decimal value i.e. 0.04, .0.07]")
salesTaxDefined = checkFloatDataType() # Call function to check data type and for negative values

# Calculate the subtotal of the items using the addTotalPurchases function
subtotal = addTotalPurchases(item1, item2, item3, item4, item5)

# Calculate the amount of sales tax using the calcSalesTax function
salesTax = calcSalesTax(subtotal, salesTaxDefined)

# Calculate the total of the sale, including sales tax, utilizing the finalTotal function
total = finalTotal(subtotal, salesTax)

# OUTPUT OPERATIONS(utilizing the writeResults function)
writeResults(item1, item2, item3, item4, item5, subtotal, salesTax, total)

# Close the newly formed external file where output will be written
outFile.close()

# END PROGRAM
