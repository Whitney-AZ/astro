---
title: Representation and Recoupling Theory of SU(2)
date: 2025-12-27
summary: Some Notes and Comments
category: 笔记
tags: [数学, 物理, 群论, 圈量子引力]
series: 'LQG Basics'
---

This are my notes on representation and recoupling theory of $SU(2)$, which serves as a prerequisite for the ireducible unitary representations of the notorious group $SL(2,\mathbb{C})$. This also make a perfect start for my upcoming notes on LQG, so I hope I can keep this series updated.

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

Wigner's Theorem tells us that we can categorize different types of particles using different representations of $SU(2)$. Mathematicians tell us that there exists a representation space of dimension $n$ of $SU(2)$ for every $n\in\mathbb{N}$. Now since nature tells us that particles have degrees of freedom in the rest frame and that the one-to-one correspondence doesn't carry any information of the phenomena, such a degree of freedom must be reflected in the representation space. That is to say, the number of degrees of freedom of the particle in the rest frame is equal to the dimension of the representation space. This is exactly why we can sort particles by its corresponding representation. As a conclusion, the representations of $SU(2)$ are labeled by half integers $j = 0, 1/2, 1, \cdots$.

But LQG tells another story. We are forced to tackle $SL(2,\mathbb{C})$ in LQG because we are dealing with spacetime itself. However, as we stated above, the stablizer of time is $SU(2)$, meaning although we will have to use $SL(2,\mathbb{C})$ inside a chunk of spacetime, $SU(2)$ is still needed on the boundary of such a chunk. *Breve dicto*, $SU(2)$ handles the kinematics and $SL(2,\mathbb{C})$ handles the dynamics of LQG. And this ends our brief summary.

