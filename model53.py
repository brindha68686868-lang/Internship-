# Machine Learning Model - Linear Regression

from sklearn.linear_model import LinearRegression
import numpy as np

# Training Data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([10, 20, 30, 40, 50])

# Create Model
model = LinearRegression()

# Train Model
model.fit(X, y)

# Predict
new_value = np.array([[6]])
prediction = model.predict(new_value)

print("Prediction for 6:", prediction[0])