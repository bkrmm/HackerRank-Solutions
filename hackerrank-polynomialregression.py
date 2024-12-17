# -*- coding: utf-8 -*-
"""batterylife.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ntc2aBM5JjZm5SAckMtdzUarLxmIrIRf
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures

filepath = "/content/hackerrank-polynomialregression.txt"
with open(filepath, 'r') as file:
  lines = file.readlines()

F,N = map(int, lines[0].split())
print("F: ", F)
print("N: ",N)

F = 2  # Number of features
X_train = np.array([row[:F] for row in traindata])  # Features
y_train = np.array([row[F] for row in traindata])   # Target

# Print the shapes to verify
print("Shape of X_train:", X_train.shape)  # Should be (N, F) -> (100, 2)
print("Shape of y_train:", y_train.shape)  # Should be (N,)   -> (100,)

print(X_train.shape)
print(y_train.shape)
print(xtest.shape)

traindata = [list(map(float, line.split())) for line in lines[1:N+1]]
testdata = [list(map(float, line.split())) for line in lines[N+2:]]

print("First 5 rows of train_data:")
for row in traindata[:5]:
    print(row)
print("\nFirst 5 rows of test_data:")
for row in testdata[:5]:
    print(row)

X_test = np.array(testdata)

X_train_split, X_val_split, y_train_split, y_val_split = train_test_split(
    X_train, y_train, test_size=0.2, random_state=42
)

degree = 3
poly = PolynomialFeatures(degree=degree)
X_train_poly = poly.fit_transform(X_train_split)
X_val_poly = poly.transform(X_val_split)
X_test_poly = poly.transform(X_test)

print("Shape of X_train_poly:", X_train_poly.shape)
print("Shape of X_val_poly:", X_val_poly.shape)
print("Shape of X_test_poly:", X_test_poly.shape)
print("Shape of y_train_split:", y_train_split.shape)
print("Shape of y_val_split:", y_val_split.shape)

model = LinearRegression()
model.fit(X_train_poly, y_train_split)

v_val_pred = model.predict(X_val_poly)
mse = mean_squared_error(y_val_split, v_val_pred)
r2 = r2_score(y_val_split, v_val_pred)
print(f"Validation Mean Squared Error: {mse:.2f}")
print("R2 score: ", r2)

y_test_pred = model.predict(X_test_poly)
print("Predictions for test data:")
for pred in y_test_pred:
    print(f"{pred:.2f}")

# prompt: plot y_test_pred  and accuracy

# Assuming y_test_pred and the accuracy (e.g., R2 score) are already calculated
# as in your provided code.  Replace 'r2' with your actual accuracy metric variable

plt.figure(figsize=(10, 6))
plt.plot(y_test_pred, label="Predicted Values")
plt.xlabel("Data Point Index")
plt.ylabel("Predicted Value")
plt.title(f"Predictions for Test Data (R2 Score: {r2:.2f})")
plt.legend()
plt.grid(True)
plt.show()