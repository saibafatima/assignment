# Q3. Create a python program to compute the electricity bill for a household.
#     The per-unit charges in rupees are as follows: For the first 100 units, the user will be charged Rs. 4.5 per
# unit, for the next 100 units, the user will be charged Rs. 6 per unit, and for the next 100 units, the user will
# be charged Rs. 10 per unit, After 300 units and above the user will be charged Rs. 20 per unit.

units_consumed = int(input("enter the total number of units consumed:"))
total_bill = 0  #initialize the total bill  amount
if units_consumed <= 100 :
    total_bill = units_consumed *4.5
elif units_consumed <=200 :
    total_bill = 100 *4.5 + (units_consumed - 100)
elif units_consumed <= 300:
    total_bill = 100 * 4.5 + 100 * 6 + (units_consumed - 200) * 10
else:
    total_bill = 100 * 4.5 + 100 * 6 +100 *10 + (units_consumed - 300) * 20

print("electricity bill : Rs.", total_bill)