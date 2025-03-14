square_num = {x: x**2 for x in range(10)} # Dictionary comprehension
print(square_num) # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

cube_num = {y: y**3 for y in range(10)} # Dictionary comprehension
print(cube_num) # Output: {0: 0, 1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512, 9: 729}

print(square_num.clear()) # Output: None
print(square_num) # Output: {}

key = ["a", "b", "c", "d", "e"]
print(key) # Output: ['a', 'b', 'c', 'd', 'e']

defaultValue = "Delicious"
print(defaultValue) # Output: Delicious

new_dict = dict.fromkeys(key, defaultValue)
print(new_dict) # Output: {'a': 'Delicious', 'b': 'Delicious', 'c': 'Delicious', 'd': 'Delicious', 'e': 'Delicious'}

new_dict= dict.fromkeys(key, key) 
print(new_dict) # Output: {'a': ['a', 'b', 'c', 'd', 'e'], 'b': ['a', 'b', 'c', 'd', 'e'], 'c': ['a', 'b', 'c', 'd', 'e'], 'd': ['a', 'b', 'c', 'd', 'e'], 'e': ['a', 'b', 'c', 'd', 'e']}
