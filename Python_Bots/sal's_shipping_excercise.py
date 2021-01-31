
#shipping excercise
def groundShipping(weight):
  flat_charge = 20
  if weight <= 2:
    return weight * 1.5 + flat_charge
  if weight > 2 and weight <= 6:
    return weight *3 + flat_charge
  if weight > 6 and weight <=10:
    return weight * 4 + flat_charge
  if weight > 10:
    return weight *4.75 + flat_charge

def droneShipping(weight):
  if weight <= 2:
    return weight * 4.5
  if weight > 2 and weight <= 6:
    return weight *9
  if weight > 6 and weight <= 10:
    return weight *12
  if weight > 10:
    return weight *14.25

weight = 41.5

def cost(weight):
  drone =  droneShipping(weight)
  ground = groundShipping(weight)
  if drone > ground:
     print("Ground shipping is cheaper: " + str(ground) + " in comparison to Drone: "+ str(drone))
     print("cost: " + str(ground))
  else:
    print("Drone shipping costs: " + str(drone) + " while Ground is: "+str(ground))

cost(weight)
