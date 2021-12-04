
# Package weight
weight = 80


# Ground Shipping

if weight <= 2:
  cost_of_ground = weight * 1.50 + 20

elif weight <= 6:
  cost_of_ground = weight * 3.00 + 20

elif weight <= 10:
  cost_of_ground = weight * 4.00 + 20

elif weight > 10:
  cost_of_ground = weight * 4.75 + 20

print("Ground Shipping is ${0}".format(cost_of_ground))

### Drone Shipping!

if weight <= 2:
  cost_of_drone = weight * 4.50

elif weight <= 6:
  cost_of_drone = weight * 9.00

elif weight <= 10:
  cost_of_drone = weight * 12.00

elif weight > 10:
  cost_of_drone = weight * 14.25

print("Drone Shipping is ${0}".format(cost_of_drone))

### Ground Shipping Premium

