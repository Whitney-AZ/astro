---
title: Lorentz Currents
date: 2024-12-12
summary: A Problem from Schwartz's QFT Book.
category: 笔记
tags: [数学, 物理, 量子场论]
---

### Lorentz Currents

&emsp;A global lorentz transformation $x^\mu \to \Lambda^\mu_{\ \,\nu}x^\nu$ should produce a conserved current $K$. Now we try to derive such a current.

Consider a infinitesimal lorentz transformation

$$
\Lambda^\mu_{\ \,\nu} = I^\mu_{\ \,\nu} + \frac{1}{2}\omega_{\alpha\beta}J^{\alpha\beta\mu}_{\quad\ \,\nu} + \cdots
$$

where $J$ is antisymmetric in the first two indices :

$$
J^{\alpha\beta\mu}_{\quad\ \,\nu} = -J^{\beta\alpha\mu}_{\quad\ \,\nu}
$$

then $\delta x^\mu$ is the difference between such a small spin and the original $x^\mu$, that is

$$
\delta x^\mu = \frac{1}{2}\omega_{\alpha\beta}J^{\alpha\beta\mu}_{\quad\ \,\nu}x^\nu.
$$

&emsp;Now we turn to look at the arbitrary current $J^\mu$. Such a current must satisfy $\partial_\mu J^\mu = 0$, which lead to

$$
\partial_\mu \left[\mathcal{L}\delta x^\mu + \frac{\partial \mathcal{L}}{\partial(\partial_\mu\phi)}\delta\phi \right] = 0
$$

it is then obvious that

$$
\delta\phi = \phi(x^\mu) - \phi(\Lambda^\mu_{\ \,\nu}x^\nu)  = -\frac{1}{2}\omega_{\alpha\beta}J^{\alpha\beta\mu}_{\quad\ \,\nu}x^\nu\partial_\mu\phi
$$

then the whole equation becomes

$$
\partial_\mu\left[\frac{\partial \mathcal{L}}{\partial(\partial_\mu\phi)}\partial_\lambda\phi\omega_{\alpha\beta}J^{\alpha\beta\lambda}_{\quad\ \,\nu}x^\nu - \mathcal{L}\omega_{\alpha\beta}J^{\alpha\beta\mu}_{\quad\ \,\nu}x^\nu\right] =0
$$

consider an antisymmetric tensor $g_{\mu\nu}$. We will have the following:

$$
\begin{aligned}
    g_{\mu\nu}x^\mu x^\nu
    &=  \left[\frac{1}{2}(g_{\mu\nu} + g_{\nu\mu}) + \frac{1}{2}(g_{\mu\nu} - g_{\nu\mu})\right]x^\mu x^\nu\\
    &=  \frac{1}{2}(g_{\mu\nu}x^\mu x^\nu - g_{\nu\mu}x^\mu x^\nu)\\
    &=  \frac{1}{2}g_{\mu\nu}(x^\mu x^\nu - x^\nu x^\mu).
\end{aligned}
$$

Then the whole current-conservation-equation will become

$$
\begin{gathered}
    \partial_\mu\omega_{\nu\lambda}\left[\frac{\partial \mathcal{L}}{\partial(\partial_\mu\phi)}\partial^\lambda\phi x^\nu - \frac{\partial \mathcal{L}}{\partial(\partial_\mu\phi)}\partial^\nu\phi x^\lambda - \mathcal{L}g^{\lambda\mu}x^\nu + \mathcal{L}g^{\nu\mu}x^\lambda\right] =0\\
    \partial_\mu\omega_{\nu\lambda}\left[\left(\frac{\partial \mathcal{L}}{\partial(\partial_\mu\phi)}\partial^\lambda\phi-  \mathcal{L}g^{\lambda\mu}\right)x^\nu - \left(\frac{\partial \mathcal{L}}{\partial(\partial_\mu\phi)}\partial^\nu\phi  - \mathcal{L}g^{\nu\mu}\right)x^\lambda\right] =0\\
    \partial_\mu\omega_{\nu\lambda}\left[T^{\mu\lambda}x^\nu - T^{\mu\nu}x^\lambda\right] = 0\\
    \omega_{\nu\lambda}\left(T^{\mu\lambda}x^\nu - T^{\mu\nu}x^\lambda\right) = J^\mu
\end{gathered}
$$

in which we used the fact that

$$
J^{\alpha\beta\mu}_{\quad\ \,\nu} = J^{\alpha\beta}_{\quad\lambda\nu}g^{\mu\lambda} = (\delta^\alpha_\lambda\delta^\beta_\nu - \delta^\alpha_\nu\delta^\beta_\lambda)g^{\mu\lambda}.
$$

Having $\omega$ as an arbitrary parameter, the part inside the brackets is a conserved tensor as well, namely

$$
\partial_\mu\left(T^{\mu\lambda}x^\nu - T^{\mu\nu}x^\lambda\right) = 0 \Longrightarrow \partial_\mu K^{\mu\nu\lambda} = 0
$$

where the $K^{\mu\nu\lambda}$ is our Lorentz Current.
