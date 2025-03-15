weather = {
    "sunny": "go for a walk",
    "rainy": "read a book",
    "snowy": "build a snowman"
    }

today_weather = input("choose today's weather (sunny, rainy, snowy)").lower()

if today_weather in weather:
    print(weather[today_weather])

else:
    print("Invalid input. Please enter sunny, rainy, or snowy")
