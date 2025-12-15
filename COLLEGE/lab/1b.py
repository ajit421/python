# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

print("--- 1. Pandas Library Example ---")
# Creating a simple dataset (dictionary)
data = {
    'Student': ['Amit', 'Priya', 'Rahul', 'Neha'],
    'Marks': [85, 90, 78, 92],
    'Age': [20, 21, 20, 22]
}

# Converting dictionary to a DataFrame (Table)
df = pd.DataFrame(data)
print("Student DataFrame:")
print(df)

print("\n--- 2. Matplotlib Library Example ---")
# Plotting the marks
x = df['Student']
y = df['Marks']

plt.bar(x, y, color='skyblue')
plt.xlabel('Student Name')
plt.ylabel('Marks Obtained')
plt.title('Student Marks Distribution')
plt.show()

print("Graph generated successfully.")