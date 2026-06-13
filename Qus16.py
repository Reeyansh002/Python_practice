"""6. Take the number of units consumed and calculate the bill:
 Up to 100 units → ₹5 per unit
 101–200 units → ₹6 per unit
 201–300 units → ₹7 per unit

 Above 300 units → ₹8 per unit"""

unit = int(input("Enter how many units consumed:"))

if unit <= 100 :
    print("your bill is :",unit * 5)
elif unit >= 101 and unit <= 200 :
    print("Your bill is :",unit * 6)
elif unit >= 201 and unit <= 300 :
    print("Your bill is :",unit * 7)
else:
    unit > 300 
    print("Your bill is :",unit * 8)

