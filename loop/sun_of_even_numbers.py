# Problem: Calculate the sum of even numbers up to a given number n.

n=int(input("Enter a number"))
count_even=0
sum_even=0

for i in range(1,n+1):
    # print(i, end=" ")

    if i%2==0:
        print(i,"even")
        count_even+=1 # counting even numbers
        sum_even+=i # summing even numbers

print("total even number is: ",count_even)
print("sum of even number is: ", sum_even)
 
