import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.optimize import root
from scipy.optimize import fsolve

from matplotlib import rcParams

rcParams.update(
    {"font.family": "STIXGeneral", "mathtext.fontset": "stix", "font.serif": ["SimSun"]}
)

def a():
    # 定义微分方程
    def ode_system(t, y):
        u, up = y
        return [up, 10 * u**3 + 3 * u + t**2]

    # 定义目标函数，用于寻找合适的初始斜率
    def shooting_function(up0):
        if isinstance(up0, np.ndarray):
            up0 = up0[0]
        sol = solve_ivp(ode_system, [0, 1], [0, up0], t_eval=[1])
        return sol.y[0, -1] - 1

    # 寻找合适的初始斜率
    up0_guess = 1.0  # 初始猜测
    sol = root(shooting_function, up0_guess)
    up0_optimal = sol.x[0]

    # 使用找到的初始斜率求解 ODE
    t_values = np.linspace(0, 1, 100)
    sol = solve_ivp(ode_system, [0, 1], [0, up0_optimal], t_eval=t_values)

    # 绘制结果
    plt.plot(sol.t, sol.y[0], label="Shooting Method")
    plt.xlabel("$t$")
    plt.ylabel("$u(t)$")
    plt.legend()
    plt.show()


def b():
    def finite_difference_non_linear(n, tol=1e-10, max_iter=100):
        h = 1 / (n + 1)
        t_values = np.linspace(0, 1, n + 2)

        # 初始猜测
        u = np.linspace(0, 1, n + 2)

        # 牛顿迭代法
        for _ in range(max_iter):
            # u_old = u.copy()
            F = np.zeros(n)
            J = np.zeros((n, n))

            for i in range(1, n + 1):
                F[i - 1] = (u[i + 1] - 2 * u[i] + u[i - 1]) / h**2 - (
                    10 * u[i] ** 3 + 3 * u[i] + t_values[i] ** 2
                )
                J[i - 1, i - 1] = -2 / h**2 - 30 * u[i] ** 2 - 3
                if i > 1:
                    J[i - 1, i - 2] = 1 / h**2
                if i < n:
                    J[i - 1, i] = 1 / h**2

            # 求解线性方程组 J * delta_u = -F
            delta_u = np.linalg.solve(J, -F)

            # 更新解
            u[1 : n + 1] += delta_u

            # 检查收敛性
            if np.linalg.norm(delta_u) < tol:
                break

        return t_values, u

    # 求解并绘图
    n_values = [1, 3, 7, 15]
    for n in n_values:
        t_values, u = finite_difference_non_linear(n)
        plt.plot(t_values, u, label=f"$n={n}$")

    plt.xlabel("$t$")
    plt.ylabel("$u(t)$")
    plt.legend()
    plt.show()


def c():
    def collocation_method(n):
        # 使用等距节点，包含 n 个节点
        t_values = np.linspace(0, 1, n)


        def func_u(t, x):
            _u = 0
            for i in range(n):
                _u += x[i] * t**i
            return _u

        def func_ddu_dtt(t, x):
            _ddu_dtt = 0
            for i in range(2, n):
                _ddu_dtt += i * (i - 1) * x[i] * t ** (i - 2)
            return _ddu_dtt

        def residuals(x):
            res = (
                [func_u(0, x) - 0]
                + [
                    func_ddu_dtt(t, x)
                    - 10 * func_u(t, x) ** 3
                    - 3 * func_u(t, x)
                    - t**2
                    for t in t_values[1:-1]
                ]
                + [func_u(1, x) - 1]
            )
            return res

        result = root(residuals, np.linspace(0, 1, n))
        x = result.x
        u = [func_u(t, x) for t in t_values]

        return t_values, u

    # 求解并绘图
    n_values = [3, 4, 5, 6]
    for n in n_values:
        t_values, u = collocation_method(n)
        plt.plot(t_values, u, label=f"$n={n}$")

    plt.xlabel("$t$")
    plt.ylabel("$u(t)$")
    plt.legend()
    plt.show()


def main():
    a()
    b()
    c()


if __name__ == "__main__":
    main()
