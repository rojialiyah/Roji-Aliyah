import numpy as np

np.random.seed(42)

X = 2 * np.random.rand(100, 1)

# Create a linear ground truth target with added random noise
noise = np.random.randn(100, 1)
y = 4 * X + 3 + noise
#Task 2: Build Gradient Descent From Scratch
def fit_line(X, y, lr, epochs):
  w = 0.0
  b = 0.0
  n = len(X)
    losses = []
#MSE = (1/n) × Σ(actual - predicted)²
for epoch in range(epochs):
  y_pred = w * X + b
  error = y - y_pred
  mse_loss = np.mean(error**2)
  losses.append(mse_loss)


  
