import numpy as np
from scipy.integrate import quad, fixed_quad
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams.update(
    {"font.family": "STIXGeneral", "mathtext.fontset": "stix", "font.serif": ["SimSun"]}
)


# Define the function to integrate
def f(x):
    return np.exp(x)


# Exact value of the integral calculated using numerical integration
exact_value = quad(f, 0, 3)[0]

# Define ranges for h
hs = np.array([2**-i for i in range(1, 11)])

# Initialize lists to store results
midpoint_errors = []
trapezoid_errors = []
simpson_errors = []
gauss_errors = []

# Calculate the integral using various numerical methods
for h in hs:
    # Number of intervals
    n = int(3 / h)
    xs = np.linspace(0, 3, n + 1)

    # Midpoint Rule
    midpoints = (xs[:-1] + xs[1:]) / 2
    midpoint_integral = np.sum(f(midpoints) * h)
    midpoint_error = np.abs(midpoint_integral - exact_value)
    midpoint_errors.append(midpoint_error)

    # Trapezoidal Rule
    fxs = f(xs)
    fxs[0] /= 2
    fxs[-1] /= 2
    trapezoid_integral = np.sum(fxs) * h
    trapezoid_error = np.abs(trapezoid_integral - exact_value)
    trapezoid_errors.append(trapezoid_error)

    # Simpson's Rule
    if n % 2 == 1:  # Ensure even number of segments for Simpson's rule
        assert False
    # xs = np.linspace(0, 3, n + 1)
    simpson_integral = (2 * midpoint_integral + trapezoid_integral) / 3
    simpson_error = np.abs(simpson_integral - exact_value)
    simpson_errors.append(simpson_error)

    # Gauss Quadrature
    gauss_integral = np.sum([fixed_quad(f, xs[i], xs[i + 1], n=3)[0] for i in range(n)])
    gauss_error = np.abs(gauss_integral - exact_value)
    gauss_errors.append(gauss_error)

# Plotting the results
plt.figure(figsize=(10, 6))
plt.loglog(hs, midpoint_errors, "o-", label="Midpoint", base = 2)
plt.loglog(hs, trapezoid_errors, "s-", label="Trapezoid", base = 2)
plt.loglog(hs, simpson_errors, "^-", label="Simpson", base = 2)
plt.loglog(hs, gauss_errors, "x-", label="Gauss", base = 2)
plt.xlabel("$h$")
plt.ylabel("Error")
plt.title("Error Analysis of Numerical Integration Methods")
plt.legend()
plt.grid(True, which="both", ls="--")
plt.show()


# Fit the error as a function of h
def fit_errors(hs, errors):
    log_hs = np.log(hs)
    log_errors = np.log(errors)
    poly = np.polyfit(log_hs, log_errors, 1)
    return np.exp(poly[1]), poly[0]

# Calculate C and order for each method

midpoint_C, midpoint_order = fit_errors(hs, midpoint_errors)
trapezoid_C, trapezoid_order = fit_errors(hs, trapezoid_errors)
simpson_C, simpson_order = fit_errors(hs, simpson_errors)

# Remove zero errors for Gauss Quadrature
gauss_errors = np.array(gauss_errors)
hs = hs[gauss_errors > 2**-45]
gauss_errors = gauss_errors[gauss_errors > 2**-45]

gauss_C, gauss_order = fit_errors(hs, gauss_errors)

# Display the fitting results
print(midpoint_C, midpoint_order)
print(trapezoid_C, trapezoid_order)
print(simpson_C, simpson_order)
print(gauss_C, gauss_order)
