---
title: "Condition Number"
layout: single
permalink: /linear-algebra/condition-number
toc: true
toc_label: "On this page"
toc_sticky: true
toc_icon: "file-alt"
mathjax: true
categories:
  - Mathematics
tags:
 - Linear Algebra
---

## The Steering Wheel Analogy
*Imagine you are driving an old car where the steering wheel is so 'loose' that a tiny twitch of your hand sends your vehicle swerving into the adjacent lane. Or perhaps the opposite case, where the steering wheel is so 'stiff' that turning it halfway barely changes the direction of the car.*
<br>

In both cases, there is a mismatch between your input (the turn of the wheel) and the output (the direction of the car). If a small adjustment leads to an uncontrollable shift, you're dealing with an unstable system. To measure this instability, mathematicians rely on a single, crucial value known as the **condition number**.

## Bridging the Gap: From Cars to Matrices

When we solve a problem, like a linear regression or a system of equations, we assume our data is perfect. But it never is. There’s always a little "noise" or a rounding error (the "twitch" on the steering wheel). 

Let's consider a system of equations $Ax=b$, where $A \in \mathbb{R}^{n \times n}$ is square, invertible matrix and $b$ is non-zero. There is a unique solution $x$, which is non-zero. Now we are pertubing the input $b$ by $\delta b$ to get the following perturbed system:

$$
A \hat{x}=b+\delta{b}
$$

where, 
$\hat{x}=x+\delta{x}$.

Since the error $\delta{x}$ may be negligible or catastrophic depending on the magnitude of $x$, it is more meaningful to work with the relative error $\frac{\lVert \delta{x} \rVert}{\lVert x \rVert}$. Here, we use vector norm $\lVert \cdot \rVert$, to quantify the size of vectors and induced matrix norm to measure matrices. Similarly, the relative size of $\delta b$ with respect to $b$ is given by $\frac{\lVert \delta{b} \rVert}{\lVert b \rVert}$. The relationship between these relative errors is captured by the following inequality, which bounds how perturbations in the input $b$ propagate to the solution $x$.

$$
\frac{\lVert \delta{x} \rVert}{\lVert x \rVert} \leq \lVert A \rVert \lVert A^{-1} \rVert \frac{\lVert \delta{b} \rVert}{\lVert b \rVert}
$$

where, the factor $\lVert A \rVert \lVert A^{-1} \rVert$ is called the **condition number of A, $\kappa(A)$**, i.e., 

$$
\kappa(A) = \lVert A \rVert \lVert A^{-1} \rVert
$$

So, **condition number** ($\kappa$) is essentially the **multiplier of error**.
- **A Low Condition Number (Near 1)**: The steering is precise. A small error in your data ($=\frac{\lVert \delta{b} \rVert}{\lVert b \rVert}$) leads to a small, predictable error ($=\frac{\lVert \delta{x} \rVert}{\lVert x \rVert}$) in your result. Thus if $\kappa(A)$ is not too large, we say that problem is well-conditioned.
- **A High Condition Number (e.g., 1,000+)**: The steering is "loose" and dangerous. A tiny error in your data ($=\frac{\lVert \delta{b} \rVert}{\lVert b \rVert}$) is amplified into a massive error in your result ($=\frac{\lVert \delta{x} \rVert}{\lVert x \rVert}$). In other words, the sytem is very sensitive to perturbations in $b$. The problem is ill-conditioned. 
<br>

**NOTE**: *A condition number of 1 represents the ideal scenario; however, what should be considered “high” or “problematic” depends upon a number of factors like the numerical precision of the computing environment, the amount of error which is tolerable, etc.*

###  Example of an Ill-Conditioned System

Let 
$$A = \begin{bmatrix} 
1000 & 998 \\
999 & 997 
\end{bmatrix}
$$, then 
$$A^{-1} = \begin{bmatrix} 
-498.5 & 499 \\
499.5 & -500 
\end{bmatrix}$$ 


We see that $\kappa(A) = 1.99 \times 10^6$ <br>

Now consider a linear system having $A$ as its coefficient matrix:

$$
\begin{bmatrix} 
1000 & 998\\
999 & 997\\
\end{bmatrix}

\begin{bmatrix} x_1 \\
                x_2
                \end{bmatrix} =
\begin{bmatrix} 1998 \\
                1996
                \end{bmatrix}
$$ 


This is a system of two linear equations: 

$$
1000x_1+998x_2=1998 
$$

$$
999x_1 + 997x_2=1996,
$$


each of which represents a line in the plane. The slopes of the lines are:

$m_1 \approx -1000/998 \approx -1.002004008016$ <br>
$m_2 \approx -999/997 \approx -1.002006018054$ <br>

Thus the solution of the system (point 'a') is the intersection of two nearly parallel lines. Now, a small perturbation in the first line will cause a parallel shift in the line. The new perturbed line is denoted by dashed line. Since both lines are almost parallel, even a small shift in any of the lines cause a drastic shift in the solution from point 'a' to 'b' (as shown in figure below). 


This shows that this system of equations or the given matrix $A$ is ill-conditioned, as also suggested by very high condition number.

<p align="center">
<img src="/linear-algebra/images/condition_number-parallel_lines.jpg">
</p>


## Properties of Condition Number
-  **$\kappa(A) \geq 1$**, for square invertible matrices <br>

    **Proof**: <br>
    From $I = AA^{-1}$, we have: <br>
    $$\lVert I \rVert = \lVert AA^{-1} \rVert \leq \lVert A \rVert \lVert A^{-1} \rVert$$ <br>

    Since $\lVert I \rVert = 1$, it follows that: <br>
    $$\kappa(A) = \lVert A \rVert \lVert A^{-1} \rVert \geq 1$$

- **$\kappa(cA) = \kappa(A)$**, where $c$ is non-zero scalar

    **Proof**: <br>
    $$\kappa(cA) = \lVert cA \rVert \lVert (cA)^{-1} \rVert = \lVert cA \rVert \lVert c^{-1}A^{-1} \rVert$$
    $$= |c| \lVert A \rVert \cdot |c|^{-1} \lVert A^{-1} \rVert = \lVert A \rVert \lVert A^{-1} \rVert = \kappa(A)$$

- $\kappa(A) = \kappa(A^{-1})$

    **Proof**: <br>
    $$\kappa(A^{-1}) = \lVert A^{-1} \rVert \lVert (A^{-1})^{-1} \rVert = \lVert A^{-1} \rVert \lVert A \rVert$$
    $$= \lVert A \rVert \lVert A^{-1} \rVert = \kappa(A)$$

### Decomposition of ill-conditioning (obsidian notes)
### Discuss example 2.2.8 (Fundamnetals of Matrix Computation (FMC))
### Discuss how Cond Numb is subjective Pg 125 & 126 (FMC)



## Geometric Interpretation 

- First derive 2-Norm from max magnification & min magnification
- Explain intuitively the above point
- How Ax transforms the vector x and A-1 undo the transformation. Check book Fundamen
- From circle to ellipse
- Condition Nunber = maxmag(A)/minmag(A)
- Well-conditioned matrix preserves shape

    https://chatgpt.com/s/t_69651ed618c08191be5c0b1311050c3a
    https://chatgpt.com/s/t_69651ee3541481919e45bed6074f8d03
    https://chatgpt.com/s/t_69651eedec1881919c55dccc157e8f6e

- A large condition number means the matrix treats different directions very unevenly.


### Example 2.2.16
### Ill-conditioning due to poor scaling (Pg 130 - FMC)

### Condition Number in Multicollienarity
- Presence of condition number in statsmodel summary

- "weak" directions is the property of feature matrix. Therefore, changes in beta along this "weak" directions causes large swings in beta but with negligible change in prediction
    https://chatgpt.com/s/t_6962af95956c819184f44c467cab4ec2
    https://chatgpt.com/s/t_6962afb41a4c8191a8e4a211928d1ad8

## Appendix

All proofs will be placed in this section, including 'Properties' sections proofs