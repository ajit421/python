chai_types = {"Masala": "spicy", "Ginger": "Zesty", "Green": "Mild", "Black": "Strong"}
print(chai_types) # Output: {'Masala': 'spicy', 'Ginger': 'Zesty', 'Green': 'Mild', 'Black': 'Strong'}

# Accessing the values using the keys
print(chai_types["Masala"]) # Output: spicy
print(chai_types["Ginger"]) # Output: Zesty
print(chai_types["Green"]) # Output: Mild
print(chai_types["Black"]) # Output: Strong

chai_types["Black"] = "Robust"
print(chai_types) # Output: {'Masala': 'spicy', 'Ginger': 'Zesty', 'Green': 'Mild', 'Black': 'Robust'}

# Adding a new key-value pair
chai_types["Herbal"] = "Medicinal"
print(chai_types) # Output: {'Masala': 'spicy', 'Ginger': 'Zesty', 'Green': 'Mild', 'Black': 'Strong', 'Herbal': 'Medicinal'}

# Deleting a key-value pair
del chai_types["Herbal"]
print(chai_types) # Output: {'Masala': 'spicy', 'Ginger': 'Zesty', 'Green': 'Mild', 'Black': 'Strong'}


for chai in chai_types:
    print(chai) 

# Output:
# Masala
# Ginger
# Green
# Black

for chai in chai_types:
    print(chai, chai_types[chai])

# Output:
# Masala spicy
# Ginger Zesty
# Green Mild
# Black Robust

for key, Value in chai_types.items():
    print(key, Value)

# Output:
# Masala spicy
# Ginger Zesty
# Green Mild
# Black Robust

if "Masala" in chai_types:
    print("Masala is in the dictionary")
else:
    print("Masala is not in the dictionary")

# Output: Masala is in the dictionary


chai_types.pop("Masala")
print(chai_types) # Output: {'Ginger': 'Zesty', 'Green': 'Mild', 'Black': 'Strong'}

