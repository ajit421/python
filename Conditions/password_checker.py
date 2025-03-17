password=input("Enter your password: ")
passlen=len(password)
# print(passlen)

if passlen <6:
    passchar="Weak"
elif passlen<=10:
    passchar="Medium"
else :
    passchar="Strong"

print (passchar)
