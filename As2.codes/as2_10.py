import numpy as np

import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams.update(
    {"font.family": "STIXGeneral", "mathtext.fontset": "stix", "font.serif": ["SimSun"]}
)

# Function to plot the optimization path
def plot_optimization_path(function, path, title):
    # Create a grid of points for plotting
    x = np.linspace(-3, 3, 400)
    y = np.linspace(-3, 3, 400)
    X, Y = np.meshgrid(x, y)
    Z = function(X, Y)

    # Plot the function contour
    plt.figure(figsize=(8, 8))
    contour = plt.contour(
        X, Y, Z, levels=np.logspace(-0.5, 3.5, 20, base=10), cmap="jet"
    )
    plt.clabel(contour, inline=1, fontsize=6)

    # Plot the path
    path = np.array(path)
    plt.plot(
        path[:, 0],
        path[:, 1],
        label=title,
        color="r",
        marker=".",
        markersize=4,
        linestyle="--",
    )

    # Annotate start and end points
    plt.scatter(path[0, 0], path[0, 1], color="b", label="Start", zorder=5, s=7)
    plt.scatter(path[-1, 0], path[-1, 1], color="g", label="End", zorder=5, s=7)

    # Set plot labels and title
    plt.title(f"Optimization Path using {title}")
    plt.xlabel("$x$")
    plt.ylabel("$y$")
    plt.legend()
    plt.show()


# Define the Rosenbrock function
def rosenbrock(x, y):
    return 100 * (y - x**2) ** 2 + (1 - x) ** 2


# Define the gradient of the Rosenbrock function
def f_g(x, y):
    # Partial derivative with respect to x
    df_dx = -400 * x * (y - x**2) - 2 * (1 - x)
    # Partial derivative with respect to y
    df_dy = 200 * (y - x**2)
    return np.array([df_dx, df_dy])


# Define the Hessian matrix of the Rosenbrock function
def f_g_g(x, y):
    # Second partial derivative with respect to x
    d2f_dx2 = -400 * (y - x**2) + 800 * x**2 + 2
    # Second mixed partial derivative with respect to x and y
    d2f_dxdy = -400 * x
    # Second partial derivative with respect to y
    d2f_dy2 = 200
    return np.array([[d2f_dx2, d2f_dxdy], [d2f_dxdy, d2f_dy2]])


def steepest_descent_method(
    start_point, alpha=2e-3, tolerance=1e-5, max_iterations=4000
):
    # Starting point
    x, y = start_point

    # Keep track of the iterations and the path taken
    path = [(x, y)]
    for iteration in range(max_iterations):
        # Calculate the gradient at the current point
        grad = f_g(x, y)

        # Check if the magnitude of the gradient is small enough to stop
        if np.linalg.norm(grad) < tolerance:
            break

        # Update the current point by moving in the opposite direction of the gradient
        x, y = x - alpha * grad[0], y - alpha * grad[1]

        # Save the new point
        path.append((x, y))

    # Return the final point and the path
    return (x, y), path


def newton_method(start_point, tolerance=1e-5, max_iterations=4000):
    # Starting point
    x, y = start_point

    # Keep track of the iterations and the path taken
    path = [(x, y)]
    for iteration in range(max_iterations):
        # Calculate the gradient and Hessian at the current point
        grad = f_g(x, y)
        hessian = f_g_g(x, y)

        # Check if the magnitude of the gradient is small enough to stop
        if np.linalg.norm(grad) < tolerance:
            break

        # Calculate the Newton update step
        # Note: We use `np.linalg.inv` to invert the Hessian matrix
        # This could be improved by solving the linear system instead of inverting the Hessian
        delta = np.linalg.solve(hessian, -grad)

        # Update the current point with the Newton step
        x, y = x + delta[0], y + delta[1]

        # Save the new point
        path.append((x, y))

    # Return the final point and the path
    return (x, y), path


def main():
    # Example use of the gradient and Hessian
    # example_point = (0, 0)
    # gradient_at_example = rosenbrock_gradient(*example_point)
    # hessian_at_example = rosenbrock_hessian(*example_point)

    # gradient_at_example, hessian_at_example

    # Initial guess
    initial_point = (-1, -1)

    # Run the steepest descent optimization
    result, path_sd = steepest_descent_method(initial_point)

    # Return the final result and the number of iterations it took

    # Run the Newton optimization
    result_newton, path_newton = newton_method(initial_point)

    # Return the final result and the number of iterations it took

    # Plot the path for Steepest Descent
    plot_optimization_path(rosenbrock, path_sd, "Steepest Descent")

    # Plot the path for Newton's method
    plot_optimization_path(rosenbrock, path_newton, "Newton's method")

    print(result, len(path_sd) )
    print(result_newton, len(path_newton))


if __name__ == "__main__":
    main()
