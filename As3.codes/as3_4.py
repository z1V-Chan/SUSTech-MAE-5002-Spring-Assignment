import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams.update(
    {"font.family": "STIXGeneral", "mathtext.fontset": "stix", "font.serif": ["SimSun"]}
)

def runge_function(t):
    return 1 / (1 + 25 * t**2)

def chebyshev_nodes(n, a, b):
    return 0.5 * (a + b) + 0.5 * (b - a) * np.cos(np.pi * (2 * np.arange(1, n + 1) - 1) / (2 * n))

# Lagrange polynomial interpolation
def polynomial_interpolation(points, x_values):
    x_points, y_points = points
    polynomial = np.zeros_like(x_values)
    n = len(x_points)
    for i in range(n):
        term = y_points[i]
        for j in range(n):
            if i != j:
                term *= (x_values - x_points[j]) / (x_points[i] - x_points[j])
        polynomial += term
    return polynomial

# Parameters for plots
x_range = np.linspace(-1, 1, 400)
y_true = runge_function(x_range)

# Equally spaced points
n5 = 6  # Using 6 points for a degree 5 polynomial
n10 = 11  # Using 11 points for a degree 10 polynomial

x_equally_5 = np.linspace(-1, 1, n5)
y_equally_5 = runge_function(x_equally_5)
p5_equally = polynomial_interpolation((x_equally_5, y_equally_5), x_range)

x_equally_10 = np.linspace(-1, 1, n10)
y_equally_10 = runge_function(x_equally_10)
p10_equally = polynomial_interpolation((x_equally_10, y_equally_10), x_range)

# Chebyshev points
x_chebyshev_5 = chebyshev_nodes(n5, -1, 1)
y_chebyshev_5 = runge_function(x_chebyshev_5)
p5_chebyshev = polynomial_interpolation((x_chebyshev_5, y_chebyshev_5), x_range)

x_chebyshev_10 = chebyshev_nodes(n10, -1, 1)
y_chebyshev_10 = runge_function(x_chebyshev_10)
p10_chebyshev = polynomial_interpolation((x_chebyshev_10, y_chebyshev_10), x_range)

# Plotting
fig, ax = plt.subplots(1, 2, figsize=(12, 6), sharey=True)

ax[0].plot(x_range, y_true, label='$f(t)$', linestyle='-')
ax[0].plot(x_range, p5_equally, label='$p_5(t)$', linestyle='--')
ax[0].plot(x_range, p10_equally, label='$p_{10}(t)$', linestyle=':')
ax[0].set_title('Figure 7.7: Equally Spaced Points')
ax[0].legend()

ax[1].plot(x_range, y_true, label='$f(t)$', linestyle='-')
ax[1].plot(x_range, p5_chebyshev, label='$p_5(t)$', linestyle='--')
ax[1].plot(x_range, p10_chebyshev, label='$p_{10}(t)$', linestyle=':')
ax[1].set_title('Figure 7.8: Chebyshev Points')
ax[1].legend()

plt.show()