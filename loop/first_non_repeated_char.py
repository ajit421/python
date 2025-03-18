# Problem: Given a string, find the first non-repeated character.

input_string=input("Enter your character: ")
# strawberry
# teeter

for char in input_string:
    if input_string.count(char)==1:
        print("Char is: ",char)
        break # terminate next char

