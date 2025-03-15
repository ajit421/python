math = int(input("Enter your Math score: "))
physics = int(input("Enter your Physics score: "))
chemistry = int(input("Enter your Chemistry score: "))
biology = int(input("Enter your Biology score: "))
english = int(input("Enter your English score: "))

total_score = math + physics + chemistry + biology + english
percentage = total_score / 5 

if total_score >=501:
    print("Please check your score")
    exit()

print("Total Score:", total_score)
print("Percentage:", percentage)


if percentage >=90 :
    print("Grade: A")

elif 80<=percentage <90:
    print("Grade: B")

elif 70<=percentage <80:
    print("Grade: C")
    
elif 60<=percentage<70:
    print("Grade: D")
else:
    print("Grade: F")
