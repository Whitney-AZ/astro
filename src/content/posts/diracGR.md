---
title: The Connection Formulation of General Relativity
date: 2026-04-12
summary: From a constrained BF theory, we derive the connection formulation of general relativity using dirac's constraint analysis method.
category: 笔记
tags: [数学, 物理, 广义相对论]
pdf: false
series: 'LQG Notes'
---

> It should be noted that this is typesetted by Gemini based on my written notes. They have not been manually checked and may (do) contain errors.

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

This gives the derivative of the action with respect to $\Lambda$:

$$
\frac{\delta S}{\delta \Lambda_{IJKL}} = B^{IJ}\wedge B^{KL} - \frac{1}{4!}\epsilon^{IJKL}\epsilon_{MNOP}B^{MN}\wedge B^{OP} = 0.
$$

which implies

$$
\epsilon^{\mu\nu\rho\sigma} B^{IJ}_{\mu\nu} B^{KL}_{\rho\sigma} = \frac{1}{4!} \epsilon^{IJKL} \epsilon_{MNOP} B^{MN}_{\mu\nu} B^{OP}_{\rho\sigma} \epsilon^{\mu\nu\rho\sigma}.
$$

This equation constraints the degrees of freedom of $B$, limiting its dimension down to $16 = 4\times 4$. So if we define:

$$
e := \frac{1}{4!} \epsilon_{MNOP} B^{MN}_{\mu\nu} B^{OP}_{\rho\sigma} \epsilon^{\mu\nu\rho\sigma}
$$

It behaves exactly as the local tetrad. The solution of $B$ would be

$$
B = \pm ^\star(e\wedge e) \quad\text{and}\quad \pm e\wedge e.
$$

Here $e$ is the new variable, and the term $\lambda B\wedge B$ in the action is simply the constraint. So if we put $B = \pm^\star(e\wedge e)$ back into the action $S$, we obtain

$$
S[e, \omega] = \frac{1}{\kappa}\int_\mathcal{M} \operatorname{Tr}\left[\left(^\star(e\wedge e) + \frac{1}{\gamma}e\wedge e\right) \wedge F(\omega)\right].
$$

## Canonical Analysis

We perform the 3+1 decomposition. We use labels $a,b = 1,2,3$ as spacial indices on $\Sigma_t$. Introduce

$$
\begin{aligned}
\Pi_{ab}^{IJ} &= ^\star B_{ab}^{IJ} + \frac{1}{\gamma}B_{ab}^{IJ}\implies \text{pure spacial; lives on }\Sigma_t\\
H_a^{IJ} &= ^\star B_{0a}^{IJ} + \frac{1}{\gamma}B_{0a}^{IJ}\implies \text{space-time}.
\end{aligned}
$$

Also, we decompose the curvature form $F_{\mu\nu}$:

$$
\begin{aligned}
F_{ab} &= \partial_{[a}\omega_{b]} + [\omega_a, \omega_b]\\
F_{0a} &= \partial_0\omega_a - \partial_a\omega_0 + [\omega_0, \omega_a] = \dot{\omega}_a - (\partial_a\omega_0 - [\omega_a, \omega_0]) =: \dot{\omega}_a - \mathcal{D}_a\omega_0.
\end{aligned}
$$

The action is originally:

$$
S[\Pi, H, \omega, \lambda] = \frac{1}{\kappa}\int_\mathcal{M}\left[\left(^\star B^{IJ} + \frac{1}{\gamma}B^{IJ}\right)\wedge F_{IJ} + \lambda_{IJKL} B^{IJ}\wedge B^{KL}\right]
$$

Substituting the 3+1 decomposed variables:

$$
S = \frac{1}{\kappa}\int_\mathcal{M} \left[(\Pi_{ab}^{IJ}\wedge F_{IJ,0a}) + (H_{a}^{IJ}\wedge F_{IJ,ab}) + \lambda_{IJKL}B_{0a}^{IJ}\wedge B_{ab}^{KL}\right]
$$

After some algebra, this leads to:

$$
\begin{aligned}
S
&= \frac{1}{\kappa}\int_\mathcal{M}\left(\Pi_{ab}^{IJ}\wedge \dot{\omega}_{IJ,c} - \Pi_{ab}^{IJ}\wedge \mathcal{D}_a \omega_{0,IJ} + H_a^{IJ}\wedge F_{IJ,ab} \right. \\
&+  \left.\lambda_{IJKL}\left\{\frac{\gamma^2}{\gamma^2-1}(\gamma^\star H_{a}^{IJ} - H_{a}^{IJ}) \wedge \frac{\gamma}{\gamma^2-1}(\gamma\Pi_{bc}^{KL} - ^\star\Pi_{bc}^{KL})\right\}\right).
\end{aligned}
$$

By integrating by parts, the second term gives $\omega_0 \mathcal{D}_\omega\wedge \Pi$, and if we redefine $\lambda' = \frac{\gamma^2}{(\gamma^2-1)^2}\lambda$, the action is:

$$
S = \int dt \int_{\Sigma_t} \operatorname{Tr} \left[ \Pi \wedge \dot{\omega} + \omega_0 \mathcal{D}_\omega \wedge \Pi + H \wedge F + \lambda' (\gamma ^\star H - H) \wedge (\gamma ^\star \Pi - \Pi) \right].
$$

The canonical pair is $(\Pi^{IJ}_{ab}, \omega^{KL}_c)$. If we introduce

$$
\begin{aligned}
\mathbb{P}(\gamma, \pm)^i_{ab} &:= \frac{1}{4} \epsilon^i_{\ jk} \Pi^{jk}_{ab} \pm \frac{1}{2\gamma} \Pi^{0i}_{ab} \\
{}^{\pm}\mathbb{A}_c^i &:= \frac{1}{2} \epsilon^i_{\ mn} \omega^{mn}_c \pm \gamma \omega^{0i}_c \\
\mathbb{H}(\gamma, \pm)^i_a &:= \frac{1}{4} \epsilon^i_{\ jk} H^{jk}_a \pm \frac{1}{2\gamma} H^{0i}_a
\end{aligned}
$$

where $\mathbb{A}$ is a function of $\omega$, its time derivative corresponds to

$$
\partial_0 {}^{\pm}\mathbb{A}_c^i = \frac{1}{2} \epsilon^i_{\ mn} \partial_0 \omega^{mn}_c \pm \gamma \partial_0 \omega^{0i}_c = \frac{1}{2} \epsilon^i_{\ mn} \dot{\omega}^{mn}_c \pm \gamma \dot{\omega}^{0i}_c =: {}^{\pm}\dot{\mathbb{A}}_c^i.
$$

Also notice that

$$
\mathbb{P}(\gamma, +)^i_{ab} = \frac{1}{4} \epsilon_{ijk} \Pi^{jk}_{ab} + \frac{1}{2\gamma} \Pi^{0}_{ab, i},
$$

$$
\mathbb{P}(\gamma, -)^i_{ab} = \frac{1}{4} \epsilon_{ijk} \Pi^{jk}_{ab} - \frac{1}{2\gamma} \Pi^{0}_{ab, i}.
$$

These simplify the canonical trace term $\operatorname{Tr}[\Pi\wedge\dot{\omega}]$:

$$
\begin{aligned}
\mathbb{P}^{+} \wedge {}^{+}\dot{\mathbb{A}} + \mathbb{P}^{-} \wedge {}^{-}\dot{\mathbb{A}}
&= (\Pi + \Pi^0) \wedge (\dot{\omega} + \dot{\omega}^0) + (\Pi - \Pi^0) \wedge (\dot{\omega} - \dot{\omega}^0) \\
&= 2 \Pi \wedge \dot{\omega} + 2 \Pi^0 \wedge \dot{\omega}^0 \\
&= \frac{1}{2} \epsilon_{ijk} \Pi^{jk} \wedge \frac{1}{2} \epsilon^i_{\, mn} \dot{\omega}^{mn} + \frac{1}{\gamma} \Pi^{0}_i \wedge \gamma \dot{\omega}^{i0} \\
&= \frac{1}{2} (\delta_{jm}\delta_{kn} - \delta_{jn}\delta_{km}) \Pi^{jk} \wedge \dot{\omega}^{mn} + \Pi^{0}_i \wedge \dot{\omega}^{i0} \\
&= \frac{1}{2} \Pi_{ij} \wedge \dot{\omega}^{ij} + \Pi^0_{i} \wedge \dot{\omega}^{i0} = \operatorname{Tr} [ \Pi \wedge \dot{\omega} ].
\end{aligned}
$$

The term $\omega_0 \mathcal{D}_\omega \wedge \Pi$ acts as a Lagrangian constraint, with $\omega_0$ serving as the multiplier. We can express the connection variables as:

$$
\frac{{}^{+}\mathbb{A} + {}^{-}\mathbb{A}}{2} = \frac{1}{2} \epsilon^i_{\ mn} \omega^{mn}_c \quad \text{and} \quad ({}^{+}\mathbb{A} - {}^{-}\mathbb{A})_j = 2\gamma \omega^{0j}_c.
$$

Consequently, we can decompose the constraint term:

$$
\begin{aligned}
\omega_0 \mathcal{D}_\omega \wedge \Pi &= {}^{+}\mathbb{A}_0 (\mathcal{D}_{{}^{+}\mathbb{A}} \mathbb{P}^{+})_i + {}^{-}\mathbb{A}_0 (\mathcal{D}_{{}^{-}\mathbb{A}} \mathbb{P}^{-})_i.
\end{aligned}
$$

Expanding the first term, we find:

$$
\begin{aligned}
{}^{+}\mathbb{A}_0 \left( d \mathbb{P}^{+} + {}^{+}\mathbb{A} \times \mathbb{P}^{+} \right) &= {}^{+}\mathbb{A}_0 \left[ d \mathbb{P}^{+} + \frac{1}{2}\epsilon_{ijk} \left( \epsilon^j_{\ mn} \omega^{mn} + \gamma \omega^{0j} \right) \mathbb{P}^{+k}\right] \\
&= {}^{+}\mathbb{A}_0 \left[ d \mathbb{P}^{+} + \frac{1}{2} \epsilon_{ijk} \epsilon^j_{\ mn} \omega^{mn} \mathbb{P}^{+k} + \gamma \epsilon_{ijk} \omega^{0j} \mathbb{P}^{+k} \right] \\
&= {}^{+}\mathbb{A}_0 \, \mathcal{D}_{\left(\frac{1}{2}\epsilon \omega\right)} \mathbb{P}^{+} + {}^{+}\mathbb{A}_0 \, \epsilon_{ijk} \frac{{}^{+}\mathbb{A} - {}^{-}\mathbb{A}}{2} \mathbb{P}^{+k} \\
&\sim \eta_i \mathbb{B}^i + N_i \mathbb{G}^i.
\end{aligned}
$$

Here we introduce new constraints $\mathbb{B}^i$ and $\mathbb{G}^i$. Hence, we can rewrite the action as:

$$
\begin{aligned}
S[\mathbb{P}(\gamma, \pm), {}^{\pm}\mathbb{A}, \lambda] &= \int dt \int_{\Sigma_t} \Big\{ \mathbb{P}^{+} \wedge {}^{+}\dot{\mathbb{A}} + \mathbb{P}^{-} \wedge {}^{-}\dot{\mathbb{A}} + N_i \mathbb{G}^i + \eta_i \mathbb{B}^i \\
&+ {}^{-}\mathbb{A}_0 \, \mathcal{D}_{{}^{-}\mathbb{A}} \mathbb{P}^{-} + H \wedge F + \lambda' (\gamma ^\star H - H) \wedge (\gamma ^\star \Pi - \Pi) \Big\}.
\end{aligned}
$$

The Lagrangian multipliers $N, \eta, \lambda'$ impose the following constraints:

$$
\begin{cases}
\mathbb{B}^i := \mathcal{D}_{\frac{{}^{+}\mathbb{A} + {}^{-}\mathbb{A}}{2}} \wedge \mathbb{P}(\gamma, +)^i \approx 0 \\
\mathbb{G}^i := \frac{1}{2\gamma} \epsilon_{ijk} ({}^{+}\mathbb{A} - {}^{-}\mathbb{A})_j \wedge \mathbb{P}(\gamma, +)_k \approx 0 \\
(\gamma^\star H - H)\wedge(\gamma^\star \Pi - \Pi) = 0 \implies \epsilon_{\mu\nu\rho\sigma} B^{IJ}_{\mu\nu} B^{KL}_{\rho\sigma} - e\epsilon^{IJKL} = 0.
\end{cases}
$$

The index pair $[IJ, KL]$ must be decomposed. We separate it into three cases:

$$
\begin{cases}
IJKL = 0i0j\\
IJKL = ijkl\\
IJKL = 0ijk.
\end{cases}
$$

For case 1 ($IJKL = 0i0j$):

$$
\begin{gathered}
B^{0i} \wedge B^{0j} = 0 \\
\implies C^{0i}_H \wedge C^{0j}_\Pi + (i \leftrightarrow j) = 0 \\
\implies (\gamma ^\star H^{0i} - H^{0i}) \wedge (\gamma ^\star \Pi^{0j} - \Pi^{0j}) + (i \leftrightarrow j) = 0 \\
\implies \left(\frac{\gamma}{2}\epsilon^i_{\ jk}H^{jk} - H^{0i}\right) \wedge \left(\frac{\gamma}{2}\epsilon^j_{\ kl}\Pi^{kl} - \Pi^{0j}\right) + (i \leftrightarrow j) = 0.
\end{gathered}
$$

For case 2 ($IJKL = ijkl$):

$$
\begin{gathered}
B^{ij} \wedge B^{kl} = 0 \\
\implies C^{ij}_H \wedge C^{kl}_\Pi + (ij \leftrightarrow kl) = 0 \\
\implies (\gamma ^\star H^{ij} - H^{ij}) \wedge (\gamma ^\star \Pi^{kl} - \Pi^{kl}) + (ij \leftrightarrow kl) = 0 \\
\implies \epsilon^{(p}_{\ \ \  ij}\left(\frac{\gamma}{2}\epsilon^{ij}_{\ \ m} H^{0m} - H^{ij}\right) \wedge \epsilon^{q)}_{\ \ \ kl}\left(\frac{\gamma}{2}\epsilon^{kl}_{\ \ n} \Pi^{0n} - \Pi^{kl}\right) = 0.
\end{gathered}
$$

For case 3 ($IJKL = 0ijk$):

$$
\begin{gathered}
B^{0i} \wedge B^{jk} = \nu \epsilon^{0ijk} \\
\implies C^{0i}_H \wedge C^{jk}_\Pi + (0i \leftrightarrow jk) = \nu \epsilon^{0ijk} \\
\implies (\gamma ^\star H^{0i} - H^{0i}) \wedge (\gamma ^\star \Pi^{jk} - \Pi^{jk}) + (0i \leftrightarrow jk) = \nu \epsilon^{0ijk} \\
\begin{aligned}
\implies &\left(\frac{\gamma}{2}\epsilon^i_{\ mn} H^{mn} - H^{0i}\right) \wedge \left(\frac{\gamma}{2}\epsilon^{jk}_{\ \ l} \Pi^{0l} - \Pi^{jk}\right) +\\
&\left(\frac{\gamma}{2}\epsilon^i_{\ mn}\Pi^{mn} - \Pi^{0i}\right) \wedge \left(\frac{\gamma}{2}\epsilon^{jk}_{\ \ l}H^{0l} - H^{jk}\right) - \nu \epsilon^{0ijk}= 0.
\end{aligned}
\end{gathered}
$$

Recall that we've defined

$$
\begin{aligned}
\mathbb{H}(\gamma, \pm)^i_a &:= \frac{1}{4} \epsilon^i_{\ jk} H^{jk}_a \pm \frac{1}{2\gamma} H^{0i}_a \\
\mathbb{P}(\gamma, \pm)^i_{ab} &:= \frac{1}{4} \epsilon^i_{\ jk} \Pi^{jk}_{ab} \pm \frac{1}{2\gamma} \Pi^{0i}_{ab}.
\end{aligned}
$$

Therefore we can rewrite the constraints as:

$$
\begin{aligned}
&\mathbb{B}^i = \mathcal{D}_{({}^{+}\mathbb{A} + {}^{-}\mathbb{A})/2} \wedge \mathbb{P}(\gamma, +)^i \approx 0 \\
&\mathbb{G}^i = \frac{1}{2\gamma} \epsilon^{ijk} ({}^{+}\mathbb{A} - {}^{-}\mathbb{A})_j \wedge \mathbb{P}(\gamma, +)_k \approx 0 \\
&\mathbb{I}^{ij} = \mathbb{H}(\gamma, -)^{(i} \wedge \mathbb{P}(\gamma, -)^{j)} \approx 0 \\
&\mathbb{II}^{ij} = \mathbb{H}\left(\frac{1}{\gamma}, -\right)^{(i} \wedge \mathbb{P}\left(\frac{1}{\gamma}, -\right)^{j)} \approx 0 \\
&\mathbb{III}^{ij} = \mathbb{H}(\gamma, -)^{i} \wedge \mathbb{P}(\gamma, +)^{j} + \mathbb{H}\left(\frac{1}{\gamma}, -\right)^{i} \wedge \mathbb{P}(\gamma, -)^{j} - \frac{1}{3} \delta^{ij} \operatorname{Tr}[\dots] = 0
\end{aligned}
$$

The last three constraints are derived from the original lagrangian multiplier $\lambda$, therefore include 20 constraints in total and are simplicity constraints. In the 3+1 setting, by choosing the time gauge to be $n^I = (1, 0, 0, 0)$, $e^I_\mu$ is

$$
\begin{cases}
e^0_0 = N & (\text{lapse}) \\
e^0_a = 0 & (\text{pure spacial, no time-like component}) \\
e^i_0 = N^i & (\text{shift}) \\
e^i_a = \text{standard 3-d tetrad}
\end{cases}
$$

(Indices: $I, J \in 0, 1, 2, 3$ local; $\mu, \nu \in 0, 1, 2, 3$ global; $a,b \in 1, 2, 3$ global spacial; $i,j \in 1, 2, 3$ local spacial).
We consider the solution $B = e \wedge e \implies B^{IJ}_{\mu\nu} = e^I_\mu e^J_\nu - e^J_\mu e^I_\nu$.

Globally spacial components:

$$
\begin{aligned}
B^{0i}_{ab} &= e^0_a e^i_b - e^0_b e^i_a = 0 \implies ^\star B^{0i}_{ab} = \frac{1}{2} \epsilon_{\ \ \ jk}^{0i} B^{jk}_{ab} = \frac{1}{2} \epsilon^{0i}_{\ \ \ jk} (e^j_a e^k_b - e^j_b e^k_a) = \epsilon^{i}_{\ \ jk} e^j_a e^k_b \\
B^{jk}_{ab} &= e^j_a e^k_b - e^k_a e^j_b = 2 e^{[j}_a e^{k]}_b \implies ^\star B^{jk}_{ab} = \frac{1}{2} \epsilon^{jk}_{\ \ \ 0i} B^{0i}_{ab} = 0.
\end{aligned}
$$

Globally timelike components:

$$
\begin{aligned}
B^{0i}_{0a} &= e^0_0 e^i_a - e^0_a e^i_0 = N e^i_a \implies ^\star B^{0i}_{0a} = \frac{1}{2} \epsilon_{\ \ \ jk}^{0i} B^{jk}_{0a} = \frac{1}{2} \epsilon^{0i}_{\ \ jk} (e^j_0 e^k_a - e^k_0 e^j_a) = \epsilon^{i}_{\ \ jk} N^j e^k_a \\
B^{jk}_{0a} &= e^j_0 e^k_a - e^k_0 e^j_a = 2 N^{[j} e^{k]}_a \implies ^\star B^{jk}_{0a} = \frac{1}{2} \epsilon^{jk}_{\ \ \ 0i} B^{0i}_{0a} = \frac{1}{2} \epsilon^{jk}_{\ \ \ 0i} N e^i_a = N \epsilon^{jk}_{\ \ \ 0i} e^{i}_{\ \ a}.
\end{aligned}
$$

Now we calculate the corresponding $\Pi$ & $H$:

$$
\begin{aligned}
\Pi^{0i}_{ab} &= {}^\star B^{0i}_{ab} + \frac{1}{\gamma} B^{0i}_{ab} = \epsilon^{i}_{\ \ jk} e^{j}_{a} e^{k}_{b} \\
\Pi^{jk}_{ab} &= {}^\star B^{jk}_{ab} + \frac{1}{\gamma} B^{jk}_{ab} = \frac{2}{\gamma} e^{[j}_{a} e^{k]}_{b} \\
H^{0i}_{a} &= {}^\star B^{0i}_{0a} + \frac{1}{\gamma} B^{0i}_{0a} = \epsilon^{i}_{\ \ jk} N^{j} e^{k}_{a} + \frac{N}{\gamma} e^{i}_{a} \\
H^{jk}_{a} &= {}^\star B^{jk}_{0a} + \frac{1}{\gamma} B^{jk}_{0a} = N \epsilon_{\ \ i}^{jk} e^{i}_{a} + \frac{2}{\gamma} N^{[j} e^{k]}_{a}.
\end{aligned}
$$

Now we can show that

$$
\begin{aligned}
\mathbb{P}(\gamma, \pm)^i_{ab} &= \frac{1}{4} \epsilon^i_{\ jk} \Pi^{jk}_{ab} \pm \frac{1}{2\gamma} \Pi^{0i}_{ab} = \frac{1}{4} \epsilon^i_{\ jk} \frac{2}{\gamma} e^j_{[a} e^k_{b]} \pm \frac{1}{2\gamma} \epsilon^i_{\ jk} e^j_a e^k_b =
\begin{cases}
\mathbb{P}(\gamma, -)^i_{ab} = 0 \\
\mathbb{P}(\gamma, +)^i_{ab} = \frac{1}{\gamma} \epsilon^i_{\ jk} e^j_a e^k_b
\end{cases} \\
\mathbb{P}\left(\frac{1}{\gamma}, \pm\right)^i_{ab} &= \frac{1}{4} \epsilon^i_{\ jk} \Pi^{jk}_{ab} \pm \frac{\gamma}{2} \Pi^{0i}_{ab} = \frac{1}{2\gamma} \epsilon^i_{\ jk} e^j_a e^k_b \pm \frac{\gamma}{2} \epsilon^i_{\ jk} e^j_a e^k_b = \frac{1\pm\gamma^2}{2\gamma}\mathbb{P}(\gamma, +)^i_{ab} \\
\mathbb{H}(\gamma, -)^i_a &= \frac{1}{4} \epsilon^i_{\ jk} H^{jk}_a - \frac{1}{2\gamma} H^{0i}_a = \frac{1}{4} \epsilon^i_{\ jk} \left(N \epsilon^{jk}_{\ \ \ l} e_{a}^l + \frac{2}{\gamma} N^{[j} e^{k]}_a\right) - \frac{1}{2\gamma}\left(\epsilon^{i}_{\ \ jk} N^j e_{a}^k + \frac{N}{\gamma} e^i_a\right) \\
&= \frac{1}{2} N \delta^i_l e^l_a + \frac{1}{2\gamma} \epsilon^i_{\ jk} N^j e^k_a - \frac{1}{2\gamma} \epsilon^{i}_{\ \ jk} N^j e_{a}^k - \frac{N}{2\gamma^2}e^i_a = N \frac{\gamma^2 - 1}{2\gamma^2} e^i_a \\
\mathbb{H}\left(\frac{1}{\gamma}, -\right)^i_a &= \frac{1}{4} \epsilon^i_{\ jk} H^{jk}_a - \frac{\gamma}{2} H^{0i}_a = \frac{1}{2} N \delta^i_l e^l_a + \frac{1}{2\gamma} \epsilon^i_{\ jk} N^j e^k_a - \frac{\gamma}{2}\left(\epsilon^{i}_{\ \ jk} N^j e_{a}^k + \frac{N}{\gamma} e^i_a\right) \\
&= \frac{1-\gamma^2}{2\gamma} \epsilon^{i}_{\ \ jk} N^b e^j_b e^k_a = \frac{1 - \gamma^2}{2} N^b \mathbb{P}(\gamma, +)^i_{ba}.
\end{aligned}
$$

Notice that $\mathbb{P}(\gamma, -) = 0$ breaks the internal Lorentz gauge. From the above equations, we can parameterize the variables $H^{jk}_a$ and $H^{0i}_a$ purely down to $\mathbb{P}(\gamma, +)^i_{ab}$ and variables $N, N^i$, which we can see explicitly by solving for them:

$$
\begin{aligned}
&\mathbb{H}\left(\frac{1}{\gamma}, -\right)^i_a - \mathbb{H}(\gamma, -)^i_a = \left(\frac{1}{2\gamma} - \frac{\gamma}{2}\right) H^{0i}_a = \frac{1-\gamma^2}{2\gamma} H^{0i}_a \quad &\text{(i)}\\
&\gamma^2 \mathbb{H}(\gamma, -)^i_a - \mathbb{H}\left(\frac{1}{\gamma}, -\right)^i_a = \frac{\gamma^2 - 1}{4} \epsilon^i_{\ jk} H^{jk}_a \quad &\text{(ii)}
\end{aligned}
$$

Plugging in our findings for $\mathbb{H}(\gamma, -)$ and $\mathbb{H}\left(1/\gamma, -\right)$, we get:

$$
\begin{aligned}
\text{(i)} &\implies \frac{1 - \gamma^2}{2} N^b \mathbb{P}(\gamma, +)^i_{ba} + N \frac{1 - \gamma^2}{2\gamma^2} e^i_a = \frac{1-\gamma^2}{2\gamma} H^{0i}_a \\
&\implies H^{0i}_a = \frac{N}{\gamma} e^i_a + \gamma N^b \mathbb{P}(\gamma, +)^i_{ba} \\
\text{(ii)} &\implies - N \frac{1 - \gamma^2}{2} e^i_a - \frac{1 - \gamma^2}{2} N^b \mathbb{P}(\gamma, +)^i_{ba} = \frac{\gamma^2 - 1}{4} \epsilon^i_{\ jk} H^{jk}_a \\
&\implies \frac{1}{2} \epsilon^{i}_{\ jk} H^{jk}_a = N e^i_a + N^b \mathbb{P}(\gamma, +)^i_{ba}
\end{aligned}
$$

Thus, we have parameterized the Plebanski constraints in terms of $\mathbb{P}(\gamma, +)^i_{ab}$, a scalar lapse $N$, shift vector $N^a \in T(\Sigma_t)$, and the 3 parameters in the choice of an internal direction $n^I = (1, 0, 0, 0)$. These sum up to $9 + 1 + 3 + 3 = 16$ parameters, which is exactly the 16 degrees of freedom in the co-tetrad $e^I_\mu$.

The constraints are "simple" constraints and they must be conserved in time. By arXiv:0902.3416 [gr-qc], this follows from

$$
\mathbb{C}^{ij} = e^{(j} \dot{\mathbb{P}}(\gamma, -)^{i)} \propto N e^{(j}\wedge \left[\mathrm{d}e^{i)} + \frac{1}{2}\epsilon^{i)}_{\ \ \ lm}\left({}^+\mathbb{A} + {}^-\mathbb{A}\right)^l\wedge e^{m} \right]\approx 0.
$$

Together with $\mathbb{B}^i \approx 0$, these 9 constraints are equivalent to

$$
\mathbb{IV}^i_a = \frac{1}{2} ({}^{+}\mathbb{A} + {}^{-}\mathbb{A})_a^i - \Gamma_a^i(e) = 0.
$$

Where $\Gamma_a^i$ is the spin connection compatible with the triad $e$, i.e., the solution to

$$
\partial_{[a} e_{b]}^i + \epsilon^i_{\ jk} \Gamma_{[a}^j e_{b]}^k = 0.
$$

We can also calculate the Poisson bracket:

$$
\{ \mathbb{IV}^i_a(x), \mathbb{P}(\gamma, -)^j_{bc}(y) \} = \frac{1}{2} \epsilon_{abc} \delta^{ij} \delta(x-y).
$$

Which makes them secondary constraints. By setting them strongly to zero, we define $K_a^i = ({}^{+}\mathbb{A}^i_a - {}^{-}\mathbb{A}^i_a)/2$, such that:

$$
{}^{+}\mathbb{A}_a^i = \Gamma_a^i + \gamma K_a^i =: A_a^i.
$$

The action is then reduced to:

$$
\begin{aligned}
S[\mathbb{P}(\gamma, +), {}^{+}\mathbb{A}, N, N_i]
&= \frac{1}{\kappa} \int dt \int_{\Sigma} \Big( \mathbb{P}(\gamma, +)_i \wedge {}^+\dot{\mathbb{A}}^i \\
&+ N_i \mathcal{D}_{A} \wedge \mathbb{P}(\gamma, +)^i + \epsilon^i_{\ jk} N^j \mathbb{P}(\gamma, +)^k \wedge (\gamma F_{0i} + F^{jk}\epsilon_{ijk}) \\
&+ Ne^i \wedge (\frac{F_{0i}}{\gamma} +  F^{jk}\epsilon_{ijk} )\Big).
\end{aligned}
$$

This is the standard Hamiltonian formulation of general relativity in terms of SU(2) connection variables $A_a^i$. If we now introduce the densitized triad

$$
E^a_i = \gamma \epsilon^{abc} \mathbb{P}(\gamma, +)_{bc}^i,
$$

The Poisson bracket between $E^a_i$ and $A^j_b$ is now

$$
\{E^a_i(x), A^j_b(y)\} = \kappa \delta^a_b \delta^j_i \delta(x-y), \quad \{E^a_i(x), E^b_j(y)\} = \{A^i_a(x), A^j_b(y)\} = 0.
$$

And the action takes the familiar Ashtekar-Barbero form:

$$
\begin{aligned}
S[E, A, N, N^i, N_i] &= \frac{1}{\gamma\kappa} \int dt \int_{\Sigma_t} d^3x \Big[ E^a_i \dot{A}^i_a - N^b V_b(E^a_i, A^i_a) \\
&- N S(E^a_i, A^i_a) - N^i G_i(E^a_i, A^i_a) \Big]
\end{aligned}
$$

With the constraints

$$
\begin{cases}
V_b = E^a_j F^j_{ab} - (1+\gamma^2)K^i_b G_i \\
S = \frac{E^a_i E^b_j}{\sqrt{|\det E|}} \left( \epsilon^{ij}_{\ \ k} F^k_{ab} - 2(1+\gamma^2)K^i_{[a} K^j_{b]} \right) \\
G_i = \mathcal{D}_a E^a_i
\end{cases}
$$

These three constraints completely dictate both the symmetries and the dynamics of General Relativity. Because it is a fully constrained system, its Hamiltonian is simply a linear combination of these constraints. Physically, they can be interpreted as follows:

#### 1. The Gauss Constraint ($G_i \approx 0$)

This is the non-Abelian equivalent of Gauss's Law from Yang-Mills theory ($\nabla \cdot \vec{E} = 0$). Here, $E^a_i$ acts as the electric field conjugate to the connection $A_a^i$. It generates local $SU(2)$ internal gauge rotations. By setting $G_i \approx 0$, we ensure that the physical state of the universe is independent of how we locally orient our internal 3D reference frame (the target space of the triads). Picking a different internal $SU(2)$ basis at any point in space doesn't change the physical geometry.

#### 2. The Vector Constraint ($V_b \approx 0$)

In the action, this constraint is multiplied by the shift vector $N^b$. It is the generator of spatial diffeomorphisms upon the 3D slice $\Sigma$. Setting $V_b \approx 0$ enforces the principle that coordinates are arbitrary—if you stretch, twist, or remap the spatial coordinate grid on $\Sigma$, the underlying physical geometry remains exactly the same. The $E^a_j F^j_{ab}$ term essentially comes from the Lie derivative of the connection along the spatial slice, while the $- (1+\gamma^2)K^i_b G_i$ part is a proportional correction term.

#### 3. The Scalar Constraint ($S \approx 0$)

In the action, this is multiplied by the scalar lapse function $N$. This constraint generates "time evolution," which in General Relativity corresponds to deforming the spatial slice $\Sigma_t$ forward in the normal direction into the 4D spacetime bulk. Because this must also vanish ($S \approx 0$), it embodies the fact that there is no absolute background time in GR. This is the core dynamical equation of General Relativity.
