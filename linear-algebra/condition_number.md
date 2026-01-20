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
\begin{bmatrix} b_1 \\
                b_2
                \end{bmatrix}
$$ 


This is a system of two linear equations: 

$$
1000x_1+998x_2=b_1 
$$

$$
999x_1 + 997x_2=b_2,
$$


each of which represents a line in the plane. The slopes of the lines are:

$m_1 \approx -1000/998 \approx -1.002004008016$ <br>
$m_2 \approx -999/997 \approx -1.002006018054$ <br>

Thus the solution of the system (point 'a') is the intersection of two nearly parallel lines. Now, let's make a small perturbation in the first line, which will cause a parallel shift in the line. The new perturbed line is denoted by dashed line. Since both lines are almost parallel, even a small shift in any of the lines cause a drastic shift in the solution from point 'a' to 'b' (as shown in figure below). 


This shows that this system of equations or the given matrix $A$ is ill-conditioned, as also suggested by very high condition number.

<p align="center">
<img src="/linear-algebra/images/condition_number-parallel_lines.jpg">
</p>

The geometric picture above explains *what* goes wrong, but not yet *why* it goes wrong at a deeper level.  
The instability does not arise merely because the two lines are almost parallel; near-parallelism is only a **geometric symptom** of a more fundamental property of the matrix \(A\).

Specifically, an ill-conditioned matrix acts very differently on different directions in the input space.  
Some directions are strongly amplified, while others are barely changed. When the right-hand side \(b\) is perturbed along these sensitive directions, the solution \(x\) can change dramatically, even if the perturbation itself is small.

To make this precise, we now shift our viewpoint from intersecting lines to how a matrix transforms vectors in different directions.


> A large condition number means the matrix treats different directions very unevenly.

In other words, a matrix has a large condition number if it stretches unit vectors by very different amounts depending on their direction, strongly amplifying some directions while almost annihilating others.

Let's use the above matrix $A$ to explain aforementioned statement:

For 
$$A = \begin{bmatrix} 
1000 & 998 \\
999 & 997 
\end{bmatrix}
$$
- Direction of $x: (1, 1)$

$$
A(1, 1) = (1998, 1996) \implies \text{ large magnitude}
$$

- Direction of $x: (1, -1)$

$$
A(1, -1) = (2, 2) \implies \text{ small magnitude}
$$

**Here, we see that same length inputs have been transformed to wildly different outputs based on the direction of the input.**

<br>
Now, if we look at the same problem from a different perspective, i.e., how perturbations in different directions of $b$ affect the solution $x$.

We can check the same using following equation:

$$
\delta{x} = A^{-1}\delta{b}
$$

For:
- $\delta{b} = (1, 1) \implies \delta{x} = \begin{bmatrix} 0.5 \\ -0.5 \end{bmatrix} \implies \lVert \delta{x} \rVert \approx 0.71 \implies \text{least change}$
- $\delta{b} = (1, 0) \implies \delta{x} = \begin{bmatrix} -498.5 \\ 499.5 \end{bmatrix} \implies \lVert \delta{x} \rVert \approx 705 \implies \text{large change}$
- $\delta{b} = (1, -1) \implies \delta{x} = \begin{bmatrix} -997.5 \\ 999.5 \end{bmatrix} \implies \lVert \delta{x} \rVert \approx 1412 \implies \text{largest change}$

We observe that the same directions identified above yield the largest and smallest perturbations in $x$ for a given magnitude of perturbation in $b$.

***NOTE**: We will cover matrix sensitivity analysis in detail in a separate post where we will discuss how these directions of least & large impact on $x$ are calculated.*

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
### Discuss how Cond Numb is subjective Pg 125 & 126 (FMC)


So far we have covered blah blah, but let's look at the geometry of the transformation and also ways to calculate condition number using max & min magnification

## Geometric Interpretation 

A deeper understanding of the condition number emerges when we view a matrix as a geometric transformation.

A matrix stretches unit vectors by different amounts depending on their direction, leading to maximum and minimum magnifications.<br>
The condition number precisely measures this disparity. It is the ratio between the largest and smallest magnifications induced by the matrix.

Now, to visualize these magnifications, let's understand how a matrix transforms a unit circle and what it becomes?

Let $A \in \mathbb{R}^{n \times n}$ be an invertible matrix. Consider the set 

$$\{x \in \mathbb{R}^n\mid \lVert x \rVert_2=1  \}$$

For $n=2$, we get a unit circle with center at $\begin{pmatrix} 0 \\ 0\end{pmatrix}$ and radius $1$.

Then, the above set of $x$ can be represented as:

$$
\left\{ \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} \in \mathbb{R^2}: x_1^2 + x_2^2=1 \right\} \text{, (} \because x_1^2 + x_2^2 = \lVert x \rVert_2^2 = \lVert x \rVert_2 = 1 \text{)}
$$

On applying matrix $A$ to $x$, we get:

$$
\begin{align*}
&\Rightarrow A \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} = \begin{pmatrix} y_1 \\ y_2 \end{pmatrix} \text{, such that} \begin{pmatrix} y_1 \\ y_2 \end{pmatrix} \in \mathbb{R}^2 \\
&\Rightarrow \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} = A^{-1} \begin{pmatrix} y_1 \\ y_2 \end{pmatrix} = B \begin{pmatrix} y_1 \\ y_2 \end{pmatrix} \text{, where } B = A^{-1} \\
&\Rightarrow \begin{pmatrix} x_1 \\ x_2 \end{pmatrix}= B \begin{pmatrix} y_1 \\ y_2 \end{pmatrix} = \begin{bmatrix} \cdots  b_1^T \cdots \\ \cdots b_2^T \cdots \end{bmatrix} 
\begin{pmatrix} y_1 \\ y_2 \end{pmatrix} \\
&\Rightarrow x_1 = b_1^Ty  \text{ & } x_2 = b_2^Ty
\end{align*}
$$

Since we know: $ x_1^2 + x_2^2 = 1$

$$
\begin{align*}
&\Rightarrow (b_1^Ty)^2 + (b_2^Ty)^2 = 1 \text{ } \cdots \rightarrow (1)
\end{align*}
$$

As we already know,

$$
\begin{align*}
&b_1^T = \begin{pmatrix} b_{11} & b_{12} \end{pmatrix} \\
&b_2^T = \begin{pmatrix} b_{21} & b_{22} \end{pmatrix} \\
&y = \begin{pmatrix} y_{1} \\ y_{2} \end{pmatrix}
\end{align*}
$$

Putting values of $b_1^T \text{, } b_2^T \text{, }y$ in the equation $\(1)$ described above, we get:

$$
\begin{align*}
&\Rightarrow (b_{11}y_1 + b_{12}y_2)^2 + (b_{21}y_1 + b_{22}y_2)^2 = 1 \\
&\Rightarrow y_1^2(b_{11}^2+b_{21}^2) + y_2^2(b_{12}^2+b_{22}^2) + 2y_1y_2(b_{11}b_{12}+b_{21}b_{22}) = 1 \\
&\Rightarrow y_1^2\beta_1 + y_2^2\beta_2 + 2y_1y_2\alpha = 1 \text{ , where } \alpha \text{ , } \beta_1 \text{ , } \beta_2 \text{ are constants}
\end{align*}
$$

If you notice the above equation, it is an equation of an ellipse in $\mathbb{R}^2$. <br>
It means a unit circle is getting transformed to an ellipse on the application of matrix $A$.

<p align="center">
<img src="/linear-algebra/images/condition_number-circle_2_ellipse.jpg" style="width: 50%;">
</p>

### Introducing Maximum and Minimum Magnification

Once the unit circle is transformed into an ellipse, an important geometric fact becomes visible: **not all directions are stretched equally**.

Some unit vectors are stretched the most, landing at the tips of the ellipse’s **major axis**, while others are stretched the least, landing at the ends of the **minor axis**.

These two extreme stretch factors play a central role:
- The **maximum magnification** is the **largest length** attained by $\lVert Ax \rVert$ among all unit vector $\lVert x \rVert_2 =1$
- The **minimum magnification** is the **smallest length** attained by $\lVert Ax \rVert$ among all unit vector $\lVert x \rVert_2 =1$

**Geometrically, they correspond exactly to the lengths of the major and minor semi-axes of the ellipse produced by applying $A$ to the unit circle.**

Given below is the mathematical definitions of maximum & minimum magnifications of $A \in \mathbb{R}^{n \times n}$ :

- **Maximum Magnification**:

    $$
    \begin{equation}
    maxmag(A) = \max_{\mathbf{x} \neq \mathbf{0}} \frac{\|A\mathbf{x}\|_2}{\|\mathbf{x}\|_2} = \max_{\|\mathbf{x}\|_2=1} \|A\mathbf{x}\|_2 = \|A\|_2
    \end{equation}
    $$

    corresponding to the length of the major semi-axis of the ellipse. <br>
    Since matrix 2-norm is the largest factor by which a matrix $A$ can stretch a unit vector, maximum magnification is nothing but the induced matrix norm $\lVert A \rVert_2$

- **Minimum Magnification**: 

    $$
    \begin{equation}
    minmag(A) = \min_{\mathbf{x} \neq \mathbf{0}} \frac{\|A\mathbf{x}\|_2}{\|\mathbf{x}\|_2} = \min_{\|\mathbf{x}\|_2=1} \|A\mathbf{x}\|_2
    \end{equation}
    $$

    corresponding to the length of the minor semi-axis of the ellipse.



Next: https://chatgpt.com/s/t_696fe15315588191a763c9b8704dee89



“To make this concrete, consider how a matrix transforms the unit circle…”

Consider a unit cirecle, ...... Check whether some information from either of the two options given below can be used.
First we will show transformation of circle to ellipse. Then we will introduce magnifications based condition number and then proof of the magnification

Option 2 (slightly more visual, prepares circle → ellipse)

Geometrically, a matrix does not distort all directions equally.
When a matrix acts on unit-length vectors, some directions are stretched the most (maximum magnification) while others are stretched the least (minimum magnification).
The condition number quantifies how uneven this directional stretching is, linking algebraic sensitivity directly to geometric distortion.

Option 3 (explicitly sets up the unit circle)

To understand why a matrix amplifies errors, it helps to study how it transforms geometry.
When a matrix acts on the unit circle, it stretches it into an ellipse, whose longest and shortest axes correspond to the maximum and minimum magnifications of the transformation.
The condition number is simply the ratio of these two magnifications.


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