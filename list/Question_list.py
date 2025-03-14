tea_varities = ['green', 'black', 'herbal', 'chai', 'oolong', 'white', 'yellow', 'masala', 'ginger', 'lemon']

print(tea_varities) # Output: ['green', 'black', 'herbal', 'chai', 'oolong', 'white', 'yellow', 'masala', 'ginger', 'lemon']

if "chai" in tea_varities: # Check if 'chai' is in the list
    print("I have chai") # Output: I have chai

if "kashmiri chai" in tea_varities: # Check if 'kashmiri chai' is in the list
    print("I have Kashamiri chai") # Output: I have Kashamiri chai

tea_varities.append("kashamiri chai") # Add 'kashamiri chai' to the end of the list
print (tea_varities) # Output: ['green', 'black', 'herbal', 'chai', 'oolong', 'white', 'yellow', 'masala', 'ginger', 'lemon', 'kashamiri chai']

print(tea_varities.pop()) # Output: kashamiri chai
print(tea_varities) # Output: ['green', 'black', 'herbal', 'chai', 'oolong', 'white', 'yellow', 'masala', 'ginger', 'lemon']

tea_varities.remove("oolong") # Remove 'oolong' from the list
print(tea_varities) # Output: ['green', 'black', 'herbal', 'chai', 'white', 'yellow', 'masala', 'ginger', 'lemon']

tea_varities.insert(1,"ginger") # Insert 'ginger' at index 1
print(tea_varities) # Output: ['green', 'ginger', 'black', 'herbal', 'chai', 'white', 'yellow', 'masala', 'ginger', 'lemon']

tea_varities_copy = tea_varities.copy() # Create a copy of the list
tea_varities_copy.append('Tulsi') # Add 'Tulsi' to the end of the list
tea_varities.pop() # Remove the last element from the original list

print(tea_varities) # Output: ['green', 'ginger', 'black', 'herbal', 'chai', 'white', 'yellow', 'masala', 'ginger']
print(tea_varities_copy) # Output: ['green', 'ginger', 'black', 'herbal', 'chai', 'white', 'yellow', 'masala', 'ginger', 'Tulsi']

