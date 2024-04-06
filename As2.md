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
\epsilon=\sin(x+h)-\sin(x)
$$

### b

$$
\epsilon_r=\frac{\sin(x+h)-\sin(x)}{\sin(x)}
$$

### c

$$
\begin{align}
\kappa&=\frac{\left|\frac{\sin(x+h)-\sin(x)}{\sin(x)}\right|}{\left|\frac{h}{x}\right|}\\
&=\left|\frac{\frac{\sin(x+h)-\sin(x)}{\sin(x)}}{\frac{h}{x}}
\right|\\
&=\left|{\frac{\sin(x+h)-\sin(x)}{h}}\cdot{\frac{x}{\sin(x)}}
\right|\\
&\simeq\left|{\frac{x\cos(x)}{\sin(x)}}\right|\\
&=\left|{\frac{x}{\tan(x)}}\right|
\end{align}
$$

### d

The problem is highly sensitive where the condition number is extremely large, which typically occurs when $\tan(x)$ is close to $0$.

## 3

### a

<center><img src=".\As1.assets\Figure_1.svg" alt="Figure_1" style="width:75%;" /></center>

### b

<center><img src=".\As1.assets\Figure_2.svg" alt="Figure_2" style="width:75%;" /></center>

## 4

### b

A tolerance such that it is less than the machine epsilon was used, which is a reasonable estimate for when to stop the series summation.

### Output

```log
# x_list: [1, -1, 5, -5, 10, -10, 15, -15, 20, -20]
19
19
37
37
53
53
68
68
83
83
# max order
[(1, 2.7182818284590455, 2.718281828459045, 4.440892098500626e-16),
(-1, 0.36787944117144245, 0.36787944117144233, 1.1102230246251565e-16), 
(5, 148.4131591025766, 148.4131591025766, 0.0), 
(-5, 0.006737946999084642, 0.006737946999085467, 8.248610128269718e-16), 
(10, 22026.465794806714, 22026.465794806718, 3.637978807091713e-12), 
(-10, 4.5399929670419935e-05, 4.5399929762484854e-05, 9.206491905638936e-14), 
(15, 3269017.3724721107, 3269017.3724721107, 0.0), 
(-15, 3.059100025508472e-07, 3.059023205018258e-07, 7.682049021416746e-12), 
(20, 485165195.40979046, 485165195.4097903, 1.7881393432617188e-07), 
(-20, 6.147561848704381e-09, 2.061153622438558e-09, 4.086408226265824e-09)]
# [(x, my_exp, builtin_exp, error)]
```

## 5

$$
\begin{align}
\lVert x\rVert_1&=\sum_{1\le i\le n}{|x_i|}\\
\lVert x\rVert_2&=\sqrt{\sum_{1\le i\le n}{|x_i|^2}}\\
\lVert x\rVert_\infty&=\max_{1\le i\le n}{|x_i|}
\end{align}
$$

Notice that,
$$
\forall i,|x_i|\le\sum_{1\le i\le n}{|x_i|}=\lVert x\rVert_1
$$
As for the 1st inequality,
$$
\begin{align}
\lVert x\rVert_2^2&=\sum_{1\le i\le n}{|x_i|^2}=\sum_{1\le i\le n}{|x_i|\cdot |x_i|}\\
&\le \sum_{1\le i\le n}{|x_i|\cdot \lVert x\rVert_1}=\lVert x\rVert_1\cdot\sum_{1\le i\le n}{|x_i|}=\lVert x\rVert_1^2\\
\end{align}
$$
Since $\lVert x\rVert_2\ge0\wedge\lVert x\rVert_1\ge0$,
$$
\lVert x\rVert_2\le\lVert x\rVert_1
$$
Then,
$$
\begin{align}
\lVert x\rVert_1=\sum_{1\le i\le n}{|x_i|}=x^\top[1,\cdots,1]^\top\le \lVert x\rVert_2\cdot\lVert [1,\cdots,1]^\top\rVert_2=\sqrt{n}\lVert x\rVert_2
\end{align}
$$
Thus, 
$$
\lVert x\rVert_2\le\lVert x\rVert_1\le\sqrt{n}\lVert x\rVert_2
$$
As for the 2nd inequality, suppose $j=\arg{\max_{0\le i \le n}{|x_i|}}$,
$$
\lVert x\rVert_\infty^2=x_j^2\le\sum_{1\le i\le n, i\neq j}{x_i}^2+x_j^2=\sum_{1\le i\le n}{x_i}^2=\lVert x\rVert_2^2
$$
That is,
$$
\lVert x\rVert_\infty \le\lVert x\rVert_2
$$
Notice that,
$$
\forall i,|x_i|\le|x_j|
$$
Then,
$$
\lVert x\rVert_2=\sqrt{\sum_{1\le i\le n}{|x_i|^2}}\le \sqrt{\sum_{1\le i\le n}{|x_j|^2}}=\sqrt{n|x_j|^2}=\sqrt{n}|x_j|=\sqrt{n}\lVert x\rVert_\infty
$$


## 6

### a&b

$$
\left[\begin{array}{ccc|c}
1 & 1 & 0 & 2\\
1 & 2 & 1 & 4\\
1 & 3 & 2 & 6
\end{array}\right]
\xrightarrow{r_2-r_1,r_3-r_1}
\left[\begin{array}{ccc|c}
1 & 1 & 0 & 2\\
0 & 1 & 1 & 2\\
0 & 2 & 2 & 4
\end{array}\right]
\xrightarrow{r_2-\frac{1}{2}r_3}
\left[\begin{array}{ccc|c}
1 & 1 & 0 & 2\\
0 & 1 & 1 & 2\\
0 & 0 & 0 & 0
\end{array}\right]
$$

There are only 2 pivots in  $A$ and $b\in c(A)$ since $x=[1,1,1]^\top$ is a possible solution.

Thus, $A$ is singular and there are infinite solutions to $Ax=b$.

### c

$$
\begin{align}
\lVert A\rVert_1&=\max_{1\le j\le n }{\lVert A_{(:,j)}\rVert_1}=6\\
\lVert A\rVert_\infty&=\max_{1\le i\le n }{\lVert A_{(i,:)}\rVert_1}=6
\end{align}
$$

### d

Since $A$ is singular,
$$
\text{cond}(A)=\infty
$$

## 7

### a

Note that $L$ here is the $L^{-1}$ in the slide.
$$
\begin{align}
U&=L_mP_m\cdots L_1P_1A=LPA\\
P&=P_m\cdots P_1\\
L&=L_mP_m\cdots L_1P_1P^\top
\end{align}
$$

### b

$$
\begin{align}
Ax=b&\Leftrightarrow LPAx=\textcolor{blue}{Ux=LPb}\\
A[x_1, \cdots, x_n]=[b_1,\cdots, b_n]&\Leftrightarrow I=[e_1,\cdots,c_n]=AA^{-1}
\end{align}
$$

### c

$$
\text{cond}(A)=\lVert A\rVert\lVert A^{-1}\rVert
$$

### Output

```log
# P
[[0. 1. 0.]
 [0. 0. 1.]
 [1. 0. 0.]]
# L
[[ 1.    0.    0.  ]
 [-1.    1.    0.  ]
 [ 0.25 -0.5   1.  ]]
# U
[[4.  4.  2. ]
 [0.  2.  2. ]
 [0.  0.  0.5]]
# A_inv
[[ 1.   1.  -1. ]
 [-2.  -1.   1.5]
 [ 2.   0.5 -1. ]]
# A_inv @ A
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
# cond_1
60.0
# cond_inf
63.0
```

## 8

The code of `LPU_factorization` and `Ux_equal_b_solution` in [7](# 7) is also used here. Moreover, the package `scipy` is used to check the correctness.

### Output

```log
[-28.28427125  20.          10.         -30.          14.14213562
  20.           0.         -30.           7.07106781  25.
  20.         -35.35533906  25.        ]
[ 0.00000000e+00  0.00000000e+00 -3.55271368e-15 -1.77635684e-15
  0.00000000e+00  0.00000000e+00  8.88178420e-16  0.00000000e+00
  0.00000000e+00  0.00000000e+00  8.88178420e-16  4.44089210e-15
  7.10542736e-15]
# solutions by the manual program
[-28.28427125  20.          10.         -30.          14.14213562
  20.           0.         -30.           7.07106781  25.
  20.         -35.35533906  25.        ]
[ 0.00000000e+00  0.00000000e+00 -3.55271368e-15 -1.77635684e-15
  0.00000000e+00  0.00000000e+00  8.88178420e-16  0.00000000e+00
  0.00000000e+00  0.00000000e+00  8.88178420e-16  4.44089210e-15
  0.00000000e+00]
# solutions by scipy
```
