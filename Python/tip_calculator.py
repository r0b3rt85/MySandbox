# You're almost there! Assign the tip variable on line 5.

meal = 44.50
tax = 6.75 / 100
#tip = 0.15
tip = 15.0 / 100

meal = meal + (meal * tax)
total = meal + (meal * tip)

print("%.2f" % total)
