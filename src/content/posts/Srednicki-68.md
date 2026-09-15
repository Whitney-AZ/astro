---
title: 'Srednicki §68 量子电动力学中的沃德恒等式 II'
date: 2026-09-14
category: 笔记
tags: [物理, 量子场论, Srednicki]
series: 'Srednicki QFT'
srednickiSections: [68]
hideFromHome: true
draft: false
---

<span id="c68"></span>

上一节把光子的纵向偏振换成流的散度，再利用外腿的在壳条件证明振幅不变。
现在保留两条电子腿的离壳动量。流的散度仍然只给接触项，但这些接触项不再被
LSZ留数消去，而是留下两个精确传播子的差。截去外腿以后，这个差就把电磁顶角
同电子的逆传播子联系起来。由此可以说明，前面一圈计算中遇到的$Z_1=Z_2$
如何在更高阶继续成立，以及这一关系与电荷的定义有什么联系。

先讨论一个狄拉克场，随后转向标量电动力学。
仍用$(-,+,+,+)$和$e<0$，本节的动量改取电子以$p$入射、以$p'$出射，
光子入动量为$k=p'-p$。各核先在一般离壳的解析域中比较，再取共同的费曼边界。
维数调节时按本节约定恢复公共工程因子；
下面先用四维记号写出恒等式的结构。

<span id="c68-current-contacts"></span>

## 流的散度怎样给出传播子之差

沿用上一节的流归一，记
<span id="eq:c68-current-normalization"></span>

$$
j^\mu=e\bar\Psi\gamma^\mu\Psi,\qquad
J^\mu=Z_2j^\mu,\qquad
\mathfrak e=e\,\frac{Z_1}{Z_2}.
\tag{68.1}
$$

$J^\mu$是以电荷$e$作局域测试相位时得到的诺特流，
而麦克斯韦方程的源为$Z_1j^\mu$。暂用$\mathfrak e$保留两种归一之间的比值，
就可以在尚未证明$Z_1=Z_2$时进行计算。
定义含一个流插入的关联函数：
<span id="eq:c68-current-three-point"></span>

$$
\begin{aligned}
C^\mu_{\alpha\beta}(k,p',p)
={}&iZ_1\int d^4x\,d^4y\,d^4z\,
 e^{ikx-ip'y+ipz}\\
&\qquad\times
 \langle0|Tj^\mu(x)\Psi_\alpha(y)\bar\Psi_\beta(z)|0\rangle_c .
\end{aligned}
\tag{68.2}
$$

下标$c$表示连通部分；在平移及洛伦兹不变的真空中，一点电流为零，
真空气泡也已由真空归一除掉。这一定义显式带$iZ_1$，
与上一节给每个傅里叶场另乘$i$的写法应分开。
在图上，$iZ_1j^\mu$具有一个光子顶角的费米场结构。
如果流插入直接位于连接两条外电子腿的不可约部分中，便产生通常的1PI顶角；
它还可能先位于一个闭费米部分中，经光子线连接到外电子。
后面截腿时需要把这两类图一起考虑。

先计算$k_\mu C^\mu$。暂将式[（68.2）](#eq:c68-current-three-point)中的
坐标空间关联函数记作$G^\mu_{\alpha\beta}(x;y,z)$。
由$ik_\mu e^{ikx}=\partial_\mu e^{ikx}$，对$x$分部积分，得到
<span id="eq:c68-integration-by-parts"></span>

$$
\begin{aligned}
k_\mu C^\mu_{\alpha\beta}
={}&Z_1\int d^4x\,d^4y\,d^4z\,
 [\partial_\mu e^{ikx-ip'y+ipz}]
 G^\mu_{\alpha\beta}(x;y,z)\\
={}&-Z_1\int d^4x\,d^4y\,d^4z\,
 e^{ikx-ip'y+ipz}
 \partial_\mu G^\mu_{\alpha\beta}(x;y,z).
\end{aligned}
\tag{68.3}
$$

可先对动量用光滑波包作涂抹，使表面项消失，再将结果理解为动量空间的分布恒等式。
定义中的$Z_1$始终保留，
并将在两个端点接触项中与$Z_2$组合成式[（68.1）](#eq:c68-current-normalization)的比值。

所需的量子流恒等式已在[上一节的局域变元推导](/posts/srednicki-67/#eq:c67-noether-ward)中得到。
把无穷小偶参数提出，令$\delta\Phi_a=R_a$表示其系数，则它写成
<span id="eq:c68-local-ward"></span>

$$
\begin{aligned}
&-\partial_\mu\langle TJ^\mu(x)\Phi_1(x_1)\cdots\Phi_n(x_n)\rangle\\
&\quad=i\sum_a\delta^4(x-x_a)
 \langle T\Phi_1\cdots R_a(x_a)\cdots\Phi_n\rangle .
\end{aligned}
\tag{68.4}
$$

这里使用同一个保持矢量相位的调节、测度和复合插入处方。
局域变换的雅可比行列式及接触项的推导可直接复用；
本节新的工作是把两个带电端点代入，并完成其傅里叶积分。

对于有序拉格朗日量
$iZ_2\bar\Psi\gamma^\mu\partial_\mu\Psi-Z_m m\bar\Psi\Psi
+eZ_1A_\mu\bar\Psi\gamma^\mu\Psi$，有
<span id="eq:c68-noether-derivatives"></span>

$$
\begin{aligned}
R_\Psi&=-ie\Psi,\qquad R_{\bar\Psi}=+ie\bar\Psi,\\
\frac{\partial\mathcal L}{\partial(\partial_\mu\Psi)}
 &=iZ_2\bar\Psi\gamma^\mu,\qquad
\frac{\partial\mathcal L}{\partial(\partial_\mu\bar\Psi)}=0,\\
J^\mu
 &=\frac{\partial\mathcal L}{\partial(\partial_\mu\Psi)}R_\Psi
 =eZ_2\bar\Psi\gamma^\mu\Psi.
\end{aligned}
\tag{68.5}
$$

诺特流在这里无需加表面改变量，因为常参数相位使拉氏量严格不变。
对两个端点分别使用式[（68.4）](#eq:c68-local-ward)，
$iR_\Psi=+e\Psi$，$iR_{\bar\Psi}=-e\bar\Psi$，于是
<span id="eq:c68-two-endpoint-contacts"></span>

$$
\begin{aligned}
&-Z_2\partial_\mu
 \langle Tj^\mu(x)\Psi_\alpha(y)\bar\Psi_\beta(z)\rangle_c\\
&\quad=e[\delta^4(x-y)-\delta^4(x-z)]
       \langle T\Psi_\alpha(y)\bar\Psi_\beta(z)\rangle .
\end{aligned}
\tag{68.6}
$$

两个奇场始终保持$\Psi\bar\Psi$的次序；局域相位参数是偶数，
此处变分不交换外场，因而不再产生额外的费米号。

精确二点函数的归一沿第42、62节：
<span id="eq:c68-exact-propagator"></span>

$$
\begin{aligned}
\langle T\Psi_\alpha(y)\bar\Psi_\beta(z)\rangle
 &=\frac1i\int\frac{d^4r}{(2\pi)^4}
      e^{ir(y-z)}\widetilde S(r)_{\alpha\beta},\\
K(p)&:=\widetilde S(p)^{-1}
     =\slashed p+m-\Sigma(\slashed p).
\end{aligned}
\tag{68.7}
$$

$K$是旋量矩阵；实际费曼内线为$\widetilde S/i$。
现在分别评价式[（68.6）](#eq:c68-two-endpoint-contacts)中的两个接触项。
用$I_y,I_z$表示把共同指数和二点函数分别乘上$\delta^4(x-y)$、
$\delta^4(x-z)$后对三个坐标的积分，并记
$D_c=(2\pi)^4\delta^4(k+p-p')$。先令$x=y$，两个剩余坐标积分给
<span id="eq:c68-first-contact-integral"></span>

$$
\begin{aligned}
I_y
 &=\frac1i\int\frac{d^4r}{(2\pi)^4}\widetilde S(r)
       \int d^4y\,e^{i(k-p'+r)y}
       \int d^4z\,e^{i(p-r)z}\\
 &=\frac1i\int\frac{d^4r}{(2\pi)^4}\widetilde S(r)
       (2\pi)^4\delta^4(k-p'+r)(2\pi)^4\delta^4(p-r)\\
 &=-iD_c\,\widetilde S(p).
\end{aligned}
\tag{68.8}
$$

$z$积分固定$r=p$，另一个δ函数便成为总动量守恒。
对$x=z$的接触项，同样得到
<span id="eq:c68-second-contact-integral"></span>

$$
\begin{aligned}
I_z
 &=\frac1i\int\frac{d^4r}{(2\pi)^4}\widetilde S(r)
       \int d^4y\,e^{i(r-p')y}
       \int d^4z\,e^{i(p+k-r)z}\\
 &=-iD_c\,\widetilde S(p').
\end{aligned}
\tag{68.9}
$$

这次由$y$积分固定$r=p'$。
所以两个端点的相反电荷，恰好变成两个不同动量传播子的差：
<span id="eq:c68-current-propagator-difference"></span>

$$
k_\mu C^\mu
=\mathfrak e(I_y-I_z)
=-iD_c\,\mathfrak e[\widetilde S(p)-\widetilde S(p')] .
\tag{68.10}
$$

其中的整体$-i$来自二点函数的$1/i$；
差的次序由两个接触位置决定。

<span id="c68-proper-vertex"></span>

## 从完整流三点到不可约顶角

为了从式[（68.10）](#eq:c68-current-propagator-difference)中取出顶角，
先截去两条外电子传播子。以$iV^\mu$表示精确1PI光子—电子—电子顶角，
其直接贡献中的三个因子为
<span id="eq:c68-direct-vertex-chain"></span>

$$
\frac{\widetilde S(p')}{i}\,iV^\mu(p',p)\,
 \frac{\widetilde S(p)}{i}
=-i\widetilde S(p')V^\mu(p',p)\widetilde S(p).
\tag{68.11}
$$

流所在的闭费米圈也能通过光子线接到
一个电子顶角上。这类贡献从$e^3$阶开始；切开连接两部分的光子线，
流插入便与两条外电子腿分离，因此它不属于$V^\mu$。
完整关联函数必须把它包括进来。

所需的图分解可由流二点函数建立。先在受调节的裸理论中
记$j_B^\mu=e_B\bar\Psi_B\gamma^\mu\Psi_B$，
$\Delta_{0B}/i$为自由光子线，$i\Pi_B$为光子的完整1PI物质二点块。
把两个流之间所有可切断的单光子桥依次切开，就得到一串这样的块。
其端点有标签，先后次序已经固定，不再除以链长的阶乘。
每个光子顶角对应$ij_B$；换成两个$j_B$插入时，图值须除以$i^2$。一个不可约块给$(i\Pi_B)/i^2=\Pi_B/i$，两个块给$(i\Pi_B)(\Delta_{0B}/i)(i\Pi_B)/i^2=\Pi_B\Delta_{0B}\Pi_B/i$。因而乘回流二点定义前面的$i$，得到
<span id="eq:c68-current-polarization-chain"></span>

$$
\begin{aligned}
\mathcal H_B^{\mu\nu}(k)
 &:=i\int d^4x\,e^{-ikx}
       \langle Tj_B^\mu(x)j_B^\nu(0)\rangle_c,\\
\mathcal H_B
 &=\Pi_B+\Pi_B\Delta_{0B}\Pi_B
       +\Pi_B\Delta_{0B}\Pi_B\Delta_{0B}\Pi_B+\cdots\\
 &=\Pi_B(1-\Delta_{0B}\Pi_B)^{-1}.
\end{aligned}
\tag{68.12}
$$

矩阵乘法包含相邻洛伦兹指标的缩并。
此处的逆按耦合的形式级数定义：括号从单位矩阵开始，因而可以逐阶求逆。
若把完整光子核$\Delta_B$放入中间，同一和只有
$\Pi_B+\Pi_B\Delta_B\Pi_B$；$\Delta_B$内部已经包含任意多个中间自能块。

另一个流在局域偶相位下的变分为零，
因为$\bar\Psi_B$与$\Psi_B$的相反相位在同点相消：
<span id="eq:c68-proper-transversality"></span>

$$
\begin{aligned}
\delta j_B^\nu
 &=e_B[(ie_B\bar\Psi_B)\gamma^\nu\Psi_B
       +\bar\Psi_B\gamma^\nu(-ie_B\Psi_B)]=0,\\
k_\mu\mathcal H_B^{\mu\nu}&=0,\\
k_\mu\Pi_B^{\mu\nu}
 &=[k_\mu\mathcal H_B^{\mu\rho}]
       (1-\Delta_{0B}\Pi_B)_\rho{}^\nu=0.
\end{aligned}
\tag{68.13}
$$

第二行是将式[（68.4）](#eq:c68-local-ward)应用于第二个流插入后的结果；
同点流乘积沿同一矢量外源的导数定义，保留使沃德式成立的局部接触减除。
第三行再使用式[（68.12）](#eq:c68-current-polarization-chain)。
这样先证明完整流核横向，再从它推出不可约块横向，
没有预先使用所要证明的光子自能性质。

为了回到重整化场，使用第66节的裸量关系。它们给出
<span id="eq:c68-current-proper-normalization"></span>

$$
\begin{aligned}
\Psi_B&=\sqrt{Z_2}\Psi,& A_B&=\sqrt{Z_3}A,&
e_B&=\frac{eZ_1}{Z_2\sqrt{Z_3}},\\
Z_1j^\mu&=\sqrt{Z_3}\,j_B^\mu,&
P_J^{\mu\nu}&:=Z_3\Pi_B^{\mu\nu},&
k_\mu P_J^{\mu\nu}&=0 .
\end{aligned}
\tag{68.14}
$$

第一行按四维记号书写；在$d$维同时恢复$e_B$的工程因子。
$P_J$是把一个光子顶角换成$iZ_1j^\mu$插入后得到的不可约二点块。
它与第62节包含麦克斯韦局部反项的自能相差
<span id="eq:c68-local-maxwell-counterterm"></span>

$$
\Pi_{\rm R}^{\mu\nu}
=P_J^{\mu\nu}-(Z_3-1)(k^2g^{\mu\nu}-k^\mu k^\nu).
\tag{68.15}
$$

局部项本身横向，因此两种分拆有同一横向性质。
这一区别也固定了流乘积的局部部分；不能在几何链中只换一个核的名字，
而不同时换算其场归一和接触项。

现在从流端沿第一条光子桥分类。桥左边给$P_J$，
桥中是完整重整化光子传播子$\widetilde\Delta/i$，
桥右边是$iV$；外侧仍接精确电子传播子。由各顶角及内线的$i$相乘，
与式[（68.11）](#eq:c68-direct-vertex-chain)相同地得到
<span id="eq:c68-complete-current-three-point"></span>

$$
\begin{aligned}
C^\mu
 &=-iD_c\,\widetilde S(p')
  \left[V^\mu+
     P_J^{\mu\rho}\widetilde\Delta_{\rho\sigma}V^\sigma\right]
       \widetilde S(p),\\
k_\mu C^\mu
 &=-iD_c\,\widetilde S(p')\,k_\mu V^\mu\,\widetilde S(p).
\end{aligned}
\tag{68.16}
$$

第一行中所有核采用同一调节和相同的参数，光子二点链已经包含在
$\widetilde\Delta$中。第二行用$k_\mu P_J^{\mu\rho}=0$消去可约部分。
因此，完整流三点函数必须包含光子可约项；
收缩流端动量后，这些项才由横向性消失，留下精确1PI顶角。

将式[（68.16）](#eq:c68-complete-current-three-point)与
式[（68.10）](#eq:c68-current-propagator-difference)比较，
提出共同的$-iD_c$，得到
<span id="eq:c68-unamputated-ward"></span>

$$
\widetilde S(p')\,k_\mu V^\mu(p',p)\,\widetilde S(p)
=\mathfrak e[\widetilde S(p)-\widetilde S(p')] .
\tag{68.17}
$$

在离壳的可逆域中，先从左乘$K(p')$，再从右乘$K(p)$。
每个逆核只消去与它相邻的同动量传播子：
<span id="eq:c68-ordered-amputation"></span>

$$
\begin{aligned}
K(p')[\widetilde S(p')\,k_\mu V^\mu\,\widetilde S(p)]K(p)
 &=k_\mu V^\mu,\\
K(p')[\widetilde S(p)-\widetilde S(p')]K(p)
 &=K(p')-K(p).
\end{aligned}
\tag{68.18}
$$

这里没有交换旋量矩阵的次序。
于是得到精确沃德恒等式：
<span id="eq:c68-proper-ward"></span>

$$
(p'-p)_\mu V^\mu(p',p)
=\frac{Z_1}{Z_2}e
 [\widetilde S(p')^{-1}-\widetilde S(p)^{-1}] .
\tag{68.19}
$$

两边的质量量纲都是1，顶角无量纲而逆传播子具有质量维数1。
保留局部反项的最低阶式也直接符合这一差序：
$K_{\rm loc}=Z_2\slashed p+Z_m m$，
$V_{\rm loc}^\mu=eZ_1\gamma^\mu$，
两逆核之差中的质量项消失，右边恰为$eZ_1\slashed k$。
[下文的一圈比较](#c68-one-loop-check)将把自能和顶角的有限部分一起保留。

<span id="c68-renormalization"></span>

## 两种重整化条件为何给出同一关系

式[（68.19）](#eq:c68-proper-ward)先给出了$Z_1/Z_2$的有限性。
为看清它的含义，可在非例外离壳点选一个非零的旋量矩阵分量，
或对两边取同一个线性投影。选取使逆核差的树项不为零的投影后，
右边这个矩阵差作为形式级数可除，因而
<span id="eq:c68-finite-ratio"></span>

$$
\frac{Z_1}{Z_2}
=\frac{\mathcal P[k_\mu V^\mu]}
       {e\,\mathcal P[K(p')-K(p)]}.
\tag{68.20}
$$

$\mathcal P$只表示所选矩阵分量或其线性组合。
在去掉UV调节后，分子与分母都是已经重整化的有限量，
所以比值没有UV极点。这里取离壳点并固定共同的红外处方，
使这个判断只涉及紫外减除。

在$\overline{\mathrm{MS}}$方案中，$Z_i$是单位项加纯极部。
以单狄拉克场的电荷展开为例，
<span id="eq:c68-minimal-subtraction-series"></span>

$$
Z_i=1+\sum_{n\ge1}e^{2n}\sum_{r=1}^{n}
          \frac{z_{i,nr}}{\varepsilon^r},\qquad
\frac{Z_1}{Z_2}
=1+\sum_{n\ge1}e^{2n}\sum_{r\ge1}
          \frac{a_{nr}}{\varepsilon^r}.
\tag{68.21}
$$

每个固定圈阶只有有限多个负幂。展开$Z_2^{-1}$时，
单位项以外的每一项至少含一个负幂，因此乘上$Z_1$后仍没有独立的有限常数修正。
又由于式[（68.20）](#eq:c68-finite-ratio)证明整个比值有限，
每个$a_{nr}$只能为零。于是逐阶有
<span id="eq:c68-ms-equality"></span>

$$
Z_1=Z_2\qquad
\text{在相同的 }\overline{\mathrm{MS}}\text{ 电荷和场定义下}.
\tag{68.22}
$$

有限性与纯极部结构共同固定这一比值。若再作有限的电荷或场参数变换，
式[（68.19）](#eq:c68-proper-ward)中的系数也须相应换算。

在OS方案中，$Z_i$还含有限部分，需使用物理归一条件。
此时$m$指极点质量。先保留共同红外调节，使质量壳与软顶角附近可以取导数，
并在两电子腿尚未在壳时令$p'=p+k$。
展开式[（68.19）](#eq:c68-proper-ward)到$k$的一次项，有
<span id="eq:c68-zero-transfer-derivative"></span>

$$
\begin{aligned}
k_\mu V^\mu(p+k,p)
 &=\mathfrak e\,k_\mu\frac{\partial K(p)}{\partial p_\mu}+O(k^2),\\
V^\mu(p,p)&=\mathfrak e\,\frac{\partial K(p)}{\partial p_\mu}.
\end{aligned}
\tag{68.23}
$$

第二行来自任意小$k$方向上的一次系数相等。
如果一开始就把两外腿取在壳并令$k=0$，原差分式只剩$0=0$，
所以取导数必须在这一步之前完成。

现在把单位极点留数怎样进入导数写明。
在宇称不变真空中，逆核可由两个标量函数$A(s),B(s)$表示，其中$s=p^2$。
用$\slashed p^{\,2}=-s$求逆，并令下标0表示$s=-m^2$，有
<span id="eq:c68-onshell-inverse-expansion"></span>

$$
\begin{aligned}
K(p)&=A(s)\slashed p+B(s),\\
\widetilde S(p)&=\frac{-A(s)\slashed p+B(s)}{F(s)},
 \qquad F(s)=sA(s)^2+B(s)^2,\\
B_0&=mA_0,\qquad
F'_0=A_0[A_0+2m(B'_0-mA'_0)],\\
r_0&=\frac{A_0}{F'_0}
    =\frac1{A_0+2m(B'_0-mA'_0)}=1 .
\end{aligned}
\tag{68.24}
$$

第三行前式来自$K(p)u(p)=0$；后式对$F$直接求导，
再代入$B_0=mA_0$。极点附近，分子成为$A_0(-\slashed p+m)$，
分母成为$F'_0(s+m^2)$，所以最后一行的$r_0$正是与自由分子相比的留数。
OS条件将它规定为1。这里$A_0$从微扰的单位值展开，所作约分成立。
这与第62节的$\Sigma(-m)=0$、$\Sigma'(-m)=0$给出同一归一。
单位留数约束的是逆核在物理支附近的一次展开，传播子本身仍具有上式所示的极点。

对于相同的外动量，克利福德关系和两端在壳方程给
$\bar u\{\gamma^\mu,\slashed p\}u=-2p^\mu\bar uu
=-2m\bar u\gamma^\mu u$，即
$p^\mu\bar uu=m\bar u\gamma^\mu u$。
先按乘积法则求导，再使用这一关系，得到
<span id="eq:c68-onshell-inverse-derivative"></span>

$$
\begin{aligned}
\frac{\partial K}{\partial p_\mu}
 &=A\gamma^\mu+2p^\mu(A'\slashed p+B'),\\
\bar u\frac{\partial K}{\partial p_\mu}u
 &=[A_0+2m(B'_0-mA'_0)]\,\bar u\gamma^\mu u\\
 &=\bar u\gamma^\mu u .
\end{aligned}
\tag{68.25}
$$

第二行中先用$\slashed p\,u=-mu$消去一次斜杠，
第三行再用式[（68.24）](#eq:c68-onshell-inverse-expansion)的单位留数。
因此式[（68.23）](#eq:c68-zero-transfer-derivative)在物理旋量之间成为
<span id="eq:c68-onshell-vertex-projection"></span>

$$
\bar u V^\mu(p,p)u
=\mathfrak e\,\bar u\frac{\partial K}{\partial p_\mu}u
=\mathfrak e\,\bar u\gamma^\mu u.
\tag{68.26}
$$

第63节的物理电荷条件$F_1(0)=1$则规定同一个矩阵元为
$e\bar u\gamma^\mu u$。取其非零分量比较，就有
<span id="eq:c68-os-equality"></span>

$$
\mathfrak e=e,\qquad Z_1=Z_2\qquad\text{在OS方案中}.
\tag{68.27}
$$

这里用到的是零转移的物理投影。第63节的泡利项正比于转移动量，
在这一点不参与归一；它在非零转移和磁矩响应中仍然存在。
两个$Z$在去掉红外调节时可以含相同的奇性，
上述证明始终按同一调节下的恒等式取极限。

<span id="c68-covariant-scalar"></span>

## 协变导数与标量理论

当$Z_1=Z_2$时，拉格朗日量的动能项与电磁相互作用项可以合为
<span id="eq:c68-covariant-kinetic-term"></span>

$$
\begin{aligned}
iZ_2\bar\Psi\slashed\partial\Psi
 +eZ_1\bar\Psi\slashed A\Psi
 &=iZ_2\bar\Psi\slashed D\Psi,\\
D_\mu&=\partial_\mu-ieA_\mu .
\end{aligned}
\tag{68.28}
$$

同一个系数同时乘在普通导数与电磁势上。
这使动能的重整化仍保留第58节协变导数的结构。
从这里也能理解为什么电子场归一与顶角归一不能各自任意改变：
普通导数对局域相位产生的附加项，需要电磁势的变换以完全相同的系数抵消。

不过，量子计算使用的路径积分已经固定了规范。
应说明经典作用量的这一结构怎样传递到量子核。
[第63节](/posts/srednicki-63/#c63-gauge-constraint)已经保留费米源次序推导了这一步：
将规范固定和所用二次红外项记为$S_{\rm br}$，
作联合变换$A\mapsto A-\partial\chi$、
$\Psi\mapsto e^{-i\mathfrak e\chi}\Psi$及伴随变换。
矢量相位的两个贝雷津 雅可比行列式相消，
而$\delta S_{\rm br}$对场是线性的，取期望值即可换成平均场。
因此源变元恒等式经勒让德变换给
<span id="eq:c68-gauge-fixed-effective-action"></span>

$$
\delta\Gamma=\delta S_{\rm br},\qquad
\widehat\Gamma:=\Gamma-S_{\rm br},\qquad
\delta\widehat\Gamma=0.
\tag{68.29}
$$

在$Z_1,Z_2$尚未相等时，这里应取$\mathfrak e=eZ_1/Z_2$；
它恰好使含反项的狄拉克动能与电磁项相容。
从$\widehat\Gamma$抽出一对费米平均场得到的逆核，因而满足
<span id="eq:c68-proper-kernel-covariance"></span>

$$
\begin{aligned}
\widehat\Gamma\big|_{\bar\psi\psi}
 &=-\int d^4y\,d^4z\,\bar\psi(y)\mathcal K[A](y,z)\psi(z),\\
\mathcal K[A-\partial\chi](y,z)
 &=e^{-i\mathfrak e\chi(y)}
       \mathcal K[A](y,z)e^{+i\mathfrak e\chi(z)} .
\end{aligned}
\tag{68.30}
$$

把核的一次背景项写成$-V^\mu A_\mu$，并用
$\delta A_\mu(k)=-ik_\mu\chi(k)$，左边给$ik_\mu V^\mu\chi$。
右边的出端相位给$-i\mathfrak e K(p)\chi$，
入端相位给$+i\mathfrak e K(p')\chi$，
又得到式[（68.19）](#eq:c68-proper-ward)。
这个核推导与前面的流三点推导具有同一量子起点，
同时说明规范固定的已知变分应放在哪里。

最后转向标量电动力学。先写出流与逆核的关系，再展开双光子顶角的纵向收缩。沿第61节的电荷约定，
$J^\mu=-ieZ_2\varphi^\dagger\overleftrightarrow{\partial^\mu}\varphi
-2e^2Z_1A^\mu\varphi^\dagger\varphi$。
其中含$A^\mu$的部分与双光子顶角一起保留。
在[第65节的规范相容条件](/posts/srednicki-65/#c65-finite-gauge)$Z_4=Z_1^2/Z_2$下，
光子源仍为$(Z_1/Z_2)J^\mu$，联合相位系数仍是$\mathfrak e$。
对标量逆核应用式[（68.30）](#eq:c68-proper-kernel-covariance)的同类变换，给
<span id="eq:c68-scalar-ward"></span>

$$
\begin{aligned}
K_\varphi(p^2)&=\widetilde\Delta(p)^{-1}
              =p^2+m^2-\Pi_\varphi(p^2),\\
(p'-p)_\mu V_3^\mu(p',p)
 &=\mathfrak e[K_\varphi(p'^2)-K_\varphi(p^2)].
\end{aligned}
\tag{68.31}
$$

标量三点顶角的质量量纲为1，所以这里两边的质量量纲都是2。
离壳有限性与纯极部减除再次给出MS方案中的$Z_1/Z_2=1$。
OS方案则先在离壳关系中对$p'-p$求一次系数，再取质量壳：
<span id="eq:c68-scalar-onshell-normalization"></span>

$$
V_3^\mu(p,p)=2\mathfrak e p^\mu K_\varphi'(p^2)
 \ \xrightarrow[\ K_\varphi'(-m^2)=1\ ]{p^2=-m^2}\
 2\mathfrak e p^\mu=2ep^\mu .
\tag{68.32}
$$

最后一个等号是同一光子归一及单位标量留数下的物理电荷条件。
于是两种方案都给$\mathfrak e=e$；再用三点与双光子耦合的相容关系，
得到标量理论的重整化关系：
<span id="eq:c68-scalar-z-equality"></span>

$$
Z_1=Z_2,\qquad Z_4=\frac{Z_1^2}{Z_2}=Z_2 .
\tag{68.33}
$$

再对背景光子取一次系数，就能把双光子顶角的纵向收缩写成两个移位三点顶角之差。
同一局域电荷也约束标量的四点接触项。
这些关系给出了后续圈计算必须满足的结构条件；
有限转移处的形状因子仍须由相应图的计算确定。

<span id="c68-one-loop-check"></span>

## 一圈顶角与自能的完整差分

取光子入动量$k=p'-p$。
第62节的自由费米核记作$S_{\rm f}$，逆核为
$K_{\rm f}(r)=\slashed r+m$。
在内部传播子无极点的复动量域，有
<span id="eq:c68-ex-2-free-kernel-difference"></span>

$$
\begin{aligned}
S'&=S_{\rm f}(p'+\ell),\qquad S=S_{\rm f}(p+\ell),\\
\slashed k&=(S')^{-1}-S^{-1},\\
S'\slashed kS
&=S'\bigl[(S')^{-1}-S^{-1}\bigr]S=S-S'.
\end{aligned}
\tag{68.34}
$$

这里始终保留从出电子端到入电子端的矩阵次序。
比较完成后取共同的费曼边界；光子红外调节也在两个积分中保持相同。

为显示整体$i$和有限部分的关系，写出两种未加反项的圈图。
沿$d=4-\varepsilon$并提出外顶角公共的
$\widetilde\mu^{\varepsilon/2}$，记
$\int_\ell=\int d^d\ell/(2\pi)^d$，它们是
<span id="eq:c68-ex-2-one-loop-integrals"></span>

$$
\begin{aligned}
i\Sigma_{\rm loop}(p)
&=e^2\widetilde\mu^\varepsilon\int_\ell
 \gamma^\rho S_{\rm f}(p+\ell)\gamma^\nu
 \Delta_{{\rm f},\nu\rho}(\ell),\\
iV_{\rm loop}^\mu(p',p)
&=e^3\widetilde\mu^\varepsilon\int_\ell
 \gamma^\rho S_{\rm f}(p'+\ell)\gamma^\mu
 S_{\rm f}(p+\ell)\gamma^\nu
 \Delta_{{\rm f},\nu\rho}(\ell).
\end{aligned}
\tag{68.35}
$$

自能中两个顶角与两条内线给
$(ie)^2(1/i)^2=e^2$；
顶角图中三个顶角与三条内线给
$(ie)^3(1/i)^3=e^3$。
两式都沿[第62节](/posts/srednicki-62/#c62-vertex)的内线规则，因而可以直接比较。
将式[（68.34）](#eq:c68-ex-2-free-kernel-difference)放入第二个积分，
其余两端矩阵、光子核、测度全部相同，因此
<span id="eq:c68-ex-2-loop-ward"></span>

$$
k_\mu V_{\rm loop}^\mu(p',p)
=e\,[\Sigma_{\rm loop}(p)-\Sigma_{\rm loop}(p')] .
\tag{68.36}
$$

两项保持同一个圈动量路由，因此恒等式对整个调节积分成立，包含极部及有限部分。

现在加入任意指定方案的局部反项：
<span id="eq:c68-ex-2-counterterms"></span>

$$
\begin{aligned}
\Sigma_{\rm R}(p)
&=\Sigma_{\rm loop}(p)-\delta Z_2\slashed p-\delta Z_m m+O(e^4),\\
K_{\rm R}(p)\equiv\widetilde S_{\rm R}(p)^{-1}
&=\slashed p+m-\Sigma_{\rm R}(p),\\
V_{\rm R}^\mu(p',p)
&=e(1+\delta Z_1)\gamma^\mu+V_{\rm loop}^\mu(p',p)+O(e^5).
\end{aligned}
\tag{68.37}
$$

质量反项在$K_{\rm R}(p')-K_{\rm R}(p)$中相减为零，
动能反项则留下$\delta Z_2\slashed k$。
用上面的圈恒等式逐项相减，得到
<span id="eq:c68-ex-2-renormalized-ward"></span>

$$
\begin{aligned}
k_\mu V_{\rm R}^\mu
-e[K_{\rm R}(p')-K_{\rm R}(p)]
&=e(\delta Z_1-\delta Z_2)\slashed k+O(e^5)\\
&=0+O(e^5),\qquad \delta Z_1=\delta Z_2 .
\end{aligned}
\tag{68.38}
$$

这就是$Z_1=Z_2$时精确关系[（68.19）](#eq:c68-proper-ward)的一圈展开。
条件要求两个反项连同有限部分相等。有限重定义也要保持这个相等关系。
证明没有要求外电子在壳，所以适用于一般离壳$p,p'$。

零转移动量也应从这个离壳差分取极限。
保持红外调节，令$p'=p+k$并比较$k$的一次系数，可得
<span id="eq:c68-ex-2-zero-transfer"></span>

$$
\begin{aligned}
V_{{\rm loop}}^\mu(p,p)
&=-e\,\frac{\partial\Sigma_{\rm loop}(p)}{\partial p_\mu},\\
V_{\rm R}^\mu(p,p)
&=e\,\frac{\partial K_{\rm R}(p)}{\partial p_\mu}+O(e^5).
\end{aligned}
\tag{68.39}
$$

一次系数保留了零转移顶角的信息。

<span id="c68-scalar-contacts"></span>

## 标量流的两个端点与双光子顶角

[第67节](/posts/srednicki-67/#eq:c67-scalar-current-normalization)已经从局域相位求出含$A^\mu$的标量诺特流。把局域变元用于标量流三点函数，两个标量插入分别带电荷$e$和$-e$，故
<span id="eq:c68-ex-3-current-ward"></span>

$$
-\partial_{x\mu}
 \langle{\rm T}J^\mu(x)\varphi(y)\varphi^\dagger(z)\rangle
=e[\delta^4(x-y)-\delta^4(x-z)]
 \langle{\rm T}\varphi(y)\varphi^\dagger(z)\rangle .
\tag{68.40}
$$

为看到傅里叶变换的次序，定义
<span id="eq:c68-ex-3-current-fourier"></span>

$$
\begin{aligned}
\mathcal C^\mu(k;p',p)
&=i\frac{Z_1}{Z_2}\int d^4x\,d^4y\,d^4z\,
 e^{ikx-ip'y+ipz}\\
&\qquad\times
 \langle{\rm T}J^\mu(x)\varphi(y)\varphi^\dagger(z)\rangle_c,\\
k_\mu\mathcal C^\mu
&=-i\mathfrak e\,(2\pi)^4\delta^4(k+p-p')
 \bigl[\widetilde\Delta(p)-\widetilde\Delta(p')\bigr].
\end{aligned}
\tag{68.41}
$$

这里$\mathfrak e:=eZ_1/Z_2$。
分部积分把左侧的$-\partial_x$变为$+ik$；
右侧$x=y$的接触项留下动量$p$的二点函数，
$x=z$的接触项留下动量$p'$的二点函数。
再用$\langle{\rm T}\varphi\varphi^\dagger\rangle$的动量核
$\widetilde\Delta/i$，便得到第二行。

完整流三点还含光子可约部分；勒让德变换从量子作用量中取出1PI核，将同一个局域变元恒等式变为式[（68.31）](#eq:c68-scalar-ward)。这一标量源推导见[第65节](/posts/srednicki-65/#c65-ward-identities)。

再加入第四个插入$A^\nu(w)$。
在只改变带电标量的局域变元中，$A^\nu$不变，
所以流沃德恒等式仍只有两个带电端点的接触项：
<span id="eq:c68-ex-3-four-current-ward"></span>

$$
\begin{aligned}
-\partial_{x\mu}
 \langle{\rm T}J^\mu(x)A^\nu(w)
               \varphi(y)\varphi^\dagger(z)\rangle
={}&e[\delta^4(x-y)-\delta^4(x-z)]\\
&\times\langle{\rm T}A^\nu(w)
               \varphi(y)\varphi^\dagger(z)\rangle .
\end{aligned}
\tag{68.42}
$$

流中的$A^\mu\varphi^\dagger\varphi$项必须保留；
它所含的局部双光子顶角正是下面四点关系的一部分。
对同一个量子作用量取1PI系数，等价于将背景核多展开一阶。

总转移为$q=p'-p$，把指标$\mu$处的光子入动量记作$k$，
另一光子的入动量便为$q-k$。相应展开为
<span id="eq:c68-ex-3-two-photon-expansion"></span>

$$
\begin{aligned}
\mathcal K[A](p',p)
={}&(2\pi)^4\delta^4(q)K(p^2)-V_3^\nu(p',p)A_\nu(q)\\
&-\frac12\int\frac{d^4k}{(2\pi)^4}
 V_4^{\mu\nu}(k,p',p)A_\mu(k)A_\nu(q-k)+O(A^3).
\end{aligned}
\tag{68.43}
$$

由于两个光子相同，二次项带$1/2!$。
对它的两个位置分别作$\delta A=-\partial\chi$，
两份相等的变分正好消去这个$1/2$。
在式[（68.30）](#eq:c68-proper-kernel-covariance)的标量版本中比较两端的
$\chi(k)A_\nu(q-k)$系数，有
<span id="eq:c68-ex-3-two-endpoint-shifts"></span>

$$
\begin{aligned}
\delta\mathcal K\big|_{\chi A}
&=ik_\mu V_4^{\mu\nu}(k,p',p)
      \chi(k)A_\nu(q-k),\\
\delta\mathcal K\big|_{\chi A}
&=i\mathfrak e\,
 \bigl[V_3^\nu(p'-k,p)-V_3^\nu(p',p+k)\bigr]
      \chi(k)A_\nu(q-k).
\end{aligned}
\tag{68.44}
$$

第二行的第一项来自出端的$-i\mathfrak e\chi(x)$
乘核内的$-V_3A$，所以为正号，并把出端动量移到$p'-k$；
第二项来自入端的$+i\mathfrak e\chi(y)$，所以为负号，
把入端动量移到$p+k$。这两个移位各自都使剩余光子的动量为$q-k$。
利用$\mathfrak e=eZ_1/Z_2=eZ_4/Z_1$，最终得到
<span id="eq:c68-ex-3-four-ward"></span>

$$
k_\mu V_4^{\mu\nu}(k,p',p)
=\frac{Z_4}{Z_1}e
 \bigl[V_3^\nu(p'-k,p)-V_3^\nu(p',p+k)\bigr].
\tag{68.45}
$$

差分次序由核的出、入两个端点固定。
例如未先令$Z_i$相等的树核给
<span id="eq:c68-ex-3-tree-sign"></span>

$$
\begin{aligned}
V_{3,\mathrm{tree}}^\nu(p',p)&=eZ_1(p'+p)^\nu,&
V_{4,\mathrm{tree}}^{\mu\nu}&=-2e^2Z_4g^{\mu\nu},\\
\frac{Z_4}{Z_1}e\,
 \bigl[V_{3,\mathrm{tree}}^\nu(p'-k,p)
      -V_{3,\mathrm{tree}}^\nu(p',p+k)\bigr]
&=-2e^2Z_4k^\nu
 =k_\mu V_{4,\mathrm{tree}}^{\mu\nu}.
\end{aligned}
\tag{68.46}
$$

一般圈修正改变三点和四点的动量函数，仍须保持同一差分。
在上述两种减除方案中，前面的$eZ_4/Z_1$进一步成为相应方案的$e$：
OS中它由零转移物理条件固定，$\overline{\mathrm{MS}}$中它为该方案的运行电荷。

[第74节](/posts/srednicki-74/#c74)将从BRST对称性进一步说明规范固定后的量子约束。

---

[← 第 67 节](/posts/srednicki-67/) · [章节地图](/srednicki/) · [第 69 节 →](/posts/srednicki-69/)
