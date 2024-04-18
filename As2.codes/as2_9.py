import numpy as np


# Define the function we are going to minimize
def f(x):
    return 1 - 0.3 * x * np.exp(-(x**2))
    # return 0.5 - x * np.exp(-(x**2))


# Implementation of the Golden Section Search algorithm
def golden_section_search(f, a, b, tol=3e-3):
    record = []

    tau = (np.sqrt(5) - 1) / 2  # Golden ratio

    # Initial two points and their function values
    x1 = a + (1 - tau) * (b - a)
    x2 = a + tau * (b - a)
    f1 = f(x1)
    f2 = f(x2)

    # Iteration loop
    while (b - a) > tol:
        record += [[x1, f1, x2, f2]]
        if f1 < f2:
            b = x2
            x2 = x1
            f2 = f1
            x1 = a + (1 - tau) * (b - a)
            f1 = f(x1)
        else:
            a = x1
            x1 = x2
            f1 = f2
            x2 = a + tau * (b - a)
            f2 = f(x2)

    # Return the approximated minimum location
    return a, b, record


def main():
    # Using the Golden Section Search algorithm to find the minimum
    initial_interval = [0, 2]
    a, b, record = golden_section_search(f, initial_interval[0], initial_interval[1])

    minimum_location = (a + b) / 2
    minimum_value = f(minimum_location)

    print(minimum_location, minimum_value)
    for iter in record:
        print(iter)


if __name__ == "__main__":
    main()
