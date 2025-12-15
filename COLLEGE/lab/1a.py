import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# --- Step 1: Create Data ---
# X = Hours Studied (Input)
# y = Marks Obtained (Output)
# Reshape(-1, 1) converts the list into a column format required by sklearn
X = np.array([1, 2, 3, 4, 5, 6]).reshape(-1, 1)
y = np.array([15, 28, 42, 50, 65, 78])

# --- Step 2: Create and Train the Model ---
model = LinearRegression()
model.fit(X, y)

# --- Step 3: Make Predictions ---
y_pred = model.predict(X)

# --- Step 4: Display Results ---
print(f"Slope (m): {model.coef_[0]:.2f}")
print(f"Intercept (c): {model.intercept_:.2f}")

# Prediction for someone studying 7 hours
hours = [[7]]
prediction = model.predict(hours)
print(f"Predicted marks for 7 hours of study: {prediction[0]:.2f}")

# --- Step 5: Plotting the Graph ---
plt.scatter(X, y, color='blue', label='Actual Data')  # The dots
plt.plot(X, y_pred, color='red', label='Regression Line') # The line
plt.xlabel('Hours Studied')
plt.ylabel('Marks Obtained')
plt.title('Simple Linear Regression: Hours vs Marks')
plt.legend()
plt.show()