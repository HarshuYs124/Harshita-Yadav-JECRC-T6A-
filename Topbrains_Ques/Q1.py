# An electricity board charges consumers based on units consumed:

# First 100 units → ₹5 per unit
# Next 200 units → ₹7 per unit
# Above 300 units → ₹10 per unit
# Calculate total bill amount.

units = int(input())
bill = 0

if units <= 100:
    bill = units * 5
elif units <= 300:
    bill = (100 * 5) + (units - 100) * 7
else:
    bill = (100 * 5) + (200 * 7) + (units - 300) * 10

print(bill)