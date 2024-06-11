# Assignment 3

<center>Name: 陈子蔚	SID: 12332440</center>

## 1

Data points $(-1,1),(0,0),(1,1)$.

### a

Since there are 3 data points, $\phi_1(t)=1,\phi_2(t)=x,\phi_3(t)=t^2,\theta=[a,b,c]^\top$.
$$
\begin{align}
\Phi_{i,j}&=\phi_j(i)\\
\Phi&=\begin{bmatrix}
1&-1&1\\
1&0&0\\
1&1&1
\end{bmatrix}\\
\Phi\theta=y
\Leftrightarrow \begin{bmatrix}
1&-1&1\\
1&0&0\\
1&1&1
\end{bmatrix}\begin{bmatrix}
a\\b\\c
\end{bmatrix}&=\begin{bmatrix}
1\\0\\1
\end{bmatrix}
\Leftrightarrow \begin{bmatrix}
a\\b\\c
\end{bmatrix}=\begin{bmatrix}
0\\0\\1
\end{bmatrix}
\end{align}
$$

Thus, $p(t)=\phi(t)^\top\theta=t^2$.

### b

As for Lagrange basis, 
$$
\begin{align}
\phi_i(t)&=\prod_{0\le j\le n \wedge i\neq j}{\frac{t-t_j}{t_i-t_j}}\\
\phi_1(t)&=\frac{t-0}{-1-0}\frac{t-1}{-1-1}=\frac{t(t-1)}{2}\\
\phi_2(t)&=\frac{t+1}{0+1}\frac{t-1}{0-1}=-t^2+1\\
\phi_3(t)&=\frac{t+1}{1+1}\frac{t-0}{1-0}=\frac{t(t+1)}{2}\\
p(t)&=\phi(t)^\top y=t^2
\end{align}
$$

### c

As for Newton basis, $\theta=[a,b,c]^\top$,
$$
\begin{align}
\phi_i(t)&=\prod_{0\le j\le n \wedge i\neq j}{(t-t_j)}\\
\phi_1(t)&=1\\
\phi_2(t)&=t+1\\
\phi_3(t)&=t(t+1)\\
\theta_1&=y_1=1\\
\theta_{i+1}&=\frac{y_{i+1}-p_i(t_{i+1})}{\phi_{i+1}(t_{i+1})}
\end{align}
$$
Thus, $\theta=[1,-1,1]^\top,p(t)=\phi(t)^\top\theta=t^2$.

### d

$p(t)=t^2$  is always obtained.

### e

As for linear interpolating,
$$
p(t)=\begin{cases}
-t,-1\le t<0\\
t,0\le t\le 1
\end{cases}
$$

### f

As for cubic natural spline interpolation,
$$
p(t)=\begin{cases}
p_1(t)=\alpha_1+\alpha_2t+\alpha_3t^2+\alpha_4t^3,-1\le t<0\\
p_2(t)=\beta_1+\beta_2t+\beta_3t^2+\beta_4t^3,0\le t\le 1
\end{cases}
$$
Interpolate the data at the endpoints,
$$
\begin{align}
p_1(-1)=\alpha_1-\alpha_2+\alpha_3-\alpha_4&=1\label{17}\\
p_1(0)=\alpha_1&=0\\
p_2(0)=\beta_1&=0\\
p_2(1)=\beta_1+\beta_2+\beta_3+\beta_4&=1
\end{align}
$$
The first derivative of the interpolating function is continuous at $t=0$,
$$
\frac{\partial p_1(t)}{\partial t}_{|t=0}=\alpha_2=\beta_2=\frac{\partial p_2(t)}{\partial t}_{|t=0}
$$
The second derivative of the interpolating function is continuous at $t=0$,
$$
\frac{\partial^2 p_1(t)}{\partial t^2}_{|t=0}=2\alpha_3=2\beta_3=\frac{\partial^2 p_2(t)}{\partial t^2}_{|t=0}
$$
A natural spline has second derivative equal to zero at the endpoints,
$$
\begin{align}
\frac{\partial^2 p_1(t)}{\partial t^2}_{|t=-1}&=2\alpha_3-6\alpha_4=0\\
\frac{\partial^2 p_2(t)}{\partial t^2}_{|t=1}&=2\beta_3+6\beta_4=0\label{24}
\end{align}
$$
From $\eqref{17}$ to $\eqref{24}$,
$$
[\alpha_1,\alpha_2,\alpha_3,\alpha_4,\beta_1,\beta_2,\beta_3,\beta_4]^\top=\left[0,0,\frac{3}{2},\frac{1}{2},0,0,\frac{3}{2},-\frac{1}{2}\right]^\top
$$
Thus,
$$
p(t)=\begin{cases}
p_1(t)=\frac{1}{2}t^3+\frac{3}{2}t^2,-1\le t<0\\
p_2(t)=-\frac{1}{2}t^3+\frac{3}{2}t^2,0\le t\le 1
\end{cases}
$$

## 2

Notice that $[-1,1]$ is a symmetric interval.
$$
P_1(x)P_2(x)w(x)=(3x^3-x)w(x)
$$
 is odd function when $w(x)$ is even.

That is, when $w(x)$ is even, 
$$
\int_{-1}^1{P_1(x)P_2(x)w(x){\rm d}x}=0
$$

## 3

$$
T_{k}(x)=\cos(k\arccos(t)),t\in[-1,1]
$$

### a

$$
\begin{align}
\int_{-1}^1{\frac{T_i(t)T_j(t)}{\sqrt{1-t^2}}{\rm d}t}
&=\int_{-\pi}^0{\frac{T_i(\cos{x})T_j(\cos{x})}{\sqrt{1-\cos^2{x}}}{\rm d}\cos{x}}\\
&=\int_{-\pi}^0{\frac{\cos{ix}\cos{jx}}{-\sin{x}}(-\sin{x}{\rm d}x)}\\
&=\int_{-\pi}^0{\cos{ix}\cos{jx}{\rm d}x}\\
\end{align}
$$

When $i\neq j$,
$$
\int_{-\pi}^0{\cos{ix}\cos{jx}{\rm d}x}=\int_{-\pi}^0{\frac{1}{2}\left[\cos{(i+j)t}+\cos{(i-j)t}\right]{\rm d}x}=0
$$
When $i=j$,
$$
\begin{align}
\int_{-\pi}^0{\cos{ix}\cos{jx}{\rm d}x}
&=\int_{-\pi}^0{\cos^2{ix}{\rm d}x}\\
&=\int_{-\pi}^0{\frac{1+\cos{2ix}}{2}{\rm d}x}\\
&=\frac{\pi}{2}
\end{align}
$$
Thus,
$$
\int_{-1}^1{\frac{T_i(t)T_j(t)}{\sqrt{1-t^2}}{\rm d}t}=\frac{\pi}{2}\delta_{i,j}
$$



## 4

### Core Code

```python
def chebyshev_nodes(n, a, b):
    return 0.5 * (a + b) + 0.5 * (b - a) * np.cos(np.pi * (2 * np.arange(1, n + 1) - 1) / (2 * n))

# Lagrange polynomial interpolation
def polynomial_interpolation(points, x_values):
    x_points, y_points = points
    polynomial = np.zeros_like(x_values)
    n = len(x_points)
    for i in range(n):
        term = y_points[i]
        for j in range(n):
            if i != j:
                term *= (x_values - x_points[j]) / (x_points[i] - x_points[j])
        polynomial += term
    return polynomial
```

### Result

<img src=".\As3.assets\Figure_1.svg" style="width:95%;" />

## 5

### a

$$
\begin{align}
M(f)&=(b-a)f\left(\frac{a+b}{2}\right)=1\cdot\left(\frac{1}{2}\right)^3=\frac{1}{8}\\
T(f)&=\frac{b-a}{2}(f(a)+f(b))=\frac{1}{2}(0+1)=\frac{1}{2}
\end{align}
$$

### b

$$
\begin{align}
E(f)&=\frac{T(f)-M(f)}{3}=\frac{1}{8}\\
-2E(f)&=-\frac{1}{4}
\end{align}
$$

### c

$$
S(f)=\frac{2M(f)+T(f)}{3}=\frac{1}{4}
$$

### d

Yes, since when $I(f)=S(f)$, $\frac{\partial^3 R(f)}{\partial x^3}=0$, which means the Simpson rule is of degree $3$.

### e

$$
\int_{0}^1{x^3{\rm d}x}=A_0f(x_0)+A_1f(x_1)
$$

There are $4$ parameters.
$$
\begin{align}
\int_0^1{1}&=1=A_0+A_1\\
\int_0^1{x}&=\frac{1}{2}=A_0x_0+A_1x_1\\
\int_0^1{x^2}&=\frac{1}{3}=A_0x_0^2+A_1x_1^2\\
\int_0^1{x^3}&=\frac{1}{4}=A_0x_0^3+A_1x_1^3
\end{align}
$$
The solution is $[A_0,A_1,x_0,x_1]^\top=[\frac{1}{2},\frac{1}{2},\frac{3-\sqrt{3}}{6},\frac{3+\sqrt{3}}{6}]^\top$
$$
G(f)=A_0f(x_0)+A_1f(x_1)=\frac{1}{4}
$$
The result is exact since $G(f)$ is of degree $4-1=3$.

### f

$$
M_2(f)=(0.5-0)f(0.25)+(1-0.5)f(0.75)=0.21875
$$

<div style="page-break-after:always"></div>

## 6

$$
\begin{align}
f(x)&=L_n(x)=\sum_{0\le k\le n}{f(x_k)l_k(x)}\\
I(f)&=\int_a^b{L_n(x){\rm d} x}=\int_a^b{\sum_{0\le k\le n}{f(x_k)l_k(x)}{\rm d} x}\\
&=\sum_{0\le k\le n}{f(x_k)\int_a^b{l_k(x){\rm d}x}}\\
&=\sum_{0\le k\le n}{w_kf(x_k)}
\end{align}
$$

## 7

$$
e=C\cdot h^n\Leftrightarrow\log{e}=\log{C}+n\log{h}
$$

### Output

```bash
# (C, order)
0.7923224542232744 1.9992933732410973
1.587137649897742 1.9995965300241643
0.007343895022866783 4.041227723532598
9.372066198851523e-06 5.99563201077984
```

That is, the dominant term in error of composite midpoint or Trapezoid rules is $O(h^2)$, the dominant term in error of the composite Simpson rule is $O(h^4)$ and the dominant term in error of the composite 3-points Gauss rules is $O(h^6)$.

### Result

<img src=".\As3.assets\Figure_2.svg" style="width:95%;" />

## 8

### 8.12

Average them,
$$
\frac{\frac{f(x+h)-f(x)}{h}+\frac{f(x)-f(x-h)}{h}}{2}=\frac{f(x+h)-f(x-h)}{2h}
$$
By Taylor series,
$$
\begin{align}
f(x+h)=f(x)+f'(x)h+\frac{1}{2}f''(x)h^2+O(h^3)\\
f(x-h)=f(x)-f'(x)h+\frac{1}{2}f''(x)h^2+O(h^3)\\
\end{align}
$$
Thus,
$$
\frac{f(x+h)-f(x-h)}{2h}=f'(x)+O(h^2)
$$
, which is second-order accurate.

### 8.13

$$
\begin{align}
f(x+h)=f(x)+f'(x)h+\frac{1}{2}f''(x)h^2+O(h^3)\\
f(x+2h)=f(x)+2f'(x)h+2f''(x)h^2+O(h^3)
\end{align}
$$

Consider the linear composition $af(x)+bf(x+h)+cf(x+2h)$,
$$
\begin{align}
\frac{b}{2}+2c&=0
\end{align}
$$
Suppose $b=4,c=-1$, then $a=-b-c=-3$ and $b+2c=2$.

That is,
$$
f'(x)=\frac{-3f(x)+4f(x+h)-f(x+2h)}{2h}+O(h^2)
$$
, which is second-order accurate.
