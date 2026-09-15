---
title: 'Srednicki §51 汤川理论中的圈修正'
date: 2026-09-14
category: 笔记
tags: [物理, 量子场论, Srednicki]
series: 'Srednicki QFT'
srednickiSections: [51]
hideFromHome: true
draft: false
---

<span id="c51"></span>

前几章已经给出费米子的传播子、顶角和外态规则，并用它们计算了树图。
现在将同样的规则用于圈图。重整化的思路仍与标量理论相同：
先找出对称性允许的局部项，再用质量、场归一和耦合的定义决定反项。
新的工作主要在分子上。标量圈的分子通常是数，费米圈却带着有序的gamma矩阵；
一条费米线闭合时，还会出现反对易关系带来的负号。
我们将先算两个传播子，再算两个相互作用顶角，看看这些变化怎样进入结果。

<span id="c51-model"></span>

## 选取一个便于计算的理论

圈修正会产生哪些相互作用，可以先由量纲和对称性判断。
在四维中，动能项给出$[\varphi]=1$、$[\Psi]=3/2$，
所以系数具有非负质量量纲的纯标量项可以一直写到$\varphi^4$。
对于原来的$g\varphi\bar\Psi\Psi$理论，$\varphi$在宇称下为偶，
线性项、三次项和四次项都不受对称性禁止。
即使起初把它们的系数设为零，圈积分也一般要求相应反项。

含费米子的候选项少得多。两个费米场已经占去三个质量维数，
因而最多再加一个导数或一个标量场。洛伦兹不变的动能、质量和原汤川项
已经在拉氏量中；赝标量质量$i\bar\Psi\gamma_5\Psi$违反宇称，
而$\Psi^T\mathcal C\Psi$在$\Psi\mapsto e^{i\alpha}\Psi$下带有两单位相位，
违反狄拉克场的$U(1)$对称性。四费米项的维数为六，属于负量纲耦合。
分部积分后，这样便列尽了本节所需的局部项。

为了少处理两个新的标量耦合，我们改选
<span id="eq:c51-pseudoscalar-coupling"></span>

$$
\mathcal L_{\rm Yuk}=ig\varphi\bar\Psi\gamma_5\Psi,\qquad
P^{-1}\varphi(\mathbf x,t)P=-\varphi(-\mathbf x,t).
\tag{51.1}
$$

$i\bar\Psi\gamma_5\Psi$是厄米的赝标量，故实$g$使相互作用厄米，
而$\varphi$的奇宇称使乘积为偶。现在$\varphi$和$\varphi^3$都为奇，
只有$\varphi^4$仍须加入。这里保留狄拉克的$U(1)$及相应离散对称性；
讨论围绕保持宇称的$\langle\varphi\rangle=0$真空进行。
第45—50章的标量汤川顶角为$ig$，本节则由$i\mathcal L_{\rm Yuk}$
得到$-g\gamma_5$。这一改变会同时影响闭圈的迹和开链的分子。

将拉氏量分成自由部分和微扰部分：
<span id="eq:c51-lagrangian"></span>

$$
\begin{aligned}
\mathcal L&=\mathcal L_0+\mathcal L_1,\\
\mathcal L_0&=i\bar\Psi\slashed\partial\Psi-m\bar\Psi\Psi
 -\frac12\partial^\mu\varphi\partial_\mu\varphi-\frac12M^2\varphi^2,\\
\mathcal L_1&=iZ_g g\varphi\bar\Psi\gamma_5\Psi
 -\frac{Z_\lambda\lambda}{4!}\varphi^4+\mathcal L_{\rm ct},\\
\mathcal L_{\rm ct}
&=i\delta Z_\Psi\bar\Psi\slashed\partial\Psi
 -\delta Z_m m\bar\Psi\Psi
 -\frac12\delta Z_\varphi(\partial\varphi)^2
 -\frac12\delta Z_M M^2\varphi^2,\qquad \delta Z_j=Z_j-1 .
\end{aligned}
\tag{51.2}
$$

场与质量的四个反项将由两个传播子的极点位置和留数确定。
耦合则在外四动量为零时定义，使相应顶角等于树级值。
这是本节选取的在壳方案；只消去维数极点的$\overline{\mathrm{MS}}$方案
将在这些反项的有限部分作不同选择。

以下取$m>0$及$0<M<2m$。于是赝标量不能衰变为电子–正电子对，
两个基本粒子在所讨论的微扰真空中都有孤立的单粒子极点。
圈积分沿既有约定取$d=4-\epsilon$，并写
<span id="eq:c51-dimension-scales"></span>

$$
g_d=\widetilde\mu^{\epsilon/2}g,\qquad
\lambda_d=\widetilde\mu^\epsilon\lambda,\qquad
\mu^2=4\pi e^{-\gamma_E}\widetilde\mu^2 .
\tag{51.3}
$$

在$d$维，$[\varphi]=1-\epsilon/2$、$[\Psi]=3/2-\epsilon/2$，
所以这两个尺度幂正好补回耦合的维数。
后面在顶角中提出共同的树级尺度幂，每个单圈积分便都带
$\widetilde\mu^\epsilon$。我们保留各图的单圈贡献，包括有限部分，
并在最后令$\epsilon\to0$。

<span id="c51-spectral"></span>

## 精确传播子的极点与连续谱

在计算反项之前，先说明它们要保持怎样的传播子。
[第13节](/posts/srednicki-13/#c13-spectral)已从中间态求和推得实场的谱表示。
把那里的单粒子质量换成$M$，并按LSZ要求归一化场，得到
<span id="eq:c51-scalar-spectral"></span>

$$
\widetilde{\boldsymbol\Delta}(k^2)
=\frac1{k^2+M^2-i0}
 +\int_{M_{\rm th}^2}^\infty ds\,\frac{\rho(s)}{k^2+s-i0},
\qquad \rho(s)\ge0,\qquad M_{\rm th}=\min(2m,3M).
\tag{51.4}
$$

两个阈值分别来自费米子–反费米子和三个赝标量。
两个自旋零粒子若要由自旋零场产生，在质心系必须取轨道角动量$L=0$。
两个赝标量的内禀宇称相乘为正，轨道因子$(-1)^L$也为正，
因而不能与$\varphi$的奇宇称相接。三个赝标量则可以构成奇宇称的总自旋零态。
这给出本节微扰粒子谱中的最低连续阈值；若另有束缚态，谱中还须另列其极点。

将截去外传播子的单粒子不可约二点图之和记为$i\Pi$。
第14节的几何级数于是给出
<span id="eq:c51-scalar-pole-conditions"></span>

$$
\widetilde{\boldsymbol\Delta}^{-1}(k^2)
=k^2+M^2-i0-\Pi(k^2),\qquad
\Pi(-M^2)=0,\qquad \Pi'(-M^2)=0 .
\tag{51.5}
$$

第一个条件保持极点在$k^2=-M^2$；在极点附近作一次泰勒展开，
分母的线性项为$(k^2+M^2)[1-\Pi'(-M^2)]$，
所以第二个条件使留数为一。它们共同固定$\delta Z_M$和$\delta Z_\varphi$，
包括两个有限部分。

费米子的谱表示需要两个实函数。为确定它们对应的洛伦兹结构，我们在矩阵元
$\langle0|\Psi_a(x)\bar\Psi_b(0)|0\rangle$中插入完整态集，
再按中间态的总四动量$q$和不变质量$s=-q^2$分组。
平移不变性给出$e^{iqx}$；自旋指标组成一个$4\times4$矩阵。
宇称守恒排除了$\gamma_5$和$\slashed q\gamma_5$，
单个四动量又不能组成非零的反对称二阶张量。
因而只剩$I$与$\slashed q$两种结构。将系数归一写成
<span id="eq:c51-wightman-spectral"></span>

$$
\begin{aligned}
W_>(x)&:=\langle0|\Psi(x)\bar\Psi(0)|0\rangle\\
&=\int_0^\infty ds\int\frac{d^3q}{(2\pi)^3\,2\omega_s}
\bigl[-\slashed q\,\sigma_1(s)+\sqrt{s}\,\sigma_2(s)\bigr]e^{iqx},
\qquad \omega_s=\sqrt{\mathbf q^2+s}.
\end{aligned}
\tag{51.6}
$$

正性可以直接在中间态静止系看出。
把式[（51.6）](#eq:c51-wightman-spectral)的谱分子记为$R(q)$。
乘上$\beta=\gamma^0$后，中间态矩阵变成
$\sum_n\langle0|\Psi|n\rangle\langle n|\Psi^\dagger|0\rangle$，
是正半定的。由于$q=(\sqrt{s},\mathbf0)$时$-\slashed q=\sqrt{s}\beta$，
它的两组本征值为
<span id="eq:c51-spectral-positivity"></span>

$$
R(q)\beta=\sqrt{s}\,[\sigma_1(s)I+\sigma_2(s)\beta],
\qquad \sqrt{s}\,[\sigma_1(s)\pm\sigma_2(s)]\ge0.
\tag{51.7}
$$

因此$\sigma_1\ge|\sigma_2|$，并非只需$\sigma_1\ge\sigma_2$。
有离散谱时，这一不等式理解为对两种非负谱测度
$\sigma_1+\sigma_2$和$\sigma_1-\sigma_2$的要求。

单位留数的单粒子贡献由$\sum_su_s\bar u_s=-\slashed q+m$给出，
故两函数都含$\delta(s-m^2)$。在本理论的电荷共轭关系下，
另一算符次序中的反粒子贡献将质量项变号，正如自由场的
$\sum_sv_s\bar v_s=-\slashed q-m$。
把这两个次序按费米子的时间排序合并，再对$q^0$作
[第42节的极点积分](/posts/srednicki-42/#c42)，每个固定$s$都给出质量为$\sqrt{s}$的分母。
从$\sigma_{1,2}$中分离单粒子$\delta$项，便得到
<span id="eq:c51-fermion-spectral"></span>

$$
\begin{aligned}
\widetilde{\boldsymbol S}(\slashed p)
&=\frac{-\slashed p+m}{p^2+m^2-i0}
 +\int_{m_{\rm th}^2}^\infty ds\,
 \frac{-\slashed p\,\rho_1(s)+\sqrt{s}\,\rho_2(s)}
 {p^2+s-i0},\\
\rho_1(s)&\ge|\rho_2(s)|,\qquad m_{\rm th}=m+M .
\end{aligned}
\tag{51.8}
$$

带一个单位狄拉克荷的中间态可以是一个费米子加一个赝标量，
其阈值为$m+M$。只由费米子和反费米子组成的下一种态至少含三个粒子，
阈值为$3m$；$M<2m$保证前者更低。
这也解释了为何费米谱不能从两个费米粒子开始。

为了把极点条件写得像标量情形一样简洁，将
$z=\slashed p$视为解析变量。gamma代数给$z^2=-p^2$，
所以无穷小边界处的自由传播子可写成$(z+m-i0)^{-1}$，
物理极点在$z=-m$。这里的线性$i0$只规定靠近极点的边界方向。
若保留一个有限的正数$\delta$，精确的因子化应写成
<span id="eq:c51-pole-factorization"></span>

$$
\zeta_\delta(s)=\sqrt{s-i\delta},\quad \operatorname{Re}\zeta_\delta>0,
\qquad
(-z+\zeta_\delta)(z+\zeta_\delta)=p^2+s-i\delta .
\tag{51.9}
$$

展开$\zeta_\delta=\sqrt{s}-i\delta/(2\sqrt{s})+O(\delta^2)$后，
才能把每个线性因子记成相应的$i0$边界。
由于连续谱从$m_{\rm th}>m$开始，
它在孤立的单粒子极点附近解析，因而不影响下面的局部展开：
<span id="eq:c51-fermion-pole-conditions"></span>

$$
\widetilde{\boldsymbol S}^{-1}(z)=z+m-i0-\Sigma(z),
\qquad \Sigma(-m)=0,\qquad \Sigma'(-m)=0 .
\tag{51.10}
$$

$i\Sigma$是截去外传播子的1PI费米二点图之和。
前一条件固定质量，后一条件固定留数，从而决定$\delta Z_m$与$\delta Z_\Psi$。
求导时必须同时使用$p^2=-z^2$；圈积分中的$p^2$不是独立于$z$的变量。
这个细节将在费米自能的有限反项中产生一个质量平方因子。

<span id="c51-scalar-loop"></span>

## 标量自能：闭圈、迹与参数积分

现在开始计算。到单圈阶，标量二点函数有闭合费米圈、标量蝌蚪和二价反项三种贡献。
下图中实线箭头规定费米流，虚线表示赝标量：

<span id="fig:c51-scalar-selfenergy"></span>

![标量二点函数的费米圈、标量蝌蚪和二价反项三种贡献](/images/srednicki/s51_scalar_self_energy.svg)

标量自能的三个贡献。闭圈的两段动量为$\ell$与$\ell+k$；
中图的两条圈端接在同一个四标量顶点，右图的叉号表示二价反项。

每个汤川顶角给$-g\gamma_5$，每条内部费米线给$\widetilde S/i$，
每条闭合费米圈再给$-1$。这个号来自奇场的换序，下面用四次源求导把它写出。
把自旋指标沿闭链相接便形成迹，因此
<span id="eq:c51-scalar-loop-integrand"></span>

$$
\begin{aligned}
i\Pi_\Psi(k^2)
&=(-1)(-g)^2(1/i)^2
\int\frac{d^4\ell}{(2\pi)^4}
\operatorname{Tr}\!\left[
\widetilde S(\ell+k)\gamma_5\widetilde S(\ell)\gamma_5\right],\\
\widetilde S(p)&=\frac{-\slashed p+m}{p^2+m^2-i0}.
\end{aligned}
\tag{51.11}
$$

三个显式因子的乘积为$+g^2$。
在圈图内令$Z_g=1$已足够，因$\delta Z_g$本身从更高耦合阶开始；
它在这幅图中的插入属于下一阶修正。
利用$\gamma_5^2=1$及$\gamma_5\slashed\ell=-\slashed\ell\gamma_5$，
分子中的两个$\gamma_5$先相消：
<span id="eq:c51-scalar-numerator"></span>

$$
\begin{aligned}
\operatorname{Tr}[(-\slashed\ell-\slashed k+m)
\gamma_5(-\slashed\ell+m)\gamma_5]
&=\operatorname{Tr}[(-\slashed\ell-\slashed k+m)(\slashed\ell+m)]\\
&=4[(\ell+k)\cdot\ell+m^2]\equiv4N .
\end{aligned}
\tag{51.12}
$$

线性gamma项的迹为零；二次项使用
$\operatorname{Tr}(\slashed a\slashed b)=-4a\cdot b$，
与分子已有的负号相乘后成为正的内积。
本节先把这类成对的$\gamma_5$消去，再对剩余迹作维数延拓，
并取$\operatorname{Tr}I=4$。顶角计算也将只留下链末的一个$\gamma_5$。
这样足以处理本节各图；它没有用到含一个$\gamma_5$的闭迹，
也不把第47节的四维$\epsilon$迹公式延拓为任意$d$维恒等式。

<span id="c51-loop-source-sign"></span>

闭圈的负号可以在作动量积分以前确定。沿[第43节的左导数规则](/posts/srednicki-43/#c43-left-derivatives)，费米自由源泛函和插入为

$$
Z_F=e^{i\bar\eta S\eta},\qquad
\bar\Psi_a\longleftrightarrow i\partial^L_{\eta_a},\qquad
\Psi_b\longleftrightarrow\frac1i\partial^L_{\bar\eta_b}.
$$

为同时处理标量和赝标量顶角，暂记双线性为$\bar\Psi G\Psi$，其中$G$是普通偶矩阵。令$B_c(y)=(\bar\eta S)_c(y)$、$C_d(y)=(S\eta)_d(y)$；它们都是奇量。在第一个顶点依次作用两个左导数，得

$$
\begin{aligned}
\partial^L_{\bar\eta_d(y)}Z_F&=iC_d(y)Z_F,\\
\partial^L_{\eta_c(y)}\partial^L_{\bar\eta_d(y)}Z_F
&=iS_{dc}(y,y)Z_F-iC_d(y)[-iB_c(y)Z_F]\\
&=[iS_{dc}(y,y)+B_c(y)C_d(y)]Z_F.
\end{aligned}
$$

再作用另一个顶点的$\partial^L_{\bar\eta_b(x)}$。第一项给$-S_{dc}(y,y)C_b(x)Z_F$，第二项给$S_{bc}(x,y)C_d(y)Z_F$以及含三个源的项。最后作用$\partial^L_{\eta_a(x)}$并令源为零，便有

<span id="eq:c51-four-source-derivatives"></span>

$$
\left.
\partial^L_{\eta_a(x)}\partial^L_{\bar\eta_b(x)}
\partial^L_{\eta_c(y)}\partial^L_{\bar\eta_d(y)}Z_F
\right|_0
=-S_{ba}(x,x)S_{dc}(y,y)+S_{bc}(x,y)S_{da}(y,x).
$$

第一项是两个同点收缩的乘积；第二项才把两个顶点连成一条闭链。物理费米收缩为$K_F=S/i$，故第二项中的$SS=-K_FK_F$。乘上两个顶点矩阵并缩并指标，得到

$$
\langle T(\bar\Psi G\Psi)_x(\bar\Psi G\Psi)_y\rangle_{0,c}
=-\operatorname{Tr}[G K_F(x-y)G K_F(y-x)].
$$

指数展开的$1/2!$再与两条固定标量外腿接到两个顶点的$2!$种方法相消。取赝标量的$G=\gamma_5$和顶角$-g\gamma_5$，截去外标量传播子后，正好得到式[（51.11）](#eq:c51-scalar-loop-integrand)的$(-1)(-g)^2(1/i)^2$。闭圈号由此直接来自源导数次序。

分母的处理与第14节相同。用$x$合并两条线，令$a=x(1-x)$，
再平移$q=\ell+xk$，有
<span id="eq:c51-scalar-parameterization"></span>

$$
\begin{aligned}
&x[(\ell+k)^2+m^2]+(1-x)(\ell^2+m^2)
=(\ell+xk)^2+m^2+ak^2,\\
D&=m^2+ak^2,\\
N&=q^2-ak^2+m^2+(1-2x)k\cdot q,\\
i\Pi_\Psi(k^2)
&=4g^2\int_0^1dx\,\widetilde\mu^\epsilon
\int\frac{d^dq}{(2\pi)^d}\frac{N}{(q^2+D-i0)^2}.
\end{aligned}
\tag{51.13}
$$

这一步的平移与删去奇$q$项，先在积分收敛的维数域进行，
再由维数正规化的解析延拓定义发散处的结果。
因此不会在平移动量时另引入一个截止边界项。
外动量可先取使$D>0$的区域，算完后沿原分母的$-i0$继续延拓。

两个所需的动量积分都已包含在[第31节的四维展开](/posts/srednicki-31/#c31-integrals)中。
为追踪分子$q^2$所带来的有限常数，这里把代入写开。记
<span id="eq:c51-master-integral"></span>

$$
\begin{aligned}
I_n(D)&:=\widetilde\mu^\epsilon
\int\frac{d^dq}{(2\pi)^d}\frac1{(q^2+D-i0)^n}\\
&=\frac{i\widetilde\mu^\epsilon}{(4\pi)^{d/2}}
\frac{\Gamma(n-d/2)}{\Gamma(n)}D^{d/2-n}.
\end{aligned}
\tag{51.14}
$$

$i$来自$q^0=iq_E^0$的威克旋转。
取$n=2$时，$\Gamma(\epsilon/2)=2/\epsilon-\gamma_E+O(\epsilon)$；
同时展开$(4\pi\widetilde\mu^2/D)^{\epsilon/2}$，便把$\gamma_E$和$4\pi$
并入$\mu$。取$n=1$时还要用
$\Gamma(-1+\epsilon/2)=\Gamma(\epsilon/2)/(-1+\epsilon/2)$。
这个分母的一阶展开产生额外的常数一：
<span id="eq:c51-two-integrals"></span>

$$
\begin{aligned}
I_2(D)&=\frac{i}{16\pi^2}
\left[\frac2\epsilon-\ln\frac D{\mu^2}\right]+O(\epsilon),\\
I_1(D)&=-\frac{iD}{16\pi^2}
\left[\frac2\epsilon+1-\ln\frac D{\mu^2}\right]+O(\epsilon),\\
\widetilde\mu^\epsilon
\int\frac{d^dq}{(2\pi)^d}\frac{q^2}{(q^2+D-i0)^2}
&=I_1(D)-DI_2(D)\\
&=-\frac{2iD}{16\pi^2}
\left[\frac2\epsilon+\frac12-\ln\frac D{\mu^2}\right]+O(\epsilon).
\end{aligned}
\tag{51.15}
$$

最后一步用了$q^2=(q^2+D)-D$，其中常数$1/2$
来自前两个积分的相减。

把式[（51.15）](#eq:c51-two-integrals)代回，剩余的$x$积分分成多项式和对数两部分。
从动量积分中提出公共因子$i/(16\pi^2)$后，被积式为
<span id="eq:c51-scalar-integrand-expanded"></span>

$$
\begin{aligned}
&-2D\left[\frac2\epsilon+\frac12-\ln\frac D{\mu^2}\right]
 +(m^2-ak^2)\left[\frac2\epsilon-\ln\frac D{\mu^2}\right]\\
&\hspace{6mm}
=-\frac{2m^2+6ak^2}{\epsilon}
 -(m^2+ak^2)+(m^2+3ak^2)\ln\frac D{\mu^2}.
\end{aligned}
\tag{51.16}
$$

利用$\int_0^1a\,dx=1/6$，并除去$i\Pi$前的$i$，得到
<span id="eq:c51-scalar-loop-result"></span>

$$
\Pi_\Psi(k^2)
=-\frac{g^2}{4\pi^2}\left[
\frac{k^2+2m^2}{\epsilon}+\frac{k^2}{6}+m^2
-\int_0^1dx\,(3ak^2+m^2)\ln\frac D{\mu^2}\right].
\tag{51.17}
$$

发散部分只有$k^2$和质量平方两种局部结构，
正好可由标量动能和质量的反项吸收。
非多项式的动量依赖留在对数中；它将决定连续谱及传播子的离壳变化。

<span id="c51-scalar-subtraction"></span>

## 标量的质量和场归一

费米圈之外，还要加上四标量顶点产生的蝌蚪图。
它与第31节的图相同，只需把内部质量换成$M$。
两个外腿接到顶点有$4\cdot3$种方式，剩余两腿互相缩并，
与顶点的$1/4!$相乘后给$1/2$。
因此$i\Pi_\varphi=(-i\lambda)(1/i)I_1(M^2)/2$，即
<span id="eq:c51-scalar-tadpole-counterterm"></span>

$$
\Pi_\varphi
=\frac{\lambda M^2}{16\pi^2}
\left[\frac1\epsilon+\frac12-\frac12\ln\frac{M^2}{\mu^2}\right],
\qquad
\Pi_{\rm ct}=-\delta Z_\varphi k^2-\delta Z_M M^2 .
\tag{51.18}
$$

蝌蚪图与外动量无关，所以它只直接改变质量项。
将它与费米圈相加，按$k^2$和常数分别抵消$1/\epsilon$，得到
<span id="eq:c51-scalar-counterterm-poles"></span>

$$
\begin{aligned}
\left.\delta Z_\varphi\right|_{\rm pole}
&=-\frac{g^2}{4\pi^2\epsilon},\\
\left.\delta Z_M\right|_{\rm pole}
&=\frac1\epsilon\left[
\frac{\lambda}{16\pi^2}
-\frac{g^2m^2}{2\pi^2M^2}\right].
\end{aligned}
\tag{51.19}
$$

有限部分还没有确定，因为消去发散并不足以定义物理质量和场归一。
若记$F(y)=\Pi_\Psi(y)+\Pi_\varphi$、$y=k^2$，
两个在壳条件要求
<span id="eq:c51-scalar-double-subtraction"></span>

$$
\begin{aligned}
\delta Z_\varphi&=F'(-M^2),\\
\delta Z_M&=\frac{F(-M^2)}{M^2}+F'(-M^2),\\
\Pi(y)&=F(y)-F(-M^2)-(y+M^2)F'(-M^2).
\end{aligned}
\tag{51.20}
$$

这个减除式同时去掉$F$在极点处的值和斜率。
尤其$\Pi_\varphi$作为常数被整个吸收，所以最终自能在$\lambda$的一次阶
不再有贡献；$\lambda$仍留在将拉氏量质量与裸质量联系起来的反项中。

两次减除会消去常数项和一次多项式，有限动量依赖只需从下式求出：
$H(y)=\int_0^1dx\,(3ay+m^2)\ln[(m^2+ay)/\mu^2]$。
它的导数包含两项：前因子求导给$3a\ln(D/\mu^2)$，
对数求导给$a(3ay+m^2)/D$。
把$y_0=-M^2$代入式[（51.20）](#eq:c51-scalar-double-subtraction)，
前一项与$H(y_0)$合起来将对数变成$\ln(D/D_0)$；
后一项给一个线性有限反项。结果为
<span id="eq:c51-scalar-renormalized"></span>

$$
\begin{aligned}
\Pi(k^2)&=\frac{g^2}{4\pi^2}
\left[\int_0^1dx\,(3ak^2+m^2)\ln\frac{D}{D_0}
 +\kappa_\varphi(k^2+M^2)\right],\\
D_0&=m^2-aM^2,\qquad
\kappa_\varphi=\int_0^1dx\,
\frac{a(3aM^2-m^2)}{D_0}.
\end{aligned}
\tag{51.21}
$$

$a\le1/4$且$M<2m$，故$D_0>0$，减除点没有越过二费米阈值。
在$k^2=-M^2$处，对数为零，线性项也为零；再求一次导数，
积分给$\int a(m^2-3aM^2)/D_0$，恰与$\kappa_\varphi$抵消。
因而两个在壳条件都已实现。

有限归一常数还可以显式积分，借此看出接近阈值时的行为。
令$r=M^2/m^2$，其中$0<r<4$，把分子除以$1-ra$，有
<span id="eq:c51-scalar-kappa-closed"></span>

$$
\begin{aligned}
\kappa_\varphi
&=-\frac12+\frac2r[J(r)-1],\\
J(r)&=\int_0^1\frac{dx}{1-rx(1-x)}
=\frac4{\sqrt{r(4-r)}}\arctan\sqrt{\frac r{4-r}} .
\end{aligned}
\tag{51.22}
$$

第二行令$u=2x-1$后成为
$4\int_0^1du/(4-r+ru^2)$，其原函数是一个反正切。
在小$r$处，直接展开$J=1+r/6+r^2/30+\cdots$，
得到$\kappa_\varphi=-1/6+r/15+\cdots$。
当$r\to4^-$时，$D_0$在$x=1/2$附近变小，$J$随之增大；
归一条件对阈值的敏感性由此显现。
若离壳动量远离极点与阈值，且各动量和质量尺度同阶、没有大的对数，
传播子的相对单圈修正便为$g^2/(4\pi^2)$量级。

<span id="c51-fermion-loop"></span>

## 费米自能：开链与混合质量

接着计算费米传播子。下图的一圈贡献含一条内部费米线和一条标量线，
自旋指标沿外部费米线连通，不形成迹，也没有闭圈的额外负号：

<span id="fig:c51-fermion-selfenergy"></span>

![费米子自能的标量交换圈和动能质量反项，内部费米动量为p加ell](/images/srednicki/s51_fermion_self_energy.svg)

费米自能。内部费米动量为$p+\ell$，上方标量弧的动量$\ell$
流向左顶点。右图表示费米动能及质量反项。

仍按逆着费米箭头的次序相乘，两个顶角夹住内部传播子，得到
<span id="eq:c51-fermion-loop-integrand"></span>

$$
\begin{aligned}
i\Sigma_{\rm loop}(\slashed p)
&=(-g)^2(1/i)^2\widetilde\mu^\epsilon
\int\frac{d^d\ell}{(2\pi)^d}\,
\gamma_5\widetilde S(p+\ell)\gamma_5\,
\widetilde\Delta(\ell^2),\\
\widetilde\Delta(\ell^2)&=\frac1{\ell^2+M^2-i0},\\
\gamma_5(-\slashed p-\slashed\ell+m)\gamma_5
&=\slashed p+\slashed\ell+m .
\end{aligned}
\tag{51.23}
$$

显式因子这次为$-g^2$。
用$x$乘费米分母、$1-x$乘标量分母，令$q=\ell+xp$，
则
<span id="eq:c51-fermion-parameterization"></span>

$$
\begin{aligned}
&x[(\ell+p)^2+m^2]+(1-x)(\ell^2+M^2)=q^2+D,\\
D&=x(1-x)p^2+xm^2+(1-x)M^2,\\
N&=\slashed q+(1-x)\slashed p+m,\\
i\Sigma_{\rm loop}(\slashed p)
&=-g^2\int_0^1dx\,\widetilde\mu^\epsilon
\int\frac{d^dq}{(2\pi)^d}\frac{N}{(q^2+D-i0)^2}.
\end{aligned}
\tag{51.24}
$$

这个$D$把两条不同质量的传播子合在一起；它不同于标量自能中的
$m^2+x(1-x)k^2$。删去奇$\slashed q$项后，
整个矩阵分子都与积分变量无关，因而只需$I_2(D)$：
<span id="eq:c51-fermion-loop-result"></span>

$$
\Sigma_{\rm loop}(z)
=-\frac{g^2}{16\pi^2}\left[
\frac{z+2m}{\epsilon}
-\int_0^1dx\,[(1-x)z+m]\ln\frac D{\mu^2}\right],
\qquad z=\slashed p .
\tag{51.25}
$$

其中$z/\epsilon$来自$(2/\epsilon)\int_0^1(1-x)z\,dx$，
$2m/\epsilon$来自质量项在整个单位区间上的积分。
费米自能的质量维数为一，发散也只含$z$与$m$两种允许的结构。

二价反项为
$\Sigma_{\rm ct}=-\delta Z_\Psi z-\delta Z_m m$。
分别比较这两种结构的极点，得到
<span id="eq:c51-fermion-counterterm-poles"></span>

$$
\left.\delta Z_\Psi\right|_{\rm pole}
=-\frac{g^2}{16\pi^2\epsilon},\qquad
\left.\delta Z_m\right|_{\rm pole}
=-\frac{g^2}{8\pi^2\epsilon}.
\tag{51.26}
$$

有限部分仍由极点条件决定。
令$F(z)=\Sigma_{\rm loop}(z)$，
与标量的两次减除一样，现在应取
<span id="eq:c51-fermion-double-subtraction"></span>

$$
\begin{aligned}
\delta Z_\Psi&=F'(-m),\qquad
\delta Z_m=\frac{F(-m)}m+F'(-m),\\
\Sigma(z)&=F(z)-F(-m)-(z+m)F'(-m).
\end{aligned}
\tag{51.27}
$$

这里必须对$D=-x(1-x)z^2+xm^2+(1-x)M^2$一起求导。
在$z=-m$处，分子$(1-x)z+m=xm$，
而$D'=2x(1-x)m$。于是对数导数带来的有限项为
$2x^2(1-x)m^2/D_0$，其中
<span id="eq:c51-fermion-renormalized"></span>

$$
\begin{aligned}
D_0&=x^2m^2+(1-x)M^2,\\
\Sigma(z)&=\frac{g^2}{16\pi^2}
\left[\int_0^1dx\,[(1-x)z+m]\ln\frac D{D_0}
 +\kappa_\Psi(z+m)\right],\\
\kappa_\Psi&=-2\int_0^1dx\,\frac{x^2(1-x)m^2}{D_0}.
\end{aligned}
\tag{51.28}
$$

在减除点，积分及线性项同时为零；
其导数则由刚算出的正项与$\kappa_\Psi$抵消。
$m,M>0$保证$D_0$在闭区间上为正，
所以费米单粒子极点与连续谱之间确有解析邻域。
与标量情形比较可见，反项的确定并未增加新的原则；
新增的工作是保留开链的矩阵结构，并在求导时正确处理$z^2=-p^2$。

<span id="c51-vertex"></span>

## 汤川顶角的单圈修正

两个传播子已按物理质量和单位留数归一化，还须确定相互作用的强度。
先看一条赝标量线与两条费米线相接的顶角。
令费米动量从$p$变为$p'$，流入的标量动量便为$k=p'-p$。
本节的顶角函数用$iV_Y(p',p)$表示截去外传播子后的图之和，
所以树级$iV_Y=-g\gamma_5$。
一圈贡献如下：

<span id="fig:c51-yukawa-vertex"></span>

![赝标量汤川顶角的一圈修正，两段内费米线动量为p加ell与p撇加ell](/images/srednicki/s51_vertex.svg)

汤川顶角的一圈图。沿费米箭头，两段内线分别携带$p+\ell$和$p'+\ell$；
上方标量弧携带$\ell$，中央入射动量满足$k=p'-p$。

三次顶角与三条内部传播子的因子相乘为
$(-g)^3(1/i)^3=-ig^3$。保留矩阵的顺序，有
<span id="eq:c51-vertex-loop"></span>

$$
\begin{aligned}
iV_Y(p',p)&=-Z_g g\gamma_5+iV_{Y,{\rm loop}}(p',p),\\
iV_{Y,{\rm loop}}(p',p)
&=(-g)^3(1/i)^3\widetilde\mu^\epsilon
\int\frac{d^d\ell}{(2\pi)^d}
\gamma_5\widetilde S(p'+\ell)\gamma_5
\widetilde S(p+\ell)\gamma_5\widetilde\Delta(\ell^2).
\end{aligned}
\tag{51.29}
$$

两边按圈数保留到单圈阶，$g$与$\lambda$作为两个独立耦合计数；更高圈项还包括混合耦合修正。

将最左边的两个$\gamma_5$移到一起，分子成为
$N=(\slashed p'+\slashed\ell+m)(-\slashed p-\slashed\ell+m)\gamma_5$。
令动量$\ell+p$和$\ell+p'$的费米分母分别乘$x_1,x_2$，标量分母乘$x_3$。
沿[第14节已证明的参数公式](/posts/srednicki-14/#c14-parameters)，使用
<span id="eq:c51-vertex-parameters"></span>

$$
\begin{aligned}
dF_3&=2!\,dx_1dx_2dx_3\,
\delta(1-x_1-x_2-x_3),\quad x_i\ge0,\quad \int dF_3=1,\\
q&=\ell+x_1p+x_2p',\\
D&=x_1(1-x_1)p^2+x_2(1-x_2)p'^2-2x_1x_2p\cdot p'\\
&\hspace{8mm}+(x_1+x_2)m^2+x_3M^2 .
\end{aligned}
\tag{51.30}
$$

第一行的$2!$来自合并三个一次分母，不是图的对称因子。
消去$x_3$后，积分域是$0\le x_1\le1$、$0\le x_2\le1-x_1$，
面积为$1/2$，因此测度确实归一为一。
第二、三行则来自
$x_1(\ell+p)^2+x_2(\ell+p')^2+x_3\ell^2$
配成$q^2$后留下的常数。

在分子中也作同一平移。为保持两个开链矩阵的次序，记
<span id="eq:c51-vertex-numerator"></span>

$$
\begin{aligned}
A&=-x_1\slashed p+(1-x_2)\slashed p'+m,\\
B&=-(1-x_1)\slashed p+x_2\slashed p'+m,\\
N&=(\slashed q+A)(-\slashed q+B)\gamma_5\\
&=q^2\gamma_5+AB\gamma_5
 +(\slashed q B-A\slashed q)\gamma_5,\\
\widetilde N&=AB\gamma_5,\\
iV_{Y,{\rm loop}}
&=-ig^3\int dF_3\,\widetilde\mu^\epsilon
\int\frac{d^dq}{(2\pi)^d}\frac{N}{(q^2+D-i0)^3}.
\end{aligned}
\tag{51.31}
$$

首项的正号来自$-\slashed q\slashed q=q^2$。
末项对$q$为奇，积分后为零；$\widetilde N$则是与$q$无关的有序矩阵。
一般的$p,p'$使$A,B$不对易，不能把它们当作两个普通数交换。

现在只有两个径向积分需要计算。
在式[（51.14）](#eq:c51-master-integral)中取$n=3$，得到
$I_3=i/(32\pi^2D)+O(\epsilon)$。
对于$q^2$项，使用$I_2-DI_3$，因而
<span id="eq:c51-vertex-loop-result"></span>

$$
\begin{aligned}
I_3(D)&=\frac{i}{32\pi^2D}+O(\epsilon),\\
\widetilde\mu^\epsilon
\int\frac{d^dq}{(2\pi)^d}\frac{q^2}{(q^2+D-i0)^3}
&=\frac{i}{16\pi^2}
\left[\frac2\epsilon-\ln\frac D{\mu^2}-\frac12\right]+O(\epsilon),\\
iV_{Y,{\rm loop}}
&=\frac{g^3}{8\pi^2}\left[
\left(\frac1\epsilon-\frac14-\frac12\int dF_3\ln\frac D{\mu^2}\right)\gamma_5
 +\frac14\int dF_3\frac{\widetilde N}{D}\right].
\end{aligned}
\tag{51.32}
$$

原来的$-i$与积分的$i$相乘，使最后一行的整体系数为正。
只有$q^2$项产生对数发散，且其矩阵结构仍为$\gamma_5$。
因此一个汤川反项就足以抵消它：
<span id="eq:c51-vertex-counterterm-pole"></span>

$$
\left.\delta Z_g\right|_{\rm pole}=\frac{g^2}{8\pi^2\epsilon}.
\tag{51.33}
$$

有限的$-1/4$与$\widetilde N/D$项决定了零外动量处的减除量，下面用它们固定耦合。

<span id="c51-vertex-subtraction"></span>

## 用零动量顶角定义耦合

用零动量顶角定义汤川耦合，条件为$V_Y(0,0)=ig\gamma_5$，也就是$iV_Y(0,0)=-g\gamma_5$。
零外动量不满足有质量外粒子的在壳条件；它在这里是一个便于明确规定耦合的
离壳减除点。由于$m,M>0$，这个点没有红外奇性。

先直接在圈图分子中令$p=p'=0$。
这比分别积分式[（51.32）](#eq:c51-vertex-loop-result)的两项更简便：
<span id="eq:c51-vertex-zero-cancellation"></span>

$$
N=(\slashed\ell+m)(-\slashed\ell+m)\gamma_5
=(\ell^2+m^2)\gamma_5 .
\tag{51.34}
$$

交叉项$m\slashed\ell-m\slashed\ell$相消，
余下的一因子约掉两条同质量费米分母中的一条。
于是三分母积分化为两分母积分，只需一个参数：
<span id="eq:c51-vertex-zero-integral"></span>

$$
\begin{aligned}
iV_{Y,{\rm loop}}(0,0)
&=-ig^3\gamma_5\widetilde\mu^\epsilon
\int\frac{d^d\ell}{(2\pi)^d}
\frac1{(\ell^2+m^2-i0)(\ell^2+M^2-i0)}\\
&=\frac{g^3}{16\pi^2}
\left[\frac2\epsilon-L(m^2,M^2;\mu^2)\right]\gamma_5,\\
L(A,B;\mu^2)&=\int_0^1dx\,
\ln\frac{xA+(1-x)B}{\mu^2}.
\end{aligned}
\tag{51.35}
$$

令$t=B+x(A-B)$，有$dx=dt/(A-B)$，
再用$\int\ln(t/\mu^2)\,dt=t\ln(t/\mu^2)-t$，得到
<span id="eq:c51-vertex-zero-closed"></span>

$$
L(A,B;\mu^2)=
\begin{cases}
\displaystyle
\frac{A\ln(A/\mu^2)-B\ln(B/\mu^2)}{A-B}-1,&A\ne B,\\[2mm]
\ln(A/\mu^2),&A=B.
\end{cases}
\tag{51.36}
$$

$A=B$处的表面分母由可去奇点构成，
因为分子的差商趋于$\ln(A/\mu^2)+1$。
由$-\delta Z_g g\gamma_5+iV_{Y,{\rm loop}}(0,0)=0$，
全部单圈反项为
<span id="eq:c51-vertex-counterterm-finite"></span>

$$
\delta Z_g=\frac{g^2}{16\pi^2}
\left[\frac2\epsilon-L(m^2,M^2;\mu^2)\right].
\tag{51.37}
$$

它既包含此前的极点，也包含当前耦合定义所需的有限部分。

一般动量处，只需从圈图减去其零动量值。
令$D_{00}=(x_1+x_2)m^2+x_3M^2$，
并注意$\widetilde N(0,0)=m^2\gamma_5$，
式[（51.32）](#eq:c51-vertex-loop-result)中的极点和常数便同时消去：
<span id="eq:c51-vertex-renormalized"></span>

$$
\begin{aligned}
iV_Y(p',p)=-g\gamma_5+\frac{g^3}{8\pi^2}
\bigg[&
-\frac12\int dF_3\ln\frac D{D_{00}}\,\gamma_5\\
&+\frac14\int dF_3
\left(\frac{\widetilde N}{D}-\frac{m^2\gamma_5}{D_{00}}\right)\bigg].
\end{aligned}
\tag{51.38}
$$

这里每一项都是确定的有限参数积分；在$D$越过负实轴时，
对数和分母沿原费曼处方取边界值。
在$p=p'=0$，两项的被积函数分别为零，因此耦合条件直接成立。
这也可以从三参数积分直接验证。令$A=m^2$、$B=M^2$、$y=x_1+x_2$，则$D_*=yA+(1-y)B$。在$0\le x_1\le y\le1$上积分，测度化为

$$
\int dF_3 f(x_1+x_2)=2\int_0^1dy\int_0^y dx_1,f(y)
=2\int_0^1y f(y),dy.
$$

记$L_3=2\int_0^1y\ln(D_*/\mu^2)\,dy$、$R_3=2\int_0^1y/D_*\,dy$。在$g^3\gamma_5/(16\pi^2)$的归一下，式[（51.32）](#eq:c51-vertex-loop-result)的有限部分为$-1/2-L_3+AR_3/2$，两分母算法则给$-L$。对$y(y-1)\ln(D_*/\mu^2)$作分部积分，两端的边界项都为零，于是

<span id="eq:c51-zero-vertex-equivalence"></span>

$$
\begin{aligned}
0&=\int_0^1dy\left[(2y-1)\ln\frac{D_*}{\mu^2}
+y(y-1)\frac{A-B}{D_*}\right],\\
L_3-L&=(A-B)\int_0^1\frac{y(1-y)}{D_*}\,dy\\
&=A\int_0^1\frac y{D_*}\,dy-\int_0^1y\,dy
=\frac A2R_3-\frac12.
\end{aligned}
$$

第二个等号用了$A-D_*=(A-B)(1-y)$。所以$-1/2-L_3+AR_3/2=-L$，两种计算给出完全相同的有限反项；测度的$2!$和径向积分中的常数项都参与了这一等式。

<span id="c51-four-vertex"></span>

## 四标量顶角与新耦合的必要性

最后计算四条外标量线的顶角。
除了已经在第31节处理过的纯标量泡图，还多出一个四边形费米圈。
固定一个外标签后，其余三个标签在有向闭圈上有$3!=6$种排列。
这是狄拉克圈；反向排列也属于这些收缩中的一项，不能再将六项除以二。
下图只画其中一种，所有外动量均流入：

<span id="fig:c51-fermion-box"></span>

![四条外标量线连接的有向费米盒图，四段内动量从左弧起依次标出](/images/srednicki/s51_box.svg)

四标量顶角的一种费米盒图。四个外动量均入射，$\sum_i k_i=0$。
本图把圈动量$\ell$选在左弧，四段动量可直接用于正文的传播子链。

沿逆箭头方向读取，矩阵链为
<span id="eq:c51-four-fermion-loop"></span>

$$
\begin{aligned}
iV_{4,\Psi}
=-g^4\widetilde\mu^\epsilon
\int\frac{d^d\ell}{(2\pi)^d}\,
\operatorname{Tr}\big[&
\widetilde S(\ell)\gamma_5
\widetilde S(\ell-k_1)\gamma_5\\
&\times\widetilde S(\ell+k_2+k_3)\gamma_5
\widetilde S(\ell+k_2)\gamma_5\big]
 +\text{另外五种排列}.
\end{aligned}
\tag{51.39}
$$

整体负号是闭费米圈的号；四顶角给$g^4$，四条内线给$(1/i)^4=1$。
图中的圈动量从左弧起标；顺着箭头逐个加入流入顶点的外动量，就得到式[（51.39）](#eq:c51-four-fermion-loop)中的四条内线。

本节只需从一般四点图中抽出局部发散，供后续重整化群计算使用。
四个费米传播子的大动量行为各为$1/\ell$，
故四维圈积分的表面发散度为零。
在大$\ell$展开中增加一个外动量，便至少再减去一幂$\ell$，
所以发散项不依赖外动量。
保持$m>0$而令全部$k_i=0$，不会引入新的红外发散，
可以直接求出这个局部系数。

只取分子的最高动量项时，
$\operatorname{Tr}[(\slashed\ell\gamma_5)^4]=4(\ell^2)^2$。
在零外动量处，连质量项也可以一起化简：
<span id="eq:c51-four-fermion-zero"></span>

$$
\begin{aligned}
{}[(-\slashed\ell+m)\gamma_5]^2
&=(-\slashed\ell+m)(\slashed\ell+m)
 =(\ell^2+m^2)I,\\
\operatorname{Tr}\!\left\{[(-\slashed\ell+m)\gamma_5]^4\right\}
&=4(\ell^2+m^2)^2,\\
V_{4,\Psi}(0)
&=-\frac{24g^4}{i}I_2(m^2)
 =-\frac{3g^4}{\pi^2}
\left[\frac1\epsilon-\frac12\ln\frac{m^2}{\mu^2}\right].
\end{aligned}
\tag{51.40}
$$

因子24为六种排列乘以狄拉克迹的4。
最后一行同时保留了极点和零动量方案需要的有限项。
纯标量部分有三个道，每道的对称因子为$1/2$。
沿[第31节的顶点计数](/posts/srednicki-31/#c31-fourpoint)，
$(-i\lambda)^2(1/i)^2=+\lambda^2$，
因此在零外动量处
<span id="eq:c51-four-scalar-zero"></span>

$$
V_{4,\varphi}(0)
=\frac{3\lambda^2}{2i}I_2(M^2)
=\frac{3\lambda^2}{16\pi^2}
\left[\frac1\epsilon-\frac12\ln\frac{M^2}{\mu^2}\right].
\tag{51.41}
$$

两个顶角使纯标量圈从耦合的二次阶开始。

将两个圈与树顶角相加，
$V_4=-Z_\lambda\lambda+V_{4,\Psi}+V_{4,\varphi}$。
按照零外动量的定义$V_4(0)=-\lambda$，包含有限部分的加性反项为
<span id="eq:c51-quartic-counterterm"></span>

$$
\begin{aligned}
\delta\lambda:=\lambda\delta Z_\lambda
&=\frac{3\lambda^2}{16\pi^2}
\left[\frac1\epsilon-\frac12\ln\frac{M^2}{\mu^2}\right]
-\frac{3g^4}{\pi^2}
\left[\frac1\epsilon-\frac12\ln\frac{m^2}{\mu^2}\right],\\
\left.\delta Z_\lambda\right|_{\rm pole}
&=\frac1\epsilon\left[
\frac{3\lambda}{16\pi^2}-\frac{3g^4}{\pi^2\lambda}\right],
\qquad \lambda\ne0 .
\end{aligned}
\tag{51.42}
$$

当$\lambda=0$时，$Z_\lambda$的这种乘法记法不再适合，
但第一行的$\delta\lambda$仍有明确意义。
尤其$g\ne0$时它含非零的$g^4$项：
只保留汤川相互作用而不允许四标量反项，便无法消去四点函数的发散。
开头由量纲与对称性提出的要求，现在由一幅具体的圈图实现了。

至此，两个传播子的质量和留数、两个顶角在零动量处的数值都已经固定。
反项的极点只记录局部短距离结构，有限部分则体现本节对参数的定义；
传播子的对数和顶角的有限参数函数保留了实际动量依赖。
下一节将利用这些局部反项考察参数随重整化尺度的变化。

<span id="c51-source-reference"></span>

---

[← 第 50 节](/posts/srednicki-50/) · [章节地图](/srednicki/) · [第 52 节 →](/posts/srednicki-52/)
