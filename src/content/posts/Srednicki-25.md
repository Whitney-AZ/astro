---
title: 'Srednicki §25 不稳定粒子与共振'
date: 2026-09-14
category: 笔记
tags: [物理, 量子场论, Srednicki]
series: 'Srednicki QFT'
srednickiSections: [25]
hideFromHome: true
draft: false
---

<span id="c25"></span>

前面用传播子的实极点确定粒子质量，再用极点留数归一化场，使它能产生精确的渐近单粒子态。若粒子的质量足以使它衰变成更轻的粒子，这个描述就需要改变：衰变使初始粒子的存活概率随时间减小，自能在质量壳上也将出现与此相应的虚部。本节先沿第11节的方法计算树级衰变率，再从重场的自能中求出同一个数，最后把重粒子放到散射图的内线上，说明它的质量和寿命怎样表现为稳定粒子散射中的共振。以下用$M$、$m$分别表示重场$\varphi$与轻场$\chi$的质量。

<span id="c25-phase-space"></span>

## 两体衰变的六维相空间

先考虑两个实标量场的拉格朗日量：

<span id="eq:c25-model"></span>

$$
\begin{aligned}
\mathcal L={}&-\frac12(\partial\varphi)^2-\frac12M^2\varphi^2
-\frac12(\partial\chi)^2-\frac12m^2\chi^2\\
&+\frac g2\varphi\chi^2+\frac h6\varphi^3+\mathcal L_{\rm ct}.
\end{aligned}
\tag{25.1}
$$

这里仍取六维时空。动能项给出$[\varphi]=[\chi]=2$，因此$g,h$均无量纲，模型中的三价相互作用属于第12、18节讨论的可重整化相互作用。取$M>2m>0$，重粒子的静止能便足以产生两个轻粒子。相互作用前的$1/2$与两份$\chi$的收缩数$2!$相消，所以该顶点的费曼规则是$ig$，图25a给出的树级振幅为

<span id="eq:c25-tree-decay"></span>

$$
\mathcal T^{(0)}_{\varphi\to\chi\chi}=g,\qquad
k=k'_1+k'_2,\qquad k^2=-M^2,\quad (k'_i)^2=-m^2.
\tag{25.2}
$$

图中按衰变过程画出一条入射线和两条出射线，箭头表示物理动量。若写成前面完整顶角所用的全入记号，三个宗量就是$(k,-k'_1,-k'_2)$。

![一条重场虚线通过三价顶点衰变成两条轻场实线](/images/srednicki/c25_decay.svg)

重粒子的树级衰变。虚线表示$\varphi$，实线表示$\chi$。
同一顶点的因子为$ig$；两个相同末态的计数因子在相空间积分中处理。

<span id="fig:c25-decay"></span>

有了树级振幅，就可以在领先弱耦合近似下代入第11节的衰变公式。两份末态虽然在积分中各有一个动量标签，物理上却是相同粒子；若积分遍及两个标签的全部动量空间，必须除去交换标签造成的重复计数。因此物理微分率写为

<span id="eq:c25-decay-measure"></span>

$$
d\Gamma
=\frac{1}{2!}\frac{|\mathcal T|^2}{2M}\,d\mathrm{LIPS}_2,
\qquad
d\mathrm{LIPS}_2
=(2\pi)^6\delta^6(k-k'_1-k'_2)\,d\widetilde k'_1d\widetilde k'_2.
\tag{25.3}
$$

这个$1/2!$也可以留到全角积分后再乘，但在整个计算中只应计入一次。为完成相空间积分，先把六维单粒子测度写成两种等价形式：

<span id="eq:c25-shell-measure"></span>

$$
d\widetilde k
=\frac{d^5\mathbf k}{(2\pi)^5\,2\omega_{\mathbf k}}
=\frac{d^6k}{(2\pi)^6}\,
2\pi\delta(k^2+m^2)\theta(k^0),
\qquad \omega_{\mathbf k}=\sqrt{\mathbf k^2+m^2}.
\tag{25.4}
$$

要从第二种写法恢复第一种，只需先积分能量。质量壳delta函数的宗量有两个根，按各根处导数的绝对值展开，得到

<span id="eq:c25-shell-jacobian"></span>

$$
\delta\bigl(\omega_{\mathbf k}^2-(k^0)^2\bigr)
=\frac{\delta(k^0-\omega_{\mathbf k})+\delta(k^0+\omega_{\mathbf k})}
{2\omega_{\mathbf k}}.
\tag{25.5}
$$

其中$\theta(k^0)$选出正能量根，余下的$2\pi$正好把六维傅里叶测度变成五维测度。这个写法在后面把自能虚部化为相空间时还会用到。

现在选初始粒子的静止系$k=(M,\mathbf0)$。动量守恒的空间delta函数令$\mathbf k'_2=-\mathbf k'_1=-\mathbf p$，两份末态能量随之相等。先用这五个delta函数消去一个动量积分，再把剩余积分写成球坐标，便有

<span id="eq:c25-radial-lips"></span>

$$
d\mathrm{LIPS}_2
=\frac{p^4\,dp\,d\Omega}{(2\pi)^4\,4\omega_p^2}
\delta(M-2\omega_p).
\tag{25.6}
$$

这里的$p^4$来自五维动量空间的径向测度。剩下的能量delta函数把径向动量固定在唯一的正根上；求出这个根，同时计算其宗量对径向动量的导数：

<span id="eq:c25-radial-root"></span>

$$
p_*=\frac12\sqrt{M^2-4m^2},\qquad
\omega_*=\frac M2,\qquad
\delta(M-2\omega_p)=\frac{\omega_*}{2p_*}\delta(p-p_*).
\tag{25.7}
$$

在径向积分中，除把$p$取为$p_*$外，还须乘以上式最后给出的逆导数因子。于是

<span id="eq:c25-angular-lips"></span>

$$
\int_0^\infty\frac{p^4dp}{4\omega_p^2}\delta(M-2\omega_p)
=\frac{p_*^3}{8\omega_*}
=\frac{p_*^3}{4M},
\qquad
d\mathrm{LIPS}_2=\frac{p_*^3\,d\Omega}{4(2\pi)^4M}.
\tag{25.8}
$$

径向积分完成后，余下的被积函数与方向无关。由[第14节高斯积分求出的球面面积](/posts/srednicki-14/#eq:c14-gaussian-sphere)，五维动量空间的全角面积为

<span id="eq:c25-solid-angle"></span>

$$
\Omega_5=\frac{2\pi^{5/2}}{\Gamma(5/2)}
=\frac{8\pi^2}{3}.
\tag{25.9}
$$

将径向结果、全角面积和树级振幅一起代回式[（25.3）](#eq:c25-decay-measure)，便得到总衰变宽度：

<span id="eq:c25-width"></span>

$$
\begin{aligned}
\Gamma_0
&=\frac{g^2}{4M}\,
\frac{p_*^3}{4(2\pi)^4M}\,\frac{8\pi^2}{3}
=\frac{g^2p_*^3}{96\pi^2M^2}\\
&=\frac{g^2M}{768\pi^2}
\left(1-\frac{4m^2}{M^2}\right)^{3/2}
=\frac{\pi\alpha M}{12}\,\beta^3,\\
\alpha&=\frac{g^2}{(4\pi)^3},\qquad
\beta=\sqrt{1-\frac{4m^2}{M^2}}.
\end{aligned}
\tag{25.10}
$$

下标0表示这里只保留领先的弱耦合结果。$\Gamma_0$有质量维数1，因而可以与寿命的倒数联系起来。这个结果也显示了阈值附近的相空间压低：径向体积$p^4dp$与能量delta函数带来的$1/p$合成$p^3$，使宽度按$\beta^3$趋于零。若轻粒子质量趋于零，则有$\Gamma_0/M=\pi\alpha/12$；在弱耦合下，宽度仍远小于重粒子质量。

<span id="c25-self-energy"></span>

## 自能的实部减除与吸收部

重场 $\varphi$ 的激发会衰变成轻粒子，寿命有限；稳定 $\chi$ 粒子仍可作为 LSZ 的渐近外态。以下从重场二点函数求出复极点，再把它放入 $\chi\chi$ 散射，确定式[（25.10）](#eq:c25-width)与共振寿命的关系。

取$|h|\ll|g|$，一圈近似中便可先保留双$\chi$内线，略去正比于$h^2$的重场圈。图25b中交换两条内部$\chi$不改变图，故其对称因子为2。沿用第14节的记号，把截腿图记为$i\Pi$，逐次插入自能后得到完整传播子

<span id="eq:c25-dyson"></span>

$$
\boldsymbol\Delta_\varphi(z)
=\frac1{z+M^2-\Pi(z)},\qquad z=k^2,
\tag{25.11}
$$

这里的物理边界值仍按费曼处方取得，自能的号也与前面各节相同。

![两条轻场内线组成的重场单圈自能图](/images/srednicki/c25_self_energy.svg)

重场的双$\chi$自能圈。两条内部动量均从左流向右，
满足$\ell_1+\ell_2=k$。截去虚线外传播子后，整图为$i\Pi$；
交换两条$\chi$内线给出对称因子2。

<span id="fig:c25-self-energy"></span>

第14节已经求出了六维圈积分，并完成了正则化和紫外局部项的分离。现在圈内粒子的质量变为$m$，外场质量变为$M$，其余参数积分步骤保持原来的形式。为施加适合不稳定粒子的减除条件，先定义

<span id="eq:c25-finite-unsubtracted"></span>

$$
\begin{gathered}
a=x(1-x),\qquad D(z,x)=m^2+az-i0,\qquad D_0(x)=m^2-aM^2,\\
F(z)=\frac\alpha2\int_0^1dx\,D(z,x)\ln\frac{D(z,x)}{\mu_R^2},
\qquad
\Pi(z)=F(z)-A'z-B'M^2.
\end{gathered}
\tag{25.12}
$$

其中$A',B'$是吸收发散后仍可选择的有限反项。参照尺度$\mu_R$使对数的宗量无量纲，随后在减除中消去。由于拉格朗日量为实，$A',B'$也必须为实数。一旦$D$在部分参数区间为负，$F$就有虚部，实反项因而无法施加稳定粒子所用的两个复条件$\Pi(-M^2)=\Pi'(-M^2)=0$。现在把质量和场归一化固定在实部上，取

<span id="eq:c25-real-os"></span>

$$
\operatorname{Re}\Pi(-M^2)=0,\qquad
\operatorname{Re}\Pi'(-M^2)=0.
\tag{25.13}
$$

第二个条件先确定线性反项$A'$，再把它代入第一个条件求出常数反项$B'$，有

<span id="eq:c25-finite-counterterms"></span>

$$
A'=\operatorname{Re}F'(-M^2),\qquad
B'=\frac{\operatorname{Re}F(-M^2)}{M^2}
+\operatorname{Re}F'(-M^2).
\tag{25.14}
$$

把这两个系数放回自能，可将减除写成一个直观的形式：从未减除函数中扣去在壳点处的实部及其实部的斜率，得到

<span id="eq:c25-real-taylor-subtraction"></span>

$$
\Pi(z)=F(z)-\operatorname{Re}F(-M^2)
-(z+M^2)\operatorname{Re}F'(-M^2).
\tag{25.15}
$$

为了继续完成参数积分，先将这里用到的两个实部展开：

<span id="eq:c25-real-subtraction-integrands"></span>

$$
\begin{aligned}
\operatorname{Re}F(-M^2)
&=\frac\alpha2\int_0^1dx\,D_0\ln\frac{|D_0|}{\mu_R^2},\\
\operatorname{Re}F'(-M^2)
&=\frac\alpha2\int_0^1dx\,a
\left(\ln\frac{|D_0|}{\mu_R^2}+1\right).
\end{aligned}
\tag{25.16}
$$

虽然$D_0$在两个内部点为零，这些点附近只出现$\ln|x-x_\pm|$型奇性，参数积分仍收敛。接着利用$D_0+a(z+M^2)=m^2+az$合并对数的系数，再用$\int_0^1a\,dx=1/6$完成不含对数的部分，式[（25.15）](#eq:c25-real-taylor-subtraction)便成为

<span id="eq:c25-subtracted-self-energy"></span>

$$
\Pi(z)=\frac\alpha2\int_0^1dx\,
D(z,x)\ln\frac{D(z,x)}{|D_0(x)|}
-\frac{\alpha}{12}(z+M^2).
\tag{25.17}
$$

式中的$i0$按同一个边界极限处理，参照尺度已在减除中相消。分母的绝对值来自减除点处的实部；分子的复对数则继续保留费曼处方，其虚部正是我们要求的吸收部。

令$z=-s-i0$、$s>4m^2$，考察物理类时区域。此时实分母$m^2-sx(1-x)$会在一段参数区间内变成负数，这一区间的端点由二次方程确定：

<span id="eq:c25-threshold-roots"></span>

$$
x_\pm=\frac12(1\pm\beta_s),\qquad
\beta_s=\sqrt{1-\frac{4m^2}{s}},\qquad x_-<x<x_+.
\tag{25.18}
$$

在两个根之间，费曼处方给出$\ln(D)=\ln|D|-i\pi$，所以对数的虚部为$-\pi$。

由于反项为实，吸收部完全来自这段负分母区间。代入对数的虚部后，需要计算的积分就是

<span id="eq:c25-absorptive-integral"></span>

$$
\operatorname{Im}\Pi(-s-i0)
=-\frac{\pi\alpha}{2}\int_{x_-}^{x_+}dx\,[m^2-sx(1-x)].
\tag{25.19}
$$

为把区间化成关于原点对称的形式，置$u=2x-1$。这时$dx=du/2$，积分限变为对称的$\pm\beta_s$，括号内的二次式则变为$s(u^2-\beta_s^2)/4$。于是积分可逐项完成：

<span id="eq:c25-threshold-evaluation"></span>

$$
\int_{x_-}^{x_+}dx\,[m^2-sx(1-x)]
=\frac s8\left(\frac{2\beta_s^3}{3}-2\beta_s^3\right)
=-\frac{s\beta_s^3}{6}.
\tag{25.20}
$$

将这个参数积分代回吸收部，并在重粒子质量壳上取值，得到

<span id="eq:c25-absorption-width"></span>

$$
\begin{gathered}
\operatorname{Im}\Pi(-s-i0)
=\frac{\pi\alpha s}{12}
\left(1-\frac{4m^2}{s}\right)^{3/2}\theta(s-4m^2),
\\
I:=\operatorname{Im}\Pi(-M^2-i0)=M\Gamma_0.
\end{gathered}
\tag{25.21}
$$

吸收部之所以为正，是因为负分母乘上了对数的负虚部。按式[（25.11）](#eq:c25-dyson)中自能前的负号，正的$I$将使正能量极点移向下半平面，正好对应随时间衰减的振幅。

为了进一步求极点位置，还需要自能在质量壳附近的斜率。先对$s\beta_s^3$求导：

$$
\frac{d}{ds}(s\beta_s^3)
=\beta_s^3+\frac{6m^2}{s}\beta_s
=\beta_s\left(1+\frac{2m^2}{s}\right).
$$

再用$d/dz=-d/ds$转回自能的宗量，并结合实部的在壳减除条件，就有

<span id="eq:c25-imaginary-derivative"></span>

$$
\Pi'(-M^2-i0)
=-\frac{i\pi\alpha}{12}\,
\beta\left(1+\frac{2m^2}{M^2}\right).
\tag{25.22}
$$

因此在壳点的完整导数仍含有虚部。对于不稳定粒子，实部归一化并不使复极点的留数自动等于1；求更高阶的极点位置和宽度时，这个斜率也要保留下来。

<span id="c25-cut"></span>

## 从双切线直接得到相空间

前面分别计算了衰变相空间和圈图，发现两者由自能虚部联系起来。下面直接处理圈图，看看两条虚内线怎样给出真实末态的相空间。为同时保留两个能量方向的信息，暂不消去第二条内线动量，记

<span id="eq:c25-two-loop-variables"></span>

$$
\int_k:=\int\frac{d^6\ell_1}{(2\pi)^6}
\frac{d^6\ell_2}{(2\pi)^6}(2\pi)^6
\delta^6(\ell_1+\ell_2-k),\qquad
X_i=\ell_i^2+m^2.
\tag{25.23}
$$

把两顶点、两传播子以及对称因子放在一起，系数为$(ig)^2(1/i)^2/2=g^2/2$。按截腿图的定义，这给出$i\Pi_{\rm loop}=(g^2/2)\int_k[(X_1-i0)(X_2-i0)]^{-1}$；除去图前的虚数单位后，自能写成

<span id="eq:c25-original-loop"></span>

$$
\Pi(k^2)=-\frac{ig^2}{2}
\int_k\frac1{X_1-i0}\frac1{X_2-i0}
-Ak^2-BM^2.
\tag{25.24}
$$

这里$A,B$包含实的紫外减除，对吸收部没有贡献。因此关键在于费曼分母的虚部如何产生质量壳delta函数。先对单个实变量分解分母：

<span id="eq:c25-sokhotski"></span>

$$
\frac1{X-i\eta}=\frac{X}{X^2+\eta^2}
+i\frac{\eta}{X^2+\eta^2}
\ \longrightarrow\
\operatorname{PV}\frac1X+i\pi\delta(X).
\tag{25.25}
$$

箭头表示$\eta\downarrow0$的分布极限。将两边与光滑测试函数$f$相乘并积分，第一项在原点两侧对称删去小区间后趋于主值。第二项作代换$X=\eta u$，便有$\int du\,f(\eta u)/(1+u^2)\to\pi f(0)$，所以给出delta函数，其系数为正的$\pi$。

简记$P_i=\operatorname{PV}(1/X_i)$、$\delta_i=\delta(X_i)$。把这个分解分别用于两条线，分母之积为

<span id="eq:c25-denominator-product"></span>

$$
(P_1+i\pi\delta_1)(P_2+i\pi\delta_2)
=P_1P_2-\pi^2\delta_1\delta_2
+i\pi(P_1\delta_2+\delta_1P_2).
\tag{25.26}
$$

圈积分外的$-i$会把实部与虚部联系起来，因此$\Pi$的虚部由上式的实部给出：

<span id="eq:c25-im-before-cut"></span>

$$
\operatorname{Im}\Pi(k^2)
=-\frac{g^2}{2}\int_k
\left(P_1P_2-\pi^2\delta_1\delta_2\right).
\tag{25.27}
$$

可见，式[（25.25）](#eq:c25-sokhotski)中的两个delta项还不是全部贡献，主值乘积也在其中。为了把结果完全写成质量壳上的积分，需要再找出主值乘积与双delta项之间的关系。这可以利用时间支撑相反的两个因果核来实现。

先看坐标空间与圈动量之间的对应。将$\Delta(x)=\int d^6\ell\,e^{i\ell x}/[(2\pi)^6(\ell^2+m^2-i0)]$与自身相乘，再对$x$作傅里叶积分，便得到

<span id="eq:c25-fourier-convolution"></span>

$$
\int d^6x\,e^{-ikx}\Delta(x)^2
=\int_k\frac1{X_1-i0}\frac1{X_2-i0}.
\tag{25.28}
$$

其中$x$积分产生$(2\pi)^6\delta^6(\ell_1+\ell_2-k)$，恰好恢复两条内线在顶点的动量守恒。改用[第8节的推迟和超前传播子](/posts/srednicki-08/#eq:c08-retarded)时，两份核具有相反的时间支撑。下面用能量围道直接求出它们卷积的零值，同时确定时间边界的处理。

令$\ell_2^0=k^0-\ell_1^0$，先固定空间动量，同时保留实的空间紫外截断。两份混合核的能量分母取为

<span id="eq:c25-mixed-prescription"></span>

$$
\frac1{\omega_1^2-(\ell_1^0-i\eta)^2}\,
\frac1{\omega_2^2-(k^0-\ell_1^0+i\eta)^2},
\qquad \eta>0.
\tag{25.29}
$$

把两个分母各自分解为一次因子，四个$\ell_1^0$极点分别位于

<span id="eq:c25-mixed-poles"></span>

$$
\ell_1^0=\pm\omega_1+i\eta,\qquad
\ell_1^0=k^0\mp\omega_2+i\eta.
\tag{25.30}
$$

这四个极点全部在上半平面，而被积函数在大圆上按$(\ell_1^0)^{-4}$下降。因此向下半平面闭合围道时没有留数，能量积分为零。先在固定空间动量和截断下得到这一结果，再取边界值与空间截断极限，就给出了所需零积分的具体含义。

记$\sigma_i=\operatorname{sign}\ell_i^0$。式[（25.29）](#eq:c25-mixed-prescription)中的第一因子趋于$P_1-i\pi\sigma_1\delta_1$，第二因子趋于$P_2+i\pi\sigma_2\delta_2$。两者相乘，并对刚才得到的零积分取实部，便有

<span id="eq:c25-zero-mixed-real"></span>

$$
0=\int_k\left(P_1P_2+\pi^2\sigma_1\sigma_2\delta_1\delta_2\right).
\tag{25.31}
$$

把这个零积分从式[（25.27）](#eq:c25-im-before-cut)中的组合减去，主值乘积便相消，只留下两条线同时在壳上的部分：

<span id="eq:c25-double-cut"></span>

$$
\operatorname{Im}\Pi(k^2)
=\frac{g^2\pi^2}{2}\int_k
(1+\sigma_1\sigma_2)\delta_1\delta_2.
\tag{25.32}
$$

能量异号时，$1+\sigma_1\sigma_2=0$；同号时这个因子等于2。又因为$k^0>0$，且动量守恒要求$\ell_1^0+\ell_2^0=k^0$，两条线不可能同时具有负能量。因此，在当前积分内可以把它改写成

<span id="eq:c25-positive-energy-cut"></span>

$$
(1+\sigma_1\sigma_2)\delta_1\delta_2
=2\theta(\ell_1^0)\theta(\ell_2^0)\delta_1\delta_2.
\tag{25.33}
$$

再将系数写为$g^2\pi^2=(g^2/4)(2\pi)^2$，把两个圆周因子分别归到两条线上，就得到

<span id="eq:c25-cut-lips"></span>

$$
\begin{aligned}
\operatorname{Im}\Pi(k^2)
={}&\frac{g^2}{4}\int_k
\bigl[2\pi\delta(\ell_1^2+m^2)\theta(\ell_1^0)\bigr]\\
&\hspace{34mm}\times
\bigl[2\pi\delta(\ell_2^2+m^2)\theta(\ell_2^0)\bigr]\\
={}&\frac{g^2}{4}\int d\mathrm{LIPS}_2.
\end{aligned}
\tag{25.34}
$$

每个方括号都把原来的六维积分变成一份正能量单粒子测度，两条内线的虚动量积分因此落到了可达末态的质量壳上。这就是把内部线“切开”的含义。在$k^2=-M^2$处，式[（25.3）](#eq:c25-decay-measure)给出$M\Gamma_0=(g^2/4)\int d\mathrm{LIPS}_2$，再次得到$\operatorname{Im}\Pi(-M^2-i0)=M\Gamma_0$。系数$1/4$已经包含原图的对称计数以及虚部关系中的二，两个相同粒子的$2!$无需再除一次。

同一个结果也可以从原费曼圈的能量积分直接得到。这样还能看清切线规定的能量方向怎样由费曼极点选出。在$k=(E,\mathbf0)$、$E>2m$时，两份$\omega$相同，下半平面的极点为$\ell^0=\omega-i0$和$\ell^0=E+\omega-i0$。暂略去共同的无穷小量，把两处留数相加，有

<span id="eq:c25-energy-residue-sum"></span>

$$
-\frac1{2\omega E(2\omega-E)}
+\frac1{2\omega E(2\omega+E)}
=-\frac1{\omega(4\omega^2-E^2)}.
\tag{25.35}
$$

下半平面围道按顺时针方向闭合，与测度$d\ell^0/(2\pi)$一起给出$-i$。恢复费曼边界值后，能量积分因而为

<span id="eq:c25-energy-integral"></span>

$$
\int\frac{d\ell^0}{2\pi}
\frac1{\omega^2-(\ell^0)^2-i0}
\frac1{\omega^2-(E-\ell^0)^2-i0}
=\frac{i}{\omega(4\omega^2-E^2-i0)}.
\tag{25.36}
$$

将这个结果乘回式[（25.24）](#eq:c25-original-loop)中的$-ig^2/2$，再取虚部，能量分母便产生一个径向delta函数。其宗量在根处的雅可比为$|d(4\omega_p^2-E^2)/dp|_{p_*}=8p_*$，所以

<span id="eq:c25-cut-radial-check"></span>

$$
\begin{aligned}
\operatorname{Im}\Pi(-E^2-i0)
&=\frac{\pi g^2}{2}\frac{\Omega_5}{(2\pi)^5}
\int_0^\infty dp\,\frac{p^4}{\omega_p}
\delta(4\omega_p^2-E^2)\\
&=\frac{\pi g^2}{2}\frac{\Omega_5}{(2\pi)^5}
\frac{p_*^3}{8(E/2)}
=\frac{g^2E^2}{768\pi^2}
\left(1-\frac{4m^2}{E^2}\right)^{3/2}.
\end{aligned}
\tag{25.37}
$$

这里$p_*=\sqrt{E^2-4m^2}/2$，所得阈值因子和系数与式[（25.21）](#eq:c25-absorption-width)相同。两种计算中，一种先把费曼分母分解成分布，另一种先完成能量积分；它们都把吸收部归结为正能量末态的相空间。

更一般的切线规则（Cutkosky rules）把图的不连续性写成所有允许切法之和：穿过切面的线取正能量质量壳，两侧振幅按共轭关系组合。对于厄米相互作用、稳定渐近态以及保持这些关系的正则化，最大时间等式把这一关系推广到各阶图。其传播子分解、顶点标记与切线规则的关系，可参看 [Denner 与 Lang 的 §2.2](https://arxiv.org/pdf/1406.6280v2#page=4)。

<span id="c25-pole-time"></span>

## 共振极点与寿命

自能虚部与衰变相空间的联系确定了宽度的数值。要进一步了解这个数怎样决定寿命，先考察量子力学中的共振。若一条分波振幅在能量$E_0$附近由孤立简单极点支配，将缓变留数吸收到系数中后，可以写成

<span id="eq:c25-partial-wave-pole"></span>

$$
f_\ell(E)\simeq\frac{r_\ell}{E-E_0+i\Gamma/2}.
\tag{25.38}
$$

这个近似保留了洛朗展开的极点项，要求被忽略的正则部分在所讨论能量区间内较小。为了求相应的时间变化，再将不同能量的振幅合成为波包。若其能量分布为$\widetilde\psi(E)$，要计算的积分就是

<span id="eq:c25-wavepacket-integral"></span>

$$
\int_{-\infty}^{\infty}dE\,
\frac{\widetilde\psi(E)e^{-iEt}}{E-E_0+i\Gamma/2}.
\tag{25.39}
$$

取$t>0$，并假定波包因子在所用下半平面区域解析、大弧贡献消失。此时按顺时针方向闭合围道，只需取极点$E_0-i\Gamma/2$的留数，得到极点部分的时间依赖

<span id="eq:c25-wavepacket-residue"></span>

$$
-2\pi i\,\widetilde\psi(E_0-i\Gamma/2)
e^{-iE_0t-\Gamma t/2}.
\tag{25.40}
$$

完整波包还包含割线与背景的贡献。在极点项占主导的时间范围内，振幅的模方按$e^{-\Gamma t}$下降，对应的指数衰减寿命为$\tau=1/\Gamma$。这说明能量极点的负虚部与衰减率之间相差一个因子二。

对重场传播子作同样的傅里叶积分，就能把前面求出的自能虚部放入这一解释。先在共振附近将$\Pi$冻结为$iI=iM\Gamma_0$，并定义

<span id="eq:c25-complex-frequency"></span>

$$
\Omega_{\mathbf k}=\sqrt{\mathbf k^2+M^2-iI},
\qquad \operatorname{Re}\Omega_{\mathbf k}>0,\quad
\operatorname{Im}\Omega_{\mathbf k}<0.
\tag{25.41}
$$

按前面的约定，时间有序二点核是$\boldsymbol\Delta_\varphi/i$。在正能量极点处，带时间指数的被积函数留数为$i e^{-i\Omega_{\mathbf k}t}/(2\Omega_{\mathbf k})$；乘上顺时针围道给出的$-i$，便有

<span id="eq:c25-time-propagator"></span>

$$
\int\frac{dE}{2\pi}\,
\frac{-i\,e^{-iEt}}{-E^2+\mathbf k^2+M^2-iI}
=\frac{e^{-i\Omega_{\mathbf k}t}}{2\Omega_{\mathbf k}},
\qquad t>0.
\tag{25.42}
$$

在静止系中，$\Omega_{\mathbf0}=M-i\Gamma_0/2+O(\Gamma_0^2/M)$，因此恢复式[（25.40）](#eq:c25-wavepacket-residue)中的衰减指数。对于运动的重粒子，令$E_{\mathbf k}=\sqrt{\mathbf k^2+M^2}$，将平方根按小宽度展开，得到

<span id="eq:c25-time-dilation"></span>

$$
\Omega_{\mathbf k}
=E_{\mathbf k}-\frac{iM\Gamma_0}{2E_{\mathbf k}}
+O\!\left(\frac{M^2\Gamma_0^2}{E_{\mathbf k}^3}\right).
\tag{25.43}
$$

虚部随动量的变化使实验室系中的概率衰减率成为$M\Gamma_0/E_{\mathbf k}$，寿命相应延长为静止寿命的$E_{\mathbf k}/M$倍，与相对论的时间延缓一致。

这里的指数律来自极点近似，其时间范围也由极点近似决定。例如，若归一化制备态具有有限的能量方差，直接在制备时刻附近展开时间演化，有

<span id="eq:c25-short-time"></span>

$$
\begin{aligned}
\langle\psi|e^{-iHt}|\psi\rangle
&=1-i\langle H\rangle t-\frac12\langle H^2\rangle t^2+o(t^2),\\
\bigl|\langle\psi|e^{-iHt}|\psi\rangle\bigr|^2
&=1-\bigl(\langle H^2\rangle-\langle H\rangle^2\bigr)t^2+o(t^2).
\end{aligned}
\tag{25.44}
$$

模方中的两个一次项相消，所以极短时间内的概率下降从二次项开始。前面的指数描述则对应随后由近极点谱权重支配的衰减区间。

要将复极点与第13、15节的谱表示相接，还须说明它位于哪一张解析面。物理费曼值取在$z=-s-i0$的下岸，而冻结自能后求得$z_p=-M^2+iI$。这个极点由物理下岸穿过割线延拓到相邻的第二张黎曼面；若在第一张面的上岸直接取复共轭值，得到的就不是同一个延拓。不稳定粒子在谱中表现为连续态结构，稳定粒子所具有的孤立实质量壳已被取代。因此，精确的共振极点应定义为

<span id="eq:c25-second-sheet-pole"></span>

$$
z_p+M^2-\Pi_{\rm II}(z_p)=0,\qquad
s_p=-z_p=(M_p-i\Gamma_p/2)^2.
\tag{25.45}
$$

令$\delta z=z_p+M^2$，并在远离阈值的局部解析区展开逆核，就有

<span id="eq:c25-pole-expansion"></span>

$$
\bigl[1-\Pi'_{\rm II}(-M^2)\bigr]\delta z
=iI+\frac12\Pi''_{\rm II}(-M^2)(\delta z)^2+\cdots.
\tag{25.46}
$$

领先阶只保留自能在壳上的值，给出$\delta z=iI$，即$s_p=M^2-iM\Gamma_0$。若再保留$\Pi'_{\rm II}(-M^2)=ib$，仅求线性项所得的解就已经改为

<span id="eq:c25-pole-derivative"></span>

$$
\delta z=\frac{iI}{1-ib}
=\frac{-Ib+iI}{1+b^2},
\tag{25.47}
$$

从$s_p$取平方根还会继续产生更高阶修正。因此，$I/M$、固定宽度峰形中的宽度以及由复极点定义的$\Gamma_p$在领先窄宽度阶相等；若提高精度，就应按式[（25.45）](#eq:c25-second-sheet-pole)连同自能斜率一起求极点。在更高阶计算中，切线规则仍用来计算吸收部，而由吸收部求宽度还须结合所采用的宽度定义和极点留数。

<span id="c25-resonance"></span>

## 在稳定粒子的散射中观察共振

现在可以把重粒子的复极点放回可观测的散射过程。考虑$\chi\chi\to\chi\chi$，并取保持$\chi\mapsto-\chi$的真空。此时含奇数个$\chi$的完整顶角均为零，特别是三$\chi$顶角以及$\varphi$–$\chi$混合二点核都消失，所以单线可约交换只能由$\varphi$承担。轻场仍可在完整顶角和四点核内部成圈。

按第19、21节的完整核展开，将可能出现共振的$s$道单独提出，其余项合在背景中，得到

<span id="eq:c25-resonant-amplitude"></span>

$$
\mathcal T(s,t)
=\frac{V_L(s)V_R(s)}
{-s+M^2-\Pi(-s-i0)}+B(s,t).
\tag{25.48}
$$

其中$V_L,V_R$为两个完整$\varphi\chi\chi$顶角，稳定的$\chi$外腿已归一化；$B$包含$t,u$交换和四点不可约核。图25c画出第一项，两个空心圆之间的双虚线代表一条完整重场传播子。整图因子为$(iV_L)(\boldsymbol\Delta_\varphi/i)(iV_R)
=iV_L\boldsymbol\Delta_\varphi V_R$，除去散射图共同的$i$后，便得到式[（25.48）](#eq:c25-resonant-amplitude)中的正分子。

![稳定轻粒子通过完整重场传播子发生 s 道共振散射](/images/srednicki/c25_resonance.svg)

稳定轻粒子散射中的重粒子共振。空心圆表示完整三点顶角，
双虚线表示一条完整$\varphi$传播子。四条实线均为$\chi$，中心线带总入射动量。

<span id="fig:c25-resonance"></span>

在远离共振的区域，每多插入一次自能只带来$O(\alpha)$的相对修正，可以按圈数逐阶展开。接近共振时，树传播子的逆核本身变小；一旦达到

<span id="eq:c25-resonance-power-counting"></span>

$$
|s-M^2|\sim M\Gamma_0=O(\alpha M^2),
\qquad
\left|\frac{\Pi(-s)}{M^2-s}\right|\sim1,
\tag{25.49}
$$

各次自能插入就同样重要，需要保留Dyson求和后的完整分母。若共振孤立且窄，$t,u$交换和不可约四点项在这个小能量窗口内缓慢变化，第一项则因接近极点而增强。因此，在计算领先峰形时可以略去$B$，并以$V_LV_R\simeq g^2$近似缓变的顶角乘积。

将顶角近似为实耦合$g$同样只适用于这里的领先阶。阈值以上的完整顶角一般含有吸收部，实反项只能调节实部，不能将整个复顶角调成实$g$。例如，在$g^3$三角图中，可以切开外$\varphi$顶点旁的两条$\chi$线。剩下的重场交换分母为$M^2+(q-p)^2>0$，因为同质量、未来指向的壳上动量$q,p$满足$(q-p)^2\ge0$。只要两体相空间非零，这种切法就给出非零吸收项。因而可在所选运动学点用$\operatorname{Re}V_3$定义实耦合，并在本节所保留的阶数内使用

<span id="eq:c25-real-coupling"></span>

$$
V_3=g+O(g\alpha).
\tag{25.50}
$$

以下用这个实耦合及其领先宽度求出窄共振的峰形。

为把分母写成能量偏离共振位置的形式，令质心总能量为

<span id="eq:c25-cm-energy"></span>

$$
\sqrt s=M+\varepsilon,\qquad
s=M^2+2M\varepsilon+\varepsilon^2,\qquad
|\varepsilon|\ll M.
\tag{25.51}
$$

这里$\varepsilon$是两份入射轻粒子的总能量偏差。将运动学部分和自能都在共振附近展开，有

<span id="eq:c25-resonance-denominator"></span>

$$
\begin{aligned}
-s+M^2-\Pi(-s-i0)
={}&-2M\varepsilon-\varepsilon^2-\Pi(-M^2-i0)\\
&+2M\varepsilon\Pi'(-M^2-i0)+\cdots.
\end{aligned}
\tag{25.52}
$$

在$\varepsilon=O(\Gamma_0)$的窗口内，$\varepsilon^2$和$\varepsilon\Pi'$比领先分母多一个弱耦合阶。若还满足$M\Gamma_0\ll M^2-4m^2$，这个窗口就与轻粒子阈值充分分离，自能和顶角在窗口内的能量变化可以先忽略。于是使用$\operatorname{Re}\Pi(-M^2)=0$及$I=M\Gamma_0$，保留领先项后得到：

<span id="eq:c25-breit-wigner"></span>

$$
\mathcal T(s,t)\simeq
-\frac{g^2}{2M}\frac1{\varepsilon+i\Gamma_0/2},
\qquad
|\mathcal T|^2\simeq
\frac{g^4}{4M^2}\frac1{\varepsilon^2+\Gamma_0^2/4}.
\tag{25.53}
$$

这就是Breit–Wigner共振形式。整体负号来自传播子逆核中的$-s+M^2-\Pi$；能量分母内虚部的正号则使极点位于下半平面，与前面求出的时间衰减相符。振幅模方在$\varepsilon=\pm\Gamma_0/2$处降到峰值的一半，所以按质心总能量扫描时，半高全宽为$\Gamma_0$。

实验中的截面还含有通量、末态相空间，并可能受到与$B$干涉的影响。这些因子在窄峰内近似不变时，截面峰宽就直接给出上述宽度；若接近阈值或相邻共振，则需保留背景、相空间和$\Pi$的能量依赖。由此，最初从衰变相空间算出的参数，通过自能吸收部和复极点，成为稳定粒子散射中可以测量的共振宽度。

---

[← 第 24 节](/posts/srednicki-24/) · [章节地图](/srednicki/) · [第 26 节 →](/posts/srednicki-26/)
