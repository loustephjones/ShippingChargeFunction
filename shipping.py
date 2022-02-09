weight = 1.5 
mode = "drone"
premium = True

#Ground Shipping

if weight <= 2:
  ground_cost = weight * 1.50 + 20.00
elif weight <=6:
  ground_cost = weight * 3.00 + 20.00
elif weight <=10:
  ground_cost = weight * 4.00 + 20.00
elif weight > 10:
  ground_cost = weight * 4.75 + 20.00

if mode == "ground" and premium:
  print(round(ground_cost + 125.00, 2))
elif mode == "ground": 
  print(round(ground_cost, 2))

#Drone Shipping

if weight <= 2:
  drone_cost = weight * 4.50
elif weight <=6:
  drone_cost = weight * 9.00
elif weight <=10:
  drone_cost = weight * 12.00
else:
    
  drone_cost = weight * 14.25

if mode == "drone":
  print(round(drone_cost, 2))
elif mode == "":
  print("Which method of shipping do you want to use?")

