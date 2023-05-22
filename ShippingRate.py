import random


# ------------------------Ground shipping-----------------------------# 

destinationTax = .005
maxWeight = 120


States = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado",
  "Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois",
  "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
  "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",
  "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York",
  "North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
  "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah",
  "Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]



loc = str(input("Where you shipping to? \n"))

packageWeight = int(input("How much your package weight? \n"))
  
if loc in States: 
  if packageWeight in range(1, 10):
     costofShipping = packageWeight * destinationTax + random.randint(5, 10)
                                                      # \\ Price ranges between $5 to $10

  if packageWeight in range(10, 20):
    costofShipping = packageWeight * destinationTax + random.randint(10, 15)
    
  if packageWeight in range(20,30):
    costofShipping = packageWeight * destinationTax + random.randint(20, 25)

  if packageWeight in range(30, 40):
    costofShipping = packageWeight * destinationTax + random.randint(30, 35)

  if packageWeight in range(40, 50):
    costofShipping = packageWeight * destinationTax + random.randint(35, 40)

  if packageWeight in range(50, 60):
    costofShipping = packageWeight * destinationTax + random.randint(40, 45)

  if packageWeight in range(60, 70):
    costofShipping = packageWeight * destinationTax + random.randint(50, 55)

  if packageWeight in range(70, 80):
    costofShipping = packageWeight * destinationTax + random.randint(60, 65)

  if packageWeight in range(80, 90):
    costofShipping = packageWeight * destinationTax + random.randint(70, 75)

  if packageWeight in range(90, 100):
    costofShipping = packageWeight * destinationTax + random.randint(80, 85)
    
print("Your shipping total is ${0}".format(costofShipping))
    

  

