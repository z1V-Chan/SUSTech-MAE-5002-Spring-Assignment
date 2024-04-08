# Define the function
def f(x):
    return x**2 - 1


# Define the secant method
def secant_method(f, x0, x1, iterations,):
    results = []
    for _ in range(iterations):
        # Calculate the next approximation
        h = -f(x1) * (x1 - x0) / (f(x1) - f(x0))
        x2 = x1 + h
        results += [[x1, h]]
        # Update x0 and x1 for the next iteration
        x0, x1 = x1, x2
    results += [[x1]]
    return results


# Apply the secant method
x0 = 3
x1 = 2
iterations = 6
approximations = secant_method(f, x0, x1, iterations)
print(approximations)
