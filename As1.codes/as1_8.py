import numpy as np
from scipy.linalg import solve
from as1_7 import *

def main():
    # Define the value of alpha
    alpha = np.sqrt(2) / 2

    A_ = np.array([
        [0, 1, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0],  # f2 = f6
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],   # f3 = 10
        [alpha, 0, 0, -1, -alpha, 0, 0, 0, 0, 0, 0, 0, 0], # alpha*f1 = f4 + alpha*f5
        [alpha, 0, 1, 0, alpha, 0, 0, 0, 0, 0, 0, 0, 0],   # alpha*f1 + f3 + alpha*f5 = 0
        [0, 0, 0, -1, 0, 0, 0, 1, 0, 0, 0, 0, 0],  # f4 = f8
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],   # f7 = 0
        [0, 0, 0, 0, alpha, 1, 0, 0, -alpha, -1, 0, 0, 0], # alpha*f5 + f6 = alpha*f9 + f10
        [0, 0, 0, 0, alpha, 0, 1, 0, alpha, 0, 0, 0, 0],   # alpha*f5 + f7 + alpha*f9 = 15
        [0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 1],  # f10 = f13
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],   # f11 = 20
        [0, 0, 0, 0, 0, 0, 0, 1, alpha, 0, 0, -alpha, 0], # f8 + alpha*f9 = alpha*f12
        [0, 0, 0, 0, 0, 0 ,0, 0, alpha, 0, 1, alpha, 0],  # alpha*f9 + f11 + alpha*f12 = 0
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, alpha, 1]  # f13 + alpha*f12 = 0
    ])
    b_ = np.array([ 0., 10.,  0.,  0.,  0.,  0.,  0., 15.,  0., 20.,  0.,  0.,  0.])

    P, L, U = LPU_factorization(A_)
    y = L @ P @ b_

    f = Ux_equal_b_solution(U, y)

    print(f)
    print(A_ @ f - b_)

    # Solve eqautions by scipy
    f = solve(A_, b_)

    # Display the solution for f1 to f13
    print(f)
    print(A_ @ f - b_)

if __name__ == "__main__":
    main()