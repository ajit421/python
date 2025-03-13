import itertools
from itertools import product, chain, combinations

setOne = {1, 2, 3, 4, 5}
setTwo = {4, 5, 6, 7, 8, 9}

print("Set One:", setOne) # Output: {1, 2, 3, 4, 5}
print("Set Two:", setTwo) # Output: {4, 5, 6, 7, 8, 9}

# Length of a set
print("Length of Set One:", len(setOne)) # Output: 5
print("Length of Set Two:", len(setTwo)) # Output: 6

# Union of two sets
print("Union:", setOne | setTwo) # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9}

# Intersection of two sets
print("Intersection:", setOne & setTwo) # Output: {4, 5}

# Difference between two sets
print("Difference (SetOne - SetTwo):", setOne - setTwo) # Output: {1, 2, 3}
print("Difference (SetTwo - SetOne):", setTwo - setOne) # Output: {8, 9, 6, 7}

# Symmetric difference between two sets
print("Symmetric Difference:", setOne ^ setTwo) # Output: {1, 2, 3, 6, 7, 8, 9}

# Check if an element is in a set
print("Is 1 in Set One:", 1 in setOne) # Output: True
print("Is 1 in Set Two:", 1 in setTwo) # Output: False

# Check subset/superset
print("Set One is Subset of Set Two:", setOne.issubset(setTwo)) # Output: False
print("Set One is Superset of Set Two:", setOne.issuperset(setTwo)) # Output: False

# Check if two sets have a null intersection
print("Null Intersection:", setOne.isdisjoint(setTwo)) # Output: False

# Add and remove elements
setOne.add(6) 
print("After Adding 6:", setOne) # Output: {1, 2, 3, 4, 5, 6}

setOne.remove(6)
print("After Removing 6:", setOne) # Output: {1, 2, 3, 4, 5}

# Cartesian Product
print("Cartesian Product:", set(product(setOne))) # Output: {(1,), (2,), (3,), (4,), (5,)}
print("Cartesian Product:", set(product(setOne, setTwo))) # Output: {(1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9)}

# Power Set function
def power_set(s):
    return set(chain.from_iterable(combinations(s, r) for r in range(len(s)+1))) 

print("Power Set of Set One:", power_set(setOne)) 
# Output: {(), (1,), (2,), (3,), (4,), (5,), (1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5), (1, 2, 3), (1, 2, 4), (1, 2, 5), (1, 3, 4), (1, 3, 5), (1, 4, 5), (2, 3, 4), (2, 3, 5), (2, 4, 5), (3, 4, 5), (1, 2, 3, 4), (1, 2, 3, 5), (1, 2, 4, 5), (1, 3, 4, 5), (2, 3, 4, 5), (1, 2, 3, 4, 5)}


