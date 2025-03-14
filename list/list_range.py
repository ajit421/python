squared_num = range(10) # range(10) is a generator
print(squared_num) # Output: range(0, 10)

squared_num=[x**2 for x in range(10)] # List comprehension
print(squared_num) # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

cube_num = [y**3 for y in range(10)] # List comprehension
print(cube_num) # Output: [0, 1, 8, 27, 64, 125, 216, 343, 512, 729] 



