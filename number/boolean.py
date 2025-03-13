x, y, z = 4, 5, 6

print(x==y)  # Output: False
print(x!=y)  # Output: True

print(x is y)  # Output: False
print(x is not y)  # Output: True

print(x>y)   # Output: False
print(x<y)   # Output: True

print(x<y<z) # Output: True
print(x<y>z) # Output: False

print(x<y and y<z) # Output: True
print(x<y and y>z) # Output: False


# ⚠️ Be Careful: `&` is a **bitwise AND operator**, not a logical AND.
print(x < y & y < z)  # ❌ Incorrect logic (explained below)
print(x < y & y > z)  # ❌ Incorrect logic


a, b = 9, 10
print(a & b)  
print(a and b)
# Output: 8
# Output: 10

#     1001   (9)
# &   1010   (10)
#   --------------
#     1000   (8)

# Explanation:
# 9 in binary is 1001
# 10 in binary is 1010
# 1001 & 1010 = 1000 = 8
# 9 and 10 are both non-zero, so the `and` operator returns the last value, which is 10
# The `&` operator is a bitwise AND operator, which compares the binary representation of the two numbers.
