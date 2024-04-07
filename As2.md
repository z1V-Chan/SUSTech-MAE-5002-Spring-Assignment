# Assignment 2

<center>Name: 陈子蔚	SID: 12332440</center>

## 1

### a

$$
\begin{align}
11.60&=x_1+10x_2\label{1}\\
11.85&=x_1+15x_2\label{2}\\
12.25&=x_1+20x_2\label{3}\\
\Leftrightarrow \begin{bmatrix}11.60\\11.85\\12.25\end{bmatrix}&=\begin{bmatrix}1 &10\\1&15\\1&20\end{bmatrix}\begin{bmatrix}x_1\\x_2\end{bmatrix}
\end{align}
$$

Denote it as

$$
{\rm y}={\rm A}{\rm x}
$$

### b

- Choose $\eqref{1}$&$\eqref{2}$, ${\rm x}=[11.1,0.05]^\top$
- Choose $\eqref{1}$&$\eqref{3}$, ${\rm x}=[10.95 ,  0.065]^\top$
- Choose $\eqref{2}$&$\eqref{3}$, ${\rm x}=[10.65 ,  0.08]^\top$
Not consistent obviously. There's no particular reason to prefer one of these results over the others without additional context or constraints.

### c

$$
{\rm x}= ({\rm A}^{\top}{\rm A})^{-1}{\rm A}^{\top}y=[10.925,0.065]^\top
$$

Comparing this result with those obtained in part (b), we see that the least squares solution gives a different result from any pair of solutions obtained by considering only two of the three points. This least squares solution is preferred when dealing with an overdetermined system because it takes into account all available data to minimize the MSE.

### 2

### a

$$
A\in \mathbb{R}^{m\times n}\wedge m>n
$$

Thus,
$$
A=Q\begin{bmatrix}R\\0\end{bmatrix}\Leftrightarrow \#H=\#\text{column}=3
$$

### b

$$
\Vert c_1\Vert e_1=[2,0,0,0]^\top
$$

### c

The first column would not change.
$$
[2,0,0,0]^\top
$$

## 3

### 

$$
A\in \mathbb{R}^{m\times n}\wedge m>n
$$

Thus,
$$
A=QR\wedge Q\in\mathbb{R}^{m\times n}\wedge R\in\mathbb{R}^{n\times n}\\
\Leftrightarrow Q^\top Q=I\in\mathbb{R}^{n\times n}
$$
As for the equation,
$$
\begin{align}
Ax&=QRx=b\\
\Leftrightarrow Rx&=Q^{\top}b
\end{align}
$$

## 4

Firstly prove the $\Vert A\Vert_2=\max_i{\sqrt{\lambda_i}}=\max_i{\sigma_i}$,
$$
\Vert A\Vert_2=\sup_{\Vert x\Vert_2=1}{\Vert Ax\Vert_2}
$$
Since $A^{\top}A$ is semi-positive,
$$
\begin{align}
A^{\top}A&=H^\top \text{diag}(\lambda_i) H\\
\text{diag}(\lambda_i) &=
\begin{bmatrix}
\lambda_1 & 0 & \dots & 0 \\
0 & \lambda_2 & \dots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \dots & \lambda_n
\end{bmatrix}
\end{align}
$$
$\forall x \in \{ x | \| x \|_2 = 1 \}$, denote 
$$
Hx = y = (y_1, y_2, ..., y_n)^\top\wedge \| y \|_2 = \| x \|_2 = 1
$$

$$
\| Ax \|_2^2 = x^\top A^\top Ax = (Hx)^\top \text{diag}(\lambda_i) (Hx) = \sum_{i=1}^n \lambda_i y_i^2 \leq \| y \|_2^2\max_{1 \leq i \leq n} \lambda_i=\max_{1 \leq i \leq n} \lambda_i
$$

That is, 
$$
\begin{align}
&\Vert A\Vert_2=\max{\sigma(A)}\\\Leftrightarrow &\Vert A^{-1}\Vert_2=\max{\sigma(A^{-1})}=\max{\frac{1}{\sigma(A)}}=\frac{1}{\min{\sigma(A)}}
\end{align}
$$

## 5

```python
import sympy as sp

# Define the variable and function for Newton's method
x = sp.symbols('x')
f = x**2 - 1

# Compute the derivative of the function
f_prime = sp.diff(f, x)

# Define the Newton's method function
def newtons_method(f, f_prime, initial_guess, iterations):
    approximations = [initial_guess]
    x_n = initial_guess
    for n in range(iterations):
        x_n = x_n - f.subs(x, x_n) / f_prime.subs(x, x_n)
        approximations.append(x_n)
    return approximations

# Apply Newton's method with x0 = 2 for 4 iterations
approximations_positive = newtons_method(f, f_prime, 2, 4)

# Apply Newton's method with x0 = -2 for 4 iterations
approximations_negative = newtons_method(f, f_prime, -2, 4)

(approximations_positive, approximations_negative)

```



The iteration history for the function $f(x)=x^2-1$ using Newton's method with $x_0=2$ for 4 iterations is:

1. $x_1={5\over4}$
2. $x_2={41\over40}$
3. $x_3={3281\over 3280}$
4. $x_3={21523361\over 21523360}$

When we start with $x_0=-2$, the iteration history is:

1. $x_1=-{5\over4}$
2. $x_2=-{41\over40}$
3. $x_3=-{3281\over 3280}$
4. $x_3=-{21523361\over 21523360}$

The sequences converge to the roots of the function, which are $x=1$ and $x=-1$, respectively. The sequences are symmetrical because the function is symmetrical and the initial guesses are symmetrical about the origin.

## 6

```python
import numpy as np

# Define the function
def f(x):
    return x**2 - 1

# Define the secant method
def secant_method(f, x0, x1, iterations):
    results = []
    for _ in range(iterations):
        # Calculate the next approximation
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        results.append(x2)
        # Update x0 and x1 for the next iteration
        x0, x1 = x1, x2
    return results

# Apply the secant method
x0 = 3
x1 = 2
iterations = 6
approximations = secant_method(f, x0, x1, iterations)
approximations
```

After applying the secant method to the function $f(x)=x^2-1$ with starting points $x_0=3$ and $x_1=2$, and performing 6 iterations, the sequence of approximations to the root is:

1. $x_2=1.4$
2. $x_3=1.1176470588235294$
3. $x_4=1.0186915887850467$
4. $x_5=1.0010293360782296$
5. $x_6=1.0000095260322646$
6. $x_7=1.0000000049001991$

As we can see, the approximations are converging towards $1$.

## 7

