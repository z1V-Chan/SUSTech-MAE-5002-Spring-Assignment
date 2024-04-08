import numpy as np

# Define the Legendre polynomial L5(x)
def L5(x):
    return (63 * x**5 - 70 * x**3 + 15 * x) / 8

# First derivative of L5(x) for Newton's method
def L5_prime(x):
    return (315 * x**4 - 210 * x**2 + 15) / 8

# Bisection method to find an interval where a zero occurs
def find_zero_interval(func, start, end, num_intervals):
    intervals_idx = np.linspace(start, end, num_intervals + 1)
    intervals = []
    a = intervals_idx[0]
    for b in intervals_idx[1:]:
        if func(a) * func(b) < 0:
            intervals.append((a, b))
        a = b
    return intervals

# Define the Newton's method function
def newton(f, df, a, b, iterations=5):
    x_n = (a + b) / 2
    for _ in range(iterations):
        fx = f(x_n)
        dfx = df(x_n)
        x_n = x_n - fx / dfx

    assert a <= x_n <= b # Ensure the root is within the interval
    return x_n

# Define the Bisection method function
def bisect(f, a, b, iterations=15):
    for _ in range(iterations):
        c = (a + b) / 2
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return c

def main():
    num_intervals = 5

    # We divide the interval [-1, 1] into subintervals to detect zero crossings
    subintervals = find_zero_interval(L5, -1, 1, num_intervals)

    # Now we use bisection on each interval to find a rough estimate of the zeros
    bisect_roots = [bisect(L5, a, b) for a, b in subintervals]

    print(bisect_roots)

    # Refine the estimates using Newton's method
    newton_roots = [newton(L5, L5_prime, a, b) for a, b in subintervals]

    print(newton_roots)

if __name__ == "__main__":
    main()
