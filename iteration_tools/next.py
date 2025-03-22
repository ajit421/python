myList = [1, 2, 3, 4]

i=iter(myList)
print(next(i))
print(next(i))
print(next(i)) 
print(next(i))
print(next(i)) # StopIteration exception

# Output
# 1
# 2
# 3
# 4

