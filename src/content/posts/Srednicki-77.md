---
title: 'Srednicki §77 反常与费米子路径积分'
date: 2026-09-14
category: 笔记
tags: [物理, 量子场论, Srednicki]
series: 'Srednicki QFT'
srednickiSections: [77]
hideFromHome: true
draft: false
---

<span id="c77"></span>

第76节从三角图求出了轴流的散度。计算中，保持两个向量流守恒便固定了有限的局域项，剩下的轴流反常于是成为确定的结果。不过，三角图只包含两个外部规范场。我们还要知道，在任意背景场中应当怎样写这个结果，以及更多圈图会不会改变它的系数。本节用藤川方法，从费米子路径积分出发回答这些问题。经典作用量的变换仍与上一节相同；新的内容在于，定义无穷多个费米积分变量时必须引入调节，而这个调节使轴变换的积分测度发生变化。

先计算狄拉克场的轴流，再由规范变换的一致性确定外尔场的规范反常。群论消除条件和场强密度的全导数公式都可从所得表达式逐项推出；最后再看局域条件之外的整体规范反常。

<span id="c77-background"></span>

## 从三角图到背景场

设无质量狄拉克场属于规范群的表示$R$。把规范场写成表示空间中的矩阵，就有

<span id="eq:c77-background-definitions"></span>

$$
\begin{gathered}
A_\mu=T_R^aA_\mu^a,\qquad D_\mu=\partial_\mu-igA_\mu,\\
F_{\mu\nu}
=\partial_\mu A_\nu-\partial_\nu A_\mu-ig[A_\mu,A_\nu],
\qquad [D_\mu,D_\nu]=-igF_{\mu\nu},\\
j_A^\mu=\bar\Psi\gamma^\mu\gamma_5\Psi .
\end{gathered}
\tag{77.1}
$$

由$[T^a,T^b]=if^{abc}T^c$，矩阵交换子给分量场强中的$+gf^{abc}A_\mu^bA_\nu^c$。这里的轴变换对$R$的所有分量取相同相位，因而$j_A^\mu$是规范单态。第76节的狄拉克三角图中，两个规范顶角现在各带一个生成元，轴顶角在表示空间中是单位矩阵。因此，原来的结果只需乘上$\operatorname{Tr}_R(T^aT^b)$。对于一个简单因子，采用第70节的正交归一，得到二次背景场项

<span id="eq:c77-quadratic-background"></span>

$$
\left.\partial_\mu j_A^\mu\right|_{A^2}
=-\frac{g^2T(R)}{16\pi^2}
 \epsilon^{\mu\nu\rho\sigma}
 (\partial_\mu A_\nu^a-\partial_\nu A_\mu^a)
 (\partial_\rho A_\sigma^a-\partial_\sigma A_\rho^a).
\tag{77.2}
$$

这里的方括号反对称化不含$1/2$。若规范群有多个因子，先保留$\operatorname{Tr}_R(T^aT^b)$，再按各因子的指标与耦合展开，便不会把不同的$T(R)$混在一起。

在非阿贝尔理论中，$\partial_\mu A_\nu-\partial_\nu A_\mu$本身不作协变变换。把它补成$F_{\mu\nu}$，可以得到一个规范不变、维数为四、宇称为奇的局域密度：

<span id="eq:c77-axial-target"></span>

$$
\begin{gathered}
\mathcal P[A]
=\epsilon^{\mu\nu\rho\sigma}
 \operatorname{Tr}_R(F_{\mu\nu}F_{\rho\sigma}),\qquad
\partial_\mu j_A^\mu=-\frac{g^2}{16\pi^2}\mathcal P[A],\\
\epsilon^{\mu\nu\rho\sigma}\operatorname{Tr}_R(D_\mu D_\nu F_{\rho\sigma})
=-\frac{ig}{2}\epsilon^{\mu\nu\rho\sigma}
 \operatorname{Tr}_R[F_{\mu\nu},F_{\rho\sigma}]=0.
\end{gathered}
\tag{77.3}
$$

$F\mapsto UFU^{-1}$与迹的循环性保证了这个密度的规范不变性，它的二次项也确实等于[（77.2）](#eq:c77-quadratic-background)。第二行作用于矩阵场强的导数取伴随形式$D_\mu X=\partial_\mu X-ig[A_\mu,X]$。在四维平直时空中，仅含规范背景的这一阶局域赝标量由两个场强构成；上式用反对称性取出两个协变导数的对易子，再利用交换子之迹为零，排除了含一个场强和两个导数的独立单态项。下面直接计算积分测度，既确定这一规范补全，也确定它的系数。

<span id="c77-measure"></span>

## 轴变换为什么改变积分测度

暂时把$A_\mu$固定，规范场和鬼场的积分留到最后。费米作用量是格拉斯曼变量的二次型，故其积分可以形式地写成行列式：

<span id="eq:c77-fermion-determinant"></span>

$$
\begin{aligned}
S_f[\Psi,\bar\Psi;A]&=\int d^4x\,\bar\Psi\,i\slashed D\,\Psi,\\
Z_f[A]&=\int\mathcal D\Psi\,\mathcal D\bar\Psi\,e^{iS_f}
       \ \propto\ \det(i\slashed D).
\end{aligned}
\tag{77.4}
$$

与背景无关的常数和相位可以并入归一化。对数行列式的连通背景展开是一条费米圈上任意多个规范场插入；随后对$A$积分，才把这些插入接成含规范传播子的更多圈图。这样分步积分，正好把反常发生的位置单独显露出来。有些背景使无质量狄拉克算符出现零模，此时$Z_f[A]$可能为零；可保留费米源，或先加小质量并保留第76节的经典质量散度，最后取质量零极限。以下变元恒等式本身不需要除以$Z_f[A]$。

取紧支撑的无穷小函数$\alpha(x)$，作上一节的局域轴变换

<span id="eq:c77-local-axial-transformation"></span>

$$
\delta_\alpha\Psi=-i\alpha\gamma_5\Psi,\qquad
\delta_\alpha\bar\Psi=-i\alpha\bar\Psi\gamma_5.
\tag{77.5}
$$

两个指数同号，是因为$\gamma^0$与$\gamma_5$反对易。把两项代入作用量时，不含$\partial\alpha$的部分用$\{\gamma^\mu,\gamma_5\}=0$相消，留下

<span id="eq:c77-action-variation"></span>

$$
\begin{aligned}
\delta_\alpha S_f
&=\int d^4x\,(\partial_\mu\alpha)
      \bar\Psi\gamma^\mu\gamma_5\Psi\\
&=-\int d^4x\,\alpha\,\partial_\mu j_A^\mu .
\end{aligned}
\tag{77.6}
$$

第二步的边界项由$\alpha$的紧支撑性消失。若测度也不变，变换后的积分与原积分相等，就会导出轴流守恒的沃德恒等式。问题在于测度能否不变。

先看有限个格拉斯曼变量。若$\eta'_n=J_{nm}\eta_m$，则$\eta'_1\cdots\eta'_N=(\det J)\eta_1\cdots\eta_N$。贝雷津积分以最高次单项式的积分等于一来定义，因而变量变换必须满足

<span id="eq:c77-inverse-berezin"></span>

$$
\prod_{n=1}^{N}d\eta'_n=(\det J)^{-1}\prod_{n=1}^{N}d\eta_n.
\tag{77.7}
$$

费米路径积分中的$\Psi$和$\bar\Psi$是独立积分变量；它们的轴变换矩阵互为转置，但行列式相同，所以出现两个逆行列式。形式地，变换核和测度比为

<span id="eq:c77-formal-jacobian"></span>

$$
\begin{aligned}
J(x,y)&=\delta^{(4)}(x-y)e^{-i\alpha(x)\gamma_5},\\
\mathcal J_\alpha
&=\frac{\mathcal D\Psi'\mathcal D\bar\Psi'}
        {\mathcal D\Psi\mathcal D\bar\Psi}
  =(\det J)^{-2},\\
\ln\mathcal J_\alpha
&=2i\int d^4x\,\alpha(x)\,
  \operatorname{tr}_{s,R}\!\left[\gamma_5\delta^{(4)}(x-x)\right]
  +O(\alpha^2).
\end{aligned}
\tag{77.8}
$$

这里$\operatorname{tr}_{s,R}$取旋量和表示指标的迹，函数空间的迹已经写成$x$积分。有限维的$\operatorname{tr}_s\gamma_5$虽等于零，$\delta^{(4)}(0)$却是紫外发散量。必须先定义重合极限中的完整算符，再取旋量迹；把两个因子分别赋值为零与无穷大并不能计算这个表达式。

这一步可以从谱展开精确地理解：用热核（heat kernel）调节重合点的$\delta$函数。由于实闵可夫斯基四动量上的$e^{-k^2/M^2}$不衰减，我们先规定它所代表的欧氏积分。取

<span id="eq:c77-euclidean-conventions"></span>

$$
\begin{gathered}
x_M^0=-ix_E^4,\qquad
\Gamma^4=\gamma^0,\qquad \Gamma^i=-i\gamma^i,\\
A_{E4}=-iA_{M0},\qquad A_{Ei}=A_{Mi},\qquad
\epsilon_E^{4123}=+1,\\
\{\Gamma^a,\Gamma^b\}=2\delta^{ab},\qquad
\Gamma_5=\Gamma^4\Gamma^1\Gamma^2\Gamma^3=\gamma_5.
\end{gathered}
\tag{77.9}
$$

欧氏指标$a,b$取$4,1,2,3$；表示指标仍用$T_R^a$时，由上下文区分。先在有限体积中取使狄拉克算符自伴的边界条件，例如光滑周期背景和相应的周期盒，再在内部考察局域极限。先在厄米欧氏连接上定义谱，所得局域多项式再按[（77.9）](#eq:c77-euclidean-conventions)续回实时坐标。$D_{Ea}$是反厄米的，故

<span id="eq:c77-spectral-basis"></span>

$$
H_E=i\Gamma^aD_{Ea}=H_E^\dagger,\qquad
H_E\phi_n=\lambda_n\phi_n,\qquad
\int d^4x_E\,\phi_n^\dagger\phi_m=\delta_{nm}.
\tag{77.10}
$$

用同一正交完备基展开$\Psi_E=\sum_nc_n\phi_n$、$\bar\Psi_E=\sum_n\bar c_n\phi_n^\dagger$，测度就是各$d c_n\,d\bar c_n$的乘积。无穷小变换在这个基中的矩阵为$\delta_{nm}-i\int\phi_n^\dagger\alpha\Gamma_5\phi_m$。对角迹中的高频模用$e^{-\lambda_n^2/M^2}$衰减，得到

<span id="eq:c77-regulated-spectral-trace"></span>

$$
\begin{aligned}
\mathcal T_{E,M}(x)
&=\sum_n e^{-\lambda_n^2/M^2}
       \phi_n^\dagger(x)\Gamma_5\phi_n(x)\\
&=\operatorname{tr}_{s,R}
  \langle x|\Gamma_5e^{-H_E^2/M^2}|x\rangle .
\end{aligned}
\tag{77.11}
$$

这里$M$的量纲是质量，取$M\to\infty$才恢复所有模。局域$\alpha$一般会混合高频和低频模，因此我们先求无穷小雅可比，再移去调节；沃德恒等式只需要这一阶。形式上的有限指数可以沿变换参数积分得到，但不必把局域变换的有限维投影当成一个封闭的变换群。

谱的选择还说明三种调节之间的区别。前两个候选在欧氏记号中分别是$e^{\partial_E^2/M^2}\delta_E^{(4)}(x-y)$和$e^{D_E^2/M^2}\delta_E^{(4)}(x-y)$。以普通$\partial^2$调节，不能保持背景规范变换下的核协变性；以$D^2$调节虽有这一协变性，却把狄拉克算符的自旋耦合删掉了。若只按自旋无关的$D^2$截断测度，所得零迹并不等于上面这个费米行列式的轴变分，差别须在行列式的其余调节中补回。由作用量中的狄拉克谱同时定义测度与行列式，则应使用[（77.11）](#eq:c77-regulated-spectral-trace)。它保留向量规范变换，又把自旋与背景场强的耦合完整地包括进来。下面正是这个耦合给出非零答案。

<span id="c77-heat-kernel"></span>

## 热核中留下的局域项

先在闵可夫斯基记号中整理算符，再用[（77.9）](#eq:c77-euclidean-conventions)指定的欧氏积分求值。两套狄拉克算符满足$i\slashed D_M=-\slashed D_E$，所以$\exp[(i\slashed D_M)^2/M^2]$正是$\exp[-H_E^2/M^2]$的延拓。对$\delta$函数作傅里叶展开，把平面波移到微分算符左边，有

<span id="eq:c77-shifted-kernel"></span>

$$
\begin{aligned}
K_M(x,y)
&=\int\frac{d^4k}{(2\pi)^4}\,
 e^{(i\slashed D_x)^2/M^2}e^{ik(x-y)}\\
&=\int\frac{d^4k}{(2\pi)^4}\,
 e^{ik(x-y)}
 \exp\!\left[\frac{(i\slashed D-\slashed k)^2}{M^2}\right]1.
\end{aligned}
\tag{77.12}
$$

这是因为$D_\mu(e^{ikx}f)=e^{ikx}(D_\mu+ik_\mu)f$，反复作用便适用于指数的每一幂。最右端的$1$保留了微分算符的作用次序：$\partial_\mu1=0$，但$D_\mu1=-igA_\mu$；中间的导数还会作用在右侧的$A$和$F$上。

现在把平方展开。记$S^{\mu\nu}=\frac{i}{4}[\gamma^\mu,\gamma^\nu]$，则所选Clifford代数给$\gamma^\mu\gamma^\nu=-g^{\mu\nu}-2iS^{\mu\nu}$。逐项计算为

<span id="eq:c77-dirac-square"></span>

$$
\begin{aligned}
(i\slashed D-\slashed k)^2
&=-\gamma^\mu\gamma^\nu D_\mu D_\nu
  -i\{\gamma^\mu,\gamma^\nu\}k_\mu D_\nu
  +\gamma^\mu\gamma^\nu k_\mu k_\nu\\
&=D^2+2iS^{\mu\nu}D_\mu D_\nu+2ik\cdot D-k^2\\
&=D^2+gS^{\mu\nu}F_{\mu\nu}+2ik\cdot D-k^2.
\end{aligned}
\tag{77.13}
$$

最后一步先用$S^{\mu\nu}$的反对称性把$D_\mu D_\nu$换成$\frac12[D_\mu,D_\nu]$，再用$[D_\mu,D_\nu]=-igF_{\mu\nu}$。因子$2i$、$\frac12$与$-ig$相乘，给自旋势前面的正号$+g$。

将旧积分变量写成$k_{\rm old}=Mk$，四维雅可比an是$M^4$。取$x=y$后平面波等于一，得到

<span id="eq:c77-rescaled-trace"></span>

$$
\mathcal T_M(x)
=M^4\int\frac{d^4k}{(2\pi)^4}e^{-k^2}
 \operatorname{tr}_{s,R}
 \left\{\gamma_5
 \exp\!\left[
  \frac{2ik\cdot D}{M}
 +\frac{D^2+gS^{\mu\nu}F_{\mu\nu}}{M^2}
 \right]1\right\}.
\tag{77.14}
$$

这里只把标量$-k^2$从指数中提出；其余算符仍保留在同一个指数中。特别是$D_\mu$与$F_{\rho\sigma}(x)$一般不对易，不能把指数拆成三个因子的乘积。

要找$M\to\infty$时的有限项，无须把整个热核求出。$2ik\cdot D$和$D^2$都不带gamma矩阵，而$SF$带两个。乘上$\gamma_5$后，零个或两个gamma矩阵的迹为零，因此一个非零有序词至少要含两个$SF$。每个$SF$又带$M^{-2}$，恰好两个已达到$M^{-4}$；再插入一个$D$或第三个$SF$便是更高负幂，不能与外面的$M^4$共同留下有限项。于是只有指数展开的二次项贡献：

<span id="eq:c77-surviving-word"></span>

$$
\lim_{M\to\infty}\mathcal T_M(x)
=\frac{g^2}{2}\int\frac{d^4k}{(2\pi)^4}e^{-k^2}
 \operatorname{tr}_s(\gamma_5S^{\mu\nu}S^{\rho\sigma})
 \operatorname{Tr}_R(F_{\mu\nu}F_{\rho\sigma}).
\tag{77.15}
$$

这段计数是在光滑固定背景的局部小热时展开中进行的，所有导数都作用在按上述次序保留的光滑系数上。它没有要求$D$与$F$对易，也没有假定$gA$很小；所取的展开参数是$M^{-1}$。被舍去的项至少多一个$M^{-1}$，与相应的局域导数或场强相乘。这里的$\frac12$来自指数的$2!$，不是图的对称因子。

自旋迹可以直接从第75节的四gamma恒等式得到。展开两个对易子，并用$\epsilon$对每一对指标的反对称性，四项同号相加：

<span id="eq:c77-spin-trace"></span>

$$
\begin{aligned}
\operatorname{tr}_s(\gamma_5S^{\mu\nu}S^{\rho\sigma})
&=-\frac1{16}
 \operatorname{tr}_s\!\left(
 \gamma_5[\gamma^\mu,\gamma^\nu]
          [\gamma^\rho,\gamma^\sigma]\right)\\
&=-\frac14\operatorname{tr}_s
  (\gamma_5\gamma^\mu\gamma^\nu\gamma^\rho\gamma^\sigma)
=+i\epsilon^{\mu\nu\rho\sigma}.
\end{aligned}
\tag{77.16}
$$

动量积分必须沿前面规定的Wick轮廓计算。令$k_M^0=ik_E^4$，则$k_M^2=k_E^2$、$d^4k_M=i\,d^4k_E$。四个实Gaussian积分各给$\sqrt\pi$，故

<span id="eq:c77-gaussian-integral"></span>

$$
\int_{\rm Wick}\frac{d^4k_M}{(2\pi)^4}e^{-k_M^2}
=\frac{i}{(2\pi)^4}\prod_{a=4,1,2,3}
   \int_{-\infty}^{\infty}dk_E^a\,e^{-(k_E^a)^2}
=\frac{i}{16\pi^2}.
\tag{77.17}
$$

[（77.16）](#eq:c77-spin-trace)与[（77.17）](#eq:c77-gaussian-integral)各带一个$i$，所以最终重合迹为实的负值：

<span id="eq:c77-minkowski-heat-coefficient"></span>

$$
\mathcal T(x)\equiv\lim_{M\to\infty}\mathcal T_M(x)
=-\frac{g^2}{32\pi^2}
 \epsilon^{\mu\nu\rho\sigma}
 \operatorname{Tr}_R(F_{\mu\nu}F_{\rho\sigma}).
\tag{77.18}
$$

也可以始终在欧氏空间确定这个号。此时
$\slashed D_E^{\,2}=D_E^2+E$，其中
$E=-\frac{ig}{4}[\Gamma^a,\Gamma^b]F_{Eab}$，而
$\operatorname{tr}_s(\Gamma_5\Gamma^a\Gamma^b\Gamma^c\Gamma^d)
=4\epsilon_E^{abcd}$。于是相同的$\frac12E^2$项给

<span id="eq:c77-euclidean-crosscheck"></span>

$$
\begin{aligned}
\mathcal T_E(x)
&=\frac{1}{16\pi^2}\frac12
 \left(-\frac{ig}{4}\right)^2
 \operatorname{tr}_s
 \!\left(\Gamma_5[\Gamma^a,\Gamma^b]
                  [\Gamma^c,\Gamma^d]\right)
 \operatorname{Tr}_R(F_{Eab}F_{Ecd})\\
&=-\frac{g^2}{32\pi^2}
 \epsilon_E^{abcd}\operatorname{Tr}_R(F_{Eab}F_{Ecd}).
\end{aligned}
\tag{77.19}
$$

[（77.9）](#eq:c77-euclidean-conventions)还给$F_{E4i}=-iF_{M0i}$，故$\epsilon_MFF=i\epsilon_EFF$。同时$d^4x_M=-i\,d^4x_E$要求$\delta_M^{(4)}=i\delta_E^{(4)}$，所以重合核满足$\mathcal T_M=i\mathcal T_E$。这两处转换把[（77.19）](#eq:c77-euclidean-crosscheck)送回[（77.18）](#eq:c77-minkowski-heat-coefficient)，与直接保留Wick因子的计算一致。

<span id="c77-ward"></span>

## 从雅可比恢复量子沃德恒等式

将重合迹代入[（77.8）](#eq:c77-formal-jacobian)，两个独立费米测度把系数乘以二：

<span id="eq:c77-regulated-jacobian"></span>

$$
\mathcal J_\alpha
=\exp\!\left[
 -i\frac{g^2}{16\pi^2}
 \int d^4x\,\alpha(x)\mathcal P[A](x)
 \right]+O(\alpha^2).
\tag{77.20}
$$

再把[（77.6）](#eq:c77-action-variation)的作用量变分一起放回积分，得到

<span id="eq:c77-changed-integral"></span>

$$
\begin{aligned}
Z_f[A]
={}&\int\mathcal D\Psi\,\mathcal D\bar\Psi\,e^{iS_f}\\
&\times\exp\!\left\{-i\int d^4x\,\alpha(x)
 \left[\partial_\mu j_A^\mu
       +\frac{g^2}{16\pi^2}\mathcal P[A]\right]\right\}
 +O(\alpha^2).
\end{aligned}
\tag{77.21}
$$

左边与右边是同一个积分的两套变量。因此，对任意紧支撑的$\alpha$取一阶，其系数必须为零。若还插入一个由场构成的乘积$\mathcal O$，变换也要作用在$\mathcal O$上，完整关系是

<span id="eq:c77-ward-insertions"></span>

$$
\begin{aligned}
0={}&\int\mathcal D\Psi\,\mathcal D\bar\Psi\,e^{iS_f}
 \biggl\{\delta_\alpha\mathcal O\\
&\quad-i\int d^4x\,\alpha(x)\mathcal O
 \left[\partial_\mu j_A^\mu(x)
       +\frac{g^2}{16\pi^2}\mathcal P[A](x)\right]\biggr\}.
\end{aligned}
\tag{77.22}
$$

$\delta_\alpha\mathcal O$给出流插入点与其他算符重合时的接触项。例如取$\mathcal O=\Psi(y)\bar\Psi(z)$，两处场的变分给出

$$
\begin{aligned}
\delta_\alpha[\Psi(y)\bar\Psi(z)]
={}&-i\alpha(y)\gamma_5\Psi(y)\bar\Psi(z)\\
&-i\alpha(z)\Psi(y)\bar\Psi(z)\gamma_5 .
\end{aligned}
$$

在不与其他插入重合的位置，或把接触项一并纳入复合算符恒等式时，[（77.22）](#eq:c77-ward-insertions)便是[（77.3）](#eq:c77-axial-target)。这也把上一节从双光子矩阵元认出的局域项推广到了任意光滑背景。

到这里始终没有按$g$展开费米行列式。热核只选出$M^{-4}$项，其中两个自旋势已经固定了$g^2$系数。对剩下的规范场及鬼场积分，相当于把[（77.22）](#eq:c77-ward-insertions)乘上它们的权重再积分，线性的变元恒等式仍然成立。因而在同一调节与复合算符归一下，局域反常的系数就是一圈得到的值。规范场的量子涨落仍会改变$\mathcal P[A]$的矩阵元；这与局域系数不受高阶修正完全相容。

移去调节后，轴流及场强平方都是需要定义的复合算符。同一量子数的$\partial j_A$与$\mathcal P$可以发生混合，轴流也可有有限的归一变化。我们以保持向量规范沃德及[（77.22）](#eq:c77-ward-insertions)的共同归一来表述轴反常的一圈精确性。若在另一减除方案中定义流，必须把两个算符同时转换后比较，不能只替换$g$或单独重标轴流。Adler–Bardeen的一圈精确性须在这种相容的量子定义下使用；测度推导确定其局域系数，重整化后恒等式的全阶保持还将在后面说明。

<span id="c77-consistent"></span>

## 外尔流与规范变换的一致性

换成左手外尔场后，规范变换本身便涉及手征投影。欧氏狄拉克算符把左手空间映到右手空间，外尔行列式的相位因此比上面的狄拉克行列式更难定义。我们可以沿第75节的三角图确定规范反常的局域结构：先用三角图确定二次背景项，再要求连续两次规范变换服从原来的群代数。后一要求称为韦斯—祖米诺（Wess–Zumino）一致性条件，它将固定三次项。

令$e^{iW[A]}$为外尔场积分，流用这个有效作用量的变分定义。在没有零模的局部定义域中，

<span id="eq:c77-consistent-current-definition"></span>

$$
\begin{aligned}
\frac{\delta W}{\delta A_\mu^a(x)}
 &=g\langle j^{a\mu}(x)\rangle_A,\qquad
 j^{a\mu}=\bar\Psi T_R^a\gamma^\mu P_L\Psi,\\
\delta_\theta A_\mu&=-\frac1gD_\mu\theta,\qquad
\delta_\theta\Psi=-i\theta\Psi,\qquad \theta=\theta^aT_R^a,\\
\delta_\theta W
&=-\int d^4x\,\langle j^{a\mu}\rangle_A(D_\mu\theta)^a
\\
&=\int d^4x\,\theta^a(D_\mu\langle j^\mu\rangle_A)^a
 \equiv\mathscr A[\theta,A].
\end{aligned}
\tag{77.23}
$$

$\theta=g\Gamma$为无量纲局域参数。最后一步采用紧支撑参数与不变的群指标内积，故协变积分分部和普通积分分部一样给一个负号。经典规范不变性要求协变散度为零，量子有效作用量若仍保持这个对称性也应如此。这里定义的流称为一致流；对$W$多次求变分得到的规范流插入自动具有玻色对称性。

第75节已经对三个相同规范顶角取$c=1/3$，并求出三角沃德的有限局域项。把其中一腿解释为[（77.23）](#eq:c77-consistent-current-definition)的变分，保留流中不带$g$的归一，它给出

<span id="eq:c77-consistent-quadratic"></span>

$$
\mathscr A_2[\theta,A]
=\frac{g^2}{24\pi^2}\int d^4x\,
 \epsilon^{\mu\nu\rho\sigma}\theta^a
 \operatorname{Tr}_R
 \!\left(T_R^a\,\partial_\mu A_\nu\,\partial_\rho A_\sigma\right).
\tag{77.24}
$$

这个系数还可用上一节两向量流保持守恒的结果来追踪：奇宇称链中的$P_L=(1-\gamma_5)/2$给$-1/2$，把同一局域收缩平均分到三条相同规范腿又给$1/3$。把轴结果中的两个线性场强展开，与列维—奇维塔张量缩并会给因子四，故其二次项系数是$-g^2/(4\pi^2)$；乘上这两个数便变成$+g^2/(24\pi^2)$。群迹中必须同时加入所变分那条规范腿的$T_R^a$；规范反常在阿贝尔情形含$Q^3$，轴单态反常则含$Q^2$。

设$\mathscr A[\theta,A]=\delta_\theta W$。两个变换在背景场上满足$[\delta_{\theta_1},\delta_{\theta_2}]=\delta_{\theta_{12}}$，其中$\theta_{12}=i[\theta_1,\theta_2]$。将同样的交换子作用于$W$，立刻得到

<span id="eq:c77-wess-zumino-condition"></span>

$$
\delta_{\theta_1}\mathscr A[\theta_2,A]
-\delta_{\theta_2}\mathscr A[\theta_1,A]
=\mathscr A[i[\theta_1,\theta_2],A].
\tag{77.25}
$$

参数在左边的各次变分中保持不动。这一条件来自有效作用量是同一个泛函，比仅要求右边具有某个指标结构更强。它同时说明为什么不能任取一个规范协变的局域表达式，便把它当作一致流的散度。

### 矩阵值微分形式与一致性方程

记矩阵值一形式与二形式为

<span id="eq:c77-ex-matrix-forms"></span>

$$
\begin{aligned}
A&=A_\mu\,dx^\mu,\\
dA&=(\partial_\mu A_\nu)\,dx^\mu\wedge dx^\nu,\\
F&=dA-igA\wedge A
  =\frac12F_{\mu\nu}\,dx^\mu\wedge dx^\nu.
\end{aligned}
\tag{77.41}
$$

这里$dx^\mu\wedge dx^\nu=-dx^\nu\wedge dx^\mu$；例如
$A\wedge A=\tfrac12[A_\mu,A_\nu]dx^\mu\wedge dx^\nu$，一般不为零。以下省略楔积符号，$A^3$便指$A\wedge A\wedge A$，并保持三个矩阵的原来次序。

计算只需两条运算法则。若$P,Q$分别是$p$次、$q$次矩阵值形式，则

<span id="eq:c77-ex-graded-rules"></span>

$$
\begin{aligned}
d(PQ)&=(dP)Q+(-1)^pP\,dQ,\\
\operatorname{Tr}_R(PQ)
 &=(-1)^{pq}\operatorname{Tr}_R(QP).
\end{aligned}
\tag{77.42}
$$

第一条是把外微分越过$p$个$dx$所产生的符号；第二条先对矩阵取循环迹，再把$p$个微分与$q$个微分交换次序。矩阵本身仍按原次序相乘。普通偏导彼此对易还保证$d^2=0$。

把这些法则用于[（77.25）](#eq:c77-wess-zumino-condition)。令$a=-igA_\mu dx^\mu$，并用一个格拉斯曼奇的辅助参数$w$代替$i\theta$。把$dx^\mu$也与$w$取为反对易，则总次数等于形式次数加鬼数。记$b=da$、$q=dw$；四个字母的总奇偶性依次为$a$奇、$b$偶、$w$奇、$q$偶。BRST形式的一致性运算为

<span id="eq:c77-graded-brst"></span>

$$
\begin{gathered}
sa=-q-aw-wa,\qquad sw=-w^2,\qquad sd=-ds,\\
sb=bw-wb-aq+qa,\qquad sq=qw-wq,\\
s(PQ)=(sP)Q+(-1)^{|P|}P(sQ),\qquad
\operatorname{Tr}(PQ)=(-1)^{|P||Q|}\operatorname{Tr}(QP).
\end{gathered}
\tag{77.26}
$$

例如$sb=s(da)=-d(sa)$，用$d^2=0$及外微分的分级乘积律便给第二行；$sq=-d(sw)=d(w^2)=qw-wq$同理。这些规则使$s^2=0$，而将两个独立奇参数的系数展开，$s\mathscr A=0$正好恢复[（77.25）](#eq:c77-wess-zumino-condition)。这里的$w$只为整理规范代数，不引入新的传播粒子。

在四维平直背景中，三角图给出的奇宇称局部密度是四形式，且对规范参数只取一次。把参数的导数积分分部后，单个费米迹中允许的项只有两个$da$、两个$a$与一个$da$、或四个$a$。先把已知二次项的系数归一为一，最一般的这种单迹代表可写为

<span id="eq:c77-local-anomaly-ansatz"></span>

$$
\Omega=\operatorname{Tr}_R
 w\left(bb+b_1aab+b_2aba+b_3baa+c\,aaaa\right).
\tag{77.27}
$$

三个$b_i$对应不同矩阵次序，一致性要求$s\Omega$是全微分。先在通用矩阵迹中求解，再代入具体表示。这个局部结构的推导也见[Bilal，第 9.3 节](https://arxiv.org/pdf/0802.0634v1#page=76)；下面直接列出系数方程。

为了比较全微分，先列出形式次数为三、鬼数为二的迹。在循环等价下，一个完整的候选集是

<span id="eq:c77-primitive-word-basis"></span>

$$
\begin{gathered}
aqq,\quad bqw,\quad bwq,\quad aaqw,\quad aawq,\quad abww,\\
aqaw,\quad awbw,\quad awwb,\quad aaaww,\quad aawaw .
\end{gathered}
\tag{77.28}
$$

记这些词的任意线性组合之迹为$\Xi$，依所列顺序以$t_1,\ldots,t_{11}$为系数。列举可以按含几个$b$或$q$来完成：$b$占两个形式次数，$q$同时占一个形式次数和一个鬼数；剩余次数只能由$a,w$补齐，再把循环重复的排列去掉。诸如$\operatorname{Tr}(aqaq)$的自身循环若带负号，其迹就是零。

对$s\Omega=d\Xi$逐词比较就得到普通线性方程。先展示进入计算的外微分，让符号可以直接核算：

<span id="eq:c77-primitive-derivatives"></span>

$$
\begin{aligned}
d\operatorname{Tr}(a^2qw)
 &=\operatorname{Tr}(aqwb-abqw+aaqq),\\
d\operatorname{Tr}(a^2wq)
 &=\operatorname{Tr}(awqb-abwq+aaqq),\\
d\operatorname{Tr}(abw^2)
 &=\operatorname{Tr}(bbww-abqw+abwq),\\
d\operatorname{Tr}(a^3w^2)
 &=\operatorname{Tr}(aawwb-abaww+aabww-aaaqw+aaawq).
\end{aligned}
\tag{77.29}
$$

例如最后一行先用$d(a^3)=ba^2-aba+a^2b$及$d(w^2)=qw-wq$，再把最左的$b$循环移到最后。它是偶元，所以该次循环不添负号。另一方面，对固定项施加$s$有
$s\operatorname{Tr}(wbb)
=\operatorname{Tr}(bbww-aqbw+abwq-aqwb+awbq)$；
这是把[（77.26）](#eq:c77-graded-brst)分别作用到三个因子后，消去成对项并作循环归并的结果。其余四项按同样的乘积律展开，下面七个词的系数已经足以确定全部$b_i,c$：

<span id="eq:c77-coefficient-equations"></span>

$$
\begin{array}{c|c|c}
\text{迹内的词}&s\Omega\text{中的系数}&d\Xi\text{中的系数}\\ \hline
aabww&b_1&t_{10}\\
aawwb&b_3&t_{10}\\
abaww&b_2&-t_{10}\\
aaaaww&c&0\\
aaqq&0&t_4+t_5\\
abqw&b_2&-t_4-t_6\\
abwq&1-b_1&-t_5+t_6
\end{array}
\tag{77.30}
$$

前四行给$b_1=b_3=-b_2=t_{10}$及$c=0$。第五行给$t_5=-t_4$，第六行再给$t_6=b_1-t_4$；将它们代入最后一行，便得到$1-b_1=b_1$。因此

<span id="eq:c77-consistency-coefficients"></span>

$$
b_1=b_3=\frac12,\qquad b_2=-\frac12,\qquad c=0,\qquad
\Omega=\operatorname{Tr}_R w\left[da\,da+\frac12d(a^3)\right].
\tag{77.31}
$$

这些必要条件也足够。取下面的三形式，按[（77.26）](#eq:c77-graded-brst)及[（77.29）](#eq:c77-primitive-derivatives)展开，两边所有词逐项相等：

<span id="eq:c77-exact-descent-certificate"></span>

$$
\begin{aligned}
\Xi_*&=\operatorname{Tr}_R
 \left(-\frac12a^2qw+\frac12a^2wq+abw^2
       +\frac12aqaw+\frac12a^3w^2\right),\\
s\,\operatorname{Tr}_R w
 \left[da\,da+\frac12d(a^3)\right]&=d\Xi_* .
\end{aligned}
\tag{77.32}
$$

例如还未在[（77.29）](#eq:c77-primitive-derivatives)列出的那一项为
$d\operatorname{Tr}(aqaw)=\operatorname{Tr}(awbq-aqbw)$；
将它和前四行以$\Xi_*$中的系数组合，即可完成这个等式的右边。
$\Xi_*$的形式次数为三、鬼数为二，故$d\Xi_*$恰有$s\Omega$的次数。
紧支撑参数使其积分为零，从而验证了一致性。这样，三次项的$\frac12$由规范代数与二次项共同确定。

恢复$a=-igA$、$w=i\theta$。有$a\,da=-g^2A\,dA$及$a^3=ig^3A^3$，因此

<span id="eq:c77-consistent-form"></span>

$$
\begin{aligned}
\operatorname{Tr}_R w\,d\!\left(a\,da+\frac12a^3\right)
&=-ig^2\operatorname{Tr}_R
 \theta\,d\!\left(A\,dA-\frac{ig}{2}A^3\right),\\
\mathscr A[\theta,A]
&=\frac{g^2}{24\pi^2}
 \int\operatorname{Tr}_R
 \theta\,d\!\left(A\,dA-\frac{ig}{2}A^3\right).
\end{aligned}
\tag{77.33}
$$

第二行的整体归一由[（77.24）](#eq:c77-consistent-quadratic)匹配。对照[Bilal 的联络与参数定义](https://arxiv.org/pdf/0802.0634v1#page=63)，有$A_B=gA$、$\omega_B=-\theta$，故其反厄米联络与奇参数分别为这里的$a$和$w$。展开外微分并利用$\theta(x)$的任意性，得到一致流的协变散度：

<span id="eq:c77-consistent-anomaly"></span>

$$
(D_\mu j^\mu)^a
=\frac{g^2}{24\pi^2}\epsilon^{\mu\nu\rho\sigma}\partial_\mu
 \operatorname{Tr}_R\!\left[
 T_R^a\left(A_\nu\partial_\rho A_\sigma
           -\frac{ig}{2}A_\nu A_\rho A_\sigma\right)\right].
\tag{77.34}
$$

这里和前面一样，流恒等式在相关函数中带相应接触项。右边虽写在协变散度之后，却不是协变形式的局部多项式；一致流由$W$的变分定义，在有反常时不必自身按伴随表示协变变换。若改用一个专门保持局部协变性的流，其定义会多出背景场的局域项，散度也随之改变。这两种流的区别在三条相同规范腿的玻色对称要求中已经出现。

<span id="c77-comparison"></span>

## 消除条件及轴流公式的比较

将[（77.34）](#eq:c77-consistent-anomaly)的右边记为$\mathscr A^a[A](x)$。对于非零耦合，反常在所有光滑背景中消失的充要条件是

<span id="eq:c77-local-cancellation"></span>

$$
B_R^{abc}\equiv\frac12\operatorname{Tr}_R
   \!\left(T_R^a\{T_R^b,T_R^c\}\right)=0
\quad\text{对全部 }a,b,c
\tag{77.35}
$$

若表示可约，迹取遍各不可约块。下面分别证明必要性和充分性。

<span id="c77-cancellation-proof"></span>

对任意紧支撑的局域参数$\theta^a(x)$和任意光滑背景$A$，反常泛函应满足

<span id="eq:c77-ex-local-functional"></span>

$$
\mathfrak A[\theta,A]
 \equiv\int d^4x\,\theta^a(x)\mathscr A^a[A](x)=0 .
\tag{77.43}
$$

由于$\theta$可以在任一点附近任意选择，这等价于$\mathscr A^a[A](x)$对所有背景逐点为零。

先按规范势的次数展开。二次项中，$\partial_\mu$作用于$\partial_\rho A_\sigma$的部分被$\epsilon^{\mu\nu\rho\sigma}$消去，因为$\partial_\mu\partial_\rho$对$\mu,\rho$对称。因此只剩

<span id="eq:c77-ex-quadratic-density"></span>

$$
\mathscr A_2^a[A]
 =\frac{g^2}{24\pi^2}
 \epsilon^{\mu\nu\rho\sigma}
 (\partial_\mu A_\nu^b)(\partial_\rho A_\sigma^c)
 \operatorname{Tr}_R(T^aT^bT^c).
\tag{77.44}
$$

交换两个时空指标对$(\mu,\nu)$与$(\rho,\sigma)$是偶置换。再交换哑指标$b,c$，场的分量系数彼此对易，所以这个二次项只保留群迹关于$b,c$的对称部分。用（77.35）定义的$B_R$，得到

<span id="eq:c77-ex-quadratic-symmetric-trace"></span>

$$
\mathscr A_2^a[A]
 =\frac{g^2}{24\pi^2}B_R^{abc}
 \epsilon^{\mu\nu\rho\sigma}
 (\partial_\mu A_\nu^b)(\partial_\rho A_\sigma^c).
\tag{77.45}
$$

$B_R$对$b,c$的对称性由定义给出；把迹中的三个矩阵循环移动，又可交换$a$与$b$，因此它对三个指标完全对称。

这个二次项已经给出必要条件。把所考察的点取为原点，令$\chi(x)$是紧支撑光滑函数，并在原点附近等于1。任取两个实群向量$u^b,v^b$，设置

<span id="eq:c77-ex-test-background"></span>

$$
A_1^b(x)=u^b x^0\chi(x),\qquad
A_3^b(x)=v^b x^2\chi(x),\qquad
A_0^b(x)=A_2^b(x)=0 .
\tag{77.46}
$$

在原点，$A_\mu=0$，只有$\partial_0A_1^b=u^b$和$\partial_2A_3^b=v^b$非零。于是[（77.34）](#eq:c77-consistent-anomaly)的三次项及其一次导数都在该点消失，而$\epsilon^{0123}=\epsilon^{2301}=+1$给出

<span id="eq:c77-ex-necessity"></span>

$$
\mathscr A^a[A](0)
 =\frac{g^2}{12\pi^2}B_R^{abc}u^bv^c .
\tag{77.47}
$$

若[（77.43）](#eq:c77-ex-local-functional)对所有背景恒为零，这个结果必须对每个$a$及所有$u,v$为零。依次令$u,v$只在指定的一个分量非零，便得到每个$B_R^{abc}=0$。反之，只要有一个非零分量，[（77.46）](#eq:c77-ex-test-background)就构造出局部反常非零的背景。

还须证明$B_R=0$也消去三次项。三次项中的矩阵乘积要按时空指标的反对称性归并。令

<span id="eq:c77-ex-antisymmetric-three-generators"></span>

$$
\begin{aligned}
\mathcal S^{bcd}
 &\equiv T^bT^cT^d+T^cT^dT^b+T^dT^bT^c\\
 &\quad-T^bT^dT^c-T^dT^cT^b-T^cT^bT^d\\
 &=T^b[T^c,T^d]+T^c[T^d,T^b]+T^d[T^b,T^c].
\end{aligned}
\tag{77.48}
$$

这是不含$1/3!$的完全反对称和。在$\epsilon^{\mu\nu\rho\sigma}A_\nu^bA_\rho^cA_\sigma^d$中，同时交换任意两个群指标及相应的时空指标，会带来一个负号。因此，三次群迹在这一缩并中等于$\operatorname{Tr}_R(T^a\mathcal S^{bcd})/6$。

为计算这个迹，先保留一般的二次迹

<span id="eq:c77-ex-trace-decomposition"></span>

$$
\begin{aligned}
K_R^{af}&\equiv\operatorname{Tr}_R(T^aT^f),\\
\operatorname{Tr}_R(T^aT^bT^e)
 &=B_R^{abe}+\frac{i}{2}f^{bef}K_R^{af}.
\end{aligned}
\tag{77.49}
$$

后一式只是把$T^bT^e$写成反对易子与对易子的各一半。保留$K_R$，使这一步也直接适用于可约表示与多个简单因子。把[（77.49）](#eq:c77-ex-trace-decomposition)用在[（77.48）](#eq:c77-ex-antisymmetric-three-generators)中，得到

<span id="eq:c77-ex-four-trace-reduction"></span>

$$
\begin{aligned}
\operatorname{Tr}_R(T^a\mathcal S^{bcd})
 &=i\left(f^{cde}B_R^{abe}
          +f^{dbe}B_R^{ace}
          +f^{bce}B_R^{ade}\right)\\
 &\quad-\frac12K_R^{af}
 \left(f^{cde}f^{bef}
      +f^{dbe}f^{cef}
      +f^{bce}f^{def}\right).
\end{aligned}
\tag{77.50}
$$

最后一行的括号为零。具体地，雅可比恒等式
$[T^b,[T^c,T^d]]+[T^c,[T^d,T^b]]+[T^d,[T^b,T^c]]=0$
给出结构常数的关系

<span id="eq:c77-ex-jacobi-coefficient"></span>

$$
f^{cde}f^{bef}
 +f^{dbe}f^{cef}
 +f^{bce}f^{def}=0 .
\tag{77.51}
$$

这是一条李代数本身的恒等式，因而在非忠实表示中也成立。

[（77.50）](#eq:c77-ex-four-trace-reduction)剩下的三个$fB$项，在三次规范势的反对称缩并中相等。把$(b,c,d)$及$(\nu,\rho,\sigma)$作同一个三循环即可互相变换；三循环是偶置换。因此，因子$1/6$与三个相等项合成$1/2$，给出

<span id="eq:c77-ex-cubic-symmetric-trace"></span>

$$
\begin{aligned}
&\epsilon^{\mu\nu\rho\sigma}
 \operatorname{Tr}_R(T^aA_\nu A_\rho A_\sigma)\\
&\qquad=\frac{i}{2}f^{cde}B_R^{abe}
 \epsilon^{\mu\nu\rho\sigma}
 A_\nu^bA_\rho^cA_\sigma^d .
\end{aligned}
\tag{77.52}
$$

乘上[（77.34）](#eq:c77-consistent-anomaly)中三次项的$-ig/2$，两个$i$给出正的$g/4$。这样，一致反常的整个右边都写成

<span id="eq:c77-ex-density-all-in-b"></span>

$$
\begin{aligned}
\mathscr A^a[A]
 =\frac{g^2}{24\pi^2}\epsilon^{\mu\nu\rho\sigma}
 \biggl[&
 B_R^{abc}(\partial_\mu A_\nu^b)(\partial_\rho A_\sigma^c)\\
 &+\frac g4 f^{cde}B_R^{abe}
  \partial_\mu(A_\nu^bA_\rho^cA_\sigma^d)\biggr].
\end{aligned}
\tag{77.53}
$$

所以$B_R^{abc}=0$同时消去二次项和三次项，与[（77.47）](#eq:c77-ex-necessity)合起来证明

<span id="eq:c77-ex-anomaly-iff"></span>

$$
\mathfrak A[\theta,A]\equiv0
\quad\Longleftrightarrow\quad
B_R^{abc}=0\quad\text{对所有 }a,b,c .
\tag{77.54}
$$

只有共同三次不变张量空间是一维且已选非零$d^{abc}$时，才可写$B_R^{abc}=A(R)d^{abc}$，将条件缩写成$A(R)=0$。一般情形保留完整张量；可约表示对各左手多重态求和，直积群的混合反常条件也包括在内。

<span id="c77-chern-simons-proof"></span>

### 轴流密度的全导数形式

在具有光滑规范势的坐标片内，由$F=dA-igA^2$及分级迹循环，轴流反常可写为

<span id="eq:c77-axial-chern-simons"></span>

$$
\begin{aligned}
\operatorname{Tr}_R(F^2)
&=\operatorname{Tr}_R(dA\,dA-2ig\,dA\,A^2)\\
&=d\,\operatorname{Tr}_R\!\left(A\,dA-\frac{2ig}{3}A^3\right),\\
\partial_\mu j_A^\mu
&=-\frac{g^2}{4\pi^2}\epsilon^{\mu\nu\rho\sigma}\partial_\mu
 \operatorname{Tr}_R\!\left(
 A_\nu\partial_\rho A_\sigma-\frac{2ig}{3}A_\nu A_\rho A_\sigma
 \right).
\end{aligned}
\tag{77.36}
$$

展开两个场强的乘积：

<span id="eq:c77-ex-field-strength-square"></span>

$$
\begin{aligned}
\operatorname{Tr}_R(F^2)
 &=\operatorname{Tr}_R\left(
 dA\,dA-ig\,dA\,A^2-ig\,A^2dA-g^2A^4\right)\\
 &=\operatorname{Tr}_R(dA\,dA)
   -2ig\operatorname{Tr}_R(dA\,A^2)
   -g^2\operatorname{Tr}_R(A^4).
\end{aligned}
\tag{77.55}
$$

$dA$和$A^2$都是二形式，故交换它们的迹循环不带负号，两个交叉项相等。四次项则不同：把最前面的一个$A$循环移过后面的三个$A$，会得到$(-1)^3$，所以

<span id="eq:c77-ex-quartic-vanishes"></span>

$$
\operatorname{Tr}_R(A^4)
=(-1)^3\operatorname{Tr}_R(A^4)=0 .
\tag{77.56}
$$

也可以直接在分量中看见这个消去。令
$Q=\epsilon^{\mu\nu\rho\sigma}\operatorname{Tr}_R(A_\mu A_\nu A_\rho A_\sigma)$。
普通矩阵迹的循环性给

<span id="eq:c77-ex-quartic-component-cycle"></span>

$$
\begin{aligned}
Q&=\epsilon^{\mu\nu\rho\sigma}
       \operatorname{Tr}_R(A_\nu A_\rho A_\sigma A_\mu)\\
 &=-\epsilon^{\mu\nu\rho\sigma}
       \operatorname{Tr}_R(A_\mu A_\nu A_\rho A_\sigma)
 =-Q .
\end{aligned}
\tag{77.57}
$$

第二行重新命名四个哑指标，四循环是奇置换，因而$Q=0$。若从$F_{\mu\nu}F_{\rho\sigma}$中的两个对易子开始，四项依次为

<span id="eq:c77-ex-quartic-commutator-expansion"></span>

$$
\begin{aligned}
&\epsilon^{\mu\nu\rho\sigma}
 \operatorname{Tr}_R([A_\mu,A_\nu][A_\rho,A_\sigma])\\
&=\epsilon^{\mu\nu\rho\sigma}\operatorname{Tr}_R
 \left(A_\mu A_\nu A_\rho A_\sigma
      -A_\mu A_\nu A_\sigma A_\rho\right)\\
&\quad+\epsilon^{\mu\nu\rho\sigma}\operatorname{Tr}_R
 \left(-A_\nu A_\mu A_\rho A_\sigma
       +A_\nu A_\mu A_\sigma A_\rho\right)\\
&=4Q=0 .
\end{aligned}
\tag{77.58}
$$

这里第二项交换$\rho,\sigma$，第三项交换$\mu,\nu$，第四项同时作两次交换，分别恢复成$Q$。四项取迹后均等于$Q$，再由迹循环性得到零。

再对三形式求外微分。首先，$d^2A=0$给出

<span id="eq:c77-ex-derivative-a-da"></span>

$$
d\,\operatorname{Tr}_R(A\,dA)
 =\operatorname{Tr}_R(dA\,dA).
\tag{77.59}
$$

其次，依次让$d$作用于三个$A$，

<span id="eq:c77-ex-derivative-cubic"></span>

$$
\begin{aligned}
d\,\operatorname{Tr}_R(A^3)
 &=\operatorname{Tr}_R\left(dA\,A^2-A\,dA\,A+A^2dA\right)\\
 &=3\operatorname{Tr}_R(dA\,A^2).
\end{aligned}
\tag{77.60}
$$

第一项已经具有所需次序。第二项中，把最左的$A$循环移过二形式$dA$及最后的一形式$A$，得到负号，恰好消去它前面的负号。第三项中，$A^2$与$dA$都是二形式，循环移动给正号。因此三项在迹内相等。

由[（77.55）](#eq:c77-ex-field-strength-square)、[（77.56）](#eq:c77-ex-quartic-vanishes)及[（77.59）](#eq:c77-ex-derivative-a-da)、[（77.60）](#eq:c77-ex-derivative-cubic)，得到

<span id="eq:c77-ex-chern-simons-form"></span>

$$
\begin{aligned}
d\,\operatorname{Tr}_R\left(A\,dA-\frac{2ig}{3}A^3\right)
 &=\operatorname{Tr}_R(dA\,dA)
     -2ig\operatorname{Tr}_R(dA\,A^2)\\
 &=\operatorname{Tr}_R(F^2).
\end{aligned}
\tag{77.61}
$$

这解释了$2/3$：两个场强交叉项给2，而外微分作用于三次项给3。括号内的三形式称为此归一下的Chern–Simons形式。

最后恢复分量，确定[（77.36）](#eq:c77-axial-chern-simons)中的因子4。选定定向
$d^4x=dx^0\wedge dx^1\wedge dx^2\wedge dx^3$，于是
$dx^\mu\wedge dx^\nu\wedge dx^\rho\wedge dx^\sigma
=\epsilon^{\mu\nu\rho\sigma}d^4x$。两个$F$各含一个$1/2$，故

<span id="eq:c77-ex-four-form-components"></span>

$$
\operatorname{Tr}_R(F^2)
 =\frac14\epsilon^{\mu\nu\rho\sigma}
       \operatorname{Tr}_R(F_{\mu\nu}F_{\rho\sigma})\,d^4x .
\tag{77.62}
$$

而三形式及其外微分为

<span id="eq:c77-ex-chern-simons-components"></span>

$$
\begin{aligned}
&\operatorname{Tr}_R\left(A\,dA-\frac{2ig}{3}A^3\right)\\
&\quad=\operatorname{Tr}_R\left(
 A_\nu\partial_\rho A_\sigma-\frac{2ig}{3}A_\nu A_\rho A_\sigma
 \right)dx^\nu\wedge dx^\rho\wedge dx^\sigma,\\
&d\,\operatorname{Tr}_R\left(A\,dA-\frac{2ig}{3}A^3\right)\\
&\quad=\epsilon^{\mu\nu\rho\sigma}\partial_\mu
 \operatorname{Tr}_R\left(
 A_\nu\partial_\rho A_\sigma-\frac{2ig}{3}A_\nu A_\rho A_\sigma
 \right)d^4x .
\end{aligned}
\tag{77.63}
$$

将最后两式代入[（77.61）](#eq:c77-ex-chern-simons-form)，消去共同的$d^4x$，便得到$\epsilon\operatorname{Tr}_R FF$与全导数之间的因子4。乘回轴反常系数$-g^2/(16\pi^2)$，即恢复[（77.36）](#eq:c77-axial-chern-simons)。这是每个坐标片内的密度恒等式；将它对整个时空积分时，还要拼接各片的规范势并计算边界贡献。

### 一致流与协变流的系数

现在两个系数的差别就清楚了。在具有相同群插入的二次背景项上，

<span id="eq:c77-half-and-third"></span>

$$
-\frac{g^2}{4\pi^2}
 \left(-\frac12\right)\left(\frac13\right)
=+\frac{g^2}{24\pi^2}.
\tag{77.37}
$$

$-1/2$反映左手投影，$1/3$反映三个规范流插入的对称处理。但整体乘上这两个数不会把[（77.36）](#eq:c77-axial-chern-simons)的$2/3$变成[（77.34）](#eq:c77-consistent-anomaly)的$1/2$；后者还需要刚才的一致性计算。所以系数的比例与局域多项式的结构必须分别确定。

以单位电荷的阿贝尔场为例，$A^2=0$，三次形式项消失，区别只剩系数。协变热核在指定的流腿保留手征投影，相当于取轴结果的$-1/2$；一致流则还把局域项平均分配给三条腿。于是

<span id="eq:c77-abelian-two-currents"></span>

$$
\begin{aligned}
\partial_\mu j_{\rm cov}^\mu
 &=+\frac{g^2}{32\pi^2}\epsilon^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma},\\
\partial_\mu j_{\rm cons}^\mu
 &=+\frac{g^2}{96\pi^2}\epsilon^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}.
\end{aligned}
\tag{77.38}
$$

第二行正是[（77.34）](#eq:c77-consistent-anomaly)的阿贝尔极限，因为$\epsilon FF=4\epsilon\,\partial A\,\partial A$。它的三倍差别是流定义和规范腿对称条件的差别。第75节以相同规范顶角计算的反常应与第二行比较；第76节则始终保护两个向量沃德。

[（77.35）](#eq:c77-local-cancellation)是我们由一圈三角图与局域一致性得到的条件。把它推广成“微扰论每一阶都可保持规范沃德”，还需一个关于重整化的定理：在四维局部、可重整、微扰可幺正且耦合通常物质场的规范理论中，若一圈的局域规范反常可由局域反项消去，就存在一个减除方案，使规范反常在全部微扰阶消失。改用其他方案时，可以相应调整有限局域反项。这是[Anselmi 所述的 Adler–Bardeen 定理](https://arxiv.org/pdf/1402.6453v2#page=4)；[第 8 节](https://arxiv.org/pdf/1402.6453v2#page=35)将证明扩展到标量、右手费米子及阿贝尔因子。它保证满足一圈消除条件的规范理论，可以在重整化的各阶继续保持规范沃德恒等式。

<span id="c77-global"></span>

## 整体规范反常

局域规范变换只比较与恒等变换连续相连的场配置。即使[（77.35）](#eq:c77-local-cancellation)成立，仍可能沿规范轨道的一条非平凡闭路遇到测度相位的障碍。对于一个具有实符号选择的手征费米积分，把它沿连接$A$与$A^U$的路径连续延拓，可能得到

<span id="eq:c77-global-sign"></span>

$$
Z_f[A^U]=-Z_f[A],
\tag{77.39}
$$

其中$U$是不能连续缩到恒等变换的大规范变换。两个端点代表同一个物理规范配置，费米振幅却相差一个不可统一选去的符号，这就是整体规范反常的典型情形。用几何语言说，费米行列式或普法夫式的相位须在规范轨道空间上拼接，而这条闭路使实测度的定向翻转。

若形式地同时积分符号相反的规范等价配置，它们的贡献会两两抵消。这一抵消反映了规范商上的测度无法一致定义。由零模导致的无插入积分为零则可通过源插入处理，其含义与这里的定向障碍不同。

第75节已给出普通自旋四流形上的$SU(2)$例子。一个左手基本双重态在非平凡大变换下翻号，$N$个这样的双重态相乘给$(-1)^N$，所以双重态数必须为偶数。对一般自旋$j$表示，普通$SU(2)$障碍的条件是

<span id="eq:c77-su2-global-condition"></span>

$$
\sum_i2T(j_i)=0\pmod2,\qquad
T(j)=\frac{j(j+1)(2j+1)}3,\qquad T(\mathbf2)=\frac12.
\tag{77.40}
$$

这一整体指标的计算见[Wang、Wen 与 Witten，第 2.2–2.3 节](https://arxiv.org/pdf/1810.00844v4#page=9)，第75节已写出普通自旋流形上的表示条件。例如$j=3/2$虽为伪实表示，却有$2T=10$，对这种普通自旋时空的$SU(2)$反常不翻号；各多重态须按$2T(j)$的奇偶性计数。

局域反常与整体反常提出两种互补的要求：局部沃德恒等式须在量子理论中保持，测度相位须在整个规范轨道空间上一致定义。后者取决于群的全局形式、表示及允许的时空结构。在无反常的理论中，下一节将利用背景规范不变性组织有效作用量的计算。

---

[← 第 76 节](/posts/srednicki-76/) · [章节地图](/srednicki/) · [第 78 节 →](/posts/srednicki-78/)
