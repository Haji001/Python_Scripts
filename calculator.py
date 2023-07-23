


def addition(x, y):
    return x + y

def substraction(x, y):
    return x - y

def multiplication(x, y):
    return x - y

def division(x, y):
    return x / y



# firstNum = float(input("Enter first number:"))
# secondNum = float(input("Enter second number:"))

def calculation():

     print(f"Enter 1 for addition")
     print(f"Enter 2 for substraction")
     print(f"Enter 3 for multiplication")
     print(f"Enter 4 for division")
     print(f"Enter 5 to exit the calculator")
    
     
     
     while True:
        
        print(" ")
        choice = input("Select operation of choice:\n")
        option_list = ['1', '2', '3', '4', '5']
       
        if choice not in option_list:
            print(f"{choice} is a invalid selection. Try again.")
            continue

        if choice == '5':
            break

        
        firstNum = eval(input("Enter first number:"))
        secondNum = eval(input("Enter second number:"))
        

        if choice == '1':
            results = addition(firstNum, secondNum)
            print(f"Result:\t{results}")

        elif choice == '2':
            results = substraction(firstNum, secondNum)
            print(f"Result:\t{results}")

        elif choice == '3':
            results = multiplication(firstNum, secondNum)
            print(f"Result:\t{results}")

        elif choice == '4':
            results = division(firstNum, secondNum)
            print(f"Result:\t{results}")
    
calculation()



    
