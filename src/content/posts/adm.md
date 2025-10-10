---
title: ADM Action
date: 2025-10-10
summary: 3 + 1 = 4
category: 笔记
tags: [数学, 物理, 广义相对论, 微分几何]
---

&emsp;&emsp;出于朴素的好奇心，我们想考虑哈密顿体系下的广义相对论。我们遇到的第一个难点就是，既然在广义相对论中我们的时间和空间是耦合在一起的，我们该如何计算广义速度等等与时间有关的量？幸运的是，对于一个足够好的时空流形（简单来说，“足够好”意味着我们在这个流形上能够找出合法的柯西面），我们总能对其做分解：$M \cong \mathbb{R}\times \sigma$. 这也就是说，

$$
\forall t \in \mathbb{R},\quad \exists X_t : \sigma \to M. \quad(X_t(x):= X(t,x))
$$

其中$X^\mu$是$M$上选定一个坐标系后的坐标，$x^a$是$\sigma$上的坐标，$\mu = 1,2,3,\cdots, D+1, \quad a = 1,2,3,\cdots, D$.我们可以发现，这时对时空流形的分解是**依赖于坐标系的**；因此，对于$M$的一个微分同胚变换$\varphi$，有

$$
X^\prime = \varphi\circ X \Rightarrow \varphi = X^\prime \circ X^{-1}.
$$

这也就意味着$M$的微分同胚不变性等价于我们取分解$X$时的任意性。

&emsp;&emsp;接下来我们对这个分解做参数化。考虑一个形变向量场

$$
T^\mu(X):= \left(\frac{\partial X^\mu(t,x)}{\partial t}\right) =: N(X)n^\mu(X) + N^\mu(X).
$$

其中$N^\mu(X)$是$\Sigma_t$上的基矢量，衡量$\Sigma_t$上$x^a$点相对于$\Sigma_{t^\prime}$上$x^a$点的空间位移；$n^\mu(X)$是$\Sigma_t$法线方向上的单位矢量，$N(X)n^\mu(X)$“连接”两个相邻的超曲面，系数$N(X)$衡量的是固有时$t$流逝的速率：

$$
\Sigma_t \to \Sigma_{t+dt}: \Delta t = Ndt.
$$

他们有如下性质：

$$
g_{\mu\nu}n^\mu n^\nu = s, \quad g_{\mu\nu}N^\mu X^\nu_{,a} = 0.
$$

我们还能发现，$n^\mu$正比于一个1-形式：$n = Fdf$.鉴于以上原因，我们称$N^\mu(X)$为**_shift_**，$n^\mu(X)$为**_lapse_**。

&emsp;&emsp;我们先观察一下正常的E-H作用量：

$$
S = \int d^{D+1}x\sqrt{|det(g)|}R^{(D+1)}.
$$

为了能够分离出时间和空间，我们需要分解的是体元$d^{D+1}x\sqrt{det(g)}$和曲率$R^{(D+1)}$.这两者都依赖于$M$中的度规张量，因此我们应该试图构建一个$\Sigma$上的张量微积分系统，然后再考虑怎么用其上的张量表示这两个部分。

&emsp;&emsp;我们考虑一个任意的嵌入$X:\sigma\to M$，$\Sigma = X(\sigma)$，并有法向量$n^\mu(X)$.我们定义两个张量：

$$
q_{\mu\nu} = g_{\mu\nu} - sn_\mu n_\nu, \quad K_{\mu\nu} = q_\mu^\rho q_\nu^\sigma\nabla_\rho n_\sigma.
$$

其中$\nabla$是与$g$适配的导数算符，$s$指代时空的类型。在之后的推导中，我们取$s = -1$.我们立刻可以发现，这两个张量都是“纯空间的”；或者说，他们都在$\Sigma$上。这是因为，$q$和$K$的任意一个指标和$n^\mu$缩并都得0：

$$
q_{\mu\nu}n^\nu = g_{\mu\nu}n^\nu - sn_\mu n_\nu n^\nu = (1-s^2)n^\mu = 0.
$$

$K$同理。另一个非常有用的性质是，$K$的两个角标是对易的：

$$
\begin{aligned}
    K_{[\mu\nu]}
    &=  q_{[\mu}^\rho q_{\nu]}^\sigma\nabla_\rho n_\sigma
    =  q_\mu^\rho q_\nu^\sigma(\nabla_\rho n_\sigma - \nabla_\sigma n_\rho),\\
    &=  q_\mu^\rho q_\nu^\sigma[\nabla_\rho(F\nabla_\sigma f) - \nabla_\sigma(F\nabla_\rho f)],\\
    &=  q_\mu^\rho q_\nu^\sigma[(\nabla_{[\rho}F)(\nabla_{\sigma]}f) + F\nabla_{[\rho}\nabla_{\sigma]}f],\\
    &=  q_\mu^\rho q_\nu^\sigma[\nabla_{[\rho}(\ln F)(F\nabla_{\sigma]}f) + F\nabla_{[\rho}\nabla_{\sigma]}f],\\
    &=  q_\mu^\rho q_\nu^\sigma[\nabla_{[\rho}(\ln F)n_{\sigma]} + F\nabla_{[\rho}\nabla_{\sigma]}f] = 0.
\end{aligned}
$$

这就导致

$$
2K_{\mu\nu} = 2K_{(\mu\nu)} + 2K_{[\mu\nu]} = 2K_{(\mu\nu)} = 2q_\mu^\rho q_\nu^\sigma(\mathcal{L}_n q)_{\rho\sigma}.
$$

如果我们考虑一个纯空间的向量$v^\nu$，由于$v^\nu n_\nu = 0$，我们可以立刻得到

$$
q_{\mu\nu}v^\mu v^\nu = g_{\mu\nu}v^\mu v^\nu.
$$

这告诉我们$q$其实是$\Sigma$上的一个度规。如果再观察$q$的具体形式，我们可以发现$q$实际上是一个投影算符；它将所有的张量投影到$\Sigma$上，并且不同角标独立投影。因此，由于李导数已经显然是纯空间的了，那么$q$就退化成了delta函数.再代入$n^\mu = (T^\mu - N^\mu)/N$，有

$$
(\mathcal{L}_n q)_{\mu\nu} = \frac{1}{N}(\mathcal{L}_{T-N} q)_{\mu\nu} + (\partial_\mu \frac{1}{N})q_{\rho\nu}n^\rho + (\partial_\nu \frac{1}{N})q_{\rho\mu}n^\rho = \frac{1}{N}(\mathcal{L}_{T-N} q)_{\mu\nu}.
$$

&emsp;&emsp;因此我们可以自然的考虑一个与$q$适配的导数算符：

$$
D_\mu q_{\nu\rho} = 0, \quad D_{[\mu}D_{\nu]}f = 0.
$$

我们也有显然的指标变换公式：

$$
D_\mu f = q^\nu_\mu\nabla_\nu f, \quad D_\mu u_\nu = q^\rho_\mu q^\sigma_\nu\nabla_\rho\tilde{u}_\sigma.
$$

&emsp;&emsp;构造导数算符的目的是为了导出$R^{(D)\,\sigma}_{\mu\nu\rho}$. 先不考虑协变导数的对易子，而是

$$
\begin{aligned}
    D_\mu D_\nu u_\rho
    &=  q^{\mu^\prime}_\mu q^{\nu^\prime}_\nu q^{\rho^\prime}_\rho \nabla_{\mu^\prime}D_{\nu^\prime}u_{\rho\prime}\\
    &=
\end{aligned}
$$
