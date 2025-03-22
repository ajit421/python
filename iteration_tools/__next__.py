D= {'a' :1, 'b':2, 'c':3}

for key in D.keys():
    print(key, D[key])

# Output
# a 1
# b 2
# c 3

I= iter(D)
print(I.__next__()) # a
print(I.__next__()) # b
print(I.__next__()) # c
print(I.__next__()) # StopIteration
print(I.__next__()) # StopIteration