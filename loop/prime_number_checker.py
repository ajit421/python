# Problem: Check if a number is prime.

input_num=int(input("Enter a number if you check prime or not: "))

is_prime=True # assume the number is prime

if input_num>1:
    for i in range(2,input_num):
        if (input_num%i)==0:
            is_prime=False # it is not prime
            break # exit the loop

if is_prime and input_num > 1:
    print(input_num, "is a prime number")
else:
    print(input_num , "is not a prime number")