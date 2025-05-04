---
title: Introduction to Linear Algebra
layout: single
permalink: /linear-algebra/subspaces/
mathjax: true
toc: true
toc_label: "On this page"
toc_sticky: true
---

Notes:
1. What does matrix multiplication with vector mean? How does it transform the vector
2. Linear Functions

## Types of subspaces

### 1. Null subspace

Given $ A \in \mathbb{R}^{m \times n} $, we define null space of $A$ as: $$ N(A) = \{x \in \mathbb{R}^n | Ax = 0\} $$


In easier terms, $N(A)$ is all solutions $x \in \mathbb{R}^n;\ x = \begin{bmatrix}
x_{1}\\
x_{2}\\
\vdots\\
x_{n}\end{bmatrix}$ to equation $Ax = 0$.

Let's look at $N(A)$ from another perspective.
We can represent its rows as row vectors: 
$$A = \begin{pmatrix}
a^T_{1}\\
a^T_{2}\\
a^T_{3}\\
\vdots\\
a^T_{m}
\end{pmatrix} $$
where $a^T_i$ is the transpose of the $i^{th}$ row vector ($a_i$ is a column vector in $\mathbb{R}^n$).<br>
Now, when we compute $Ax$, we are essentially taking the dot product of each row of $A$ with the matrix $x$.

$$Ax = \begin{pmatrix}
a^T_{1} x\\
a^T_{2} x\\
a^T_{3} x\\
\vdots\\
a^T_{m} x\\
\end{pmatrix} = \begin{pmatrix}
a_{1} .x\\
a_{2} .x\\
a_{3} .x\\
\vdots\\
a_{m} .x\\
\end{pmatrix}$$

For $x$ to be in the $N(A)$, we must have $Ax = 0$.This means

$$\begin{pmatrix}
a_{1} .x\\
a_{2} .x\\
a_{3} .x\\
\vdots\\
a_{m} .x\\
\end{pmatrix}= \begin{pmatrix}
0\\
0\\
0\\
\vdots\\
0
\end{pmatrix}$$

This set of equations implies that for every row vector $a_i$ of $A$, the dot product with $x$ must be zero:

$$a_i.x = 0$$
for all $i = 1, 2, 3,..., m $

Since we know that dot product of two vectors being zero means that the vectors are orthogonal to each other. <b>Therefore, a vector $x$ is in the null space of $A$ if and only if $x$ is orthogonal to every row vector of the matrix A.</b>

<b> Notes: </b>

- <b>Row Space :</b> The row space of $A$, denoted as $Row(A)$, is the span of row vectors of $A$. Since $x$ is orthogonal to each row vector, it must also be orthogonal to any linear combinations of the row vectos. This means that $N(A)$ is orthogonal to the entire row space of $A$. We can write this as:

$$N(A) \perp Row(A)$$




\
<b>Example</b>:

$$Ax = \begin{bmatrix}
1 & 1 & 2\\
2 & 1 & 3\\
3 & 1 & 4\\
4 & 1 & 5\end{bmatrix}
\begin{bmatrix}
x_{1}\\
x_{2}\\
x_{3}\end{bmatrix} = \begin{bmatrix}
0\\
0\\
0\\
0\end{bmatrix}$$

The solutions to this system of linear equations are as follow:
$$x = t \begin{bmatrix}
1\\
1\\
-1\end{bmatrix}, t \in \mathbb{R}$$
Here, we can observe that  $x = \begin{bmatrix}
0\\
0\\
0\end{bmatrix}$ is one of the solutions, which means that $N(A)$ is a line passing through origin.


<br>
<br>
<br>
<br>







$$ N(A) = (R({A}^T))^\perp $$







