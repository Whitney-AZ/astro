---
title: 'Srednicki §52 汤川 理论中的 beta 函数'
date: 2026-09-14
category: 笔记
tags: [物理, 量子场论, Srednicki]
series: 'Srednicki QFT'
srednickiSections: [52]
hideFromHome: true
draft: false
---

<span id="c52"></span>

上一节的圈图给出了自能和顶角，也告诉我们应当怎样选择反项，
使质量、留数和耦合满足预定的归一条件。现在换一个问题：
若用不同的重整化能标描述同一个理论，耦合常数应当怎样变化？
计算所需的信息已经包含在那些反项中。我们只须保持裸作用量不变，
就能从紫外极点求出两个耦合的beta函数。
与第28节相比，这里的新特点是$g$和$\lambda$同时参与重整化；
一个反项对两个耦合的依赖都必须计入尺度微分。

以下沿用上一节的赝标量相互作用$ig\varphi\bar\Psi\gamma_5\Psi$，
并采用第28节的$\overline{\mathrm{MS}}$方案。
两章之间有限归一条件的转换将在计算中说明。

<span id="c52-bare"></span>

## 从裸作用量确定耦合关系

先把场的归一化从相互作用系数中分离出来。裸场的动能取通常的单位系数，
而重整化场的动能带有$Z_\varphi$或$Z_\Psi$。因此

<span id="eq:c52-bare-fields"></span>

$$
\begin{gathered}
\varphi_0=Z_\varphi^{1/2}\varphi,\qquad
\Psi_0=Z_\Psi^{1/2}\Psi,\qquad
\bar\Psi_0=Z_\Psi^{1/2}\bar\Psi,\\
\mathcal L_{0,\mathrm{int}}
=ig_0\varphi_0\bar\Psi_0\gamma_5\Psi_0
-\frac{\lambda_0}{4!}\varphi_0^4.
\end{gathered}
\tag{52.1}
$$

汤川项中有一条标量腿、两条旋量腿，代入场的关系后，
它的系数为$g_0Z_\varphi^{1/2}Z_\Psi$。
四标量项则带有$Z_\varphi^2$。逐项与上一节的重整化拉格朗日量比较，便得到

<span id="eq:c52-bare-couplings"></span>

$$
\begin{aligned}
g_0&=Z_\varphi^{-1/2}Z_\Psi^{-1}Z_g
       \widetilde\mu^{\varepsilon/2}g,\\
\lambda_0&=Z_\varphi^{-2}Z_\lambda
       \widetilde\mu^\varepsilon\lambda .
\end{aligned}
\tag{52.2}
$$

其中$d=4-\varepsilon$，
$g,\lambda$无量纲，裸耦合的质量维数分别为$\varepsilon/2$和$\varepsilon$。
这些工程维数决定了两个不同的尺度因子。我们仍取
$\mu^2=4\pi e^{-\gamma_E}\widetilde\mu^2$，
所以对$\ln\mu$和对$\ln\widetilde\mu$求导相同，
但有限对数里的两个尺度不能直接互换。

还有一项归一条件需要接清楚。上一节把$m,M$定义为极点质量，
把单粒子留数归一为一，并在零外动量处定义$g,\lambda$。
以下把这组参数记为下标$o$，把$\overline{\mathrm{MS}}$参数记为下标$r$。
对于上一节已算出的每个反项，可写成

<span id="eq:c52-scheme-counterterms"></span>

$$
Z_j^{o}=1+\frac{a_j}{\varepsilon}+f_j+\text{更高圈},
\qquad
Z_j^{r}=1+\frac{a_j}{\varepsilon}+\text{更高圈}.
\tag{52.3}
$$

$a_j$是简单极点的残数，$f_j$是上一节归一条件要求的有限部分。
第二个等式规定了这里的最小减除方案。两个方案描述同一个裸作用量，
于是把它们分别代入式[（52.2）](#eq:c52-bare-couplings)，再展开到一圈，
极点相消后给出

<span id="eq:c52-finite-matching"></span>

$$
\begin{aligned}
g_r&=g_o\left(1+f_g-\tfrac12f_\varphi-f_\Psi\right)
       +\text{更高圈},\\
\lambda_r&=\lambda_o+f_{\delta\lambda}
               -2\lambda_o f_\varphi+\text{更高圈},
\qquad f_{\delta\lambda}:=\lambda_o f_\lambda .
\end{aligned}
\tag{52.4}
$$

右边的有限项全部用$o$方案的参数评价。这里各个负号来自裸耦合关系中的
逆场归一因子，例如$(1+f_\varphi)^{-1/2}=1-f_\varphi/2+\cdots$。
四价耦合用加性形式书写，因而$\lambda_o=0$时仍然适用。
这些有限项的具体表达式留在本节最后与尺度微分一起使用；
求beta函数本身只需要简单极点。以下省去$r$下标，
$g,\lambda,m,M$均指$\overline{\mathrm{MS}}$参数。

<span id="c52-residues"></span>

## 两个极点函数

最小减除的反项只有$\varepsilon$的负幂。
把裸耦合中的几个$Z$因子合并并取对数，可以把后面的链式微分写得更紧凑。
定义

<span id="eq:c52-pole-functions"></span>

$$
\begin{aligned}
G(g,\lambda,\varepsilon)
&:=\ln\!\left(Z_\varphi^{-1/2}Z_\Psi^{-1}Z_g\right)
  =\sum_{n\geq1}\frac{G_n(g,\lambda)}{\varepsilon^n},\\
L(g,\lambda,\varepsilon)
&:=\ln\!\left(Z_\varphi^{-2}Z_\lambda\right)
  =\sum_{n\geq1}\frac{L_n(g,\lambda)}{\varepsilon^n}.
\end{aligned}
\tag{52.5}
$$

$n$表示极点次数，每个$G_n,L_n$本身还要按圈数展开。
对数仍只有极点，是因为$\ln(1+u)=u-u^2/2+\cdots$中的$u$
没有有限部分；$u^2$至少含二重极点。特别地，$\ln Z$和$Z-1$
的简单极点相同。上一节的四个有关残数为

<span id="eq:c52-pole-data"></span>

$$
\begin{aligned}
a_\varphi&=-\frac{4g^2}{16\pi^2},&
a_\Psi&=-\frac{g^2}{16\pi^2},\\
a_g&=\frac{2g^2}{16\pi^2},&
a_\lambda&=\frac{3\lambda-48g^4/\lambda}{16\pi^2}.
\end{aligned}
\tag{52.6}
$$

最后一项来自三种标量泡图与六种费米盒图。
这里使用的是[上一节四标量顶角](/posts/srednicki-51/#c51-four-vertex)中已经由顶角次数确定的$\lambda^2$贡献。
按式[（52.5）](#eq:c52-pole-functions)中的幂次相加，得到

<span id="eq:c52-simple-residues"></span>

$$
\begin{aligned}
G_1
&=-\tfrac12a_\varphi-a_\Psi+a_g+\text{更高圈}
 =\frac{(2+1+2)g^2}{16\pi^2}+\text{更高圈},\\
L_1
&=-2a_\varphi+a_\lambda+\text{更高圈}
 =\frac{3\lambda+8g^2-48g^4/\lambda}{16\pi^2}
       +\text{更高圈}.
\end{aligned}
\tag{52.7}
$$

汤川顶角的反项只给出了第一个残数中的最后一项；
场归一化还贡献$2+1$。这说明，顶角的紫外修正虽然直接改变相互作用，
却不能独自决定耦合的尺度变化。把相互作用写成归一化场的系数后，
外腿的归一化也进入裸耦合关系。

<span id="c52-rg"></span>

## 固定裸耦合的尺度微分

现在令$t=\ln\mu$，在固定裸参数和$\varepsilon$的条件下求导。
在$g,\lambda$非零的定号区间，裸耦合关系可写成

<span id="eq:c52-bare-logs"></span>

$$
\begin{aligned}
\ln|g_0|
 &=\ln|g|+\frac{\varepsilon}{2}\ln\widetilde\mu
     +\sum_{n\geq1}\frac{G_n}{\varepsilon^n},\\
\ln|\lambda_0|
 &=\ln|\lambda|+\varepsilon\ln\widetilde\mu
     +\sum_{n\geq1}\frac{L_n}{\varepsilon^n}.
\end{aligned}
\tag{52.8}
$$

有量纲的量在取对数前可各除以一个固定单位；
这个选择不影响以下导数。绝对值则使同一推导也适用于负$\lambda$的定号区间。
在耦合的零点，我们稍后直接对加性裸关系求导。

记$B_g=dg/dt$、$B_\lambda=d\lambda/dt$。
因为每个极点函数都依赖两个耦合，其导数为
$dG_n/dt=B_g\partial_gG_n+B_\lambda\partial_\lambda G_n$；
对$L_n$也一样。裸耦合不变，分别乘回$g$和$\lambda$后便有

<span id="eq:c52-chain-rule"></span>

$$
\begin{aligned}
0={}&B_g+\frac{\varepsilon g}{2}
 +g\sum_{n\geq1}
 \frac{B_g\partial_gG_n+B_\lambda\partial_\lambda G_n}{\varepsilon^n},\\
0={}&B_\lambda+\varepsilon\lambda
 +\lambda\sum_{n\geq1}
 \frac{B_g\partial_gL_n+B_\lambda\partial_\lambda L_n}{\varepsilon^n}.
\end{aligned}
\tag{52.9}
$$

为看清$B_g,B_\lambda$对调节参数的依赖，把它们写成一个矩阵方程：

<span id="eq:c52-matrix-chain"></span>

$$
\begin{gathered}
\left[I+\sum_{n\geq1}\frac{\mathcal A_n}{\varepsilon^n}\right]
\begin{pmatrix}B_g\\B_\lambda\end{pmatrix}
=-\varepsilon\begin{pmatrix}g/2\\\lambda\end{pmatrix},\\
\mathcal A_n=
\begin{pmatrix}
g\partial_gG_n&g\partial_\lambda G_n\\
\lambda\partial_gL_n&\lambda\partial_\lambda L_n
\end{pmatrix}.
\end{gathered}
\tag{52.10}
$$

左边矩阵为单位阵加圈修正。按圈数展开其逆矩阵，
第一项是$I$，其它每一项都至少含一个$\varepsilon^{-1}$。
再乘右边的$-\varepsilon$，树项给出工程维数的贡献，
其余各项至多含$\varepsilon^0$，不会产生新的正幂。
重整化参数的尺度导数须在$\varepsilon\to0$时逐阶有限，
于是负幂系数全部相消，剩下

<span id="eq:c52-regulated-beta"></span>

$$
B_g=-\frac{\varepsilon}{2}g+\beta_g(g,\lambda),
\qquad
B_\lambda=-\varepsilon\lambda+\beta_\lambda(g,\lambda).
\tag{52.11}
$$

其中$\beta_g,\beta_\lambda$就是四维的尺度导数。
这个结论用到了纯极点方案和有限性两项条件：
前者限定了可能出现的$\varepsilon$次幂，后者消去了负幂。
第28节对一个耦合所作的论证，在这里成为同一个形式逆矩阵的展开。

将工程维数的两项合并，定义微分算符

<span id="eq:c52-euler"></span>

$$
\mathscr E:=\frac{g}{2}\frac{\partial}{\partial g}
              +\lambda\frac{\partial}{\partial\lambda}.
\tag{52.12}
$$

例如$B_g\partial_gG_n+B_\lambda\partial_\lambda G_n$
等于$-\varepsilon\mathscr EG_n+
(\beta_g\partial_g+\beta_\lambda\partial_\lambda)G_n$。
将此式代入式[（52.9）](#eq:c52-chain-rule)，单独提出$n=1$的有限项，
再把其余工程项的下标从$n$换成$n+1$，得到

<span id="eq:c52-laurent-matching"></span>

$$
\begin{aligned}
0={}&\beta_g-g\mathscr EG_1\\
&+g\sum_{n\geq1}
\frac{(\beta_g\partial_g+\beta_\lambda\partial_\lambda)G_n
      -\mathscr EG_{n+1}}{\varepsilon^n},\\
0={}&\beta_\lambda-\lambda\mathscr EL_1\\
&+\lambda\sum_{n\geq1}
\frac{(\beta_g\partial_g+\beta_\lambda\partial_\lambda)L_n
      -\mathscr EL_{n+1}}{\varepsilon^n}.
\end{aligned}
\tag{52.13}
$$

这里的有限贡献有一个很直接的来源：
工程项中的$\varepsilon$恰好约去简单极点中的$1/\varepsilon$。
比较有限项便得到双耦合的beta函数公式

<span id="eq:c52-beta-from-poles"></span>

$$
\boxed{\displaystyle
\beta_g=g\mathscr EG_1,\qquad
\beta_\lambda=\lambda\mathscr EL_1.}
\tag{52.14}
$$

其余负幂系数也必须为零，因此

<span id="eq:c52-higher-poles"></span>

$$
\begin{aligned}
\mathscr EG_{n+1}
 &=(\beta_g\partial_g+\beta_\lambda\partial_\lambda)G_n,\\
\mathscr EL_{n+1}
 &=(\beta_g\partial_g+\beta_\lambda\partial_\lambda)L_n,
\qquad n\geq1 .
\end{aligned}
\tag{52.15}
$$

这些关系约束多重极点，保证不同圈阶的反项能够共同消除发散。
它们并不提供尚未计算的高圈简单极点；因而知道一圈$G_1,L_1$，
仍然只能确定一圈beta函数。要推进到更高圈，还需相应的简单极点作为新的独立输入。

<span id="c52-beta"></span>

## 一圈结果及其物理含义

式[（52.7）](#eq:c52-simple-residues)中只出现$g^2,\lambda,g^4/\lambda$
三种结构。$\mathscr E$对它们的作用可以直接算出：

<span id="eq:c52-weights"></span>

$$
\mathscr E g^2=g^2,\qquad
\mathscr E\lambda=\lambda,\qquad
\mathscr E\frac{g^4}{\lambda}
=\frac{g}{2}\frac{4g^3}{\lambda}
 +\lambda\left(-\frac{g^4}{\lambda^2}\right)
=\frac{g^4}{\lambda}.
\tag{52.16}
$$

最后一项同时依赖两个耦合，对$\lambda$的导数少算一次，
费米盒图对beta函数的贡献就会多出一倍。
三项的权重都是一，所以代入式[（52.14）](#eq:c52-beta-from-poles)后有

<span id="eq:c52-one-loop-beta"></span>

$$
\begin{aligned}
\beta_g(g,\lambda)
 &=\frac{5g^3}{16\pi^2}+\text{更高圈},\\
\beta_\lambda(g,\lambda)
 &=\frac{3\lambda^2+8\lambda g^2-48g^4}{16\pi^2}
       +\text{更高圈}.
\end{aligned}
\tag{52.17}
$$

四价耦合的第一项来自标量圈，第二项来自标量场归一化，
第三项来自费米盒图。在$g=0$时，后两项消失，
此时$\beta_\lambda=3\lambda^2/(16\pi^2)$，正是四维实四次理论的一圈结果。
对于非零$g$，即使在某个能标把$\lambda$取为零，
其尺度导数仍为$-3g^4/\pi^2$。
因此$\lambda=0$不能在改变能标时一直保持，四标量相互作用会被费米圈生成。

上述结论在$\lambda=0$处是有限的，虽然用于中间计算的$L_1$含有
$g^4/\lambda$。为了直接看到这一点，把裸耦合写成加性形式：

<span id="eq:c52-additive-bare"></span>

$$
\begin{aligned}
g_0&=\widetilde\mu^{\varepsilon/2}
 \left[g+\frac{b_g}{\varepsilon}+\cdots\right],
& b_g&=\frac{5g^3}{16\pi^2},\\
\lambda_0&=\widetilde\mu^\varepsilon
 \left[\lambda+\frac{b_\lambda}{\varepsilon}+\cdots\right],
& b_\lambda&=\frac{3\lambda^2+8\lambda g^2-48g^4}{16\pi^2}.
\end{aligned}
\tag{52.18}
$$

省略号包括更高圈的简单极点和多重极点。
对第一式求尺度导数时，显式的$\widetilde\mu^{\varepsilon/2}$
乘$b_g/\varepsilon$留下$b_g/2$；
反项的耦合导数则由工程项给出$-\mathscr Eb_g$。
第二式中的相应两项是$b_\lambda$和$-\mathscr Eb_\lambda$。
因此一圈有限部分满足

<span id="eq:c52-additive-beta"></span>

$$
\beta_g=(\mathscr E-\tfrac12)b_g,\qquad
\beta_\lambda=(\mathscr E-1)b_\lambda.
\tag{52.19}
$$

$b_g$的权重为$3/2$，$b_\lambda$的每一项权重均为二，
所以仍得到式[（52.17）](#eq:c52-one-loop-beta)。
这次推导只用了多项式，在耦合的零点同样有效。
$L_1$中的分母来自把加性反项除以$\lambda$，
并不表示四价顶角在零耦合处发生新的发散。

一圈近似要求$g^2/(16\pi^2)$和$|\lambda|/(16\pi^2)$都小。
更高圈会带来额外的$g^2$或$\lambda$因子及相应圈因子；
它们在接近强耦合时不能继续忽略。
在这一范围内，第一条beta函数已经能说明汤川耦合的变化方向。
取参考能标$\mu_\star$及$g_\star=g(\mu_\star)$，则
$d(g^{-2})/d\ln\mu=-5/(8\pi^2)$，积分得到

<span id="eq:c52-g-running"></span>

$$
g^2(\mu)=
\frac{g_\star^2}
 {1-\dfrac{5g_\star^2}{8\pi^2}\ln(\mu/\mu_\star)}
\qquad\text{（一圈演化）}.
\tag{52.20}
$$

因而$|g|$随能标升高而增大。若把这个解外推，分母会在某个有限能标为零；
在到达该处以前，耦合已进入一圈计算不再可靠的区域。
四价耦合还受到三个不同号的贡献，其演化须与$g$一起求解，
不能单凭$\beta_g$的正号判断。

<span id="c52-finite-conversion"></span>

## 从有限归一条件理解同一尺度变化

为了把这一结果与上一节接起来，现在具体计算
式[（52.4）](#eq:c52-finite-matching)中的有限项。
这也给出另一种理解beta函数的办法：固定上一节定义的质量和零动量耦合，
考察相应的$\overline{\mathrm{MS}}$参数怎样随$\mu$变化。
以下右边全部使用$m_o>0,\ 0<M_o<2m_o$及$g_o,\lambda_o$。

令$a=x(1-x)$。在上一节的标量质量壳上，费米泡图的参数分母为
$D_s=m_o^2-aM_o^2>0$。对未减除自能关于$k^2$求导，
取$k^2=-M_o^2$并去掉极点，得到波函数反项的有限部分

<span id="eq:c52-finite-scalar-z"></span>

$$
\begin{aligned}
f_\varphi
&=\frac{g_o^2}{4\pi^2}
\left[-\frac16+\int_0^1dx
\left(3a\ln\frac{D_s}{\mu^2}
       +\frac{a(m_o^2-3aM_o^2)}{D_s}\right)\right],\\
D_s&=m_o^2-aM_o^2 .
\end{aligned}
\tag{52.21}
$$

其中$-1/6$来自自能的显式$k^2/6$项；
积分的第一项来自对对数前面的多项式求导，
第二项来自对分母中的$k^2$求导。标量蝌蚪图不依赖$k^2$，
所以不进入$f_\varphi$。
费米子一边则须以$z=\slashed p$为变量，同时使用$p^2=-z^2$。
在$z=-m_o$处，参数分母是$D_f=x^2m_o^2+(1-x)M_o^2$，
对其对数的导数为$2am_o/D_f$。连同分子的导数，给出

<span id="eq:c52-finite-fermion-z"></span>

$$
\begin{aligned}
f_\Psi
&=\frac{g_o^2}{16\pi^2}\int_0^1dx
\left[(1-x)\ln\frac{D_f}{\mu^2}
       +\frac{2x^2(1-x)m_o^2}{D_f}\right],\\
D_f&=x^2m_o^2+(1-x)M_o^2 .
\end{aligned}
\tag{52.22}
$$

这两个有限项正是上一节单位留数条件的结果。
它们的质量比依赖保留在有限参数积分中，而尺度变化只作用于显式的对数。
零外动量顶角的有限部分也已在上一节算出：

<span id="eq:c52-finite-vertex-z"></span>

$$
\begin{aligned}
f_g&=-\frac{g_o^2}{16\pi^2}
       \mathcal L(m_o^2,M_o^2;\mu^2),\\
f_{\delta\lambda}
&=-\frac{3\lambda_o^2}{32\pi^2}\ln\frac{M_o^2}{\mu^2}
  +\frac{3g_o^4}{2\pi^2}\ln\frac{m_o^2}{\mu^2},\\
\mathcal L(A,B;\mu^2)
&=\frac{A\ln(A/\mu^2)-B\ln(B/\mu^2)}{A-B}-1
 \quad(A\ne B),\\
\mathcal L(A,A;\mu^2)&=\ln(A/\mu^2).
\end{aligned}
\tag{52.23}
$$

$\mathcal L$的积分评价与等质量极限见
[上一节的零动量顶角](/posts/srednicki-51/#c51-vertex-subtraction)；
此处用花体字母以区别极点函数$L$。
现在固定$o$参数，每个$\ln(D/\mu^2)$的导数都是$-2$。
由于$\int_0^1a\,dx=1/6$、$\int_0^1(1-x)\,dx=1/2$，
有限项的导数化为

<span id="eq:c52-finite-log-derivatives"></span>

$$
\begin{aligned}
\frac{\partial f_\varphi}{\partial\ln\mu}\bigg|_o
 &=-\frac{4g_o^2}{16\pi^2},&
\frac{\partial f_\Psi}{\partial\ln\mu}\bigg|_o
 &=-\frac{g_o^2}{16\pi^2},\\
\frac{\partial f_g}{\partial\ln\mu}\bigg|_o
 &=\frac{2g_o^2}{16\pi^2},&
\frac{\partial f_{\delta\lambda}}{\partial\ln\mu}\bigg|_o
 &=\frac{3\lambda_o^2-48g_o^4}{16\pi^2}.
\end{aligned}
\tag{52.24}
$$

把这些导数代入有限转换关系，就得到

<span id="eq:c52-finite-running"></span>

$$
\begin{aligned}
\frac1{g_o}\frac{dg_r}{d\ln\mu}
 &=\frac{\partial}{\partial\ln\mu}
   (f_g-\tfrac12f_\varphi-f_\Psi)\bigg|_o
   =\frac{5g_o^2}{16\pi^2},\\
\frac{d\lambda_r}{d\ln\mu}
 &=\frac{\partial}{\partial\ln\mu}
   (f_{\delta\lambda}-2\lambda_o f_\varphi)\bigg|_o
   =\frac{3\lambda_o^2+8\lambda_o g_o^2-48g_o^4}{16\pi^2}
\end{aligned}
\tag{52.25}
$$

到这一圈，把右边的$o$参数换成$r$参数只改变更高阶，
所以结果与极点提取完全一致。
同一个裸理论可以用固定的极点质量和零动量耦合描述，
也可以用随能标变化的最小减除参数描述。
beta函数正是后一组参数为保持同一理论而必须满足的变化律。

<span id="c52-mass-and-fields"></span>

## 质量与场的反常量纲

耦合的尺度导数确定后，同一方法也能用于质量和场。
质量项和动能项各有自己的反项，因此先写出它们与裸量的关系。
上一节的质量系数分别为$Z_m m$和$Z_M M^2$，
再除去场归一化便有

<span id="eq:c52-ex-bare"></span>

$$
m_0=\frac{Z_m}{Z_\Psi}m,\qquad
M_0^2=\frac{Z_M}{Z_\varphi}M^2,\qquad
\Psi_0=Z_\Psi^{1/2}\Psi,\qquad
\varphi_0=Z_\varphi^{1/2}\varphi .
\tag{52.26}
$$

沿[第28节](/posts/srednicki-28/#c28-mass)的定义，
$\gamma_m=d\ln m/d\ln\mu$、$\gamma_M=d\ln M/d\ln\mu$。
场的反常量纲则定义为

<span id="eq:c52-ex-field-definition"></span>

$$
\gamma_\Psi=\frac12\frac{d\ln Z_\Psi}{d\ln\mu},\qquad
\gamma_\varphi=\frac12\frac{d\ln Z_\varphi}{d\ln\mu},\qquad
\frac{d\Psi}{d\ln\mu}=-\gamma_\Psi\Psi,\qquad
\frac{d\varphi}{d\ln\mu}=-\gamma_\varphi\varphi .
\tag{52.27}
$$

后两个等式是固定裸场后对前面的场关系求导得到的，
负号由此确定。这里的$m,M$仍为$\overline{\mathrm{MS}}$参数，
所以它们可以随能标变化。

一圈的有限尺度导数只需让工程项
$B_g=-\varepsilon g/2+\cdots$、
$B_\lambda=-\varepsilon\lambda+\cdots$
作用于简单极点。若$Z_j=1+a_j/\varepsilon+\cdots$，
那么$d\ln Z_j/d\ln\mu$的这一有限项为$-\mathscr Ea_j$，
其中$\mathscr E=(g/2)\partial_g+\lambda\partial_\lambda$。
用前面的$a_\Psi=-g^2/(16\pi^2)$和
$a_\varphi=-g^2/(4\pi^2)$，立刻得到

<span id="eq:c52-ex-field-gammas"></span>

$$
\gamma_\Psi=-\frac12\mathscr Ea_\Psi
 =\frac{g^2}{32\pi^2},\qquad
\gamma_\varphi=-\frac12\mathscr Ea_\varphi
 =\frac{g^2}{8\pi^2}
\qquad\text{（一圈）}.
\tag{52.28}
$$

费米子质量由两个反项之比决定。
上一节给出$a_m=-g^2/(8\pi^2)$，于是
$\ln(Z_m/Z_\Psi)$的简单极点为
$(a_m-a_\Psi)/\varepsilon=-g^2/(16\pi^2\varepsilon)$。
固定$m_0$求导，有

<span id="eq:c52-ex-fermion-mass"></span>

$$
0=\gamma_m-\mathscr E(a_m-a_\Psi)+\text{更高圈},
\qquad
\gamma_m=-\frac{g^2}{16\pi^2}+\text{更高圈}.
\tag{52.29}
$$

这里的$m$有质量维数一；我们求的是有量纲参数本身的对数导数，
因此没有另加工程项$-1$。若改求$m/\mu$的尺度导数，
才得到$-1+\gamma_m$。

标量的情形多出一个质量混合项。根据上一节，
$a_M=\lambda/(16\pi^2)-g^2m^2/(2\pi^2M^2)$。
在裸关系中乘回$M^2$，便得到在$M^2=0$处仍然有限的加性形式：

<span id="eq:c52-ex-scalar-bare-additive"></span>

$$
M_0^2=M^2+
\frac{(\lambda+4g^2)M^2-8g^2m^2}{16\pi^2\varepsilon}
+\text{更高圈}.
\tag{52.30}
$$

其中$4g^2M^2$来自$Z_\varphi^{-1}$，$-8g^2m^2$来自费米泡图的质量反项。
固定裸质量求尺度导数时，$g^2$与$\lambda$的工程导数分别为
$-\varepsilon g^2$与$-\varepsilon\lambda$，
正好消去这一简单极点中的分母。质量参数的尺度导数本身从一圈起始，
它们再作用于反项会进入更高圈，因而不贡献当前的有限项。于是

<span id="eq:c52-ex-scalar-mass"></span>

$$
\begin{aligned}
\beta_{M^2}:=\frac{dM^2}{d\ln\mu}
 &=\frac{(\lambda+4g^2)M^2-8g^2m^2}{16\pi^2}
       +\text{更高圈},\\
\gamma_M
 &=\frac{\lambda+4g^2-8g^2m^2/M^2}{32\pi^2}
       +\text{更高圈}
\qquad(M^2>0).
\end{aligned}
\tag{52.31}
$$

第二式比第一式多除以$2M^2$，因为$\gamma_M$对应的是$M$的对数导数。
在$M^2=0$处应当使用第一式；此时尺度变化仍会由$m^2$生成标量质量项。
把两个质量平方放在一起，结果可写为

<span id="eq:c52-ex-mass-matrix"></span>

$$
\frac{d}{d\ln\mu}
\begin{pmatrix}m^2\\M^2\end{pmatrix}
=\frac1{16\pi^2}
\begin{pmatrix}
-2g^2&0\\
-8g^2&\lambda+4g^2
\end{pmatrix}
\begin{pmatrix}m^2\\M^2\end{pmatrix}
+\text{更高圈}.
\tag{52.32}
$$

每个矩阵元无量纲，右边的质量维数因此仍为二。
在$g=0$时，费米子质量和两种场没有这一圈的变化，
标量质量则满足$\gamma_M=\lambda/(32\pi^2)$，
与实四次理论的结果相同。
反过来，只要费米质量非零，标量质量的运行就不必正比于$M^2$。

这些变化也能从两个方案的有限转换中看出。
令$f_m,f_M$为上一节质量反项的有限部分，由同一裸量相等可得

<span id="eq:c52-ex-finite-matching"></span>

$$
\begin{aligned}
\Psi_r&=(1+\tfrac12f_\Psi)\Psi_o,&
\varphi_r&=(1+\tfrac12f_\varphi)\varphi_o,\\
m_r&=m_o(1+f_m-f_\Psi),&
M_r^2&=M_o^2(1+f_M-f_\varphi)
\qquad\text{（到一圈）}.
\end{aligned}
\tag{52.33}
$$

固定$o$方案的质量与场，第一行的显式对数导数就是
$-\gamma_\Psi$和$-\gamma_\varphi$。质量转换中的两个差值则由上一节
质量壳上的自能有限部分给出。仍用前面的$a=x(1-x)$、
$D_s=m_o^2-aM_o^2$、$D_f=x^2m_o^2+(1-x)M_o^2$，有

<span id="eq:c52-ex-finite-mass-terms"></span>

$$
\begin{aligned}
f_m-f_\Psi
 &=\frac{g_o^2}{16\pi^2}\int_0^1dx\,x\ln\frac{D_f}{\mu^2},\\
M_o^2(f_M-f_\varphi)
 &=-\frac{g_o^2}{4\pi^2}
 \left[m_o^2-\frac{M_o^2}{6}
       -\int_0^1dx\,(m_o^2-3aM_o^2)\ln\frac{D_s}{\mu^2}\right]\\
 &\quad+\frac{\lambda_oM_o^2}{32\pi^2}
       \left(1-\ln\frac{M_o^2}{\mu^2}\right).
\end{aligned}
\tag{52.34}
$$

第一式的$x$来自费米自能分子在$z=-m_o$处变为$xm_o$。
第二式就是标量自能在$k^2=-M_o^2$处的有限值；
求$f_M$时原有的波函数导数项在减去$f_\varphi$后恰好消失。
对两个等式的显式对数求导，利用
$\int_0^1x\,dx=1/2$和$\int_0^1a\,dx=1/6$，得到

<span id="eq:c52-ex-finite-mass-derivative"></span>

$$
\begin{aligned}
\frac{\partial(f_m-f_\Psi)}{\partial\ln\mu}\bigg|_o
 &=-\frac{g_o^2}{16\pi^2},\\
M_o^2\frac{\partial(f_M-f_\varphi)}{\partial\ln\mu}\bigg|_o
 &=-\frac{g_o^2}{2\pi^2}
       \left(m_o^2-\frac{M_o^2}{2}\right)
       +\frac{\lambda_oM_o^2}{16\pi^2}.
\end{aligned}
\tag{52.35}
$$

将它们代入式[（52.33）](#eq:c52-ex-finite-matching)，就恢复了前面求出的
$\gamma_m$和$\beta_{M^2}$。因此，最小减除质量的运行是在重新表示
同一固定极点质量时产生的；有限归一条件与固定裸量的计算给出了同一变化。

---

[← 第 51 节](/posts/srednicki-51/) · [章节地图](/srednicki/) · [第 53 节 →](/posts/srednicki-53/)
