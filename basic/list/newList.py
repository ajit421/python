l1=[1,2,3]
l2=l1
print(l1,l2)
# Output:
# [1, 2, 3] [1, 2, 3]

l1[0]=4
print(l1,l2)
# Output:
# [4, 2, 3] [4, 2, 3]

p1=[1,2,3]
p2=p1
p2=[1,2,3]
print(p1,p2)
# Output:
# [1, 2, 3] [1, 2, 3]

p1[0]=4
print(p1,p2)
# Output:
# [4, 2, 3] [1, 2, 3]
