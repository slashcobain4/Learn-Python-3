weight = 0
cost = 0

# Ground Shipping
if weight <= 2:
  cost = weight * 1.50 + 20
  print (cost)
elif weight <= 6:
  cost = weight * 3.00 + 20
  print (cost)
elif weight <= 10:
  cost = weight * 4.00 + 20
  print (cost)
else:
  cost = weight * 4.75 + 20
  print (cost)

#Premium Ground Shipping
premium_ground_shipping = 125
print("Ground shipping premium cost is $" + str(premium_ground_shipping))

# Drone Shipping
if weight <= 2:
  cost = weight * 4.50
  print (cost)
elif weight <= 6:
  cost = weight * 9.00
  print (cost)
elif weight <= 10:
  cost = weight * 12.00
  print (cost)
else:
  cost = weight * 14.25
  print (cost)
