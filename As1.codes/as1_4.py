import numpy as np

# Redefine the function to compute the exponential in case the environment has been reset

tolerance = np.finfo(float).eps

def compute_exponential(x, tolerance):
    term = 1  # The first term in the series
    sum_e_x = 1  # Initialize sum of series
    n = 1  # Counter for factorial and term power

    # Add terms until the next term is smaller than the tolerance
    while abs(term) > tolerance:
        term *= x / n
        sum_e_x += term
        n += 1
    
    print(n)

    return sum_e_x


# Define the x values to test
x_values = [1, -1, 5, -5, 10, -10, 15, -15, 20, -20]

# Calculate the exponential using our function and the built-in exp function
results = []
for x in x_values:
    my_exp = compute_exponential(x, tolerance)
    builtin_exp = np.exp(x)
    error = abs(my_exp - builtin_exp)
    results.append((x, my_exp, builtin_exp, error))

print(results)
