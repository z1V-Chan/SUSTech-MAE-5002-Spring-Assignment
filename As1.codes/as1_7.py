import numpy as np

def matrix_norm(A: np.ndarray, p: int) -> float:
    assert len(A.shape) == 2, "Matrix A must be 2D"
    assert p in [1, np.inf], "p must be 1, or np.inf"

    if p == 1:
        return np.max(np.sum(np.abs(A), axis=0))
    elif p == np.inf:
        return np.max(np.sum(np.abs(A), axis=1))


def Ux_equal_b_solution(U: np.ndarray, b: np.ndarray) -> np.ndarray:
    assert len(U.shape) == 2, "Matrix U must be 2D"
    assert U.shape[0] == U.shape[1], "Matrix U must be square"
    assert (
        U.shape[0] == b.shape[0]
    ), "Matrix U and vector b must have the same number of rows"

    n = U.shape[0]
    x = np.zeros(n)

    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - U[i, i + 1 :] @ x[i + 1 :]) / U[i, i]

    return x


def LPU_factorization(A: np.ndarray) -> tuple[np.ndarray]:
    assert len(A.shape) == 2, "Matrix A must be 2D"
    assert A.shape[0] == A.shape[1], "Matrix A must be square"

    n = A.shape[0]

    P = np.eye(n)  # Initialize the permutation matrix as the identity matrix
    # L = np.eye(n)  # Initialize the L matrix as the identity matrix
    LP = np.eye(n)  # Initialize the L matrix as the identity matrix
    U = A.copy()  # Copy of the matrix A

    for k in range(0, n - 1):
        P_i = np.eye(n)  # Initialize the permutation matrix as the identity matrix

        # Step 1: Partial pivoting
        pivot = np.argmax(np.abs(U[k:, k])) + k
        if pivot != k:
            P_i[[k, pivot]] = P_i[[pivot, k]]
            P[[k, pivot]] = P[[pivot, k]]
            U[[k, pivot]] = U[[pivot, k]]

        # Step 2: LU factorization
        M = (U[k + 1 :, k] / U[k, k]).reshape((-1, 1))
        P_i[k + 1 :, :] = P_i[k + 1 :, :] - M @ (P_i[k, :]).reshape((1, -1))
        U[k + 1 :, k:] = U[k + 1 :, k:] - M @ (U[k, k:]).reshape((1, -1))

        # Step 3: Store the LP matrix
        LP = P_i @ LP

    # Step 4: Calculate the L matrix, L here is the inverse of L in the slide
    L = LP @ P.T

    return P, L, U


def main():
    A = np.array([[1, 2, 2], [4, 4, 2], [4, 6, 4]], dtype=float)
    P, L, U = LPU_factorization(A)
    print(P, L, U, sep="\n")

    B = np.eye(3)
    A_inv = []

    for i in range(3):
        y = L @ P @ B[i]
        A_inv += [Ux_equal_b_solution(U, y)]

    A_inv = np.array(A_inv).T
    print(A_inv, A_inv @ A, sep="\n")

    cond_1 = matrix_norm(A, 1) * matrix_norm(A_inv, 1)
    cond_inf = matrix_norm(A, np.inf) * matrix_norm(A_inv, np.inf)

    print(cond_1, cond_inf, sep="\n")


if __name__ == "__main__":
    main()