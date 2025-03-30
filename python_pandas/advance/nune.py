import pandas as pd

data = {
    "Name": ['Ram', 'Shyam', None, 'Dhanshyam', 'Aditi', 'Jagdish', 'Raji', 'Simran'],
    "Age": [25, 30, None, 52, 49, 40, 33, 28],
    "Salary": [50000, 60000, None, 52000, 49000, 70000, 48000, 58000],
    "Performance_Score": [85, 90, None, 92, 88, 95, None, 89]
}

df = pd.DataFrame(data)
print(df)

# isnull()  --> showing all NuN value,  --> bool
print(df.isnull())
print(df.isnull().sum())