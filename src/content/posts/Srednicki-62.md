---
title: 'Srednicki §62 旋量电动力学中的圈修正'
date: 2026-09-14
category: 笔记
tags: [物理, 量子场论, Srednicki]
series: 'Srednicki QFT'
srednickiSections: [62]
hideFromHome: true
draft: false
---

<span id="c62"></span>

前几节的电动力学散射计算只用了树图。现在把一圈图加进来，电子与光子的传播子、
以及电子发射光子的顶角都会改变。计算仍沿第51节的次序进行：
先确定允许出现的反项，再用质量、留数和耦合的定义固定它们。
电动力学多出一个需要留意的尺度：光子可以任意软，电子质量壳因而紧邻连续谱。
紫外发散与这个红外问题将在同一计算中出现，须分别处理。

<span id="c62-model"></span>

## 对称性允许哪些反项

在四维中，$[A_\mu]=1$、$[\Psi]=3/2$。第18节的幂次计数与第29节的局部展开
告诉我们，应当把维数不超过四、又与所要求对称性相容的局域项全部列出。
这里要求洛伦兹不变性、局域$U(1)$以及$P,T,C$。除去只改真空能的常数项，
并把分部积分相差的项视为同一个算符，纯电磁部分由两个场强构成。
它们的两个洛伦兹标量是$F_{\mu\nu}F^{\mu\nu}$和
$\epsilon_{\mu\nu\rho\sigma}F^{\mu\nu}F^{\rho\sigma}$。后者正比于
$\mathbf E\cdot\mathbf B$，在宇称及时间反演下均变号，故不加入当前理论；
在本节的阿贝尔微扰边界条件下，它也只给一个全导数。
具体地，展开两个反对称场强得到
$\epsilon^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}
=4\partial_\mu(\epsilon^{\mu\nu\rho\sigma}A_\nu\partial_\rho A_\sigma)$；
导数再作用到后一个$A$所给的二阶偏导，因$\mu,\rho$的反对称性相消。
场强本身可以由$[D_\mu,D_\nu]=-ieF_{\mu\nu}$构造，这正是
第58节局域相位要求在纯规范部分的表现。

含两费米场的质量项已有维数三，最多再放一个导数。狄拉克矩阵基中的标量给
$\bar\Psi\Psi$，一个导数与矢量矩阵缩并给$i\bar\Psi\slashed D\Psi$；
相应含$\gamma_5$的项因宇称而被排除。$\Psi^T\mathcal C\Psi$带两个单位的
狄拉克荷，也不保持$U(1)$。四费米项的维数已经是六，磁矩型的
$\bar\Psi\sigma^{\mu\nu}\Psi F_{\mu\nu}$则是五，都不在这个反项空间内。
因此，与标量电动力学需要另外允许四标量项的情形相比，这里没有新的独立耦合。
把自由部分和反项分开写为
<span id="eq:c62-model"></span>

$$
\begin{aligned}
\mathcal L_0&=i\bar\Psi\slashed\partial\Psi-m\bar\Psi\Psi
 -\frac14F^{\mu\nu}F_{\mu\nu},\\
\mathcal L_1&=Z_1e\bar\Psi\slashed A\Psi+\mathcal L_{\rm ct},\\
\mathcal L_{\rm ct}
 &=i\delta Z_2\bar\Psi\slashed\partial\Psi
   -\delta Z_m m\bar\Psi\Psi-\frac14\delta Z_3F^{\mu\nu}F_{\mu\nu},
\qquad \delta Z_a=Z_a-1 .
\end{aligned}
\tag{62.1}
$$

暂时把四个$Z$分别记账。场归一化、质量和电荷的定义给出减除条件，
规范对称性则把其中一些条件联系起来。
本节采用壳上方案。需特别区分$Z_m$与裸质量的比值；把费米动能归一以后，
后者为$m_{\rm B}/m=Z_m/Z_2$。

<span id="c62-gauge"></span>

## 光子核的纵横分解

先确定用来连接光子自能插入的自由传播核。在第57节的麦克斯韦二次作用量上加入
$-(\partial\cdot A)^2/(2\xi)$，作一次分部积分和傅里叶变换，得到
<span id="eq:c62-gauge-kernel"></span>

$$
\begin{aligned}
S^{(2)}_\xi
 &=-\frac12\int\frac{d^4k}{(2\pi)^4}\,
 \widetilde A_\mu(-k)K_\xi^{\mu\nu}(k)\widetilde A_\nu(k),\\
K_\xi^{\mu\nu}
 &=k^2g^{\mu\nu}-(1-\xi^{-1})k^\mu k^\nu
   =k^2(P^{\mu\nu}+\xi^{-1}L^{\mu\nu}),\\
L^{\mu\nu}&=\frac{k^\mu k^\nu}{k^2},\qquad
P^{\mu\nu}=g^{\mu\nu}-L^{\mu\nu},\\
P^\mu{}_\rho P^\rho{}_\nu&=P^\mu{}_\nu,\qquad
L^\mu{}_\rho L^\rho{}_\nu=L^\mu{}_\nu,\qquad PL=LP=0 .
\end{aligned}
\tag{62.2}
$$

这里先取$k^2\ne0$、$\xi\ne0$。纵横子空间上的本征值分别是$k^2/\xi$和$k^2$，
所以求逆只需把两者各自倒过来：
<span id="eq:c62-gauge-propagator"></span>

$$
\begin{aligned}
\widetilde\Delta_\xi^{\mu\nu}
 &=\frac{P^{\mu\nu}+\xi L^{\mu\nu}}{k^2-i0}
 =\frac1{k^2-i0}\left[g^{\mu\nu}
 -(1-\xi)\frac{k^\mu k^\nu}{k^2}\right],\\
\widetilde\Delta_\xi^{\mu\nu}
 &=\lim_{\delta\downarrow0}
 \left[\frac{g^{\mu\nu}}{d_\delta}
 -(1-\xi)\frac{k^\mu k^\nu}{d_\delta^2}\right],
\qquad d_\delta=k^2-i\delta .
\end{aligned}
\tag{62.3}
$$

第一行是离壳的代数写法；光锥上的含义由第二行的共同边界值给出，
其分布极限已在[第57节](/posts/srednicki-57/)说明。$\xi=1$为费曼规范，$\xi\to0$留下横向核，
对应朗道规范。后一个极限也可在欧氏规范平均中看出：
$\exp[-\int(\partial\cdot A)^2/(2\xi)]$在$\xi\downarrow0$时集中到
$\partial\cdot A=0$。[下文](#c62-gauge-limit)用归一化高斯极限具体说明这个条件。以下把这族规范记为$R_\xi$规范。

把截去外线的光子1PI图之和定义为$i\Pi_{\mu\nu}$。
插入一次时，各因子中的$i$满足
$(1/i)\,i\,(1/i)=1/i$，故在去掉传播子的共同$1/i$后，
<span id="eq:c62-photon-dyson"></span>

$$
\widetilde{\boldsymbol\Delta}
 =\widetilde\Delta+\widetilde\Delta\Pi\widetilde\Delta
 +\widetilde\Delta\Pi\widetilde\Delta\Pi\widetilde\Delta+\cdots .
\tag{62.4}
$$

规范不变性要求$\Pi_{\mu\nu}$横向，一般关系将在[第68节](/posts/srednicki-68/)讨论。
这里先直接计算一圈图，证明它的两个纵向缩并都为零。
先看横向性一旦成立，会怎样简化上面的级数。洛伦兹协变性只允许
$a(k^2)g^{\mu\nu}+b(k^2)k^\mu k^\nu$，缩并$k_\mu$给
$(a+b k^2)k^\nu$，因此
<span id="eq:c62-polarization-structure"></span>

$$
k_\mu\Pi^{\mu\nu}=k_\nu\Pi^{\mu\nu}=0
\quad\Longrightarrow\quad
\Pi^{\mu\nu}
 =\Pi(k^2)(k^2g^{\mu\nu}-k^\mu k^\nu)
 =k^2\Pi(k^2)P^{\mu\nu}.
\tag{62.5}
$$

每次插入都消去相邻自由核的纵向部分，而横向部分各多一个$\Pi(k^2)$。
用$P^2=P$逐项相乘，就得到
<span id="eq:c62-dressed-photon"></span>

$$
\begin{aligned}
\widetilde{\boldsymbol\Delta}^{\mu\nu}
 &=\frac{P^{\mu\nu}}{k^2}
   \sum_{n=0}^\infty\Pi(k^2)^n+\xi\frac{L^{\mu\nu}}{k^2}\\
 &=\frac{P^{\mu\nu}}{k^2[1-\Pi(k^2)]-i0}
   +\xi\frac{L^{\mu\nu}}{k^2-i0}.
\end{aligned}
\tag{62.6}
$$

级数可先在$|\Pi|<1$处求和，再按同一解析边界延拓。第二行在离壳求和以后，按共同的因果边界取分布极限。
将它夹在物理横向偏振或守恒源之间，纵向项消失。
在当前有质量电子的一圈计算中，$\Pi$在零动量附近正则，
因而物理光子极点的留数为$1/[1-\Pi(0)]$。LSZ要求单位留数，给出
<span id="eq:c62-photon-onshell"></span>

$$
\Pi(0)=0.
\tag{62.7}
$$

这样使用留数就不必给$k^2=0$上的$k^\mu k^\nu/k^2$单独赋值。

<span id="c62-photon-loop"></span>

## 费米圈为何恰好给出横向张量

一圈光子二点函数只有一个闭合费米圈，再加上光子动能反项。
图62a中每个顶角的内线动量差都是外动量$k$。

![光子真空极化的有向费米圈与光子二点反项](/images/srednicki/s62-c62_01.svg)

<span id="c62-photon-figure"></span>

图62a：一圈光子二点函数。上弧沿箭头带$\ell+k$，
下弧沿箭头带$\ell$；两个外光子的动量都向右。右图叉号表示光子二点反项。

用$\widetilde S(p)=(-\slashed p+m)/(p^2+m^2-i0)$，各因子给
<span id="eq:c62-photon-loop"></span>

$$
\begin{aligned}
i\Pi^{\mu\nu}(k)
 &=(-1)(ie)^2\left(\frac1i\right)^2
 \int\frac{d^d\ell}{(2\pi)^d}\widetilde\mu^\varepsilon
 \operatorname{tr}\!\left[
 \widetilde S(\ell+k)\gamma^\mu\widetilde S(\ell)\gamma^\nu\right]\\
 &\quad-i\delta Z_3(k^2g^{\mu\nu}-k^\mu k^\nu)+O(e^4).
\end{aligned}
\tag{62.8}
$$

第一个负号来自闭合费米线，两个顶角与两个内部传播子的乘积则为$e^2$。
相互作用指数的二阶展开给$1/2!$，而把两条有标签的外光子线
接到两个顶点上有$2!$种方式，两者抵消；这幅二点图的对称因子因而为1。
顶角中的$Z_1=1+O(e^2)$，在已有$e^2$的一圈项中改用1只略去$e^4$阶。
这里已预先记$d=4-\varepsilon$及$e_d=e\widetilde\mu^{\varepsilon/2}$；
原来的四维积分发散，后续的平移与对称积分都在维数正规化下进行。

令$a=\ell+k$、$b=\ell$。分子中带一次$m$的两项都有奇数个伽马矩阵，迹为零。
剩下的四矩阵迹与二矩阵迹按第47节分别为
<span id="eq:c62-photon-trace"></span>

$$
\begin{aligned}
4N^{\mu\nu}
 &=a_\alpha b_\beta\operatorname{tr}
   (\gamma^\alpha\gamma^\mu\gamma^\beta\gamma^\nu)
   +m^2\operatorname{tr}(\gamma^\mu\gamma^\nu),\\
\operatorname{tr}
   (\gamma^\alpha\gamma^\mu\gamma^\beta\gamma^\nu)
 &=4(g^{\alpha\mu}g^{\beta\nu}
      -g^{\alpha\beta}g^{\mu\nu}+g^{\alpha\nu}g^{\mu\beta}),\\
N^{\mu\nu}
 &=a^\mu b^\nu+b^\mu a^\nu-(a\cdot b+m^2)g^{\mu\nu}.
\end{aligned}
\tag{62.9}
$$

质量项前的负号来自$\operatorname{tr}(\gamma^\mu\gamma^\nu)=-4g^{\mu\nu}$，
与本书的克利福德约定一致。现在合并两个分母：
<span id="eq:c62-photon-parameters"></span>

$$
\begin{aligned}
\frac1{AB}&=\int_0^1\frac{dx}{[xA+(1-x)B]^2},\\
A&=(\ell+k)^2+m^2-i0,\qquad B=\ell^2+m^2-i0,\\
q&=\ell+xk,\qquad
xA+(1-x)B=q^2+D,\qquad
D=m^2+x(1-x)k^2-i0.
\end{aligned}
\tag{62.10}
$$

平移的雅可比为1。将$a=q+(1-x)k$、$b=q-xk$代入式
[（62.9）](#eq:c62-photon-trace)，两个交叉项合成
$(1-2x)(q^\mu k^\nu+k^\mu q^\nu-q\cdot k\,g^{\mu\nu})$。
它们对$q$为奇，故在平移不变的调节中积分为零；偶部留下
<span id="eq:c62-photon-shift"></span>

$$
N^{\mu\nu}_{\rm even}
=2q^\mu q^\nu-2x(1-x)k^\mu k^\nu
 -[q^2-x(1-x)k^2+m^2]g^{\mu\nu}.
\tag{62.11}
$$

这里尚有一个看似会产生光子质量的$m^2g^{\mu\nu}$项。
不能先把$q^\mu q^\nu$中的维数设成4；它的$O(\varepsilon)$部分
会乘紫外极点，恰好参与这一项的抵消。

对于只依赖$q^2$的标量$f$，洛伦兹协变性使二阶积分正比于$g^{\mu\nu}$。
缩并两指标便确定系数：
<span id="eq:c62-tensor-reduction"></span>

$$
\int d^dq\,q^\mu q^\nu f(q^2)
=g^{\mu\nu}C,\qquad
dC=\int d^dq\,q^2f(q^2).
\tag{62.12}
$$

用这个积分恒等式处理式
[（62.11）](#eq:c62-photon-shift)以后，$g^{\mu\nu}$的系数成为
$(2/d-1)q^2+x(1-x)k^2-m^2$。还须把含$q^2$的径向积分与不含$q^2$的积分联系起来。
记$I_1=\int_q(q^2+D)^{-1}$、$I_2=\int_q(q^2+D)^{-2}$、
$J=\int_q q^2(q^2+D)^{-2}$，其中$\int_q=\int d^dq/(2\pi)^d$。
在欧氏旋转后的收敛域$0<\operatorname{Re}d<2$、$\operatorname{Re}D>0$中，
分部积分的表面项为零，于是
<span id="eq:c62-radial-identity"></span>

$$
\begin{aligned}
0&=\int_q\frac{\partial}{\partial q^\mu}
       \frac{q^\mu}{q^2+D}=dI_1-2J,\\
J&=I_1-DI_2,\\
\left(\frac2d-1\right)J&=DI_2 .
\end{aligned}
\tag{62.13}
$$

两边随后按同一维数函数解析延拓。这个步骤说明$q^2$与参数质量$D$的替换关系只在相应积分中成立。以$D=m^2+x(1-x)k^2$代入，两个质量项消去，两个外动量项相加，得到
<span id="eq:c62-loop-transverse"></span>

$$
\int_q\frac{N^{\mu\nu}}{(q^2+D)^2}
=2x(1-x)(k^2g^{\mu\nu}-k^\mu k^\nu)\,I_2 .
\tag{62.14}
$$

因果边界从$\operatorname{Re}D>0$的等式连续取得。
现在横向性已由实际积分给出：缩并任一外动量，两项直接抵消。
这里保留了$d$维张量平均以及调节的平移不变性。

<span id="c62-photon-subtraction"></span>

## 紫外减除与真空极化的物理区域

余下的径向积分沿第14节的威克旋转与Γ函数公式求得。将本次$n=2$、
$d=4-\varepsilon$代入，并展开到有限项，
<span id="eq:c62-master-integral"></span>

$$
\begin{aligned}
\widetilde\mu^\varepsilon I_2
 &=\frac{i}{(4\pi)^{d/2}}
   \Gamma(2-d/2)\widetilde\mu^\varepsilon D^{d/2-2}\\
 &=\frac{i}{16\pi^2}\Gamma(\varepsilon/2)
   \left(\frac{4\pi\widetilde\mu^2}{D}\right)^{\varepsilon/2}\\
 &=\frac{i}{8\pi^2}
   \left[\frac1\varepsilon-\frac12\ln\frac D{\mu^2}\right]+O(\varepsilon),
\qquad \mu^2=4\pi e^{-\gamma_E}\widetilde\mu^2 .
\end{aligned}
\tag{62.15}
$$

其中$\Gamma(\varepsilon/2)=2/\varepsilon-\gamma_E+O(\varepsilon)$，
幂函数展开给$(\varepsilon/2)\ln(4\pi\widetilde\mu^2/D)$。
两者相乘产生有限对数；这就是$\mu$与$\widetilde\mu$的换算，
而不是把壳上方案换成了最小减除。
式[（62.8）](#eq:c62-photon-loop)的$-e^2$、迹的4以及横向分子的$2x(1-x)$相乘，
再除去定义中的$i$，给出
<span id="eq:c62-polarization-unsubtracted"></span>

$$
\Pi(k^2)
=-\frac{e^2}{\pi^2}\int_0^1dx\,x(1-x)
 \left[\frac1\varepsilon-\frac12\ln\frac D{\mu^2}\right]
 -\delta Z_3+O(e^4).
\tag{62.16}
$$

在$k^2=0$处，$D=m^2$不再依赖参数，且
$\int_0^1x(1-x)dx=1/6$。壳上条件因此同时固定极部与有限部分：
<span id="eq:c62-polarization-onshell"></span>

$$
\begin{aligned}
Z_3&=1-\frac{e^2}{6\pi^2}
 \left[\frac1\varepsilon-\ln\frac m\mu\right]+O(e^4),\\
\Pi_{\rm OS}(k^2)
 &=\frac{e^2}{2\pi^2}\int_0^1dx\,x(1-x)
 \ln\!\left[1+\frac{k^2}{m^2}x(1-x)-i0\right]+O(e^4).
\end{aligned}
\tag{62.17}
$$

质量非零使减除点处没有红外困难；
下一步考察电子自能时，情形就会不同。

这个有限参数积分也能用来直接观察动量依赖。作为补充，先取类空$k^2>0$，
令$z=k^2/m^2$、$v^2=z/(z+4)$，并记积分为$I(z)$。
换元$x=(1+t)/2$，利用关于$t$的偶性，再对对数分部积分，得到
<span id="eq:c62-polarization-evaluation"></span>

$$
\begin{aligned}
I(z)
 &=\frac14\int_0^1dt\,(1-t^2)
   \ln[1+z(1-t^2)/4]\\
 &=\frac{v^2}{2}\int_0^1dt\,
      \frac{t^2-t^4/3}{1-v^2t^2},\\
J_0&=\int_0^1\frac{dt}{1-v^2t^2}
     =\frac{\operatorname{artanh}v}{v},\\
J_1&=\int_0^1\frac{t^2dt}{1-v^2t^2}
     =\frac{J_0-1}{v^2},\qquad
J_2=\int_0^1\frac{t^4dt}{1-v^2t^2}
     =\frac{J_1-1/3}{v^2}.
\end{aligned}
\tag{62.18}
$$

分部积分在$t=1$的边界为零，因为原对数在那里为$\ln1$；
$t=0$处的原函数$t-t^3/3$也为零。最后两行只用多项式除法。
代回第二行就把积分实际算完：
<span id="eq:c62-polarization-limits"></span>

$$
\begin{aligned}
I(z)&=\frac12\left(1-\frac1{3v^2}\right)
 \left(\frac{\operatorname{artanh}v}{v}-1\right)+\frac1{18},
\qquad z>0,\\
\Pi_{\rm OS}(k^2)
 &=\frac{e^2k^2}{60\pi^2m^2}
   +O(e^2k^4/m^4)+O(e^4),\qquad |k^2|\ll m^2,\\
\Pi_{\rm OS}(k^2)
 &=\frac{e^2}{12\pi^2}
   \left[\ln\frac{k^2}{m^2}-\frac53\right]
   +O(e^2m^2/k^2)+O(e^4),\qquad k^2\gg m^2 .
\end{aligned}
\tag{62.19}
$$

低动量式也可从对数的首项核对：
$\int_0^1x^2(1-x)^2dx=1/30$。高动量时，参数端点之外的对数分为
$\ln z+\ln[x(1-x)]$；后者的积分为
$2\int_0^1(x-x^2)\ln x\,dx=-5/18$。精确式给出端点修正的阶数，
所以这里的高能展开仍从整个积分得到。光子极点保留在零处，
而传播核在离壳时已经获得对数变化。

类时外动量可写为$k^2=-s$。当$s>4m^2$时，参数分母在
$x_-<x<x_+$间变负，其中$x_\pm=(1\pm\beta_s)/2$、
$\beta_s=\sqrt{1-4m^2/s}$。费曼边界给
$\ln(-|D|-i0)=\ln|D|-i\pi$，故
<span id="eq:c62-polarization-cut"></span>

$$
\begin{aligned}
\operatorname{Im}\Pi_{\rm OS}(-s-i0)
 &=-\frac{e^2}{2\pi}\int_{x_-}^{x_+}x(1-x)\,dx\\
 &=-\frac{e^2}{2\pi}\left(\frac{\beta_s}{4}
                  -\frac{\beta_s^3}{12}\right)
 =-\frac{e^2}{12\pi}
   \left(1+\frac{2m^2}{s}\right)\sqrt{1-\frac{4m^2}{s}} .
\end{aligned}
\tag{62.20}
$$

在阈值以下该虚部为零。其起点是光子足以产生电子正电子对的能量，
平方根则显示两粒子相空间在阈值处的闭合。负号随本节$\Pi$及$-i0$的定义而来。

<span id="c62-infrared"></span>

## 电子质量壳为什么需要红外调节

在汤川理论中，电子与另一个有质量
粒子的中间态从$m+M$开始，单粒子极点与支点之间有一段间隔。
电动力学的中间态却可以由一个电子和一个任意软的光子组成，
最低不变质量趋于$m$；极点附近的展开因而会遇到红外奇异性。
这一点与连续谱分子的细节无关；为了说明阈值，先写出费米传播子的谱结构。
先假定极点与连续谱已由红外调节隔开，并把极点留数归一；
沿第51节的洛伦兹及宇称分解，连续部分一般有两个矩阵结构：
<span id="eq:c62-fermion-spectrum"></span>

$$
\begin{aligned}
\widetilde{\boldsymbol S}(p)
 &=\frac{-\slashed p+m}{p^2+m^2-i0}
   +\int_{m_{\rm th}^2}^{\infty}ds\,
    \frac{-\slashed p\,\rho_1(s)+\sqrt{s}\rho_2(s)}
         {p^2+s-i0},\\
\frac{-z\rho_1+\sqrt{s}\rho_2}{s-z^2}
 &=\frac{\rho_1+\rho_2}{2}\frac1{z+\sqrt{s}}
   +\frac{\rho_1-\rho_2}{2}\frac1{z-\sqrt{s}},
\qquad z=\slashed p .
\end{aligned}
\tag{62.21}
$$

第二行是离开实轴的代数分解，线性因子的边界由第一行共同的二次分母取得。
若只保留$1/(z+\sqrt{s})$这一种线性分母，就相当于额外要求$\rho_1=\rho_2$。
洛伦兹及宇称本身并不要求这一等式，所以一般要保留两个谱结构。
第51节在正度量中间态空间中导出的谱正性，也不直接施加到协变规范下的局域
带电场上。本处只使用允许的矩阵结构与实际圈图的奇点位置。

为把支点与极点隔开，先给内部光子分母加入$m_\gamma^2>0$。
在费曼规范中使用
<span id="eq:c62-photon-ir-mass"></span>

$$
\widetilde\Delta_{\mu\nu}(\ell)
=\frac{g_{\mu\nu}}{\ell^2+m_\gamma^2-i0},\qquad
m_{\rm th}=m+m_\gamma>m .
\tag{62.22}
$$

它把电子加光子的支点暂时移开。这里只改积分的调节分母，
不加入有质量矢量粒子的普罗卡纵向分子。固定$m_\gamma$时，电子传播子在
$z=-m$附近可以作通常的极点展开。定义截去外线的费米1PI图为$i\Sigma(z)$，
同样的几何级数给
<span id="eq:c62-fermion-onshell"></span>

$$
\begin{aligned}
\widetilde{\boldsymbol S}^{-1}(z)&=z+m-\Sigma(z),\\
\widetilde{\boldsymbol S}^{-1}(z)
 &=-\Sigma(-m)+[1-\Sigma'(-m)](z+m)
   +O((z+m)^2),\\
\Sigma(-m)&=0,\qquad \Sigma'(-m)=0 .
\end{aligned}
\tag{62.23}
$$

第一条件固定物理质量，第二条件把留数调成1。现在二者都在有红外调节的理论中
施加；不能先令$m_\gamma=0$，再假设精确传播子仍有一个孤立且归一良好的极点。
下面的导数会明确出现$\ln m_\gamma$，把这个问题显示出来。

这一调节最终要从可观测量中去掉。实验若只分辨能量大于$\omega_{\min}$的光子，
就须把没有额外可见光子的过程，与多发射了不可分辨光子的过程一起计数。
固定分辨率以后，先按相同精度合并虚圈修正和这些真实发射，再取$m_\gamma\to0$；
这与第26节的包容截面思路相同。有质量电子的量子电动力学中，壳上方案须与这个合并顺序一起使用，单独的虚圈振幅一般不能给出有限的最终截面。

另一种办法是同时用维数正规化记录两端的发散。一个软光子的相空间测度给
$d\omega\,\omega^{d-3}$，软发射幅的平方给$\omega^{-2}$，
故软端的幂次为$d\omega\,\omega^{d-5}$；它在$\operatorname{Re}d>4$时收敛。
而紫外端的收敛域往往在相反一侧。对质量$m>0$的外电子，
$|p\cdot k|=E\omega(1-v\cos\theta)$且$v<1$，角分母不会在严格共线方向变成零。
因此有质量电子仍有软发散，却没有严格的共线奇点。采用维数正规化时，
要把各积分作为亚纯函数延拓并分别标记UV、IR极点；
并不存在一个任意非整数维数能使原来的每个积分都绝对收敛。
尤其无尺度积分的零值可能包含两个端点极部的抵消。本节不用这一套双重记账，
而保留$\varepsilon=4-d$处理UV、$m_\gamma$处理IR的明确分工。

<span id="c62-electron-loop"></span>

## 电子自能及两个局部反项

图62b中的费米线是开链，没有闭合费米圈的额外负号。内部光子从右侧顶角
流向左侧，因此两个顶角之间的费米动量为$p+\ell$。

![电子自能的一圈光子修正及动能和质量反项](/images/srednicki/s62-c62_02.svg)

<span id="c62-electron-figure"></span>

图62b：一圈电子自能及二点反项。实线箭头由左向右，
中间带$p+\ell$；弧线光子带向左的$\ell$。右图叉号合并费米动能和质量的二点反项。

两个顶角和两条内部传播子的系数仍为$(ie)^2(1/i)^2=e^2$。
由式[（62.1）](#eq:c62-model)的二次反项读出两个插入，得到
<span id="eq:c62-electron-loop"></span>

$$
\begin{aligned}
i\Sigma(p)
 &=e^2\widetilde\mu^\varepsilon\int_\ell
 \frac{\gamma_\mu(-\slashed p-\slashed\ell+m)\gamma^\mu}
 {[(p+\ell)^2+m^2-i0](\ell^2+m_\gamma^2-i0)}\\
 &\quad-i\delta Z_2\slashed p-i\delta Z_m m+O(e^4).
\end{aligned}
\tag{62.24}
$$

动能插入的负号也可直接从傅里叶导数看出：
$i\slashed\partial e^{ipx}=-\slashed p\,e^{ipx}$，再乘作用量展开中的$i$，
便得到$-i\delta Z_2\slashed p$。同样，质量反项给$-i\delta Z_m m$。

将费米分母乘$x$、光子分母乘$1-x$，合并以后平移$q=\ell+xp$。
这一次的参数质量既含电子质量，也含调节光子质量：
<span id="eq:c62-electron-parameters"></span>

$$
\begin{aligned}
D(p^2,x)&=x(1-x)p^2+xm^2+(1-x)m_\gamma^2-i0,\\
N&=\gamma_\mu(-\slashed p-\slashed\ell+m)\gamma^\mu\\
 &=-(d-2)(\slashed p+\slashed\ell)-dm\\
 &=-(d-2)[\slashed q+(1-x)\slashed p]-dm,\\
i\Sigma(p)
 &=e^2\widetilde\mu^\varepsilon
   \int_0^1dx\int_q\frac{N}{(q^2+D)^2}
   -i\delta Z_2\slashed p-i\delta Z_m m+O(e^4).
\end{aligned}
\tag{62.25}
$$

分子缩并用的是$\gamma_\mu\gamma^\mu=-d$及
$\gamma_\mu\slashed a\gamma^\mu=(d-2)\slashed a$；
后一个式子由把右端$\gamma^\mu$依次移过$\slashed a$得到，
正是第47节已经推导的$d$维恒等式。$\slashed q$积分为零。
使用式[（62.15）](#eq:c62-master-integral)，在其余两项中保留$d=4-\varepsilon$，
便有
<span id="eq:c62-electron-unexpanded"></span>

$$
\begin{aligned}
\Sigma(z)
 &=-c\int_0^1dx\,[(2-\varepsilon)(1-x)z+(4-\varepsilon)m]
    \left[\frac1\varepsilon-\frac12\ln\frac D{\mu^2}\right]\\
 &\quad-\delta Z_2z-\delta Z_m m+O(e^4),
\qquad c=\frac{e^2}{8\pi^2},\qquad z=\slashed p .
\end{aligned}
\tag{62.26}
$$

乘开后更容易分辨反项与有限部分：
<span id="eq:c62-electron-expanded"></span>

$$
\Sigma(z)
=c\left\{\int_0^1dx\,[(1-x)z+2m]\ln\frac D{\mu^2}
 +\frac z2+m-\frac{z+4m}{\varepsilon}\right\}
 -\delta Z_2z-\delta Z_m m+O(e^4).
\tag{62.27}
$$

其中$z/2+m$来自$-\varepsilon$乘$1/\varepsilon$；
若在积分前把分子设为四维，这两个有限数就会漏掉。
极部只含$z$与$m$，因而分别要求
<span id="eq:c62-electron-uv"></span>

$$
\delta Z_2\big|_{\rm UV}=-\frac c\varepsilon,\qquad
\delta Z_m\big|_{\rm UV}=-\frac{4c}{\varepsilon}.
\tag{62.28}
$$

有限部分还需按壳上条件确定。

<span id="c62-electron-subtraction"></span>

## 留数条件中的红外对数

在$z=-m$时，$p^2=-z^2=-m^2$，参数质量变成
$D_0=x^2m^2+(1-x)m_\gamma^2$。对固定$m_\gamma>0$，它在整个积分区间为正。
把式[（62.27）](#eq:c62-electron-expanded)的对数拆为
$\ln(D/D_0)+\ln(D_0/\mu^2)$，并定义两个有限数
<span id="eq:c62-counterterm-finite"></span>

$$
\begin{aligned}
B_0&=\int_0^1dx\,\ln\frac{D_0}{\mu^2},\qquad
B_1=\int_0^1dx\,(1-x)\ln\frac{D_0}{\mu^2},\\
\delta Z_2&=c\left[-\frac1\varepsilon+\frac12+B_1-\kappa_2\right],\\
\delta Z_m&=c\left[-\frac4\varepsilon+1+2B_0-\kappa_2\right].
\end{aligned}
\tag{62.29}
$$

将后两行代回原自能，极点、常数以及$\ln D_0$的局部部分逐项抵消，得到
<span id="eq:c62-electron-mass-subtracted"></span>

$$
\Sigma(z)=c\left\{\int_0^1dx\,[(1-x)z+2m]\ln\frac{D(z)}{D_0}
                 +\kappa_2(z+m)\right\}+O(e^4).
\tag{62.30}
$$

在$z=-m$处，对数与线性项都为零，质量条件已经实现。
还剩一个$\kappa_2$，它正是单位留数要固定的有限自由度。
这个变量不是另一个耦合；式[（62.29）](#eq:c62-counterterm-finite)说明了它在两反项中的位置。

现在求导。必须连同$D$中的$p^2=-z^2$一起求导，不能把参数分母视为常数：
<span id="eq:c62-residue-integral"></span>

$$
\begin{aligned}
\frac{\partial D}{\partial z}&=-2x(1-x)z,\qquad
\left.\frac{\partial D}{\partial z}\right|_{z=-m}=2mx(1-x),\\
\left.\frac{d}{dz}
 \left([(1-x)z+2m]\ln\frac D{D_0}\right)\right|_{z=-m}
 &=m(1+x)\frac{2mx(1-x)}{D_0}
 =\frac{2m^2x(1-x^2)}{D_0},\\
\kappa_2&=-2\int_0^1dx\,\frac{m^2x(1-x^2)}
                              {x^2m^2+(1-x)m_\gamma^2}.
\end{aligned}
\tag{62.31}
$$

乘在对数前面的因子求导也会有一项，但它在减除点乘$\ln1=0$。
代入$\Sigma'(-m)=0$，就固定了最后一行的$\kappa_2$。

为求出$\kappa_2$在小光子质量下的对数项与常数项，记$a=m_\gamma/m$，取$0<a\le1/2$。
把分母暂时换成$x^2+a^2$，差额完整保留为$R(a)$：
<span id="eq:c62-ir-integral-evaluation"></span>

$$
\begin{aligned}
-\frac{\kappa_2}{2}
 &=\int_0^1dx\,\frac{x(1-x^2)}{x^2+a^2}+R(a),\\
R(a)
 &=a^2\int_0^1dx\,
 \frac{x^2(1-x^2)}
 {[x^2+a^2(1-x)](x^2+a^2)},\\
\int_0^1\frac{x\,dx}{x^2+a^2}
 &=\frac12\ln\frac{1+a^2}{a^2},\\
\int_0^1\frac{x^3dx}{x^2+a^2}
 &=\frac12\left[1-a^2\ln\frac{1+a^2}{a^2}\right].
\end{aligned}
\tag{62.32}
$$

两条初等积分都可令$y=x^2+a^2$求得。为了确定常数，尚须证明换分母的差没有
留下有限贡献。把区间在$x=1/2$分开便知
$x^2+a^2(1-x)\ge(x^2+a^2)/2$：前半段用$1-x\ge1/2$，
后半段用$x^2\ge a^2$。所以
$0\le R(a)\le2a^2\int_0^1x^2(x^2+a^2)^{-2}dx$。
再在$x=a$分开，前半段不超过$2a/3$，后半段不超过$2a$。
由此$R(a)=O(a)$，换分母的差额确实消失。两条显式积分相减以后，
<span id="eq:c62-kappa-ir"></span>

$$
\begin{aligned}
-\frac{\kappa_2}{2}
 &=\frac{1+a^2}{2}\ln\frac{1+a^2}{a^2}-\frac12+O(a),\\
\kappa_2&=-2\ln\frac m{m_\gamma}+1+O(m_\gamma/m).
\end{aligned}
\tag{62.33}
$$

红外发散来自$x\approx0$的端点；若先令$m_\gamma=0$，原积分在这里包含
$\int dx/x$。因此留数条件比单纯的质量条件更敏感，正如阈值讨论所预示的。

有限反项也可以明确写出。$a\to0$时，
$B_0=2\ln(m/\mu)-2+o(1)$，
$B_1=\ln(m/\mu)-3/2+o(1)$，分别用了
$\int_0^1\ln x\,dx=-1$和$\int_0^1x\ln x\,dx=-1/4$。
这些极限可在积分中取得：对$0<a\le1$，
$x^2\le x^2+a^2(1-x)\le1$，其对数的绝对值由$-2\ln x$支配。
于是式[（62.29）](#eq:c62-counterterm-finite)给
<span id="eq:c62-onshell-z-finite"></span>

$$
\begin{aligned}
\delta Z_2&=c\left[-\frac1\varepsilon+\ln\frac m\mu
                       +2\ln\frac m{m_\gamma}-2+o(1)\right]+O(e^4),\\
\delta Z_m&=c\left[-\frac4\varepsilon+4\ln\frac m\mu
                       +2\ln\frac m{m_\gamma}-4+o(1)\right]+O(e^4),\\
\frac{Z_m}{Z_2}
 &=1+c\left[-\frac3\varepsilon+3\ln\frac m\mu-2+o(1)\right]+O(e^4).
\end{aligned}
\tag{62.34}
$$

两反项各有红外对数，但质量比中的对数消去。电子质量与插值场的留数因而表现
不同：前者的这一圈在壳移位具有有限的$m_\gamma\to0$极限，
后者的归一仍要依赖软光子调节。式[（62.30）](#eq:c62-electron-mass-subtracted)与
[（62.31）](#eq:c62-residue-integral)是在固定$m_\gamma$下的完整参数结果；
最后一组式子只是为显示小调节质量的对数与常数所作的展开。

<span id="c62-vertex"></span>

## 顶角修正的动量次序与三参数积分

最后考察电子与光子顶角的一圈修正。
设费米子以$p$入射、以$p'$出射，光子以$k=p'-p$入射。
把具有这些外腿的1PI图之和记为$iV^\mu(p',p)$，则一圈精度为
<span id="eq:c62-vertex-definition"></span>

$$
iV^\mu(p',p)=iZ_1e\gamma^\mu+iV^\mu_{\rm loop}(p',p)+O(e^5).
\tag{62.35}
$$

沿开费米链从出射端向入射端读矩阵，右侧内部费米传播子必须在$\gamma^\mu$左边，
左侧内部传播子则在其右边：

![电子光子顶角的一圈修正及费米矩阵次序](/images/srednicki/s62-c62_03.svg)

<span id="c62-vertex-figure"></span>

图62c：一圈顶角修正。光子弧携$\ell$从右向左；
两段内部费米线分别携$p+\ell$、$p'+\ell$。中间光子以$k=p'-p$进入，
矩阵乘积从右侧出射端读回左侧入射端。

每条内线仍各给一个$1/i$，故
<span id="eq:c62-vertex-loop"></span>

$$
\begin{aligned}
iV^\mu_{\rm loop}
 &=(ie)^3\left(\frac1i\right)^3\widetilde\mu^\varepsilon
 \int_\ell\gamma^\rho\widetilde S(p'+\ell)
 \gamma^\mu\widetilde S(p+\ell)\gamma^\nu
 \widetilde\Delta_{\nu\rho}(\ell),\\
(ie)^3(1/i)^3&=e^3 .
\end{aligned}
\tag{62.36}
$$

两条费米内线加一条光子内线，共给出$(1/i)^3$；与三个顶角中的$i$相乘以后，只留下实系数$e^3$。

把动量为$p+\ell$、$p'+\ell$的两条费米分母分别配以$x_1,x_2$，
光子分母配以$x_3$。
三参数公式的$2!$来自$\Gamma(3)$，其测度总重恰好为1：
<span id="eq:c62-vertex-parameters"></span>

$$
\begin{aligned}
\frac1{A_1A_2A_3}
 &=\int dF_3\,\frac1{(x_1A_1+x_2A_2+x_3A_3)^3},\\
\int dF_3
 &:=2\int_0^1dx_1dx_2dx_3\,
     \delta(x_1+x_2+x_3-1),\qquad \int dF_3\,1=1,\\
q&=\ell+x_1p+x_2p',\\
D&=x_1(1-x_1)p^2+x_2(1-x_2)p'^2-2x_1x_2p\cdot p'\\
 &\quad+(x_1+x_2)m^2+x_3m_\gamma^2-i0 .
\end{aligned}
\tag{62.37}
$$

将$\ell^2+2\ell\cdot(x_1p+x_2p')$配成$q^2$时，
减去$(x_1p+x_2p')^2$，就给出$D$中两个$(1-x_i)$以及交叉项前的负号。
平移仍有单位雅可比。为把分子展开得紧凑，定义
$a=x_1p-(1-x_2)p'$、$b=-(1-x_1)p+x_2p'$，于是
<span id="eq:c62-vertex-numerator"></span>

$$
\begin{aligned}
N^\mu
 &=\gamma_\nu(-\slashed q+\slashed a+m)
                 \gamma^\mu(-\slashed q+\slashed b+m)\gamma^\nu\\
 &=\gamma_\nu\slashed q\gamma^\mu\slashed q\gamma^\nu
   +\widetilde N^\mu\\
 &\quad-\gamma_\nu\slashed q\gamma^\mu(\slashed b+m)\gamma^\nu
        -\gamma_\nu(\slashed a+m)\gamma^\mu\slashed q\gamma^\nu,\\
\widetilde N^\mu
 &=\gamma_\nu(\slashed a+m)\gamma^\mu(\slashed b+m)\gamma^\nu,\\
iV^\mu_{\rm loop}
 &=e^3\widetilde\mu^\varepsilon
   \int dF_3\int_q\frac{N^\mu}{(q^2+D)^3}.
\end{aligned}
\tag{62.38}
$$

两项线性$q$的积分都为零。$\widetilde N^\mu$不含圈动量，
其径向积分在四维UV收敛，所以可以在这一部分取$d=4$。
如果希望继续作外旋量收缩，还可以先把两端的$\gamma_\nu,\gamma^\nu$实际缩去。
第47节的四维夹乘给
<span id="eq:c62-vertex-finite-numerator"></span>

$$
\begin{aligned}
\gamma_\nu\slashed a\gamma^\mu\slashed b\gamma^\nu
 &=2\slashed b\gamma^\mu\slashed a,\\
\gamma_\nu\slashed a\gamma^\mu\gamma^\nu&=4a^\mu I,\qquad
\gamma_\nu\gamma^\mu\slashed b\gamma^\nu=4b^\mu I,\\
\widetilde N^\mu
 &=2\slashed b\gamma^\mu\slashed a
   +4m(a+b)^\mu I+2m^2\gamma^\mu .
\end{aligned}
\tag{62.39}
$$

这些号随本书$\{\gamma^\mu,\gamma^\nu\}=-2g^{\mu\nu}$确定；
尤其五个矩阵的夹乘使三个内部矩阵反序。
这就把式[（62.38）](#eq:c62-vertex-numerator)中的有限分子写成了较短的矩阵链。

<span id="c62-vertex-uv"></span>

## 顶角的极部与有限常数

二次$q$项的径向幂次为$\int dq/q$，是顶角中唯一的UV对数。
用式[（62.12）](#eq:c62-tensor-reduction)，并连续作两次$d$维伽马夹乘，
<span id="eq:c62-vertex-tensor-reduction"></span>

$$
\begin{aligned}
\gamma_\nu\slashed q\gamma^\mu\slashed q\gamma^\nu
 &\longrightarrow\frac{q^2}{d}
  \gamma_\nu\gamma_\rho\gamma^\mu\gamma^\rho\gamma^\nu\\
 &=\frac{(d-2)^2}{d}\,q^2\gamma^\mu,\\
\frac{(d-2)^2}{d}
 &=1-\frac34\varepsilon+O(\varepsilon^2).
\end{aligned}
\tag{62.40}
$$

这一阶$\varepsilon$会与径向积分的紫外极点相乘，因而必须保留。
记已经求出的二分母径向积分为$I_2(D)$，同一公式在$n=3$时给
<span id="eq:c62-vertex-radial-integrals"></span>

$$
\begin{aligned}
\widetilde\mu^\varepsilon I_3(D)
 &=\frac{i}{(4\pi)^{d/2}}\,
   \frac{\Gamma(3-d/2)}{2}\,
   \widetilde\mu^\varepsilon D^{d/2-3}
 =\frac{i}{32\pi^2D}+O(\varepsilon),\\
\widetilde\mu^\varepsilon\int_q\frac{q^2}{(q^2+D)^3}
 &=\widetilde\mu^\varepsilon[I_2(D)-DI_3(D)]\\
 &=\frac{i}{8\pi^2}
   \left[\frac1\varepsilon-\frac12\ln\frac D{\mu^2}-\frac14\right]
   +O(\varepsilon),\\
\frac{(d-2)^2}{d}\,
 \widetilde\mu^\varepsilon\int_q\frac{q^2}{(q^2+D)^3}
 &=\frac{i}{8\pi^2}
   \left[\frac1\varepsilon-\frac12\ln\frac D{\mu^2}-1\right]
   +O(\varepsilon).
\end{aligned}
\tag{62.41}
$$

最后的$-1$由两部分构成：约分$q^2=(q^2+D)-D$给$-1/4$，
而$-3\varepsilon/4$乘极点给$-3/4$。
这与电子自能中$z/2+m$的来源相同，都表明有限项不能在维数展开之前判断。
把两个径向积分合在一起，并用$\int dF_3=1$，便得到
<span id="eq:c62-vertex-result"></span>

$$
V^\mu_{\rm loop}(p',p)
=\frac{e^3}{8\pi^2}
\left\{\left[\frac1\varepsilon-1
 -\frac12\int dF_3\ln\frac D{\mu^2}\right]\gamma^\mu
 +\frac14\int dF_3\,\frac{\widetilde N^\mu}{D}\right\}.
\tag{62.42}
$$

现在圈动量已经完全积分；留下的两个有限参数积分保留一般离壳的$p,p'$依赖。
下一节将把它们夹在在壳旋量之间，按可测的形状因子进一步评价。
当前顶角的UV极部正比于原顶角的$\gamma^\mu$，
故$\delta Z_1 e\gamma^\mu$足以吸收它：
<span id="eq:c62-vertex-uv"></span>

$$
\delta Z_1\big|_{\rm UV}
=-\frac{e^2}{8\pi^2\varepsilon}
=\delta Z_2\big|_{\rm UV}
\qquad(\xi=1).
\tag{62.43}
$$

本节到这里仅确定$Z_1$的极部，有限部分将由[第63节的物理电荷定义](/posts/srednicki-63/#c63-charge)固定。
先检查这个一般参数结果的零外动量极限。

作为补充，取离壳的$p=p'=0$，并在已积分的有限项中令$m_\gamma\to0$。
令$u=x_1+x_2$，三角域可写为$0<u<1$、$0<x_1<u$，所以
$\int dF_3\,f(u)=2\int_0^1u f(u)\,du$。
此时$D=um^2$、$\widetilde N^\mu=2m^2\gamma^\mu$，两个参数积分成为
<span id="eq:c62-vertex-zero-momenta"></span>

$$
\begin{aligned}
\int dF_3\ln\frac D{\mu^2}
 &=2\int_0^1u\left[\ln\frac{m^2}{\mu^2}+\ln u\right]du
   =2\ln\frac m\mu-\frac12,\\
\frac14\int dF_3\,\frac{\widetilde N^\mu}{D}
 &=\gamma^\mu,\\
V^\mu_{\rm loop}(0,0)
 &=\frac{e^3}{8\pi^2}
   \left[\frac1\varepsilon-\ln\frac m\mu+\frac14\right]\gamma^\mu .
\end{aligned}
\tag{62.44}
$$

端点$u=0$的测度使$u\ln u$与$u/D$均可积，故这个离壳例没有软发散。
它仍含尚待反项减除的UV极点；这里评价的是一圈图，不是已经按物理电荷归一的顶角。

式[（62.43）](#eq:c62-vertex-uv)中两个极部相等还有一个直接解释。
先在传播子没有极点的复动量域中令$S=S(p+\ell)$、$S'=S(p'+\ell)$。
自由逆核为$\slashed p+\slashed\ell+m$，两逆核之差是$\slashed k$。
按矩阵次序相乘，再取共同的费曼边界，便有
<span id="eq:c62-one-loop-vertex-ward"></span>

$$
\begin{aligned}
S'\slashed k S
 &=S'\bigl[(S')^{-1}-S^{-1}\bigr]S=S-S',\\
k_\mu V^\mu_{\rm loop}(p',p)
 &=e[\Sigma_{\rm loop}(p)-\Sigma_{\rm loop}(p')].
\end{aligned}
\tag{62.45}
$$

第二行将第一行放回式[（62.36）](#eq:c62-vertex-loop)，其余顶角、光子核及积分完全相同，
正好留下两幅未加反项的自能之差。这是本节一圈积分自身的恒等式，

自能的UV极部为$-c(z+4m)/\varepsilon$，差中质量项相消，
于是右侧给$ec\,\slashed k/\varepsilon$，与顶角的极部一致。
在$p'=p$的微分极限中，它也给
$V^\mu_{\rm loop}(p,p)=-e\,\partial\Sigma_{\rm loop}/\partial p_\mu$；
把式[（62.27）](#eq:c62-electron-expanded)在$p=0$求导，
用$\int_0^1(1-x)\ln x\,dx=-3/4$，便得到式
[（62.44）](#eq:c62-vertex-zero-momenta)的同一个$1/4$。

至此，一圈计算分别给出了光子动能、电子动能、电子质量及电荷顶角所需的局部项。
光子质量项由横向性排除，顶角与电子自能之间则由上面的差分关系相连。
下面把这些紫外系数推广到一般$\xi$，再计算六幅四光子盒图的局部极部如何相消。
下一节沿已求出的顶角参数式施加物理归一条件，分离两个形状因子，
为随后计算电子磁矩作准备。

<span id="c62-gauge-limit"></span>

## 从规范固定作用量到零参数极限

把规范固定项与麦克斯韦项一起分部积分，可以直接核对纵向核的符号。

沿本书$(-+++)$度规，从麦克斯韦项展开可得
<span id="eq:c62-ex-1-fourier-kernel"></span>

$$
\begin{aligned}
-\frac14F_{\mu\nu}F^{\mu\nu}
&=-\frac12\partial_\mu A_\nu\partial^\mu A^\nu
 +\frac12\partial_\mu A_\nu\partial^\nu A^\mu,\\
\int d^4x\left[-\frac14F^2-\frac1{2\xi}(\partial\cdot A)^2\right]
&=\frac12\int d^4x\,
 A_\mu\bigl[g^{\mu\nu}\Box-(1-\xi^{-1})
                         \partial^\mu\partial^\nu\bigr]A_\nu\\
&=-\frac12\int\frac{d^4k}{(2\pi)^4}\,
 \widetilde A_\mu(-k)
 \bigl[k^2g^{\mu\nu}-(1-\xi^{-1})k^\mu k^\nu\bigr]
 \widetilde A_\nu(k).
\end{aligned}
\tag{62.46}
$$

第二行把导数从左侧场上移开，表面项按第57节的边界条件消去；第三行用$\partial_\mu\to ik_\mu$。特别是规范固定项分部积分后带正的$A_\mu\partial^\mu\partial^\nu A_\nu/(2\xi)$，傅里叶变换后才成为负的纵向二次型。

令$K=k^2(P+\xi^{-1}L)$，其中$P,L$由式[（62.2）](#eq:c62-gauge-kernel)定义。对$k^2\ne0$和$\xi\ne0$，直接相乘有
<span id="eq:c62-ex-1-inverse-check"></span>

$$
K^\mu{}_\rho\,
\frac{P^\rho{}_\nu+\xi L^\rho{}_\nu}{k^2}
=(P^2+L^2)^\mu{}_\nu
=\delta^\mu{}_\nu.
\tag{62.47}
$$

交叉项由$PL=LP=0$消失。因而式[（62.3）](#eq:c62-gauge-propagator)就是所求传播核，实际费曼内线再乘$1/i$。其光锥处方沿上文所写的共同边界值取得。

要理解$\xi\to0$，回到第57、58节的规范平均。作欧氏延拓后，令$f=\partial\cdot A$，其权重为$\exp[-\int f^2/(2\xi)]$。在有限模式下，每一实模式都满足
<span id="eq:c62-ex-1-lorenz-limit"></span>

$$
\lim_{\xi\downarrow0}\frac1{\sqrt{2\pi\xi}}
 \int_{-\infty}^{\infty}df\,e^{-f^2/(2\xi)}h(f)=h(0).
\tag{62.48}
$$

令$f=\sqrt\xi\,y$便把左侧变成单位高斯平均；对连续有界的$h$，支配收敛给出右侧。因此归一化的规范平均在这个极限成为$\delta[f]$，只保留$\partial_\mu A^\mu=0$的场。这就是洛伦茨规范条件；在$R_\xi$族中取零参数的这项规定也称朗道规范。传播子中的纵向系数随$\xi$消失，而作用量中的$1/\xi$须按上述极限理解。

<span id="c62-general-gauge-uv"></span>

## 一般规范参数下的紫外系数

现在求$Z_1,Z_2,Z_3,Z_m$中$e^2/\varepsilon$的系数，观察它们怎样依赖规范参数$\xi$。费曼规范的答案已在上文求出。一般$\xi$与它的差完全来自内部光子核的纵向部分，因而只须求出这一部分的大圈动量项。以下保持$m>0$及一般欧氏离壳外动量来分离UV贡献，最后按同一费曼边界延拓。

将光子核之差代入式[（62.24）](#eq:c62-electron-loop)，得到尚未加入反项的自能之差
<span id="eq:c62-ex-2-longitudinal-numerator"></span>

$$
\begin{aligned}
i\bigl[\Sigma_\xi(p)-\Sigma_1(p)\bigr]_{\rm loop}
&=e^2(\xi-1)\widetilde\mu^\varepsilon
 \int_\ell
 \frac{\slashed\ell(-\slashed\ell-\slashed p+m)\slashed\ell}
      {(\ell^2)^2[(\ell+p)^2+m^2]},\\
\slashed\ell\slashed p\slashed\ell
&=\ell^2\slashed p-2(\ell\cdot p)\slashed\ell,\\
\slashed\ell(-\slashed\ell-\slashed p+m)\slashed\ell
&=\ell^2\slashed\ell-\ell^2(\slashed p+m)
  +2(\ell\cdot p)\slashed\ell.
\end{aligned}
\tag{62.49}
$$

这里为显示UV幂次暂不写分母的共同边界符号。第二行把中间的$\slashed p$移过一个$\slashed\ell$，使用$\slashed\ell^{\,2}=-\ell^2$；因此质量项也带负号。

分母在大动量下的展开为
<span id="eq:c62-ex-2-ultraviolet-expansion"></span>

$$
\frac1{(\ell+p)^2+m^2}
=\frac1{\ell^2}-\frac{2\ell\cdot p}{(\ell^2)^2}
 +O(|\ell_E|^{-4}).
\tag{62.50}
$$

余项的系数由固定的$p_E,m$控制。分子中的$\ell^2\slashed\ell$乘第一项是奇函数，其对称积分为零；它乘第二项恰与分子最后一项乘$1/\ell^2$相消。余下的偶函数UV对数项只有
<span id="eq:c62-ex-2-ultraviolet-cancellation"></span>

$$
\frac{-\ell^2(\slashed p+m)+2(\ell\cdot p)\slashed\ell}
     {(\ell^2)^3}
-\frac{2(\ell\cdot p)\slashed\ell}{(\ell^2)^3}
=-\frac{\slashed p+m}{(\ell^2)^2}.
\tag{62.51}
$$

这次相消发生在作角平均之前，所以没有留下额外的$d$维张量系数。

为求出这个UV尾的积分，给减除项放入任意正辅助质量$M$，即用$(\ell^2+M^2-i0)^{-2}$替代其$(\ell^2)^{-2}$。两者的大动量差为$O(|\ell|^{-6})$，不会改变UV极点。式[（62.15）](#eq:c62-master-integral)随即给
<span id="eq:c62-ex-2-massive-ultraviolet-tail"></span>

$$
\widetilde\mu^\varepsilon\int_\ell
 \frac1{(\ell^2+M^2-i0)^2}
=\frac{i}{8\pi^2}\left[\frac1\varepsilon-\ln\frac M\mu\right]
 +O(\varepsilon).
\tag{62.52}
$$

辅助质量只用于这个局部减除项；完整自能仍用原来的分母。这样明确分开UV极点与IR端点，便不会因无标度积分在维数正规化中为零而丢失所求系数。

将式[（62.51）](#eq:c62-ex-2-ultraviolet-cancellation)与上式相乘，并除去自能图值中的$i$，得$\Sigma_\xi-\Sigma_1$的极部为$-(\xi-1)c(\slashed p+m)/\varepsilon$，其中$c=e^2/(8\pi^2)$。再加上上文已经算出的$-c(\slashed p+4m)/\varepsilon$，得到
<span id="eq:c62-ex-2-electron-counterterms"></span>

$$
\begin{aligned}
\Sigma_{\xi,\rm loop}\big|_{\rm UV}
 &=-\frac c\varepsilon\,[\xi\slashed p+(3+\xi)m],\\
\delta Z_2\big|_{\rm UV}&=-\frac{\xi c}{\varepsilon},\qquad
\delta Z_m\big|_{\rm UV}=-\frac{(3+\xi)c}{\varepsilon}.
\end{aligned}
\tag{62.53}
$$

两反项在$\Sigma$中分别以$-\delta Z_2\slashed p$与$-\delta Z_m m$进入，因此上式正好抵消相应的圈极点。

光子真空极化的一圈图只含内部费米线，不含规范参数，故$Z_3$仍由式[（62.17）](#eq:c62-polarization-onshell)给出。顶角则可用上文的一圈差分关系：其推导只要求自能和顶角使用同一个光子核，因而对一般$\xi$仍然成立。把刚求出的自能极部代入，质量项在差中消去，留下
<span id="eq:c62-ex-2-vertex-counterterm"></span>

$$
\begin{aligned}
k_\mu V^\mu_{\xi,\rm loop}\big|_{\rm UV}
 &=e\,[\Sigma_{\xi,\rm loop}(p)-\Sigma_{\xi,\rm loop}(p')]_{\rm UV}
 =\frac{e\xi c}{\varepsilon}\slashed k,\\
V^\mu_{\xi,\rm loop}\big|_{\rm UV}
 &=\frac{e\xi c}{\varepsilon}\gamma^\mu.
\end{aligned}
\tag{62.54}
$$

从第一行到第二行还用了局域性：顶角表面发散度为零，极部不含外动量；在本节保持宇称的矢量理论中，所需的常矩阵向量只能正比于$\gamma^\mu$。因此不存在未被任意$k_\mu$的缩并确定的另一个局部系数。

四个所求系数合为
<span id="eq:c62-ex-2-all-ultraviolet-coefficients"></span>

$$
\begin{aligned}
Z_1\big|_{\rm UV}=Z_2\big|_{\rm UV}
 &=1-\frac{\xi e^2}{8\pi^2\varepsilon}+O(e^4),\\
Z_3\big|_{\rm UV}
 &=1-\frac{e^2}{6\pi^2\varepsilon}+O(e^4),\\
Z_m\big|_{\rm UV}
 &=1-\frac{(3+\xi)e^2}{8\pi^2\varepsilon}+O(e^4),\\
\left(\frac{Z_m}{Z_2}-1\right)_{\rm UV}
 &=-\frac{3e^2}{8\pi^2\varepsilon}+O(e^4).
\end{aligned}
\tag{62.55}
$$

这里前三行的记号表示只列出常数1与UV极部。取$\xi=1$回到上文的全部系数，裸质量比的极点则对任意$\xi$相同。取$\xi=0$时，$Z_1,Z_2$的一圈UV极点同时消失，在只减极部的方案中可写成$Z_1=Z_2=1+O(e^4)$。本节采用的壳上方案还要求固定有限部分，电子的单位留数又含红外依赖，完整的壳上$Z_1,Z_2$不能只凭UV极部为零就置为1。

<span id="c62-four-photon"></span>

## 六幅四光子盒图的紫外抵消

四条外光子线围绕一个费米圈排列，单独一图的最高动量项给出对数发散；只有把外光子的所有排列放在一起，规范不变性才表现出来。下面先求出这些发散项的张量结构，再说明它与允许的局部反项有什么关系。

取四个外动量全部入射，$\sum_{j=1}^4k_j=0$，相应洛伦兹指标依次为 $\mu,\nu,\rho,\sigma$。保持电子质量 $m>0$，先在一般欧氏外动量区域计算，再按共同的费曼边界值延拓到所需物理区域。这样提取紫外极点时不会混入无质量或特殊动量配置引起的红外问题。仍用 $d=4-\varepsilon$、$e_d=e\widetilde\mu^{\varepsilon/2}$ 和 $\operatorname{tr}1=4$；这里没有 $\gamma_5$，所以全部克利福德缩并可按第47节的形式 $d$ 维规则进行。

<span id="c62-ex62-3-orderings"></span>

### 六种排列与共同的领先项

沿费米矩阵链固定从外光子1开始读，剩下三个标签有 $3!$ 种次序：
<span id="eq:c62-ex-3-six-orderings"></span>

$$
(1234),\quad(1243),\quad(1324),\quad
(1342),\quad(1423),\quad(1432).
\tag{62.56}
$$

循环更换起点已经由“从1开始”消去。固定四个外标签后，每个有向盒图的对称因子为1；反向的矩阵链仍在上述六图中，不能再除以一个2。从[第53节的有向圈计数](/posts/srednicki-53/#c53-dirac-gaussian)看，同一个结论来自四次背景插入的循环因子 $1/4$：给四个插入标号后，$4!/4=6$。这里沿用狄拉克场的闭圈负号，每图的公共系数为
<span id="eq:c62-ex-3-common-sign"></span>

$$
-(ie_d)^4\left(\frac1i\right)^4=-e_d^4.
\tag{62.57}
$$

以 $\mathcal B_{1234}^{\mu\nu\rho\sigma}$ 表示第一图已经包括全部 $i$ 因子的图值，采用一组与全入射外动量相容的路由，可写为
<span id="eq:c62-ex-3-full-box"></span>

$$
\begin{aligned}
\mathcal B_{1234}^{\mu\nu\rho\sigma}
={}&-e_d^4\int\frac{d^d\ell}{(2\pi)^d}\,
\operatorname{tr}\bigl[
\gamma^\mu\widetilde S(\ell-k_1)
\gamma^\nu\widetilde S(\ell-k_1-k_2)\\
&\hspace{29mm}\times
\gamma^\rho\widetilde S(\ell+k_4)
\gamma^\sigma\widetilde S(\ell)\bigr],\\
\widetilde S(p)&=\frac{-\slashed p+m}{p^2+m^2-i0}.
\end{aligned}
\tag{62.58}
$$

例如在指标 $\nu$ 的顶点，矩阵链左、右传播子的动量差为 $k_2$；其余三点同样满足守恒。别的排列只需同时排列光子动量与指标。

大动量下，每条费米传播子为 $O(\ell^{-1})$，故四维表面发散度为 $4-4=0$。唯一可能的极点是外动量的零次局部项；减去这一项后，至少多出一个外动量或质量与大动量之比，径向积分便在紫外收敛。为使所减项在红外也有定义，保留分母中的正质量 $m$。于是
<span id="eq:c62-ex-3-uv-subtraction"></span>

$$
\begin{aligned}
\mathcal B_{1234}^{\mu\nu\rho\sigma}
&=-e_d^4\int\frac{d^d\ell}{(2\pi)^d}\,
\frac{N_{1234}^{\mu\nu\rho\sigma}(\ell)}
     {(\ell^2+m^2-i0)^4}
+\mathcal B_{1234,\mathrm{rem}}^{\mu\nu\rho\sigma},\\
N_{1234}^{\mu\nu\rho\sigma}(\ell)
&=\operatorname{tr}
(\gamma^\mu\slashed\ell\gamma^\nu\slashed\ell
 \gamma^\rho\slashed\ell\gamma^\sigma\slashed\ell).
\end{aligned}
\tag{62.59}
$$

四个分子中的负号相乘为正。余项的大动量行为至少为 $O(|\ell|^{-5})$，在 $d$ 接近4时紫外可积；因此全部 $1/\varepsilon$ 极点都在显示的积分里。盒图没有需要另行减去的一圈子发散，保留$m$使减除项在红外可积。

<span id="c62-ex62-3-tensors"></span>

### 求出单图的角平均张量

以下横线表示先作威克旋转后的欧氏角平均，再将指标写回协变形式。旋转对称性和指标缩并分别确定二阶、四阶角平均：
<span id="eq:c62-ex-3-angular-moments"></span>

$$
\begin{aligned}
\overline{\ell^\alpha\ell^\beta}
&=\frac{\ell^2}{d}g^{\alpha\beta},\\
\overline{\ell^\alpha\ell^\beta\ell^\gamma\ell^\delta}
&=\frac{(\ell^2)^2}{d(d+2)}
\bigl(g^{\alpha\beta}g^{\gamma\delta}
+g^{\alpha\gamma}g^{\beta\delta}
+g^{\alpha\delta}g^{\beta\gamma}\bigr).
\end{aligned}
\tag{62.60}
$$

第一式与 $g_{\alpha\beta}$ 缩并给 $\ell^2$，因而系数为 $1/d$；第二式与 $g_{\alpha\beta}g_{\gamma\delta}$ 缩并，括号给 $d^2+2d$，所以分母为 $d(d+2)$。

记三个独立的度规配对为
<span id="eq:c62-ex-3-tensor-basis"></span>

$$
\begin{aligned}
P^{\mu\nu\rho\sigma}&=g^{\mu\nu}g^{\rho\sigma},&
Q^{\mu\nu\rho\sigma}&=g^{\mu\rho}g^{\nu\sigma},&
R^{\mu\nu\rho\sigma}&=g^{\mu\sigma}g^{\nu\rho},\\
\overline{N_{1234}^{\mu\nu\rho\sigma}}
&=(\ell^2)^2H_{1234}^{\mu\nu\rho\sigma},&
H_{1234}&=a_d(P+R)+b_dQ.
\end{aligned}
\tag{62.61}
$$

无 $\gamma_5$ 的角平均只能给这些度规乘积。迹的循环性将 $P,R$ 互换，所以二者系数相同。只需求出 $a_d,b_d$ 即可。

先用任意辅助向量 $A_\mu$ 收缩四个外指标。令 $L=\slashed\ell$、$X=\slashed A$、$s=\ell\cdot A$、$r=\ell^2A^2$。本书的克利福德号给
<span id="eq:c62-ex-3-lx-polynomial"></span>

$$
LX+XL=-2s,\qquad
L^2=-\ell^2,\qquad X^2=-A^2,
\qquad (LX)^2=-2s(LX)-r.
\tag{62.62}
$$

又有 $\operatorname{tr}(LX)=-4s$，所以
<span id="eq:c62-ex-3-four-background-trace"></span>

$$
\begin{aligned}
\operatorname{tr}[(LX)^2]&=8s^2-4r,\\
\operatorname{tr}[(LX)^4]
&=4s^2\operatorname{tr}[(LX)^2]
+4sr\operatorname{tr}(LX)+4r^2\\
&=32s^4-32s^2r+4r^2.
\end{aligned}
\tag{62.63}
$$

将式[（62.60）](#eq:c62-ex-3-angular-moments)用于 $s^2,s^4$，得到
<span id="eq:c62-ex-3-background-average"></span>

$$
\begin{aligned}
\overline{\operatorname{tr}[(LX)^4]}
&=4(\ell^2)^2(A^2)^2
\left[\frac{24}{d(d+2)}-\frac8d+1\right]\\
&=\frac{4(d-2)(d-4)}{d(d+2)}
(\ell^2)^2(A^2)^2.
\end{aligned}
\tag{62.64}
$$

另一方面，$P,Q,R$ 与四个相同的 $A$ 缩并都给 $(A^2)^2$，故
<span id="eq:c62-ex-3-first-coefficient-equation"></span>

$$
2a_d+b_d=\frac{4(d-2)(d-4)}{d(d+2)}.
\tag{62.65}
$$

为了分开两个系数，再以 $g_{\mu\nu}$ 缩并原迹。第47节的缩并式和四伽马迹给
<span id="eq:c62-ex-3-contraction-identities"></span>

$$
\gamma^\mu L\gamma_\mu=(d-2)L,\qquad
\operatorname{tr}(\gamma^\rho L\gamma^\sigma L)
=4(2\ell^\rho\ell^\sigma-g^{\rho\sigma}\ell^2).
\tag{62.66}
$$

于是
<span id="eq:c62-ex-3-second-coefficient-equation"></span>

$$
\begin{aligned}
g_{\mu\nu}\overline{N_{1234}^{\mu\nu\rho\sigma}}
&=-(d-2)\ell^2\,
\overline{\operatorname{tr}(\gamma^\rho L\gamma^\sigma L)}\\
&=\frac{4(d-2)^2}{d}(\ell^2)^2g^{\rho\sigma},\\
(d+1)a_d+b_d&=\frac{4(d-2)^2}{d}.
\end{aligned}
\tag{62.67}
$$

用最后一式减去式[（62.65）](#eq:c62-ex-3-first-coefficient-equation)，先解出
$a_d=4(d-2)/(d+2)$，再代回求 $b_d$，便得到单图所需的完整结果：
<span id="eq:c62-ex-3-ordered-tensor"></span>

$$
H_{1234}
=\frac{4(d-2)}{d(d+2)}
\bigl[d(P+R)-(d+4)Q\bigr].
\tag{62.68}
$$

例如取 $\mu=\nu=0,\rho=\sigma=1$，在四维有 $P=-1,Q=R=0$，该分量等于 $-4/3$，确实可以给出非零的单图对数极点。

<span id="c62-ex62-3-cancellation"></span>

### 六图求和与有限余项

对六个排列，两个相隔一个顶点的外指标总是出现在式[（62.68）](#eq:c62-ex-3-ordered-tensor)的负系数配对中。按固定的全局指标 $\mu,\nu,\rho,\sigma$ 排列，四维极点系数分成三对：

| 循环排列        | $H_{1\pi}$ 在 $d=4$ 的值 |
| --------------- | ------------------------ |
| $(1234),(1432)$ | $\frac43(P+R-2Q)$        |
| $(1243),(1342)$ | $\frac43(P+Q-2R)$        |
| $(1324),(1423)$ | $\frac43(Q+R-2P)$        |

每个度规配对在六图中得到四次正系数、两次负二倍系数，所以极点逐张量相消。令 $\pi$ 排列标签2、3、4。保留 $d$ 而不先令其等于4，六图之和则为
<span id="eq:c62-ex-3-six-tensor-sum"></span>

$$
\begin{aligned}
\sum_{\pi\in S_3}H_{1\pi}
&=\frac{8(d-2)(d-4)}{d(d+2)}(P+Q+R)\\
&=-\frac23\varepsilon(P+Q+R)+O(\varepsilon^2).
\end{aligned}
\tag{62.69}
$$

这一步所消掉的是 $1/\varepsilon$ 的留数，尚不能把整个显示积分置为零。

为看清区别，将公共径向积分也写出来。威克旋转提供因子 $i$；用施温格参数表示分母，并对高斯的参数求两次导数以产生 $(\ell_E^2)^2$，可得
<span id="eq:c62-ex-3-radial-integral"></span>

$$
\begin{aligned}
J_d(m)
&=\int\frac{d^d\ell}{(2\pi)^d}
\frac{(\ell^2)^2}{(\ell^2+m^2-i0)^4}\\
&=\frac{i}{6}\int_0^\infty dt\,t^3e^{-tm^2}
\frac{d(d+2)}{4(4\pi)^{d/2}}t^{-d/2-2}\\
&=\frac{i}{(4\pi)^{d/2}}\frac{d(d+2)}{24}
\Gamma\!\left(2-\frac d2\right)(m^2)^{d/2-2}\\
&=\frac{i}{(4\pi)^2}\left(\frac2\varepsilon+O(1)\right).
\end{aligned}
\tag{62.70}
$$

其中 $\Gamma(4)=6$，而二次参数导数给 $(d/2)(d/2+1)=d(d+2)/4$。正质量使参数积分的大 $t$ 端收敛；小 $t$ 端的极点就是所讨论的紫外发散。将其与式[（62.69）](#eq:c62-ex-3-six-tensor-sum)相乘，六图领先减除项满足
<span id="eq:c62-ex-3-evanescent-finite-part"></span>

$$
\begin{aligned}
\mathcal B_{\rm lead}
&=-e_d^4J_d(m)\sum_{\pi\in S_3}H_{1\pi},\\
\lim_{\varepsilon\to0}\varepsilon\mathcal B_{\rm lead}&=0,\\
\lim_{\varepsilon\to0}\mathcal B_{\rm lead}
&=\frac{4ie^4}{3(4\pi)^2}(P+Q+R).
\end{aligned}
\tag{62.71}
$$

这里最后一行只是式[（62.59）](#eq:c62-ex-3-uv-subtraction)所选择的共同领先项之和。完整盒图还包含六个紫外收敛的余项；这些余项保留外动量依赖，并与该有限常数共同组成规范不变的结果。领先项与余项的分割本身不分别满足沃德恒等式，不能把这个有限常数单独解释成新的 $A^4$ 相互作用。也不能在角平均后直接删去 $d-4$，因为这样会漏掉它乘极点产生的有限贡献。

<span id="c62-ex62-3-gauge"></span>

### 规范不变性为何要求这个结果

这六图的和必须对每条外光子动量横向。其代数起点是第58节的纵向插入式[纵向插入式](/posts/srednicki-58/#eq:c58-longitudinal-identity)。写 $\mathscr D(p)=\slashed p+m$，便有
<span id="eq:c62-ex-3-ward-insertion"></span>

$$
\begin{aligned}
\slashed k&=\mathscr D(p+k)-\mathscr D(p),\\
\widetilde S(p+k)\slashed k\,\widetilde S(p)
&=\widetilde S(p)-\widetilde S(p+k).
\end{aligned}
\tag{62.72}
$$

把一个光子依次插入同一费米圈的各个相邻位置，右边两项便成对抵消；闭圈没有外费米端点项。固定其余三个光子后，在循环次序234中插入1得到 $(1234),(1342),(1423)$，在反向次序243中插入1得到 $(1243),(1432),(1324)$；两个次序的三个插入位置正好组成上述六图。某些相消项需要平移圈动量，所以必须对全部图采用同一个允许动量平移的调节。可先在 $m>0$、欧氏外动量及 $0<\operatorname{Re}d<3$ 的共同收敛区域完成这些积分移位，再解析延拓至 $d=4-\varepsilon$。这里只有矢量顶角，所用的 $d$ 维迹循环性与反对易关系相容；第58节已经说明相容的费米测度保持这项矢量规范对称性。这样六图之和满足
<span id="eq:c62-ex-3-four-ward-identities"></span>

$$
\begin{aligned}
k_{1\mu}\sum_\pi\mathcal B_{1\pi}^{\mu\nu\rho\sigma}&=0,\\
k_{2\nu}\sum_\pi\mathcal B_{1\pi}^{\mu\nu\rho\sigma}&=0,
\qquad\text{另两腿同理}.
\end{aligned}
\tag{62.73}
$$

还可以完全从可能的局部反项看出为什么不允许留下极点。表面发散度为零，故极部没有外动量，即对应不含导数的四次势项。洛伦兹不变性与玻色对称性只容许它正比于 $(A_\mu A^\mu)^2$。但在 $A_\mu\to A_\mu-\partial_\mu\Gamma$ 下，
<span id="eq:c62-ex-3-forbidden-a4"></span>

$$
\begin{aligned}
\delta_\Gamma(A_\mu A^\mu)^2
&=-4A^2A^\mu\partial_\mu\Gamma,\\
\delta_\Gamma\int d^4x\,(A^2)^2
&=4\int d^4x\,\Gamma\,\partial_\mu(A^2A^\mu).
\end{aligned}
\tag{62.74}
$$

第二式取紧支撑的规范参数并作分部积分，结果一般不为零，因而第一式也不是可忽略的全导数。等价地，一个局部常张量 $c(P+Q+R)$ 与任意 $k_{1\mu}$ 缩并并不为零，式[（62.73）](#eq:c62-ex-3-four-ward-identities)因而要求其极点系数 $c$ 消失。

四维局部规范不变的纯光子算符在质量维数4只能由 $F_{\mu\nu}$ 的二次式构成，例如 $F_{\mu\nu}F^{\mu\nu}$；$F_{\mu\nu}\widetilde F^{\mu\nu}$则是阿贝尔理论的全导数。它们都只有两个光子场，不能提供四光子反项。四光子的局部规范不变项要到维数8才出现，例如
<span id="eq:c62-ex-3-finite-light-scattering"></span>

$$
\begin{gathered}
\frac1{m^4}(F_{\mu\nu}F^{\mu\nu})^2,
\qquad
\frac1{m^4}(F_{\mu\nu}\widetilde F^{\mu\nu})^2,\\
\widetilde F^{\mu\nu}
=\frac12\epsilon^{\mu\nu\alpha\beta}F_{\alpha\beta}.
\end{gathered}
\tag{62.75}
$$

这些结构可以出现在 $|k_i|\ll m$ 的有限低能展开中。规范不变性排除了所需维数的紫外反项，光子仍可通过虚电子圈发生散射，其振幅由六图剩下的有限动量积分决定。

---

[← 第 61 节](/posts/srednicki-61/) · [章节地图](/srednicki/) · [第 63 节 →](/posts/srednicki-63/)
