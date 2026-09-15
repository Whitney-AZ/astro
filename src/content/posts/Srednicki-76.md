---
title: 'Srednicki §76 整体对称性中的反常'
date: 2026-09-14
category: 笔记
tags: [物理, 量子场论, Srednicki]
series: 'Srednicki QFT'
srednickiSections: [76]
hideFromHome: true
draft: false
---

<span id="c76"></span>

上一节的困难发生在规范流上：如果纵向规范模式不能退耦，建立物理态空间所需的恒等式就会受到破坏。不过，一个规范理论还可能具有别的对称性。它们只涉及常参数变换，相应流也不与独立的规范场耦合。这些整体对称性在量子论中失效，可以产生新的物理效应。本节研究最简单的例子：无质量狄拉克场的轴向对称性。这一结果将在[第90节](/posts/srednicki-90/#c90)的强子衰变中再次出现。

推导将复用[第75节](/posts/srednicki-75/#c75)已经算出的三角图。这里“整体对称性中的反常”指常参数对称性对应的流不守恒，含义不同于上一节由大规范变换引起的“整体规范反常”。以下取耦合记号$g$、度规$(-,+,+,+)$和$\epsilon^{0123}=+1$，并沿第75节的$\{\gamma^\mu,\gamma^\nu\}=-2g^{\mu\nu}$约定。

<span id="c76-symmetries"></span>

## 无质量狄拉克场的两种相位变换

取一个电荷$Q=+1$的狄拉克场，令其质量为零。拉格朗日量为
<span id="eq:c76-action"></span>

$$
\begin{gathered}
\mathcal L=i\bar\Psi\gamma^\mu D_\mu\Psi
 -\frac14F^{\mu\nu}F_{\mu\nu},\\
D_\mu=\partial_\mu-igA_\mu,\qquad
F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu .
\end{gathered}
\tag{76.1}
$$

单个U(1)理论只有一个规范场，无需另列内部生成元指标。在四维，$\Psi,A_\mu,F_{\mu\nu}$的质量维数分别为$3/2,1,2$，$g$无量纲。用$g$而不用前面电子的电荷$e$，是因为这里先把这个理论作为研究对称性的例子。

为了看清两个独立的相位，按第36节把狄拉克场写成两个左手外尔场。它们的规范电荷相反：
<span id="eq:c76-two-left-fields"></span>

$$
\begin{gathered}
\Psi=\begin{pmatrix}\chi\\ \xi^\dagger\end{pmatrix},
\qquad Q_\chi=+1,\qquad Q_\xi=-1,\\
\mathcal L=
i\chi^\dagger\bar\sigma^\mu(\partial_\mu-igA_\mu)\chi
+i\xi^\dagger\bar\sigma^\mu(\partial_\mu+igA_\mu)\xi
-\frac14F^{\mu\nu}F_{\mu\nu}.
\end{gathered}
\tag{76.2}
$$

第二行与四分量写法相差一个全散度。具体地，右手块给出的动能可以重排为
<span id="eq:c76-weyl-boundary"></span>

$$
\begin{aligned}
&i\xi\sigma^\mu(\partial_\mu-igA_\mu)\xi^\dagger\\
&\quad=i\xi^\dagger\bar\sigma^\mu(\partial_\mu+igA_\mu)\xi
+ \partial_\mu(i\xi\sigma^\mu\xi^\dagger).
\end{aligned}
\tag{76.3}
$$

对导数分部积分产生一个负号，再交换两个奇场产生第二个负号，因此动能的号不变；规范耦合没有分部积分的负号，所以在换序后反号。这就解释了$\xi$的相反电荷。边界项按前章的作用量边界条件处理。

熟悉的局域规范变换是
<span id="eq:c76-gauge-phases"></span>

$$
\begin{aligned}
\Psi(x)&\longmapsto e^{-ig\Gamma(x)}\Psi(x),
&\bar\Psi(x)&\longmapsto\bar\Psi(x)e^{+ig\Gamma(x)},\\
A_\mu(x)&\longmapsto A_\mu(x)-\partial_\mu\Gamma(x),\\
\chi(x)&\longmapsto e^{-ig\Gamma(x)}\chi(x),
&\xi(x)&\longmapsto e^{+ig\Gamma(x)}\xi(x).
\end{aligned}
\tag{76.4}
$$

它使两个外尔场获得相反相位。规范势的变换恰好消去导数作用在相位上所给出的项：
<span id="eq:c76-covariant-transformation"></span>

$$
\begin{aligned}
D'_\mu\Psi'
 &=\bigl[\partial_\mu-ig(A_\mu-\partial_\mu\Gamma)\bigr]
             e^{-ig\Gamma}\Psi\\
 &=e^{-ig\Gamma}\bigl[-ig(\partial_\mu\Gamma)\Psi
       +\partial_\mu\Psi-igA_\mu\Psi
       +ig(\partial_\mu\Gamma)\Psi\bigr]\\
 &=e^{-ig\Gamma}D_\mu\Psi .
\end{aligned}
\tag{76.5}
$$

这里第二行只是把第一行展开；$F_{\mu\nu}$则因两个混合偏导相消而不变。因此拉格朗日量保持不变。

没有质量项时，还可以让两个左手场获得相同的常相位，而保持$A_\mu$不变：
<span id="eq:c76-axial-phases"></span>

$$
\begin{gathered}
\chi\longmapsto e^{i\alpha}\chi,\qquad
\xi\longmapsto e^{i\alpha}\xi,\qquad
\alpha=\text{常数},\\
\gamma_5=\begin{pmatrix}-\mathbf1_2&0\\0&\mathbf1_2\end{pmatrix},
\qquad
\Psi\longmapsto e^{-i\alpha\gamma_5}\Psi .
\end{gathered}
\tag{76.6}
$$

因为$\xi^\dagger$的相位是$e^{-i\alpha}$，四分量场的上下两个块正好具有相反相位。这是轴向变换。用$\bar\Psi=\Psi^\dagger\gamma^0$求出伴随场的变换：
<span id="eq:c76-axial-adjoint"></span>

$$
\begin{aligned}
\bar\Psi'
 &=\Psi^\dagger e^{i\alpha\gamma_5}\gamma^0
  =\bar\Psi\gamma^0 e^{i\alpha\gamma_5}\gamma^0
  =\bar\Psi e^{-i\alpha\gamma_5},\\
e^{-i\alpha\gamma_5}\gamma^\mu
 &=\gamma^\mu e^{i\alpha\gamma_5}.
\end{aligned}
\tag{76.7}
$$

这里用了$(\gamma^0)^2=1$和$\{\gamma_5,\gamma^\mu\}=0$。正是第二个恒等式，使动能与规范耦合中的两个轴相位相消。因此$\Psi$与$\bar\Psi$的两个轴相位指数须取同号。

<span id="c76-axial-current"></span>

## 轴流及其经典守恒

求这个对称性的诺特流时，暂把$\alpha$换成位置函数。动能中只有导数作用于$\alpha$的部分不再相消，因而
<span id="eq:c76-noether-axial"></span>

$$
\begin{aligned}
\delta_\alpha\mathcal L
 &=i\bar\Psi\gamma^\mu[-i(\partial_\mu\alpha)\gamma_5\Psi]
   =(\partial_\mu\alpha)j_A^\mu,\\
j_A^\mu&:=\bar\Psi\gamma^\mu\gamma_5\Psi .
\end{aligned}
\tag{76.8}
$$

这一局域变分固定了轴流的整体号。把变分作用量分部积分，得到$-\int d^4x\,\alpha\,\partial_\mu j_A^\mu$；在经典场方程成立且$\alpha$紧支撑时，变分作用量为零，所以轴流守恒。

同时记与规范耦合有关的向量流为$j^\mu$。四分量矩阵相乘后，右手块出现$\xi\sigma^\mu\xi^\dagger$；按第35节的指标约定交换两个奇场，它等于$-\xi^\dagger\bar\sigma^\mu\xi$。于是两个流可写成
<span id="eq:c76-vector-axial-currents"></span>

$$
\begin{aligned}
j_\chi^\mu&=\chi^\dagger\bar\sigma^\mu\chi,\qquad
j_\xi^\mu=\xi^\dagger\bar\sigma^\mu\xi,\\
j^\mu:=\bar\Psi\gamma^\mu\Psi&=j_\chi^\mu-j_\xi^\mu,
\qquad\mathcal L_{\rm int}=gA_\mu j^\mu,\\
j_A^\mu&=-j_\chi^\mu-j_\xi^\mu .
\end{aligned}
\tag{76.9}
$$

这些双线性使用相同的正规序或局域复合场定义。向量流中两个电荷相减，轴流中两个左手场则同号相加。上一节的规范三次迹于是为$1^3+(-1)^3=0$；带一个轴流和两个向量流的三角图却具有$(-1)(+1)^2+(-1)(-1)^2=-2$的内部权重。向量规范对称性与轴向整体对称性，因而可以有不同的量子行为。

经典守恒也可以直接用狄拉克方程检查。令$D_\mu\bar\Psi=\partial_\mu\bar\Psi+igA_\mu\bar\Psi$；双线性中两个规范势项相消，所以
<span id="eq:c76-classical-divergence"></span>

$$
\begin{aligned}
\partial_\mu j_A^\mu
 &=(D_\mu\bar\Psi)\gamma^\mu\gamma_5\Psi
   +\bar\Psi\gamma^\mu\gamma_5D_\mu\Psi\\
 &=(D_\mu\bar\Psi)\gamma^\mu\gamma_5\Psi
   -\bar\Psi\gamma_5\gamma^\mu D_\mu\Psi=0
 \qquad(m=0,\ \text{经典场方程}).
\end{aligned}
\tag{76.10}
$$

若加入$-m\bar\Psi\Psi$，它在轴变换下产生$2im\alpha\bar\Psi\gamma_5\Psi$，相应地$\partial_\mu j_A^\mu=2im\bar\Psi\gamma_5\Psi$。因此本节取无质量，正是为了分开质量造成的显式破缺与量子反常。

轴流的名称还反映它的宇称性质。沿第40节的宇称作用，记$\mathsf P^\mu{}_\nu=\operatorname{diag}(1,-1,-1,-1)$。场的常相位在双线性中相消，而
<span id="eq:c76-axial-parity"></span>

$$
\begin{aligned}
\gamma^0\gamma^\mu\gamma_5\gamma^0
 &=-\mathsf P^\mu{}_\nu\gamma^\nu\gamma_5,\\
P^{-1}j_A^0(t,\mathbf x)P&=-j_A^0(t,-\mathbf x),\\
P^{-1}j_A^i(t,\mathbf x)P&=+j_A^i(t,-\mathbf x).
\end{aligned}
\tag{76.11}
$$

普通矢量的空间部分在宇称下反号，轴矢量则为时间分量奇、空间分量偶。它的散度是赝标量，随后出现的$\epsilon FF$也有这一宇称。

量子轴流的散度能否包含一个由两个场强组成的项？可以先计算轴流在真空与双光子态之间的矩阵元，再与场强乘积相比较，以判断这一项及其系数。这样既用到了上一节的三角图，也给出了这个局域表达式的直接物理含义。

<span id="c76-current-correlator"></span>

## 用流三点函数计算双光子矩阵元

设两个出射光子的动量为$p,q$，偏振为$\varepsilon_\mu,\varepsilon'_\nu$。沿第55、56节，偏振定义为场展开中产生部分的系数，故单光子矩阵元为$\langle p,\lambda|A_\mu(x)|0\rangle=\varepsilon_\mu e^{-ipx}$。在取外腿物理边界时，$p^2=q^2=0$，且$p\cdot\varepsilon=q\cdot\varepsilon'=0$。螺旋度标签以下省去。

定义连通的流三点函数
<span id="eq:c76-three-current"></span>

$$
\begin{gathered}
G^{\mu\nu\rho}(x,y,z)
=\langle0|Tj^\mu(x)j^\nu(y)j_A^\rho(z)|0\rangle_c,\\
G=G_0+O(g^2).
\end{gathered}
\tag{76.12}
$$

$G_0$由自由狄拉克场收缩得到。三个流各含两个费米场，把它们连起来便形成一圈；这一圈本身没有规范耦合因子，因为流的定义中没有$g$。两个外光子则要经由$gA_\mu j^\mu$与这条圈相连。

按[第67节的外光子约化](/posts/srednicki-67/#c67-photon-current)，每条出光子腿给一个$ig$、一个偏振和一个负指数的傅里叶积分。也可以直接在相互作用展开中看出其组合因子：二阶项带$(ig)^2/2!$，两个带固定标签的外光子可分别接到两个相互作用点，有$2!$种接法；二者相消。外传播子被LSZ逆核消去后，最低阶矩阵元为
<span id="eq:c76-lsz-current"></span>

$$
\begin{aligned}
M^\rho(z)&:=\langle p,q|j_A^\rho(z)|0\rangle\\
&=(ig)^2\varepsilon_\mu\varepsilon'_\nu
\int d^4x\,d^4y\,e^{-i(px+qy)}
 G_0^{\mu\nu\rho}(x,y,z)+O(g^4).
\end{aligned}
\tag{76.13}
$$

本节计算到$g^2$阶；光子外腿重叠的$O(g^2)$修正和流核中的内光子交换，都会从矩阵元的$g^4$阶才开始贡献。为求反常的局域紫外系数，仍先采用上一节的非例外外动量或共同红外调节，再取上述外腿边界。

如果两个诺特流的经典守恒关系都能直接用于这个三点函数，三个流端的散度就都应为零。通常的沃德推导还会对其他插入作变分，但这里两个流在两种相位变换下都不变。向量相位在双线性两端直接相消；对轴相位，具体有
<span id="eq:c76-current-invariance"></span>

$$
\begin{aligned}
\delta_\alpha j^\mu
 &=-i\alpha\bar\Psi
   (\gamma_5\gamma^\mu+\gamma^\mu\gamma_5)\Psi=0,\\
\delta_\alpha j_A^\mu
 &=-i\alpha\bar\Psi
   (\gamma_5\gamma^\mu\gamma_5+\gamma^\mu)\Psi=0.
\end{aligned}
\tag{76.14}
$$

因此，由其他流插入的变分产生的接触项为零。经典预期是
<span id="eq:c76-classical-ward-expectation"></span>

$$
\begin{gathered}
\partial_{x^\mu}G^{\mu\nu\rho}=0,\qquad
\partial_{y^\nu}G^{\mu\nu\rho}=0,\qquad
\partial_{z^\rho}G^{\mu\nu\rho}=0,\\
\partial_{z^\rho}M^\rho(z)=0
\qquad\text{（三条流沃德式均成立时）}.
\end{gathered}
\tag{76.15}
$$

量子三流乘积在点重合处还需要重整化，三角图的有限局域项将决定这三条沃德式的散度。

为使用上一节的结果，对三个插入位置作傅里叶变换。取三个动量都流出，定义
<span id="eq:c76-fourier-kernel"></span>

$$
\begin{aligned}
&(2\pi)^4\delta^4(p+q+r)\,C^{\mu\nu\rho}(p,q,r)\\
&\qquad=\int d^4x\,d^4y\,d^4z\,
 e^{-i(px+qy+rz)}G^{\mu\nu\rho}(x,y,z),\\
&C=C_0+O(g^2).
\end{aligned}
\tag{76.16}
$$

$x,y,z$处的三个流分别携带自由指标$\mu,\nu,\rho$。$p,\mu$和$q,\nu$对应两个向量流，$r,\rho$对应轴流。

总动量$\delta$来自共同平移三个插入点。由真空平移不变性，$G(x,y,z)=G(x-z,y-z,0)$。令$X=x-z,Y=y-z$，雅可比因子为1；三个位置积分中的共同$z$积分就是$\int d^4z\,e^{-i(p+q+r)z}=(2\pi)^4\delta^4(p+q+r)$。如果像矩阵元中那样保持$z$不积分，则
<span id="eq:c76-fixed-insertion-transform"></span>

$$
\begin{aligned}
&\int d^4x\,d^4y\,e^{-i(px+qy)}
 G_0^{\mu\nu\rho}(x,y,z)\\
&\quad=e^{-i(p+q)z}
 \int d^4X\,d^4Y\,e^{-i(pX+qY)}
 G_0^{\mu\nu\rho}(X,Y,0)\\
&\quad=\left.C_0^{\mu\nu\rho}(p,q,r)e^{irz}\right|_{r=-p-q}.
\end{aligned}
\tag{76.17}
$$

定义中的总$\delta$已经提出，所以最后一行没有额外的$(2\pi)^4$。代回约化式，便得到本阶矩阵元及其散度：
<span id="eq:c76-matrix-from-kernel"></span>

$$
\begin{aligned}
M^\rho(z)
 &=-g^2\varepsilon_\mu\varepsilon'_\nu
  C_0^{\mu\nu\rho}(p,q,r)e^{irz}\big|_{r=-p-q}
  +O(g^4),\\
\langle p,q|\partial_\rho j_A^\rho(z)|0\rangle
 &=-ig^2\varepsilon_\mu\varepsilon'_\nu
 r_\rho C_0^{\mu\nu\rho}(p,q,r)e^{irz}\big|_{r=-p-q}
 +O(g^4).
\end{aligned}
\tag{76.18}
$$

第一行的负号来自$(ig)^2$，第二行的$i$来自对$e^{irz}$求导。轴流是局域算符插入，$r=-p-q$不受单光子的质量壳条件限制。

同样，对坐标沃德式分部积分，$\partial_{x^\mu}$给$ip_\mu$，另两项给$iq_\nu,ir_\rho$。于是经典守恒所要求的三个动量空间恒等式为
<span id="eq:c76-momentum-ward-targets"></span>

$$
p_\mu C^{\mu\nu\rho}=0,\qquad
q_\nu C^{\mu\nu\rho}=0,\qquad
r_\rho C^{\mu\nu\rho}=0 .
\tag{76.19}
$$

轴流散度的问题已经归结为最后一个收缩。现在可以回到上一节的两张三角图。

<span id="c76-triangle"></span>

## 保持两个向量流的沃德恒等式

三点函数$C_0$的两个费米定向正是[第75节的两幅三角图](/posts/srednicki-75/#fig:c75-triangles)。区别在于顶角：本节的三个插入分别为$\gamma^\mu,\gamma^\nu,\gamma^\rho\gamma_5$，上一节的三个规范顶角则各带$ig\gamma^\lambda P_L$。上一节已把三个左投影移到同一个位置，并利用$P_L^2=P_L$合并。在两个定向之和中，不含$\gamma_5$的部分相消，因此只有$P_L$中的$-\gamma_5/2$部分留下。这个消去过程见式[（75.16）](/posts/srednicki-75/#eq:c75-reflection)。

为同时追踪传播线的负号，仍沿同一圈动量标记，记
<span id="eq:c76-triangle-integrand"></span>

$$
\begin{aligned}
\mathcal D_\ell
 &=[(\ell-p)^2-i0][\ell^2-i0][(\ell+q)^2-i0],\\
\mathcal T^{\mu\nu\rho}(\ell)
 &=\operatorname{tr}\bigl[
 (\slashed\ell-\slashed p)\gamma^\mu\slashed\ell\gamma^\nu
 (\slashed\ell+\slashed q)\gamma^\rho\gamma_5\bigr].
\end{aligned}
\tag{76.20}
$$

每条无质量狄拉克线是$S/i$，且$S=-\slashed k/(k^2-i0)$。所以一个定向的三个分子给$(-1)^3$，闭费米圈再给$-1$；三个$1/i$相乘为$i$。与上一节相比较，有
<span id="eq:c76-loop-normalization"></span>

$$
\begin{aligned}
C_{0,1}^{\mu\nu\rho}
 &=(-1)\left(\frac1i\right)^3(-1)^3
 \int\frac{d^4\ell}{(2\pi)^4}
 \frac{\mathcal T^{\mu\nu\rho}(\ell)}{\mathcal D_\ell}\\
 &=i\int\frac{d^4\ell}{(2\pi)^4}
 \frac{\mathcal T^{\mu\nu\rho}(\ell)}{\mathcal D_\ell},\\
V_{75,1}^{\mu\nu\rho}
 &=\frac{ig^3}{2}\int\frac{d^4\ell}{(2\pi)^4}
 \frac{\mathcal T^{\mu\nu\rho}(\ell)}{\mathcal D_\ell}.
\end{aligned}
\tag{76.21}
$$

两个定向的奇部分相加，所以两种核的总和满足
<span id="eq:c76-chiral-to-vva"></span>

$$
\begin{gathered}
iV_{75}^{\mu\nu\rho}
 =-\frac12(ig)^3C_0^{\mu\nu\rho}+O(g^5),\\
V_{75}^{\mu\nu\rho}
 =\frac{g^3}{2}C_0^{\mu\nu\rho}+O(g^5).
\end{gathered}
\tag{76.22}
$$

右端的$C_0$从$g^0$开始，左端顶角从$g^3$开始；这正是两边圈图相同而顶角因子不同所要求的阶数。

上一节用$a=c(p-q)$描述共同的圈动量选线改变，并算出了三个收缩。将其式[（75.32）](/posts/srednicki-75/#eq:c75-routing-ward)除以$g^3/2$，得到
<span id="eq:c76-routing-wards"></span>

$$
\begin{aligned}
p_\mu C_0^{\mu\nu\rho}
 &=-\frac{i}{4\pi^2}(1-c)
    \epsilon^{\nu\rho\alpha\beta}q_\alpha r_\beta,\\
q_\nu C_0^{\mu\nu\rho}
 &=-\frac{i}{4\pi^2}(1-c)
    \epsilon^{\rho\mu\alpha\beta}r_\alpha p_\beta,\\
r_\rho C_0^{\mu\nu\rho}
 &=-\frac{i}{4\pi^2}(2c)
    \epsilon^{\mu\nu\alpha\beta}p_\alpha q_\beta .
\end{aligned}
\tag{76.23}
$$

这次必须让前两行同时为零，因为这两个流与光子耦合，它们的沃德恒等式保证光子偏振的规范部分退耦。因此取$c=1$。第三个插入是轴流，与前两个插入不同；三点函数只须在两个向量插入之间对称。所以这里的选择与上一节三个相同手征规范流所要求的$c=1/3$相容，各自对应不同的流身份。

取定$c=1$以后，向量流保持守恒，轴流则留下非零散度：
<span id="eq:c76-axial-ward-anomaly"></span>

$$
\begin{gathered}
p_\mu C^{\mu\nu\rho}=q_\nu C^{\mu\nu\rho}=0,\\
r_\rho C^{\mu\nu\rho}
 =-\frac{i}{2\pi^2}
   \epsilon^{\mu\nu\alpha\beta}p_\alpha q_\beta+O(g^2).
\end{gathered}
\tag{76.24}
$$

两个向量沃德恒等式可以由保持规范对称性的定义继续维持；第二行是本节实际求得的一圈项。改变局域三点项能够重新分配三条腿上的破缺，却不能令它们同时消失。保持规范耦合所需的两条恒等式以后，剩下的破缺就表现为轴向整体对称性的反常。

还可以把这个结论变回位置空间，以看清接触项从哪里出现。式[（76.16）](#eq:c76-fourier-kernel)中，对$z$的散度变为$ir_\rho C^{\mu\nu\rho}$；另一方面，$\partial_{x^\alpha}\delta^4(x-z)$的傅里叶积分为$ip_\alpha e^{-ipz}$。因此
<span id="eq:c76-local-contact-anomaly"></span>

$$
\partial_{z^\rho}G^{\mu\nu\rho}(x,y,z)
 =-\frac{1}{2\pi^2}\epsilon^{\mu\nu\alpha\beta}
 \partial_{x^\alpha}\delta^4(x-z)\,
 \partial_{y^\beta}\delta^4(y-z)+O(g^2).
\tag{76.25}
$$

右边两个导数各给一个$i$，使其傅里叶变换成为$+\epsilon^{\mu\nu\alpha\beta}p_\alpha q_\beta/(2\pi^2)$，恰好等于式[（76.24）](#eq:c76-axial-ward-anomaly)的$ir_\rho C$。这个量子接触分布支撑在三个流重合之处。再对$x^\mu$或$y^\nu$求散度时，对称的双导数与$\epsilon$缩并为零，仍与两个向量沃德恒等式相符。

<span id="c76-local-operator"></span>

## 场强乘积及反常的局域形式

现在将式[（76.24）](#eq:c76-axial-ward-anomaly)代回双光子矩阵元。来自位置导数的$-i$与来自三角核的$-i$相乘，给出一个负号：
<span id="eq:c76-divergence-matrix-element"></span>

$$
\begin{aligned}
\langle p,q|\partial_\rho j_A^\rho(z)|0\rangle
 &=-\frac{g^2}{2\pi^2}
 \epsilon^{\mu\nu\alpha\beta}
 p_\alpha q_\beta\varepsilon_\mu\varepsilon'_\nu
 e^{-i(p+q)z}+O(g^4).
\end{aligned}
\tag{76.26}
$$

两光子交换时，$\mu,\nu$和$\alpha,\beta$同时交换，两个负号相消。若把任一偏振换成同腿动量，反对称张量与两个相同动量缩并为零，所以结果具有外光子所需的规范不变性。

为了把这个动量结构认成场强乘积，先在自由场中写出光子态和场展开的归一。取两种物理偏振$\lambda,\lambda'$，用协变连续标签归一的态：

<span id="eq:c76-ex-states"></span>

$$
\begin{gathered}
|p,\lambda;q,\lambda'\rangle
 =a_\lambda^\dagger(\mathbf p)
  a_{\lambda'}^\dagger(\mathbf q)|0\rangle,\\
\relax[a_\lambda(\mathbf p),a_\sigma^\dagger(\mathbf k)]
 =(2\pi)^3\,2p^0\delta_{\lambda\sigma}
             \delta^3(\mathbf p-\mathbf k).
\end{gathered}
\tag{76.31}
$$

对光滑波包，这些关系给出通常的福克空间内积。在库仑规范$\varepsilon^0=0$下，

<span id="eq:c76-ex-photon-expansion"></span>

$$
A_\mu(z)=\sum_\sigma\int
 \frac{d^3k}{(2\pi)^3\,2k^0}
 \left[
  \varepsilon^*_{\sigma\mu}(k)a_\sigma(\mathbf k)e^{ikz}
 +\varepsilon_{\sigma\mu}(k)a_\sigma^\dagger(\mathbf k)e^{-ikz}
 \right].
\tag{76.32}
$$

产生部分的偏振系数是$\varepsilon_\mu$，相应湮灭部分带其复共轭。直接用对易子收缩，得到

<span id="eq:c76-ex-one-photon-overlap"></span>

$$
\begin{aligned}
\langle p,\lambda|A_\mu(z)|0\rangle
 &=\sum_\sigma\int\frac{d^3k}{(2\pi)^3\,2k^0}
   \varepsilon_{\sigma\mu}(k)e^{-ikz}
   (2\pi)^3\,2p^0\delta_{\lambda\sigma}
                     \delta^3(\mathbf p-\mathbf k)\\
 &=\varepsilon_\mu e^{-ipz}.
\end{aligned}
\tag{76.33}
$$

这样，每条模式积分中的$(2\pi)^3\,2k^0$都由外态归一约去。对产生部分的相位$e^{-ipz}$微分，便有

<span id="eq:c76-one-photon-field-strength"></span>

$$
\begin{aligned}
f_{\mu\nu}(p,\varepsilon)
 &:=p_\mu\varepsilon_\nu-p_\nu\varepsilon_\mu,\\
\langle p,\lambda|F_{\mu\nu}(z)|0\rangle
 &=-if_{\mu\nu}(p,\varepsilon)e^{-ipz}.
\end{aligned}
\tag{76.27}
$$

将式[（76.31）](#eq:c76-ex-states)中的对易子记为$\mathcal I(p,\lambda;k,\sigma)$，两次收缩给

<span id="eq:c76-ex-two-pairings"></span>

$$
\begin{aligned}
&\langle0|a_{\lambda'}(\mathbf q)a_\lambda(\mathbf p)
   a_\sigma^\dagger(\mathbf k)a_\tau^\dagger(\mathbf l)|0\rangle\\
&\quad=\mathcal I(p,\lambda;k,\sigma)
       \mathcal I(q,\lambda';l,\tau)
      +\mathcal I(p,\lambda;l,\tau)
       \mathcal I(q,\lambda';k,\sigma).
\end{aligned}
\tag{76.34}
$$

第一项把$p$配给第一个场强，第二项把$p$配给第二个场强，两个配对取玻色正号。用自由威克乘积定义同点场强，其真空减除项是单位算符，对真空到双光子的矩阵元无贡献。因此

<span id="eq:c76-two-photon-field-strength"></span>

$$
\begin{aligned}
&\langle p,q|:F_{\mu\nu}(z)F_{\rho\sigma}(z):|0\rangle\\
&\quad=-\bigl[
 f_{\mu\nu}(p,\varepsilon)f_{\rho\sigma}(q,\varepsilon')
 +f_{\mu\nu}(q,\varepsilon')f_{\rho\sigma}(p,\varepsilon)
 \bigr]e^{-i(p+q)z}.
\end{aligned}
\tag{76.28}
$$

这里的负号是 $(-i)^2$；两个配对间取玻色正号。协变外态归一给出的 $(2\pi)^3\,2\omega$ 与每条模式积分中的测度分母相消。再与列维—奇维塔张量缩并，每种配对都给出四个相等的项：

<span id="eq:c76-four-equal-terms"></span>

$$
\begin{aligned}
&\epsilon^{\mu\nu\rho\sigma}
 f_{\mu\nu}(p,\varepsilon)f_{\rho\sigma}(q,\varepsilon')\\
&=\epsilon^{\mu\nu\rho\sigma}
 \bigl(p_\mu\varepsilon_\nu q_\rho\varepsilon'_\sigma
      -p_\mu\varepsilon_\nu q_\sigma\varepsilon'_\rho\bigr)\\
&\quad+\epsilon^{\mu\nu\rho\sigma}
 \bigl(-p_\nu\varepsilon_\mu q_\rho\varepsilon'_\sigma
      +p_\nu\varepsilon_\mu q_\sigma\varepsilon'_\rho\bigr)\\
&=4\epsilon^{\mu\nu\rho\sigma}
         p_\mu\varepsilon_\nu q_\rho\varepsilon'_\sigma.
\end{aligned}
\tag{76.35}
$$

展开乘积后，在第二项交换 $\rho,\sigma$，第三项交换 $\mu,\nu$，第四项同时作这两次交换，列维—奇维塔张量的符号便把各项都变成第一项。交换整个指标对是偶置换，所以另一种光子配对贡献相同。把指标整理成三角图所用的次序，结果为
<span id="eq:c76-local-photon-matching"></span>

$$
\begin{aligned}
&\langle p,q|
 \epsilon^{\mu\nu\rho\sigma}:F_{\mu\nu}F_{\rho\sigma}:(z)
 |0\rangle\\
&\quad=-8\epsilon^{\alpha\mu\beta\nu}
 p_\alpha q_\beta\varepsilon_\mu\varepsilon'_\nu e^{-i(p+q)z}\\
&\quad=+8\epsilon^{\mu\nu\alpha\beta}
 p_\alpha q_\beta\varepsilon_\mu\varepsilon'_\nu e^{-i(p+q)z}.
\end{aligned}
\tag{76.29}
$$

数值8来自两种配对乘每个场强的两个反对称项。最后的指标置换为奇，恰好消去两次微分的负号。将这个式子乘以$-g^2/(16\pi^2)$，就得到三角图的矩阵元。

要把匹配写成局域形式，还要确定允许出现哪些密度。轴流散度的维数是4，并且是赝标量。保持向量规范不变性时，纯光子局域项应由场强和它的导数组成。两个场强已用尽维数4；其赝标量缩并只有$\epsilon^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}$。一个场强配两个导数的赝标量候选可写成$\epsilon^{\mu\nu\rho\sigma}\partial_\mu\partial_\nu F_{\rho\sigma}$，它因两个导数对称而为零；把一个导数先缩并到场强的写法也由比安基恒等式给零。因此，在保持向量沃德恒等式、以式[（76.8）](#eq:c76-noether-axial)固定轴流归一的定义下，本节确定
<span id="eq:c76-anomaly-local-coefficient"></span>

$$
\left.\partial_\mu j_A^\mu\right|_{\text{一圈局域光子项}}
 =-\frac{g^2}{16\pi^2}
  \epsilon^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}.
\tag{76.30}
$$

双光子匹配固定了这一局域项；含其他插入时的运动方程项和接触项，需要把轴流作为复合算符统一定义。[第77节](/posts/srednicki-77/#c77-ward)从费米子积分测度导出任意插入的轴向沃德恒等式，并说明反常系数的一圈精确性所采用的共同算符归一。

在无质量理论中，规范耦合保持向量流的守恒，局域场强乘积则成为轴荷变化的源。轴向整体对称性的反常由此与光子的规范沃德恒等式并存。

---

[← 第 75 节](/posts/srednicki-75/) · [章节地图](/srednicki/) · [第 77 节 →](/posts/srednicki-77/)
