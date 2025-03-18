# Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.

n=int(input("Enter a number: "))

for i in range(1,11):
    if i==5:
        continue # skip the fifth iteration
    print(n," * ",i, " = ", n*i)