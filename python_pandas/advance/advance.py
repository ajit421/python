import pandas as pd

data = {
    "Name": ['Ram', 'Shyam', 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish', 'Raji', 'Simran'],
    "Age": [25, 30, 45, 52, 49, 40, 33, 28],
    "Salary": [50000, 60000, 45000, 52000, 49000, 70000, 48000, 58000],
    "Performance_Score": [85, 90, 78, 92, 88, 95, 80, 89]
}

df=pd.DataFrame(data)
print(df)

# create a new colume
df["Bonus"]=df['Salary'] *0.7 
print(df)

# replace a execting value
df['Bonus']=df['Salary']
print(df)

df.insert(0, "Employee ID", [10,20,30,40,50,60,70,80])
print(df)

