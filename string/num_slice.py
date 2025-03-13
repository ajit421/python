num_list = "0123456789"

# Basic Slicing
print(num_list[:])      # Output: '0123456789' (Full list)
print(num_list[:5])     # Output: '01234'  (First 5 digits)
print(num_list[5:])     # Output: '56789'  (Last 5 digits)

# Reverse Slicing
print(num_list[::-1])   # Output: '9876543210' (Full Reverse)
print(num_list[-1::-1]) # Output: '9876543210' (Reverse using -1 index)
print(num_list[:-6:-1]) # Output: '98765'  (Last 5 elements in reverse)
print(num_list[-5:-1])  # Output: '5678'  (Slice from -5 to -1)

# Step Size in Slicing
print(num_list[::2])   # Output: '02468'  (Even indices)
print(num_list[1::2])  # Output: '13579'  (Odd indices)

# Custom Step Sizes
print(num_list[::3])   # Output: '0369'   (Every third character)
print(num_list[1::3])  # Output: '147'    (Every third character starting at index 1)
print(num_list[2::3])  # Output: '258'    (Every third character starting at index 2)
print(num_list[::-2])  # Output: '97531'  (Reverse every second character)

# Slicing with Mixed Start and Step
print(num_list[3:10:3])  # Output: '369'
print(num_list[4:9:3])   # Output: '47'
print(num_list[5:10:3])  # Output: '58'
print(num_list[6:10:3])  # Output: '69'
print(num_list[7:10:3])  # Output: '7'
print(num_list[1:10:4])  # Output: '159'  (Every 4th character from index 1)

# Edge Cases
print(num_list[10:])   # Output: '' (Empty string since index 10 is out of range)
print(num_list[10:12]) # Output: '' (Empty string)
print(num_list[-1:])   # Output: '9' (Last character)
print(num_list[-3:])   # Output: '789' (Last 3 characters)
print(num_list[:-3])   # Output: '0123456' (Excluding last 3 characters)

