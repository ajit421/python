age = int(input("Enter your age: "))

Day= input("Enter the day of the week: ")


pricing = 12 if 20<=age<=59 else 8

if Day == "wednesday":
    pricing=pricing-2

print("Your tickets price $", pricing)
