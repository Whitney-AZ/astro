---
title: The Connection Formulation of General Relativity
date: 2026-04-04
summary: From a constrained BF theory, we derive the connection formulation of general relativity using dirac's constraint analysis method.
category: 笔记
tags: [数学, 物理, 广义相对论]
pdf: true
---

It has long been known that general relativity can be formulated by applying a constraint on the BF theory. Plebanski successfully obtained the Riemannian action:
$$
S[B, \omega, \lambda] = \frac{1}{\kappa}\int_\mathcal{M}\left[\left(^\star\!B^{IJ} + \frac{1}{\gamma}B^{IJ}\right)\wedge F_{IJ}(\omega) + \lambda_{IJKL} B^{IJ}\wedge B^{KL}\right].
$$
This can be thought of as a $\mathrm{Spin}(4)$ BF theory and a constraint imposed by the lagrangian multiplier $\lambda$. It depends on a $\mathfrak{so}(4)$ connection $\omega$ and a Lie-algebra valued 2-form $B$.

The symmetry of $B$ and $\wedge$ imposes a constraint on $\lambda$ as well. Since switching between the indices of $B^{IJ}$ is antisymmetric and that the operation $\wedge$ is symmetric, we have the following relation:
$$
\lambda_{IJKL} = -\lambda_{JIKL} = -\lambda_{IJLK} = \lambda_{KLIJ}.
$$
This restrains the dimension of $\lambda$ down to 21. However, if $\lambda_{IJKL}\propto \epsilon_{IJKL}$ the lagrangian multiplier will give $\epsilon_{IJKL}B^{IJ}\wedge B^{KL}$, which implies a degenerate metric. Therefore $\epsilon^{IJKL}\lambda_{IJKL} = 0$, and that $\mathrm{dim}\lambda = 20$.

To actually calculate the constraint given by the lagrangian multiplier, we introduce
$$
\lambda_{IJKL} = \Lambda_{IJKL} - \frac{1}{4!}\Lambda_{MNOP}\epsilon^{MNOP}\epsilon_{IJKL}.
$$
We make this substitution because if we assume $\Lambda$ to be the unconstrained lagrangian multiplier and 
$$
\Lambda_{[IJKL]} = c\cdot\epsilon_{IJKL}
$$
we can multiply both sides with $\epsilon$ and have
$$
\Lambda_{[IJKL]}\epsilon^{IJKL} = c\cdot\epsilon^2\implies c = \frac{1}{4!}\Lambda_{[MNOP]}\epsilon^{MNOP}.
$$
