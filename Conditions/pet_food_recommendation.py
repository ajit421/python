print("Which type of pet do you have?")
print("1 - Dog")
print("2 - Cat")
print("3 - Other")

pet = int(input("Enter your choice (1/2/3) "))

if pet == 1:
    dog_age = int(input("Enter your dog's age in years: "))
    if dog_age < 2:
        print("Recommended: Puppy food")
    else:
        print("Recommended: Senior dog food")

elif pet == 2:
    cat_age = int(input("Enter your cat's age in years: "))
    if cat_age > 5:
        print("Recommended: Senior cat food")
    else:
        print("Recommended: Regular cat food")

else:
    print("No specific food recommendation for this pet type.")
