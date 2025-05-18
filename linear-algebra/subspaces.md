---
title: Subspaces
layout: single
permalink: /linear-algebra/subspaces/
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

Notes:
1. What does matrix multiplication with a vector mean? How does it transform the vector?
2. Linear Functions
3. Geometrical interpretation of subspaces
## Types of subspaces

### 1. Null subspace

Given $A \in \mathbb{R}^{m \times n}$, we define the null space of $A$ as: 

$$
N(A) = \{ x \in \mathbb{R}^n \mid Ax = 0 \}
$$

In easier terms, $N(A)$ is all solutions $x \in \mathbb{R}^n$, where $$
x = \begin{bmatrix}
x_{1} \\
x_{2} \\
\vdots \\
x_{n}
\end{bmatrix}
$$ such that $Ax = 0$. Let's look at $N(A)$ from another perspective. We can represent its rows as row vectors:

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

Intuitively, we can think of null space of a linear transformation (or a matrix that represents it) as the set of "invisible" input vectors. Let's break it down further:
- <b> Linear Transformation as a mapping: </b> Imagine a linear trasnformation as a function that takes an input vector and transforms it into an output vector in a (possibly) different vector space. Its like a machine that takes something in and spits something else out.
- <b> The Zero Vector as the "Target": </b> The zero vector in the output space is a special "target".
- <b> Null Space - The Inputs that Vanish:</b> The null space is the collection of all the vectors when fed into this "machine" (the linear transformation) get squashed down and become the zero vector in the output space. They are the inputs that the transformation "annihilates" or makes "null".

<b> Example: </b>
1. When we project a 3D object onto a 2D plane, all the information about the object's depth (the component perpendicular to the plane) is lost and maps to zero in that dimension on the 2D plane. The vectors representing that "depth-only" information would be in the null space of the projection transformation.


In essence, the null space tells you about the "loss of information" inherent in the linear transformation. If the null space only contains the zero vector, it means the transformation is "one-to-one" – every distinct input vector gets mapped to a distinct output vector, and no information is lost in that sense. However, if the null space contains non-zero vectors, it means there are different input vectors that end up at the same output vector (specifically, the zero vector), indicating some information is being "lost" or "ignored" by the transformation.
So, the null space is a fundamental concept that helps us understand which input vectors are "invisible" to a particular linear transformation because they get mapped to zero. It reveals the non-uniqueness of inputs that lead to a specific output (especially the zero output) and provides insights into the structure and properties of the linear transformation itself.


**Notes:**

- **Row Space:**  
  The row space of $A$, denoted as $\text{Row}(A)$, is the span of the row vectors of $A$. Since $x$ is orthogonal to each row vector, it must also be orthogonal to any linear combination of the row vectors. This means that $N(A)$ is orthogonal to the entire row space of $A$. We can write this as:

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


