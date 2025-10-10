---
title: 克氏符到底是什么？
date: 2025-05-19
summary: 关于主丛上的联络的一般讨论
category: 笔记
tags: [数学, 物理, 微分几何]
---

&emsp;&emsp;在梁老的熏陶下，我们从小学二年级时就已经知道克氏符$\Gamma$不是一个张量，因为在坐标变换下，克氏符的变换规则是

$$
\bar{\Gamma}^i_{\ \mu j} = \frac{\partial \bar{x}^i}{\partial x^k}\frac{\partial x^l}{\partial \bar{x}^j}\frac{\partial x^\nu}{\partial \bar{x}^\mu}\Gamma^k_{\ \nu l} + \frac{\partial \bar{x}^i}{\partial x^k}\frac{\partial^2 \bar{x}^k}{\partial x^\mu \partial \bar{x}^j}
$$

而一般的张量的变换规则应该是

$$
\bar{T}^i_{\ \mu j} = \frac{\partial \bar{x}^i}{\partial x^k}\frac{\partial x^l}{\partial \bar{x}^j}\frac{\partial x^\nu}{\partial \bar{x}^\mu}T^k_{\ \nu l}
$$

可以发现，正是克氏符变换规则多出来的一个看起来很奇怪的项让克氏符有别于一般的张量，而变成了一个“赝张量”。果真如此吗？在探讨这个问题之前，我们先来从纤维丛的角度重新考虑一下克氏符。

---

&emsp;&emsp;设$x(\tau)$是$M$中的一条曲线，$S(x)$是一般向量丛的一个截面，也就是$M$上的一个向量场。向量丛上的联络亦可以用平行移动来定义；也就是说，如果截面满足$\nabla_{\frac{\mathrm{d}}{\mathrm{d}\tau}}S = 0$，那么我们就称$S$沿$x(\tau)$平行移动，于是就有

$$
\nabla_{\frac{\mathrm{d}}{\mathrm{d}\tau}}S = \nabla_{\frac{\mathrm{d}}{\mathrm{d}\tau}}(e_iz^i) = \nabla_{\frac{\mathrm{d}}{\mathrm{d}\tau}}e_iz^i + e_i\nabla_{\frac{\mathrm{d}}{\mathrm{d}\tau}}z^i = 0
$$

其中$e_i$是向量丛的一个标架，$z^i$是截面的分量。注意到有关系$\frac{\mathrm{d}}{\mathrm{d}\tau} = \frac{\mathrm{d}x^\mu}{\mathrm{d}\tau}\frac{\partial }{\partial x^\mu}$，因此按照协变微分算符的定义，上式第一项就是

$$
\begin{aligned}
    \nabla_{\frac{\mathrm{d}}{\mathrm{d}\tau}}e_iz^i
    &=  \langle\nabla e_i, \frac{\mathrm{d}x^\mu}{\mathrm{d}\tau}\frac{\partial }{\partial x^\mu}\rangle z^i \\
    &=  \langle e_j\bar{\Gamma}^j_{\ \nu i}\mathrm{d}x^\nu, \frac{\mathrm{d}x^\mu}{\mathrm{d}\tau}\frac{\partial }{\partial x^\mu}\rangle z^i \\
    &=  e_j\bar{\Gamma}^j_{\ \mu i}\frac{\mathrm{d}x^\mu}{\mathrm{d}\tau}z^i
\end{aligned}
$$

第二项更简单：

$$
\begin{aligned}
    e_i\nabla_{\frac{\mathrm{d}}{\mathrm{d}\tau}}z^i
    &=  \langle\nabla z^i, \frac{\mathrm{d}x^\mu}{\mathrm{d}\tau}\frac{\partial }{\partial x^\mu}\rangle e_i\\
    &=  \langle \frac{\partial z^i}{\partial x^\nu}\mathrm{d}x^\nu, \frac{\mathrm{d}x^\mu}{\mathrm{d}\tau}\frac{\partial }{\partial x^\mu}\rangle e_i\\
    &=  \frac{\partial z^i}{\partial x^\mu}\frac{\mathrm{d}x^\mu}{\mathrm{d}\tau}e_i
\end{aligned}
$$

于是两项加在一起就是

$$
\begin{aligned}
    \nabla_{\frac{\mathrm{d}}{\mathrm{d}\tau}}S &= \nabla_{\frac{\mathrm{d}}{\mathrm{d}\tau}}e_iz^i + e_i\nabla_{\frac{\mathrm{d}}{\mathrm{d}\tau}}z^i \\
    &=  e_j\Gamma^j_{\ \mu i}\frac{\mathrm{d}x^\mu}{\mathrm{d}\tau}z^i + \frac{\partial z^i}{\partial x^\mu}\frac{\mathrm{d}x^\mu}{\mathrm{d}\tau}e_i \\
    &=  e_j\frac{\mathrm{d}x^\mu}{\mathrm{d}\tau}\left(\Gamma^j_{\ \mu i}z^i + \frac{\partial z^j}{\partial x^\mu}\right) = 0.
\end{aligned}
$$

注意到这一形式与流行上的平行移动的形式完全相同，于是我们就可以等价的认为$\Gamma^j_{\ \mu i}$也是向量丛上的联络。更严格一些，$\Gamma^j_{\ \mu i}$是联络1-形式$\Gamma^j_{\ i} = \Gamma^j_{\ \mu i}\mathrm{d}x^\mu$的分量。

&emsp;&emsp;更一般而言，$\Gamma$是标架丛上的联络，也就是说他在接受一个向量之后指导标架的变换关系，这一点和普通的联络类似。然而在标架丛上一般线性变换也可以进行标架变换：$f \to gf, g\in GL(n)$，所以事实上联络就是一个李代数取值的1-形式，就可以做展开：$\Gamma = \Gamma_\mu\mathrm{d}x^\mu$，此时$\Gamma^\mu \in \mathfrak{gl}(n)$。在李代数的局部标架下又可以做展开，进而得到$\Gamma_\mu = (\Gamma_\mu)^i_{\ j}\partial_i\otimes\mathrm{d}x^j$。这说明，当我们写出$(\Gamma_\mu)^i_{\ j}$之类具有三个指标的克氏符（分量）时，其实是固定了标架丛上的坐标系而取的分量，此时就无法再按照一个(1,2)型张量场做变换了。我们又可以进一步发现，此时克氏符的分量取值也不再是李代数，而是李代数某一矩阵的一个矩阵元，变成了一个实数。

&emsp;&emsp;接下来我们考虑联络的变换规律。考虑一般的联络$\omega$，标架（场）$e$，因此就有$\mathrm{d}e = e\omega(e)$，或者写作分量形式$\mathrm{d}e_\alpha = e_\beta\omega^\beta_{\ \alpha}$。再考虑一个可逆的矩阵$g$，它将标架$e$变为新标架$e^\prime$，也就是有$e^\prime = eg$。对其外微分，得到

$$
\mathrm{d}e^\prime = (\mathrm{d}e)g + e(\mathrm{d}g)
$$

而$LHS = e^\prime\omega(e^\prime) = e^\prime\omega(eg)$，这就意味着

$$
\begin{gathered}
    e^\prime\omega(eg) = e\omega(e)g + e\mathrm{d}g\\
    eg\omega(eg) = e\omega(e)g + e\mathrm{d}g\\
    \omega(eg) = g^{-1}\omega(e)g + g^{-1}\mathrm{d}g.
\end{gathered}
$$

这也说明联络的变换确实不像张量一样变换；其多了一个非齐次项$g^{-1}\mathrm{d}g$，因此联络也算是某种“规范势”。由此我们可以倒过来推得克氏符分量的变换方式。

&emsp;&emsp;在这种情况下，$\omega = \Gamma = \Gamma_\mu\mathrm{d}x^\mu$，规范变换在标架下展开可以写作

$$
g = g^i_{\ j}\partial_i\otimes \mathrm{d}x^j = \frac{\partial x^i}{\partial \bar{x}^j}\partial_i\otimes \mathrm{d}x^j,\qquad g^{-1} = \frac{\partial \bar{x}^i}{\partial x^j}\partial_i\otimes \mathrm{d}x^j
$$

而$\mathrm{d}g$项是规范变换在切丛上的微分，应该按流形上的坐标展开：$\mathrm{d}g = (\bar{\partial}_\mu g)\mathrm{d}\bar{x}^\mu$。有了这些准备，变换就可以写成

$$
\begin{gathered}
    \bar{\Gamma}_\mu\mathrm{d}\bar{x}^\mu = (g^{-1})^i_k\partial_i\otimes \mathrm{d}x^k\Gamma_\nu\mathrm{d}x^\nu  g^k_j\partial_k\otimes \mathrm{d}x^j + (g^{-1})^i_k\partial_i\otimes \mathrm{d}x^k(\bar{\partial}_\mu g)\mathrm{d}\bar{x}^\mu\\

    \bar{\Gamma}_\mu = (g^{-1})^i_k\partial_i\otimes \mathrm{d}x^k\Gamma_\nu g^\nu_\mu  g^k_j\partial_k\otimes \mathrm{d}x^j + (g^{-1})^i_k\partial_i\otimes \mathrm{d}x^k(\bar{\partial}_\mu g^k_j\partial_k\otimes \mathrm{d}x^j)\\

    (\bar{\Gamma}_\mu)^i_j = (g^{-1})^i_k(\Gamma_\nu)^k_lg^\nu_\mu  g^k_j + (g^{-1})^i_k\bar{\partial}_\mu g^k_j\\

    (\bar{\Gamma}_\mu)^i_j = \frac{\partial x^\nu}{\partial \bar{x}^\mu}\frac{\partial \bar{x}^i}{\partial x^k}  \frac{\partial x^k}{\partial \bar{x}^j}(\Gamma_\nu)^k_l + \frac{\partial \bar{x}^i}{\partial x^k}\frac{\partial}{\partial \bar{x}^\mu}\left(\frac{\partial x^k}{\partial \bar{x}^j}\right)\\

    \bar{\Gamma}^i_{\ \mu j} = \frac{\partial x^\nu}{\partial \bar{x}^\mu}\frac{\partial \bar{x}^i}{\partial x^k} \frac{\partial x^k}{\partial \bar{x}^j}\Gamma_{\ \nu l}^k + \frac{\partial \bar{x}^i}{\partial x^k}\frac{\partial^2 x^k}{\partial \bar{x}^\mu\partial \bar{x}^j}.
\end{gathered}
$$

这即是克氏符分量的变换式。可以注意到对待$i,j$指标和$\mu$指标时的差别。

&emsp;&emsp;用类似的方法，我们还可以证明曲率2-形式是一个张量。我们已知曲率2-形式可以写作

$$
\Omega = \mathrm{d}\omega + \omega\wedge\omega
$$

因此，考虑$\bar{\omega} = g^{-1}\omega g + g^{-1}\mathrm{d}g$

$$
\begin{aligned}
    \bar{\Omega}
    &=  \mathrm{d}\bar{\omega} + \bar{\omega}\wedge\bar{\omega}\\
    &=  \mathrm{d}(g^{-1}\omega g + g^{-1}\mathrm{d}g) + (g^{-1}\omega g + g^{-1}\mathrm{d}g)\wedge(g^{-1}\omega g + g^{-1}\mathrm{d}g)\\
    &=\;\!{\color{red}-\;g^{-1}\mathrm{d}gg^{-1}\wedge\omega g} + g^{-1}\mathrm{d}\omega g \;{\color{blue}-\;g^{-1}\omega\wedge\mathrm{d}g} + g^{-1}\omega g\wedge g^{-1}\omega g\\
    &\quad\;\!{\color{green}\;-\;g^{-1}\mathrm{d}gg^{-1}\wedge\mathrm{d}g}
    {\color{blue}\;+\;g^{-1}\omega g\wedge g^{-1}\mathrm{d}g} \;{\color{red}+\;g^{-1}\mathrm{d}g\wedge g^{-1}\omega g} \\
    &\quad\;\!{\color{green}\;+\;g^{-1}\mathrm{d}g\wedge g^{-1}\mathrm{d}g}\\
    &=  g^{-1}(\mathrm{d}\omega + \omega\wedge\omega)g = g^{-1}\Omega g.
\end{aligned}
$$

曲率的变化只有齐次项，是规范不变的，因此是一个张量场的分量。
