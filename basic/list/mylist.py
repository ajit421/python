myListOne=[1,2,3]
myListTwo=myListOne
myListOne='namaste'
print(myListOne)
print(myListTwo)

# Output:
# namaste
# [1, 2, 3]


myListOne=[1,2,3]
myListOne[0]=4
print(myListOne)
print(myListTwo)

# Output:
# [4, 2, 3]
# [1, 2, 3]