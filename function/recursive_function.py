# Problem: Create a recursive function to calculate the factorial of a number.
number=4

def factorial(n):
    if n==0:
        return 1
    else:
        return(n)*factorial(n-1)

print(factorial(number))