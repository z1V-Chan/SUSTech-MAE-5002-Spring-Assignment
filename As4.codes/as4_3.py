import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams.update(
    {"font.family": "STIXGeneral", "mathtext.fontset": "stix", "font.serif": ["SimSun"]}
)


# Define the Lorenz system
def lorenz_system(state, t, sigma=10, rho=28, beta=(8 / 3)):
    x, y, z = state
    dx_dt = sigma * (y - x)
    dy_dt = x * (rho - z) - y
    dz_dt = x * y - beta * z
    return np.array([dx_dt, dy_dt, dz_dt])


# Classical fourth-order Runge-Kutta method
def runge_kutta_4(f, y0, t):
    n = len(t)
    y = np.zeros((n, len(y0)))
    y[0] = y0
    dt = t[1] - t[0]
    for i in range(1, n):
        k1 = dt * f(y[i - 1], t[i - 1])
        k2 = dt * f(y[i - 1] + 0.5 * k1, t[i - 1] + 0.5 * dt)
        k3 = dt * f(y[i - 1] + 0.5 * k2, t[i - 1] + 0.5 * dt)
        k4 = dt * f(y[i - 1] + k3, t[i - 1] + dt)
        y[i] = y[i - 1] + (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return y


# Initial conditions and time vector
initial_conditions_a = [0.1, 0.1, 0.0]
initial_conditions_b = [0.1, 0.100001, 0.0]
t = np.arange(0, 100, 0.01)

# Solve the system
trajectory_a = runge_kutta_4(lorenz_system, initial_conditions_a, t)
trajectory_b = runge_kutta_4(lorenz_system, initial_conditions_b, t)

# Plot the trajectories in phase space
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.plot(
    trajectory_a[:, 0],
    trajectory_a[:, 1],
    trajectory_a[:, 2],
    label="Trajectory A",
    linewidth=0.25,
)
ax.plot(
    trajectory_b[:, 0],
    trajectory_b[:, 1],
    trajectory_b[:, 2],
    label="Trajectory B",
    linewidth=0.25,
)
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.set_zlabel("$z$")
ax.legend()
plt.title("Phase Space Trajectories")
plt.show()

# Plot x(t) for t in [95, 100]
plt.figure()
plt.plot(t, trajectory_a[:, 0], label="Trajectory A", color="blue", linewidth=0.7)
plt.plot(t, trajectory_b[:, 0], label="Trajectory B", color="red", linewidth=0.7)
plt.xlim(95, 100)
plt.xlabel("$t$")
plt.ylabel("$x(t)$")
plt.title("$x(t), t \in [95, 100]$")
plt.legend()
plt.show()
