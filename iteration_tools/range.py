range(0, 5)

R=range(0, 5)

print(R) # range(0, 5)
print(type(R)) # <class 'range'>
print(list(R)) # [0, 1, 2, 3, 4]

I=iter(R)
print(next(I)) # 0
print(next(I)) # 1
print(next(I)) # 2
print(next(I)) # 3
print(next(I)) # 4
print(next(I)) # StopIteration
print(next(I)) # StopIteration