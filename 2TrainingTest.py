

from TrainingTest import GetFormatted



print("Enter 'q' at anytime to quit")


while True:
    
    first = input("Please give me a first name:\n")
    if first == 'q':
        break

    last = input("Please give a last name:\n")
    if last == 'q':
        break

    formatted_name = GetFormatted(first, last)
    print(f"Neatly formatted name: {formatted_name}")