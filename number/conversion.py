# Decimal to Other Bases
# Binary: 0b
# Octal: 0o
# Hex: 0x

# Other Bases to Decimal
# Binary: 2
# Octal: 8
# Hex: 16

print(0o100)  # Output: 64
print(0x40)   # Output: 64
print(0b1000000)  # Output: 64


# Decimal to Other Bases
print(bin(64)) # Decimal to Binary → 0b1000000
print(oct(64)) # Decimal to Octal → 0o100
print(hex(64)) # Decimal to Hex → 0x40

# Other Bases to Decimal (int() function)
print(int('1000000', 2))  # Binary to Decimal → 64
print(int('100', 8))      # Octal to Decimal → 64
print(int('40', 16))      # Hex to Decimal → 64

