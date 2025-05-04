---
title: Introduction to Linear Algebra
layout: single
permalink: /linear-algebra/subspaces/
toc: true
toc_label: "On this page"
toc_sticky: true
mathjax: true
---

Notes:
1. What does matrix multiplication with a vector mean? How does it transform the vector?
2. Linear Functions

## Types of subspaces

### 1. Null subspace

Given $A \in \mathbb{R}^{m \times n}$, we define the null space of $A$ as:

$$
N(A) = \{ x \in \mathbb{R}^n \mid Ax = 0 \}
$$

In easier terms, $N(A)$ is all solutions $x \in \mathbb{R}^n$, where:

$$
x = \begin{bmatrix}
x_{1} \\
x_{2} \\
\vdots \\
x_{n}
\end{bmatrix}
$$

such that $Ax = 0$.

Let's look at $N(A)$ from another perspective.  
We can represent its rows as row vectors:

$$
A = \begin{pmatrix}
a^T_{1} \\
a^T_{2} \\
a^T_{3} \\
\vdots \\
a^T_{m}
\end{pmatrix}
$$

where $a^T_i$ is the transpose of the $i^{\text{th}}$ row vector ($a_i$ is a column vector in $\mathbb{R}^n$).  
Now, when we compute $Ax$, we are essentially taking the dot product of each row of $A$ with the vector $x$:

$$
Ax = \begin{pmatrix}
a^T_{1} x \\
a^T_{2} x \\
a^T_{3} x \\
\vdots \\
a^T_{m} x
\end{pmatrix}
= 
\begin{pmatrix}
a_{1} \cdot x \\
a_{2} \cdot x \\
a_{3} \cdot x \\
\vdots \\
a_{m} \cdot x
\end{pmatrix}
$$

For $x$ to be in the null space $N(A)$, we must have $Ax = 0$. This means:

$$
\begin{pmatrix}
a_{1} \cdot x \\
a_{2} \cdot x \\
a_{3} \cdot x \\
\vdots \\
a_{m} \cdot x
\end{pmatrix}
=
\begin{pmatrix}
0 \\
0 \\
0 \\
\vdots \\
0
\end{pmatrix}
$$

This set of equations implies that for every row vector $a_i$ of $A$, the dot product with $x$ must be zero:

$$
a_i \cdot x = 0 \quad \text{for all } i = 1, 2, 3, \dots, m
$$

Since we know that the dot product of two vectors being zero means the vectors are orthogonal to each other,  
**a vector $x$ is in the null space of $A$ if and only if $x$ is orthogonal to every row vector of matrix $A$.**

**Notes:**

- **Row Space:**  
  The row space of $A$, denoted as $\text{Row}(A)$, is the span of the row vectors of $A$.  
  Since $x$ is orthogonal to each row vector, it must also be orthogonal to any linear combination of the row vectors.  
  This means that $N(A)$ is orthogonal to the entire row space of $A$. We can write this as:

  $$
  N(A) \perp \text{Row}(A)
  $$

**Example**:

$$
Ax =
\begin{bmatrix}
1 & 1 & 2 \\
2 & 1 & 3 \\
3 & 1 & 4 \\
4 & 1 & 5
\end{bmatrix}
\begin{bmatrix}
x_{1} \\
x_{2} \\
x_{3}
\end{bmatrix}
=
\begin{bmatrix}
0 \\
0 \\
0 \\
0
\end{bmatrix}
$$

The solutions to this system of linear equations are:

$$
x = t \begin{bmatrix}
1 \\
1 \\
-1
\end{bmatrix}, \quad t \in \mathbb{R}
$$

Here, we can observe that $x = \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix}$ is one of the solutions, which means that $N(A)$ is a line passing through the origin.

<br><br><br>

Finally, we can also write the null space as the orthogonal complement of the row space:

$$
N(A) = \left( R(A^T) \right)^\perp
$$
