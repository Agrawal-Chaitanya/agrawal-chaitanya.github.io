---
title: "Understanding the Null Space – From Geometry to ML Applications"
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

## Let's Start with a Question!

- What does it really mean for a matrix to "send" a vector to zero?  
- Why should an ML engineer or a data scientist care about such a concept?

If you're diving into machine learning, understanding the **null space** is more than a textbook exercise. It’s key to understanding how models behave under the hood.


## Too Many Solutions? Welcome to the Null Space

Let’s say you're building a regression model to predict house prices and you are using the following features to train the model:
- <b>Feature 1</b> : Area of the house
- <b>Feature 2</b> : Number of rooms
- <b>Feature 3</b> : 2 * (Area of the house)

You fit your model, get great accuracy and then realize: there are infinitely many sets of weights that yield the exact same predictions. 

What’s going on here? 

This is where the null space enters the picture. It represents the "invisible directions" (vectors) in your feature space, i.e., changes that don’t affect the output at all. In our example, this has happened because of the presence of multicollinearity. <br>
[Check the maths below](#Null-Space-in-Linear-Regression)

## The Black Hole of Matrices: What Gets Pulled In and Lost
Let’s build some intuition before jumping into the math.

When we project a 3D object onto a 2D plane, all the information about the object's depth (the component perpendicular to the plane) is lost and maps to zero in that dimension on the 2D plane. The vectors representing that "depth-only" information would be in the null space of the projection transformation.

A matrix transformation does something similar: it takes a vector and transforms it, but certain directions get completely wiped out. Those are the directions that belong to the null space.

So when we say a vector lies in the null space of a matrix $A$, we mean that applying $A$ to that vector turns it into the zero vector. <br>
[Check the math below](#null-space-of-projection-matrix)

## What Exactly Is the Null Space?

Given matrix $A \in \mathbb{R}^{m \times n}$, we define the null space of $A$ as: 

$$
\mathcal{N}(A) = \{ x \in \mathbb{R}^n \mid Ax = 0 \}
$$

In simple terms:
- It’s the set of all input vectors 𝑥 that the matrix "kills" — sends to the origin.
- It always forms a subspace of $\mathbb{R}^n$
- Its dimension tells you how many directions are "invisible" to your matrix.

> If the null space contains more than just the zero vector, your matrix is not full-rank, and your system of equations (or ML model) has multiple solutions.


Let's look at $N(A)$ from another perspective. We can represent its rows as row vectors:

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

For $x$ to be in the $N(A)$, we must have $Ax = 0$. This means:

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

>  The row space of $A$, denoted as $\text{Row}(A)$, is the span of the row vectors of $A$. Since $x$ is orthogonal to each row vector, it must also be orthogonal to any linear combination of the row vectors. This means that $N(A)$ is orthogonal to the entire row space of $A$. We can write this as: <br>
> \begin{gathered} 
 N(A) \perp \text{Row}(A) 
\end{gathered}


## Zooming into the Math

### Null Space in Linear Regression

Let’s say you’re building a regression model. What if there are multiple equally good solutions?
This usually means your data matrix has a null space.

Now, let's look at the equation to solve for 𝛽:

$$
y=X\beta+ \epsilon
$$

where, <br>
X: features matrix <br>
β: vector of coefficients you want to learn <br>
y: obutput/target vector <br>
ϵ: Noise <br>

Now imagine that there is not just one 𝛽 that gives you a good fit, but infinitely many.
Why? Because the system has redundant information, and part of 𝛽 can move freely without changing the outcome 𝑦. This “freedom” is precisely what the null space captures.

The null space of 𝑋 is the set of all vectors 𝑣 such that:

$$
𝑋𝑣=0
$$

If 𝑣 is in the null space, and you have any solution $𝛽_{0}$, then $𝛽_0+𝑣$ is also a solution. Why? Because:

$$
Xβ=X(𝛽_0+𝑣) = X𝛽_0 + X𝑣 = y+0
$$

This means the null space contains the "directions" along which we can move without affecting predictions.



>If the null space of features matrix is non-trivial (i.e., not just the zero vector), then there is **collinearity** (linearly dependent features).

Now, let's use the house price prediction example discussed above to see how we can calculate those "invisible directions", along which changing the coefficients will not affect predictions. First, let's create a matrix using mock data:

- <b>Feature 1</b> : Area of the house
- <b>Feature 2</b> : Number of rooms
- <b>Feature 3</b> : 2 * (Area of the house)

$$
X = \begin{bmatrix}
100 & 2 & 200 \\
300 & 4 & 600 \\
150 & 1 & 300 \\
450 & 3 & 900
\end{bmatrix} 
$$

For the unique solution of the linear regression to exist, the Gram matrix $X^TX$ in the Normal Equation ($ \hat\beta = (X^TX)^{-1}.(X^Ty)$) should be invertible.
But due to presence of collinearity in the example above, the Gram matrix $X^TX$ is clealy not invertible, which implies multiple solutions exist for $X\beta=y$. **Since, $\beta = \beta_0 + \nu$,
where $\nu \in \mathcal{N}(X)$, any two solutions differ by a vector in the null space of $X$**.

Let's solve the following for $\nu$, to find the null space of $X$:

$$
X\nu=0
$$

i.e., get **non-zero** coefficient directions invisible to the data; moving along those directions does not change predictions.


$$
\mathcal{N}(X) = \left\{ t\begin{bmatrix}
      -2\\
      0\\
      1
      \end{bmatrix} \bigg | t \in \mathbb{R} \right\}
$$

It means any coefficient vector differing by a multiple of $\begin{bmatrix} -2 & 0 & 1 \end{bmatrix}^T$ produces identical predictions.

**Important points to note:**
-  For a linear regression features matrix $X \in \mathbb{R}^{n \times p} $: 

   <center>
   $$
   \mathcal{N}(X) \neq \{0\} \iff \text{columns of $X$ are linearly dependent}
   $$ 
   </center>

   And linear dependence of features is exactly what multicollinearity means.
   So in regression analysis:
   > A non-trivial null space of $X$ implies perfect multicollinearity among the features.
 
-  High correlation $\Leftrightarrow$ numerical instability (not null space). <br>
   It means columns of $X$ are nearly linearly dependent but no exact linear combination equals zero. <br>
   So: <br>
   <center>
   $$
      \mathcal{N}(X) = \{0\}
   $$
   </center>

   For a highly correlated features matrix (feature 1 $\approx$ feature 2), the regression coefficients are highly sensitive to noise and rounding erros in the features. <br>
   The model struggles to decide how to split weight between them. Consequently, even small noise can drastically flip the magnitude or reverse the signs of the coefficients.




### Null Space of Projection Matrix

As discussed in the example above, let's consider a simple projection from 3D to 2D.

$$
T:\mathbb{R}^3 \to \mathbb{R}^2
$$


For example, projecting 3D object onto the $xy$-plane:

$$
T(x,y,z) = (x,y)
$$

This transformation **keeps** the $x$ and $y$ components and <b>drops</b> the $z$ component.
Any point with different $z$-values but the same $x,y$ will map to the same point in 2D:

$$
(1, 2, 5) \mapsto (1,2)
$$

$$
(1, 2, -7) \mapsto (1,2)
$$

All depth information (the $z$-direction) is destroyed by the projection. <br>
Now, this projection matrix, given by the linear transformation $T$, can be written as:

$$
T = \begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0
\end{bmatrix}
$$

This matrix:
- keeps the $x$ and $y$ components
- discard the $z$ component entirely

<br>
Applying it to a vector $(x,y,z)$:

$$
T\begin{bmatrix}
x \\
y \\
z
\end{bmatrix}= \begin{bmatrix} x \\ y \end{bmatrix}
$$

Let's see which vectors get mapped to zero, i.e., the directions that disappear when we project a 3D object onto a 2D plane.

Solve:

$$
T\nu=0
$$

$$
\begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0
\end{bmatrix}

\begin{bmatrix}
x \\
y \\
z
\end{bmatrix}=
\begin{bmatrix}
0 \\
0 \\
\end{bmatrix}
$$

This implies:
- $x=0$
- $y=0$
- $z$ can be *anything*

So the null space is:

$$
\mathcal{N}(T) = \left\{ \begin{bmatrix}
      0\\
      0\\
      z
      \end{bmatrix} \,\bigg|\, z \in \mathbb{R} \right\}
$$

Here, key interpretation is that any moveement purely along the $z$-axis produce no change at all in the projected 2D output. Therefore, $z$-direction is invisible to the matrix $T$.