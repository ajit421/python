distance = int(input("Enter your distance without including KM: "))

if distance <0:
    mode="Enter a valid Distance"
elif distance <3:
    mode ="Walk"
elif distance <=15:
    mode = "Bike"
else:
    mode = "Car"

print(mode)