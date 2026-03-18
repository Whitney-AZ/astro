---
title: Some Trivial Examples of RAQ
date: 2026-03-17
summary: Including momentum constraint, angular momentum constraint, etc.
category: 笔记
tags: [数学, 物理, 广义相对论, 微分几何]
series: 'LQG Notes'
---

In this post we put forward four examples of quantizing systems with constraints using the RAQ programme. In each case our final goal is to derive the dirac observables and the physical hilbert space.

---

### Momentum Constraint

Consider the phase space $\mathcal{M} = T^\ast \mathbb{R}^2$ with poisson brackets among $q^a$ and $p_a$. Our constraint is $C = p_1$, and we choose $\mathcal{H}_{kin} = L_2(\mathbb{R}^2, \mathrm{d}^2x)$, $\mathcal{D}_{kin} = \mathcal{S}(\mathbb{R}^2)$ and $\mathcal{D}^\ast_{kin} = \mathcal{S}^\ast(\mathbb{R}^2)$.

By the constraint $C = p_1$, we have the constraint equation $l(\hat{C}^\dagger\phi) = 0$, where $l \in \mathcal{D}^\ast_{kin}$ and $\phi \in \mathcal{D}_{kin}$. Working in the momentum representation, we can write the constraint equation as

$$
l(\hat{p}_1\phi(\hat{p}_1, \hat{p_2})) = 0
$$

where we can cleanly see that a function of the form $l = \delta(p_1)f(p_2)$ solves the equation. We construct the new inner product as $\langle l_{f_1}, l_{f_2}\rangle := l_1[\phi_2]$, therefore we have

$$
l_1[\phi_2] = \int \int \delta(p_1) f_1^*(p_2) \phi_2(p_1, p_2) \mathrm{d}p_1 \mathrm{d}p_2 = \int f_1^*(p_2) \phi_2(p_2) \mathrm{d}p_2.
$$

which is a perfectly well-defined inner product, therefore $\mathcal{H}_{phys} = L_2(\mathbb{R},\mathrm{d}x_2)$.

From the constraint it's also trivial to find the dirac observables to be $q^2, p_2$ because these operators must commute with the constraint, which in this case is $p_1$.

---

### Angular Momentum Constraint

We consider the phase space to be $\mathcal{M} = T^\ast \mathbb{R}^3$ with poisson brackets among $q^a$ and $p_a$. Our constraints are $C_a = \epsilon_{abc}x_bp_c$, and we choose $\mathcal{H}_{kin} = L_2(\mathbb{R}^3, \mathrm{d}^3x)$, $\mathcal{D}_{kin} = \mathcal{S}(\mathbb{R}^3)$ and $\mathcal{D}^\ast_{kin} = \mathcal{S}^\ast(\mathbb{R}^3)$.

The constraint algebra is simply the angular momentum algebra, so we can identify $\hat{C}_a \equiv \hat{L}_a$. The constraint equation is now $\hat{L}_a \Psi = 0$. By expanding it into spherical harmonics, we have

$$
\Psi = \sum_{l = 0}^{\infty}\sum_{m = -l}^lR_{lm}(r)Y^m_l(\theta,\phi).
$$

The constraint equation implies $\hat{L}^2\Psi = 0$, but from QM we know that $\hat{L}^2\Psi = l(l+1)\hbar^2Y^m_l$, thus $l = 0$. Our physical states are then $\Psi = \phi(r)$, which can be perfectly normalized in $\mathcal{H}_{kin}$ because $SO(3)$ is compact and the integral on the group manifold gives a finite result. Therefore, we have

$$
\mathcal{H}_{phys} = L_2(\mathbb{R},r^2\mathrm{d}r) \subset \mathcal{H}_{kin}.
$$

Now we find the dirac observables. We'll have to find operators that are self-adjoint under the physical inner product induced by $\mathcal{H}_{kin}$. Notice that if we define $\hat{p} = -\mathrm{i}\hbar r^{-1}\frac{\mathrm{d}}{\mathrm{d}r}r$, such a inner product can be written as

$$
\begin{aligned}
    \langle\phi, \hat{p}\psi\rangle = \int \phi^\ast\hat{p}\psi r^2\mathrm{d}r
    &=  \int \phi^\ast\left(-\mathrm{i}\hbar \frac{1}{r}\frac{\mathrm{d}}{\mathrm{d}r}\left(r\psi\right) \right)r^2\mathrm{d}r\\
    &=  -\mathrm{i}\hbar \int r\phi^\ast\left(\partial_r\left(r\psi\right) \right)\mathrm{d}r\\
    &=  \left(-\mathrm{i}\hbar(r\phi^\ast)(r\phi)\right)\Big|^{+\infty}_{-\infty} + \mathrm{i}\hbar \int \partial_r(r\phi^\ast)\left(r\psi\right)\mathrm{d}r\\
    &=  \int\left(\hat{p}\phi\right)^\ast\psi r^2\mathrm{d}r = \langle\hat{p}\phi, \psi\rangle.
\end{aligned}
$$

Similarly the operator $\hat{r} := r$ is also a dirac observable, completing the programme.

---

### Relativistic Particle

From the form of the Lagrangian

$$
L = -m\sqrt{-\eta_{\mu\nu} \dot{q}^\mu\dot{q}^\nu}
$$

and the definition of conjugate momenta $p_\mu = \partial L/\partial \dot{q}^\mu$, we can surprisingly see

$$
\frac{\partial L}{\partial \dot{q}^\mu} = m\frac{\dot{q}_\mu}{\sqrt{-\eta_{\mu\nu} \dot{q}^\mu\dot{q}^\nu}} = p_\mu \implies \eta^{\mu\nu}p_\mu p_\nu + m^2 = 0.
$$

which is the mass-shell constraint. In this case, the constraint came directly from the lagrangian. We shall later see this is the result of the disappearing Hamiltonian.

Next we prove the action $S = \int \mathrm{d}t L$ to be $\mathrm{Diff}(\mathbb{R})$ invariant. Consider the reparameterization $t\mapsto \varphi(t)$. With this new time variable, the action is now

$$
S^\prime = \int -m\sqrt{-\eta_{\mu\nu}\frac{\mathrm{d}\dot{q}^\mu}{\mathrm{d}\varphi}\frac{\mathrm{d}\dot{q}^\nu}{\mathrm{d}\varphi}}\mathrm{d}\varphi = \int -m\sqrt{-\eta_{\mu\nu}\frac{\mathrm{d}\dot{q}^\mu}{\mathrm{d}t}\frac{\mathrm{d}\dot{q}^\nu}{\mathrm{d}t}}\dot{\varphi}\dot{\varphi}^{-1}\mathrm{d}t = S.
$$

Under reparameterization, although $\dot{q}^\mu$ is variant, $p_\mu$ stayed constant. This means the mapping from velocity space to momentum space is not one-to-one, namely every momentum correpsonds to a ray in velocity space. Therefore we need to have some kind of constraint on $\mathcal{M}$, limiting the physical momentum to a hypersurface, here the mass-shell constraint.

Next we calculate the hamiltonian, which is trivially vanishing:

$$
H = p_\mu \dot{q}^\mu - L = 0.
$$

This means in this system, evolution is simply a gauge transformation and there are no dynamics.

We consider the phase space to be $\mathcal{M} = T^\ast \mathbb{R}^{D+1}$ with poisson brackets among $q^a$ and $p_a$. Our constraint is the mass-shell constraint, and we choose $\mathcal{H}_{kin} = L_2(\mathbb{R}^{D+1}, \mathrm{d}^{D+1}x)$, $\mathcal{D}_{kin} = \mathcal{S}(\mathbb{R}^{D+1})$ and $\mathcal{D}^\ast_{kin} = \mathcal{S}^\ast(\mathbb{R}^{D+1})$. This system is rather similar to the momentum one, so we work in the momentum representation again to get

$$
l(\hat{C}\Psi) = 0 \implies l((-\partial^2 + m^2)\Psi) = 0 \implies l((-p_0^2 + p^2 + m^2)\Psi) = 0.
$$

We assume the solution is of the form $l_f = \delta(-p_0^2 + p^2 + m^2)f(p_0,p_i)$. Applying the same physical inner product as in 1, we can get

$$
\langle l_{f_1}, l_{f_2}\rangle = \int l^\ast_{f_1}f_2(p_i)\mathrm{d}^Dp.
$$

that is to say the physical hilbert space is $\mathcal{H}_{phys} := L_2(\mathbb{R}^2,\mathrm{d}^Dp)$. The dirac observables are $Q^a = q^a - q^0\frac{p_a}{\sqrt{m^2+p^2}}$. It is easy to verify that for every $q^0$, $[Q^a,C] = 0$. This is another sign that coordinate time in relativistic systems are gauge, and for simplicity reasons we set $q^0 = 0$.

---

### Maxwell Theory

As we all know, the lagrangian for a free maxwell theory is $\mathcal{L} = -1/4F_{\mu\nu}F^{\mu\nu}$. We define $E^a = \dot{A}_a - \partial_a A_0$, and $B^a = \epsilon^{abc}\partial_b A_c$. The lagrangian is therefore

$$
L = \int \mathrm{d}^3x\frac{1}{2}\left(E^aE_a - B^aB_a\right)
$$

the generalized coordinates in this case are $A^\mu$. If we compute the conjugate momenta of $A^\mu$, we find

$$
\begin{cases}
    \frac{\partial L}{\partial \dot{A}_0} = 0 =: \pi^0,\\
    \frac{\partial L}{\partial \dot{A}_a} = E^a =: \pi^a.
\end{cases}
$$

and the hamiltonian to be

$$
H = \int\mathrm{d}^3x\left(\pi^0 \dot{A}_0 + \pi^a\dot{A}_a - \mathcal{L}\right) = \int\mathrm{d}^3x\frac{1}{2}(\pi^2 + B^2) + \pi^a\partial_a A_0.
$$

For the term $\pi^a\partial_a A_0$, we perform integration by parts: $\pi^a\partial_a A_0 = -A_0\partial_a\pi^a$. The time evolution of $\pi^0$ should be 0, which leads to the poisson bracket $\{\pi^0, H\} = -\delta H/\delta A_0 = \partial_a\pi^a = \partial_a E^a = 0$. But this is exactly the Gauss constraint! $A_0$ has lost all it's dynamics under this constraint, but only a lagrange multiplier.

Now we demonstrate that the Gauss constraint does indeed generate the $U(1)$ gauge transformation. We consider the integration of $\partial_a E^a$ mutiplied by some function $\lambda(x)$:

$$
C(\lambda) = \int \mathrm{d}^3x \lambda(x) \partial_a E^a = - \int d^3x (\partial_a \lambda) E^a
$$

Varying $A$ gives

$$
\delta A(x) = \{A_a(x), C(\lambda)\} = -\partial_a\lambda(x),
$$

which is the standard $U(1)$ gauge transformation. Similarly, we can see that $E$ is gauge invariant.

In order to do quantization, we first apply the Helmholtz decomposition on $A_a$ and $E^a$:

$$
\begin{cases}
    A_a = A^L_a + A^T_a,\\
    E^a = (E^L)^a + (E^T)^a.
\end{cases}
$$

where $\nabla\cdot A^T = 0, A^L_a = \partial_a\phi$ and $\nabla\cdot E^T = 0, (E^L)^a = \partial_a\psi$. Now the Gauss constraint becomes $C = \partial_a E^a = \partial_a (E^L)^a = \nabla^2\psi = 0$. Therefore, the gauge condition suggests that the dirac observables are the transversal parts of $A$ and $E$.

Now we do the quantization. Consider the three corresponding massless scalar fields of $A_a$. $\mathcal{H}_{kin}$ is the Fock space generated by $\hat{z}^\dagger_a(k)$ and $\hat{z}_a(k)$, the creation and annihilation operators respectively. Under fourier transform, the constraint can be written as $\hat{C} = k_aE^a(k)$, which leads to $k^a\hat{z}_a(k)|\Psi\rangle_{phys} = 0$. Next we introduce polarized vectors $e_a(k)$. But because by the gauss constraint $E^a$ only consist of components parallel to $k$, the constraint equation is simply $\hat{z}_3(k)|\Psi\rangle_{phys} = 0$. This means physical states are states without longitudonal excitations, therefore $\mathcal{H}_{phys}$ is the Fock space spanned by $\hat{z}^\dagger_1(k)$ and $\hat{z}^\dagger_2(k)$. This is why there are only two tranverse polarization states of a photon.

---

In the next part, we will use the ADM formulation to construct the phase space of General Relativity.
