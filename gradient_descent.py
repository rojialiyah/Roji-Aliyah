import numpy as np

np.random.seed(42)

X = 2 * np.random.rand(100, 1)

# Create a linear ground truth target with added random noise
noise = np.random.randn(100, 1)
y = 4 * X + 3 + noise
