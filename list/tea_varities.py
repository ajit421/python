tea_varities = ['green', 'black', 'herbal', 'chai', 'oolong', 'white', 'yellow', 'masala', 'ginger', 'lemon', 'tulsi', 'rose', 'jasmine',]
print(len(tea_varities)) # Output: 13
print (tea_varities) # Output: ['green', 'black', 'herbal', 'chai', 'oolong', 'white', 'yellow', 'masala', 'ginger', 'lemon', 'tulsi', 'rose', 'jasmine']

print(tea_varities[0]) # Output: green
print(tea_varities[1:]) # Output: ['black', 'herbal', 'chai', 'oolong', 'white', 'yellow', 'masala', 'ginger', 'lemon', 'tulsi', 'rose', 'jasmine']
print(tea_varities[:]) # Output: ['green', 'black', 'herbal', 'chai', 'oolong', 'white', 'yellow', 'masala', 'ginger', 'lemon', 'tulsi', 'rose', 'jasmine']
print(tea_varities[-1]) # Output: jasmine

tea_varities[3] = "Masala chai"  # ('chai' → 'Masala chai')
print(tea_varities)  # ['green', 'black', 'herbal', 'Masala chai', 'oolong', 'white', 'yellow', 'masala', 'ginger', 'lemon', 'tulsi', 'rose', 'jasmine']

tea_varities.append("earl grey")  # Add 'earl grey' to the end of the list
print(tea_varities)  # ['green', 'black', 'herbal', 'Masala chai', 'oolong', 'white', 'yellow', 'masala', 'ginger', 'lemon', 'tulsi', 'rose', 'jasmine', 'earl grey']

print(tea_varities[1:1]) # Output: []

tea_varities[1:1] = ['tea', 'coffee'] # Insert 'tea' and 'coffee' at index 1
print(tea_varities) # ['green', 'tea', 'coffee', 'black', 'herbal', 'Masala chai', 'oolong', 'white', 'yellow', 'masala', 'ginger', 'lemon', 'tulsi', 'rose', 'jasmine', 'earl grey']

print(tea_varities[1:3]) # Output: ['tea', 'coffee']

tea_varities[:4] = [] # Remove the first 4 elements
print(tea_varities) # ['herbal', 'Masala chai', 'oolong', 'white', 'yellow', 'masala', 'ginger', 'lemon', 'tulsi', 'rose', 'jasmine', 'earl grey']

for tea in tea_varities: 
    print(tea, end="-") # Output: herbal-Masala chai-oolong-white-yellow-masala-ginger-lemon-tulsi-rose-jasmine-earl grey-

for tea in tea_varities:
    print(tea, end="") # Output: herbalMasala chaioolongwhiteyellowmasalagingerlemontulsirosejasmineearl grey

for tea in tea_varities:
    print(tea) 

# Output:
# herbal
# Masala chai
# oolong
# white
# yellow
# masala
# ginger
# lemon
# tulsi
# rose
# jasmine
# earl grey




