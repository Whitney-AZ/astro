---
title: 'Srednicki §95 超对称'
date: 2026-09-14
category: 笔记
tags: [物理, 量子场论, Srednicki]
series: 'Srednicki QFT'
srednickiSections: [95]
hideFromHome: true
draft: false
---

<span id="c95"></span>

规范对称性把具有相同自旋的场组织在同一表示中。另一种连续变换可以把标量变成旋量，也把旋量变回玻色场。这样的生成元带有旋量指标，而且是格拉斯曼奇的。它与通常时空生成元组成的代数，称为超对称代数（supersymmetry algebra）。用反对易坐标构成的超空间，可以把各分量场及其变换合写在一个有限的格拉斯曼展开中；作用量随后由这个展开的最高分量构造。

以下采用第69节的规范群记法，以及第34–36章的旋量升降和奇场换序规则。先讨论无规范耦合的手征场，再引入实矢量超场和超规范变换，最后推广到非阿贝尔群。

<span id="c95-algebra"></span>

## 从超荷到超空间

设$Q_{aA}$为左手超荷（supercharge），$a=1,2$是旋量指标，$A=1,\ldots,\mathcal N$区分不同的超荷。它的物理Hilbert空间伴随记为$Q^\dagger_{\dot aA}$。除了已有的Poincaré代数，我们取
<span id="eq:c95-superalgebra"></span>

$$
\begin{aligned}
\relax[Q_{aA},P^\mu]&=[Q^\dagger_{\dot aA},P^\mu]=0,\\
[Q_{aA},M^{\mu\nu}]&=(S_L^{\mu\nu})_a{}^cQ_{cA},\\
[Q^\dagger_{\dot aA},M^{\mu\nu}]&=(S_R^{\mu\nu})_{\dot a}{}^{\dot c}Q^\dagger_{\dot cA},\\
\{Q_{aA},Q_{bB}\}&=Z_{AB}\epsilon_{ab},\\
\{Q_{aA},Q^\dagger_{\dot bB}\}&=-2\delta_{AB}\sigma^\mu_{a\dot b}P_\mu .
\end{aligned}
\tag{95.1}
$$

第一行使超荷不随时间改变，也不改变态的四动量；第二、三行规定它们的旋量变换。最后一行尤为特别：两个奇变换的反对易子产生普通时空平移。因而超对称同时联系粒子的自旋和动力学。

交换第四行的两个完整标签$(a,A)$与$(b,B)$，左边不变，而$\epsilon_{ba}=-\epsilon_{ab}$，所以
<span id="eq:c95-central-antisymmetry"></span>

$$
Z_{AB}=-Z_{BA}.
\tag{95.2}
$$

这里取$Z_{AB}$与全部生成元对易，称它为中心荷（central charge）。本节只用$\mathcal N=1$；这时$Z_{11}=0$，可以省去内部指标。

如果已经找到分量场的超变换，超流与超荷便可由第22节的Noether程序得到。具体说，把常量奇参数暂换为$\varepsilon^a(x)$，从作用量变分中收集$\partial_\mu\varepsilon^a$的系数，便得到相应超流$j^\mu_a$；在运动方程成立时$\partial_\mu j^\mu_a=0$，其空间积分给守恒的$Q_a$。现在我们先反过来，从所需代数寻找较方便的场表示。

给时空坐标添上$\theta^a$及$\bar\theta^{\dot a}\equiv\theta^{*\dot a}$。在计算时把它们作为独立奇坐标，故
<span id="eq:c95-odd-coordinates"></span>

$$
\{\theta^a,\theta^b\}=\{\bar\theta^{\dot a},\bar\theta^{\dot b}\}
 =\{\theta^a,\bar\theta^{\dot b}\}=0.
\tag{95.3}
$$

超场（superfield）就是这些变量的函数$\Phi(x,\theta,\bar\theta)$。四个奇生成元的多项式只有$2^4=16$个独立单项式，所以“函数”在奇坐标中必为有限多项式，其系数是通常的时空场。若整个超场为偶，则奇次坐标的系数为费米场，偶次的系数为玻色场。所有费米系数也与$\theta,\bar\theta$反对易，这一点在取乘积时同样要用到。

<span id="c95-odd-calculus"></span>

### 左导数、右导数与共轭

定义左导数$\partial_a=\partial/\partial\theta^a$、$\bar\partial_{\dot a}=\partial/\partial\bar\theta^{\dot a}$，使它在变分$\delta X=\delta\theta^a\partial_aX$中直接给出右侧系数。若$X$为齐次奇偶量，移动变分越过$X$便得到
<span id="eq:c95-left-leibniz"></span>

$$
\begin{aligned}
\partial_a(XY)&=(\partial_aX)Y+(-1)^{|X|}X(\partial_aY),\\
\partial_a\theta^b&=\delta_a{}^b,\qquad
\{\partial_a,\theta^b\}=\delta_a{}^b,\\
\{\partial_a,\bar\theta^{\dot b}\}&=0,
\qquad\{\partial_a,\partial_b\}=0.
\end{aligned}
\tag{95.4}
$$

第二行前式是导数的作用值，后式是作用于任意多项式的算符恒等式。例如$\partial_2(\theta^1\theta^2)=-\theta^1$，因为导数须越过第一个奇变量。点导数有完全相同的规则。

第35节已规定，共轭反转乘积次序。因此若右导数定义为
$\delta X=(X\overleftarrow\partial_a)\delta\theta^a$，则
<span id="eq:c95-derivative-conjugation"></span>

$$
\begin{aligned}
(\partial_aX)^*&=X^*\overleftarrow{\bar\partial}_{\dot a},\\
X\overleftarrow\partial_a&=(-1)^{|X|+1}\partial_aX.
\end{aligned}
\tag{95.5}
$$

第一行由变分等式反序共轭直接得到；第二行来自把$\delta\theta$从最左移到最右，所越过的导数系数奇偶为$|X|+1$。这说明，共轭后先改变的是作用侧别。

例如取$X=\theta^a$，导数作用值的共轭为1。将共轭后的右导数移回左边时，符号由式[（95.5）](#eq:c95-derivative-conjugation)中的$|X|$决定。以下把两套配对微分算符分别记为$\mathcal Q$和$\overline{\mathcal Q}$，物理态空间的超荷则记为$Q,Q^\dagger$。

<span id="c95-supertranslations"></span>

## 超平移的微分实现

普通平移满足$[\Phi,P^\mu]=-i\partial^\mu\Phi$。仿照它，先对偶超场要求
<span id="eq:c95-superfield-action"></span>

$$
[\Phi,Q_a]=-i\mathcal Q_a\Phi,\qquad
[\Phi,Q^\dagger_{\dot a}]=-i\overline{\mathcal Q}_{\dot a}\Phi.
\tag{95.6}
$$

如果只取$\mathcal Q_a=\partial_a$和$\overline{\mathcal Q}_{\dot a}=-\bar\partial_{\dot a}$，混合反对易子便为零，不能给出时空平移。因此每个算符还应含有另一种奇坐标乘时空导数。取如下形式：
<span id="eq:c95-q-differential"></span>

$$
\begin{aligned}
\mathcal Q_a&=\partial_a+i\sigma^\mu_{a\dot c}\bar\theta^{\dot c}\partial_\mu,\\
\overline{\mathcal Q}_{\dot b}&=-\bar\partial_{\dot b}
                 -i\theta^c\sigma^\mu_{c\dot b}\partial_\mu .
\end{aligned}
\tag{95.7}
$$

检验其代数只需把四类乘积分别收集。混合反对易子中，两个接触项为
<span id="eq:c95-q-contact-terms"></span>

$$
\begin{aligned}
\{\partial_a,-i\theta^c\sigma^\mu_{c\dot b}\partial_\mu\}
 &=-i\sigma^\mu_{a\dot b}\partial_\mu,\\
\{i\sigma^\mu_{a\dot c}\bar\theta^{\dot c}\partial_\mu,-\bar\partial_{\dot b}\}
 &=-i\sigma^\mu_{a\dot b}\partial_\mu.
\end{aligned}
\tag{95.8}
$$

纯奇导数相加为零；两个坐标乘导数的项则含$\bar\theta\theta+\theta\bar\theta=0$。同类两个$\mathcal Q$中，导数和所乘坐标属于不同种类，没有接触项，余项也两两相消。因此
<span id="eq:c95-q-algebra"></span>

$$
\begin{aligned}
\{\mathcal Q_a,\mathcal Q_b\}
 &=\{\overline{\mathcal Q}_{\dot a},\overline{\mathcal Q}_{\dot b}\}=0,\\
\{\mathcal Q_a,\overline{\mathcal Q}_{\dot b}\}
 &=-2i\sigma^\mu_{a\dot b}\partial_\mu .
\end{aligned}
\tag{95.9}
$$

这里两个相等的接触贡献就是因子2的来源。

还要核对微分实现的号与算符代数相容。对偶$\Phi$，先展开两个嵌套的分次括号，得到
<span id="eq:c95-jacobi-expanded"></span>

$$
\begin{aligned}
\{[\Phi,Q],Q^\dagger\}
={}&\Phi QQ^\dagger-Q\Phi Q^\dagger
       +Q^\dagger\Phi Q-Q^\dagger Q\Phi,\\
\{[\Phi,Q^\dagger],Q\}
={}&\Phi Q^\dagger Q-Q^\dagger\Phi Q
       +Q\Phi Q^\dagger-QQ^\dagger\Phi.
\end{aligned}
\tag{95.10}
$$

中间四项相消，剩下$[\Phi,\{Q,Q^\dagger\}]$。由式[（95.1）](#eq:c95-superalgebra)，它等于$2i\sigma^\mu\partial_\mu\Phi$。另一方面，式[（95.6）](#eq:c95-superfield-action)的两个$-i$乘式[（95.9）](#eq:c95-q-algebra)，正好也给$+2i\sigma^\mu\partial_\mu\Phi$。

对一般奇偶的场$X$，同一计算用右作用分次括号
<span id="eq:c95-graded-right-action"></span>

$$
R_aX=XQ_a-(-1)^{|X|}Q_aX,\qquad
(R_a\bar R_{\dot b}+\bar R_{\dot b}R_a)X
 =[X,\{Q_a,Q^\dagger_{\dot b}\}].
\tag{95.11}
$$

奇分量于是出现反对易子，偶分量出现交换子。后面从超场读出费米分量的变换时，正是按这个规则匹配。

<span id="c95-chiral-constraint"></span>

## 手征约束及其一般解

一个无约束超场包含许多分量。我们希望施加一个与超变换相容的条件，把它约化成较小的多重态。为此把式[（95.7）](#eq:c95-q-differential)中两个时空导数项的号同时反转，定义超协变导数（supercovariant derivative）
<span id="eq:c95-supercovariant-derivatives"></span>

$$
\begin{aligned}
\mathcal D_a&=\partial_a-i\sigma^\mu_{a\dot c}\bar\theta^{\dot c}\partial_\mu,\\
\overline{\mathcal D}_{\dot b}&=-\bar\partial_{\dot b}
                       +i\theta^c\sigma^\mu_{c\dot b}\partial_\mu .
\end{aligned}
\tag{95.12}
$$

沿用刚才的接触项计算，两个$\mathcal D$之间的混合贡献都变成$+i\sigma\partial$。一个$\mathcal D$与一个$\mathcal Q$之间则是一个正、一个负。例如$\{\partial_a,-i\theta\sigma\partial\}=-i\sigma\partial$，而$\{-i\sigma\bar\theta\partial,-\bar\partial\}=+i\sigma\partial$。故
<span id="eq:c95-d-algebra"></span>

$$
\begin{gathered}
\{\mathcal D_a,\mathcal D_b\}
 =\{\overline{\mathcal D}_{\dot a},\overline{\mathcal D}_{\dot b}\}=0,
\qquad
\{\mathcal D_a,\overline{\mathcal D}_{\dot b}\}
 =2i\sigma^\mu_{a\dot b}\partial_\mu,\\
\{\mathcal D_a,\mathcal Q_b\}
 =\{\mathcal D_a,\overline{\mathcal Q}_{\dot b}\}
 =\{\overline{\mathcal D}_{\dot a},\mathcal Q_b\}
 =\{\overline{\mathcal D}_{\dot a},\overline{\mathcal Q}_{\dot b}\}=0.
\end{gathered}
\tag{95.13}
$$

特别是，若$\overline{\mathcal D}_{\dot a}\Phi=0$，那么$\overline{\mathcal D}_{\dot a}\mathcal Q_b\Phi=-\mathcal Q_b\overline{\mathcal D}_{\dot a}\Phi=0$；对另一超变换也一样。因此可以一致地定义左手手征超场（left-chiral superfield）及其共轭：
<span id="eq:c95-chiral-conditions"></span>

$$
\overline{\mathcal D}_{\dot a}\Phi=0,\qquad
\mathcal D_a\Phi^\dagger=0.
\tag{95.14}
$$

第二个条件也可以直接对后面给出的共轭展开求导检验。

解这个约束的关键是改用
<span id="eq:c95-chiral-coordinates"></span>

$$
y^\mu=x^\mu-iB^\mu,\qquad B^\mu=\theta\sigma^\mu\bar\theta.
\tag{95.15}
$$

点左导数越过$\theta$产生负号，所以$\bar\partial_{\dot a}y^\mu=+i\theta^c\sigma^\mu_{c\dot a}$。将它代入式[（95.12）](#eq:c95-supercovariant-derivatives)，两项相消：
<span id="eq:c95-chiral-chain-rule"></span>

$$
\overline{\mathcal D}_{\dot a}\theta^b=0,\qquad
\overline{\mathcal D}_{\dot a}y^\mu=0,\qquad
\left.\overline{\mathcal D}_{\dot a}\right|_{y,\theta}
 =-\bar\partial_{\dot a}.
\tag{95.16}
$$

坐标变化的逆为$x=y+iB$；其幂零部分只需有限Taylor展开。在新坐标中，约束就是说与$\bar\theta$无关。因此局部一般解为$\Phi(y,\theta)$，而不只是找到了一个特殊解。两个独立的$\theta$使三次积为零，故一般偶手征场可写为
<span id="eq:c95-chiral-multiplet"></span>

$$
\Phi(y,\theta)=A(y)+\sqrt2\theta^a\psi_a(y)+tF(y),
\qquad t=\theta^a\theta_a.
\tag{95.17}
$$

$A,F$为复标量，$\psi$为左手Weyl场。一次项的$\sqrt2$是约定，稍后它使标准动能的归一较简单。

<span id="c95-theta-expansion"></span>

### 展开回普通时空坐标

先把反复出现的二次积算清。写$\theta^1=u,\theta^2=w$，则$\theta_1=-w,\theta_2=u$，所以$t=-2uw$。对点坐标取$\bar\theta^{\dot1}=\bar u,\bar\theta^{\dot2}=\bar w$，但缩并按先下后上，故$\bar t=2\bar u\bar w$。逐个非零分量给
<span id="eq:c95-quadratic-theta"></span>

$$
\begin{aligned}
\theta_a\theta_b&=\tfrac12t\epsilon_{ab},&
\theta^a\theta^b&=-\tfrac12t\epsilon^{ab},\\
\bar\theta_{\dot a}\bar\theta_{\dot b}
 &=-\tfrac12\bar t\epsilon_{\dot a\dot b},&
\bar\theta^{\dot a}\bar\theta^{\dot b}
 &=\tfrac12\bar t\epsilon^{\dot a\dot b}.
\end{aligned}
\tag{95.18}
$$

例如第一式在$a=1,b=2$时是$(-w)u=uw=(-2uw)(-1)/2$；其余非零分量由反交换得到。对$B^\mu B^\nu$，先把中间的点坐标移过第二个无点坐标，再用式[（35.5）](/posts/srednicki-35/#eq:c35-two-epsilon-sigma)，得到
<span id="eq:c95-theta-vector-product"></span>

$$
\begin{aligned}
B^\mu B^\nu
 &=-\theta^a\theta^b\bar\theta^{\dot a}\bar\theta^{\dot b}
                 \sigma^\mu_{a\dot a}\sigma^\nu_{b\dot b}\\
 &=\frac14t\bar t\epsilon^{ab}\epsilon^{\dot a\dot b}
                 \sigma^\mu_{a\dot a}\sigma^\nu_{b\dot b}
 =-\frac12t\bar t g^{\mu\nu}.
\end{aligned}
\tag{95.19}
$$

这条Fierz缩并中的初始负号来自奇变量换序。

现在逐项展开式[（95.17）](#eq:c95-chiral-multiplet)。标量项的Taylor级数在二阶终止：
<span id="eq:c95-scalar-taylor"></span>

$$
\begin{aligned}
A(y)&=A(x)-iB^\mu\partial_\mu A
 -\frac12B^\mu B^\nu\partial_\mu\partial_\nu A\\
 &=A-iB^\mu\partial_\mu A+\frac14t\bar t\partial^2A.
\end{aligned}
\tag{95.20}
$$

费米项只须保留一次位移。利用第一组theta的缩并及barsigma的升降定义，
<span id="eq:c95-fermion-taylor"></span>

$$
\begin{aligned}
\theta^aB^\mu\partial_\mu\psi_a
 &=-\tfrac12t\epsilon^{ac}\sigma^\mu_{c\dot b}
                         \bar\theta^{\dot b}\partial_\mu\psi_a
 =\tfrac12t\bar\theta\bar\sigma^\mu\partial_\mu\psi,\\
\sqrt2\theta\psi(y)
 &=\sqrt2\theta\psi(x)-\frac{i}{\sqrt2}t\bar\theta\bar\sigma^\mu\partial_\mu\psi.
\end{aligned}
\tag{95.21}
$$

第二次位移会含三个无点theta而为零；$tF(y)$的第一次位移也如此。因此完整展开是
<span id="eq:c95-chiral-x-expansion"></span>

$$
\begin{aligned}
\Phi(x,\theta,\bar\theta)
={}&A+\sqrt2\theta\psi+tF-iB^\mu\partial_\mu A\\
 &-\frac{i}{\sqrt2}t\bar\theta\bar\sigma^\mu\partial_\mu\psi
     +\frac14t\bar t\partial^2A.
\end{aligned}
\tag{95.22}
$$

求动能时将用到这六项的交叉乘积。

<span id="c95-components"></span>

## 分量变换与超势

在$y,\theta$坐标中，$\mathcal Q_a y^\mu=0$，而
$\overline{\mathcal Q}_{\dot a}y^\mu=-2i\theta^c\sigma^\mu_{c\dot a}$。因此作用于手征场的两个算符简化为
<span id="eq:c95-q-chiral-coordinates"></span>

$$
\mathcal Q_a=\partial_a,\qquad
\overline{\mathcal Q}_{\dot a}=-2i\theta^c\sigma^\mu_{c\dot a}\partial_\mu,
\qquad\partial_a t=2\theta_a.
\tag{95.23}
$$

这里$\partial_\mu$对$y$求导。把它们作用在三项展开上，得到
<span id="eq:c95-q-on-chiral-field"></span>

$$
\begin{aligned}
\mathcal Q_a\Phi&=\sqrt2\psi_a+2\theta_aF,\\
\overline{\mathcal Q}_{\dot a}\Phi
 &=-2i\theta^c\sigma^\mu_{c\dot a}\partial_\mu A
       +i\sqrt2t\partial_\mu\psi^c\sigma^\mu_{c\dot a}.
\end{aligned}
\tag{95.24}
$$

第二行的二次项用$\theta^c\theta^b=-t\epsilon^{cb}/2$化简，三次项为零。再匹配式[（95.6）](#eq:c95-superfield-action)两边相同的theta次数。因为$Q$与theta反对易，$[\theta\psi,Q]=\theta\{\psi,Q\}$；于是
<span id="eq:c95-chiral-component-transformations"></span>

$$
\begin{aligned}
\relax[A,Q_a]&=-i\sqrt2\psi_a,&[A,Q^\dagger_{\dot a}]&=0,\\
\{\psi_c,Q_a\}&=-i\sqrt2\epsilon_{ac}F,&
\{\psi_c,Q^\dagger_{\dot a}\}&=-\sqrt2\sigma^\mu_{c\dot a}\partial_\mu A,\\
[F,Q_a]&=0,&[F,Q^\dagger_{\dot a}]&=\sqrt2\partial_\mu\psi^c\sigma^\mu_{c\dot a}.
\end{aligned}
\tag{95.25}
$$

虽然从$y$坐标得到这些式子，$y$是任意自变量，分量关系因而也可统一改记为$x$处的场关系。

这些变换不借助运动方程就闭合，称为离壳闭合（off-shell closure）。以混合反对易子为例，直接把式[（95.25）](#eq:c95-chiral-component-transformations)代入，
<span id="eq:c95-offshell-closure"></span>

$$
\begin{aligned}
\{R_a,\bar R_{\dot b}\}A
 &=2i\sigma^\mu_{a\dot b}\partial_\mu A,\\
\{R_a,\bar R_{\dot b}\}\psi_c
 &=2i\left(\sigma^\mu_{c\dot b}\partial_\mu\psi_a
       -\epsilon_{ac}\sigma^\mu_{d\dot b}\partial_\mu\psi^d\right)
 =2i\sigma^\mu_{a\dot b}\partial_\mu\psi_c,\\
\{R_a,\bar R_{\dot b}\}F
 &=-2i\epsilon^{cd}\epsilon_{ad}\sigma^\mu_{c\dot b}\partial_\mu F
 =2i\sigma^\mu_{a\dot b}\partial_\mu F.
\end{aligned}
\tag{95.26}
$$

第二行用二维恒等式$X_c\psi_a-\epsilon_{ac}X_d\psi^d=X_a\psi_c$；若$a=c$两边相同，若$a\ne c$，只需把$\psi^1=\psi_2,\psi^2=-\psi_1$代入。第三行用$\epsilon^{cd}\epsilon_{ad}=-\delta_a{}^c$。同类两个超荷的作用也按反对称epsilon抵消，与微分算符式[（95.9）](#eq:c95-q-algebra)一致。复$A,F$共有四个实离壳分量，一个Weyl场也有四个实分量；辅助$F$让这套变换在求解动力学以前就封闭。

式[（95.25）](#eq:c95-chiral-component-transformations)的最后一式给出构造作用量的入口：最高分量的变化是全导数。对常量超变换参数，若场在边界的行为使表面项消失，那么$\int d^4x\,F$不变。为得到相互作用，考虑两个手征超场的乘积；它仍只依赖$y,\theta$，最高分量中的费米交叉项为
<span id="eq:c95-product-multiplet"></span>

$$
\begin{aligned}
2(\theta\psi_1)(\theta\psi_2)
 &=-2\theta^a\theta^b\psi_{1a}\psi_{2b}
 =t\epsilon^{ab}\psi_{1a}\psi_{2b}
 =-t\psi_1\psi_2,\\
\Phi_1\Phi_2
 &=A_1A_2+\sqrt2\theta(A_1\psi_2+A_2\psi_1)
       +t(A_1F_2+A_2F_1-\psi_1\psi_2).
\end{aligned}
\tag{95.27}
$$

第一个负号来自把$\psi_1$移过第二个theta，最后一个来自将epsilon按无点先上后下的缩并次序排列。

更一般地，取局部全纯函数$W(\Phi_i)$，即只依赖手征场而不依赖其共轭。展开到二次便足以找出F项：一次Taylor项贡献$W_iF_i$，二次项的两个费米分量贡献$-W_{ij}\psi_i\psi_j/2$，所以
<span id="eq:c95-superpotential-f-term"></span>

$$
\begin{aligned}
W_i&=\frac{\partial W(A)}{\partial A_i},\qquad
W_{ij}=\frac{\partial^2W(A)}{\partial A_i\partial A_j},\\
[W(\Phi)]_F&=W_iF_i-\frac12W_{ij}\psi_i\psi_j.
\end{aligned}
\tag{95.28}
$$

物种指标$i,j$求和。奇旋量缩并$\psi_i\psi_j$对$i,j$对称，故它与对称Hessian相配；这里的$1/2$来自Taylor级数的$2!$。$W$称为超势（superpotential），其F项与共轭相加就给实的超对称相互作用。

由$\{Q,Q^\dagger\}\sim P$知$[Q]=1/2$，式[（95.7）](#eq:c95-q-differential)给$[\theta]=-1/2$。取标准标量维数$[A]=1$，于是$[\Phi]=1,[\psi]=3/2,[F]=2$，F项提取会增加1单位质量维数。四维拉格朗日量维数4便要求$[W]=3$。在多项式、可重整的模型中，超势因而至多三次；更高次项可在指定截止的有效理论中使用。

<span id="c95-d-terms"></span>

## 动能怎样从超场中产生

超势给出了相互作用，但我们还没有标量和旋量的动能。手征场与它的共轭相乘，恰好能补上这一部分。这个乘积不再手征，却是实的；因此先考察一般实超场。按四个奇坐标的全部单项式展开，再要求$V^\dagger=V$，可写为
<span id="eq:c95-real-superfield"></span>

$$
\begin{aligned}
V={}&C+\theta\chi+\bar\theta\chi^\dagger+tM+\bar tM^*+B^\mu v_\mu\\
 &+t\bar\theta\lambda^\dagger+\bar t\theta\lambda+\frac12t\bar tD.
\end{aligned}
\tag{95.29}
$$

$C,D,v_\mu$为实场，$M$为复场，$\chi,\lambda$为Weyl场。这样有八个实玻色分量和八个实费米分量。它也称为矢量超场（vector superfield），因为展开中包含一个时空矢量$v_\mu$；整个$V$仍是洛伦兹标量。式中以最高项的$1/2$定义辅助分量$D$的归一。

用$[U]_{22}$表示任意超场中$t\bar t$的系数，称它为D项。对上式，$[V]_{22}=D/2$。考察它的超变换时，$\partial_a$会降低theta次数，不能产生最高项；$i\sigma^\mu_{a\dot c}\bar\theta^{\dot c}\partial_\mu$则只能从三次项$t\bar\theta\lambda^\dagger$产生最高项。由$\bar\theta^{\dot c}\bar\theta_{\dot d}=-\bar t\delta^{\dot c}{}_{\dot d}/2$，有
<span id="eq:c95-d-term-transformation"></span>

$$
\begin{aligned}
\relax[\mathcal Q_aV]_{22}
 &=-\frac i2\sigma^\mu_{a\dot c}\partial_\mu\lambda^{\dagger\dot c},\\
\frac12[D,Q_a]&=[-i\mathcal Q_aV]_{22}
 =-\frac12\sigma^\mu_{a\dot c}\partial_\mu\lambda^{\dagger\dot c},\\
[D,Q_a]&=-\sigma^\mu_{a\dot c}\partial_\mu\lambda^{\dagger\dot c},\qquad
[D,Q^\dagger_{\dot a}]=\partial_\mu\lambda^c\sigma^\mu_{c\dot a}.
\end{aligned}
\tag{95.30}
$$

最后一个关系可由前一个反序取伴随得到。最高分量的变化仍然是全导数，所以它的时空积分也可用来构造超对称作用量。从$[V]_{22}$转换到$D$时，变换关系也相应乘2。

现在把式[（95.22）](#eq:c95-chiral-x-expansion)取伴随。按照第35节的反序共轭规则，所得右手手征场为
<span id="eq:c95-antichiral-expansion"></span>

$$
\begin{aligned}
\Phi^\dagger={}&A^*+\sqrt2\bar\theta\psi^\dagger+\bar tF^*
       +iB^\mu\partial_\mu A^*\\
 &+\frac i{\sqrt2}\bar t\partial_\mu\psi^\dagger\bar\sigma^\mu\theta
       +\frac14t\bar t\partial^2A^*.
\end{aligned}
\tag{95.31}
$$

把上式和$\Phi$相乘，先收集不含费米子的部分。两个二阶Taylor项分别给$A\partial^2A^*/4$和$A^*\partial^2A/4$；两个一次位移的乘积则为
$(iB^\mu\partial_\mu A^*)(-iB^\nu\partial_\nu A)
=-t\bar t\partial^\mu A^*\partial_\mu A/2$。辅助分量直接给$t\bar tF^*F$。

费米动能来自一次项与三次项的两个交叉乘积。把theta移到左边，再用式[（95.18）](#eq:c95-quadratic-theta)缩并，具体得到
<span id="eq:c95-kinetic-cross-products"></span>

$$
\begin{aligned}
\left[(\sqrt2\bar\theta\psi^\dagger)
 \left(-\frac i{\sqrt2}t\bar\theta\bar\sigma^\mu\partial_\mu\psi\right)\right]_{22}
 &=\frac i2\psi^\dagger\bar\sigma^\mu\partial_\mu\psi,\\
\left[\left(\frac i{\sqrt2}\bar t\partial_\mu\psi^\dagger
       \bar\sigma^\mu\theta\right)(\sqrt2\theta\psi)\right]_{22}
 &=-\frac i2\partial_\mu\psi^\dagger\bar\sigma^\mu\psi.
\end{aligned}
\tag{95.32}
$$

例如第一行的点旋量乘积满足
$(\bar\theta\psi^\dagger)(\bar\theta\eta)=-\bar t\psi^\dagger\eta/2$，其中$\eta=\bar\sigma^\mu\partial_\mu\psi$；换序产生的这个负号与原来的$-i$相乘。第二行用无点theta的相应恒等式，给出相反的一阶导数次序。两项一起保证密度为实。至此全部最高项为
<span id="eq:c95-kinetic-d-coefficient"></span>

$$
\begin{aligned}
\relax[\Phi^\dagger\Phi]_{22}={}&-\frac12\partial^\mu A^*\partial_\mu A
 +\frac14 A\partial^2A^*+\frac14 A^*\partial^2A\\
 &+\frac i2\psi^\dagger\bar\sigma^\mu\partial_\mu\psi
 -\frac i2\partial_\mu\psi^\dagger\bar\sigma^\mu\psi+F^*F.
\end{aligned}
\tag{95.33}
$$

对两个标量二阶导数各分部积分一次，它们各再给$-\partial A^*\partial A/4$；对第二个费米项分部积分，则把它变成与第一个相同的形式。因此
<span id="eq:c95-kinetic-boundary-term"></span>

$$
\begin{aligned}
\relax[\Phi^\dagger\Phi]_{22}
 &=-\partial^\mu A^*\partial_\mu A
       +i\psi^\dagger\bar\sigma^\mu\partial_\mu\psi+F^*F
       +\partial_\mu K^\mu,\\
K^\mu&=\frac14(A\partial^\mu A^*+A^*\partial^\mu A)
             -\frac i2\psi^\dagger\bar\sigma^\mu\psi.
\end{aligned}
\tag{95.34}
$$

在作用量中舍去这个表面项，便得到复标量和Weyl旋量的标准动能。$F$没有导数，因而没有自己的传播模；它是辅助场（auxiliary field）。两个密度相差已写出的全导数，在上述边界条件下给出相同作用量。

<span id="c95-auxiliary-fields"></span>

## 辅助场与Wess–Zumino模型

对一组手征场，现在可以把动能和超势合在一起：
<span id="eq:c95-auxiliary-square"></span>

$$
\begin{aligned}
\mathcal L&=[\Phi_i^\dagger\Phi_i]_{22}+[W(\Phi)]_F+[W(\Phi)]_F^*,\\
\mathcal L_F&=F_i^*F_i+W_iF_i+W_i^*F_i^*
       =|F_i+W_i^*|^2-|W_i|^2.
\end{aligned}
\tag{95.35}
$$

这里及以下的物种指标求和。把$F_i,F_i^*$作为独立变量变分，分别得到$F_i^*+W_i=0$及其共轭，即
<span id="eq:c95-f-elimination"></span>

$$
F_i=-W_i^*,\qquad
V_F(A,A^*)=\sum_i|W_i|^2.
\tag{95.36}
$$

在路径积分中也是同一结果：逐点作平移$F_i'=F_i+W_i^*$，平移的Jacobian为1，剩下的积分只含$F_i^{\prime *}F_i'$。在统一的收敛处方下，这个与物质场无关的高斯因子并入归一常数。因此，采用本节的正则二次辅助项时，积分消去$F_i$等价于代入它的代数方程。

消元后的全部拉格朗日量为
<span id="eq:c95-chiral-component-action"></span>

$$
\begin{aligned}
\mathcal L={}&-\partial^\mu A_i^*\partial_\mu A_i
 +i\psi_i^\dagger\bar\sigma^\mu\partial_\mu\psi_i
 -\sum_i|W_i|^2\\
 &-\frac12\left(W_{ij}\psi_i\psi_j+W_{ij}^*\psi_i^\dagger\psi_j^\dagger\right).
\end{aligned}
\tag{95.37}
$$

势能是平方和，费米质量和Yukawa耦合则由同一个超势的二阶导数决定。辅助场使超对称变换原先能离壳闭合；消去它以后，若要在剩余分量上核对同样的闭合关系，就还需使用费米场方程。这不会改变消元前已建立的作用量对称性。

最简单的相互作用例是Wess–Zumino模型：只有一个手征场，取
<span id="eq:c95-wz-superpotential"></span>

$$
W(A)=\frac m2A^2+\frac g6A^3,\qquad
W_A=mA+\frac g2A^2,\qquad W_{AA}=m+gA.
\tag{95.38}
$$

这里$[m]=1,[g]=0$。暂允许$m,g$为复数，代入上面的通式便得
<span id="eq:c95-wz-component-couplings"></span>

$$
\begin{aligned}
V={}&|m|^2|A|^2+\frac12m^*gA^*A^2
       +\frac12mg^*A^{*2}A+\frac{|g|^2}{4}|A|^4,\\
\mathcal L_{\rm mass+Yuk}
 &=-\frac12(m+gA)\psi\psi+\mathrm{h.c.}
\end{aligned}
\tag{95.39}
$$

实$m,g$是这组公式的一个特例。看$A=0$附近的二次项，令$A=(a+ib)/\sqrt2$，其动能是$-[(\partial a)^2+(\partial b)^2]/2$，势为$|m|^2(a^2+b^2)/2$。两个实标量的质量都是$|m|$；Weyl质量项也给相同质量，复$m$的相位可由旋量相位变换吸收。

若$g\ne0$，还有一个零势真空$A=-2m/g$。在那里$W_{AA}=-m$，同样的展开仍给质量$|m|$。当$m=0$时两零点合并，二次质量为零；当$g=0$时回到自由质量多重态。这个例子说明超对称怎样限制相互作用：一旦指定超势，标量三次、四次耦合以及Yukawa耦合就一起确定，不能再各自任意选择。

<span id="c95-supergauge"></span>

## 超规范变换与Wess–Zumino规范

实超场中已有$v_\mu$，我们可以尝试把它用作阿贝尔规范场。为此，需要一种保持$V$为实超场、又能包含$v_\mu\mapsto v_\mu-\partial_\mu b$的变换。若$\Xi$是任意左手手征超场，那么$i(\Xi^\dagger-\Xi)$是实的，因此取
<span id="eq:c95-abelian-supergauge"></span>

$$
V'=V+i(\Xi^\dagger-\Xi).
\tag{95.40}
$$

这称为超规范变换（supergauge transformation）。这里把参数场的一次项归一成$\theta\xi$，没有物质场中的$\sqrt2$。直接在式[（95.22）](#eq:c95-chiral-x-expansion)中置$\psi=\xi/\sqrt2$，得到
<span id="eq:c95-gauge-parameter-expansion"></span>

$$
\begin{aligned}
\Xi={}&B+\theta\xi+tG-iB^\mu\partial_\mu B
       -\frac i2t\bar\theta\bar\sigma^\mu\partial_\mu\xi
       +\frac14t\bar t\partial^2B,\\
\Xi^\dagger={}&B^*+\bar\theta\xi^\dagger+\bar tG^*
       +iB^\mu\partial_\mu B^*
       +\frac i2\bar t\partial_\mu\xi^\dagger\bar\sigma^\mu\theta
       +\frac14t\bar t\partial^2B^*.
\end{aligned}
\tag{95.41}
$$

没有时空指标的$B$在这里是规范参数场的复标量分量；$B^\mu=\theta\sigma^\mu\bar\theta$仍表示前面定义的坐标双线性。令$B=(b+ia)/2$，其中$a,b$实。相减后最低项为$a$，矢量项为$-B^\mu\partial_\mu b$，完整增量为
<span id="eq:c95-gauge-parameter-increment"></span>

$$
\begin{aligned}
i(\Xi^\dagger-\Xi)={}&a-i\theta\xi+i\bar\theta\xi^\dagger
       -itG+i\bar tG^*-B^\mu\partial_\mu b\\
 &-\frac12t\bar\theta\bar\sigma^\mu\partial_\mu\xi
       -\frac12\bar t\partial_\mu\xi^\dagger\bar\sigma^\mu\theta
       +\frac14t\bar t\partial^2a.
\end{aligned}
\tag{95.42}
$$

与一般$V$展开逐项比较，便有
<span id="eq:c95-low-component-gauge-transform"></span>

$$
C'=C+a,\qquad \chi'=\chi-i\xi,\qquad
M'=M-iG,\qquad v'_\mu=v_\mu-\partial_\mu b.
\tag{95.43}
$$

选$a=-C,\xi=-i\chi,G=-iM$，即可消去$C,\chi,M$。把变换后的其余场仍记为原符号，就得到Wess–Zumino规范：
<span id="eq:c95-wz-gauge"></span>

$$
V=B^\mu v_\mu+t\bar\theta\lambda^\dagger+\bar t\theta\lambda
          +\frac12t\bar tD.
\tag{95.44}
$$

此时$b(x)$还未选定。只取$B=b/2,\xi=G=0$的超规范变换保持这个形式，并实现通常的阿贝尔规范变换。这样，$C,\chi,M$对应的自由度已被规范选择除去，而普通规范自由度仍保留。

Wess–Zumino规范使分量计算大为简化，但一次未经补偿的超变换通常会离开它。例如$\partial_a(B^\mu v_\mu)=\sigma^\mu_{a\dot b}\bar\theta^{\dot b}v_\mu$重新产生一次奇坐标项。可再用式[（95.43）](#eq:c95-low-component-gauge-transform)选择依赖于场的$\xi,G,a$，恢复$C=\chi=M=0$。因此，规范固定后的超变换包含这一步补偿；两次变换的闭合也允许相差一个剩余普通规范变换。前面未固定规范的超场作用量，已经给出了计算这些补偿的统一起点。

<span id="c95-charged-matter"></span>

## 带电手征场

令$\Phi$带电荷$+1$，把普通局域相位变换推广为
<span id="eq:c95-charged-superfield-action"></span>

$$
\Phi'=e^{-2ig\Xi}\Phi,\qquad
\Phi^{\dagger\prime}=\Phi^\dagger e^{2ig\Xi^\dagger},\qquad
\mathcal L_{\rm matter}=[\Phi^\dagger e^{-2gV}\Phi]_{22}.
\tag{95.45}
$$

这里$g$是规范耦合。指数中的$\Xi$是手征的，所以变换后的$\Phi$仍手征。在阿贝尔情形，各偶指数互相可交换，$V'=V+i(\Xi^\dagger-\Xi)$给
<span id="eq:c95-abelian-invariance"></span>

$$
e^{2ig\Xi^\dagger}e^{-2gV'}e^{-2ig\Xi}
=e^{2ig\Xi^\dagger}e^{-2gV}
       e^{-2ig\Xi^\dagger+2ig\Xi}e^{-2ig\Xi}
=e^{-2gV}.
\tag{95.46}
$$

所以括号中的实超场规范不变，其D项积分同时保持超对称。对于剩余变换$B=b/2$，最低分量满足$A'=e^{-igb}A$。结合$v'_\mu=v_\mu-\partial_\mu b$，直接求导得
<span id="eq:c95-component-covariant-derivative"></span>

$$
\begin{aligned}
D_\mu A&=(\partial_\mu-igv_\mu)A,\\
(\partial_\mu-igv'_\mu)(e^{-igb}A)
 &=e^{-igb}(\partial_\mu-igv_\mu)A.
\end{aligned}
\tag{95.47}
$$

这解释了超场指数中$2g$与通常协变导数中$g$之间的关系。

来计算式[（95.45）](#eq:c95-charged-superfield-action)的分量。Wess–Zumino规范中$V$最低为二次奇坐标，故$V^3=0$；$V^2$仅有两个矢量项的乘积。使用式[（95.19）](#eq:c95-theta-vector-product)，指数完全截断为
<span id="eq:c95-wz-exponential"></span>

$$
\begin{aligned}
V^2&=-\frac12t\bar t v^\mu v_\mu,\qquad V^3=0,\\
e^{-2gV}&=1-2gV+2g^2V^2\\
 &=1-2gB^\mu v_\mu-2gt\bar\theta\lambda^\dagger
       -2g\bar t\theta\lambda-t\bar t(gD+g^2v^2).
\end{aligned}
\tag{95.48}
$$

这是格拉斯曼幂零性给出的精确式，未作小$g$近似。

指数中除了常数只含二次及以上项，所以只需$\Phi^\dagger\Phi$的零次、一次、矢量二次项和已求得的最高项。其中两个一次费米项的乘积可用第35节sigma完备关系重排成
$2(\bar\theta\psi^\dagger)(\theta\psi)
=B^\mu\psi^\dagger\bar\sigma_\mu\psi$。具体说，把中间的$\psi^\dagger$移过$\theta$先得负号，再以$\sigma^\mu_{a\dot a}\bar\sigma_\mu^{\dot b b}=-2\delta_a{}^b\delta_{\dot a}{}^{\dot b}$配对两个旋量槽，恰好恢复前面的2。因此有关系数是
<span id="eq:c95-matter-current-coefficient"></span>

$$
\begin{aligned}
\Phi^\dagger\Phi={}&|A|^2+\sqrt2\bar\theta\psi^\dagger A
       +\sqrt2\theta\psi A^*+B^\mu J_\mu
       +\cdots+t\bar t[\Phi^\dagger\Phi]_{22},\\
J_\mu={}&\psi^\dagger\bar\sigma_\mu\psi
       -iA^*\partial_\mu A+iA\partial_\mu A^*.
\end{aligned}
\tag{95.49}
$$

省略项的theta次数不与式[（95.48）](#eq:c95-wz-exponential)中的任何项相补为$t\bar t$，所以不会进入当前计算。两个矢量系数相乘给
$(-2gB\cdot v)(B\cdot J)=gt\bar t v\cdot J$。两个三次规范微子项则分别与一次物质项相乘；例如
$(-2g\bar t\theta\lambda)(\sqrt2\theta\psi A^*)
=\sqrt2gt\bar t A^*\lambda\psi$，用到了式[（95.27）](#eq:c95-product-multiplet)中的奇旋量乘积。于是相对于自由动能新增
<span id="eq:c95-matter-interaction-expansion"></span>

$$
\begin{aligned}
\Delta\mathcal L={}&-igv^\mu(A^*\partial_\mu A-A\partial_\mu A^*)
       -g^2v^2|A|^2+gv_\mu\psi^\dagger\bar\sigma^\mu\psi\\
 &+\sqrt2g(A^*\lambda\psi+\psi^\dagger\lambda^\dagger A)-g|A|^2D.
\end{aligned}
\tag{95.50}
$$

标量前两项与$-\partial A^*\partial A$合成$-(D^\mu A)^*D_\mu A$；费米电流项与$i\psi^\dagger\bar\sigma\partial\psi$合成协变动能。舍去式[（95.34）](#eq:c95-kinetic-boundary-term)的表面项后，得到
<span id="eq:c95-charged-component-action"></span>

$$
\begin{aligned}
\mathcal L_{\rm matter}={}&-(D^\mu A)^*D_\mu A
       +i\psi^\dagger\bar\sigma^\mu D_\mu\psi+F^*F\\
 &+\sqrt2g(A^*\lambda\psi+\psi^\dagger\lambda^\dagger A)-gA^*DA.
\end{aligned}
\tag{95.51}
$$

规范耦合同时确定了协变导数、标量与规范微子的Yukawa项以及辅助$D$耦合。单个带电手征场可作为这样的经典构件；若组成量子规范理论，费米子内容还须满足第75–77章的反常消去条件。后面将用电荷$+1,-1$两个手征场构成SQED，其立方电荷和及一次电荷和都为零。

<span id="c95-field-strength"></span>

## 场强超场

现在还缺规范场和规范微子的动能。普通规范理论通过$F_{\mu\nu}$消去$v_\mu$的非物理梯度；这里也要从$V$构造一个超规范不变量。先用$\mathcal D_a$去掉反手征规范参数，再用两个$\overline{\mathcal D}$投影到手征场，正好能做到这一点。

在固定归一之前，先算清投影算符本身。我们的左导数按第35节的epsilon升指标，所以
$\bar\partial^{\dot1}=\bar\partial_{\dot2}$、$\bar\partial^{\dot2}=-\bar\partial_{\dot1}$。写$\bar t=2\bar u\bar w$，右边的导数先作用，得到
<span id="eq:c95-antitheta-projection"></span>

$$
\begin{aligned}
\bar\partial_{\dot b}\bar\partial^{\dot b}
 &=2\partial_{\bar u}\partial_{\bar w},\\
\bar\partial_{\dot b}\bar\partial^{\dot b}\bar t
 &=2\partial_{\bar u}\partial_{\bar w}(2\bar u\bar w)
 =2\partial_{\bar u}(-2\bar u)=-4.
\end{aligned}
\tag{95.52}
$$

投影作用值为$-4$。为使场强超场的最低分量是$+\lambda_a$，将投影系数取为$-1/4$，定义
<span id="eq:c95-field-strength-definition"></span>

$$
\widehat W_a=-\frac14\overline{\mathcal D}_{\dot b}
      \overline{\mathcal D}^{\dot b}\mathcal D_aV.
\tag{95.53}
$$

这个归一给$\widehat W_a|_{\theta=0}=\lambda_a$；稍后构造规范作用量时使用其平方$\widehat W^a\widehat W_a$。

由于$\overline{\mathcal D}$只有两个反对易分量，任意三个的乘积都为零，所以$\overline{\mathcal D}_{\dot c}\widehat W_a=0$。它是手征的。对超规范增量，最右的$\mathcal D_a$直接湮灭$\Xi^\dagger$；对于$\Xi$，将一个点导数移到最右，得到
<span id="eq:c95-projection-gauge-identity"></span>

$$
\overline{\mathcal D}_{\dot b}\overline{\mathcal D}^{\dot b}\mathcal D_a
 =-\left(\overline{\mathcal D}_{\dot b}\mathcal D_a
              +2i\sigma^\mu_{a\dot b}\partial_\mu\right)
                \overline{\mathcal D}^{\dot b}.
\tag{95.54}
$$

这里先用$\{\overline{\mathcal D}^{\dot b},\mathcal D_a\}
=2i\epsilon^{\dot b\dot c}\sigma^\mu_{a\dot c}\partial_\mu$，再用
$\epsilon^{\dot b\dot c}\overline{\mathcal D}_{\dot b}
=-\overline{\mathcal D}^{\dot c}$重排接触项。最右的导数湮灭手征$\Xi$，故$\widehat W_a$超规范不变。

求分量时用手征坐标最方便。把$x=y+iB$代入式[（95.44）](#eq:c95-wz-gauge)，只有矢量最低项的一次位移还能留下：
$iB^\mu B^\nu\partial_\mu v_\nu=-it\bar t\partial\cdot v/2$。其余位移都含三个同类theta。因此
<span id="eq:c95-vector-in-chiral-coordinates"></span>

$$
\begin{aligned}
V(y,\theta,\bar\theta)
 &=B^\mu v_\mu+t\bar\theta\lambda^\dagger+\bar t\theta\lambda
       +\frac12t\bar t(D-i\partial\cdot v),\\
\left.\mathcal D_a\right|_{y,\theta,\bar\theta}
 &=\partial_a-2i\sigma^\mu_{a\dot b}\bar\theta^{\dot b}\partial_\mu,
 \qquad \overline{\mathcal D}_{\dot a}=-\bar\partial_{\dot a}.
\end{aligned}
\tag{95.55}
$$

所有分量的自变量现在都是$y$。第二行由$\mathcal D_ay^\mu=-2i\sigma^\mu_{a\dot b}\bar\theta^{\dot b}$和链式法则得到。投影只保留$\bar t$的系数，因此无需计算$\mathcal D_aV$的所有项。四个非零贡献分别是
<span id="eq:c95-four-projection-contributions"></span>

$$
\begin{aligned}
\relax[\partial_a(\bar t\theta\lambda)]_{\bar t}&=\lambda_a,\\
\left[\partial_a\left(\frac12t\bar t(D-i\partial\cdot v)\right)\right]_{\bar t}
 &=\theta_a(D-i\partial\cdot v),\\
[-2i\sigma^\mu_{a\dot b}\bar\theta^{\dot b}\partial_\mu(B^\nu v_\nu)]_{\bar t}
 &=-i(\sigma^\mu\bar\sigma^\nu\theta)_a\partial_\mu v_\nu,\\
[-2i\sigma^\mu_{a\dot b}\bar\theta^{\dot b}\partial_\mu
             (t\bar\theta\lambda^\dagger)]_{\bar t}
 &=it\sigma^\mu_{a\dot b}\partial_\mu\lambda^{\dagger\dot b}.
\end{aligned}
\tag{95.56}
$$

第三行先把外面的$\bar\theta$移过$B^\nu$中的$\theta$，再以$\bar\theta^{\dot a}\bar\theta^{\dot b}=\bar t\epsilon^{\dot a\dot b}/2$缩并；barsigma正是这个epsilon升降后的sigma。第四行则用$\bar\theta^{\dot b}\bar\theta_{\dot c}=-\bar t\delta^{\dot b}{}_{\dot c}/2$。式[（95.53）](#eq:c95-field-strength-definition)的$-1/4$与投影的$-4$相乘，因而这四项之和就是$\widehat W_a$。

第35节已得到
$(\sigma^\mu\bar\sigma^\nu)_a{}^b
=-g^{\mu\nu}\delta_a{}^b-2i(S_L^{\mu\nu})_a{}^b$。
把这个两边自由指标同为$a,b$的恒等式代入第三项，度规部分给$+i\theta_a\partial\cdot v$，与第二项的负散度相消；反对称的$S_L^{\mu\nu}$则只选出$\partial_\mu v_\nu-\partial_\nu v_\mu$。于是
<span id="eq:c95-field-strength-components"></span>

$$
\begin{aligned}
F_{\mu\nu}&=\partial_\mu v_\nu-\partial_\nu v_\mu,\\
\widehat W_a&=\lambda_a+\theta_aD
 -(S_L^{\mu\nu})_a{}^c\theta_cF_{\mu\nu}
 +it\sigma^\mu_{a\dot b}\partial_\mu\lambda^{\dagger\dot b}.
\end{aligned}
\tag{95.57}
$$

矢量场只通过场强出现，符合刚才证明的规范不变性。$\widehat W_a$为奇手征超场，其底分量维数为$3/2$；$\theta D$、$\theta F_{\mu\nu}$及$t\partial\lambda^\dagger$也都有这个维数。

<span id="c95-gauge-kinetic"></span>

## 从旋量迹得到规范动能

两个奇场强超场可以缩并成偶的洛伦兹标量$\widehat W^a\widehat W_a$。它是手征场，故F项的时空积分保持超对称。令
<span id="eq:c95-spinor-strength-matrix"></span>

$$
M_a{}^b=D\delta_a{}^b-(S_L^{\mu\nu})_a{}^bF_{\mu\nu},\qquad
K_a=i\sigma^\mu_{a\dot b}\partial_\mu\lambda^{\dagger\dot b},
\qquad \widehat W_a=\lambda_a+M_a{}^b\theta_b+tK_a.
\tag{95.58}
$$

底项与最高项交叉给$2\lambda^aK_a$，因为两个奇旋量的无点标量缩并是对称的。两个一次项给$t\det M$：写成分量，$W^aW_a=-2W_1W_2$，而
$(M_1{}^1\theta_1+M_1{}^2\theta_2)
(M_2{}^1\theta_1+M_2{}^2\theta_2)
=(\det M)\theta_1\theta_2=-(\det M)t/2$。
对$2\times2$矩阵，用$\det M=[(\operatorname{Tr}M)^2-\operatorname{Tr}M^2]/2$以及$\operatorname{Tr}S_L=0$，有
<span id="eq:c95-strength-square-trace"></span>

$$
\begin{aligned}
\relax[\widehat W^a\widehat W_a]_F
 &=2i\lambda^a\sigma^\mu_{a\dot b}\partial_\mu\lambda^{\dagger\dot b}
       +D^2-\frac12\operatorname{Tr}(S_L^{\mu\nu}S_L^{\rho\sigma})
                   F_{\mu\nu}F_{\rho\sigma}.
\end{aligned}
\tag{95.59}
$$

旋量迹前面的$1/2$由此确定。

若直接按旋量指标缩并，所用的对称性是式[（35.7）](/posts/srednicki-35/#eq:c35-lowered-symmetry)中的$(S_L^{\mu\nu})_{ac}=(S_L^{\mu\nu})_{ca}$，所得迹为$(S_L^{\mu\nu})_a{}^c(S_L^{\rho\sigma})_c{}^a$。上面的行列式计算将同一次epsilon缩并写成了普通二阶矩阵运算。

还需把这个迹算出。用已建立的
$S_L^{i0}=i\sigma_i/2$、$S_L^{ij}=\epsilon_{ijk}\sigma_k/2$，每一类都化为$\operatorname{tr}(\sigma_i\sigma_j)=2\delta_{ij}$：
<span id="eq:c95-three-trace-cases"></span>

$$
\begin{aligned}
\operatorname{Tr}(S_L^{i0}S_L^{j0})&=-\frac12\delta_{ij},\\
\operatorname{Tr}(S_L^{i0}S_L^{jk})&=\frac i2\epsilon_{jki},\\
\operatorname{Tr}(S_L^{ij}S_L^{kl})
 &=\frac12(\delta_{ik}\delta_{jl}-\delta_{il}\delta_{jk}).
\end{aligned}
\tag{95.60}
$$

这三类穷尽两个反对称洛伦兹指标对的独立组合。依$\epsilon^{0123}=+1$重新合写，得到
<span id="eq:c95-covariant-spinor-trace"></span>

$$
\operatorname{Tr}(S_L^{\mu\nu}S_L^{\rho\sigma})
 =\frac12(g^{\mu\rho}g^{\nu\sigma}-g^{\mu\sigma}g^{\nu\rho})
       -\frac i2\epsilon^{\mu\nu\rho\sigma}.
\tag{95.61}
$$

例如$(\mu\nu,\rho\sigma)=(10,23)$时，$\epsilon^{1023}=-1$，虚项为$+i/2$，与第二类一致。代回式[（95.59）](#eq:c95-strength-square-trace)，两个度规缩并分别给$F^2$和$-F^2$；epsilon缩并则满足$\epsilon^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}=2\widetilde F^{\mu\nu}F_{\mu\nu}$。所以
<span id="eq:c95-strength-square-evaluated"></span>

$$
\begin{aligned}
\relax[\widehat W^a\widehat W_a]_F
 &=2i\lambda\sigma^\mu\partial_\mu\lambda^\dagger
       -\frac12F^{\mu\nu}F_{\mu\nu}
       +\frac i2\widetilde F^{\mu\nu}F_{\mu\nu}+D^2,\\
\widetilde F^{\mu\nu}&=\frac12\epsilon^{\mu\nu\rho\sigma}F_{\rho\sigma}.
\end{aligned}
\tag{95.62}
$$

对偶项的正号由旋量迹和$\epsilon^{0123}=+1$共同固定；场强超场的整体重定号已在平方中消失。

取实系数$1/4$再加共轭，虚的对偶项相消。规范微子部分先用
$\lambda\sigma^\mu\partial_\mu\lambda^\dagger
=-(\partial_\mu\lambda^\dagger)\bar\sigma^\mu\lambda$换序，再分部积分，具体为
<span id="eq:c95-gaugino-kinetic-boundary"></span>

$$
\begin{aligned}
\frac14(2i\lambda\sigma^\mu\partial_\mu\lambda^\dagger+\mathrm{h.c.})
 &=\frac i2\lambda^\dagger\bar\sigma^\mu\partial_\mu\lambda
       -\frac i2(\partial_\mu\lambda^\dagger)\bar\sigma^\mu\lambda\\
 &=i\lambda^\dagger\bar\sigma^\mu\partial_\mu\lambda
       -\frac i2\partial_\mu(\lambda^\dagger\bar\sigma^\mu\lambda).
\end{aligned}
\tag{95.63}
$$

因此，舍去表面项后的规范拉格朗日量为
<span id="eq:c95-abelian-gauge-action"></span>

$$
\mathcal L_{\rm gauge}
 =\frac14[\widehat W^a\widehat W_a]_F+\mathrm{h.c.}
 \simeq i\lambda^\dagger\bar\sigma^\mu\partial_\mu\lambda
       -\frac14F^{\mu\nu}F_{\mu\nu}+\frac12D^2.
\tag{95.64}
$$

符号$\simeq$在此表示相差已写出的全导数。$v_\mu$与规范微子（gaugino）$\lambda$都具有标准动能，实场$D$则与先前的$F$一样为辅助场。质量为零时，规范矢量的两个物理极化与Weyl规范微子的两个物理自由度相配。

<span id="c95-nonabelian"></span>

## 非阿贝尔推广

非阿贝尔理论使用矩阵值超场$V=V^AT_R^A$和$\Xi=\Xi^AT_R^A$，其中$T_R^A$为厄米生成元，$A$在这一节是群指标。物质场仍按式[（95.45）](#eq:c95-charged-superfield-action)变换，但指数不能再任意交换次序。记
<span id="eq:c95-ordered-gauge-matrices"></span>

$$
H=e^{-2gV},\qquad U=e^{-2ig\Xi},\qquad K=e^{-2ig\Xi^\dagger}.
\tag{95.65}
$$

由于$\Phi'=U\Phi$、$\Phi^{\dagger\prime}=\Phi^\dagger K^{-1}$，要使$\Phi^\dagger H\Phi$不变，必须取
<span id="eq:c95-nonabelian-matter-invariance"></span>

$$
H'=KHU^{-1},\qquad
\Phi^{\dagger\prime}H'\Phi'
 =\Phi^\dagger K^{-1}(KHU^{-1})U\Phi
 =\Phi^\dagger H\Phi.
\tag{95.66}
$$

在这个有序变换中，各相邻逆矩阵依次消去，未交换任何两个矩阵。阿贝尔极限中把指数相加，它又约化为式[（95.40）](#eq:c95-abelian-supergauge)。

场强的定义也相应取为
<span id="eq:c95-nonabelian-strength-definition"></span>

$$
\widehat W_a=\frac1{8g}\overline{\mathcal D}_{\dot b}
              \overline{\mathcal D}^{\dot b}(H^{-1}\mathcal D_aH).
\tag{95.67}
$$

这个号已与式[（95.53）](#eq:c95-field-strength-definition)统一：阿贝尔时$H^{-1}\mathcal D_aH=-2g\mathcal D_aV$，恰好回到$-1/4$投影。

来检验协变性。$K$是反手征的，故$\mathcal D_aK=0$；$H,K,U$都是偶矩阵，Leibniz规则没有额外奇号。因此
<span id="eq:c95-connection-supergauge-law"></span>

$$
\begin{aligned}
H'^{-1}\mathcal D_aH'
 &=UH^{-1}K^{-1}\mathcal D_a(KHU^{-1})\\
 &=U(H^{-1}\mathcal D_aH)U^{-1}+U\mathcal D_aU^{-1}.
\end{aligned}
\tag{95.68}
$$

$U,U^{-1}$是手征矩阵，所以两个$\overline{\mathcal D}$穿过它们时不产生导数项。第二项中的$\overline{\mathcal D}_{\dot b}\overline{\mathcal D}^{\dot b}\mathcal D_aU^{-1}$又由式[（95.54）](#eq:c95-projection-gauge-identity)为零。于是
<span id="eq:c95-strength-covariance"></span>

$$
\widehat W'_a=U\widehat W_aU^{-1}.
\tag{95.69}
$$

取群迹后，$\operatorname{Tr}(\widehat W^a\widehat W_a)$规范不变。它的F项因而可以同时提供非阿贝尔规范不变和超对称的作用量。

接着求分量展开。非阿贝尔场强的新项来自矩阵交换子，需要在展开时保留各矩阵的先后次序。在Wess–Zumino规范中$V^3=0$，展开微分指数乘积，
<span id="eq:c95-finite-connection-expansion"></span>

$$
\begin{aligned}
H^{-1}\mathcal D_aH
 &=(1+2gV+2g^2V^2)
       \{-2g\mathcal D_aV+2g^2[(\mathcal D_aV)V+V\mathcal D_aV]\}\\
 &=-2g\mathcal D_aV-2g^2[V,\mathcal D_aV].
\end{aligned}
\tag{95.70}
$$

第一行中所有含两个$V$再乘$\mathcal D_aV$的项，至少有五次奇坐标而为零。保留的二阶系数是$2g^2-4g^2=-2g^2$，这给出交换子前的因子。将其代入式[（95.67）](#eq:c95-nonabelian-strength-definition)后，阿贝尔部分已经算过，只需新求$[V,\mathcal D_aV]$的$\bar t$系数。

令$V_2=B^\mu v_\mu$、$V_3=t\bar\theta\lambda^\dagger+\bar t\theta\lambda$表示二次和三次部分。对$\bar t\theta$项，只可能有$[V_2,\partial_aV_2]$。把点坐标缩并后，其系数为
<span id="eq:c95-vector-commutator-projection"></span>

$$
[V_2,\partial_aV_2]_{\bar t}
 =\frac12\theta^c\sigma^\nu_{c\dot d}\sigma^\mu_{a\dot b}
              \epsilon^{\dot d\dot b}[v_\nu,v_\mu]
 =i(S_L^{\mu\nu})_a{}^c\theta_c[v_\mu,v_\nu].
\tag{95.71}
$$

第一个$1/2$来自两个点坐标的缩并。将两个sigma用式[（35.18）](/posts/srednicki-35/#eq:c35-left-generator-product)分解，度规部分被反对称的群交换子消去，留下第二式。也可用一个具体分量查看符号：取$v_0=X,v_1=Y$、$a=1$，则$V_2=(u\bar u+w\bar w)X+(u\bar w+w\bar u)Y$，而$\partial_1V_2=\bar uX+\bar wY$。交叉乘积给$2u\bar u\bar w[X,Y]=u\bar t[X,Y]$，与右边的$iS_L^{\mu\nu}\theta[v_\mu,v_\nu]$相同。

对于$t\bar t$项，只有$[V_2,\partial_a(t\bar\theta\lambda^\dagger)]$与$[t\bar\theta\lambda^\dagger,\partial_aV_2]$。前者用$\partial_at=2\theta_a$，后者用$\partial_aB^\mu=\sigma^\mu_{a\dot b}\bar\theta^{\dot b}$；将两种theta分别缩并，各得
<span id="eq:c95-gaugino-commutator-projection"></span>

$$
\begin{aligned}
\relax[V_2,\partial_a(t\bar\theta\lambda^\dagger)]_{t\bar t}
 &=\frac12\sigma^\mu_{a\dot b}[v_\mu,\lambda^{\dagger\dot b}],\\
[t\bar\theta\lambda^\dagger,\partial_aV_2]_{t\bar t}
 &=\frac12\sigma^\mu_{a\dot b}[v_\mu,\lambda^{\dagger\dot b}].
\end{aligned}
\tag{95.72}
$$

含$\bar t\theta\lambda$的相应乘积有三个点坐标而为零；$\mathcal D_a$中带时空导数的部分与$V$相乘也至少五次。这就列尽了新增项。

式[（95.70）](#eq:c95-finite-connection-expansion)的交换子项在$\widehat W$中带$-g/4$，再乘投影$-4$，给$g$乘刚算出的系数。因此最终只是将式[（95.57）](#eq:c95-field-strength-components)中的场强和导数换成
<span id="eq:c95-nonabelian-components"></span>

$$
\begin{aligned}
F_{\mu\nu}&=\partial_\mu v_\nu-\partial_\nu v_\mu-ig[v_\mu,v_\nu],\\
D_\mu^{\rm ad}\lambda^\dagger
 &=\partial_\mu\lambda^\dagger-ig[v_\mu,\lambda^\dagger],\\
\widehat W_a&=\lambda_a+\theta_aD
       -(S_L^{\mu\nu})_a{}^c\theta_cF_{\mu\nu}
       +it\sigma^\mu_{a\dot b}(D_\mu^{\rm ad}\lambda^\dagger)^{\dot b}.
\end{aligned}
\tag{95.73}
$$

例如场强中的$-ig[v_\mu,v_\nu]$与前面的$-S_L\theta$相乘，正好给$+igS_L\theta[v_\mu,v_\nu]$。规范微子项中的$i(-ig)=g$也与式[（95.72）](#eq:c95-gaugino-commutator-projection)一致。

采用$\operatorname{Tr}_R(T_R^AT_R^B)=T(R)\delta^{AB}$，且选$T(R)\ne0$的表示写矩阵，归一的规范作用量为
<span id="eq:c95-nonabelian-gauge-action"></span>

$$
\begin{aligned}
\mathcal L_{\rm gauge}
 &=\frac1{4T(R)}\operatorname{Tr}_R[\widehat W^a\widehat W_a]_F+\mathrm{h.c.}\\
 &\simeq i\lambda^{\dagger A}\bar\sigma^\mu(D_\mu^{\rm ad}\lambda)^A
       -\frac14F^{A\mu\nu}F^A_{\mu\nu}+\frac12D^AD^A.
\end{aligned}
\tag{95.74}
$$

旋量迹的计算与阿贝尔情形相同，群矩阵则在乘积外取迹；二次群迹产生的$T(R)$恰被分母消去。规范微子分部积分使用协变导数，交换子项在群迹的循环性质下也组成全导数。乘积规范群应对每个因子分别采用它的耦合与归一。

物质部分的有序展开沿式[（95.50）](#eq:c95-matter-interaction-expansion)进行，保留群矩阵在两个物质场之间的位置，便有
<span id="eq:c95-nonabelian-matter-action"></span>

$$
\begin{aligned}
\mathcal L_{\rm matter}={}&-(D^\mu A)^\dagger D_\mu A
       +i\psi^\dagger\bar\sigma^\mu D_\mu\psi+F^\dagger F\\
 &+\sqrt2g(A^\dagger\lambda^AT_R^A\psi
                +\psi^\dagger T_R^A\lambda^{\dagger A}A)
       -gD^AA^\dagger T_R^AA.
\end{aligned}
\tag{95.75}
$$

多个表示分别求和。若再加入规范不变的超势，$F_i$仍按式[（95.36）](#eq:c95-f-elimination)消去；$D^A$也只以二次及一次出现，令$J^A=\sum_iA_i^\dagger T_{R_i}^AA_i$，则
<span id="eq:c95-d-potential"></span>

$$
\frac12D^AD^A-gD^AJ^A
 =\frac12(D^A-gJ^A)^2-\frac{g^2}{2}J^AJ^A,\qquad
D^A=gJ^A,\qquad V_D=\frac{g^2}{2}J^AJ^A.
\tag{95.76}
$$

这样，标量势分成超势给出的F项平方和与规范相互作用给出的D项平方和。下一节构造超对称标准模型时，正要用这两部分确定Higgs势；下面先用具体模型研究辅助场的非零真空值和超对称自发破缺，再写出SQED的完整分量作用量。

<span id="ex95-1"></span>

## 超荷与能量的正性

在正定物理态空间中，取$Q_a^\dagger$为$Q_a$的伴随，态处于这些算符共同的定义域。将式[（95.1）](#eq:c95-superalgebra)的混合反对易子对$a=\dot a$求和，使用$P_0=-H$、$\operatorname{tr}\sigma^0=2$及$\operatorname{tr}\sigma^i=0$，有
<span id="eq:x95-positive-hamiltonian"></span>

$$
\sum_{a=1}^2\{Q_a,Q_a^\dagger\}=4H,\qquad
\langle\Psi|H|\Psi\rangle
 =\frac14\sum_a\left(\|Q_a\Psi\|^2+\|Q_a^\dagger\Psi\|^2\right)\ge0.
\tag{95.77}
$$

这证明哈密顿量半正定。若$|\Psi\rangle$是可归一化的零能量态，右边各项都非负，和为零迫使每项分别为零，所以所有$Q_a,Q_a^\dagger$都湮灭该态。反过来，若全部超荷湮灭一个态，算符等式也直接给$H|\Psi\rangle=0$。这里能量零点已经由超对称代数固定，不能在保持同一代数的同时另给$H$加任意常数。

<span id="ex95-2"></span>

## 辅助场的破缺判据

<span id="ex95-2a"></span>

### F项

假定真空保持超对称，则$Q_a|0\rangle=Q_a^\dagger|0\rangle=0$。在式[（95.25）](#eq:c95-chiral-component-transformations)中取真空期望，
<span id="eq:x95-f-breaking-order-parameter"></span>

$$
0=\langle0|\{\psi_c,Q_a\}|0\rangle
 =-i\sqrt2\epsilon_{ac}\langle F\rangle.
\tag{95.78}
$$

左边第一项中的$Q_a$湮灭右真空，第二项中的$Q_a$则因$Q_a^\dagger|0\rangle=0$而湮灭左真空。选$a\ne c$，epsilon非零，便有$\langle F\rangle=0$。取逆否命题，非零的辅助$F$真空期望必然破坏超对称。多个手征场中，只要有一个$F_i$非零便已足够。

<span id="ex95-2b"></span>

### D项

这里要注意$\widehat W_a$是奇超场。偶$V$满足$[V,Q_b]=-i\mathcal Q_bV$；在等式两边作用构成$\widehat W_a$的三个奇超协变导数，每个都与$\mathcal Q_b$反对易，故
<span id="eq:x95-odd-strength-transformation"></span>

$$
\{\widehat W_a,Q_b\}=+i\mathcal Q_b\widehat W_a.
\tag{95.79}
$$

这个正号与偶手征场的负号不同。采用前面的手征坐标，$\mathcal Q_b=\partial_b$，并且$\partial_b\theta_c=\epsilon_{cb}$。在式[（95.57）](#eq:c95-field-strength-components)中取最低分量，得到
<span id="eq:x95-d-breaking-order-parameter"></span>

$$
\begin{aligned}
\{\lambda_a,Q_b\}
 &=i\epsilon_{ab}D-i(S_L^{\mu\nu})_a{}^c\epsilon_{cb}F_{\mu\nu},\\
\epsilon^{ab}\{\lambda_a,Q_b\}&=-2iD.
\end{aligned}
\tag{95.80}
$$

第一项使用$\epsilon^{ab}\epsilon_{ab}=-2$；第二项的epsilon收缩等于$-\operatorname{Tr}S_L^{\mu\nu}=0$，也可由两下指标的$S_L$对称直接看出。若真空保持超对称，反对易子的真空期望为零，因此$\langle D\rangle=0$。非零$D$期望也是破缺的充分判据。对规范理论，这些真空关系须在物理态空间及相容的超对称算符定义中使用；下面的势能计算则给出树级真空中的具体实现。

<span id="ex95-3"></span>

## O’Raifeartaigh模型：破缺与真空位置

先取$m,\kappa,v$为正实且非零，$[m]=[v]=1$、$[\kappa]=0$，超势为$W=mBC+\kappa A(C^2-v^2)$。三个一阶导数给
<span id="eq:x95-oraifeartaigh-potential"></span>

$$
\begin{aligned}
W_A&=\kappa(C^2-v^2),&W_B&=mC,&W_C&=mB+2\kappa AC,\\
V&=\kappa^2|C^2-v^2|^2+m^2|C|^2+|mB+2\kappa AC|^2.
\end{aligned}
\tag{95.81}
$$

若全部$F$为零，$W_B=0$先给$C=0$，但这时$W_A=-\kappa v^2\ne0$，产生矛盾。因此任何真空都不能使全部辅助场消失，超对称因而自发破缺。

为了找到极小值，先固定$A,C$，选择$B=-2\kappa AC/m$，使最后一个平方为零。设$x=|C|^2\ge0$。第一项中的$-2v^2\operatorname{Re}C^2$要求非零$C$的相位使$C^2$正实，于是只需极小化
<span id="eq:x95-oraifeartaigh-radial-minimum"></span>

$$
f(x)=\kappa^2(x-v^2)^2+m^2x,\qquad
f'(x)=2\kappa^2(x-v^2)+m^2,
\qquad f''(x)=2\kappa^2>0.
\tag{95.82}
$$

若无约束驻点为负，就取端点$x=0$；否则取驻点。因此真空族为
<span id="eq:x95-oraifeartaigh-vacuum-branches"></span>

$$
\begin{cases}
C=B=0,\quad A\in\mathbb C,&m^2\ge2\kappa^2v^2,\\[2pt]
C=\pm\sqrt{v^2-m^2/(2\kappa^2)},\quad
B=-2\kappa AC/m,\quad A\in\mathbb C,
&m^2<2\kappa^2v^2.
\end{cases}
\tag{95.83}
$$

每一支都沿复$A$方向平坦；第二个参数区间有两条这样的平坦线。在任一平稳点，$\partial_{A_j}V=W_{ij}W_i^*=0$，而破缺使向量$W_i^*$非零。因此费米质量矩阵$W_{ij}$有一个零向量$W_i^*$，对应无质量的Goldstone费米子（goldstino）。

还可以在平坦线的任一点求出全部树级质量。记该点为$(A_0,B_0,c)$，其中$c$取上式相应的实根。模型有$R(A)=R(B)=2$、$R(C)=0$的经典R对称性，因而可把$A_0$的相位转掉，质量谱只依赖$|A_0|$。定义
<span id="eq:x95-or-spectrum-parameters"></span>

$$
M_*=\sqrt{m^2+4\kappa^2c^2},\qquad
h=2\kappa|A_0|,\qquad b_*=2\kappa^2(v^2-c^2),
\qquad
\begin{pmatrix}X\\Y\end{pmatrix}
=\frac1{M_*}
\begin{pmatrix}m&-2\kappa c\\2\kappa c&m\end{pmatrix}
\begin{pmatrix}\delta A\\\delta B\end{pmatrix}.
$$

这个实正交变换保持标准动能。$X$沿平坦线，$Y$则与$\delta C$耦合。原费米质量矩阵及其在$(X,Y,\delta C)$基中的形式为
<span id="eq:x95-or-fermion-masses"></span>

$$
W_{ij}=
\begin{pmatrix}
0&0&2\kappa c\\
0&0&m\\
2\kappa c&m&h
\end{pmatrix}
\ \longrightarrow\
\begin{pmatrix}
0&0&0\\
0&0&M_*\\
0&M_*&h
\end{pmatrix},
\qquad
m_{F,0}=0,\qquad
m_{F,\pm}=\frac{\sqrt{h^2+4M_*^2}\pm h}{2}.
$$

右边两个非零质量是实对称块本征值的绝对值，也就是其正奇异值。零模$\psi_X$正沿辅助场的非零方向：当$c=0$时只有$F_A$非零；当$c\ne0$时，$(W_A^*,W_B^*)$正比于$(m,-2\kappa c)$。

标量质量还受到超势三阶导数的影响。把$z_i=(A,B,C)$在真空附近展开，二次势是
<span id="eq:x95-or-quadratic-potential"></span>

$$
V^{(2)}
=\delta z^\dagger(W''^\dagger W'')\delta z
 +\frac12\left(W_i^*W_{ijk}\delta z_j\delta z_k+\mathrm{h.c.}\right)
=\left|M_*\delta C\right|^2+
 \left|M_*Y+h\delta C\right|^2
 -\frac{b_*}{2}\left[(\delta C)^2+(\delta C^*)^2\right].
$$

这里唯一非零的第二种系数为$W_i^*W_{iCC}=2\kappa W_A^*=-b_*$。因此$X$的两个实分量均无质量。再写$Y=(Y_R+iY_I)/\sqrt2$、$\delta C=(C_R+iC_I)/\sqrt2$，两个实对称质量平方块为
<span id="eq:x95-or-scalar-masses"></span>

$$
\begin{gathered}
\mathsf H_\eta=
\begin{pmatrix}
M_*^2&hM_*\\
hM_*&M_*^2+h^2+\eta b_*
\end{pmatrix},
\qquad
\eta=-1\ \text{对应实部},\quad \eta=+1\ \text{对应虚部},\\
m_{B,\eta,\pm}^2
=M_*^2+\frac{h^2+\eta b_*}{2}
 \pm\frac12\sqrt{(h^2+\eta b_*)^2+4h^2M_*^2}.
\end{gathered}
$$

这给出余下四个实标量的质量。第一真空区间有$M_*^2=m^2\ge b_*=2\kappa^2v^2$；第二区间有$M_*^2=4\kappa^2v^2-m^2>b_*=m^2$。所以两个块的迹为正、行列式$M_*^2(M_*^2+\eta b_*)$非负，所求各点确为稳定的树级极小值。在边界$m^2=2\kappa^2v^2$上，实部块另有一个零本征值。平坦方向能否在量子修正后继续保持平坦，需要计算有效势。

<span id="ex95-4"></span>

## 超对称量子电动力学

<span id="ex95-4a"></span>

### 分量作用量

取两个独立手征场$\Phi_+$、$\Phi_-$，分量为$(A_q,\psi_q,F_q)$，$q=\pm1$。取$D_\mu^{(q)}=\partial_\mu-iqe v_\mu$以及$W=m\Phi_+\Phi_-$。超场作用量为
<span id="eq:x95-sqed-superfield-action"></span>

$$
\mathcal L=\sum_{q=\pm1}[\Phi_q^\dagger e^{-2qeV}\Phi_q]_{22}
       +\left[\frac14\widehat W^a\widehat W_a+m\Phi_+\Phi_-\right]_F
       +\mathrm{h.c.},
\tag{95.84}
$$

其中h.c.只加在F项上，前面的D项已经为实。对两个电荷分别在式[（95.51）](#eq:c95-charged-component-action)中置$g=qe$，再加规范动能。超势部分由$W_+=mA_-$、$W_-=mA_+$及$W_{+-}=W_{-+}=m$给出，因此
<span id="eq:x95-sqed-component-action"></span>

$$
\begin{aligned}
\mathcal L={}&-\frac14F_{\mu\nu}F^{\mu\nu}
       +i\lambda^\dagger\bar\sigma^\mu\partial_\mu\lambda+\frac12D^2\\
 &+\sum_{q=\pm1}\left[-(D^{(q)\mu}A_q)^*D_\mu^{(q)}A_q
       +i\psi_q^\dagger\bar\sigma^\mu D_\mu^{(q)}\psi_q+|F_q|^2\right]\\
 &+\sqrt2e\left(A_+^*\lambda\psi_+-A_-^*\lambda\psi_-+\mathrm{h.c.}\right)
       -eD(|A_+|^2-|A_-|^2)\\
 &+\left[m(A_+F_-+A_-F_+-\psi_+\psi_-)+\mathrm{h.c.}\right].
\end{aligned}
\tag{95.85}
$$

两个不同物种的奇旋量标量积满足$\psi_+\psi_-=\psi_-\psi_+$，所以两个Hessian交叉元素与$1/2$相消，质量项为$-m\psi_+\psi_-$。它把两个相反电荷的Weyl场组合成一个Dirac场。

<span id="ex95-4b"></span>

### 消去辅助场

逐个辅助场变分，得到
<span id="eq:x95-sqed-auxiliary-solutions"></span>

$$
F_+=-m^*A_-^*,\qquad F_-=-m^*A_+^*,\qquad
D=e(|A_+|^2-|A_-|^2).
\tag{95.86}
$$

代回时，两个$F$平方各留下$-|m|^2|A_q|^2$；$D$的完成平方留下$-e^2(|A_+|^2-|A_-|^2)^2/2$。消元后的作用量就是式[（95.85）](#eq:x95-sqed-component-action)的规范、物质动能，加上
<span id="eq:x95-sqed-eliminated-action"></span>

$$
\begin{aligned}
\mathcal L_{\rm nonkinetic}
 &=-V-m\psi_+\psi_--m^*\psi_+^\dagger\psi_-^\dagger
       +\sqrt2e(A_+^*\lambda\psi_+-A_-^*\lambda\psi_-+\mathrm{h.c.}),\\
V&=|m|^2(|A_+|^2+|A_-|^2)
       +\frac{e^2}{2}(|A_+|^2-|A_-|^2)^2.
\end{aligned}
\tag{95.87}
$$

当$m\ne0$时，真空为$A_+=A_-=0$，全部辅助场为零。两个复标量和Dirac费米子的质量为$|m|$，光子与规范微子无质量；$m=0$时则出现$|A_+|=|A_-|$的平坦真空族。两个物质Weyl场的电荷满足$1^3+(-1)^3=0$以及$1+(-1)=0$，同时消去阿贝尔立方反常与混合引力规范反常。

<span id="ex95-5"></span>

## Fayet–Illiopoulos项

<span id="ex95-5a"></span>

### 超对称与规范不变性

加入$\mathcal L_{\rm FI}=e\xi D=2e\xi[V]_{22}$，其中$\xi$为质量平方量纲的实常数。式[（95.30）](#eq:c95-d-term-transformation)说明其超变换是全导数，故作用量保持超对称。超规范变换式[（95.42）](#eq:c95-gauge-parameter-increment)给$\Delta D=\partial^2a/2$，于是规范变化的积分也是表面项。

若试图沿非阿贝尔方向加入$\xi_AD^A$，普通规范变换要求$\xi_Af^{ABC}=0$。这意味着$\xi$必须是伴随表示中的不变向量，也就是李代数的中心方向；非阿贝尔简单群没有这样的非零向量。因此FI项只允许沿$U(1)$因子加入。一个同时含非阿贝尔因子的乘积群仍可在它的$U(1)$方向具有此项。

<span id="ex95-5b"></span>

### 加入SQED并消元

在[刚才的SQED作用量](#ex95-4)中加入FI项后，$F_\pm$方程不变，而$D$部分变成
<span id="eq:x95-fi-potential"></span>

$$
\begin{aligned}
\mathcal L_D&=\frac12D^2-eD(|A_+|^2-|A_-|^2-\xi),\\
D&=e(|A_+|^2-|A_-|^2-\xi),\\
V&=|m|^2(|A_+|^2+|A_-|^2)
       +\frac{e^2}{2}(|A_+|^2-|A_-|^2-\xi)^2.
\end{aligned}
\tag{95.88}
$$

其余动能、质量和Yukawa项均由式[（95.87）](#eq:x95-sqed-eliminated-action)给出。

<span id="ex95-5c"></span>

### 真空的两个区域

取$e>0$、$m\ne0$。令$z=|A_+|^2-|A_-|^2$，则固定$z$时有$|A_+|^2+|A_-|^2\ge|z|$，且只保留一种带电标量即可达到等号。因此问题化为在实轴上极小化
<span id="eq:x95-fi-one-variable-minimum"></span>

$$
f(z)=|m|^2|z|+\frac{e^2}{2}(z-\xi)^2.
\tag{95.89}
$$

在$z>0$区间导数为$|m|^2+e^2(z-\xi)$，其零点只有$\xi>|m|^2/e^2$时落在本区间；在$z<0$区间导数为$-|m|^2+e^2(z-\xi)$，同理只有$\xi<-|m|^2/e^2$时有内部零点。其余情况两个单侧导数夹住零，极小值在$z=0$。故
<span id="eq:x95-fi-vacuum-energy"></span>

$$
\begin{aligned}
z_{\min}&=\begin{cases}
0,&|\xi|\le |m|^2/e^2,\\
\xi-\operatorname{sign}(\xi)|m|^2/e^2,&|\xi|>|m|^2/e^2,
\end{cases}\\
V_{\min}&=\begin{cases}
e^2\xi^2/2,&|\xi|\le |m|^2/e^2,\\
|m|^2|\xi|-|m|^4/(2e^2),&|\xi|>|m|^2/e^2.
\end{cases}
\end{aligned}
\tag{95.90}
$$

第一种情况$A_+=A_-=0$，$D=-e\xi$、$F_\pm=0$，普通$U(1)$未破缺。第二种情况与$\xi$同号的电荷标量凝聚，普通规范对称性也破缺，同时$D=-\operatorname{sign}(\xi)|m|^2/e$以及另一多重态的$F$非零。只要$\xi\ne0$，两种区域的真空能都严格为正，超对称都破缺；阈值区分的是标量是否凝聚。当$m=0$时，可选$z=\xi$使全部辅助场为零，所以前面的破缺判据需要$m\ne0$这个条件。

<span id="ex95-6"></span>

## R对称性

<span id="ex95-6a"></span>

### 物质场的R荷

定义荷为$r_X$的场按以下相位方向变换：$X\mapsto e^{-ir_X\alpha}X$，并固定$r_\lambda=1$，矢量及$D$中性。物质Yukawa项$A_i^*\lambda\psi_i$的不变性要求
$-r_{A_i}+1+r_{\psi_i}=0$。在场强展开$\widehat W_a=\lambda_a+\theta_aD+\cdots$中，$\lambda$荷为1而$D$中性，因此取$\theta$荷为1，使各项具有相同的总荷。记$r_i=r_{A_i}$，再比较$A_i+\sqrt2\theta\psi_i+tF_i$各项，得到
<span id="eq:x95-r-component-charges"></span>

$$
r_{\psi_i}=r_i-1,\qquad r_{F_i}=r_i-2.
\tag{95.91}
$$

动能只配同一场与其共轭，自动不变；前面的规范微子动能及$D$耦合也分别中性。

<span id="ex95-6b"></span>

### 对超势的限制

把耦合参数固定为R中性。超势必须具有荷2，即
<span id="eq:x95-r-superpotential-condition"></span>

$$
W(e^{-ir_i\alpha}A_i)=e^{-2i\alpha}W(A_i).
\tag{95.92}
$$

逐项微分可知$W_i$荷为$2-r_i$，故$W_iF_i$荷为零；$W_{ij}$荷为$2-r_i-r_j$，也恰好抵消$\psi_i\psi_j$的$r_i+r_j-2$。因此这个条件同时保证辅助场耦合和Yukawa项不变，消元后$|W_i|^2$亦不变。对于多项式超势，每个非零单项式中的场荷之和必须为2；无动力学作用的常数超势可另行忽略。

<span id="ex95-6c"></span>

### SQED的选择

当$m\ne0$时，$W=mA_+A_-$给$r_++r_-=2$。最对称的选择是
<span id="eq:x95-sqed-r-charges"></span>

$$
r_{A_+}=r_{A_-}=1,\qquad r_{\psi_+}=r_{\psi_-}=0,
\qquad r_{F_+}=r_{F_-}=-1,
\qquad r_\lambda=1.
\tag{95.93}
$$

也可取$r_+=1+s,r_-=1-s$，相当于把R流与电荷流作线性组合。量子理论中的混合反常由[第75节的三角系数](/posts/srednicki-75/#c75)确定。对这个SQED例，规范微子为阿贝尔中性，物质贡献为$\sum q_i^2r_{\psi_i}=s-s=0$，所以R流的阿贝尔规范混合反常也相消。

---

[← 第 94 节](/posts/srednicki-94/) · [章节地图](/srednicki/) · [第 96 节 →](/posts/srednicki-96/)
