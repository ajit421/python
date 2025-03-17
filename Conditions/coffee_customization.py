coffee_size = input("Enter coffee order: (eg. small, medium, large)").lower()

if coffee_size not in ["small", "medium", "large"]:
    print("invalid selection. please choose small, medium, large.")
    exit()

extra_short= input("do you need Extra shot ? yes/no")

if extra_short=="yes":
    order = coffee_size + " coffee with an extra short"
else:
    order=coffee_size + " coffee"

print(order)