tea_types = ("Masala", "Ginger", "Green", "Black")

print(type(tea_types)) # Output: <class 'tuple'>
print(tea_types) # Output: ('Masala', 'Ginger', 'Green', 'Black')

# Accessing the values using the keys
print(tea_types[0]) # Output: Masala
print(tea_types[1]) # Output: Ginger
print(tea_types[:]) # Output: ('Masala', 'Ginger', 'Green', 'Black')

print(len(tea_types)) # Output: 4

more_tea = ("Herbal", "Oolong", "White")
print(tea_types + more_tea) # Output: ('Masala', 'Ginger', 'Green', 'Black', 'Herbal', 'Oolong', 'White')

print(tea_types * 2) # Output: ('Masala', 'Ginger', 'Green', 'Black', 'Masala', 'Ginger', 'Green', 'Black')

print("Masala" in tea_types) # Output: True

if "Masala" in tea_types:
    print("Masala is in the tuple")
else:
    print("Masala is not in the tuple")
# Output: Masala is in the tuple



