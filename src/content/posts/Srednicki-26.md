---
title: 'Srednicki §26 红外发散'
date: 2026-09-14
category: 笔记
tags: [物理, 量子场论, Srednicki]
series: 'Srednicki QFT'
srednickiSections: [26]
hideFromHome: true
draft: false
---

<span id="c26"></span>

第20节在六维$\varphi^3$理论中算出的高能振幅含有$\ln(s/m^2)$；这个对数在固定碰撞能量、质量趋于零时越来越大。大圈动量引起的发散已经经过重整化，这个小质量极限中的问题提示我们，还应检查所算的“两个粒子散射”与实验事件之间的对应。如果探测器把两个几乎同向的粒子记录成一个，精确两粒子末态的截面就没有包含所有能给出同一读数的过程。本节从这种有限分辨率出发，计算遗漏的真实分裂，并将它与虚圈修正相比较。为控制共线区域的积分，质量$m$先保留非零，最后再考察小质量极限。

<span id="c26-observable"></span>

## 大对数与未分辨的粒子

先回到$s,|t|,|u|\gg m^2$且$t/s,u/s$固定的高能区域。此时第20节三个通道中的对数可以分成共同的质量对数和固定散射角的部分，振幅因而写成

<span id="eq:c26-hard-log"></span>

$$
\begin{gathered}
\mathcal T=\mathcal T_0
\left[1-\frac{11\alpha}{12}L+O(\alpha m^0)+O(\alpha^2)\right],\\
\mathcal T_0=-g^2\left(\frac1s+\frac1t+\frac1u\right),
\qquad L=\ln\frac{s}{m^2},\qquad \alpha=\frac{g^2}{(4\pi)^3}.
\end{gathered}
\tag{26.1}
$$

例如，第20节的$L_t$可写成$L+\ln(|t|/s)$，而$L_s=L-i\pi$。固定角比值的对数以及$i\pi$在$m\to0$时均有限，属于$O(m^0)$。这个记号汇集了不含发散质量对数的部分，其中的有限项仍可在需要时保留。重组各通道的对数时，仍须沿用第20节已经确定的物理分支。

这种质量极限也影响了对外态的理解。第5节隔离单粒子态时，曾使用单粒子与多粒子连续谱之间的间隔；质量趋于零后，几个同向粒子的总不变质量也可以趋于零，原来的隔离条件便失去保障。对应到测量，能量很低的粒子可能不被记录，夹角很小的两个粒子也可能合成一个读数。前者称为软（soft）区域，后者称为共线（collinear）区域。初态中若还有未识别的粒子，也应根据实际制备方式把它们计入。

为了先把末态分辨率说清楚，固定初态$a$，用对相同粒子置换对称的函数$F_n$表示探测器对$n$粒子末态的选择。对所有接受的末态求和，事件截面便有如下形式：

<span id="eq:c26-measured-rate"></span>

$$
\sigma[F]=\frac1{\mathcal F_a}
\sum_n\frac1{n!}\int d\Phi_n\,
F_n(k_1,\ldots,k_n)|\mathcal T_{na}|^2.
\tag{26.2}
$$

这里$d\Phi_n$是带标签的相空间，$\mathcal F_a$是初态通量；$F_n=0$表示剔除事件，$F_n=1$表示接受事件。不同粒子数的末态相互正交，即使仪器给出同一读数，它们对截面的贡献仍应按概率相加。对于同一个末态，各幅费曼图则共同构成它的振幅，要先相加振幅再取模方。把产生同一读数的未分辨末态都纳入求和，所得截面称为包容截面（inclusive cross section）。

本节取两个彼此分离的硬方向，并规定：若一对子动量的夹角$\theta<\delta$，就将它们的空间动量合并，计入同一个硬动量区间。这个区间应容纳小的共线反冲，才能在共线近似下提出公共的硬相空间。提出这一公共部分后，将未分辨末态的概率和记为$|\mathcal T|_{\rm obs}^2$，便有

<span id="eq:c26-inclusive-sum"></span>

$$
|\mathcal T|_{\rm obs}^2\,d\widetilde{\bar k}
=|\mathcal T|^2\,d\widetilde{\bar k}
+\frac12|\mathcal T_{\rm split}|^2\,d\widetilde k_1d\widetilde k_2+\cdots.
\tag{26.3}
$$

式中省写了其他末态的公共测度、通量和总delta函数，第二项在未分辨区域内积分。两子粒子相同，完整的带标签积分会把同一个无序对子计数两次，因此出现$1/2$；顶点中的收缩阶乘已经包含在三价费曼规则内。

<span id="c26-singular-regions"></span>

## 分裂振幅和红外幂计数

现在计算第二项中的分裂振幅。图26a在原来的一条出射硬腿上接入一个三价顶点，原来的外线变成一条内部传播子。把这个传播子和新增顶点乘到硬过程图块上，得到

<span id="eq:c26-splitting-factor"></span>

$$
i\mathcal T_{\rm split}
=(i\mathcal T_{\rm hard})
\frac{-i}{k_{\rm pair}^2+m^2-i0}(ig),
\qquad
\mathcal T_{\rm split}
=\frac{g}{k_{\rm pair}^2+m^2-i0}\mathcal T_{\rm hard}.
\tag{26.4}
$$

其中$k_{\rm pair}=k_1+k_2$，两条子腿分别满足$k_i^2=-m^2$。上式直接给出这一指定图块的费曼因子。当两条子腿趋于共线、其他硬方向仍彼此分离时，新增传播子接近质量壳，产生领先增强；此时硬图块中对离壳量的依赖可按共线极限展开，领先项就用原来的在壳振幅表示。

![硬过程的一条出射腿通过三价顶点分裂为两个近共线粒子](/images/srednicki/c26_split.svg)

一条出射腿的共线分裂。灰圆表示硬过程的图之和。
内部总动量$k_{\rm pair}$流入显式顶点，再分成$k_1,k_2$；箭头表示动量方向。

<span id="fig:c26-split"></span>

先令质量为零，以便找出增强可能出现在哪些区域。两个正能量动量的和满足

<span id="eq:c26-massless-virtuality"></span>

$$
k_{\rm pair}^2
=-2\omega_1\omega_2(1-\cos\theta)
=-4\omega_1\omega_2\sin^2\frac\theta2.
\tag{26.5}
$$

只要一个粒子的能量很小，或者两个动量的夹角很小，这个分母的绝对值就会减小。是否真的产生发散，还取决于相空间在这些区域内的体积。在一般$d>2$维时空中，单粒子测度的径向部分正比于$\omega^{d-3}d\omega$，两个方向的相对极角又给出$\sin^{d-3}\theta\,d\theta$。将这些因子除以传播子平方，并在小角度处展开，得到局部幂次：

<span id="eq:c26-ir-power-counting"></span>

$$
\frac{d\widetilde k_1d\widetilde k_2}{(k_{\rm pair}^2)^2}
\ \sim\
\omega_1^{d-5}d\omega_1\,
\omega_2^{d-5}d\omega_2\,
\theta^{d-7}d\theta.
\tag{26.6}
$$

因为$\int_0^\epsilon y^pdy$仅在$p>-1$时收敛，软能量下限在$d\le4$时发散，共线角下限则在$d\le6$时发散。因此，对本节的六维模型，纯软区域仍可积，留下的是共线对数。下面将以探测器的小角锥为积分区域，求出这一对数的系数。

在逐腿计算之前，还需说明同一末态中不同发射图的干涉怎样处理。设$q$为额外出射的软动量，$p_i$为原来正能量的物理硬动量，并以$\eta_i=+1$表示原出腿、$\eta_i=-1$表示原入腿。外腿旁的内部动量为$p_i+\eta_iq$，其分母满足

$$
(p_i+\eta_iq)^2+m^2=2\eta_i p_iq-m^2.
$$

先固定非零夹角，在$m\ll\omega_q\ll Q_{\rm hard}$的质量领先区域保留软动量的一次项，便得到各外腿的软因子。它们产生的是同一个额外粒子末态，因此应相干相加：

<span id="eq:c26-soft-sum"></span>

$$
\mathcal T_{n+1}(q)
=g\mathcal T_n\sum_i\frac{\eta_i}{2p_iq}
+O(\omega_q^0).
\tag{26.7}
$$

入腿的相对号来自$p_i-q$的分母。对于硬过程内部的线，其虚度仍为$O(Q_{\rm hard}^2)$，故没有同阶的$1/\omega_q$增强；这里假定硬过程没有同时接近另一共振或前向奇异区。将所有外腿项相加后，对同一个$q$末态取模方，得到

<span id="eq:c26-soft-interference"></span>

$$
g^2|\mathcal T_n|^2
\left[
\sum_i\frac1{4(p_iq)^2}
+2\sum_{i<j}\frac{\eta_i\eta_j}{4(p_iq)(p_jq)}
\right].
\tag{26.8}
$$

其中第二项是不同外腿发射之间的干涉，探测器未分辨$q$并不会使它消失。不过，在$q$只与一条硬腿共线的区域，平方项的角积分为$\theta^{d-7}d\theta$，它与另一固定硬方向的交叉项则为$\theta^{d-5}d\theta$。六维时，两者分别成为$d\theta/\theta$和$\theta\,d\theta$。前者产生共线对数，后者在小锥内可积，并受到小锥面积的抑制。因此，彼此不重叠的小锥所给出的领先对数可以逐腿相加，干涉留在相应的有限修正中。

<span id="c26-phase-space"></span>

## 合并动量与六维测度

接下来把分裂后的相空间写成原来硬腿测度乘上一项局部修正。为此，在分裂项中插入一份空间单位分辨式：

<span id="eq:c26-cluster-resolution"></span>

$$
1=\int d\widetilde{\bar k}\,
(2\pi)^{d-1}2\bar\omega_{\mathbf k}\,
\delta^{d-1}(\mathbf k_1+\mathbf k_2-\mathbf k),
\qquad \bar\omega_{\mathbf k}=\sqrt{\mathbf k^2+m^2}.
\tag{26.9}
$$

这条恒等式只规定合并后的空间动量。它使用参考硬粒子的在壳能量$\bar\omega_{\mathbf k}$，而真实两子粒子的能量应相加，所以这里有两个不同的四动量：

<span id="eq:c26-two-cluster-momenta"></span>

$$
\bar k=(\bar\omega_{\mathbf k},\mathbf k),\qquad
k_{\rm pair}=(\omega_1+\omega_2,\mathbf k),\qquad
-k_{\rm pair}^2=M_{\rm pair}^2\ge4m^2.
\tag{26.10}
$$

传播子中使用真实的离壳总动量$k_{\rm pair}$，硬相空间中的在壳参考动量$\bar k$则在共线展开时再引入。这个区别也可以通过精确的全相空间分解来说明：先把两子粒子当成质量为$M_{\rm pair}$的一条合并腿，再对其不变质量积分，写成

<span id="eq:c26-exact-phase-factorization"></span>

$$
d\Phi_{n+1}(P;k_1,k_2,\ldots)
=\int\frac{dM_{\rm pair}^2}{2\pi}\,
d\Phi_n(P;k_{\rm pair},\ldots)
d\Phi_2(k_{\rm pair};k_1,k_2).
\tag{26.11}
$$

从右侧恢复左侧时，先用两体空间delta函数固定合并动量，再做$M_{\rm pair}^2$积分。令$E_M=\sqrt{\mathbf k^2+M_{\rm pair}^2}$，便有$dM_{\rm pair}^2=2E_MdE_M$，正好消去合并腿测度中的$1/(2E_M)$。同时，$dM_{\rm pair}^2/(2\pi)$里余下的$1/(2\pi)$与两体能量delta前的$2\pi$相消。最后，$\delta(E_M-\omega_1-\omega_2)$将硬过程的能量delta变回原来的总能量delta，其余测度也就组成了左侧的完整相空间。

在共线区域内，硬振幅和测量权重可以按$M_{\rm pair}^2/s$展开。提出它们的领先项后，再用式[（26.9）](#eq:c26-cluster-resolution)分离公共硬腿测度，得到单腿修正：

<span id="eq:c26-local-splitting-probability"></span>

$$
\mathcal P_{\rm split}
=\frac{g^2}{2}\int_{\theta<\delta}
d\widetilde k_1d\widetilde k_2\,
\frac{(2\pi)^5\,2\bar\omega_{\mathbf k}\,
\delta^5(\mathbf k_1+\mathbf k_2-\mathbf k)}
{(k_{\rm pair}^2+m^2)^2}.
\tag{26.12}
$$

从这里起取$d=6$。对于$m>0$的两粒子末态，分母始终不穿零，故这一实积分中可略去费曼无穷小量。额外相空间连同插入因子的质量维数为$d-2$，而$g^2/(k_{\rm pair}^2+m^2)^2$的维数为$2-d$，两者相消，说明$\mathcal P_{\rm split}$是无量纲的相对修正。

先用空间delta函数完成$\mathbf k_2$积分，在被积函数中将它换成$\mathbf k-\mathbf k_1$。两份测度中的$1/(2\omega_i)$、插入因子$2\bar\omega$和全同粒子因子$1/2$合起来给出$\bar\omega/(4\omega_1\omega_2)$。以$\mathbf k$为极轴，再记$r_1=|\mathbf k_1|$、$\beta=\angle(\mathbf k_1,\mathbf k)$，剩下的积分便为

<span id="eq:c26-five-dimensional-measure"></span>

$$
\mathcal P_{\rm split}
=\frac{g^2\Omega_4}{4(2\pi)^5}
\int\frac{\bar\omega}{\omega_1\omega_2}
\frac{r_1^4\,dr_1\,\sin^3\beta\,d\beta}
{(k_{\rm pair}^2+m^2)^2},
\qquad \Omega_4=2\pi^2.
\tag{26.13}
$$

这里$\Omega_4$表示横向四维空间中$S^3$的面积；上一节的$\Omega_5$则是五维动量空间的全角面积。

局部分裂的$1/2$也可从完整三粒子末态的$1/3!$得到。三个带标签末态共有3种近共线对子，在互不重叠的共线区内合给$3/3!=1/2$。若改为从原来的两条硬腿出发计数，同一个因子写成

<span id="eq:c26-identical-consistency"></span>

$$
\frac1{2!}\times
2\times\frac1{2!}=\frac12.
\tag{26.14}
$$

第一个因子属于Born两粒子末态，中间的2选择哪条硬腿发生分裂，最后一个因子除去子粒子对的重复计数。由此，完整三粒子相空间与逐硬腿的局部分解给出了相同的物理计数。

<span id="c26-geometry"></span>

## 小角几何与质量截断

要把剩下的径向和极角积分改写成子粒子的动量份额，先理清动量三角形。令$K=|\mathbf k|$、$\gamma=\angle(\mathbf k_2,\mathbf k)$，两子动量位于合并方向的两侧，因而$\theta=\beta+\gamma$。对这个三角形使用正弦定理，就有

<span id="eq:c26-sine-geometry"></span>

$$
r_1=K\frac{\sin\gamma}{\sin\theta},\qquad
r_2=K\frac{\sin\beta}{\sin\theta}.
\tag{26.15}
$$

取$\beta=x\theta$、$\gamma=(1-x)\theta$，其中$0<x<1$、$0<\theta<\delta$。将正弦函数按小角展开后，$x$也成为第二子粒子所占的动量份额：

<span id="eq:c26-collinear-fractions"></span>

$$
r_1=(1-x)K[1+O(\theta^2)],\qquad
r_2=xK[1+O(\theta^2)],\qquad
\sin\beta=x\theta[1+O(\theta^2)].
\tag{26.16}
$$

从$(r_1,\beta)$换到$(x,\theta)$时，径向动量和极角都依赖两个新变量，因此要同时计算二维变量代换的雅可比。先对精确正弦关系求导，得到行列式

<span id="eq:c26-geometric-jacobian"></span>

$$
\begin{aligned}
\det\frac{\partial(r_1,\beta)}{\partial(x,\theta)}
&=x\,\partial_xr_1-\theta\,\partial_\theta r_1\\
&=-\frac{K\theta}{\sin^2\theta}
\bigl[\cos\gamma\sin\theta-\sin\gamma\cos\theta\bigr]\\
&=-\frac{K\theta\sin(x\theta)}{\sin^2\theta}.
\end{aligned}
\tag{26.17}
$$

取其绝对值并在小角处展开，积分所需的雅可比为$Kx[1+O(\theta^2)]$。将它连同式[（26.16）](#eq:c26-collinear-fractions)一起代入测度，并在传播子分母以外保留领先质量项，各个因子依次合成为

<span id="eq:c26-measure-jacobian-product"></span>

$$
\begin{aligned}
\frac{\bar\omega}{\omega_1\omega_2}
r_1^4\sin^3\beta\,dr_1\,d\beta
&\simeq
\frac{K}{x(1-x)K^2}(1-x)^4K^4
x^3\theta^3(Kx)\,dx\,d\theta\\
&=K^4x^3(1-x)^3\theta^3\,dx\,d\theta.
\end{aligned}
\tag{26.18}
$$

其中最后一份$x$来自变量代换的雅可比，它参与决定后面能量份额积分的权重。

传播子接近质量壳时，质量项会与小角项竞争，因而需要保留。为明确它们各自的来源，先将分母写成精确的实表达式：

<span id="eq:c26-exact-pair-denominator"></span>

$$
D_{\rm pair}:=k_{\rm pair}^2+m^2
=-m^2-2(\omega_1\omega_2-r_1r_2\cos\theta).
\tag{26.19}
$$

在固定$x\in(0,1)$时，分别使用$\omega_i=r_i+m^2/(2r_i)+\cdots$和$1-\cos\theta=\theta^2/2+\cdots$，保留最先出现的质量项与小角项，得到

<span id="eq:c26-denominator-expansion"></span>

$$
D_{\rm pair}
=-r_1r_2\theta^2
-m^2\left(1+\frac{r_1}{r_2}+\frac{r_2}{r_1}\right)+\cdots.
\tag{26.20}
$$

不含径向比值的$-m^2$由两子粒子的质量壳条件及分母外加的一份$m^2$合成，另外两项则来自能量乘积的展开。再利用动量份额之间的恒等式

$$
1+\frac{1-x}{x}+\frac{x}{1-x}
=\frac{1-x+x^2}{x(1-x)}
$$

把这三个质量项合并，并提出与角度项相同的公共因子，便得到

<span id="eq:c26-mass-regulated-denominator"></span>

$$
D_{\rm pair}\simeq-x(1-x)K^2
\left[\theta^2+\frac{m^2}{K^2}f(x)\right],
\qquad
f(x)=\frac{1-x+x^2}{x^2(1-x)^2}.
\tag{26.21}
$$

以等分动量$x=1/2$、$\theta=0$为例，精确分母为$-3m^2$，这个展开式也给出$-3m^2$。质量项因此使传播子分母保持非零，其影响主要集中在$\theta^2\lesssim(m^2/K^2)f(x)$的区域，正好截住了无质量情形的共线增强。

现在将式[（26.18）](#eq:c26-measure-jacobian-product)除以传播子分母平方，公共的$K^4x^2(1-x)^2$相消，动量份额权重只留下$x(1-x)$。六维的整体归一化也可用圈展开参数表示，因为

$$
\frac{g^2\Omega_4}{4(2\pi)^5}
=\frac{g^2}{(4\pi)^3}=\alpha,
$$

单腿贡献于是化为一个动量份额积分和一个小角积分：

<span id="eq:c26-double-integral"></span>

$$
\mathcal P_{\rm split}
\simeq\alpha\int_0^1dx\,x(1-x)
\int_0^\delta\frac{\theta^3d\theta}
{\left[\theta^2+(m^2/K^2)f(x)\right]^2}.
\tag{26.22}
$$

这一步所用的质量与角分辨率层级是

<span id="eq:c26-hierarchy"></span>

$$
\frac{m^2}{K^2}\ll\delta^2\ll1.
\tag{26.23}
$$

小角展开控制几何和硬过程图块的误差，$m/(K\delta)$则衡量质量截断区域相对于整个未分辨锥的大小。满足这一层级后，可以依次完成角度和动量份额积分，并保留对数以外的有限常数。

<span id="c26-integrals"></span>

## 角积分、有限常数与端点

先固定$x$，记$a=(m^2/K^2)f(x)>0$。作代换$y=\theta^2$，再将分子分解为$y=(y+a)-a$，角积分就成为两个初等积分：

<span id="eq:c26-exact-angular-integral"></span>

$$
\begin{aligned}
I_\theta(a,\delta)
&=\frac12\int_0^{\delta^2}\frac{y\,dy}{(y+a)^2}\\
&=\frac12\left[
\ln\left(1+\frac{\delta^2}{a}\right)
-\frac{\delta^2}{\delta^2+a}\right].
\end{aligned}
\tag{26.24}
$$

第二项来自$-a/(y+a)^2$的积分。在$a/\delta^2\to0$时，它趋于有限常数$-1/2$，而第一项给出质量与角分辨率的对数，于是

<span id="eq:c26-angular-asymptotic"></span>

$$
I_\theta
=\frac12\ln\frac{\delta^2K^2}{m^2}
-\frac12\ln f(x)-\frac12+o(1).
\tag{26.25}
$$

角积分留下了对数及一个有限项。将它们一起对动量份额积分，才能确定单腿修正中的有限常数。

令$w=x(1-x)$，把剩下的动量份额积分分解为三个矩：

<span id="eq:c26-log-moments"></span>

$$
\int_0^1w\,dx=\frac16,\qquad
\int_0^1w\ln w\,dx=-\frac5{18},\qquad
\int_0^1w\ln(1-w)\,dx
=-\frac{17}{18}+\frac{\pi}{2\sqrt3}.
\tag{26.26}
$$

第二式先用$x\leftrightarrow1-x$将两份对数合并，再由$\int_0^1x^n\ln x\,dx=-1/(n+1)^2$得到$2(-1/4+1/9)=-5/18$。第三式已经在第14节的式[（14.44）](/posts/srednicki-14/#eq:c14-j1-evaluated)中求出：本节的$w$与当时的费曼参数组合$x(1-x)$相同，因而直接代入那个积分结果即可。最后，由$f=(1-w)/w^2$把两种对数合起来，有

<span id="eq:c26-f-log-moment"></span>

$$
J_f:=\int_0^1w\ln f\,dx
=-\frac{17}{18}+\frac{\pi}{2\sqrt3}
-2\left(-\frac5{18}\right)
=-\frac7{18}+\frac{\pi}{2\sqrt3}.
\tag{26.27}
$$

将这个对数矩代回角积分后的表达式，再合并不含对数的部分，得到

<span id="eq:c26-collinear-constant"></span>

$$
\begin{aligned}
\int_0^1wI_\theta\,dx
&=\frac1{12}\ln\frac{\delta^2K^2}{m^2}
-\frac12J_f-\frac1{12}+o(1)\\
&=\frac1{12}\left[\ln\frac{\delta^2K^2}{m^2}+c\right]+o(1),\\
c&=-1-6J_f=\frac43-\sqrt3\pi\simeq-4.10806.
\end{aligned}
\tag{26.28}
$$

乘回整体因子$\alpha$，一条硬腿的未分辨分裂概率修正就是

<span id="eq:c26-single-leg-result"></span>

$$
\mathcal P_{\rm split}
=\frac\alpha{12}
\left[\ln\frac{\delta^2K^2}{m^2}+c\right]
+\text{小角与小质量的高阶项}.
\tag{26.29}
$$

其中$c$取两位小数时为$-4.11$。

上面先使用了式[（26.25）](#eq:c26-angular-asymptotic)，再对$x$积分，因此还要看渐近式在端点附近的误差。当$x$接近0或1时，$f(x)$发散，条件$a\ll\delta^2$不再对整个区间一致成立。令$r=m^2/(K^2\delta^2)$，将精确角积分与式[（26.25）](#eq:c26-angular-asymptotic)前三项相减，余项可直接写成

<span id="eq:c26-endpoint-remainder"></span>

$$
E_r(x)=\frac12\left[
\ln(1+rf(x))+\frac{rf(x)}{1+rf(x)}
\right]\ge0.
\tag{26.30}
$$

在$x\le1/2$的半区间内，有$w=O(x)$和$f=O(x^{-2})$。把积分在$x=\sqrt r$处分开：第一段作$x=\sqrt r\,u$代换，$\int wE_rdx$由$r\int_0^1u[1+\ln(1+u^{-2})]du$控制，因该无量纲积分收敛而为$O(r)$；第二段使用$\ln(1+y)\le y$及$y/(1+y)\le y$，得到$O(r\int_{\sqrt r}^{1/2}dx/x)$。另一端由对称性给出相同估计，两端合起来便有

<span id="eq:c26-endpoint-bound"></span>

$$
\int_0^1wE_r\,dx=O(r|\ln r|)\longrightarrow0.
\tag{26.31}
$$

因此，固定$x$得到的小质量展开在加权积分后仍保留正确的对数和有限常数。

分母外的能量展开也应先在$\eta<x<1-\eta$上使用，再让$\eta$趋于零。对于$r_i=O(m)$的极端软端点，要保留精确能量$\omega_i=\sqrt{r_i^2+m^2}$。例如，$x\lesssim m/K$时有$r_1\sim K$、$\omega_2\sim m$，而$\omega_2-r_2$仍为$m$的量级，所以$|D_{\rm pair}|$至少为$Km$的量级。与此同时，精确测度中的$\sin^3(x\theta)$和雅可比分别给出$x^3\theta^3$和$Kx$，足以将这一窄区间的贡献压低到

$$
\frac{K^3}{m^3}\int_0^{m/K}x^4dx
\int_0^\delta\theta^3d\theta
=O\!\left(\frac{m^2}{K^2}\delta^4\right)
$$

所示的量级。另一端的估计相同，因此这两个窄区间都不改变有限常数，也不产生额外的纯软对数。

也可以数值比较两种局部积分。取 $K=1$，从式[（26.13）](#eq:c26-five-dimensional-measure)使用精确正弦几何和能量得到 $I_{\rm geom}=\mathcal P_{\rm split}/\alpha$；用式[（26.24）](#eq:c26-exact-angular-integral)再对 $x$ 积分得到共线近似 $I_{\rm coll}$：

| $\delta$ | $m$              | $I_{\rm geom}$ | $I_{\rm coll}$ | 两者之差              |
| -------- | ---------------- | -------------- | -------------- | --------------------- |
| $0.1$    | $10^{-4}$        | $0.8090226734$ | $0.8089671307$ | $5.5543\times10^{-5}$ |
| $0.03$   | $3\times10^{-5}$ | $0.8089721288$ | $0.8089671307$ | $4.9981\times10^{-6}$ |
| $0.03$   | $3\times10^{-6}$ | $1.1927231780$ | $1.1927181779$ | $5.0000\times10^{-6}$ |

前两行保持 $m/(K\delta)=10^{-3}$，差值之比与 $\delta^2$ 之比相符；后两行固定角分辨率而减小质量，小角误差基本不变。这些结果对应已提出公共硬过程的局部分裂积分。

<span id="c26-initial-states"></span>

## 入射配置与四条腿的求和

两个出射硬方向彼此分离，因此另一条出射腿也给出同样的式[（26.29）](#eq:c26-single-leg-result)。若还要为两条入射腿各加上一份相同贡献，就须指定初态制备：末态探测器怎样合并读数，与束流中包含多少额外入射粒子，是事件概率中的两种不同权重。

可在有限体积内用归一化初态密度矩阵表示制备。若$\rho_I=\sum_a w_a|a\rangle\langle a|$是非相干混合，满足$w_a\ge0$和$\sum_aw_a=1$，接受事件的概率为

<span id="eq:c26-initial-density"></span>

$$
\mathcal P(F|\rho_I)
=\sum_f F(f)\langle f|S\rho_I S^\dagger|f\rangle
=\sum_{a,f}w_aF(f)|S_{fa}|^2.
\tag{26.32}
$$

末态求和由$F$确定，初态的混合则由$w_a$确定。若$\rho_I$固定为纯两粒子态，求和中便没有额外初粒子的吸收通道；若初态含有非对角的相干项，上式还须保留相应干涉。

可以采用一种初末态对称的规定：将每个入射、出射硬方向都视为未分辨粒子簇，对互为时间反演的共线配置赋予相同的局部相空间权重。提出同一硬过程的归一化和通量后，每个簇的附加权重取为

<span id="eq:c26-symmetric-cluster-weight"></span>

$$
\frac12d\widetilde k_1d\widetilde k_2\,
(2\pi)^5\,2\bar\omega\,
\delta^5(\mathbf k_1+\mathbf k_2-\mathbf k).
\tag{26.33}
$$

在有限体积和有限硬动量区间内，这给出一种可归一化的正混合制备权重。与同一制备下的Born参考率作比时，共同归一化因子一起提出。若实际两粒子簇的权重随$x$变化，则应将它乘回积分，所得结果也会相应改变。

对于实标量理论，时间反演使配对过程的平方矩阵元相等。两条共线入腿先融合，再进入硬过程图块，局部顶点与内部虚度仍给出$g^2/(k_{\rm pair}^2+m^2)^2$。因此，配以式[（26.33）](#eq:c26-symmetric-cluster-weight)的相同局部权重后，每条入腿的积分便等于一条出腿的积分。四条硬腿在相对$O(\alpha)$各贡献一份，合起来得到

<span id="eq:c26-four-leg-result"></span>

$$
|\mathcal T|_{\rm obs}^2
=|\mathcal T|^2
\left[
1+\frac{4\alpha}{12}
\left(\ln\frac{\delta^2K^2}{m^2}+c\right)+O(\alpha^2)
\right].
\tag{26.34}
$$

若只指定末态分辨率，而初态仍固定为两个粒子，同一计算只包含两条出腿的未分辨分裂贡献。

<span id="c26-real-virtual"></span>

## 真实分裂与虚圈的对数

有了真实分裂的概率修正，现在将它与原硬过程的虚圈修正合并。对式[（26.1）](#eq:c26-hard-log)取模方时，共同的实质量对数在振幅及其共轭中各出现一次，因而

<span id="eq:c26-virtual-square"></span>

$$
|\mathcal T|^2
=|\mathcal T_0|^2
\left[1-\frac{11\alpha}{6}L
+O(\alpha m^0)+O(\alpha^2)\right].
\tag{26.35}
$$

真实分裂已经是相对$O(\alpha)$的修正，其中的硬振幅只需保留$\mathcal T_0$；若再乘一圈硬修正，就进入了$O(\alpha^2)$。在两体质心系的领先质量阶，$K^2=s/4$，故真实分裂中的对数可以改写为

<span id="eq:c26-cm-log"></span>

$$
\ln\frac{\delta^2K^2}{m^2}+c
=L+\ln\delta^2-\ln4+c.
\tag{26.36}
$$

有限组合$-\ln4+c$可并入式[（26.35）](#eq:c26-virtual-square)的其他有限项。按四腿规定将真实与虚圈贡献相加，并只保留同一弱耦合阶，两个大对数分别为

<span id="eq:c26-residual-logs"></span>

$$
\begin{aligned}
\frac{|\mathcal T|_{\rm obs}^2}{|\mathcal T_0|^2}
&=1+\alpha\left[
-\frac{11}{6}L+\frac13L+\frac13\ln\delta^2+O(m^0)
\right]+O(\alpha^2)\\
&=1-\alpha\left[
\frac32L+\frac13\ln\frac1{\delta^2}+O(m^0)
\right]+O(\alpha^2).
\end{aligned}
\tag{26.37}
$$

未分辨的真实分裂补回正的概率，抵消了虚圈的一部分负对数。如果只对两条出腿求和，质量对数的系数则为$-11/6+2/12=-5/3$；它与四腿结果中的$-3/2$分别对应不同的初态规定。

余下的$\ln(1/\delta^2)$记录探测器的角分辨率。取更小的$\delta$，就能识别并剔除夹角更小的额外粒子，接受为两簇事件的条件随之变严格，所以这一对数随分辨能力提高而增大。要继续使用一圈截断，除了小耦合本身，还须满足

<span id="eq:c26-perturbative-log-domain"></span>

$$
\alpha\ll1,\qquad
\alpha\left|\ln\frac{s}{m^2}\right|\ll1,\qquad
\alpha\ln\frac1{\delta^2}\ll1.
\tag{26.38}
$$

当大对数使高阶项不再比领先项小，就需要将更高阶贡献纳入处理。另一方面，式[（26.37）](#eq:c26-residual-logs)中仍有$\tfrac32\ln(s/m^2)$，说明在当前耦合定义下，单靠修正事件计数尚不能得到有限的无质量极限。这个残项将引向下一节：继续检查耦合常数的重整化条件。

---

[← 第 25 节](/posts/srednicki-25/) · [章节地图](/srednicki/) · [第 27 节 →](/posts/srednicki-27/)
