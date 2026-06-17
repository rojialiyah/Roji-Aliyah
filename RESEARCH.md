EPOCH lookat every single piece of data in a training set at once. One complete epoch means the model has looked at every single piece of data in your training dataset exactly one time.
Learning rate is a hyper parameter that controls how much the model's weight are adjusted during training.

When the Learning Rate is Too High (> 1.0): the model overshoot the optimal weight. The curve diverges and turns towards infinity

When the Learning Rate is Too Small (< 0.00001): the training become so slow and The loss curve will look almost completely flat, with a microscopic downward slope

What does "convex" mean? If for any two points within its domain, the line segment connecting the two points lie below or on the graph of the function.

What does the error surface look like?With one weight (one feature): The error surface looks like a perfect, 2D U-shaped curve (a parabola).

With two weights (two features): It looks exactly like a smooth, perfectly round mixing bowl (a 3D paraboloid).

With many weights: It becomes a multi-dimensional bowl (a hyper-paraboloid). We cannot visualize it in 3D space, but the mathematical properties remain exactly the same.

Why Convexity Guarantees Finding the Global Minimum? Convexity guarantees that Gradient Descent will find the global minimum for a very simple reason: a convex surface only has one bottom. Because the MSE error surface for linear regression has no dents,there are absolutely zero local minima for the algorithm to get trapped in.

