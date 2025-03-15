weather = input("Enter today's weather condition. (sunny, rainy, snowy)").lower()

if weather == "sunny":
    activity = "Go for a walk"
elif weather == "rainy":
    activity = "Read a book"
elif weather == "snowy":
    activity = "Build a snowman"
else:
    activity = "Invalid input. Please enter sunny, rainy, or snowy."

print(activity)

