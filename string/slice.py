chai= 'Masala chai'

# Basic Slicing
print(chai[7:])  # Output: 'chai'
print(chai[7:11])  # Output: 'chai'


print(chai[0:6]) # Output: 'Masala'
slice_chai=chai[:6]
print(slice_chai)  # Output: 'Masala'

first_chai=chai[0]
print(first_chai)  # Output: 'M'

last_chai=chai[-1]
print(last_chai)  # Output: 'i'

# Slice with negative index
print(chai[-3:])  # Output: 'hai'
print(chai[:-3])  # Output: 'Masala ch'

# step size in slicing
print(chai[0:11:2])  # Output: 'Msl hi' (step size is 2)

# Reverse a string
print(chai[::-1])  # Output: 'iahc alasaM

# String Methods
print(chai.upper())  # Output: 'MASALA CHAI'
print(chai.lower())  # Output: 'masala chai'
print(chai.title())  # Output: 'Masala Chai'


print(chai.count('a'))  # Output: 4
print(chai.find('chai')) # Output: 7

print(chai.replace('Masala', 'Kashmiri'))  # Output: 'Kashmiri chai'

# String Concatenation
str1 = 'Masala'
str2 = 'Chai'
print(str1 + ' ' + str2)  # Output: 'Masala Chai'

# string Formatting
Name='Ajit'
drink='chai'
print(f'{Name} loves {drink}')  # Output: 'Ajit loves chai'

# String Multiplication
print('chai ' * 3)  # Output: 'chai chai chai '

