# Problem: Compute the factorial of a number using a while loop.

input_num=int(input("Enter a number: "))

fac_num=1 # factorial starts at 1

i=1
while i<=input_num:
    fac_num*=i # multiply instead of adding 
    i+=1 # increment the counter

print(f"Factorial of {input_num} is {fac_num}")