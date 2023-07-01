import pyinputplus as pyip



def salary():
   
    try:
        total_salary = float(input("Enter this month's salary:\n"))
        return total_salary
    except ValueError:
        print('INVALID INPUT.\nPlease enter the right numeric value:\n')



def saving(salary_amount):

    saving_percentage = 0.6
    salary_amount = salary()
    savings = saving_percentage * salary_amount
    remaining = salary_amount - savings

    return savings, remaining



def expenses():
    try:
        rent_or_mortgage = float(input("How much is rent/mortgage?\n"))
        food = float(input("How much money you spend on food?\n"))

        car_payments = pyip.inputYesNo(prompt="Do you have any car payments?\nEnter (y)es or (n)o\n")
        if car_payments == 'yes':
            car_payment = float(input("How much is your car payment?\n"))
            car_insurance = float(input("How much is your car insurance?\n"))

        
        entertaiment = float(input("How much do you spend on entertainment?\n"))
        other_expenses = float(input("Other expenses:\n"))

       
        total_expenses = (
            rent_or_mortgage +
            food +
            car_payment +
            car_insurance +
            entertaiment +
            other_expenses
        )

        return total_expenses

    except ValueError:
        print('INVALID INPUT.\nPlease enter the right numeric value:\n')


this_month_salary = salary()
print(f"\tThis month's total salary:\t${this_month_salary}")
print(" ")

this_month_saving = saving(this_month_salary)
print(f"\tThis month's savings:\t${this_month_saving[0]}")
print("\t\t\t\tSaving|Remaining")
print(f"\t\t\t\t${this_month_saving[0]} | ${this_month_saving[1]}")
print(" ")

total_expenses = expenses()
print(f"\tTotal expenses:\t${total_expenses}")



