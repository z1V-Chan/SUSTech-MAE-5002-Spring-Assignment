import numpy as np

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

def QR_factorization(A: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    assert len(A.shape) == 2, "Matrix A must be 2D"
    m, n = A.shape
    Q = np.zeros((m, n))
    R = np.zeros((n, n))
    for j in range(n):
        v = A[:, j]
        for i in range(j):
            R[i, j] = Q[:, i] @ A[:, j]
            v = v - R[i, j] * Q[:, i]
        R[j, j] = np.linalg.norm(v)
        Q[:, j] = v / R[j, j]
    return Q, R


def main():
    A = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1], [-1, 1, 0], [-1, 0, 1], [0, -1, 1]])
    b = np.array([1237, 1941, 2417, 711, 1177, 475])
    Q, R = QR_factorization(A)
    # print(A)
    print(Q)
    print(R)
    # print(np.sum(np.abs((Q @ R) - A)))
    
    x = Ux_equal_b_solution(R, Q.T @ b)
    print(x)


if __name__ == "__main__":
    main()
