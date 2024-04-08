# Define the Newton's method function
def newtons_method(f, df, initial_guess, iterations):
    approximations = []
    x_n = initial_guess
    for n in range(iterations):
        fx = f(x_n)
        dfx = df(x_n)
        approximations += [[x_n, fx, dfx, -fx / dfx]]
        x_n = x_n - fx / dfx
    approximations += [[x_n]]

    return approximations

def main():
    f = lambda x: x**2 - 1
    df = lambda x: 2 * x

    # Apply Newton's method with x0 = 2 for 4 iterations
    approximations_positive = newtons_method(f, df, 2, 4)

    # Apply Newton's method with x0 = -2 for 4 iterations
    approximations_negative = newtons_method(f, df, -2, 4)

    print(approximations_positive)
    print(approximations_negative)

if __name__ == "__main__":
    main()