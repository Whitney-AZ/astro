---
title: Representation and Recoupling Theory of SU(2)
date: 2025-12-27
summary: Some Notes and Comments
category: 笔记
tags: [数学, 物理, 群论, 圈量子引力]
series: 'LQG Basics'
---

These are my notes on representation and recoupling theory of $SU(2)$, which serves as a prerequisite for the ireducible unitary representations of the notorious group $SL(2,\mathbb{C})$. This also make a perfect start for my upcoming notes on LQG, so I hope I can keep this series updated.

### Why do we need $SU(2)$?
As we all know, the 2-dimentional special linear group over $\mathbb{C}$ ($SL(2,\mathbb{C})$) is the double cover of our beloved proper orthochronous lorentz group ($SO^\uparrow(3,1)$), namely 

$$
SL(2,\mathbb{C})/\mathbb{Z}_2 \simeq SO^\uparrow(3,1).
$$

$SL(2,\mathbb{C})$ as the subgroup of $\mathcal{M}(\mathbb{C})$ has the same four basis: $\{\mathbb{I}, \sigma_1, \sigma_2, \sigma_3\}$ where the sigmas are the Pauli Matrices. Therefore, if we consider the definition of $SU(2)$

$$
SU(2) := \left\{u\in SL(2,\mathbb{C}) | u^\dagger u = \mathbb{I}\right\},
$$

we can realize that it is in fact the stablizer of the unit time vector $(1,0,0,0)$. This means, if we are to act $SL(2,\mathbb{C})$ on Minkovski space, $SU(2)$ preserves the time direction and only acts over the space. Other stablizers can be similarly constructed, for example $SU(1,1)$ preserves the $z$ direction and $SL(2,\mathbb{R})$ the $y$ direction.

Wigner's Theorem tells us that we can categorize different types of particles using different representations of $SU(2)$. Mathematicians have proved that there exists a representation space of dimension $n$ of $SU(2)$ for every $n\in\mathbb{N}$. Now since from observing nature we had came to the conclusion that particles have degrees of freedom in the rest frame and that the one-to-one correspondence doesn't carry any information of this phenomena, such a degree of freedom must be reflected in the representation space. That is to say, the number of degrees of freedom of the particle in the rest frame is equal to the dimension of the representation space. This is exactly why we can sort particles by its corresponding representation. As a conclusion, the representations of $SU(2)$ are labeled by half integers $j = 0, 1/2, 1, \cdots$.

But LQG gives another story. We are forced to tackle $SL(2,\mathbb{C})$ in LQG because we are dealing with spacetime itself. However, as we stated above, the stablizer of time is $SU(2)$, meaning although we will have to use $SL(2,\mathbb{C})$ inside a chunk of spacetime, $SU(2)$ is still needed on the boundary of such a chunk. *Breve dicto*, $SU(2)$ handles the kinematics and $SL(2,\mathbb{C})$ handles the dynamics of LQG, and this ends our brief summary.

### Representation Theory of $SU(2)$
As we choose a $j$ representation of $SU(2)$, the space is uniquely determined to be the hilbert space $\mathcal{Q}_j$ with a dimension of $2j + 1$. Therefore, we can choose a canonical basis with $2j + 1$ vectors. How do we choose them? 

By defining $J_i := 1/2\sigma_i$, we can see that it is indeed the generators of $SU(2)$ and satisfy

$$
\left[J_i, J_j\right] = i\epsilon_{ijk}J_k.
$$

Interestingly, they are also the angular momentums, which are observables by definition. Since the momentum along the $z$-axis $J_3$ is a generator of $SU(2)$, it has a natural operation on a state $|\psi\rangle$. Now we choose a state that diagonalizes $J_3$:

$$
J_3|\psi\rangle = m|\psi\rangle
$$

By defining $J_+ := J_1 + iJ_2$ and $J_- := J_1 - iJ_2$, it is explicit to show that

$$
J_3J_+|\psi\rangle = (m + 1)J_+|\psi\rangle
$$

up to a factor. This means the eigenvalue is determined by the basis vector $|\psi\rangle$ and that it can be laddered up and down by the difined ladder operators $J_+$ and $J_-$. Therefore we can label this basis by the eigenvalue and the representation $|j, m\rangle$, with the ladder operators:

$$
\begin{gathered}
    J_+|j, m\rangle = \sqrt{(j-m)(j+m+1)}|j, m + 1\rangle,\\
    J_-|j, m\rangle = \sqrt{(j+m)(j-m+1)}|j, m - 1\rangle.
\end{gathered}
$$

We can calculate the eigenvalue of the following casimir operator (This calculation is justified by Schur's Lemma):

$$
J_1^2+J_2^2+J_3^2 =: J^2|j, m\rangle = j(j+1)|j, m\rangle.
$$

Therefore a state is uniquely determined by $J_3$ and $J^2$. Choosing this basis enables us to treat hard, non-commuting problems into commuting second-grade-mathematics problems.

#### Wigner Matrix
For every group element $g\in SU(2)$ there exist a $(2j+1)\times(2j+1)$ matrix under j representation. This is the exact definition of a representation, which can be written as 

$$
\begin{aligned}
    R(g)|j,n\rangle 
    &= I\cdot R(g)|j,n\rangle \\
    &= \left(\sum_m|j,m\rangle\langle j,m|\right)R(g)|j,n\rangle\\
    &= \left(\sum_m\langle j,m|R(g)|j,n\rangle\right)|j,m\rangle =: \sum_m D^j_{mn}(g)|j,m\rangle.
\end{aligned}
$$

Where we call the $D^j_{mn}(g)$ a **Wigner Matrix**. From this, we can see that a Wigner matrix is nothing but the components of the vector $|j,n\rangle$ under the basis $|j,m\rangle$ after acting $g$ on it. 

From this definition, Peter-Weyl Theorem further tells us that these functions form an orthogonal basis of $L^2(SU(2))$:

$$
\begin{gathered}
    \int_{SU(2)}\mathrm{d}g\overline{D^{j^\prime}_{m^\prime n^\prime}(g)}D^j_{mn}(g) = \frac{1}{2j+1}\delta_{jj^\prime}\delta_{mm^\prime}\delta_{nn^\prime},\\
    L^2(SU(2))\ni f(g) = \sum_{j\in\mathbb{N}/2}\sum_{m=-j}^j\sum_{n=-j}^j f_{mn}^jD^j_{mn}(g).
\end{gathered}
$$

We can induce an isomorphism between an arbitrary wigner matrix $D^j_{mn}(\cdot)$ and the tensor product of two hilbert spaces:

$$
D^j_{mn}(\cdot) \simeq \mathcal{Q}_j \otimes \mathcal{Q}_j^*.
$$

This relation implies that there exists a notable equivalence

$$
L^2(SU(2)) \simeq \bigoplus_{j\in\mathbb{N}/2}\left(\mathcal{Q}_j \otimes \mathcal{Q}_j^*\right).
$$

To my knowledge, this is exactly why we can do quantum things on spin networks.

#### Homogeneous Realization
Now we want to derive the explicit formula for a wigner matrix. Recall that a group element of $SL(2,\mathbb{C})$ is a two by two complex matrix, therefore it has a natural action on $\mathbb{C}^2$. We can construct a vector space of polynomials of these two complex variables $(z_0,z_1)\in \mathbb{C}^2$ homogeneous of degree $2j\in \mathbb{N}$, with a typical element written as 

$$
P(z_0,z_1) = \sum_{k=0}^{2j}a_k z_0^k z_1^{2j-k}.
$$

