#setting variable
weight = 4.8 
ground_shipping = 20
premium_shipping = 125

print("Your package weighs:",weight, "lbs")

#ground shipping
if weight <= 2:
  land = weight * 1.5 + ground_shipping
elif weight <= 6:
  land = weight * 3.0 + ground_shipping
elif  weight <= 10:
  land = weight * 4.0 + ground_shipping
else:
  land = weight * 4.75 + ground_shipping
print("Ground cost: £", land)
#premium shipping
print("Premium cost: £",premium_shipping)
#drone shipping
if weight <= 2:
  drone = weight * 4.5 
elif weight <= 6:
  drone = weight * 9.00
elif weight <= 10:
  drone = weight * 12.0
else:
  drone = weight * 14.25
print("Drone costs: £", drone)

if land < premium_shipping and land < drone:
  print("Ground shipping cheepest")
elif land > premium_shipping and drone > premium_shipping:
  print("Premium is cheepest")
elif land > drone and premium > drone:
  print("Drone is cheapest")
else:
  print("Cost is the same")
