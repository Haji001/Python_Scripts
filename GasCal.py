

def GasMileageCal(MilesDriven, GasUsed):

    GasMileage = MilesDriven / GasUsed
    return GasMileage


if __name__ == "__main__":
    MilesDriven = float(input("Enter the number of miles you drive:\n"))
    GasUsed = float(input("Enter the number of gas you used:\n"))

    gas_mileage = GasMileageCal(MilesDriven, GasUsed)

    print(f"The gas mileage is {gas_mileage} miles per/gallon.")




print(" ")





def miles(odo, miles_driven):

    total_miles = odo + miles_driven
    return total_miles

x = miles(odo=106000, miles_driven=20000)
print(f"As of now, the total of mileage of your vehicle is:\n{x}")