import pandas as pd

data = {
    "Name": ['Ram', 'Shyam', 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish', 'Raji', 'Simran'],
    "Age": [25, 30, 45, 52, 49, 40, 33, 28],
    "Salary": [50000, 60000, 45000, 52000, 49000, 70000, 48000, 58000],
    "Performance_Score": [85, 90, 78, 92, 88, 95, 80, 89]
}

df=pd.DataFrame(data)
print(df)

df.loc[3,'Salary']=7
print(df)

df.loc[6,'Name']="sohan"
print(df)