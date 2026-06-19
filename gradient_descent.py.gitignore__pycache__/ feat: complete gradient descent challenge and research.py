import numpy as np
import matplotlib.pyplot as plt

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
#gradient of loss with respect to w
  dw = (2/n) * np.sum(error *x)
#gradient of loss wrt b
  db = (2/n) * np.sum(error)
  w = w - lr * dw
  b = b - lr * db

return losses
#Task 3: Experiment & Plot the Loss Journey
epochs = 100
alpha_A = 0.001
Loss_A = fit_line(X, y, alpha_A, epochs)
alpha_B = 0.1
Loss_B = fit_line(X, y, alpha_B, epochs)
alpha_C = 0.9
Loss_C = fit_line(X, y, alpha_C, epochs)

plt.figure(figsize=(10, 6))
plt.plot(range(epochs),Loss_A, color="red", label="f'Alpha= {alpha_A}")
plt.plot(range(epochs),Loss_B, color="blue", label="f'Alpha= {alpha_B}")
plt.plot(range(epochs),Loss_C, color="Yellow", label="f'Alpha= {alpha_C}")
plt.xlabel("Epoch")
plt.ylabel("MSE Loss")
plt.title("Epoch vs MSE Loss")
plt.legend()
plt.grid(True)
plt.show()

plt.savefig("loss_convergence.png")
print("Chart saved successfully")




  


  


  
