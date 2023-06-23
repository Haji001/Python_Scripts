names = []
phone_numbers = []
num = 1

for i in range(num):
    name = input("Enter your name: ")
    phone_number = input("Enter your phone number: ")

    names.append(name)
    phone_numbers.append(phone_number)

print("Name\t\t\tPhone Number")

for i in range(num):
    print(f"{names[i]}\t\t\t{phone_numbers[i]}")


print("Here's the results")

search_name = input("Enter search item:\n")

if search_name in names:
    index = names.index(search_name)
    phone = phone_numbers[index]

    print(f"Name:\t{search_name}\tPhone Numbers:\t{phone}")
else:
    print("Not found")
