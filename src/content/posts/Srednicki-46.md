---
title: 'Srednicki §46 自旋求和'
date: 2026-09-14
category: 笔记
tags: [物理, 量子场论, Srednicki]
series: 'Srednicki QFT'
srednickiSections: [46]
hideFromHome: true
draft: false
---

<span id="c46"></span>

上一节求出的振幅带有每个外粒子的自旋标签。实验若分别制备并测量这些自旋，所需的概率就由给定标签的振幅模平方决定；若探测器只记录动量，还要对不能分辨的末态自旋求和。逐个代入四分量旋量当然可以完成这些计算，但第38节的旋量外积提供了更直接的办法：先把振幅与共轭振幅相乘，再将首尾相接的旋量指标写成矩阵的迹。我们先处理只有一条费米线的散射，再看两条费米线之间的干涉。

<span id="c46-on-shell"></span>

## 先利用外腿方程

对于$e^-(p)\varphi(k)\to e^-(p')\varphi(k')$，从上一节已求出的振幅出发。省去共同的总动量$\delta$函数与前面的$i$，最低阶振幅为

<span id="eq:c46-electron-amplitude"></span>

$$
\begin{aligned}
\mathcal T
&=g^2\bar u_{\sigma'}(\mathbf p')
\left[
\frac{-\slashed p-\slashed k+m}{m^2-s}
+\frac{-\slashed p+\slashed k'+m}{m^2-u}
\right]u_\sigma(\mathbf p),\\
s&=-(p+k)^2,\qquad u=-(p-k')^2 .
\end{aligned}
\tag{46.1}
$$

这里取实$g$，并沿上一节在稳定外标量的质量区间$0<M<2m$讨论。两个分母均离开内费米质量壳，已经取过费曼边界值。下文保留$g^2$阶振幅，因而求得的模平方为$g^4$阶；它与较高阶振幅的干涉从$g^6$阶开始。自旋标签记为$\sigma,\sigma'=\pm1$，以免与曼德尔斯塔姆变量$s$混淆。

在取迹以前先利用外腿方程，可以减少分子中的动量矩阵。由$(\slashed p+m)u_\sigma(\mathbf p)=0$，分子直接作用于入射旋量时有

<span id="eq:c46-on-shell-reduction"></span>

$$
\begin{aligned}
(-\slashed p-\slashed k+m)u_\sigma
&=(-\slashed k+2m)u_\sigma,\\
(-\slashed p+\slashed k'+m)u_\sigma
&=(\slashed k'+2m)u_\sigma.
\end{aligned}
\tag{46.2}
$$

合并后的两个$m$分别来自原分子的质量项和$-\slashed p$对外腿的作用。这样便把显式的入射动量从两个分子中消去了。将余下的矩阵记为

<span id="eq:c46-matrix-a"></span>

$$
\begin{aligned}
\mathcal T&=\bar u' A u,\\
A&=g^2\left[
\frac{-\slashed k+2m}{m^2-s}
+\frac{\slashed k'+2m}{m^2-u}
\right],\\
u&=u_\sigma(\mathbf p),\qquad u'=u_{\sigma'}(\mathbf p').
\end{aligned}
\tag{46.3}
$$

上述替换依赖于矩阵右端紧接着外旋量：一般矩阵链内部的$-\slashed p$仍须保留。此处$[A]=-1$，两条外旋量各有维数$1/2$，因此$\mathcal T$无量纲，和散射振幅的量纲要求一致。

<span id="c46-conjugate"></span>

## 共轭链与固定自旋的迹

要计算模平方，先取振幅$\mathcal T$这个复数的共轭。利用$\bar u=u^\dagger\beta$、$\beta^\dagger=\beta$和$\beta^2=1$，可以把共轭后的行、列旋量重新写成原来的狄拉克形式。按矩阵乘法的反序规则展开，得到

<span id="eq:c46-dirac-adjoint"></span>

$$
\begin{aligned}
\mathcal T^*
&=(u'^\dagger\beta A u)^\dagger
 =u^\dagger A^\dagger\beta u'\\
&=\bar u\,(\beta A^\dagger\beta)u'
 \equiv\bar u\,\bar A\,u',
\qquad \bar A=\beta A^\dagger\beta .
\end{aligned}
\tag{46.4}
$$

这里的$\bar A$称为矩阵的狄拉克共轭。[第38节](/posts/srednicki-38/#c38-boost)已经得到$\overline{\gamma^\mu}=\gamma^\mu$，所以实四动量满足$\overline{\slashed k}=\slashed k$。式[（46.3）](#eq:c46-matrix-a)的系数在当前运动学区域内为实，从而$\bar A=A$。若仍保留有限的$-i\epsilon$，或者振幅已有吸收部分，共轭还会作用于这些复系数，此时便须保留$\bar A$。以下先用一般的$\bar A$来排列指标，再在需要时代入这一树级简化。

为了把两条旋量链合并，将模平方的指标全部写出：

<span id="eq:c46-fixed-trace"></span>

$$
\begin{aligned}
|\mathcal T|^2
&=\sum_{\alpha,\beta,\gamma,\delta}
 \bar u'_\alpha A_{\alpha\beta}u_\beta
 \bar u_\gamma\bar A_{\gamma\delta}u'_\delta\\
&=\sum_{\delta,\alpha,\beta,\gamma}
 (u'_\delta\bar u'_\alpha) A_{\alpha\beta}
 (u_\beta\bar u_\gamma)\bar A_{\gamma\delta}\\
&=\operatorname{tr}\big[(u'\bar u')A(u\bar u)\bar A\big].
\end{aligned}
\tag{46.5}
$$

从第一行到第二行，只需将最右端的$u'_\delta$移到最左端，使同一外粒子的列旋量与行旋量相邻。外旋量的分量是普通复数，可以交换，因而这一步没有新增的费米负号。相邻指标沿$\delta\to\alpha\to\beta\to\gamma\to\delta$首尾闭合，恰好形成一条迹；矩阵$A$则始终保持在原来的位置。

现在可以代入[第38节的自旋投影](/posts/srednicki-38/#c38-polarization)。固定自旋外积为

<span id="eq:c46-polarized-density"></span>

$$
\begin{aligned}
R_\sigma(p,z)
&\equiv u_\sigma(\mathbf p)\bar u_\sigma(\mathbf p)
 =\frac12(1-\sigma\gamma_5\slashed z)(-\slashed p+m),\\
z^2&=1,\qquad z\cdot p=0 .
\end{aligned}
\tag{46.6}
$$

其中$z$由粒子静止系的量子化轴随动量一起推动而来。末态的量子化轴$z'$可以独立选择，并满足相应的正交条件$z'\cdot p'=0$。将初、末两个外积代入式[（46.5）](#eq:c46-fixed-trace)，得到

<span id="eq:c46-polarized-trace"></span>

$$
\begin{aligned}
|\mathcal T_{\sigma'\sigma}|^2
&=\frac14\operatorname{tr}\!\big[
(1-\sigma'\gamma_5\slashed z')(-\slashed p'+m)
\\[-2pt]
&\hspace{35mm}\times A(1-\sigma\gamma_5\slashed z)(-\slashed p+m)\bar A
\big].
\end{aligned}
\tag{46.7}
$$

这个迹式保留了一般共轭矩阵，可直接用于指定偏振的散射，包括初、末量子化轴不同的情况。前面的$1/4$来自两个自旋投影各自的$1/2$；此时自旋标签仍然固定，还没有对初态作统计平均。

<span id="c46-spin-ensemble"></span>

## 末态求和与初态平均

固定入射自旋以后，出射电子的两个正交自旋态对应两个不同的探测结果。探测器若不分辨这两个结果，其探测投影就是$\sum_{\sigma'}|\sigma'\rangle\langle\sigma'|$，因此要相加的是两个结果的概率：

<span id="eq:c46-final-sum"></span>

$$
\sum_{\sigma'}|\mathcal T_{\sigma'\sigma}|^2.
\tag{46.8}
$$

在迹式中完成这一概率求和，只需把末态外积换成完备关系。具体地，

<span id="eq:c46-unpolarized-completeness"></span>

$$
\begin{aligned}
\sum_{\sigma=\pm1}R_\sigma(p,z)
&=\left[\frac12(1-\gamma_5\slashed z)
      +\frac12(1+\gamma_5\slashed z)\right](-\slashed p+m)
\\
&=-\slashed p+m .
\end{aligned}
\tag{46.9}
$$

求和以后，任意选择的末态量子化轴便从结果中消失了。初态如何处理则取决于入射束的制备：若一半电子处于$\sigma=+1$态，另一半处于$\sigma=-1$态，而且两者之间没有相干性，初态密度矩阵就是$\rho=I_2/2$，对应未极化束。对这样的入射集合，两个初态概率还要取等权平均，用尖括号表示为

<span id="eq:c46-unpolarized-trace"></span>

$$
\begin{aligned}
\big\langle|\mathcal T|^2\big\rangle
&\equiv\frac12\sum_{\sigma,\sigma'}|\mathcal T_{\sigma'\sigma}|^2\\
&=\frac12\operatorname{tr}
\big[(-\slashed p'+m)A(-\slashed p+m)\bar A\big].
\end{aligned}
\tag{46.10}
$$

因此，末态求和不带$1/2$，初态的等权混合才引入$1/2$。也可以直接从式[（46.7）](#eq:c46-polarized-trace)看出这些因子的来历：两次自旋求和分别把两个自旋括号变成$2I_4$，消去原有的$1/4$，再乘上初态平均的$1/2$，便得到同一结果。这种等权平均适用于上述未极化集合；入射自旋未被测量，并不单独确定它的制备权重。

若要保留更一般的制备信息，就用自旋密度矩阵$\rho_{\sigma\tau}$描述入射束，其中$\rho^\dagger=\rho$、$\rho\ge0$、$\operatorname{tr}_2\rho=1$。将量子力学的概率$\operatorname{tr}(\mathcal T\rho\mathcal T^\dagger)$展开为分量，仍可用同样的外积办法写成迹：

<span id="eq:c46-general-density"></span>

$$
\begin{aligned}
P_\rho
&=\sum_{\sigma',\sigma,\tau}
 \mathcal T_{\sigma'\sigma}\rho_{\sigma\tau}
 \mathcal T_{\sigma'\tau}^*,\\
R_\rho(p)
&=\sum_{\sigma,\tau}
 u_\sigma(\mathbf p)\rho_{\sigma\tau}\bar u_\tau(\mathbf p),\\
P_\rho
&=\operatorname{tr}
\big[(-\slashed p'+m)A R_\rho(p)\bar A\big].
\end{aligned}
\tag{46.11}
$$

这里$P_\rho$是提出共同相空间、通量等因子以后的自旋概率权重。当$\rho=I_2/2$时，$R_\rho=(-\slashed p+m)/2$，式子便回到式[（46.10）](#eq:c46-unpolarized-trace)。若$\rho$在所选轴上为$\operatorname{diag}(w_+,w_-)$，两个初态就分别按$w_+,w_-$加权；若入射态是$(|+\rangle+e^{i\alpha}|-\rangle)/\sqrt2$，某一末态$\sigma'$的权重中还会出现$\operatorname{Re}[e^{-i\alpha}\mathcal T_{\sigma'+}\mathcal T_{\sigma'-}^*]$。密度矩阵的非对角元由此保留了相干制备的干涉。

一个简单算例可以具体说明求和与平均的区别。暂取$A=aI_4$和$p=p'=(m,\mathbf0)$，利用静止旋量的归一$\bar u_{\sigma'}(0)u_\sigma(0)=2m\delta_{\sigma'\sigma}$，直接对各自旋态计算可得

<span id="eq:c46-simple-spin-check"></span>

$$
\frac12\sum_{\sigma,\sigma'}|2ma\delta_{\sigma'\sigma}|^2
=4m^2|a|^2.
\tag{46.12}
$$

同一算例也可以从迹式求出：$-\slashed p+m=m(1+\beta)$，再用$\operatorname{tr}\beta=0$和$\beta^2=1$，便有$m^2|a|^2\operatorname{tr}(1+\beta)^2/2
=m^2|a|^2(8)/2$。两种算法给出同一数值，也把旋量归一、末态求和与初态平均的因子分别显现出来。

<span id="c46-two-lines"></span>

## 两条费米线的四项乘积

接着考虑$e^-e^+\to e^-e^+$。这个过程有两条费米线，两个树图的干涉会将它们的自旋指标连在一起。为保留各条线的端点，先定义

<span id="eq:c46-two-channel-amplitude"></span>

$$
\begin{aligned}
D_t&=(\bar u_{1'}u_1)(\bar v_2v_{2'}),&
d_t&=M^2-t,\\
D_s&=(\bar v_2u_1)(\bar u_{1'}v_{2'}),&
d_s&=M^2-s,\\
\mathcal T&=-g^2\left(\frac{D_t}{d_t}-\frac{D_s}{d_s}\right).
\end{aligned}
\tag{46.13}
$$

这里沿用上一节明确的初、末福克次序，公共负号由场重排产生；取模平方时，这个号与共轭幅中的负号相乘而消失。湮灭道的分母为$M^2-s$，由内线携带两入射粒子的总动量确定。以下先在$d_t,d_s$均为非零实数的树级区域内计算。

取共轭时，每个双线性量的两个端点反转。把这一步分别用于两项振幅，得到

<span id="eq:c46-four-products"></span>

$$
\begin{aligned}
D_t^*&=(\bar u_1u_{1'})(\bar v_{2'}v_2),\\
D_s^*&=(\bar u_1v_2)(\bar v_{2'}u_{1'}),\\
|\mathcal T|^2
&=g^4\left[
\frac{D_tD_t^*}{d_t^2}+\frac{D_sD_s^*}{d_s^2}
-\frac{D_tD_s^*}{d_t d_s}
-\frac{D_sD_t^*}{d_s d_t}
\right].
\end{aligned}
\tag{46.14}
$$

前两行分别给出了两项振幅的共轭。模平方展开以后，两个交叉项的负号继承自树图之间的相对号；随后重排普通数值旋量的分量，不会再引入格拉斯曼负号。为了将四项乘积都写成迹，记固定自旋的外积为

<span id="eq:c46-four-outer-products"></span>

$$
R_1=u_1\bar u_1,\quad R_{1'}=u_{1'}\bar u_{1'},\qquad
V_2=v_2\bar v_2,\quad V_{2'}=v_{2'}\bar v_{2'} .
\tag{46.15}
$$

对任意复数旋量列$a,c$和行$\bar b,\bar d$，先把指标相乘再闭合，就有

<span id="eq:c46-rank-one-trace"></span>

$$
\begin{aligned}
\operatorname{tr}[(a\bar b)(c\bar d)]
&=\sum_{\alpha,\beta}a_\alpha\bar b_\beta c_\beta\bar d_\alpha\\
&=(\bar b c)(\bar d a).
\end{aligned}
\tag{46.16}
$$

因此，一对双线性量可以接成一条闭合指标链。将这一关系分别用于两个平方项，得到

<span id="eq:c46-direct-traces"></span>

$$
\begin{aligned}
D_tD_t^*
&=\operatorname{tr}(R_1R_{1'})\,
  \operatorname{tr}(V_{2'}V_2),\\
D_sD_s^*
&=\operatorname{tr}(R_1V_2)\,
  \operatorname{tr}(V_{2'}R_{1'}).
\end{aligned}
\tag{46.17}
$$

在每个平方项中，两条费米线的端点分别配对，形成两条独立的闭链，结果便是两个迹的乘积。干涉项的端点配对则不同；沿第一项原有的双线性量顺序连接，有

<span id="eq:c46-first-interference"></span>

$$
\begin{aligned}
\operatorname{tr}(R_1V_2V_{2'}R_{1'})
&=\operatorname{tr}
(u_1\bar u_1v_2\bar v_2v_{2'}\bar v_{2'}u_{1'}\bar u_{1'})\\
&=(\bar u_1v_2)(\bar v_2v_{2'})
  (\bar v_{2'}u_{1'})(\bar u_{1'}u_1)\\
&=D_tD_s^* .
\end{aligned}
\tag{46.18}
$$

这里中间三个行乘列先给出普通复数，只有首尾的$u_1$和$\bar u_{1'}$留在最后的迹中，余下的迹再给出$\bar u_{1'}u_1$。另一干涉项按其端点连接为

<span id="eq:c46-second-interference"></span>

$$
\begin{aligned}
\operatorname{tr}(R_1R_{1'}V_{2'}V_2)
&=(\bar u_1u_{1'})(\bar u_{1'}v_{2'})
  (\bar v_{2'}v_2)(\bar v_2u_1)\\
&=D_sD_t^* .
\end{aligned}
\tag{46.19}
$$

将两个平方项和两种干涉次序合在一起，得到

<span id="eq:c46-four-traces"></span>

$$
\begin{aligned}
|\mathcal T|^2=g^4\bigg[&
\frac{\operatorname{tr}(R_1R_{1'})
      \operatorname{tr}(V_{2'}V_2)}{d_t^2}
+\frac{\operatorname{tr}(R_1V_2)
      \operatorname{tr}(V_{2'}R_{1'})}{d_s^2}\\
&-\frac{\operatorname{tr}(R_1V_2V_{2'}R_{1'})}{d_t d_s}
-\frac{\operatorname{tr}(R_1R_{1'}V_{2'}V_2)}{d_s d_t}
\bigg].
\end{aligned}
\tag{46.20}
$$

可见，干涉将四条外旋量连成了一条闭合指标链。这条链来自振幅与共轭振幅的相乘，其中没有上一节闭费米圈图的传播子，因此也没有那种闭圈所带的额外负号。

两种干涉次序应当一起保留，因为它们互为复共轭，单独一项一般可以是复数。利用$\bar R_i=R_i$、$\bar V_j=V_j$以及$[\operatorname{tr}X]^*=\operatorname{tr}(\bar X)$，先将矩阵乘积反序，再循环移动一次，就得到

<span id="eq:c46-interference-conjugate"></span>

$$
\begin{aligned}
\big[\operatorname{tr}(R_1V_2V_{2'}R_{1'})\big]^*
&=\operatorname{tr}(R_{1'}V_{2'}V_2R_1)\\
&=\operatorname{tr}(R_1R_{1'}V_{2'}V_2).
\end{aligned}
\tag{46.21}
$$

两项之和于是成为$2\operatorname{Re}\operatorname{tr}(R_1V_2V_{2'}R_{1'})$，保证模平方为实。这里用的是$\operatorname{tr}(XY)=\operatorname{tr}(YX)$所允许的循环移动，这个等式并不允许任意交换链内的两个矩阵。

<span id="c46-four-spin-sum"></span>

## 双初态的平均

若电子束和正电子束分别未极化，而且两束的自旋统计独立，初态密度矩阵就是$(I_2/2)\otimes(I_2/2)=I_4/4$。因此，对四种初态组合取等权平均，并对两个末粒子的自旋分别求和，得到

<span id="eq:c46-two-initial-average"></span>

$$
\big\langle|\mathcal T|^2\big\rangle
=\frac14\sum_{\sigma_1,\sigma_2,\sigma'_1,\sigma'_2}
|\mathcal T|^2 .
\tag{46.22}
$$

每一项中，四个外积各出现一次，因而四个自旋求和可以分别作用于相应的外积。将反粒子完备和与电子的完备和并列，有

<span id="eq:c46-particle-antiparticle-sums"></span>

$$
U_i\equiv\sum_{\sigma_i}u_i\bar u_i=-\slashed p_i+m,
\qquad
W_j\equiv\sum_{\sigma_j}v_j\bar v_j=-\slashed p_j-m .
\tag{46.23}
$$

反粒子完备和中的负质量项来自第38节的$v$支归一$\bar v_\sigma v_\tau=-2m\delta_{\sigma\tau}$。将这两种完备和代入式[（46.20）](#eq:c46-four-traces)，未极化的结果便为

<span id="eq:c46-averaged-four-traces"></span>

$$
\begin{aligned}
\big\langle|\mathcal T|^2\big\rangle
=\frac{g^4}{4}\bigg[&
\frac{\operatorname{tr}(U_1U_{1'})
      \operatorname{tr}(W_{2'}W_2)}{d_t^2}
+\frac{\operatorname{tr}(U_1W_2)
      \operatorname{tr}(W_{2'}U_{1'})}{d_s^2}\\
&-\frac{\operatorname{tr}(U_1W_2W_{2'}U_{1'})}{d_t d_s}
-\frac{\operatorname{tr}(U_1U_{1'}W_{2'}W_2)}{d_s d_t}
\bigg].
\end{aligned}
\tag{46.24}
$$

至此，自旋标签全部消去，剩下的只是由外动量构成的矩阵迹。每个$U$或$W$至多含一个gamma矩阵，所以单个迹中最多出现四个gamma。[下一节](/posts/srednicki-47/#c47)将建立这套迹运算，[第48节](/posts/srednicki-48/#c48)再将结果用于截面。式[（46.24）](#eq:c46-averaged-four-traces)已经保留各道的分母、两个平方项和两种干涉次序，只须继续计算这些矩阵的迹。

<span id="c46-checks"></span>

## 阈值与一般运动学的例子

在建立一般的gamma迹算法以前，静止旋量已经足以算出两个阈值例。它们既能显示两道相加的作用，也能给出自旋求和后的阈值行为。电子与标量的质心三动量趋于零时，$p=p'=(m,\mathbf0)$、$k=k'=(M,\mathbf0)$，从而$s=(m+M)^2$、$u=(m-M)^2$。式[（46.3）](#eq:c46-matrix-a)化为

<span id="eq:c46-electron-threshold"></span>

$$
\begin{aligned}
A_{\rm th}
&=g^2\left[
-\frac{M\beta+2m}{M(2m+M)}
+\frac{-M\beta+2m}{M(2m-M)}
\right]\\
&=\frac{4mg^2}{4m^2-M^2}(1-\beta).
\end{aligned}
\tag{46.25}
$$

两项中$I_4$的系数相加，得到$2m[-(2m+M)^{-1}+(2m-M)^{-1}]/M
=4m/(4m^2-M^2)$；而$\beta$的系数为$-(2m+M)^{-1}-(2m-M)^{-1}=-4m/(4m^2-M^2)$。再用静止旋量满足的$\beta u_\sigma(0)=u_\sigma(0)$，就看出每个自旋振幅在该阈值极限都为零。这是两个标量接法相消的结果，因此自旋求和或平均以后仍然为零。

对于电子正电子散射的阈值，四个外动量均趋于$(m,\mathbf0)$，于是$t=u=0$、$s=4m^2$。取$M>0$并离开$M^2=4m^2$时，可以直接用静止旋量计算：正、负频率旋量在狄拉克双线性下正交，故$\bar v_2u_1=\bar u_{1'}v_{2'}=0$，湮灭项消失；直接项则由$\bar u_{1'}u_1=2m\delta_{\sigma'_1\sigma_1}$和$\bar v_2v_{2'}=-2m\delta_{\sigma_2\sigma'_2}$给出

<span id="eq:c46-pair-threshold"></span>

$$
\begin{aligned}
\mathcal T_{\rm th}
&=\frac{4g^2m^2}{M^2}
\delta_{\sigma'_1\sigma_1}\delta_{\sigma'_2\sigma_2},\\
\big\langle|\mathcal T_{\rm th}|^2\big\rangle
&=\frac14(2\cdot2)\frac{16g^4m^4}{M^4}
=\frac{16g^4m^4}{M^4}.
\end{aligned}
\tag{46.26}
$$

这两个结果给出树幅的阈值极限。若还要求通量同时趋零时的截面，就要把相空间因子一并纳入极限。

对于一般运动学点，也可以构造第38节的四分量旋量，显式枚举第一个过程的四组自旋和第二个过程的十六组自旋，逐项与上述有序迹比较。例如，以$m=1$为质量单位，取$g=0.7$、$M=0.6$，质心三动量大小为$0.8$，末动量极角为$1.1$、方位角为$0.73$弧度，得到

| 过程                       | 显式自旋幅求和并平均 |              有序迹 |
| -------------------------- | -------------------: | ------------------: |
| $e^-\varphi\to e^-\varphi$ |  $0.592805617779635$ | $0.592805617779635$ |
| $e^-e^+\to e^-e^+$         |   $4.66112818004263$ |  $4.66112818004263$ |

上表对第二个过程的四条外腿分别选了不同的自旋基。这样的基变换会改变单个极化振幅，个别干涉迹还会带有虚部；两种次序按式[（46.21）](#eq:c46-interference-conjugate)互为共轭，完成所有自旋的求和与平均以后，结果保持不变。

要将这些结果整理成动量不变量的函数，还需算出各个gamma矩阵的迹。下一节便建立这套运算方法。

---

[← 第 45 节](/posts/srednicki-45/) · [章节地图](/srednicki/) · [第 47 节 →](/posts/srednicki-47/)
