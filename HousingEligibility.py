from itertools import chain, repeat

incomeRange = list(range(49000, 89000))
#print(incomeRange)

print("**** Welcome to Enrich Apartments ****")
print(" ")


name = input("Enter your fullname: \n")
name = str(name)

   
for i in incomeRange:


  grossIncome = input('Enter your gross annual income: \n')
  grossIncome = int(grossIncome)
  
  if grossIncome < i:
    print("We're sorry, you do not the minimum income requirement")
    break

  else:
    previousAddress = input('How long did you stay at your last address?\n')
    
    break
   
