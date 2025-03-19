# Problem: Reverse a string using a loop.

input_str=input("Enter a string: ")
reversed_str= ""

for char in input_str:
    reversed_str=char+reversed_str
    # print(reversed_str)
    
print(reversed_str)