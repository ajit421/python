import random

print(random.random())
print(random.randint(1, 10))
print(random.randrange(1, 100))


# Randomly select an element from a list
myList = [1, 2, 3, 4, 5]
print(random.choice(myList))


# Randomly select a sample of elements from a list
print(random.sample(myList, 3))


# Randomly shuffle a list
random.shuffle(myList)
print(myList)


