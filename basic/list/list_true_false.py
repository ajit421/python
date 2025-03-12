n=[1,2,3]
m=n

print(n==m)
# Output:
# True

print(n is m)
# Output:  
# True

n=[1,2,3]
m=n[:]
print(n==m)
# Output:
# True

print(n is m)
# Output:
# False

