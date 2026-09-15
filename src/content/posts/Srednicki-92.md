---
title: 'Srednicki §92 孤子与磁单极子'
date: 2026-09-14
category: 笔记
tags: [物理, 量子场论, Srednicki]
series: 'Srednicki QFT'
srednickiSections: [92]
hideFromHome: true
draft: false
---

<span id="c92"></span>

前面讨论自发破缺时，我们在一个常值真空附近展开场，研究小振动所对应的粒子。现在来考察另一类构型：场在远处仍趋向真空，但沿不同的空间方向趋向不同的真空值。这样的场不能处处接近同一个常值真空；如果它的总能量有限，而且能够保持自己的形状，就会像一个新的粒子一样运动。我们先在一空间维找出一个精确解，再看规范场怎样使类似的构型出现在二、三空间维。

本节接续第84节的对称性破缺。以下三个模型各自定义自己的$v,\lambda$，量纲随时空维数改变。复场涡旋与实三重态单极子的质量，将分别从各自的二次作用量读出。

<span id="c92-kink"></span>

## 从两个真空之间的插值求出孤子

考虑一个实标量场，
<span id="eq:c92-real-model"></span>

$$
\mathcal L=-\frac12\partial^\mu\varphi\,\partial_\mu\varphi
-\frac{\lambda}{8}(\varphi^2-v^2)^2,
\qquad \lambda>0,\quad v>0.
\tag{92.1}
$$

势在$\varphi=\pm v$取零；例如令$\varphi=v+h$，
<span id="eq:c92-kink-mass"></span>

$$
V(v+h)=\frac12\lambda v^2h^2
+\frac12\lambda vh^3+\frac{\lambda}{8}h^4,
\qquad m^2=V''(v)=\lambda v^2.
\tag{92.2}
$$

在另一个真空附近，三次项反号，二次项相同。先取一个空间坐标$x$和时间$t$。作用量无量纲，动能便要求$[\varphi]=[v]=0$、$[\lambda]=2$；在动量尺度$m$处，微扰展开的小参数为$\lambda/m^2=1/v^2$。

一维空间的两个远端可以分别取$\varphi=-v$和$\varphi=+v$。若两端取同一真空，常值场已使能量为零；若取
<span id="eq:c92-kink-boundary"></span>

$$
\varphi(-\infty)=-v,\qquad \varphi(+\infty)=+v,
\tag{92.3}
$$

场就必须在中间经过势垒。我们要找这个固定边界条件下能量最低的构型。由正则动量$\Pi=\dot\varphi$，
<span id="eq:c92-kink-energy"></span>

$$
\mathcal H=\Pi\dot\varphi-\mathcal L
=\frac12\dot\varphi^2+\frac12\varphi'^2+V(\varphi),
\qquad
E=\int_{-\infty}^{\infty}dx\,\mathcal H.
\tag{92.4}
$$

时间导数项非负，最低能量解可以取为静态。把余下两项配成平方，
<span id="eq:c92-kink-square"></span>

$$
\begin{aligned}
E&=\frac12\int dx\,\bigl(\varphi'-\sqrt{2V(\varphi)}\bigr)^2
  +\int dx\,\sqrt{2V(\varphi)}\,\varphi',\\
\int dx\,\sqrt{2V(\varphi)}\,\varphi'
 &=\int_{-v}^{v}d\varphi\,\frac{\sqrt\lambda}{2}(v^2-\varphi^2)\\
 &=\frac{\sqrt\lambda}{2}
   \left[v^2\varphi-\frac{\varphi^3}{3}\right]_{-v}^{v}
 =\frac23\sqrt\lambda\,v^3
 =\frac{2m^3}{3\lambda}\equiv M .
\end{aligned}
\tag{92.5}
$$

第二项是$\sqrt{2V}$的原函数在两端之差，因此它只由边界决定。这里不要求试探场在中间一直单调；即使它来回经过同一场值，往返的原函数增量也相消。根号在整个实轴上为$\sqrt\lambda\,|\varphi^2-v^2|/2$，只有最后的端点积分位于$[-v,v]$，才写成第二行的多项式。

于是$E\ge M$。要达到下界，必须令平方逐点为零。在两真空之间，
<span id="eq:c92-kink-integrate"></span>

$$
\frac{d\varphi}{dx}=\frac{\sqrt\lambda}{2}(v^2-\varphi^2),
\qquad
\frac{1}{2v}\log\frac{v+\varphi}{v-\varphi}
=\frac{\sqrt\lambda}{2}(x-x_0).
\tag{92.6}
$$

左边可由$1/(v^2-\varphi^2)=[(v-\varphi)^{-1}+(v+\varphi)^{-1}]/(2v)$直接积分得到。解出$\varphi$便有
<span id="eq:c92-kink-profile"></span>

$$
\varphi_{\mathrm k}(x)=v\tanh\frac{m(x-x_0)}2,\qquad
\mathcal E_{\mathrm k}(x)
=\varphi_{\mathrm k}'{}^2
=\frac{v^2m^2}{4}\operatorname{sech}^4\frac{m(x-x_0)}2.
\tag{92.7}
$$

一阶方程再求导给$\varphi''=V'(\varphi)$，所以它也满足原来的静态场方程。若令$z=\tanh[m(x-x_0)/2]$，密度的积分变成
<span id="eq:c92-kink-integral"></span>

$$
\int dx\,\mathcal E_{\mathrm k}
=\frac{v^2m}{2}\int_{-1}^{1}(1-z^2)\,dz
=\frac23mv^2=M.
\tag{92.8}
$$

这同时检验了归一。能量集中在$x_0$附近，远处按$e^{-2m|x-x_0|}$衰减；位置$x_0$不改变总能量。这样的解称为孤子（soliton），此处的具体形状也称扭结（kink）。交换两个边界值，就得到反扭结。固定边界扇区内，式[（92.5）](#eq:c92-kink-square)保证能量不会低于$M$；平移后的扭结仍达到相同下界，而使平方非零的变形增加能量。它不能连续变成某个常值真空而仍保持两端条件。边界条件、能量配方和孤子解由此连在一起。

<span id="c92-kink-motion"></span>

## 推动后的能量、动量与畴壁

静态轮廓记作$\psi(\xi)$。由于原作用量具有洛伦兹对称性，以速度$u$运动的解为
<span id="eq:c92-kink-boost"></span>

$$
\varphi(x,t)=\psi(\xi),\qquad
\xi=\gamma(x-x_0-ut),\qquad
\gamma=(1-u^2)^{-1/2},\quad |u|<1 .
\tag{92.9}
$$

速度在这里记为$u$，以便与后面的耦合比区别。现在$\dot\varphi=-\gamma u\psi'$、$\partial_x\varphi=\gamma\psi'$，而静态一阶方程给$V(\psi)=\psi'^2/2$。在固定$t$的积分中，$dx=d\xi/\gamma$，因此
<span id="eq:c92-kink-four-momentum"></span>

$$
\begin{aligned}
E&=\frac{1}{2\gamma}
 \bigl[\gamma^2u^2+\gamma^2+1\bigr]\int d\xi\,\psi'^2
 =\gamma M,\\
p&=\int dx\,T^{01}
 =\int dx\,(-\dot\varphi\,\partial_x\varphi)
 =\gamma u M,\\
E^2-p^2&=M^2.
\end{aligned}
\tag{92.10}
$$

动量密度的负号来自$\partial^0=-\partial_t$。能量式中的系数用$1=\gamma^2(1-u^2)$化简，恰好给$\gamma$，并没有额外的长度收缩因子。

孤子的平移与推动因而具有质量为$M$的粒子所应有的运动学。在弱耦合时，$M/m=2m^2/(3\lambda)\gg1$；它比常值真空附近的基本激发重得多。这使我们预期量子理论还会有与孤子相联系的重粒子态。这里求出的$M$是经典领头值；若要计算它的量子质量，还需量子化平移自由度及轮廓附近的涨落。

把同一轮廓放到更高维，并令它不依赖另外的空间坐标，就得到畴壁（domain wall）。对横向坐标的积分只给壁的面积，所以单位面积的能量为
<span id="eq:c92-wall-tension"></span>

$$
\sigma=\int dx\left[\frac12\varphi'^2+V(\varphi)\right]
=\frac{2m^3}{3\lambda}.
\tag{92.11}
$$

例如四维时空中$[\lambda]=0$，故$[\sigma]=3$，正是能量除以面积的量纲。壁沿横向无限延伸时总能量无限，但张力有限；原来的一维局域解仍决定它的横截面。

<span id="c92-winding"></span>

## 从真空圆到缠绕数

若要在两个空间方向都局域，远处的边界就成为一个圆。圆是连通的，连续映射到两个离散真空时只能始终取同一个值，因而前面的双阱模型不再给出同样的边界构造。为得到连续的真空方向，改取复标量，
<span id="eq:c92-complex-model"></span>

$$
\mathcal L=-\partial^\mu\varphi^\dagger\partial_\mu\varphi
-\frac{\lambda}{4}(\varphi^\dagger\varphi-v^2)^2,
\qquad
\varphi_{\mathrm{vac}}=ve^{i\alpha}.
\tag{92.12}
$$

它的真空集合是一个圆$S^1$。用$\boldsymbol x=r(\cos\phi,\sin\phi)$表示空间，远处的场可以趋向$vU(\phi)$，其中$U:S^1\to S^1$且$U^\dagger U=1$。

沿区间$0\le\phi\le2\pi$可以连续选相位。具体地，选定$U(0)=e^{i\alpha_0}$，令
<span id="eq:c92-phase-lift"></span>

$$
\alpha(\phi)=\alpha_0-i\int_0^\phi
 U^\dagger(\vartheta)\,\partial_\vartheta U(\vartheta)\,d\vartheta.
\tag{92.13}
$$

由$\partial_\phi(U^\dagger U)=0$，被积式乘$-i$为实数；再直接求导可得$\partial_\phi(e^{-i\alpha}U)=0$，所以$U=e^{i\alpha}$。$U(2\pi)=U(0)$只要求相位差为整数倍的$2\pi$。这个整数便是缠绕数（winding number）：
<span id="eq:c92-circle-winding"></span>

$$
n=\frac{\alpha(2\pi)-\alpha(0)}{2\pi}
 =\frac{i}{2\pi}\int_0^{2\pi}
 U\partial_\phi U^\dagger\,d\phi\in\mathbb Z.
\tag{92.14}
$$

$U=e^{in\phi}$给$n$，因为$U\partial_\phi U^\dagger=-in$。正$n$和负$n$分别表示两种绕行方向。

还须说明，稍微改变映射不会改变这个整数。由单位模约束，
<span id="eq:c92-circle-variation"></span>

$$
\begin{aligned}
\delta U^\dagger&=-(U^\dagger)^2\delta U,\\
\delta(U\partial_\phi U^\dagger)
 &=\delta U\,\partial_\phi U^\dagger
   -U\partial_\phi[(U^\dagger)^2\delta U]\\
 &=-\partial_\phi(U^\dagger\delta U),\\
\delta n&=-\frac{i}{2\pi}
 [U^\dagger\delta U]_{0}^{2\pi}=0 .
\end{aligned}
\tag{92.15}
$$

最后用了$U,\delta U$在圆上单值。对整个光滑形变$U_s$，将$\delta U$换成$\partial_sU_s\,ds$便有$dn/ds=0$，这给出缠绕数的形变不变性。

反过来，任一度为$n$的映射都能连续变到$e^{in\phi}$。写$\alpha(\phi)=\alpha_0+n\phi+h(\phi)$，其中$h(0)=h(2\pi)=0$，然后取
<span id="eq:c92-circle-homotopy"></span>

$$
U_s(\phi)=\exp\{i[n\phi+(1-s)(\alpha_0+h(\phi))]\},
\qquad 0\le s\le1.
\tag{92.16}
$$

每个$s$都给单值的圆映射。这说明整数不仅在形变中不变，还把圆映射的形变类完全区分开来。两个映射相乘时相位相加，故缠绕数也相加；下面用两个半圆上的分段形变说明这一点。$n=-1$给出恒等映射在缠绕数加法下的逆，即相反取向的代表。

<span id="c92-winding-product"></span>

### 把两次绕行放到两个半圆

令$U=U_nU_k$。复数场彼此交换且单位模，乘积求导给
<span id="eq:x92-winding-product"></span>

$$
\begin{aligned}
U\partial_\phi U^\dagger
&=U_nU_k\partial_\phi(U_k^\dagger U_n^\dagger)\\
&=U_k\partial_\phi U_k^\dagger
 +U_n\partial_\phi U_n^\dagger,\\
\frac{i}{2\pi}\int_0^{2\pi}U\partial_\phi U^\dagger\,d\phi
&=k+n.
\end{aligned}
\tag{92.95}
$$

还可以用一个形变把这个加法画在圆上：让两次绕行分别发生在两个半圆上。

为使分段连接处也光滑，取一个实光滑函数$H(t)$，在$t\le0$时为0、$t\ge1$时为1，所有非零导数都集中在$0<t<1$。例如先令$w(t)=\exp[-1/(t(1-t))]$于$(0,1)$内成立、区间外为零，再定义$H(t)=\int_{-\infty}^t w(s)ds/\int_0^1w(s)ds$。把两个映射形变到
<span id="eq:x92-winding-separated"></span>

$$
\begin{aligned}
\widetilde U_n(\phi)
 &=\exp\!\left[2\pi i nH\!\left(\frac{\phi-\pi}{\pi}\right)\right],\\
\widetilde U_k(\phi)
 &=\exp\!\left[2\pi i kH\!\left(\frac{\phi}{\pi}\right)\right].
\end{aligned}
\tag{92.96}
$$

第一个映射在$0\le\phi\le\pi$等于1，第二个在$\pi\le\phi\le2\pi$等于1。它们的实相位分别增加$2\pi n$和$2\pi k$，因此缠绕数未变。若原映射的连续相位为$\alpha_n$，新映射的相位为$\widetilde\alpha_n$，则$e^{i[(1-s)\alpha_n+s\widetilde\alpha_n]}$给出所需形变：两个相位的端点差相同，所以每个$s$都在圆上单值；$k$同理。

乘积在第一半圆完成$k$次绕行，在第二半圆完成$n$次绕行，总数自然为$n+k$。两个映射的变化集中在相反的半圆，因而也直接实现了缠绕数的相加。

<span id="c92-global-vortex"></span>

## 为什么整体涡旋的能量发散

取非零整数$n$，尝试静态的径向拟设
<span id="eq:c92-global-ansatz"></span>

$$
\varphi(r,\phi)=vf(r)e^{in\phi},\qquad
f(\infty)=1,\quad f(0)=0 .
\tag{92.17}
$$

核心的零值使场离开真空圆，消除了相位在原点的多值问题。为使场光滑，实际上还要选$f(r)\sim r^{|n|}$的正则支；稍后场方程会给出这个幂次。

极坐标的梯度为$\hat{\boldsymbol r}\partial_r+\hat{\boldsymbol\phi}\partial_\phi/r$。两个单位矢量正交，故
<span id="eq:c92-global-divergence"></span>

$$
\begin{aligned}
\boldsymbol\nabla\varphi
 &=v\left[f_r\hat{\boldsymbol r}
      +\frac{in}{r}f\hat{\boldsymbol\phi}\right]e^{in\phi},\\
|\boldsymbol\nabla\varphi|^2
 &=v^2\left[f_r^2+\frac{n^2}{r^2}f^2\right],\\
E_{\mathrm{angular}}(r_0,R)
 &=2\pi n^2v^2\int_{r_0}^{R}\frac{f(r)^2}{r}\,dr
 \sim2\pi n^2v^2\log(R/r_0).
\end{aligned}
\tag{92.18}
$$

这里$r\,dr\,d\phi$的Jacobian与角导数中的$r^{-2}$共同留下$dr/r$。因为$f\to1$，例如足够远处$f^2>1/2$，最后积分必定发散；核心怎样调整都消不去这个远处的能量。

更一般的限制由Derrick缩放论证给出，它不局限于当前的对数发散。设有$D$个空间维、无约束实场$\varphi_i$、标准正动能和非负可微势，记
<span id="eq:c92-derrick-energy"></span>

$$
T=\frac12\int d^Dx\,(\boldsymbol\nabla\varphi_i)^2,\qquad
U=\int d^Dx\,V(\varphi),\qquad E=T+U.
\tag{92.19}
$$

假设构型平滑、$T,U$有限，且保留边界的缩放$\varphi_\alpha(\boldsymbol x)=\varphi(\boldsymbol x/\alpha)$是可容许的变分。令$\boldsymbol y=\boldsymbol x/\alpha$，测度给$\alpha^D$，每个梯度给$\alpha^{-1}$，于是
<span id="eq:c92-derrick-scaling"></span>

$$
E(\alpha)=\alpha^{D-2}T+\alpha^DU,\qquad
E'(1)=(D-2)T+DU=0.
\tag{92.20}
$$

第二式要求原构型是静态场方程的驻点。$D>2$时，两个非负项只能分别为零，场因而为常数。

$D=2$要多走一步：缩放式只给$U=0$。由于$V\ge0$，平滑解处处在势的极小值上，故$\partial V/\partial\varphi_i=0$，静态方程成为$\nabla^2\varphi_i=0$。每个导数$g=\partial_j\varphi_i$也是调和函数，并且$\int|g|^2<\infty$。调和函数在以$\boldsymbol x$为心的圆盘上的平均等于$g(\boldsymbol x)$：对圆周平均求半径导数，Gauss定理把它变成圆盘内$\nabla^2g$的积分，因而为零；再对半径积分就得到圆盘平均。因此Cauchy–Schwarz不等式给
<span id="eq:c92-derrick-two-dimensions"></span>

$$
|g(\boldsymbol x)|^2
 =\left|\frac1{\pi R^2}\int_{B_R(\boldsymbol x)}g(\boldsymbol y)\,d^2y\right|^2
 \le\frac1{\pi R^2}\int_{B_R(\boldsymbol x)}|g|^2\,d^2y
 \longrightarrow0 .
\tag{92.21}
$$

所以梯度仍为零。这也给出了二维的结论。定理使用的是正势、无约束标量和二导数静态能量；若改变这些条件，缩放分析也要相应改变。在当前模型中，引入规范场将提供改变缩放关系的新项。

<span id="c92-local-vortex"></span>

## 规范场怎样消去远处的角向梯度

把式[（92.12）](#eq:c92-complex-model)的整体$U(1)$对称性规范化，得到
<span id="eq:c92-abelian-model"></span>

$$
\begin{aligned}
\mathcal L&=-(D_\mu\varphi)^\dagger D^\mu\varphi
-\frac{\lambda}{4}(|\varphi|^2-v^2)^2-\frac14F_{\mu\nu}F^{\mu\nu},\\
D_\mu&=\partial_\mu-ieA_\mu,\qquad
F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu .
\end{aligned}
\tag{92.22}
$$

真空模仍是$v$。为确定场的质量，取$\varphi=v+(h+i\chi)/\sqrt2$；两个实场都具有标准的$1/2$动能归一。二次项为
<span id="eq:c92-abelian-masses"></span>

$$
\begin{aligned}
\mathcal L_2
 &=-\frac12(\partial h)^2
  -\frac12(\partial_\mu\chi-\sqrt2evA_\mu)^2
  -\frac12\lambda v^2h^2-\frac14F_{\mu\nu}F^{\mu\nu},\\
m_S^2&=\lambda v^2,\qquad m_V^2=2e^2v^2 .
\end{aligned}
\tag{92.23}
$$

在局部幺正规范$\chi=0$下，矢量二次项是$-e^2v^2A^2=-m_V^2A^2/2$，所以$m_V=\sqrt2ev$。这里的$v$与[第85节](/posts/srednicki-85/#c85-proca)的$v$不同：若比较同一复场模型，应取$v_{85}=\sqrt2v_{92}$，便恢复该章的质量公式。

令$U=e^{i\alpha(x)}$，有限规范变换满足
<span id="eq:c92-abelian-gauge-transform"></span>

$$
\begin{aligned}
\varphi&\longmapsto U\varphi,\\
A_\mu&\longmapsto UA_\mu U^\dagger+\frac{i}{e}U\partial_\mu U^\dagger
 =A_\mu+\frac1e\partial_\mu\alpha,\\
D_\mu\varphi&\longmapsto U D_\mu\varphi .
\end{aligned}
\tag{92.24}
$$

最后一式可直接展开：$\partial_\mu U$产生的$i(\partial_\mu\alpha)U\varphi$，恰被连接的新增项抵消。对常值真空$\varphi=v,A_\mu=0$，在大圆上取$\alpha=n\phi$，便得到
<span id="eq:c92-vortex-asymptotic-gauge"></span>

$$
\varphi\longrightarrow ve^{in\phi},\qquad
\boldsymbol A\longrightarrow\frac{n}{er}\hat{\boldsymbol\phi},
\qquad
(\boldsymbol\nabla-ie\boldsymbol A)ve^{in\phi}=0 .
\tag{92.25}
$$

这说明连接能够恰好抵消式[（92.18）](#eq:c92-global-divergence)中造成发散的角梯度，其中相位与连接必须带同一个整数$n$。

非零缠绕数的$U(\phi)$不能光滑延拓为整个圆盘上的单位模函数。否则把边界圆沿半径缩到圆心，就给出了它到常映射的连续形变，与式[（92.15）](#eq:c92-circle-variation)矛盾。这样的边界函数称为大规范变换（large gauge transformation），它不能充当全平面上光滑的小规范冗余。核心处场必须离开真空圆，规范势也必须偏离渐近的纯规范形式。于是取
<span id="eq:c92-local-ansatz"></span>

$$
\begin{aligned}
\varphi&=vf(r)e^{in\phi},&
A_r&=0,&
A_\phi&=\frac{n}{er}a(r),\\
f(\infty)&=a(\infty)=1,&
f(0)&=a(0)=0,\qquad n\ne0 .
\end{aligned}
\tag{92.26}
$$

$A_\phi$是沿单位矢量$\hat{\boldsymbol\phi}$的分量，而不是坐标一形式中$d\phi$的系数。后者为$rA_\phi=na/e$。协变梯度和磁场分别为
<span id="eq:c92-vortex-flux"></span>

$$
\begin{aligned}
D_r\varphi&=vf_r e^{in\phi},&
D_{\hat\phi}\varphi&=\frac{in}{r}(1-a)vf e^{in\phi},\\
B=F_{12}
 &=\frac1r\bigl[\partial_r(rA_\phi)-\partial_\phi A_r\bigr]
 =\frac{n}{er}a_r,\\
\Phi&=\int d^2x\,B
 =\frac{2\pi n}{e}\int_0^\infty a_r\,dr
 =\frac{2\pi n}{e}.
\end{aligned}
\tag{92.27}
$$

旋度与面积积分中的$r$相消；同一结果也由Stokes定理$\Phi=\lim_{r\to\infty}2\pi rA_\phi$得到。磁通只由边界缠绕数决定，核心的具体形状不影响它。$n=1$的构型称Nielsen–Olesen涡旋（vortex），负$n$则反转磁通方向。

<span id="c92-vortex-equations"></span>

## 径向能量、场方程和两端边界

取静态纯磁构型。由于$F_{ij}F_{ij}=2B^2$，规范动能给$B^2/2$。把式[（92.26）](#eq:c92-local-ansatz)代入静态能量，
<span id="eq:c92-vortex-radial-energy"></span>

$$
\begin{aligned}
E&=\int d^2x\left[
 |D_i\varphi|^2+\frac{\lambda}{4}(|\varphi|^2-v^2)^2+\frac12B^2\right]\\
 &=2\pi v^2\int_0^\infty r\,dr\left[
 f_r^2+\frac{n^2}{r^2}(1-a)^2f^2
 +\frac{\lambda v^2}{4}(f^2-1)^2
 +\frac{n^2}{2e^2v^2r^2}a_r^2\right].
\end{aligned}
\tag{92.28}
$$

磁能的$1/2$随代入保留，它将同时进入无量纲能量与规范场方程。

为便于求径向轮廓，定义无量纲变量
<span id="eq:c92-vortex-source-variables"></span>

$$
\rho=evr,\qquad \beta^2=\frac{\lambda}{e^2},
\qquad
m_Vr=\sqrt2\rho,\qquad
\frac{m_S^2}{m_V^2}=\frac{\beta^2}{2}.
\tag{92.29}
$$

此处$\beta$是耦合比，与推动速度无关。由于$r\,dr=\rho\,d\rho/(e^2v^2)$，而$f_r=evf'$、$a_r=eva'$，能量变成
<span id="eq:c92-vortex-dimensionless-energy"></span>

$$
E=2\pi v^2\int_0^\infty d\rho\,\rho
\left[
 f'^2+\frac{n^2}{\rho^2}(1-a)^2f^2
 +\frac{\beta^2}{4}(1-f^2)^2
 +\frac{n^2}{2\rho^2}a'^2
\right].
\tag{92.30}
$$

以下撇号对$\rho$求导。记被积式连同外面的$\rho$为$\ell$。变分中要用的四个导数为
<span id="eq:c92-vortex-variation"></span>

$$
\begin{aligned}
\frac{\partial\ell}{\partial f'}&=2\rho f',&
\frac{\partial\ell}{\partial f}
 &=\frac{2n^2}{\rho}(1-a)^2f-\beta^2\rho(1-f^2)f,\\
\frac{\partial\ell}{\partial a'}&=\frac{n^2}{\rho}a',&
\frac{\partial\ell}{\partial a}
 &=-\frac{2n^2}{\rho}(1-a)f^2 .
\end{aligned}
\tag{92.31}
$$

固定两端的场值，分部积分的边界项为零；由$(\partial\ell/\partial q')'-\partial\ell/\partial q=0$，第一式除以$2\rho$，第二式乘$\rho/n^2$，得到
<span id="eq:c92-vortex-odes"></span>

$$
\begin{aligned}
f''+\frac{f'}{\rho}
-\frac{n^2}{\rho^2}(1-a)^2f+\frac{\beta^2}{2}(1-f^2)f&=0,\\
a''-\frac{a'}{\rho}+2(1-a)f^2&=0 .
\end{aligned}
\tag{92.32}
$$

规范方程的末项有系数2。也可从未作径向化的规范场方程核对它：
<span id="eq:c92-vortex-current-check"></span>

$$
\begin{aligned}
\partial_jF_{ji}
 &=ie\bigl[\varphi^\dagger D_i\varphi
 -(D_i\varphi)^\dagger\varphi\bigr],\\
\frac{n}{e}\left(\frac{a_{rr}}r-\frac{a_r}{r^2}\right)
 &=-\frac{2en v^2}{r}(1-a)f^2 .
\end{aligned}
\tag{92.33}
$$

第二行取沿$\hat{\boldsymbol\phi}$的分量。左右分别是磁场的径向变化和标量电流；它独立恢复了式[（92.32）](#eq:c92-vortex-odes)的系数2。

若愿意把半径直接用物理矢量质量来量度，令$R=\sqrt2\rho$、$b=\beta/\sqrt2=m_S/m_V$。这时磁项成为$n^2a_R^2/R^2$，两个方程成为
<span id="eq:c92-vortex-physical-variables"></span>

$$
\begin{aligned}
f_{RR}+\frac{f_R}{R}
-\frac{n^2}{R^2}(1-a)^2f+\frac{b^2}{2}(1-f^2)f&=0,\\
a_{RR}-\frac{a_R}{R}+(1-a)f^2&=0 .
\end{aligned}
\tag{92.34}
$$

在这套变量中，矢量尾部的质量尺度成为一；半径与耦合比同时改变，方程描述的仍是同一个拉格朗日量。

现在看边界。令$k=|n|\ge1$。在$\rho\to0$处，标量方程最奇异的部分给
<span id="eq:c92-vortex-core-index"></span>

$$
f''+\frac{f'}{\rho}-\frac{n^2}{\rho^2}f=0,
\qquad f\propto\rho^\eta,\quad \eta^2=n^2 .
\tag{92.35}
$$

$\rho^{-k}$的支发散，故取$f=c_f\rho^k[1+O(\rho^2)]$。规范方程齐次部分的解为常数和$\rho^2$；原点的正则条件排除常数项，再代入标量首项便有
<span id="eq:c92-vortex-core-series"></span>

$$
f=c_f\rho^k[1+O(\rho^2)],\qquad
a=c_a\rho^2-\frac{c_f^2}{2k(k+1)}\rho^{2k+2}
+o(\rho^{2k+2}).
\tag{92.36}
$$

因为$(\partial_\rho^2-\rho^{-1}\partial_\rho)\rho^{2k+2}
=4k(k+1)\rho^{2k}$，第二项的系数直接抵消$2c_f^2\rho^{2k}$。这些幂次保证笛卡儿场光滑：$r^ke^{in\phi}=(x+i\,\operatorname{sign}(n)y)^k$，而$a=O(r^2)$使$\boldsymbol A$在原点为$O(r)$。因此$f\sim\rho^n$只适用于正$n$；两个零点值本身还不足以选出正则支。

在远处，写$q=1-a$、$h=1-f$。保留规范方程的线性项以及驱动标量尾部的第一个平方项，
<span id="eq:c92-vortex-tail-equations"></span>

$$
\begin{aligned}
q''-\frac{q'}{\rho}-2q&=-4hq+2h^2q,\\
h''+\frac{h'}{\rho}-\beta^2h
 &=-\frac{n^2q^2}{\rho^2}
   +O(h^2,hq^2/\rho^2).
\end{aligned}
\tag{92.37}
$$

齐次衰减支分别为$\rho K_1(\sqrt2\rho)$和$K_0(\beta\rho)$，其中$K_\nu$是衰减的改良Bessel函数。这里所需的领头形式也可直接推出：把$\rho^p e^{-\mu\rho}$代入，常数阶确定$\mu$，$1/\rho$阶确定$p$。规范方程给$\mu=\sqrt2,p=1/2$，标量齐次方程给$\mu=\beta,p=-1/2$，故
<span id="eq:c92-vortex-homogeneous-tail"></span>

$$
q\sim C\rho^{1/2}e^{-\sqrt2\rho},
\qquad
h_{\mathrm{hom}}\sim H\rho^{-1/2}e^{-\beta\rho}.
\tag{92.38}
$$

匹配到核心后才能确定$C,H$。规范尾的平方还产生
$-n^2C^2e^{-2\sqrt2\rho}/\rho$，当它比标量齐次尾衰减慢时，必须保留。记$\mu=2\sqrt2$，把$A\rho^{-1}e^{-\mu\rho}$代入标量左边，其领头项为$(8-\beta^2)A\rho^{-1}e^{-\mu\rho}$；在$\beta=\mu$处改用$Ae^{-\mu\rho}$，左边为$-\mu Ae^{-\mu\rho}/\rho$。因而通常非零涡旋的领头尾部为
<span id="eq:c92-vortex-forced-tail"></span>

$$
h\sim
\begin{cases}
H\rho^{-1/2}e^{-\beta\rho},&0<\beta<2\sqrt2,\\[2pt]
\dfrac{n^2C^2}{2\sqrt2}e^{-2\sqrt2\rho},
 &\beta=2\sqrt2,\\[6pt]
\dfrac{n^2C^2}{\beta^2-8}\,
 \rho^{-1}e^{-2\sqrt2\rho},&\beta>2\sqrt2 .
\end{cases}
\tag{92.39}
$$

所以在$\rho,\beta$变量中，标量的主指数率是$\min(\beta,2\sqrt2)$。改用物理变量$R,b$后，这个率为$\min(b,2)$。完整尾部不只有齐次解的指数，还包含上面的幂次、平方驱动和共振情形。有限尺度的核心与指数衰减的尾部也解释了能量为什么收敛；当$n,\beta$为一阶数时，无量纲积分给一阶系数，故$E$为$2\pi v^2$的量级。

<span id="c92-vortex-bound"></span>

## 涡旋的Bogomolny界

一维孤子的质量由完成平方求出；涡旋也有类似的能量恒等式，只是协变导数的交换会多给一个磁场。令$j_i=\operatorname{Im}(\varphi^\dagger D_i\varphi)$，并用$[D_1,D_2]=-ieB$，则
<span id="eq:c92-vortex-current-identity"></span>

$$
\begin{aligned}
\partial_1(\varphi^\dagger D_2\varphi)
-\partial_2(\varphi^\dagger D_1\varphi)
 &=(D_1\varphi)^\dagger D_2\varphi
 -(D_2\varphi)^\dagger D_1\varphi-ieB|\varphi|^2,\\
\partial_1j_2-\partial_2j_1
 &=2\operatorname{Im}\bigl[(D_1\varphi)^\dagger D_2\varphi\bigr]
   -eB|\varphi|^2 .
\end{aligned}
\tag{92.40}
$$

第一行把普通导数补成协变导数后，两个连接交叉项相消；第二行取虚部。若$s=\pm1$，展开$|(D_1+isD_2)\varphi|^2$中的交叉项，又得到
<span id="eq:c92-vortex-derivative-square"></span>

$$
|D_i\varphi|^2
=|(D_1+isD_2)\varphi|^2
+s(\partial_1j_2-\partial_2j_1)+seB|\varphi|^2.
\tag{92.41}
$$

这里$i(z-z^*)=-2\operatorname{Im}z$固定了平方中的手性。磁能与势能则可写成
<span id="eq:c92-vortex-magnetic-square"></span>

$$
\begin{aligned}
\frac12B^2+\frac{\lambda}{4}(v^2-|\varphi|^2)^2
={}&\frac12[B-se(v^2-|\varphi|^2)]^2\\
&+seB(v^2-|\varphi|^2)
+\frac{\lambda-2e^2}{4}(v^2-|\varphi|^2)^2 .
\end{aligned}
\tag{92.42}
$$

相加后，含$B|\varphi|^2$的两项恰好抵消。对径向构型，边界流积分为
$\oint j_i\,dx_i=2\pi n v^2f^2(1-a)$，在大圆和收缩到核心的小圆上都趋零。因此取$s=\operatorname{sign}n$，有
<span id="eq:c92-vortex-bogomolny"></span>

$$
\begin{aligned}
E={}&2\pi v^2|n|\\
&+\int d^2x\left[
 |(D_1+isD_2)\varphi|^2
 +\frac12[B-se(v^2-|\varphi|^2)]^2
 +\frac{\lambda-2e^2}{4}(v^2-|\varphi|^2)^2
\right].
\end{aligned}
\tag{92.43}
$$

边界常数来自$se v^2\Phi$。对一般不具旋转对称性的构型，同一恒等式也成立，只需相应的边界流积分消失。

在$\lambda\ge2e^2$时，被积项均非负，故$E\ge2\pi v^2|n|$；若$\lambda>2e^2$且$n\ne0$，核心附近$|\varphi|\ne v$的区域使不等式严格。临界耦合是
<span id="eq:c92-vortex-critical-coupling"></span>

$$
\lambda=2e^2,\qquad \beta^2=2,\qquad m_S=m_V .
\tag{92.44}
$$

若用物理质量比$b=m_S/m_V$，高于临界值对应$b>1$；在$\beta$变量中则是$\beta>\sqrt2$。后面的[试探场计算](#c92-vortex-trial)会给出$\beta^2=3/2$、能量低于$2\pi v^2$的光滑例子。

临界时，使两个平方为零便得到一阶方程。用
$D_1+isD_2=e^{is\phi}(D_r+isD_{\hat\phi})$和$sn=k=|n|$，
<span id="eq:c92-vortex-first-order"></span>

$$
f'=\frac{k}{\rho}(1-a)f,\qquad
a'=\frac{\rho}{k}(1-f^2).
\tag{92.45}
$$

对第一式求导并代入第二式，或反过来求导，有
<span id="eq:c92-vortex-bps-check"></span>

$$
\begin{aligned}
f''+\frac{f'}{\rho}
-\frac{k^2}{\rho^2}(1-a)^2f
 &=-\frac{k}{\rho}a'f=-(1-f^2)f,\\
a''-\frac{a'}{\rho}
 &=-\frac{2\rho}{k}ff'=-2(1-a)f^2 .
\end{aligned}
\tag{92.46}
$$

这正好是式[（92.32）](#eq:c92-vortex-odes)在$\beta^2=2$时的二阶系统。还可直接在径向能量中检查边界常数：
<span id="eq:c92-vortex-radial-square"></span>

$$
\begin{aligned}
\frac{E}{2\pi v^2}
={}&\int_0^\infty d\rho\,\rho
\left[
 \left(f'-\frac{k}{\rho}(1-a)f\right)^2
 +\frac{k^2}{2\rho^2}
 \left(a'-\frac{\rho}{k}(1-f^2)\right)^2
\right]\\
&+k\,[a+(1-a)f^2]_{0}^{\infty}\\
={}&\int_0^\infty d\rho\,\rho
 \left[\text{上列两平方}\right]+k .
\end{aligned}
\tag{92.47}
$$

交叉项合成的导数为$a'(1-f^2)+2(1-a)ff'$。这条独立配方再次固定了磁能的$1/2$、磁通的$2\pi$和绕数绝对值。

<span id="c92-vortex-trial"></span>

### 一个可以完全积分的涡旋试探场

在临界值$\beta^2=2$以下，涡旋能量可以小于$2\pi v^2|n|$。下面构造一个光滑且磁通固定的例子。取$n=1$及
<span id="eq:x92-vortex-trial"></span>

$$
f(\rho)=\sqrt{1-e^{-c\rho^2}},\qquad
a(\rho)=1-e^{-c\rho^2},\qquad c>0.
\tag{92.97}
$$

在原点，$f=\sqrt c\,\rho+O(\rho^3)$、$a=c\rho^2+O(\rho^4)$。因而$fe^{i\phi}$是$x+iy$乘一个光滑径向函数，$a\hat{\boldsymbol\phi}/r$也光滑；在无穷远二者趋1，磁通保持$2\pi/e$。

把这个场放进式[（92.30）](#eq:c92-vortex-dimensionless-energy)。令$x=c\rho^2$，径向动能给
<span id="eq:x92-trial-radial"></span>

$$
\begin{aligned}
I_r&=\int_0^\infty\rho f'^2\,d\rho
 =\frac12\int_0^\infty\frac{x e^{-2x}}{1-e^{-x}}\,dx\\
 &=\frac12\sum_{j=2}^{\infty}\int_0^\infty xe^{-jx}\,dx
 =\frac12\sum_{j=2}^{\infty}\frac1{j^2}
 =\frac12\left(\frac{\pi^2}{6}-1\right).
\end{aligned}
\tag{92.98}
$$

级数各项非负，故可交换求和与积分；分部积分给$\int_0^\infty xe^{-jx}dx=j^{-2}$。最后所用的平方倒数和也可由$f(t)=t$在$(-\pi,\pi)$的Fourier正弦系数$b_j=2(-1)^{j+1}/j$求出：Parseval关系$\pi^{-1}\int_{-\pi}^{\pi}t^2dt=\sum b_j^2$给$2\pi^2/3=4\sum j^{-2}$。

角向动能中的$1/\rho$变成$dx/(2x)$，所以
<span id="eq:x92-trial-angular"></span>

$$
\begin{aligned}
I_\phi&=\int_0^\infty\frac{(1-a)^2f^2}{\rho}\,d\rho
 =\frac12\int_0^\infty\frac{e^{-2x}-e^{-3x}}x\,dx\\
 &=\frac12\int_2^3dt\int_0^\infty e^{-tx}\,dx
 =\frac12\log\frac32.
\end{aligned}
\tag{92.99}
$$

中间用$(e^{-2x}-e^{-3x})/x=\int_2^3e^{-tx}dt$，再次只交换非负积分。剩下两项为
<span id="eq:x92-trial-energy"></span>

$$
\begin{aligned}
I_B&=\int_0^\infty\frac{a'^2}{2\rho}\,d\rho
 =2c^2\int_0^\infty\rho e^{-2c\rho^2}d\rho=\frac c2,\\
I_V&=\frac{\beta^2}{4}\int_0^\infty\rho e^{-2c\rho^2}d\rho
 =\frac{\beta^2}{16c},\\
\frac{E_{\rm trial}}{2\pi v^2}
 &=\frac12\left(\frac{\pi^2}{6}-1+\log\frac32\right)
 +\frac c2+\frac{\beta^2}{16c}.
\end{aligned}
\tag{92.100}
$$

最后两项对$c$驻定时$c=\beta/(2\sqrt2)$，二阶导数为正。这是在所选试探族中优化核心尺度。

现在取$\beta^2=3/2$、$c=\sqrt3/4$，所得能量为
<span id="eq:x92-trial-counterexample"></span>

$$
\frac{E_{\rm trial}}{2\pi v^2}
 =\frac12\left(\frac{\pi^2}{6}-1+\log\frac32\right)
 +\frac{\sqrt3}{4}
 <\frac{13}{24}+\frac7{16}=\frac{47}{48}<1.
\tag{92.101}
$$

这里用了$\pi^2<10$、交错对数级数给出的$\log(3/2)<1/2-1/8+1/24=5/12$，以及$\sqrt3<7/4$。这个构型处在绕数1扇区，满足核心正则性和无穷远条件，却有$E<2\pi v^2$。因而能量界的临界参数由$\beta^2=2$固定。

径向有限能量解的存在性可用 [Gustafson–Sigal 论文的定理2](https://arxiv.org/pdf/math/9904158v1#page=7)，该处引用了 Plohr 及 Berger–Chen 的证明。先将能量归一转换到该文的形式，令
<span id="eq:c92-vortex-external-conversion"></span>

$$
\begin{aligned}
\boldsymbol y&=\sqrt2ev\boldsymbol x,\qquad
\psi=\varphi/v,\qquad \boldsymbol{\mathcal A}=\boldsymbol A/(\sqrt2v),\\
E&=2v^2E_{\mathrm{GS}},\\
E_{\mathrm{GS}}
 &=\frac12\int d^2y\left[
 |(\nabla-i\boldsymbol{\mathcal A})\psi|^2
 +(\operatorname{curl}\boldsymbol{\mathcal A})^2
 +\frac{\lambda_{\mathrm{GS}}}{4}(|\psi|^2-1)^2\right],\\
\lambda_{\mathrm{GS}}&=\lambda/(2e^2)=b^2 .
\end{aligned}
\tag{92.48}
$$

其中$D_x\varphi=\sqrt2ev^2D_y\psi$、$B_x=2ev^2\operatorname{curl}_y\mathcal A$、$d^2x=d^2y/(2e^2v^2)$，三项分别给出这个转换。对每个非零整数$n$和$b>0$，所引定理构造了正则、有限能量的径向极小解；正半径处$0<f,a<1$并单调趋1。负$n$由复共轭和磁场反号得到。

研究高绕数涡旋的不稳定性，需要容许破坏旋转对称性的扰动。[Gustafson–Sigal 的定理1](https://arxiv.org/pdf/math/9904158v1#page=5)证明：$|n|\ge2,b>1$的上述径向涡旋具有负的能量Hessian模，而$n=\pm1$对所有$b>0$在线性意义下稳定。这里排除了规范和平移对称性给出的零模，负模属于有限能量扰动的二次型定义域。若以$u_n$表示整个静态场组、$\eta$表示该负方向，便有
<span id="eq:c92-vortex-negative-direction"></span>

$$
E(u_n+s\eta)=E(u_n)
 +\frac{s^2}{2}\langle\eta,L_n\eta\rangle+o(s^2),
\qquad \langle\eta,L_n\eta\rangle<0 .
\tag{92.49}
$$

场方程使一阶项消失，足够小的非零$s$于是降低能量。这给出了重合高绕数涡核的不稳定依据。这描述了重合涡核附近的线性不稳定性；后续运动由相应的时间演化方程决定。

在二空间维，平移与推动把涡旋变成运动的粒子状构型；在三空间维，沿第三方向延伸则形成Nielsen–Olesen弦，也称规范弦（gauge string）。此时上面的$E$应解释为单位长度能量，临界张力为$2\pi v^2|n|$。曲率半径远大于核心宽度时，可把弯曲弦的局部截面近似看成直涡旋；闭合弦环的进一步运动还受其张力支配。宇宙弦（cosmic string）是这种构型在早期宇宙模型中的应用，后面的统一理论提供可能的场内容。

<span id="c92-sphere"></span>

## 二球面映射及其度数

再增加一个空间维，远处的边界成为二球面$S^2$。相应取三个实标量，
<span id="eq:c92-triplet-model"></span>

$$
\begin{aligned}
\mathcal L&=-\frac12\partial^\mu\varphi^a\partial_\mu\varphi^a
-\frac{\lambda}{8}(\varphi^a\varphi^a-v^2)^2,\qquad a=1,2,3,\\
\varphi_{\mathrm{vac}}^a&=v\widehat\varphi^a,\qquad
\widehat\varphi^a\widehat\varphi^a=1 .
\end{aligned}
\tag{92.50}
$$

因此真空取值也是一个二球面。空间球用$(\theta,\phi)$参数化，边界场$\widehat{\boldsymbol\varphi}(\theta,\phi)$便给从空间球到真空球的映射。

为刻画这个映射，定义映射度（degree），也称缠绕数：
<span id="eq:c92-sphere-degree"></span>

$$
\begin{aligned}
n&=\frac1{8\pi}\int d\theta\,d\phi\,
 \epsilon^{abc}\epsilon^{ij}
 \widehat\varphi^a\partial_i\widehat\varphi^b
                      \partial_j\widehat\varphi^c\\
 &=\frac1{4\pi}\int_0^\pi d\theta\int_0^{2\pi}d\phi\,
 \widehat{\boldsymbol\varphi}\cdot
 \bigl(\partial_\theta\widehat{\boldsymbol\varphi}
             \times\partial_\phi\widehat{\boldsymbol\varphi}\bigr).
\end{aligned}
\tag{92.51}
$$

在第一行中$i,j$只取两个角坐标，$\epsilon^{\theta\phi}=+1$。两种非零排列相等，故$1/(8\pi)$变成$1/(4\pi)$。叉积本身已包含面积Jacobian；外面的测度不再另乘$\sin\theta$。

例如取题92.5的映射
<span id="eq:c92-sphere-example"></span>

$$
\widehat{\boldsymbol\varphi}
=(\sin\theta\cos N\phi,\ \sin\theta\sin N\phi,\ \cos\theta),
\qquad N\in\mathbb Z .
\tag{92.52}
$$

它的两个角导数为$(\cos\theta\cos N\phi,\cos\theta\sin N\phi,-\sin\theta)$和$N(-\sin\theta\sin N\phi,\sin\theta\cos N\phi,0)$。逐项取叉积，得到$N\sin\theta\,\widehat{\boldsymbol\varphi}$，所以
<span id="eq:c92-sphere-example-integral"></span>

$$
n=\frac{N}{4\pi}\int_0^{2\pi}d\phi\int_0^\pi\sin\theta\,d\theta=N .
\tag{92.53}
$$

恒等映射对应$N=1$，相反取向给$N=-1$。一般$N$的这个坐标代表在极点只是连续的：北极附近，前两个分量组成$\theta e^{iN\phi}$，通常不是局部笛卡儿坐标的可微函数。上述积分可在去掉两个小极帽后求极限；若需要处处光滑的代表，用立体坐标$z=\tan(\theta/2)e^{i\phi}$，对$N>0$取$w=z^N$，对$N<0$取$w=\bar z^{|N|}$，对$N=0$取常映射。在另一极点改用$1/z,1/w$便看出这些代表也光滑。

度数在光滑形变下不变。暂记$\boldsymbol n=\widehat{\boldsymbol\varphi}$。微分$\boldsymbol n^2=1$给
<span id="eq:c92-sphere-tangent-vectors"></span>

$$
\boldsymbol n\cdot\delta\boldsymbol n=0,\qquad
\boldsymbol n\cdot\partial_i\boldsymbol n=0,\qquad
\delta\boldsymbol n\cdot
 (\partial_i\boldsymbol n\times\partial_j\boldsymbol n)=0 .
\tag{92.54}
$$

最后一个式子因为三个向量都在二维切平面内。对度密度变分，落在首个$\boldsymbol n$上的项因而消失，落在两个导数上的项交换$i,j$后相等，于是
<span id="eq:c92-sphere-degree-variation"></span>

$$
\begin{aligned}
\delta\!\left[
 \epsilon^{ij}\boldsymbol n\cdot
 (\partial_i\boldsymbol n\times\partial_j\boldsymbol n)\right]
 &=2\epsilon^{ij}\boldsymbol n\cdot
     (\partial_i\delta\boldsymbol n\times\partial_j\boldsymbol n)\\
 &=2\partial_i\!\left[
 \epsilon^{ij}\boldsymbol n\cdot
 (\delta\boldsymbol n\times\partial_j\boldsymbol n)\right].
\end{aligned}
\tag{92.55}
$$

第二行展开后，多出的三切向量项为零，而二阶导数与反对称$\epsilon^{ij}$缩并也为零。在闭球面上积分这个全导数，各坐标片的公共边界互相抵消，故$\delta n=0$。这一写法也说明了坐标不变性：相容取向的换图中，两个导数的Jacobian与有向测度相消；若真的反转定义域球或靶球的取向，度数则变号。

把这些不变量用于任意边界映射，还要导入一个拓扑分类结果。对$k\ge1$，连续有基点映射$S^k\to S^k$的同伦类组成$\pi_k(S^k)$，度映射把它与$\mathbb Z$一一对应，恒等映射对应1；对靶球$S^2,S^3$，放开基点也不改变分类。这里“同伦”就是一个连续族$H(x,s)$，始终把每个$x$映入同一个靶球；有基点同伦还要求选定的一点在整个形变中固定。度数的分类见 Hatcher 的[推论4.25](https://pi.math.cornell.edu/~hatcher/AT/AT.pdf#page=370)，有基点与自由同伦的关系见[命题4A.2](https://pi.math.cornell.edu/~hatcher/AT/AT.pdf#page=431)。

本节的面积积分正是这个度：它在形变下不变，把两个映射分别放在两个不交小球域并在其余地方取常值时，积分直接相加；恒等映射的积分又为1，故在上述整数分类上它只能给相同的整数。这里用到的连续与光滑同伦可以衔接：把紧致域上的连续同伦在局部坐标中以光滑分片单位一致逼近，误差取小于$1/4$，所得$\mathbb R^{k+1}$值函数便不经过零；再除以其模长，就得到球面内的光滑同伦。端点附近先取恒定的时间领圈，逼近时保持端点不变即可。这样，分类定理与刚才用微分计算的形变不变性适用于同一批边界类。

非零度数使边界方向不能收缩成常方向。不过，前面的缩放分析仍阻止当前纯标量模型产生平滑有限能量静态解。我们还要像涡旋一样引入规范场。

<span id="c92-monopole-model"></span>

## 实三重态的破缺与电磁场

令三个实场处在$SU(2)$的伴随表示中，拉格朗日量为
<span id="eq:c92-georgi-glashow"></span>

$$
\begin{aligned}
\mathcal L&=-\frac12(D^\mu\varphi)^a(D_\mu\varphi)^a
 -\frac{\lambda}{8}(\varphi^a\varphi^a-v^2)^2
 -\frac14F^{a\mu\nu}F_{\mu\nu}^a,\\
(D_\mu\varphi)^a&=\partial_\mu\varphi^a
 +e\epsilon^{abc}A_\mu^b\varphi^c,\\
F_{\mu\nu}^a&=\partial_\mu A_\nu^a-\partial_\nu A_\mu^a
 +e\epsilon^{abc}A_\mu^bA_\nu^c .
\end{aligned}
\tag{92.56}
$$

取真空$\varphi^a=v\delta^{a3}$。协变梯度的前两个分量为$evA_\mu^2,-evA_\mu^1$，第三分量为零，因而
<span id="eq:c92-triplet-spectrum"></span>

$$
\begin{aligned}
\mathcal L_{\mathrm{mass}}
 &=-\frac12e^2v^2\bigl[(A_\mu^1)^2+(A_\mu^2)^2\bigr],\\
W_\mu^\pm&=\frac{A_\mu^1\mp iA_\mu^2}{\sqrt2},
\qquad m_W=ev,\qquad Q(W^\pm)=\pm e .
\end{aligned}
\tag{92.57}
$$

实场动能带$1/2$，所以这里的$ev$就是正确质量。未破缺的$T^3$使$A_\mu^3$保持无质量。把两个实分量组成$W^+$后，关于$A_\mu^3$的导数为$\partial_\mu-ieA_\mu^3$；$W^-$为其共轭，故电荷相反。我们把这个剩余$U(1)$解释为电磁群。模型称Georgi–Glashow模型；它没有标准电弱理论中的有质量中性$Z$，因此其粒子谱不能取代第87节的模型。

当Higgs方向随位置改变时，不能总把第三个内部方向称为电磁方向。令$\boldsymbol n=\boldsymbol\varphi/|\boldsymbol\varphi|$，在$|\varphi|>0$处定义
<span id="eq:c92-em-tensor"></span>

$$
\mathcal F_{\mu\nu}
 =\boldsymbol n\cdot\boldsymbol F_{\mu\nu}
 -\frac1e\boldsymbol n\cdot
       (D_\mu\boldsymbol n\times D_\nu\boldsymbol n).
\tag{92.58}
$$

这里内部矢量的点积、叉积都在伴随的三维空间中；用$\mathcal F$区分这个电磁复合场与原来的$F^a$。伴随规范变换是内部旋转，式中所有内部指标都缩并，所以它规范不变。第二项的作用在展开后最清楚。由$D_\mu\boldsymbol n=\partial_\mu\boldsymbol n+e\boldsymbol A_\mu\times\boldsymbol n$及$\boldsymbol n\cdot\partial_\mu\boldsymbol n=0$，
<span id="eq:c92-em-cross-products"></span>

$$
\begin{aligned}
\boldsymbol n\cdot
 [\partial_\mu\boldsymbol n\times(\boldsymbol A_\nu\times\boldsymbol n)]
 &=-\boldsymbol A_\nu\cdot\partial_\mu\boldsymbol n,\\
\boldsymbol n\cdot
 [(\boldsymbol A_\mu\times\boldsymbol n)\times\partial_\nu\boldsymbol n]
 &=\boldsymbol A_\mu\cdot\partial_\nu\boldsymbol n,\\
\boldsymbol n\cdot
 [(\boldsymbol A_\mu\times\boldsymbol n)\times
  (\boldsymbol A_\nu\times\boldsymbol n)]
 &=\boldsymbol n\cdot(\boldsymbol A_\mu\times\boldsymbol A_\nu).
\end{aligned}
\tag{92.59}
$$

前两行由三重积公式$\boldsymbol a\times(\boldsymbol b\times\boldsymbol c)
=\boldsymbol b(\boldsymbol a\cdot\boldsymbol c)-\boldsymbol c(\boldsymbol a\cdot\boldsymbol b)$得到；最后一行可在$\boldsymbol n=(0,0,1)$的正交基中把两个切向分量相乘，因两边都是旋转标量，结果对任意方向成立。因此
<span id="eq:c92-em-expansion"></span>

$$
\begin{aligned}
\boldsymbol n\cdot(D_\mu\boldsymbol n\times D_\nu\boldsymbol n)
={}&\boldsymbol n\cdot
 (\partial_\mu\boldsymbol n\times\partial_\nu\boldsymbol n)\\
&+e\bigl(\boldsymbol A_\mu\cdot\partial_\nu\boldsymbol n
        -\boldsymbol A_\nu\cdot\partial_\mu\boldsymbol n\bigr)\\
&+e^2\boldsymbol n\cdot
 (\boldsymbol A_\mu\times\boldsymbol A_\nu).
\end{aligned}
\tag{92.60}
$$

把它代回式[（92.58）](#eq:c92-em-tensor)，最后一行与$\boldsymbol F_{\mu\nu}$中的非阿贝尔二次项相消。其余项补成普通乘积导数，得到
<span id="eq:c92-em-ordinary-form"></span>

$$
\mathcal F_{\mu\nu}
 =\partial_\mu(\boldsymbol n\cdot\boldsymbol A_\nu)
  -\partial_\nu(\boldsymbol n\cdot\boldsymbol A_\mu)
  -\frac1e\boldsymbol n\cdot
    (\partial_\mu\boldsymbol n\times\partial_\nu\boldsymbol n).
\tag{92.61}
$$

在$\boldsymbol n=(0,0,1)$的局部规范中，它恰好为$\partial_\mu A_\nu^3-\partial_\nu A_\mu^3$，符合电磁场强的要求。在$\varphi=0$的核心处，Higgs方向本来没有定义；原始的非阿贝尔场仍可保持光滑，稍后能量也应由原始场计算。

<span id="c92-magnetic-charge"></span>

## 磁通量与狄拉克量子化条件

取空间和内部$\epsilon^{123}=+1$。电磁磁场为
<span id="eq:c92-em-magnetic-field"></span>

$$
\mathcal B_i=\frac12\epsilon_{ijk}\mathcal F_{jk}
 =\epsilon_{ijk}\partial_j(n^aA_k^a)
 -\frac1{2e}\epsilon_{ijk}\epsilon^{abc}
 n^a\partial_jn^b\partial_kn^c .
\tag{92.62}
$$

磁通量是电磁二形式在外球面上的积分。若$n^aA_i^a\,dx^i$在该球面上为全局光滑一形式，第一项的闭曲面积分为零：把球面分成两个片，对各片用Stokes定理，公共边界方向相反而抵消。这样不必把Gauss定理穿过$\boldsymbol n$未定义的核心。第二项写成角坐标后，正是式[（92.51）](#eq:c92-sphere-degree)中的面积拉回，于是
<span id="eq:c92-monopole-flux"></span>

$$
\begin{aligned}
\Phi&=\oint dS_i\,\mathcal B_i
 =-\frac1e\int d\theta\,d\phi\,
 \boldsymbol n\cdot(\partial_\theta\boldsymbol n\times\partial_\phi\boldsymbol n)\\
 &=-\frac{4\pi n}{e}\equiv Q_M .
\end{aligned}
\tag{92.63}
$$

在Heaviside–洛伦兹单位中，点电荷场为$Q_E\hat{\boldsymbol r}/(4\pi r^2)$，总电通量等于$Q_E$；磁荷沿相同方式定义。因而正度数$n=1$在当前约定下对应负磁荷，磁场朝内。

若电磁势只在南、北两个片上定义，刚才的“闭曲面上旋度积分为零”便不能直接套用，因为两个片的势并不相同。这个拼接恰好给出狄拉克电荷量子化条件。对$\mathcal B=Q_M\hat{\boldsymbol r}/(4\pi r^2)$，可取
<span id="eq:c92-dirac-patches"></span>

$$
\begin{aligned}
\boldsymbol{\mathcal A}_N
 &=\frac{Q_M}{4\pi r}\frac{1-\cos\theta}{\sin\theta}\,
   \hat{\boldsymbol\phi},\\
\boldsymbol{\mathcal A}_S
 &=-\frac{Q_M}{4\pi r}\frac{1+\cos\theta}{\sin\theta}\,
   \hat{\boldsymbol\phi},\\
\boldsymbol{\mathcal A}_N-\boldsymbol{\mathcal A}_S
 &=\boldsymbol\nabla\Lambda,\qquad
 \Lambda=\frac{Q_M\phi}{2\pi}.
\end{aligned}
\tag{92.64}
$$

北片的势在北极正则，南片的势在南极正则。用球坐标旋度，
$\mathcal B_r=(r\sin\theta)^{-1}\partial_\theta(\sin\theta\,\mathcal A_\phi)$，两者都给要求的径向场。在公共区域，带电场的协变导数为$\partial-iQ_E\mathcal A$，故应以
<span id="eq:c92-dirac-quantization"></span>

$$
\psi_N=e^{iQ_E\Lambda}\psi_S,\qquad
e^{iQ_E[\Lambda(\phi+2\pi)-\Lambda(\phi)]}
=e^{iQ_EQ_M}=1,
\qquad Q_EQ_M=2\pi k,\quad k\in\mathbb Z
\tag{92.65}
$$

拼接。最后一个条件保证过渡函数绕赤道一周仍单值。

在全局群取$SU(2)$并允许基本表示时，$T^3=\sigma^3/2$的两个权重给$Q_E=\pm e/2$。与式[（92.63）](#eq:c92-monopole-flux)相乘，便有$k=\mp n$，恰好满足量子化条件。允许哪些表示属于全局群的定义；只写伴随场的局部拉氏量，还不足以把$SU(2)$与$SO(3)$的电荷格点混同。

<span id="c92-hedgehog"></span>

## 从渐近边界构造光滑单极子

现在取最简单的度数$n=1$，令无穷远的Higgs方向沿径向，
<span id="eq:c92-hedgehog-boundary"></span>

$$
\varphi^a(\boldsymbol x)\longrightarrow v\frac{x^a}{r},
\qquad r\to\infty .
\tag{92.66}
$$

空间方向与内部方向在这个拟设中相锁定，因而称hedgehog构型。要使远处的协变梯度消失，须有
<span id="eq:c92-hedgehog-parallel"></span>

$$
\partial_i\widehat x^a+e\epsilon^{abc}A_i^b\widehat x^c=0,
\qquad
\partial_i\widehat x^a=\frac{\delta_{ai}-\widehat x_a\widehat x_i}{r}.
\tag{92.67}
$$

一般局部解可以写成
<span id="eq:c92-asymptotic-connection"></span>

$$
\boldsymbol A_i
=-\frac1e\boldsymbol n\times\partial_i\boldsymbol n+c_i\boldsymbol n .
\tag{92.68}
$$

因为$(\boldsymbol n\times\partial_i\boldsymbol n)\times\boldsymbol n
=\partial_i\boldsymbol n$，第一项恰消普通梯度，而平行分量$c_i\boldsymbol n$不影响叉积。对$\boldsymbol n=\widehat{\boldsymbol x}$选$c_i=0$，得到$A_i^a=\epsilon^{aij}x_j/(er^2)$。

直接缩并指标也可到达同一结果：把式[（92.67）](#eq:c92-hedgehog-parallel)乘$r x_j\epsilon^{jda}$，并用
$\epsilon^{jda}\epsilon^{abc}=\delta^{jb}\delta^{dc}-\delta^{jc}\delta^{db}$，
便有
<span id="eq:c92-hedgehog-contraction"></span>

$$
\epsilon^{dij}x_j+e(x^d x_jA_i^j-r^2A_i^d)=0.
\tag{92.69}
$$

取$x_jA_i^j=0$后即得上述连接，它又自动满足这个条件。这是一个相容的选择，并不排除式[（92.68）](#eq:c92-asymptotic-connection)中的平行自由度。

将渐近解延拓到核心，取拟设
<span id="eq:c92-monopole-ansatz"></span>

$$
\varphi^a=vf(r)\widehat x_a,\qquad
A_i^a=\frac{a(r)}{er}\epsilon^{aij}\widehat x_j,\qquad
f(\infty)=a(\infty)=1 .
\tag{92.70}
$$

正则核心取$f=O(r)$、$a=O(r^2)$，配合相容的奇、偶展开，便使$\varphi^a$在原点近似正比于$x_a$、$A_i^a$近似正比于$\epsilon^{aij}x_j$。下面要把这个拟设实际代入场强，算出能量。

记$A_i^a=\epsilon^{aij}K_j$。场强定义给出
<span id="eq:c92-nonabelian-magnetic"></span>

$$
B_i^a=\epsilon_{ijk}\partial_jA_k^a
+\frac e2\epsilon_{ijk}\epsilon^{abc}A_j^bA_k^c .
\tag{92.71}
$$

线性项用$\epsilon_{ijk}\epsilon^{akl}
=\delta_{il}\delta_{ja}-\delta_{ia}\delta_{jl}$变为
$\partial_aK_i-\delta_{ai}\partial_jK_j$。二次项的缩并为
<span id="eq:c92-magnetic-epsilon-contraction"></span>

$$
\begin{aligned}
\frac12\epsilon_{ijk}\epsilon^{abc}\epsilon^{bjl}\epsilon^{ckm}K_lK_m
&=\frac12\epsilon_{ijk}
  (\delta_{al}\epsilon^{jkm}-\delta_{aj}\epsilon^{lkm})K_lK_m\\
&=K_aK_i .
\end{aligned}
\tag{92.72}
$$

第一项用$\epsilon_{ijk}\epsilon^{jkm}=2\delta_{im}$；第二项与对称的$K_lK_m$缩并为零。因此
<span id="eq:c92-magnetic-k-form"></span>

$$
B_i^a=\partial_aK_i-\delta_{ai}\partial_jK_j+eK_aK_i.
\tag{92.73}
$$

最后一项带着非阿贝尔场强中的耦合$e$，与两个导数项具有相同量纲。

为继续计算，令$K_i=b(r)x_i$、$b=a/(er^2)$，并定义
$P_{ai}=\delta_{ai}-\widehat x_a\widehat x_i$、
$Q_{ai}=\widehat x_a\widehat x_i$。普通导数为
$\partial_aK_i=b\delta_{ai}+rb'Q_{ai}$、
$\partial_jK_j=3b+rb'$。于是横向和径向系数分别为
$-2b-rb'=-a_r/(er)$及$-2b+eb^2r^2=-(2a-a^2)/(er^2)$，得到
<span id="eq:c92-monopole-fields"></span>

$$
\begin{aligned}
B_i^a&=-\frac1e\left[\frac{a_r}{r}P_{ai}
                       +\frac{2a-a^2}{r^2}Q_{ai}\right],\\
(D_i\varphi)^a&=v\left[\frac{(1-a)f}{r}P_{ai}+f_rQ_{ai}\right].
\end{aligned}
\tag{92.74}
$$

第二行的普通导数给$v(fP/r+f_rQ)$，连接项减去$vafP/r$，所以只改变横向部分。

现在所有平方都可由三个简单缩并求出：
<span id="eq:c92-monopole-projectors"></span>

$$
P_{ai}P_{ai}=3-2+1=2,\qquad
Q_{ai}Q_{ai}=1,\qquad P_{ai}Q_{ai}=0.
\tag{92.75}
$$

因此
<span id="eq:c92-monopole-densities"></span>

$$
\begin{aligned}
\frac12B_i^aB_i^a
 &=\frac1{2e^2r^4}\left[2r^2a_r^2+(2a-a^2)^2\right],\\
\frac12(D_i\varphi)^a(D_i\varphi)^a
 &=\frac{v^2}{2r^2}\left[2(1-a)^2f^2+r^2f_r^2\right],\\
V&=\frac{\lambda v^4}{8}(f^2-1)^2 .
\end{aligned}
\tag{92.76}
$$

横向有两个方向，径向只有一个方向，两个因子2由此出现。把三项相加再乘球面测度$4\pi r^2dr$，就得到了径向能量泛函。

本模型中取$\rho=evr=m_Wr$、$\kappa=\lambda/e^2$，以撇号表示$d/d\rho$，有
<span id="eq:c92-monopole-radial-energy"></span>

$$
M=\frac{4\pi v}{e}\int_0^\infty d\rho\left[
a'^2+\frac{(2a-a^2)^2}{2\rho^2}
+(1-a)^2f^2+\frac{\rho^2f'^2}{2}
+\frac{\kappa\rho^2}{8}(f^2-1)^2\right].
\tag{92.77}
$$

这里$\rho$用于实三重态模型，等于物理矢量质量乘半径。对$a$的无导数项求导，分别得到
$2(2a-a^2)(1-a)/\rho^2$和$-2(1-a)f^2$；导数项给$2a''$。对$f$，导数项给$(\rho^2f')'$。由Euler–Lagrange方程便得
<span id="eq:c92-monopole-second-order"></span>

$$
\begin{aligned}
a''&=(1-a)\left[\frac{2a-a^2}{\rho^2}-f^2\right],\\
f''+\frac{2f'}{\rho}
-\frac{2(1-a)^2f}{\rho^2}
+\frac{\kappa}{2}(1-f^2)f&=0 .
\end{aligned}
\tag{92.78}
$$

它们与$f(0)=a(0)=0$的正则支以及无穷远的单位边界共同决定轮廓。接下来无需先求出一般$\kappa$下的解，就能得到它的质量下界。

<span id="c92-monopole-bound"></span>

## 磁单极子的质量界与长程作用

从完整三维静态能量出发，令$s=\operatorname{sign}n$，
<span id="eq:c92-monopole-square"></span>

$$
\frac12B_i^aB_i^a+\frac12(D_i\varphi)^a(D_i\varphi)^a
=\frac12[B_i^a+s(D_i\varphi)^a]^2
-sB_i^a(D_i\varphi)^a .
\tag{92.79}
$$

余下的交叉项仍能化成边界项。把[第70节的协变乘积法则](/posts/srednicki-70/#c70-covariant-products)用于$B_i^a\varphi^a$，
<span id="eq:c92-monopole-bianchi"></span>

$$
\begin{aligned}
\partial_i(B_i^a\varphi^a)
 &=(D_iB_i)^a\varphi^a+B_i^a(D_i\varphi)^a,\\
(D_iB_i)^a
 &=\frac12\epsilon_{ijk}(D_iF_{jk})^a=0 .
\end{aligned}
\tag{92.80}
$$

第一行中两个连接项为
$e\epsilon^{abc}A_i^b(B_i^c\varphi^a+B_i^a\varphi^c)$，因$a,c$交换而相消。第二行用[比安基恒等式](/posts/srednicki-70/#c70-bianchi)：三个循环导数项与$\epsilon_{ijk}$缩并后相等，所以每项都为零。

因此$\int B_i^a(D_i\varphi)^a=\oint dS_iB_i^a\varphi^a$。在具有本节有限能量渐近形式的外球面，$\varphi^a\to vn^a$、$D_i\boldsymbol n$的贡献趋零，式[（92.58）](#eq:c92-em-tensor)便给
<span id="eq:c92-monopole-surface"></span>

$$
\int d^3x\,B_i^a(D_i\varphi)^a
=\lim_{r\to\infty}\oint dS_i\,B_i^a\varphi^a
=v\Phi=-\frac{4\pi nv}{e}.
\tag{92.81}
$$

于是
<span id="eq:c92-monopole-bogomolny"></span>

$$
\begin{aligned}
M&=\frac{4\pi v|n|}{e}
 +\int d^3x\left\{\frac12[B_i^a+s(D_i\varphi)^a]^2+V(\varphi)\right\},\\
M&\ge\frac{4\pi v|n|}{e}
 =\frac{m_W}{\alpha}|n|,\qquad \alpha=\frac{e^2}{4\pi}.
\end{aligned}
\tag{92.82}
$$

正度数的磁荷为负，所以平方中的加号给正的边界贡献。这个推导适用于各个平滑有限能量拓扑扇区，而不依赖$n=1$的球对称拟设。在弱耦合$\alpha\ll1$时，质量至少比$m_W$大一个$1/\alpha$因子；这里同样出现了基本激发与拓扑构型之间的尺度分离。

高磁荷构型能否裂变，还需要进一步的能量比较。下界本身只给$M_n\ge C|n|$，而单个单位磁荷的质量也只知$M_1\ge C$，因而还不能比较$M_n$和$|n|M_1$。先看可直接说明的长程力。两个相同磁荷相距$R$，在核心尺度之外，磁能的交叉项是
<span id="eq:c92-monopole-coulomb"></span>

$$
V_{\mathrm{mag}}(R)
=\int d^3x\,\boldsymbol{\mathcal B}_1\cdot\boldsymbol{\mathcal B}_2
=\frac{Q_M^2}{4\pi R}.
\tag{92.83}
$$

最后一步可令$\boldsymbol{\mathcal B}_i=-\nabla\Psi_i$、
$-\nabla^2\Psi_i=Q_M\delta(\boldsymbol x-\boldsymbol X_i)$，分部积分后取$\Psi_1(\boldsymbol X_2)$。它为正，故同号磁荷相斥。Higgs径向振动质量为$m_S=\sqrt\lambda v$；若用局部源$J$描述其远场，静态二次能量为
<span id="eq:c92-monopole-scalar-force"></span>

$$
\begin{aligned}
E_h&=\frac12\int d^3x\,h(-\nabla^2+m_S^2)h-\int d^3x\,Jh,\\
h&=G_{m_S}J,\qquad
E_h=-\frac12\int d^3x\,d^3y\,J(\boldsymbol x)G_{m_S}(\boldsymbol x-\boldsymbol y)J(\boldsymbol y),\\
V_{\mathrm{scalar}}(R)&=-\frac{q_s^2}{4\pi R}e^{-m_SR}.
\end{aligned}
\tag{92.84}
$$

这里$G_m(R)=e^{-mR}/(4\pi R)$，$q_s$由核心匹配确定。平方完成后的负号说明同号标量源相吸；$\lambda>0$时这项指数衰减，而磁相互作用保留$1/R$，所以大分离处的领头作用为排斥。BPS极限中标量也无质量，不能再按这个理由略去它。

已有数值研究对特定多单极子作了进一步比较。[Kleihaus、Kunz 和 Tchrakian](https://arxiv.org/pdf/hep-th/9804192v1#page=4)用反厄米矩阵$\Phi=ih^a\sigma^a/2$及势$\lambda_K(2\operatorname{Tr}\Phi^2+1)^2/16$。取$h^a=\varphi^a/v$、无量纲坐标$ev\boldsymbol x$，由$2\operatorname{Tr}\Phi^2=-h^ah^a$，得到$\lambda_K=2\lambda/e^2$，其能量乘$v/e$才成为本节的$M$。他们的轴对称计算在$10^{-5}\le\lambda_K\le10^5$的取样范围内给出$M_2/2>M_1$，并考察了小耦合的磁荷3。

这些数值结果支持上述长程排斥。推广到更高磁荷时，还要比较不同形状构型的能量；给定初态怎样分离则由完整的时间演化决定。

<span id="c92-electroweak-topology"></span>

## 电弱真空与统一模型的区别

Georgi–Glashow模型的真空方向是二球面，允许刚才的非零度数；普通单Higgs双重态电弱模型的情形不同。在[第87节的模型](/posts/srednicki-87/#c87-model)中，
<span id="eq:c92-electroweak-vacuum-sphere"></span>

$$
\varphi^\dagger\varphi=\frac{v_{\mathrm{EW}}^2}{2},
\qquad
\frac{\sqrt2\varphi}{v_{\mathrm{EW}}}
=(z_1,z_2)\in\mathbb C^2,\qquad |z_1|^2+|z_2|^2=1 .
\tag{92.85}
$$

这是真空轨道$S^3$。一个平滑的$S^2\to S^3$映射可以收缩成常映射：紧致二球可用$O(\varepsilon^{-2})$个直径$\varepsilon$的小片覆盖，光滑映射在各片上具有有界导数，其像落在直径$O(\varepsilon)$的三球小片内。像的三维体积因而至多为$O(\varepsilon^{-2}\varepsilon^3)=O(\varepsilon)$。令$\varepsilon\to0$，可知像没有覆盖整个$S^3$。选一个未覆盖的点作立体投影，整个像就落在$\mathbb R^3$中，以线性插值收缩到一点，再逆投影回来即可。连续映射与光滑代表之间的衔接与前面的逼近相同，故
<span id="eq:c92-electroweak-pi2"></span>

$$
\pi_2(S^3)=0 .
\tag{92.86}
$$

因此该真空轨道没有本节这种由Higgs二球度数保护的平滑单极子扇区。

这里还要固定规范群的全局定义。对固定的紧致$U(1)$，周期已经规定了单值表示的荷格点，不能在同一个全局群中任意加入实数小电荷；改变场内容或群的全局定义，也是在改变模型。真空轨道的分析已经直接说明了上述两种模型的拓扑区别。

若把规范群扩大为单一非阿贝尔群，例如第97节的$SU(5)$，破缺后又可能留下带非平凡二球拓扑的真空轨道。质量的量级仍由重矢量尺度除以耦合决定，
<span id="eq:c92-gut-monopole-scale"></span>

$$
M_{\mathrm{monopole}}\sim\frac{m_X}{\alpha}.
\tag{92.87}
$$

若以$m_X\sim10^{15}\,\mathrm{GeV}$作为假设的统一尺度，这个估计说明了单极子为何极重。第97节将给出具体的场内容与破缺结构。

<span id="c92-monopole-bps"></span>

## 求出BPS单极子的闭式解

回到实三重态模型，令$\lambda=0$，并把$|\varphi|\to v$保留为无穷远的边界条件。势不再选择$v$，但这个固定边界的经典问题仍然成立。若能令式[（92.82）](#eq:c92-monopole-bogomolny)中的平方也为零，就达到质量下界。对$n=1$，饱和条件为$B_i^a=-(D_i\varphi)^a$。分别比较式[（92.74）](#eq:c92-monopole-fields)中的$P_{ai}$和$Q_{ai}$，得到
<span id="eq:c92-monopole-first-order"></span>

$$
a'=(1-a)f,\qquad
f'=\frac{2a-a^2}{\rho^2},\qquad \rho=evr .
\tag{92.88}
$$

第一式来自$a_r/(er)=v(1-a)f/r$，第二式来自$(2a-a^2)/(er^2)=vf_r$。

为了真正解出这个系统，令$w=1-a$。由$w'=-wf$及$w(0)=1$，在任意有限的正则区间中都有$w=\exp[-\int_0^\rho f(s)ds]>0$，因而可以取$w=\rho/u$。于是
<span id="eq:c92-bps-substitution"></span>

$$
f=\frac{u'}u-\frac1\rho,\qquad
f'=\frac{u''u-u'^2}{u^2}+\frac1{\rho^2}.
\tag{92.89}
$$

第二个一阶方程又要求$f'=1/\rho^2-1/u^2$，所以
<span id="eq:c92-bps-first-integral"></span>

$$
uu''-u'^2=-1,\qquad
\frac{d}{d\rho}\left(\frac{u'^2-1}{u^2}\right)
=\frac{2u'}{u^3}(uu''-u'^2+1)=0.
\tag{92.90}
$$

因此$u'^2=1+c u^2$，其中$c$是积分常数。正则核心$w(0)=1$要求$u(0)=0,u'(0)=1$。若$c=k^2>0$，分离变量给$\operatorname{arsinh}(ku)/k=\rho$，即$u=\sinh(k\rho)/k$；于是$f(\infty)=k$，单位边界固定$k=1$。$c=0$给$u=\rho$、$f=0$，不满足远边界；$c<0$给正弦解，会再次经过零，不能提供全正半轴的正则轮廓。故
<span id="eq:c92-bps-profiles"></span>

$$
a(\rho)=1-\frac{\rho}{\sinh\rho},\qquad
f(\rho)=\coth\rho-\frac1\rho .
\tag{92.91}
$$

这就是Bogomolny–Prasad–Sommerfeld解，简称BPS解；达到相应Bogomolny界的孤子称为BPS孤子。

两端边界也可直接检验。由$\sinh\rho=\rho+\rho^3/6+\rho^5/120+\cdots$和$\cosh\rho=1+\rho^2/2+\rho^4/24+\cdots$，
<span id="eq:c92-bps-limits"></span>

$$
\begin{aligned}
a&=\frac{\rho^2}{6}-\frac{7\rho^4}{360}+O(\rho^6),&
f&=\frac{\rho}{3}-\frac{\rho^3}{45}+O(\rho^5),\qquad \rho\to0,\\
1-a&=2\rho e^{-\rho}[1+O(e^{-2\rho})],&
f&=1-\frac1\rho+2e^{-2\rho}+O(e^{-4\rho}),\qquad \rho\to\infty .
\end{aligned}
\tag{92.92}
$$

核心具有所需的正则幂次；远处标量的$1/\rho$尾对应$\lambda=0$时的无质量径向场，其梯度平方仍按$r^{-4}$衰减，三维总能量有限。继续对式[（92.88）](#eq:c92-monopole-first-order)求导，
<span id="eq:c92-bps-second-order-check"></span>

$$
\begin{aligned}
a''&=-(1-a)f^2+(1-a)\frac{2a-a^2}{\rho^2},\\
f''+\frac{2f'}{\rho}
 &=\frac{2(1-a)a'}{\rho^2}
 =\frac{2(1-a)^2f}{\rho^2},
\end{aligned}
\tag{92.93}
$$

便恢复$\kappa=0$的两个二阶方程。

最后把能量积分也求完。临界时，将一阶关系代入式[（92.77）](#eq:c92-monopole-radial-energy)的密度，得到
<span id="eq:c92-bps-energy-evaluation"></span>

$$
\begin{aligned}
\mathcal I(\rho)
 &=2(1-a)^2f^2+\frac{(2a-a^2)^2}{\rho^2}\\
 &=\frac{d}{d\rho}\bigl[f(2a-a^2)\bigr],\\
M(\rho\le R)
 &=\frac{4\pi v}{e}\,f(R)[2a(R)-a(R)^2],\\
M&=\frac{4\pi v}{e}.
\end{aligned}
\tag{92.94}
$$

求导时第一项给$f'(2a-a^2)=(2a-a^2)^2/\rho^2$，第二项给$2f(1-a)a'=2(1-a)^2f^2$；下端边界为零，上端趋1。这个结果既显示质量界被饱和，也给数值计算一个带有限半径边界的检验式。注意$f(R)=1-1/R+O(e^{-2R})$，故尚在半径$R$之外的能量占总量$1/R+O(R^2e^{-2R})$。例如无量纲半径40内只含97.5%的总能量，积分时不能把剩下的长程尾部当作指数小量。

本节从同一思路得到了三种不同的构型：真空边界要求场在核心发生变化，能量配方则把一部分能量变成边界量。规范涡旋把圆的缠绕数变成磁通，实三重态单极子把二球度数变成磁荷。它们的具体质量、大小与相互作用仍由动力学决定；拓扑首先固定的是不能在保持远边界时连续改变的整数。

---

[← 第 91 节](/posts/srednicki-91/) · [章节地图](/srednicki/) · [第 93 节 →](/posts/srednicki-93/)
