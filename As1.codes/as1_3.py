import numpy as np
import matplotlib.pyplot as plt

from matplotlib import rcParams

rcParams.update(
    {"font.family": "STIXGeneral", "mathtext.fontset": "stix", "font.serif": ["SimSun"]}
)


# Define the function to approximate the derivative
def approximate_derivative(f, x, h):
    # return (f(x + h) - f(x)) / h
    return (f(x + h) - f(x - h)) / (2 * h)


# Define the function of which we are finding the derivative
def func(x):
    return np.cos(x)


# Exact derivative of the function
def exact_derivative(x):
    return -np.sin(x)


# The point at which we are computing the derivative
x0 = 1

# Array of h values
h_values = np.logspace(-16, 0, 17)

# Initialize arrays to store the errors
absolute_errors = []

# Compute the error for each h
for h in h_values:
    approx_deriv = approximate_derivative(func, x0, h)
    true_deriv = exact_derivative(x0)
    absolute_error = np.abs(approx_deriv - true_deriv)
    relative_error = absolute_error / np.abs(true_deriv)

    absolute_errors.append(absolute_error)

# Plot the magnitude of the errors
plt.figure(figsize=(5, 4))

# Absolute error plot
plt.loglog(h_values, absolute_errors, "-o", label=r"$\left|\epsilon\right|$")

# Rule of thumb for h
eps = np.finfo(float).eps
h_optimal = np.sqrt(eps)

# Mark the optimal h on the plot
plt.axvline(
    h_optimal,
    color="r",
    linestyle="--",
    label=r"$\sqrt{\epsilon_\text{mach}}=$%.1e" % h_optimal,
)

plt.xlabel("$h$")
plt.ylabel("Magnitude of Error")
plt.title("Error in Approximation of $\cos(x)$ Derivative")
plt.legend()
# plt.grid(True, which="both", ls="--")

# Show the minimum value for the magnitude of the error
min_error = min(absolute_errors)
min_error_h = h_values[np.argmin(absolute_errors)]

# plt.savefig("../As1.assets/Figure_1.svg")
plt.savefig("../As1.assets/Figure_2.svg")
plt.show()


print(min_error, min_error_h, h_optimal)