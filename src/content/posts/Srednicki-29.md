---
title: 'Srednicki §29 有效场论'
date: 2026-09-14
category: 笔记
tags: [物理, 量子场论, Srednicki]
series: 'Srednicki QFT'
srednickiSections: [29]
hideFromHome: true
draft: false
---

<span id="c29"></span>

第18节按发散幂次区分了可重整化理论和不可重整化理论。后一类理论需要不断引入新的反项，因而不能用有限个参数描述任意高能的过程。不过，实验总是在有限能量范围内进行的。如果只要求在这个范围内达到一定精度，是否仍须让同一个拉格朗日量一直适用到任意高能？Wilson的思路是先规定一个截止，再把较高动量的自由度积分掉，将它们对低能过程的影响计入新的作用量。沿着这一思路，可重整化项构成低能展开的首批项，不可重整化项则依次给出更高精度的修正。

我们先从已重整化的四维$\varphi^4$理论出发，求出只含低动量模式的作用量，看较高动量的效应怎样进入其中；随后把有限截止下的作用量本身作为输入，研究继续降低截止时各个系数的变化。前一种做法把系数与已知物理参数相联系，后一种做法则用这些系数来描述我们尚未直接探测的高能物理。

<span id="c29-wick"></span>

## 从洛伦兹作用量到欧氏积分

为了具体实行模式积分，先取四维实标量场的拉格朗日量

<span id="eq:c29-minkowski-model"></span>

$$
\mathcal L_{\rm M}
=-\frac12Z_\varphi(\partial\varphi)^2
-\frac12Z_m m_{\rm ph}^2\varphi^2
-\frac{Z_\lambda\lambda_{\rm ph}}{24}\varphi^4.
\tag{29.1}
$$

质量及外腿仍采用极点归一条件，耦合由零外四动量的四点核定义。记欧氏作用量中的正四点系数为$\mathcal V_4^{\rm E}$，相应欧氏图的值为$-\mathcal V_4^{\rm E}$；洛伦兹顶点仍采用前文的$iV_n$记法。因此两种核的关系为

<span id="eq:c29-four-point-convention"></span>

$$
\mathcal V_4^{\rm E}(0,0,0,0)=\lambda_{\rm ph},
\qquad V_4^{\rm M}=-\mathcal V_4^{\rm E}.
\tag{29.2}
$$

这样，洛伦兹树图为$-i\lambda_{\rm ph}$，欧氏树图为$-\lambda_{\rm ph}$，后面匹配耦合时就能沿用同一组号。这里选零四动量是为了简化局部系数的定义；它是离壳归一条件，因为物理质量非零时，四条腿在零四动量处不能同时在壳。

前面已多次对圈动量作Wick旋转，这里要对整个作用量作同样的延拓，使所有模式都在欧氏积分中处理。令$t=-i\tau$，则$dt=-i\,d\tau$、$\partial_t=i\partial_\tau$。把时间导数项先分出来，得到$\mathcal L_{\rm M}=
Z_\varphi(\partial_t\varphi)^2/2-Z_\varphi(\nabla\varphi)^2/2-V$。代入延拓后，时间导数项也带上负号，整个拉格朗日量变为$-\mathcal L_{\rm E}$，于是

<span id="eq:c29-wick-action"></span>

$$
\begin{gathered}
S_{\rm M}=iS_{\rm E},\qquad iS_{\rm M}=-S_{\rm E},\\
\mathcal L_{\rm E}
=\frac12Z_\varphi[(\partial_\tau\varphi)^2+(\nabla\varphi)^2]
+\frac12Z_m m_{\rm ph}^2\varphi^2
+\frac{Z_\lambda\lambda_{\rm ph}}{24}\varphi^4 .
\end{gathered}
\tag{29.3}
$$

围道沿费曼边界条件变形，运算先在有限体积和共同UV调节下进行。欧氏形式的好处在于：当动能系数和最高次偶势的系数为正时，大场构型受到指数抑制，可以把场积分化为收敛的有限模式积分。二次系数可以为负，只要正四次项控制大场方向，有限模式积分仍可收敛；稍后会遇到这种Wilson质量。

外源也必须随时间一起延拓。原来的$i\int dt\,J_{\rm M}\varphi$在旋转后成为$+\int d\tau\,J_{\rm M}(-i\tau)\varphi$，因此，把欧氏源项写在负指数中时，应同时定义

<span id="eq:c29-euclidean-source"></span>

$$
J_{\rm E}(\tau,\mathbf x)=-J_{\rm M}(-i\tau,\mathbf x),\qquad
Z[J_{\rm E}]=\int D\varphi\,e^{-S_{\rm E}-\int J_{\rm E}\varphi}.
\tag{29.4}
$$

按此约定，每次对外源微分会带出一个$-\varphi$，例如

$$
\begin{aligned}
&Z[0]^{-1}\delta^n Z/\delta J_{\rm E}(x_1)\cdots\delta J_{\rm E}(x_n)|_0\\
&\qquad=(-1)^n\langle\varphi(x_1)\cdots\varphi(x_n)\rangle .
\end{aligned}
$$

<span id="c29-blocking"></span>

## 动量模式和Wilson作用量

欧氏作用量已经给定，下一步是把积分变量改为动量模式，以便逐一分开实验能够分辨和不必显式保留的自由度。采用欧氏傅里叶变换

<span id="eq:c29-fourier"></span>

$$
\varphi(x)=\int_k e^{ikx}\widetilde\varphi(k),\qquad
\int_k=\int\frac{d^4k}{(2\pi)^4},\qquad
\widetilde\varphi(-k)=\widetilde\varphi(k)^*.
\tag{29.5}
$$

这里$k^2=\mathbf k^2+k_\tau^2\ge0$。代入二次项时，两个导数先产生$(ik_\mu)(iq_\mu)$，随后$x$积分给出$(2\pi)^4\delta^4(k+q)$，把两动量取为相反数，导数的乘积便成为$k^2$。四次项没有导数，四维坐标积分直接给出四个动量的守恒函数。作用量的动量空间形式因而为

<span id="eq:c29-momentum-action"></span>

$$
\begin{aligned}
S_{\rm E}
={}&\frac12\int_k\widetilde\varphi(-k)
(Z_\varphi k^2+Z_m m_{\rm ph}^2)\widetilde\varphi(k)\\
&+\frac{Z_\lambda\lambda_{\rm ph}}{24}
\int_{k_1}\cdots\int_{k_4}(2\pi)^4
\delta^4\left(\sum_{j=1}^4k_j\right)
\prod_{j=1}^4\widetilde\varphi(k_j).
\end{aligned}
\tag{29.6}
$$

由于场是实的，$k,-k$模式不能当作两个独立复变量积分。在有限周期盒中，可以从每对非零动量中选出一个，用它的实部和虚部作两个实积分坐标，再加上实的零模。傅里叶变换的常数雅可比则吸收到总归一中。这样选择坐标以后，按动量大小分割测度就是普通多重积分的分组。

为使高动量部分也有明确的积分上端，先保留共同调节$\Omega$，并选$m_{\rm ph},E\ll\Lambda<\Omega$。把同一个场分成低模式$\ell=P_{<\Lambda}\varphi$和高模式$h=P_{\Lambda<|k|<\Omega}\varphi$；两个投影各自同时保留$k,-k$，所以两部分仍是实场。低能实验由不含高模式分量的外源描述，在这种外源下，测度与源项的分解给出

<span id="eq:c29-wilson-definition"></span>

$$
\begin{aligned}
Z[J]&=\int D\ell\,Dh\,
e^{-S_{\rm E}[\ell+h]-\int J\ell}
=\int D\ell\,e^{-S_\Lambda[\ell]-\int J\ell},\\
e^{-S_\Lambda[\ell]}&=\int Dh\,e^{-S_{\rm E}[\ell+h]},\qquad
\ell(x)=\int_{|k|<\Lambda}\frac{d^4k}{(2\pi)^4}
e^{ikx}\widetilde\ell(k).
\end{aligned}
\tag{29.7}
$$

这样定义的$S_\Lambda$称为Wilson有效作用量（Wilsonian effective action）。高模式对低能过程的影响已经包含在它的系数中，而低模式仍留在路径积分里；第21节的$\Gamma$则是对全部模式的连通泛函作Legendre变换得到的。这个区别决定了两者的图展开也不同。部分积分还会产生场无关的真空项，它是绝对生成泛函的一部分；若只研究归一化关联函数，可以在各步统一除去$Z[0]$。

图展开可以直接从定义读出。把高模式积分写成高斯平均后，$-\ln\langle e^{-S_{\rm int}[\ell,h]}\rangle_h$选出高模式连通图，其中一般还包括由一条高模式线连接的可约图。四次势就含有这样的例子：它对高场有线性项$j_hh$，其中$j_h=P_h(\lambda\ell^3/6)$。在高模式二次型中配方，得到

<span id="eq:c29-high-source-square"></span>

$$
\frac12hHh+j_hh
=\frac12(h+H^{-1}j_h)H(h+H^{-1}j_h)
-\frac12j_hH^{-1}j_h,
\tag{29.8}
$$

取负对数后，有效作用量中便出现$-\lambda^2\int\ell^3(x)C_h(x-y)\ell^3(y)\,d^4x\,d^4y/72$。这个项用一条高动量线连接两组低模式外腿：即使六条外动量各自都小于$\Lambda$，三个同向外动量的和仍可能大于$\Lambda$，因而能流过这条线。若将范围进一步收窄到全部外动量及相应部分和都远小于$\Lambda$的局部匹配，投影便为零。下面求零动量局部势时，正是利用这个低动量条件，只需保留1PI环图。

<span id="c29-determinant"></span>

## 局部项和高模式行列式

消去的模式虽然不再作为积分变量出现，却能产生原拉格朗日量中没有的相互作用。为了把这些作用整理成低能展开，考察高模式核在外动量零点附近的行为：只要可以作泰勒展开，每个外动量幂就对应一个作用在低场上的导数。局部部分于是写成

<span id="eq:c29-local-expansion"></span>

$$
\mathcal L_\Lambda^{\rm local}
=\frac12Z(\Lambda)(\partial\ell)^2
+\frac12m^2(\Lambda)\ell^2
+\frac{\lambda(\Lambda)}{24}\ell^4
+\sum_{D\ge6,i}c_{D,i}(\Lambda)\mathcal O_{D,i}.
\tag{29.9}
$$

这里按算符质量维数$D$排列各项。四维场的维数为$[\ell]=1$，所以$[c_{D,i}]=4-D$；每个算符还必须在$\ell\mapsto-\ell$下为偶，同一维数的指标$i$用来区分经过分部积分后仍独立的项。含有$2n$个场的算符需带$D-2n$个导数，例如维6可以选$\ell^6$、$\ell^2(\partial\ell)^2$及$(\partial^2\ell)^2$。这里先按分部积分关系选择独立算符，保留运动方程或场重定义可以改变的离壳项。离散对称性则自动继承下来：在式[（29.7）](#eq:c29-wilson-definition)中作$h\mapsto-h$的变量替换，就能看出低模式作用量具有同一对称性。

不过，作局部展开还涉及积分域的选择。严格在每条内部线上实施锐截断，会由积分域边界产生非解析的外动量项，因而式[（29.9）](#eq:c29-local-expansion)只描述局部部分，不能无条件替代完整的$S_\Lambda$。零动量势的系数具有确定的锐壳积分；计算导数项时，则需指定局部投影或平滑截止。[本节补充](#c29-sharp-boundary)将直接算出边界项，以下先求零动量系数。其有限性可以随匹配逐阶建立：保留共同$\Omega$，从已经重整化的低外动量核中减去已知Wilson系数生成的有限低模式图，剩下的新系数在该阶以树项进入，因而由这个有限差确定。这个论证使用红外受控和所选局部投影存在的条件。

求一圈局部势时，把低场暂时看作慢变背景，只需先积分高场的二次部分。四次势中的相应项为$\binom42\lambda\ell^2h^2/24=\lambda\ell^2h^2/4$，所以高场二次算符为

<span id="eq:c29-high-hessian"></span>

$$
H_\ell=P_h\left[-\partial^2+m^2+\frac{\lambda}{2}\ell^2\right]P_h.
\tag{29.10}
$$

先在有限且正定的高模式空间中作高斯积分，就能同时保留行列式和线性源的贡献：

<span id="eq:c29-high-gaussian"></span>

$$
\int dh\,e^{-hH_\ell h/2-j_hh}
=(2\pi)^{N_h/2}(\det H_\ell)^{-1/2}
\exp\left(\frac12j_hH_\ell^{-1}j_h\right).
\tag{29.11}
$$

有效作用量等于这个积分的负对数，因此行列式贡献为$+\tfrac12\operatorname{Tr}\ln H_\ell$，线性源贡献为$-\tfrac12j_hH_\ell^{-1}j_h$。对局部势所需的常背景，$j_h=0$；再减去场无关的行列式，留下的一圈势可以展开为

<span id="eq:c29-determinant-series"></span>

$$
\begin{aligned}
\delta V_h(\ell)
&=\frac12\int_h\frac{d^4k}{(2\pi)^4}
\ln\left[1+\frac{\lambda\ell^2}{2(k^2+m^2)}\right]\\
&=\sum_{n\ge1}
\frac{(-1)^{n+1}\lambda^n}{2^{n+1}n}\,
I_n\,\ell^{2n},\qquad
I_n=\int_h\frac{d^4k}{(2\pi)^4(k^2+m^2)^n}.
\end{aligned}
\tag{29.12}
$$

若把对数展开作为收敛级数使用，背景需满足$|\lambda|\ell^2<2(\Lambda^2+m^2)$。计算局部势系数时，也可以直接逐阶取$\ell=0$处的泰勒系数，而不要求这个展开适用于任意大的背景。高场的三次、四次顶点则从更高圈开始贡献常背景势。

![高模式闭合环连接成对的低模式外腿](/images/srednicki/c29_high_mode_ring.svg)

高模式的环图。实线为低模式，虚线为同一场的高模式。
一般有$n$个四价点、$2n$条外线；省略点表示其余顶点和外腿。

<span id="fig:c29-high-ring"></span>

行列式中的每一项都对应[高模式环图](#fig:c29-high-ring)的一种环图，其组合因子也可以直接数出。对$n\ge3$，每个顶点的两条外腿交换给出$2^n$，环的$n$种旋转和两种反射再给出$2n$，所以带标签的$2n$个外动量共有$(2n)!/(2^n\,2n)$份等价图权重。每个欧氏顶点在最低阶贡献$-\lambda_{\rm ph}$，因为$-Z_\lambda\lambda_{\rm ph}=-\lambda_{\rm ph}+O(\lambda_{\rm ph}^2)$；把环图与局部项匹配时，$c_{2n,1}\ell^{2n}$的顶点为$-(2n)!c_{2n,1}$，因而

<span id="eq:c29-ring-count"></span>

$$
-(2n)!c_{2n,1}
=\frac{(2n)!(-\lambda_{\rm ph})^n}{2^n\,2n}I_n,
\qquad
c_{2n,1}=-\frac{(-\lambda_{\rm ph})^n}{2^n\,2n}I_n.
\tag{29.13}
$$

图的直接计数与行列式展开给出相同的系数。对于$n=1,2$，自环和双边环的对称性有退化，直接从行列式前两项读取更方便：$\delta V_h=\lambda I_1\ell^2/4-\lambda^2I_2\ell^4/16+\cdots$。注意作用量中的二次项带$1/2$，四次项带$1/24$，因此系数的变化分别为

<span id="eq:c29-mass-quartic-factors"></span>

$$
\delta m^2=\frac{\lambda}{2}I_1,\qquad
\delta\lambda=-\frac{3\lambda^2}{2}I_2.
\tag{29.14}
$$

四点耦合和质量的相对号及组合因子现在已经确定；剩下的是用同一个径向测度评价这些壳积分，找出不同局部项对截止的依赖。

<span id="c29-radial-matching"></span>

## 高次势、四点耦合和质量

四维单位三球面的面积为$2\pi^2$，因此球壳积分化为

<span id="eq:c29-radial-measure"></span>

$$
I_n(a,b;m)
=\frac{1}{8\pi^2}\int_a^b\frac{k^3\,dk}{(k^2+m^2)^n}
=\frac{1}{16\pi^2}\int_{a^2}^{b^2}\frac{u\,du}{(u+m^2)^n}.
\tag{29.15}
$$

第二步作了变量替换$u=k^2$，其雅可比给出$k^3dk=u\,du/2$。先算$n=1,2$：在分子中写$u=(u+m^2)-m^2$，就能把各项化为幂函数或对数的积分，结果为

<span id="eq:c29-first-two-integrals"></span>

$$
\begin{aligned}
I_1(a,b;m)
&=\frac{1}{16\pi^2}
\left[b^2-a^2-m^2\ln\frac{b^2+m^2}{a^2+m^2}\right],\\
I_2(a,b;m)
&=\frac{1}{16\pi^2}
\left[\ln\frac{b^2+m^2}{a^2+m^2}
+\frac{m^2}{b^2+m^2}-\frac{m^2}{a^2+m^2}\right].
\end{aligned}
\tag{29.16}
$$

高次项的情形更简单。对$n\ge3$，积分在高端收敛，可以把上端取到无穷；先令$m=0$，径向积分$k^{3-2n}$给出$\Lambda^{4-2n}/(2n-4)$。若保留第一项质量修正，则有

<span id="eq:c29-high-power-integral"></span>

$$
I_n(\Lambda,\infty;m)
=\frac{\Lambda^{4-2n}}{16\pi^2(n-2)}
\left[1-\frac{n(n-2)}{n-1}\frac{m^2}{\Lambda^2}
+O\!\left(\frac{m^4}{\Lambda^4}\right)\right].
\tag{29.17}
$$

这个修正来自固定$n$时的展开$(1+m^2/k^2)^{-n}=1-nm^2/k^2+\cdots$，其中第二项的径向积分为$-nm^2\Lambda^{2-2n}/(2n-2)$。将式[（29.17）](#eq:c29-high-power-integral)代回环图系数，便得到高次局部势的系数：

<span id="eq:c29-high-potential-coefficients"></span>

$$
\begin{gathered}
c_{2n,1}(\Lambda)
=-\frac{(-\lambda_{\rm ph}/2)^n}{32\pi^2n(n-2)}
\Lambda^{4-2n}
\left[1+O\!\left(\frac{m_{\rm ph}^2}{\Lambda^2}\right)\right]
+O(\lambda_{\rm ph}^{n+1}\Lambda^{4-2n}),\\
c_{6,1}=\frac{\lambda_{\rm ph}^3}{768\pi^2\Lambda^2}+\cdots,
\qquad
c_{8,1}=-\frac{\lambda_{\rm ph}^4}{4096\pi^2\Lambda^4}+\cdots .
\end{gathered}
\tag{29.18}
$$

这些系数具有$4-2n$的量纲；六次项为正、八次项为负，依次反映对数级数交替的号。可见即使原拉格朗日量没有高维项，高模式积分也会产生它们，而其截止负幂预示了后面低能展开中的抑制。

四点积分的高端行为不同，它是对数发散的，因而要先通过物理归一条件消去反项，再取$\Omega\to\infty$。将有效四点系数和物理四点系数放在同一个$\Omega$下比较，分别有

<span id="eq:c29-quartic-matching-pair"></span>

$$
\begin{aligned}
-\lambda(\Lambda)
&=-Z_\lambda\lambda_{\rm ph}
+\frac32\lambda_{\rm ph}^2 I_2(\Lambda,\Omega;m_{\rm ph})
+O(\lambda_{\rm ph}^3),\\
-\lambda_{\rm ph}
&=-Z_\lambda\lambda_{\rm ph}
+\frac32\lambda_{\rm ph}^2 I_2(0,\Omega;m_{\rm ph})
+O(\lambda_{\rm ph}^3).
\end{aligned}
\tag{29.19}
$$

两行中的三种外腿配对各有双线泡图的$1/2$，区别只在于积分包含的动量区间：第一行保留高模式的贡献，第二行是全部模式的零动量归一条件。把两行相减，共同反项与共同高端区间同时消失，只留下截止以下的有限积分：

<span id="eq:c29-quartic-finite"></span>

$$
\begin{aligned}
\lambda(\Lambda)
&=\lambda_{\rm ph}+\frac32\lambda_{\rm ph}^2 I_2(0,\Lambda;m_{\rm ph})
+O(\lambda_{\rm ph}^3)\\
&=\lambda_{\rm ph}+\frac{3\lambda_{\rm ph}^2}{32\pi^2}
\left[\ln\left(1+\frac{\Lambda^2}{m_{\rm ph}^2}\right)
+\frac{m_{\rm ph}^2}{\Lambda^2+m_{\rm ph}^2}-1\right]
+O(\lambda_{\rm ph}^3).
\end{aligned}
\tag{29.20}
$$

在$\Lambda\gg m_{\rm ph}$时，方括号展开为$2\ln(\Lambda/m_{\rm ph})-1$，省略的质量修正为$O(\lambda_{\rm ph}^2m_{\rm ph}^2/\Lambda^2)$。把方括号中的2提出后，对数旁的常数成为$-1/2$。它来自积分下端的质量尺度，比较有限重整化方案时应连同对数一起保留。这个固定阶结果还要求$\lambda_{\rm ph}|\ln(\Lambda/m_{\rm ph})|/(16\pi^2)\ll1$；若跨越的尺度区间太大，就要用后面的微分壳方程分步累积这些变化。

同样的匹配方法也适用于二点核。一圈只有蝌蚪图，没有外动量流过圈，所以它只能改变质量项，不能改变动能系数：

<span id="eq:c29-wavefunction-one-loop"></span>

$$
Z(\Lambda)=1+O(\lambda_{\rm ph}^2).
\tag{29.21}
$$

接着比较两种质量条件。这里的蝌蚪图只有一个$1/2$，按与四点核相同的高端调节写为

<span id="eq:c29-mass-matching-pair"></span>

$$
\begin{aligned}
-m^2(\Lambda)
&=-Z_m m_{\rm ph}^2-\frac{\lambda_{\rm ph}}2
I_1(\Lambda,\Omega;m_{\rm ph})+O(\lambda_{\rm ph}^2),\\
-m_{\rm ph}^2
&=-Z_m m_{\rm ph}^2-\frac{\lambda_{\rm ph}}2
I_1(0,\Omega;m_{\rm ph})+O(\lambda_{\rm ph}^2).
\end{aligned}
\tag{29.22}
$$

从第一行减去第二行，共同反项仍然消失；再乘$-1$，便得到低模式作用量中的质量系数：

<span id="eq:c29-mass-finite"></span>

$$
\begin{aligned}
m^2(\Lambda)
&=m_{\rm ph}^2-\frac{\lambda_{\rm ph}}2I_1(0,\Lambda;m_{\rm ph})
+O(\lambda_{\rm ph}^2)\\
&=m_{\rm ph}^2-\frac{\lambda_{\rm ph}}{32\pi^2}
\left[\Lambda^2-m_{\rm ph}^2
\ln\left(1+\frac{\Lambda^2}{m_{\rm ph}^2}\right)\right]
+O(\lambda_{\rm ph}^2).
\end{aligned}
\tag{29.23}
$$

这里的余项表示固定截止比处的更高耦合阶，其质量量纲由相应积分补足。系数$1/(32\pi^2)$由蝌蚪因子$1/2$与径向测度共同给出；常背景行列式的$\ell^2$项给出相同结果。

这个结果还说明，中间作用量的质量系数与最终粒子质量可以有很大差别。若$\Lambda$较高，$m^2(\Lambda)$甚至可以为负；继续对低模式积分时，其蝌蚪图会加回$\lambda_{\rm ph}I_1(0,\Lambda;m_{\rm ph})/2$，恢复正的物理质量。因此真空性质要由低模式的完整作用决定，不能仅由某个中间截止下二次系数的号判断。

<span id="c29-finite-cutoff"></span>

## 从有限截止的作用量出发

到这里，我们把物理质量和耦合当作已知量，求出了Wilson作用量的系数。现在倒转这个问题：先给定$\Lambda_0$及该截止下的全部系数，再用模式积分求较低尺度的理论。令初始动能归一为$Z(\Lambda_0)=1$，并记$m_0^2=m^2(\Lambda_0)$、$\lambda_0=\lambda(\Lambda_0)$。这里下标0标记初始截止，与第28节裸量下标的含义不同；场的动能归一也无需等于极点留数归一，求散射振幅时仍按第27节给各条外腿乘留数平方根。

为了先用微扰论看清这一过程，取弱耦合、小质量和小的高维初值，具体条件为

<span id="eq:c29-initial-assumptions"></span>

$$
|\lambda_0|\ll1,\qquad
|m_0^2|\ll\Lambda_0^2,\qquad
|\widehat c_{D,i}|\ll1,\qquad
\widehat c_{D,i}=c_{D,i}(\Lambda_0)\Lambda_0^{D-4}.
\tag{29.24}
$$

高维系数可以取正号或负号，因此它们的小量条件用绝对值表示。若要把有限模式积分本身定义为实欧氏测度，还需势在大场处有下界。这些条件各有作用：逐个系数很小便于按耦合展开，却不保证无穷算符级数整体收敛；实际EFT计算要另行规定能量展开的精度，只保留该阶所需的有限个独立算符。

将有限截止作用量当作输入，也更贴近有限能量实验的要求。例如，$G_N^{-1/2}$约为$10^{19}\,\mathrm{GeV}$，质子质量约为$1\,\mathrm{GeV}$，两者相差十九个数量级，高能新物理与实验尺度之间可能有巨大的间隔。这两个数只是量级参照，壳积分并不要求把$\Lambda_0$具体选在普朗克尺度。我们可以先问给定截止的理论能作出哪些低能预测，再问它是否允许$\Lambda_0\to\infty$；前一个问题本身就有物理意义。

先暂取初始$c_{D,i}$为零，以便看清四次相互作用单独产生的变化。继续把$\Lambda$到$\Lambda_0$之间的模式积分掉，低模式作用量满足

<span id="eq:c29-shell-composition"></span>

$$
e^{-S_\Lambda[\ell]}
=\int D\varphi_{\Lambda<|k|<\Lambda_0}\,
e^{-S_{\Lambda_0}[\ell+\varphi_{\Lambda<|k|<\Lambda_0}]}.
\tag{29.25}
$$

在有限收敛积分中，这个关系由不同模式的重复积分及次序交换得到；在微扰论中，也可逐个展开系数作同样的分拆。因此一次积掉整个动量壳，与分多次积掉薄壳，得到的是同一个低模式泛函。这使前面的计算可以直接用于两个有限尺度之间：在一圈式[（29.12）](#eq:c29-determinant-series)中换入初始参数，并把积分上下端改为相应截止，便有

<span id="eq:c29-shell-coefficients"></span>

$$
\begin{aligned}
m^2(\Lambda)&=m_0^2+\frac{\lambda_0}{2}I_1(\Lambda,\Lambda_0;m_0)
+O(\lambda_0^2),\\
\lambda(\Lambda)&=\lambda_0-\frac{3\lambda_0^2}{2}
I_2(\Lambda,\Lambda_0;m_0)+O(\lambda_0^3),\\
c_{2n,1}(\Lambda)&=-\frac{(-\lambda_0)^n}{2^n\,2n}
I_n(\Lambda,\Lambda_0;m_0)+O(\lambda_0^{n+1}),\qquad n\ge3 .
\end{aligned}
\tag{29.26}
$$

这里先考察高模式高斯积分的正定条件。即使$m_0^2<0$，只要$\Lambda^2>|m_0^2|$，高斯积分仍有定义。为了从这些有限积分中分离出主要的截止依赖，再取更强的条件$|m_0^2|/\Lambda^2\ll1$，将式[（29.16）](#eq:c29-first-two-integrals)按质量展开，得到

<span id="eq:c29-shell-mass-quartic"></span>

$$
\begin{aligned}
m^2(\Lambda)
={}&m_0^2+\frac{\lambda_0}{32\pi^2}
\left[\Lambda_0^2-\Lambda^2
-m_0^2\ln\frac{\Lambda_0^2}{\Lambda^2}
+O\!\left(\frac{m_0^4}{\Lambda^2}\right)\right]
+O(\lambda_0^2),\\
\lambda(\Lambda)
={}&\lambda_0-\frac{3\lambda_0^2}{16\pi^2}\ln\frac{\Lambda_0}{\Lambda}
+O\!\left(\frac{\lambda_0^2|m_0^2|}{\Lambda^2}\right)
+O(\lambda_0^3).
\end{aligned}
\tag{29.27}
$$

高次势也由同一个壳积分读取；忽略质量后为

<span id="eq:c29-shell-higher"></span>

$$
c_{2n,1}(\Lambda)
=-\frac{(-\lambda_0/2)^n}{32\pi^2n(n-2)}
\left(\Lambda^{4-2n}-\Lambda_0^{4-2n}\right)+\cdots .
\tag{29.28}
$$

取$\Lambda=\Lambda_0$时，三个式子的增量同时消失，回到给定的初始作用量。在有限尺度区间使用这些固定阶结果，还要求$\lambda_0|\ln(\Lambda_0/\Lambda)|/(16\pi^2)\ll1$；跨越更大区间时，后面的RG方程会把分步积累的大对数重新求和。

<span id="c29-mixing-naturalness"></span>

## 高维初值留下什么影响

壳积分揭示了三类系数不同的尺度敏感性。质量项的径向积分含$\int k\,dk$，主要由高端决定；四点项含$\int dk/k$，每个等宽的对数动量区间贡献相同；$\ell^{2n}$项在$n\ge3$时含$\int k^{3-2n}dk$，则主要由低端决定。这三种尺度行为分别称为相关、边缘和无关。“无关”表示其低能效应按幂次减弱，系数仍然可以携带可观测的高能物理信息。

现在把此前暂置为零的高维初值恢复。对于某个$\ell^{2n}$项，初始作用量给出的系数为$\widehat c_{2n,1}\Lambda_0^{4-2n}$，四次耦合在壳中产生的系数则为常数乘$\lambda_0^n\Lambda^{4-2n}$。为了比较在降低截止后保留了多少初始信息，取两者之比，其尺度依赖为

<span id="eq:c29-irrelevant-memory"></span>

$$
\frac{\hbox{初值贡献}}{\hbox{壳生成贡献}}
\ \sim\ \frac{\widehat c_{2n,1}}{\lambda_0^n}
\left(\frac{\Lambda}{\Lambda_0}\right)^{2n-4}.
\tag{29.29}
$$

固定耦合比以后，降低$\Lambda/\Lambda_0$就会压低高维初值的相对贡献。不过，$\widehat c_{2n,1}\ll1$和$\lambda_0\ll1$是独立条件，在有限尺度区间内比较两项大小时，仍须把二者的实际比值与尺度幂次一起考虑。

这个估计比较的是同一高维算符的系数，还没有计入高维项对低维参数的影响。高维顶点的一部分腿可以在高模式中自收缩，使剩下的外腿形成低维顶点；[六价插入图](#fig:c29-phi6-mixing)给出最简单的六次项例子。

![六价插入的两条高模式腿自收缩，留下四条低模式外腿](/images/srednicki/c29_phi6_mixing.svg)

六次项向四次项的混合。一个六价插入中的两条腿在高模式壳内收缩，
留下四条低模式外腿。黑点表示作用量系数$c_{6,1}(\Lambda_0)$，
完整欧氏顶点另含$-6!$。

<span id="fig:c29-phi6-mixing"></span>

记$c_6=c_{6,1}(\Lambda_0)$。将$c_6(\ell+h)^6$展开，留下四条低模式外腿的$\ell^4h^2$项，其系数为$\binom62c_6=15c_6$。对两条高场作一次高斯收缩，代入$\langle h^2\rangle=I_1$，就得到

<span id="eq:c29-six-to-four"></span>

$$
\delta V\big|_{\ell^4}=15c_6 I_1\,\ell^4,\qquad
\delta\lambda=24\cdot15\,c_6I_1
=\frac{360c_6}{16\pi^2}(\Lambda_0^2-\Lambda^2)+\cdots .
\tag{29.30}
$$

最后一式取了忽略质量的径向积分。若只留下两条低模式外腿，则取$\ell^2h^4$项，选取高场的组合因子为$\binom64=15$；四个高场又有三种配对，因而$\langle h^4\rangle=3I_1^2$。相应的势和质量修正为

<span id="eq:c29-six-to-two"></span>

$$
\delta V\big|_{\ell^2}=45c_6 I_1^2\ell^2,\qquad
\delta m^2=90c_6 I_1^2 .
\tag{29.31}
$$

这一质量修正虽有两个圈，却只含一个$c_6$插入。当$c_6=\widehat c_6/\Lambda_0^2$时，四点修正是无量纲的有限匹配量，质量修正则仍可达到$\widehat c_6\Lambda_0^2$量级，并带有两圈的测度因子。更高算符也能通过同样的收缩混入低维项，所以比较两个高能理论的低能预测时，要先用相同的低能实验固定质量和边缘耦合。

例如改变$c_6$后，需相应调整初始$\lambda_0$，才能保持同一个低能四点结果。式[（29.30）](#eq:c29-six-to-four)于是被吸收入这次参数匹配，剩下的六点动量依赖才按能量与$\Lambda_0$的比值减弱。因此，高维项留下按能量比的幂次减弱的低能修正，须以相同低维参数的匹配为前提。若任意指定$\widehat c_6$，其对四次项的有限修正也可能大于$\lambda_0^2\ln(\Lambda_0/\Lambda)$；比较二者的大小时，还须规定高维初值与四次耦合之间的计数关系。

质量对高端的敏感性使轻标量成为一个特别值得注意的例子。在只有弱四次初值的模型中，要让最终物理质量远小于$\Lambda_0$，初始质量就须抵消高端修正的大部分，即

<span id="eq:c29-mass-tuning"></span>

$$
m_0^2+\frac{\lambda_0\Lambda_0^2}{32\pi^2}
\simeq m_{\rm ph}^2+\hbox{较低尺度及更高阶修正}.
\tag{29.32}
$$

这种初值与量子修正之间的抵消称为精细调节（fine tuning）。若没有这种抵消，质量平方的典型大小为$\lambda_0\Lambda_0^2/(32\pi^2)$。加入一般高维初值后，低能匹配所需的临界质量也会移动。还应注意质量变化的方向：对于这里的正$\lambda_0$，式[（29.27）](#eq:c29-shell-mass-quartic)表明，降低截止会使带符号的$m^2(\Lambda)$增加。

技术自然性（technical naturalness）进一步考察这种小参数能否得到对称性的保护：若将它置零会恢复某种对称性，量子修正也可能被迫带上该参数。只有导数相互作用的标量就是一个例子，它可以具有$\varphi\mapsto\varphi+c$的平移对称性；只要测度和调节器也保持此对称性，场积分中的变量替换就使有效作用量满足相同限制。质量项$m^2\varphi^2/2$在平移后会多出$m^2c\varphi+m^2c^2/2$，因此对称性禁止从零独立生成非零质量。当前的$\varphi^4$势破坏了这种平移对称性，仍然面临式[（29.32）](#eq:c29-mass-tuning)中的调节问题。

<span id="c29-running"></span>

## 截止的跑动与场的归一

一次积掉宽壳给出了显式对数，而分步积掉薄壳能把同一变化写成局部的演化方程。在式[（29.27）](#eq:c29-shell-mass-quartic)中固定初始理论，对$\ln\Lambda$微分，先得到$+3\lambda_0^2/(16\pi^2)$；再把当前尺度作为下一薄壳的初始尺度，原来的$\lambda_0$便换为当前的$\lambda$，因而

<span id="eq:c29-cutoff-beta"></span>

$$
\frac{d\lambda}{d\ln\Lambda}
=\frac{3\lambda^2}{16\pi^2}
+O(\lambda^3)+O\!\left(\frac{\lambda^2m^2}{\Lambda^2}\right).
\tag{29.33}
$$

这个系数也能从四维 $\overline{\mathrm{MS}}$ 反项直接读出。在 $d=4-\epsilon$ 中，零动量泡图的积分为

<span id="eq:c29-dimensional-bubble"></span>

$$
\int\frac{d^dk}{(2\pi)^d(k^2+m^2)^2}
=\frac{\Gamma(\epsilon/2)}{(4\pi)^{2-\epsilon/2}}
(m^2)^{-\epsilon/2}
=\frac{2}{16\pi^2\epsilon}+O(1).
$$

三道图各有因子 $1/2$，因而 $Z_\lambda=1+3\lambda/(16\pi^2\epsilon)+O(\lambda^2)$，而一圈 $Z_\varphi=1$。固定裸耦合 $\lambda_B=\widetilde\mu^\epsilon Z_\lambda Z_\varphi^{-2}\lambda$，记 $B_\lambda=-\epsilon\lambda+\beta_\lambda$，则

<span id="eq:c29-msbar-beta-comparison"></span>

$$
0=\epsilon+\frac{B_\lambda}{\lambda}
+\frac{3B_\lambda}{16\pi^2\epsilon}+\cdots,
\qquad
\beta_\lambda=\frac{3\lambda^2}{16\pi^2}+O(\lambda^3).
$$

最后一步取方程的有限部分。与截止方案比较时，先用同一组低能条件匹配质量、耦合和高维初值，再在 $\Lambda\gg |m|$ 的区间提取这个不含质量的系数。

进一步比较高阶跑动时，还要把场的归一计入。为区分原作用量系数与正则动能场的系数，将式[（29.9）](#eq:c29-local-expansion)中的参数暂记为$m_{\rm raw}^2,\lambda_{\rm raw},c_{\rm raw}$，然后定义$\Phi=\sqrt Z\,\ell$。在这个变量下动能恢复标准形式，其余系数变为

<span id="eq:c29-canonical-coefficients"></span>

$$
m_c^2=\frac{m_{\rm raw}^2}{Z},\qquad
\lambda_c=\frac{\lambda_{\rm raw}}{Z^2},\qquad
c_{c,D,i}=\frac{c_{{\rm raw},D,i}}{Z^{n_{D,i}/2}}.
\tag{29.34}
$$

其中$n_{D,i}$表示该算符包含的场数。由于$Z$不随时空位置变化，导数不会改变重标度所需的幂次。若仍用原场书写这些正则参数，相同作用量就写成

<span id="eq:c29-rescaled-lagrangian"></span>

$$
\mathcal L_\Lambda^{\rm local}
=\frac Z2(\partial\ell)^2+\frac{Zm_c^2}{2}\ell^2
+\frac{Z^2\lambda_c}{24}\ell^4
+\sum_{D,i}Z^{n_{D,i}/2}c_{c,D,i}\mathcal O_{D,i}(\ell).
\tag{29.35}
$$

求正则参数的尺度导数时，既要微分原作用量系数，也要微分场归一因子；对四次耦合，链式法则具体给出

<span id="eq:c29-field-running-coupling"></span>

$$
\frac{d\lambda_c}{d\ln\Lambda}
=Z^{-2}\frac{d\lambda_{\rm raw}}{d\ln\Lambda}
-2\lambda_c\frac{d\ln Z}{d\ln\Lambda}.
\tag{29.36}
$$

在实$\varphi^4$理论中，一圈$Z$不变，所以后一项从$\lambda^3$才开始贡献；它不影响式[（29.33）](#eq:c29-cutoff-beta)的一圈结果，却进入下一圈的耦合演化。这里统一的是动能系数，和散射外腿所用极点留数归一的区别仍按第27节处理。

<span id="c29-scheme-change"></span>

## 更换耦合定义时哪些系数不变

设同一单耦合轨道上的两种定义在零耦合附近由解析、可逆且不显含尺度的换元联系：

<span id="eq:c29-scheme-series"></span>

$$
\beta(\lambda)=b_1\lambda^2+b_2\lambda^3+b_3\lambda^4+O(\lambda^5),\qquad
\widetilde\lambda=\lambda+c_2\lambda^2+c_3\lambda^3+O(\lambda^4).
$$

先求逆级数。代入 $\lambda=\widetilde\lambda+a_2\widetilde\lambda^2+a_3\widetilde\lambda^3+\cdots$，二次和三次项分别要求 $a_2+c_2=0$、$a_3+2c_2a_2+c_3=0$，所以

<span id="eq:c29-inverse-coupling-series"></span>

$$
\lambda=\widetilde\lambda-c_2\widetilde\lambda^2
+(2c_2^2-c_3)\widetilde\lambda^3+O(\widetilde\lambda^4).
$$

链式法则给出 $\widetilde\beta=(d\widetilde\lambda/d\lambda)\beta$。相乘后，再用逆级数把右边全部换成新耦合：

<span id="eq:c29-beta-series-conversion"></span>

$$
\begin{aligned}
\widetilde\beta
&=b_1\lambda^2+(b_2+2c_2b_1)\lambda^3
 +(b_3+2c_2b_2+3c_3b_1)\lambda^4+O(\lambda^5),\\
\lambda^2
&=\widetilde\lambda^2-2c_2\widetilde\lambda^3
 +(5c_2^2-2c_3)\widetilde\lambda^4+O(\widetilde\lambda^5),\\
\lambda^3
&=\widetilde\lambda^3-3c_2\widetilde\lambda^4+O(\widetilde\lambda^5).
\end{aligned}
$$

三次项中的 $-2c_2b_1$ 与 $+2c_2b_1$ 抵消，四次项则留下

<span id="eq:c29-scheme-universality"></span>

$$
\widetilde\beta(\widetilde\lambda)
=b_1\widetilde\lambda^2+b_2\widetilde\lambda^3
+\left[b_3-c_2b_2+(c_3-c_2^2)b_1\right]\widetilde\lambda^4
+O(\widetilde\lambda^5).
$$

前两个系数因此相同，第三个一般随耦合定义变化。若换元显含尺度，链式法则中还要加入 $\partial\widetilde\lambda/\partial\ln\Lambda$。

多个耦合的变换由同一个链式法则给出，但此时雅可比是矩阵。记 $\widetilde g^i=g^i+f_2^i(g)+O(g^3)$，$f_2$ 为二次齐次多项式，$\beta=\beta_2+\beta_3+\cdots$ 的下标表示总次数。将 $g=\widetilde g-f_2(\widetilde g)+\cdots$ 代回后，得到

<span id="eq:c29-multicoupling-change"></span>

$$
\widetilde\beta^i(\widetilde g)
=\frac{\partial\widetilde g^i}{\partial g^j}\beta^j(g),
\qquad
\widetilde\beta_2=\beta_2,\qquad
\widetilde\beta_3=\beta_3+(Df_2)\beta_2-(D\beta_2)f_2.
$$

单耦合时最后两项相等，多耦合时则一般留下差值。例如 $\beta_x=x^2,\beta_y=0$，换元 $\widetilde x=x,\widetilde y=y+ax^2$ 给出 $\widetilde\beta_y=2a\widetilde x^3$。所以多个耦合的三次系数应按这个变换律逐项比较。

<span id="c29-predictivity"></span>

## 低能预测与有限模式定义

现在可以回答本节开头的问题。有限截止作用量虽然含有无穷多个允许的局部算符，低能实验达到给定精度却只需其中有限项。设一个质量维数为$D$的算符具有系数$c_D=\widehat c_D/\Lambda_0^{D-4}$，在典型外动量$E$处，提出振幅原有量纲后，其无量纲贡献按

<span id="eq:c29-eft-power-expansion"></span>

$$
\delta\widehat{\mathcal T}_D
\sim\widehat c_D\left(\frac{E}{\Lambda_0}\right)^{D-4}
\tag{29.37}
$$

计数，圈图还带有相应耦合及对数。例如维6算符的首项通常为$E^2/\Lambda_0^2$：若实验精度达到这一阶，就保留所有对称性允许的维6项，用有限组实验确定系数，再按同样的幂次规则估计更高维项的误差。这个比较已通过前面的混合和匹配固定低维质量与耦合，并对局部系数采用一致的调节方案。若保留完整的锐截止泛函，则还需计入后面将算出的边界非局部项。

因此，不可重整化拉格朗日量同样能按能量阶数作出有限精度的预测。低维相互作用若全部消失，领先的低能理论可能就是自由场；若所有传播粒子的质量都高于所考察的能量，展开中便只剩真空项和对外源的局部响应。后一情形虽然没有轻粒子传播，外源仍能通过这些局部项探测高能自由度的效应。

有限截止的作用还不限于微扰计算。把时空离散成格点，可以直接给模型一个有限模式定义：格距$a$使动量落在$|k_\mu|\le\pi/a$的第一布里渊区内。这个区域是盒形的，因此有限系数与本节球形锐壳的结果不同，需要按相应规则匹配。在有限欧氏体积中，取

<span id="eq:c29-lattice-example"></span>

$$
S_a[\widehat\varphi]
=\frac12\sum_{\langle xy\rangle}
(\widehat\varphi_x-\widehat\varphi_y)^2
+\sum_x\left(\frac{\widehat m^2}{2}\widehat\varphi_x^2
+\frac{\widehat\lambda}{24}\widehat\varphi_x^4\right),
\qquad \widehat\lambda>0 .
\tag{29.38}
$$

每个格点只对应一个实积分变量，四次正项压制所有大场方向，因而$\int\prod_xd\widehat\varphi_x\,e^{-S_a}$在有限格点上收敛。关联函数可以直接由这一多重积分定义和计算，无需假定$\widehat\lambda$很小。若要进一步取无穷体积和去截止极限，所需建立的就是这些关联函数的极限及相应的对称、正性条件；有限格点为研究这个问题提供了明确的起点。

<span id="c29-ultraviolet"></span>

## 去掉截止时可能发生什么

有限截止已经足以描述一定范围的实验，去掉截止则提出更强的要求：固定低能物理以后，理论能否沿尺度演化一直延伸到任意高能？先假定选定的单耦合轨道满足精确方程$d\lambda/d\ln\Lambda=\beta(\lambda)$，且沿途$\beta>0$。把耦合与尺度分离积分，得到

<span id="eq:c29-integrated-beta"></span>

$$
\ln\frac{\Lambda_0}{\Lambda_r}
=\int_{\lambda(\Lambda_r)}^{\lambda(\Lambda_0)}
\frac{d\lambda}{\beta(\lambda)}.
\tag{29.39}
$$

左边是两个尺度之间的对数间隔，右边则是走过相应耦合区间所需的RG时间。如果将耦合上限推到无穷后，右边仍然有限，那么固定非零低能耦合的轨道就只能延伸到有限尺度

<span id="eq:c29-landau-integral"></span>

$$
\ln\frac{\Lambda_{\max}}{\Lambda_r}
=\int_{\lambda(\Lambda_r)}^\infty\frac{d\lambda}{\beta(\lambda)}.
\tag{29.40}
$$

因此，关键在于倒数积分的收敛性。例如，当$\beta(\lambda)\sim b\lambda^p$、$b>0,p>1$时，尾积分为$\lambda^{1-p}/[b(p-1)]$，确实给出有限的RG时间。可是$\beta=\lambda\ln\lambda$虽然也增长得比线性快，其倒数积分$\ln\ln\lambda$仍然发散。可见增长快于线性尚不足以保证有限的RG时间，还须判断倒数积分是否收敛。反过来，若$\beta$始终为正且至多线性增长，倒数积分发散，这一种有限RG时间的障碍便不存在。

在一圈近似中取$b=3/(16\pi^2)$，可以把轨道和相应尺度显式写出：

<span id="eq:c29-one-loop-landau"></span>

$$
\frac1{\lambda(\Lambda)}
=\frac1{\lambda(\Lambda_r)}
-\frac{3}{16\pi^2}\ln\frac{\Lambda}{\Lambda_r},
\qquad
\Lambda_{\rm L}^{(1)}
=\Lambda_r\exp\left[\frac{16\pi^2}{3\lambda(\Lambda_r)}\right].
\tag{29.41}
$$

选$\Lambda_r=m_{\rm ph}$，并在树阶令$\lambda(m_{\rm ph})=\lambda_{\rm ph}$，就把指数估计写成物理参数的形式。一圈有限匹配会改变指数中的常数，从而乘上一个有限前因子。这个结果给出了微扰Landau尺度：在接近它的过程中，跑动耦合已经变大，一圈近似的适用条件先行失效，因此还不能由此确定强耦合精确奇点的位置。

如果另外知道精确轨道始终具有式[（29.40）](#eq:c29-landau-integral)给出的有限上界，那么要在同一分支上取$\Lambda_0\to\infty$，就必须使低能耦合趋于零。这样的连续极限称为平庸性（triviality）。一圈图说明了产生这一判断的原因，而严格结论需要控制整个耦合区间，或者直接研究场的缩放极限。

在特定格点构造中，平庸性已经有严格结果。Aizenman 与 Duminil-Copin 证明了四维铁磁最近邻 Ising 及一类 $\varphi^4$ 格点模型的临界缩放极限为高斯场。其 [2021 年论文](https://arxiv.org/pdf/1912.07973v4#page=4)给出了下面的定义与结论。为说明这里“缩放极限”的确切含义，在其有限盒模型中定义

$$
T_{f,L}=\Sigma_L^{-1/2}\sum_x f(x/L)\widehat\varphi_x,\qquad
\Sigma_L=\left\langle\left(\sum_{x\in[-L,L]^4}\widehat\varphi_x\right)^2\right\rangle ,
$$

这里$f$为连续紧支撑函数。缩放极限先取盒尺度$R/L\to\infty$，再令$L\to\infty$，要求任意有限组$T_{f,L}$联合依分布收敛，并允许沿子序列调整格点参数。如果极限的两点Schwinger函数还满足$\lim_{|x-y|\to\infty}S_2(x,y)=0$，所得随机场就是广义高斯过程。这是该文定理 1.2 的结论：高于二阶的截断关联全部消失，而二点函数决定整个极限场。

这个格点构造与本节拉格朗日量之间的转换也可以明确写出。令$\widehat\varphi=a\sqrt Z\,\varphi$，其中$\varphi$为四维有量纲场。展开最近邻梯度项，每个格点贡献$4\widehat\varphi_x^2$，相邻场的乘积项则为$-\widehat\varphi_x\widehat\varphi_y$。将单点权重写为$e^{-\lambda_{\rm p}\widehat\varphi^4+b_{\rm p}\widehat\varphi^2}$，并取最近邻强度为1，对应关系就是

<span id="eq:c29-lattice-conversion"></span>

$$
\lambda_{\rm p}=\frac{\lambda_{\rm raw}}{24Z^2},\qquad
b_{\rm p}=-4-\frac{a^2m_{\rm raw}^2}{2Z}.
\tag{29.42}
$$

正四次势和铁磁最近邻作用因而落在上述构造中；加入任意高维算符以后，则须重新考察是否仍满足定理的假设。[第66节](/posts/srednicki-66/)将计算 QED 的$\beta$函数，它也有微扰Landau尺度。QED含有规范场和费米子，精确连续极限须单独考察。

除耦合趋于无穷以外，$\beta$还可能在有限的$\lambda_*$处出现零点。若从下方接近时有$\beta(\lambda)=a(\lambda_*-\lambda)+O((\lambda-\lambda_*)^2)$，其中$a>0$，令$\delta=\lambda_*-\lambda$，其尺度演化便为

<span id="eq:c29-ultraviolet-fixed-point"></span>

$$
\frac{d\delta}{d\ln\Lambda}=-a\delta+O(\delta^2),
\qquad
\delta(\Lambda)\simeq\delta(\Lambda_r)
\left(\frac{\Lambda}{\Lambda_r}\right)^{-a}.
\tag{29.43}
$$

倒数积分在$\lambda_*$处对数发散，因而需要无穷RG时间才能渐近到达固定点。最后，若$\beta<0$且整条UV轨道趋于零，高能处的相互作用就不断减弱，这就是渐近自由。起点处的负号只给出局部流向，UV终点仍由整条轨道决定。四维渐近自由理论将在第69节引入可重整化规范理论后继续讨论。这里的几种$\beta$行为，已说明截止能否继续提高与什么样的尺度演化有关。

<span id="c29-sharp-boundary"></span>

## 锐截止的边界为何影响导数展开

前面用局部系数组织了低能预测，现在回到局部展开所需的截止条件。完整高模式积分要求每条内部线都留在高模式空间，因此外动量不仅改变传播子的分母，也会改变允许的积分域。以四维泡图为例，令外动量为$q$，暂省写最后才去掉的共同高端$\Omega$，有

<span id="eq:c29-sharp-bubble"></span>

$$
B_h(q)=\int\frac{d^4l}{(2\pi)^4}
\frac{\Theta(|l|-\Lambda)\Theta(|l+q|-\Lambda)}
{(l^2+m^2)((l+q)^2+m^2)}.
\tag{29.44}
$$

当$q=0$时，两个投影重合，便得到前面的$I_2$。要看小$q$引起的变化，写$q=|q|e$、$l=rn$，其中$n^2=e^2=1$。在内球面$r=\Lambda$附近，展开第二条线的动量长度，得到$|l+q|=r+|q|n\cdot e+O(q^2/r)$。若$n\cdot e<0$，第二投影就会从原来的积分域中删去厚度为$-|q|n\cdot e$的一层。薄层厚度已经是一阶量，所以其中的分母只需在$r=\Lambda,q=0$处取值，一阶积分损失为

<span id="eq:c29-boundary-layer"></span>

$$
B_h(q)-B_h(0)
=-\frac{\Lambda^3|q|}{(2\pi)^4(\Lambda^2+m^2)^2}
\int_{n\cdot e<0}d\Omega_3\,(-n\cdot e)+o(|q|).
\tag{29.45}
$$

传播子本身的光滑变化也有一阶项，它正比于$l\cdot q$，在完整球壳上为奇函数，角积分为零。因此边界损失会保留下来。取$e$为极轴，此时$d\Omega_3=4\pi\sin^2\theta\,d\theta$，所需半球积分为$4\pi\int_{\pi/2}^\pi(-\cos\theta)\sin^2\theta\,d\theta=4\pi/3$，代入后得到

<span id="eq:c29-sharp-cusp"></span>

$$
B_h(q)-B_h(0)
=-\frac{\Lambda^3}{12\pi^3(\Lambda^2+m^2)^2}|q|+o(|q|).
\tag{29.46}
$$

共同外边界同样会损失一层区域，符号相同，但其四维系数随$\Omega^{-1}$趋于零。内边界留下的$|q|=\sqrt{q^2}$在零点没有关于$q^2$的泰勒级数。由此可见，零动量势仍能用前面的壳积分准确匹配，而完整锐截止作用量还含有整数次局部导数展开无法表示的边界项。为了定义导数系数，可以改用平滑调节后再作低外动量展开，或明确采用只截一个独立圈动量的局部投影；不同方案的有限系数再由相同的低能条件匹配。

<span id="c29-cubic-shell"></span>

## 六维三次模型中的壳积分

用六维三次模型可以把场的归一化和边界项一起算出。初始作用量的欧氏密度取为

<span id="eq:c29-cubic-initial"></span>

$$
\mathcal L_{\Lambda_0}
=\frac{Z_0}{2}(\partial\varphi)^2
+\frac{Z_0^{3/2}g_0}{6}\varphi^3+\text{线性和质量反项},
\qquad C_0(l)=\frac1{Z_0l^2}.
$$

这里的下标 0 表示初始截止，$g_0$ 是无量纲的欧氏耦合。实三次势向一侧无界，以下在调节好一点函数的驻点附近求微扰系数，并假定整个壳内 $|m^2|\ll\Lambda^2$。与前面的洛伦兹正三次项比较，Wick 旋转给出 $g_{\rm E}=-g_{\rm M}$。

低背景为 $\ell$ 时，高场的二次算符为 $H_\ell=Z_0[-\partial^2+\sqrt{Z_0}g_0\ell]$。展开 $\tfrac12\operatorname{Tr}\ln H_\ell$，二次背景项为

<span id="eq:c29-cubic-quadratic"></span>

$$
\delta S^{(2)}=-\frac{Z_0g_0^2}{4}
\int\frac{d^6q}{(2\pi)^6}\widetilde\ell(q)\widetilde\ell(-q)B(q),
\qquad
B(q)=\int_{\Lambda<|l|<\Lambda_0}\frac{d^6l}{(2\pi)^6l^2(l+q)^2}.
$$

这里明确采用只截独立圈动量 $l$ 的局部投影。在固定积分域内按 $q$ 展开，球面平均给出 $\langle(l\cdot q)^2\rangle=l^2q^2/6$，故

<span id="eq:c29-cubic-bubble-expansion"></span>

$$
\begin{aligned}
\frac1{l^2(l+q)^2}
&=\frac1{l^4}-\frac{2l\cdot q+q^2}{l^6}
 +\frac{4(l\cdot q)^2}{l^8}+O(q^3),\\
\left.\frac{\partial B}{\partial q^2}\right|_0
&=\left(-1+\frac46\right)I_3^{(6)}=-\frac13I_3^{(6)},\\
I_3^{(6)}
&=\frac{\pi^3}{(2\pi)^6}\int_\Lambda^{\Lambda_0}\frac{dr}{r}
=\frac1{(4\pi)^3}\ln\frac{\Lambda_0}{\Lambda}.
\end{aligned}
$$

将二次背景项与 $Zq^2\widetilde\ell(q)\widetilde\ell(-q)/2$ 比较，可读出波函数因子。三次背景项来自对数展开的 $+X^3/3$，零外动量时只需同一个 $I_3^{(6)}$，于是

<span id="eq:c29-cubic-field-vertex"></span>

$$
\frac{Z(\Lambda)}{Z_0}=1+\frac{g_0^2}{6}I_3^{(6)}+O(g_0^4),
\qquad
\delta V^{(3)}=\frac{Z_0^{3/2}g_0^3}{6}I_3^{(6)}\ell^3.
$$

在新尺度把完整三次系数写成 $Z(\Lambda)^{3/2}g(\Lambda)/6$，场因子便给出

<span id="eq:c29-cubic-coupling-running"></span>

$$
\begin{aligned}
g(\Lambda)
&=\left[\frac{Z_0}{Z(\Lambda)}\right]^{3/2}
 g_0\left[1+g_0^2I_3^{(6)}\right]+O(g_0^5)\\
&=g_0\left[1+\left(1-\frac14\right)g_0^2I_3^{(6)}\right]+O(g_0^5),\\
\beta_g&=-\frac{3g^3}{4(4\pi)^3}+O(g^5),\qquad
\beta_\alpha=-\frac32\alpha^2+O(\alpha^3).
\end{aligned}
$$

其中 $-1/4=(-3/2)(1/6)$，最后一行在固定初始量处求 $\ln\Lambda$ 导数，再换成当前耦合。结果与 [第27节](/posts/srednicki-27/#eq:c27-beta-one-loop)相同。$g_{\rm E}=-g_{\rm M}$ 同时改变 $\beta_g$ 的符号，保留上述奇次函数的形式。

若给两条内线都加上锐壳投影，两个球面会各删去一层区域。六维的半球积分为

<span id="eq:c29-six-dimensional-boundary"></span>

$$
\int_{n\cdot e<0}d\Omega_5(-n\cdot e)
=\frac{8\pi^2}{3}\int_{\pi/2}^\pi
 (-\cos\theta)\sin^4\theta\,d\theta=\frac{8\pi^2}{15}.
$$

半径 $r$ 处的径向测度 $r^5$ 除以分母 $r^4$ 留下 $r$，因此内外两层合起来给出

<span id="eq:c29-six-dimensional-cusp"></span>

$$
B_{\rm strict}(q)
=\frac{\Lambda_0^2-\Lambda^2}{128\pi^3}
-\frac{\Lambda+\Lambda_0}{120\pi^4}|q|+o(|q|).
$$

它对 $q^2$ 的导数在零点不存在。上面求 $Z$ 时使用的固定域投影提取局部导数系数，完整逐线锐壳积分则同时保留这个边界项。

---

[← 第 28 节](/posts/srednicki-28/) · [章节地图](/srednicki/) · [第 30 节 →](/posts/srednicki-30/)
