---
title: 'Srednicki §75 手征规范理论与反常'
date: 2026-09-14
category: 笔记
tags: [物理, 量子场论, Srednicki]
series: 'Srednicki QFT'
srednickiSections: [75]
hideFromHome: true
draft: false
---

<span id="c75"></span>

前面所讨论的狄拉克场，同时含有左手和右手分量。把右手分量改写成
左手场的共轭以后，一个狄拉克场就等价于两个左手外尔场。它们的规范表示
互为共轭。这种安排使左右两种螺旋度以相同的方式参与相互作用，但洛伦兹不变性
本身并不要求我们一定这样安排。我们可以只保留一个带电的左手外尔场，
也可以使若干左手场处于一组不能配成共轭对的表示中。由此得到的理论称为
手征规范理论。

这样的拉格朗日密度很容易写出，困难出现在量子计算中。经典规范不变性要求的
沃德恒等式，有时无法同时成立。从最简单的手征U(1)理论
开始，先看通常的两点函数，再计算三个规范玻色子的三角图。问题最后集中在
一个具体的积分上：线性发散的圈积分在平移积分变量时，可以留下有限的边界项。
这项不能在所有外腿上同时消去，便是本节所说的反常。

最后将这些群迹用于[直积群的反常抵消](#c75-product-group)。

<span id="c75-chiral"></span>

## 从左手外尔场构造规范理论

设$\chi$属于表示$R$，$\xi$属于共轭表示$\bar R$。于是$\xi^\dagger$与
$\chi$按同一个表示变换，可以组合成

<span id="eq:c75-dirac-weyl"></span>

$$
\Psi_D=\begin{pmatrix}\chi_\alpha\\ \xi^{\dagger\dot\alpha}\end{pmatrix},
\qquad
\chi\in R,\quad \xi\in\bar R .
\tag{75.1}
$$

对U(1)，这就是说两个左手场的电荷分别为$Q$和$-Q$。
如果$R$是实表示，可以选择使共轭表示与原表示相同的实基，并以同一个
外尔场构成马约拉纳场，

<span id="eq:c75-majorana-weyl"></span>

$$
\Psi_M=\begin{pmatrix}\psi_\alpha\\ \psi^{\dagger\dot\alpha}\end{pmatrix}.
\tag{75.2}
$$

在一般基中，下半部还须乘上第70节的表示交织矩阵；这里的简单写法已经选定了
实形式。现在不要求$\psi$有共轭伙伴，直接写

<span id="eq:c75-weyl-action"></span>

$$
\begin{aligned}
\mathcal L&=i\psi^\dagger\bar\sigma^\mu D_\mu\psi
             -\frac14F_{\mu\nu}^aF^{a\mu\nu},\\
D_\mu\psi&=(\partial_\mu-igA_\mu^aT_R^a)\psi,
\qquad (T_R^a)^\dagger=T_R^a .
\end{aligned}
\tag{75.3}
$$

规范变换在$\psi^\dagger$与$D\psi$之间消去；旋量指标由$\bar\sigma^\mu$
接成四矢量，再与导数缩并。厄米共轭也没有引入新的相互作用：
协变乘积法则给出
$(D_\mu\psi)^\dagger\bar\sigma^\mu\psi
=\partial_\mu(\psi^\dagger\bar\sigma^\mu\psi)
-\psi^\dagger\bar\sigma^\mu D_\mu\psi$，
故动能取共轭后只改变一个全散度。四维中$[\psi]=3/2$、$[A]=1$、
$[g]=0$，每项的质量量纲都是4。

为什么这里没有写质量项？旋量缩并的双线性在内部指标上是对称的：

<span id="eq:c75-mass-invariant"></span>

$$
\begin{aligned}
B_{ij}&=\epsilon^{\alpha\beta}\psi_{i\alpha}\psi_{j\beta},
&
B_{ji}
&=-\epsilon^{\alpha\beta}\psi_{i\beta}\psi_{j\alpha}
 =B_{ij},\\
\mathcal L_m&=-\frac12M^{ij}B_{ij}+\text{h.c.},
&
U^TMU&=M .
\end{aligned}
\tag{75.4}
$$

第二个等号同时使用了费米负号和$\epsilon$的反对称性。因此质量矩阵必须是
规范不变的对称双线性。一个真正复型的不可约表示与其共轭不等价，
不能有这样的非退化交织；否则$M$就把$R$与$\bar R$联系起来。
非零不变$M$的核是一个不变子空间，在不可约表示中只能为零，因而任何非零交织都可逆。
实表示可以有对称交织，单个伪实表示却只有反对称交织，与$B_{ij}$缩并为零。
多个场之间仍可出现质量，例如$R$与$\bar R$配对的狄拉克质量。
一组场的质量项由整个表示空间上的不变对称双线性决定。

宇称把左手场变成右手场；若谱中没有相应的伙伴，这个变换就不保持理论。
但洛伦兹不变性、规范不变性和上述幂计数仍然成立。它们是经典构造所需的条件，
量子理论还必须使费米积分测度也能相容地定义。[第77节](/posts/srednicki-77/#c77-measure)从测度说明这一点；
本节先用费曼图找出障碍。

为使群指标暂时不妨碍计算，取单个电荷$+1$的左手场：

<span id="eq:c75-projected-action"></span>

$$
\begin{aligned}
\mathcal L&=i\psi^\dagger\bar\sigma^\mu
                 (\partial_\mu-igA_\mu)\psi-\frac14F_{\mu\nu}F^{\mu\nu},\\
\Psi_L&=P_L\Psi=\begin{pmatrix}\psi\\0\end{pmatrix},
\qquad P_L=\frac{1-\gamma_5}{2},\\
i\psi^\dagger\bar\sigma^\mu D_\mu\psi
 &=i\bar\Psi\gamma^\mu D_\mu P_L\Psi .
\end{aligned}
\tag{75.5}
$$

最后一行只是方便使用伽马矩阵的写法。实际积分变量仍是两分量$\psi$及
$\psi^\dagger$；含$P_L$的四分量动能在整个狄拉克空间上没有逆。
也可以先加入一个完全解耦的自由右手场，以普通狄拉克动能求逆，最后把所有
相互作用端投影到左手部分。右手场的自由行列式在真空归一化中消去，
所得有相互作用的关联函数相同。

第50节已经给出无质量旋量的手征投影：
$P_Lu_+=0$、$P_Lu_-=u_-$，以及$P_Lv_-=0$、$P_Lv_+=v_+$。
把它们代入自由场展开，便有

<span id="eq:c75-mode-expansion"></span>

$$
\begin{aligned}
\Psi_L(x)
 &=\sum_{s=\pm}\int\widetilde{dp}\,
  [b_s(\mathbf p)P_Lu_s(\mathbf p)e^{ipx}
   +d_s^\dagger(\mathbf p)P_Lv_s(\mathbf p)e^{-ipx}]\\
 &=\int\widetilde{dp}\,
 [b_-(\mathbf p)u_-(\mathbf p)e^{ipx}
   +d_+^\dagger(\mathbf p)v_+(\mathbf p)e^{-ipx}],\\
\widetilde{dp}&=\frac{d^3p}{(2\pi)^3\,2|\mathbf p|}.
\end{aligned}
\tag{75.6}
$$

一个这样的场含电荷$+1$、螺旋度$-1/2$的粒子，以及电荷$-1$、
螺旋度$+1/2$的反粒子。反粒子的螺旋度由$v$旋量的投影给出。

由投影后的两点函数和相互作用$gA_\mu\bar\Psi\gamma^\mu P_L\Psi$，
费曼规则为

<span id="eq:c75-feynman-rules"></span>

$$
S_L(p)=-\frac{P_L\slashed p}{p^2-i0},
\qquad
\text{内部费米线}=\frac1iS_L(p),
\qquad
\text{顶角}=ig\gamma^\mu P_L .
\tag{75.7}
$$

这里把$S_L$定义为传播函数，
图积分中的每条实际内线还带有$1/i$。下文的图因子记为$iV$或$i\Pi$。

<span id="c75-regulator"></span>

## 手征投影给正规化带来的问题

通常的维数正规化要求我们在$d$维计算伽马矩阵链。然而$\gamma_5$在此有一个
四维定义；[第47节](/posts/srednicki-47/#c47-gamma5)已经由该定义推得

<span id="eq:c75-gamma5-trace"></span>

$$
\gamma_5=i\gamma^0\gamma^1\gamma^2\gamma^3,\qquad
\operatorname{tr}(\gamma_5\gamma^\mu\gamma^\nu\gamma^\rho\gamma^\sigma)
 =-4i\varepsilon^{\mu\nu\rho\sigma},
\quad \varepsilon^{0123}=+1 .
\tag{75.8}
$$

若添上一个与原来四个伽马矩阵都反对易的$\gamma^{\hat\mu}$，把它移过$\gamma_5$
定义中的四个因子，所得号是$(-1)^4=+1$。因此这种扩维定义满足

<span id="eq:c75-split-gamma5"></span>

$$
\{\gamma_5,\gamma^\mu\}=0\quad(\mu=0,1,2,3),
\qquad
[\gamma_5,\gamma^{\hat\mu}]=0\quad(\hat\mu\text{为额外方向}) .
\tag{75.9}
$$

它不能再被当作与所有$d$维伽马矩阵都反对易的对象。若采用这种正规化，
就要一直区分四维与额外维的指标，并保留最后可能乘上紫外极点的额外维项。
下面在四维直接计算圈积分的边界项。

另一种调节尝试是泡利—维拉斯减除。按前面的传播函数定义，
引入大质量核并作差：

<span id="eq:c75-pv-kernel"></span>

$$
-\frac{P_L\slashed p}{p^2}
\ \longmapsto\
P_L\left[-\frac{\slashed p}{p^2}
 -\frac{-\slashed p+\Lambda}{p^2+\Lambda^2}\right].
\tag{75.10}
$$

大质量项把两种手征联系起来，若只给左手分量规范电荷，右手分量是解耦的，
这样的质量便不保持手征规范对称性。将同一现象写回两分量语言，
就是式[（75.4）](#eq:c75-mass-invariant)没有所需的质量交织。

还须区别传播核的减除和闭费米圈的减除。有限维格拉斯曼
积分按固定测度次序满足
$\int d\bar\eta\,d\eta\,e^{-\bar\eta K\eta}\propto\det K$，而
$\det(-K)=(-1)^N\det K$，只改变一个与背景无关的常数。
所以单把费米动能翻号，并不会把$\operatorname{Tr}\ln K$变成
$-\operatorname{Tr}\ln K$；闭圈的PV减除需要相应的调节场统计或行列式权重。
接下来从沃德恒等式中计算这一冲突。

<span id="c75-two-point"></span>

## 两点函数为何仍给通常结果

先看[下图](#fig:c75-polarization)。它与狄拉克理论的真空极化有相同拓扑，
差别只是每段费米矩阵链上的左投影。由两顶角、两传播线和一个闭费米圈，
得到下列因子排列：

![左手外尔场的真空极化圈与规范场动能反项](/images/srednicki/s75_polarization.svg)

外尔场的真空极化及规范场二点反项。
上弧沿费米箭头带$\ell+k$，下弧反向带$\ell$；
外部规范玻色子带$k$。叉号为动能反项。

<span id="fig:c75-polarization"></span>

<span id="eq:c75-polarization-integral"></span>

$$
\begin{aligned}
i\Pi_L^{\mu\nu}(k)
 &=(-1)(ig)^2\left(\frac1i\right)^2
   \int\frac{d^4\ell}{(2\pi)^4}
     \frac{N^{\mu\nu}}{(\ell+k)^2\ell^2}\\
 &\quad-i(Z_3-1)(k^2g^{\mu\nu}-k^\mu k^\nu)+O(g^4),\\
N^{\mu\nu}
 &=\operatorname{tr}
 [P_L(-\slashed\ell-\slashed k)\gamma^\mu
  P_L(-\slashed\ell)\gamma^\nu P_L]\\
 &=\operatorname{tr}
 [(\slashed\ell+\slashed k)\gamma^\mu\slashed\ell\gamma^\nu P_L].
\end{aligned}
\tag{75.11}
$$

从第二行矩阵链到最后一行，用的是
$P_L\gamma^\mu=\gamma^\mu P_R$及$P_R\gamma^\mu=\gamma^\mu P_L$。
每越过两个普通伽马矩阵，投影就回到原来的手征；于是相邻投影以$P_L^2=P_L$
合并。分母都带共同费曼处方，下文省写$i0$以便看清代数。

将最后的$P_L$分为$1/2-\gamma_5/2$。常数项恰好是狄拉克分子的一半，
另一项用式[（75.8）](#eq:c75-gamma5-trace)求出：

<span id="eq:c75-polarization-odd"></span>

$$
\begin{aligned}
N_{\rm odd}^{\mu\nu}
 &=-\frac12(\ell+k)_\alpha\ell_\beta
    \operatorname{tr}(\gamma^\alpha\gamma^\mu\gamma^\beta\gamma^\nu\gamma_5)\\
 &=2i\varepsilon^{\alpha\mu\beta\nu}k_\alpha\ell_\beta,\\
\Pi_L^{\mu\nu}
 &=\frac12\Pi_{D,\rm loop}^{\mu\nu}
 -2g^2\varepsilon^{\alpha\mu\beta\nu}k_\alpha
   \int\frac{d^4\ell}{(2\pi)^4}
       \frac{\ell_\beta}{\ell^2(\ell+k)^2}\\
 &\quad-(Z_3-1)(k^2g^{\mu\nu}-k^\mu k^\nu)+O(g^4).
\end{aligned}
\tag{75.12}
$$

分子中$\ell_\alpha\ell_\beta$的对称性使它与$\varepsilon$缩并为零。
剩下的矢量积分只有一个外部四矢量$k_\beta$。在洛伦兹协变的调节下，
其结果只能是$k_\beta$乘一个标量，所以最后仍含
$\varepsilon^{\alpha\mu\beta\nu}k_\alpha k_\beta=0$。
这个积分的表面发散次数是1：被积函数的大动量首项为
$\ell_\beta/\ell^4$。先对称积分消去这一奇项，余下的紫外发散才是对数型。

这里$\Pi_{D,\rm loop}$只指狄拉克圈图，反项仍在后面单独加入。
因而外尔场对$Z_3$的一圈贡献为狄拉克场的一半，这与它只含一半自由度一致。
对费米自能或带一条开放费米线的规范顶角，也可沿无质量矩阵链合并投影，
余下的积分就是前面无质量QED的积分，并在适当外端留下$P_L$。
把式[（66.9）](/posts/srednicki-66/#eq:c66-charge-chain)中的电荷变量改记为$g$，
单位电荷左外尔场给出的首阶贝塔函数便为

<span id="eq:c75-weyl-beta"></span>

$$
\beta_g^{\text{一个左外尔}}
 =\frac12\beta_g^{\text{一个狄拉克}}
 =\frac{g^3}{24\pi^2}+O(g^5).
\tag{75.13}
$$

这是两点函数确定的紫外系数。它尚不能说明这个单场理论的所有规范恒等式
都相容；三个规范玻色子的顶角将给出新的检验。

<span id="c75-triangle"></span>

## 三角图和外腿收缩

狄拉克理论的三个光子图由电荷共轭消去，这是
[第58节的费里选择律](/posts/srednicki-58/#c58-furry)。
单个左外尔场不具有相同的电荷共轭对称性，需要保留[下图](#fig:c75-triangles)的两个定向。我们取外动量全部流出，$p+q+r=0$，并把第一图的未收缩幅记为
$V_1^{\mu\nu\rho}(p,q,r)$。

![三条规范外线全流出、费米方向相反的两幅三角图](/images/srednicki/s75_triangles.svg)

两个定向的费米三角。
实线箭头表示费米收缩方向，波浪线旁的箭头表示流出动量。
第一图的三条内线带$\ell-p,\ell,\ell+q$；
第二图带$\ell+p,\ell,\ell-q$。
第二图也可先交换第一图的$(p,\mu)$与$(q,\nu)$，再反射圈动量得到。

<span id="fig:c75-triangles"></span>

三条传播线各带一个负的斜线动量，三个左投影仍能合并。
以下只写三角图的$O(g^3)$项，暂略$O(g^5)$及更高阶修正。因此

<span id="eq:c75-triangle-full"></span>

$$
\begin{aligned}
iV_1^{\mu\nu\rho}
 &=(-1)(ig)^3\left(\frac1i\right)^3
  \int\frac{d^4\ell}{(2\pi)^4}
  \frac{N_{\rm full}^{\mu\nu\rho}}
       {(\ell-p)^2\ell^2(\ell+q)^2},\\
N_{\rm full}^{\mu\nu\rho}
 &=\operatorname{tr}
 [(-\slashed\ell+\slashed p)\gamma^\mu(-\slashed\ell)
  \gamma^\nu(-\slashed\ell-\slashed q)\gamma^\rho P_L],\\
V^{\mu\nu\rho}(p,q,r)
 &=V_1^{\mu\nu\rho}(p,q,r)
   +V_1^{\nu\mu\rho}(q,p,r)+O(g^5).
\end{aligned}
\tag{75.14}
$$

投影中的常数$1/2$给出半个狄拉克图，两定向之和为零。
剩下的$-\gamma_5/2$与三条传播子分子的三个负号相乘，给正的$1/2$。
把这一部分的分子简记为$N$，并在暂时的公式中用
$A=\slashed\ell-\slashed p$、$B=\slashed\ell$、$D=\slashed\ell+\slashed q$，
便有

<span id="eq:c75-odd-triangle"></span>

$$
\begin{aligned}
N^{\mu\nu\rho}
 &=\frac12\operatorname{tr}(A\gamma^\mu B\gamma^\nu D\gamma^\rho\gamma_5),\\
V_1^{\mu\nu\rho}
 &=ig^3\int\frac{d^4\ell}{(2\pi)^4}
       \frac{N^{\mu\nu\rho}}{(\ell-p)^2\ell^2(\ell+q)^2}.
\end{aligned}
\tag{75.15}
$$

系数可从上一式直接核对：
$(-1)(ig)^3(1/i)^3=-g^3$，再除去左边的$i$便是$ig^3$。
为说明两图的相对号，先在交换图中作$\ell\mapsto-\ell$。
这个反射保持以原点为中心的积分区域。三个斜线动量各给一个负号；
利用电荷共轭矩阵的
$\mathcal C(\gamma^\mu)^T\mathcal C^{-1}=-\gamma^\mu$、
$\mathcal C\gamma_5^T\mathcal C^{-1}=\gamma_5$，对迹转置并反序，得到

<span id="eq:c75-reflection"></span>

$$
\begin{aligned}
2N^{\nu\mu\rho}(-\ell;q,p)
 &=-\operatorname{tr}(D\gamma^\nu B\gamma^\mu A\gamma^\rho\gamma_5)\\
 &=-\operatorname{tr}(\gamma_5\gamma^\rho A\gamma^\mu B\gamma^\nu D)\\
 &=-\operatorname{tr}(A\gamma^\mu B\gamma^\nu D\gamma_5\gamma^\rho)\\
 &=\operatorname{tr}(A\gamma^\mu B\gamma^\nu D\gamma^\rho\gamma_5)
 =2N^{\mu\nu\rho}(\ell;p,q).
\end{aligned}
\tag{75.16}
$$

反序涉及六个普通伽马矩阵，其转置负号乘积为正；最后一行的负号来自
$\gamma_5$越过$\gamma^\rho$。没有$\gamma_5$时这最后一个负号消失，
两图就相消。含$\gamma_5$时两图相加，并且在固定的任何一条外腿上
收缩都相加。交换操作须先作用于未收缩的图，
随后再用所要检查的$p_\mu$或$q_\nu$收缩。

规范不变性要求

<span id="eq:c75-ward-targets"></span>

$$
p_\mu V^{\mu\nu\rho}=0,\qquad
q_\nu V^{\mu\nu\rho}=0,\qquad
r_\rho V^{\mu\nu\rho}=0 .
\tag{75.17}
$$

它们是把任一外部偏振换成其动量时，纵向规范模式必须退耦的条件。
先检查$r$腿。由$r=-p-q$，
$\slashed r=-D+A$；又由$\slashed k^2=-k^2$，有

<span id="eq:c75-r-cancellation"></span>

$$
D\slashed r A=D(-D+A)A
 =(\ell+q)^2A-(\ell-p)^2D .
\tag{75.18}
$$

把原迹中的$A\gamma^\mu$循环移到末端时，这两个伽马矩阵与$\gamma_5$交换，
因而可将$D\slashed r A$放在一起。代入上式，再分别计算两个四伽马迹：

<span id="eq:c75-r-ward"></span>

$$
\begin{aligned}
r_\rho N^{\mu\nu\rho}
 &=\frac12\operatorname{tr}
       (B\gamma^\nu D\slashed r A\gamma^\mu\gamma_5)\\
 &=\frac12(\ell+q)^2
       \operatorname{tr}(B\gamma^\nu A\gamma^\mu\gamma_5)
   -\frac12(\ell-p)^2
       \operatorname{tr}(B\gamma^\nu D\gamma^\mu\gamma_5)\\
 &=2i\varepsilon^{\alpha\nu\beta\mu}
   [(\ell+q)^2\ell_\alpha p_\beta
     +(\ell-p)^2\ell_\alpha q_\beta],\\
r_\rho V^{\mu\nu\rho}
 &=-4g^3\varepsilon^{\alpha\nu\beta\mu}
   \int\frac{d^4\ell}{(2\pi)^4}
   \left[
   \frac{\ell_\alpha p_\beta}{\ell^2(\ell-p)^2}
   +\frac{\ell_\alpha q_\beta}{\ell^2(\ell+q)^2}
   \right]=0 .
\end{aligned}
\tag{75.19}
$$

这里的$4$已经包含两个定向。两个矢量积分分别正比于$p_\alpha$、
$q_\alpha$，所以每项单独与$\varepsilon$缩并为零。这个结论采用当前圈动量
标记和协变的边界处理；三条外线虽然相同，这种标记却没有显式对称地对待它们。
因此还须检查另外两条腿。

对$p$腿，利用$\slashed p=B-A$消去其两侧的传播分子：

<span id="eq:c75-p-contraction"></span>

$$
\begin{aligned}
A\slashed p B&=A(B-A)B
                 =(\ell-p)^2B-\ell^2A,\\
p_\mu N^{\mu\nu\rho}
 &=\frac12(\ell-p)^2\operatorname{tr}(B\gamma^\nu D\gamma^\rho\gamma_5)
   -\frac12\ell^2\operatorname{tr}(A\gamma^\nu D\gamma^\rho\gamma_5)\\
 &=-2i\varepsilon^{\alpha\nu\beta\rho}
   [(\ell-p)^2\ell_\alpha q_\beta
     -\ell^2(\ell-p)_\alpha(p+q)_\beta],\\
p_\mu V^{\mu\nu\rho}
 &=4g^3\varepsilon^{\alpha\nu\beta\rho}
   \int\frac{d^4\ell}{(2\pi)^4}
   \left[\frac{\ell_\alpha q_\beta}{\ell^2(\ell+q)^2}
   -\frac{(\ell-p)_\alpha(p+q)_\beta}
          {(\ell-p)^2(\ell+q)^2}\right].
\end{aligned}
\tag{75.20}
$$

第二个迹中的$(\ell+q)_\beta$写成
$(\ell-p)_\beta+(p+q)_\beta$；前一项同样因反对称性消去。
最后一行的第一个积分只有外矢量$q$，因而为零。
第二个积分若能把$\ell$换成$\ell+p$，就会只剩$p+q$一个外矢量，
似乎也为零。问题在于它线性发散，平移是否保留积分值正是需要计算的地方。

为了同时固定$q$腿的号，可以在此把它的代数也做完。
这次$\slashed q=D-B$，所以

<span id="eq:c75-q-contraction"></span>

$$
\begin{aligned}
B\slashed q D&=-(\ell+q)^2B+\ell^2D,\\
q_\nu N^{\mu\nu\rho}
 &=2i\varepsilon^{\alpha\mu\beta\rho}
  [(\ell+q)^2\ell_\alpha p_\beta
     -\ell^2(\ell-p)_\alpha(p+q)_\beta],\\
q_\nu V^{\mu\nu\rho}
 &=-4g^3\varepsilon^{\alpha\mu\beta\rho}
   \int\frac{d^4\ell}{(2\pi)^4}
   \left[\frac{\ell_\alpha p_\beta}{\ell^2(\ell-p)^2}
   -\frac{(\ell-p)_\alpha(p+q)_\beta}
          {(\ell-p)^2(\ell+q)^2}\right].
\end{aligned}
\tag{75.21}
$$

第一项仍然消失，第二项与$p$腿需要同一个积分。
这样，三个沃德条件的检验已经归结到一个共同的平移边界问题。

<span id="c75-surface"></span>

## 平移积分变量留下的表面项

先用一维积分说明这种现象。设$f$在有限区间可积，并有有限端点极限
$f(+\infty)=c_+$、$f(-\infty)=c_-$。把发散积分暂时截在同一个区间
$[-R,R]$，再比较有限平移$a$：

<span id="eq:c75-one-dimensional-shift"></span>

$$
\begin{aligned}
I_R(a)-I_R(0)
 &=\int_{-R}^R[f(x+a)-f(x)]\,dx\\
 &=\int_R^{R+a}f(u)\,du
   -\int_{-R}^{-R+a}f(u)\,du,\\
\lim_{R\to\infty}[I_R(a)-I_R(0)]&=a(c_+-c_-).
\end{aligned}
\tag{75.22}
$$

第一步换元$u=x+a$的雅可比因子为1，两个积分相重叠的部分完全消去，
只剩长度为$a$的两端。对负$a$用有向积分，结论不变。
因此，有限移位差只由两个端点极限决定。

现在令$K=p+q$，定义所需的矢量函数

<span id="eq:c75-vector-integral"></span>

$$
f_\alpha(\ell;K)=\frac{\ell_\alpha}{\ell^2(\ell+K)^2},
\qquad
\int\frac{d^4\ell}{(2\pi)^4}f_\alpha(\ell;K)
 =A(K^2)K_\alpha .
\tag{75.23}
$$

$A$包含调节依赖。我们要比较的第二个积分正是$f_\alpha(\ell-p;K)$。
先在非例外欧几里得外动量域定义共同的费曼边界，并取固定中心的大球
$|\ell_E|<R$作紫外截止；最后把所得局域张量解析延拓回闵可夫斯基空间。
对平移后的函数，可先积分位移参数：

<span id="eq:c75-exact-shift-boundary"></span>

$$
\begin{aligned}
\int_{B_R}[f_\alpha(\ell-p)-f_\alpha(\ell)]\,d^4\ell
 &=-p^\beta\int_0^1dt
       \int_{B_R}\partial_\beta f_\alpha(\ell-tp)\,d^4\ell\\
 &=-p^\beta\int_0^1dt
       \int_{\partial B_R}dS_\beta\,f_\alpha(\ell-tp).
\end{aligned}
\tag{75.24}
$$

这是有限区域的恒等式。必要时先在孤立小动量奇点旁作共同光滑处理，
再令该处理消失；四维中这些奇点附近的面积项至多按小球半径的一次或二次幂
趋于零。大球上
$f_\alpha(\ell-tp)=\ell_\alpha/(\ell^2)^2+O(R^{-4})$，
而$dS$按$R^3$增长，所以首项留下常数，下一项是$O(R^{-1})$。
所以大球极限只保留首项，位移参数$t$的积分给1。

写$\ell_E=Rn$，其中$n^2=1$。四维球面元为$dS_\beta=R^3n_\beta d\Omega$。
球面对称性给
$\int n_\alpha n_\beta d\Omega=C\delta_{\alpha\beta}$；
缩并$\alpha=\beta$便有$4C=\Omega_4$。
球面积可从高斯积分算出：
$\pi^2=\int d^4u\,e^{-u^2}
=\Omega_4\int_0^\infty r^3e^{-r^2}dr=\Omega_4/2$，
故$\Omega_4=2\pi^2$。恢复时间积分的威克因子$i$和协变指标以后，

<span id="eq:c75-vector-surface"></span>

$$
\begin{aligned}
\int\frac{d^4\ell}{(2\pi)^4}\,
       \frac{\partial f_\alpha}{\partial\ell^\beta}
 &=\frac{i}{(2\pi)^4}
       \int d\Omega\,n_\alpha n_\beta\\
 &=\frac{i\Omega_4}{4(2\pi)^4}\,g_{\alpha\beta}
   =\frac{i}{32\pi^2}\,g_{\alpha\beta},\\
J_\alpha
 &\equiv\int\frac{d^4\ell}{(2\pi)^4}
       \frac{(\ell-p)_\alpha}{(\ell-p)^2(\ell+q)^2}\\
 &=A(K^2)K_\alpha-\frac{i}{32\pi^2}p_\alpha .
\end{aligned}
\tag{75.25}
$$

第一行的角平均在欧几里得空间计算，时间分量随$\ell^0=i\ell_E^4$一同转换，得到第二行的协变度规$g_{\alpha\beta}$。系数中的$i$来自$d\ell^0$，$1/4$来自角平均，
$(2\pi)^{-4}$来自圈测度。$J_\alpha$的质量量纲为1，有限项也确实与一个
外动量成正比。

将$J_\alpha$代回$p$腿和$q$腿。$AK_\alpha K_\beta$在两处都消失，
剩下的是

<span id="eq:c75-unshifted-anomaly"></span>

$$
\begin{aligned}
p_\mu V^{\mu\nu\rho}(0)
 &=\frac{ig^3}{8\pi^2}
       \varepsilon^{\alpha\nu\beta\rho}p_\alpha q_\beta,\\
q_\nu V^{\mu\nu\rho}(0)
 &=-\frac{ig^3}{8\pi^2}
       \varepsilon^{\alpha\mu\beta\rho}p_\alpha q_\beta
  =-\frac{ig^3}{8\pi^2}
       \varepsilon^{\alpha\rho\beta\mu}q_\alpha p_\beta,\\
r_\rho V^{\mu\nu\rho}(0)&=0 .
\end{aligned}
\tag{75.26}
$$

这里的$(0)$表示当前圈动量标记。以$p$腿为例，
$-4g^3$乘$-ip_\alpha/(32\pi^2)$正好给$ig^3p_\alpha/(8\pi^2)$；
这包含两个定向各自的$1/(16\pi^2)$。
第二行的号由式[（75.21）](#eq:c75-q-contraction)固定。
也可直接交换第一行的$(p,\mu)$和$(q,\nu)$，
再把$\varepsilon$的指标排列成第二行的次序，得到同一个负号。

三个结果尚不对称。既然三条外腿代表同一种规范玻色子，是否能重新安排
圈动量，使它们同时满足沃德恒等式？这需要再算一次有限的移位差。

<span id="c75-routing"></span>

## 圈动量的选择与玻色对称性

把第一图中的圈动量换成$\ell+a$，其中$a$是$p,q$的线性组合。
相应幅为

<span id="eq:c75-shifted-tensor"></span>

$$
\begin{aligned}
V_1^{\mu\nu\rho}(a)
 &=\frac{ig^3}{2}
   \operatorname{tr}
    (\gamma^\alpha\gamma^\mu\gamma^\beta\gamma^\nu
     \gamma^\gamma\gamma^\rho\gamma_5)\,I_{\alpha\beta\gamma}(a),\\
I_{\alpha\beta\gamma}(a)
 &=\int\frac{d^4\ell}{(2\pi)^4}
 \frac{(\ell+a-p)_\alpha(\ell+a)_\beta(\ell+a+q)_\gamma}
 {(\ell+a-p)^2(\ell+a)^2(\ell+a+q)^2}.
\end{aligned}
\tag{75.27}
$$

第三条内线的分子与分母都带$\ell+a+q$。
求移位产生的边界项时，只需其大动量首项
$\ell_\alpha\ell_\beta\ell_\gamma/(\ell^2)^3$。

用刚才的固定大球，位移的一阶边界项为

<span id="eq:c75-cubic-surface"></span>

$$
\begin{aligned}
I_{\alpha\beta\gamma}(a)-I_{\alpha\beta\gamma}(0)
 &=\frac{i\,a^\delta}{(2\pi)^4}
   \int d\Omega\,n_\delta n_\alpha n_\beta n_\gamma\\
 &=\frac{i}{192\pi^2}
   (a_\alpha g_{\beta\gamma}
    +a_\beta g_{\gamma\alpha}
    +a_\gamma g_{\alpha\beta}).
\end{aligned}
\tag{75.28}
$$

四阶角平均只能是三个两两配对的$\delta$之和乘常数$C$。
将两对指标都缩并，左边是$\Omega_4$，右边是
$C(4^2+4+4)=24C$。故$C=\Omega_4/24$，再除以$(2\pi)^4$
就得到$1/(192\pi^2)$。其余位移项仍至少按$R^{-1}$消失。

三个度规缩并各给一个四伽马迹，号可以逐项固定。
先由克利福德关系得到
$\gamma^\lambda\gamma^\mu\gamma_\lambda=2\gamma^\mu$。
三伽马夹持则可写成
$\gamma^\lambda\gamma^\mu\gamma^\beta\gamma^\nu\gamma_\lambda
=-4g^{\beta\nu}\gamma^\mu-2\gamma^\beta\gamma^\nu\gamma^\mu
=2\gamma^\nu\gamma^\beta\gamma^\mu$。
把式[（75.27）](#eq:c75-shifted-tensor)中的六伽马迹记为
$\mathcal T^{\alpha\mu\beta\nu\gamma\rho}$，
则式[（75.28）](#eq:c75-cubic-surface)中的三项依次给

<span id="eq:c75-six-gamma-contractions"></span>

$$
\begin{aligned}
a_\alpha g_{\beta\gamma}
 \mathcal T^{\alpha\mu\beta\nu\gamma\rho}
 &=2a_\alpha\operatorname{tr}
        (\gamma^\alpha\gamma^\mu\gamma^\nu\gamma^\rho\gamma_5)
  =8i\varepsilon^{\mu\nu\rho\delta}a_\delta,\\
a_\beta g_{\gamma\alpha}
 \mathcal T^{\alpha\mu\beta\nu\gamma\rho}
 &=2a_\beta\operatorname{tr}
        (\gamma^\nu\gamma^\beta\gamma^\mu\gamma^\rho\gamma_5)
  =8i\varepsilon^{\mu\nu\rho\delta}a_\delta,\\
a_\gamma g_{\alpha\beta}
 \mathcal T^{\alpha\mu\beta\nu\gamma\rho}
 &=2a_\gamma\operatorname{tr}
        (\gamma^\mu\gamma^\nu\gamma^\gamma\gamma^\rho\gamma_5)
  =8i\varepsilon^{\mu\nu\rho\delta}a_\delta .
\end{aligned}
\tag{75.29}
$$

每个最后的号都由把被缩并指标移到$\varepsilon$末位得到。三项相同，因此

<span id="eq:c75-one-routing-change"></span>

$$
\begin{aligned}
V_1^{\mu\nu\rho}(a)-V_1^{\mu\nu\rho}(0)
 &=\frac{ig^3}{2}\frac{i}{192\pi^2}
       (3)(8i)\varepsilon^{\mu\nu\rho\beta}a_\beta
 \\
 &=-\frac{ig^3}{16\pi^2}\varepsilon^{\mu\nu\rho\beta}a_\beta .
\end{aligned}
\tag{75.30}
$$

两幅图都要改变圈动量。交换图中的位移是$a(q,p)$，不是仍保留$a(p,q)$。
因$\varepsilon^{\nu\mu\rho\beta}=-\varepsilon^{\mu\nu\rho\beta}$，
两图相加只留下$a(p,q)-a(q,p)$。设
$a=up+vq$，这个差等于$(u-v)(p-q)$；对称部分$u+v$不贡献。
因此可以令$a=c(p-q)$，总幅的变化为

<span id="eq:c75-routing-polynomial"></span>

$$
V^{\mu\nu\rho}(c)-V^{\mu\nu\rho}(0)
 =-\frac{ig^3}{8\pi^2}\,
       c\,\varepsilon^{\mu\nu\rho\beta}(p-q)_\beta .
\tag{75.31}
$$

它是外动量的一次多项式，正是线性发散图的局域歧义所允许的量纲。
将它分别与三条外动量收缩，再用$r=-p-q$，得到

<span id="eq:c75-routing-ward"></span>

$$
\begin{aligned}
p_\mu V^{\mu\nu\rho}(c)
 &=-\frac{ig^3}{8\pi^2}(1-c)
       \varepsilon^{\nu\rho\alpha\beta}q_\alpha r_\beta,\\
q_\nu V^{\mu\nu\rho}(c)
 &=-\frac{ig^3}{8\pi^2}(1-c)
       \varepsilon^{\rho\mu\alpha\beta}r_\alpha p_\beta,\\
r_\rho V^{\mu\nu\rho}(c)
 &=-\frac{ig^3}{8\pi^2}(2c)
       \varepsilon^{\mu\nu\alpha\beta}p_\alpha q_\beta .
\end{aligned}
\tag{75.32}
$$

例如$p_\mu\varepsilon^{\mu\nu\rho\beta}p_\beta=0$，
所以$p$腿位移只留下$q_\beta$；将$\mu$移到$\varepsilon$第三位没有负号，
再把$p=-q-r$代入，就给第一行中对原系数的$-c$修正。
对$r$腿，$(p+q)_\rho(p-q)_\beta$的两个交叉项在反对称缩并下相加，
因而出现$2c$。三个系数之和恒为2，这已说明它们不可能同时为零。

取$c=1$可以使前两条沃德恒等式成立，但第三条必然留下反常。
同一种玻色子场的三点顶角，还应是有效作用量对三个$A$的泛函导数，
因而在所有外腿下玻色对称。三个沃德式应具有相同的系数，这要求
$1-c=2c$，即$c=1/3$：

<span id="eq:c75-consistent-anomaly"></span>

$$
\begin{aligned}
p_\mu V_{\text{玻色}}^{\mu\nu\rho}
 &=-\frac{ig^3}{12\pi^2}
      \varepsilon^{\nu\rho\alpha\beta}q_\alpha r_\beta,\\
q_\nu V_{\text{玻色}}^{\mu\nu\rho}
 &=-\frac{ig^3}{12\pi^2}
      \varepsilon^{\rho\mu\alpha\beta}r_\alpha p_\beta,\\
r_\rho V_{\text{玻色}}^{\mu\nu\rho}
 &=-\frac{ig^3}{12\pi^2}
      \varepsilon^{\mu\nu\alpha\beta}p_\alpha q_\beta .
\end{aligned}
\tag{75.33}
$$

交换完整图的外标签只会重新安排圈动量，因此其置换差也是上面的一次局域多项式。
带三个自由指标的奇宇称一次多项式只能是
$\varepsilon^{\mu\nu\rho\sigma}(up+vq)_\sigma$；
它若在三条腿上都横向，分别收缩$p$和$q$就迫使$v=u=0$。
所以三个沃德式的对称性已固定这部分全部的置换歧义。
再考虑是否能加一个局域反项消去剩余反常：
三次$A$、一次导数的候选奇密度与
$\varepsilon^{\mu\nu\rho\sigma}A_\mu A_\nu\partial_\rho A_\sigma$成正比，
但阿贝尔背景场的$A_\mu A_\nu$对称，这个密度恒为零。
因此单个带电外尔场没有相容的局域规范理论。
若改用维数正规化，沃德检验必须保留
式[（75.9）](#eq:c75-split-gamma5)中的额外维项与极点相乘后可能留下的有限贡献。
本节的反常系数由四维边界计算求出；[第77节](/posts/srednicki-77/#c77-measure)将用谱调节计算相应的测度变化。
从物理上说，纵向规范模式不能完全退耦，上一节建立物理态空间时所需的
量子BRST恒等式便受到破坏。两点函数正常并不足以避免这个困难。

<span id="c75-groups"></span>

## 表示和电荷怎样抵消反常

如果理论含多个左手外尔场$\psi_i$，其U(1)电荷是$Q_i$，
只须在每个规范顶角乘$Q_i$。三角有三个顶角，且闭圈内的味指标保持不变，
所以不同场的反常直接相加：

<span id="eq:c75-charge-cancellation"></span>

$$
D_\mu\psi_i=(\partial_\mu-igQ_iA_\mu)\psi_i,\qquad
\mathcal A_{U(1)^3}=\sum_iQ_i^3,\qquad
\mathcal A_{U(1)^3}=0 .
\tag{75.34}
$$

最后一式是消去本节局域规范反常的条件。电荷$Q$和$-Q$构成的共轭对
自动满足$Q^3+(-Q)^3=0$，这重新得到狄拉克理论的结果。
抵消却不要求每个场都有这样的伙伴。例如，取一个电荷$+2$的场和
八个电荷$-1$的场，

<span id="eq:c75-chiral-charge-example"></span>

$$
2^3+8(-1)^3=0,\qquad 2+8(-1)=-6 .
\tag{75.35}
$$

它的纯U(1)规范反常消失，场谱仍然是手征的。
第二个等式留到下面讨论引力耦合时使用，因为引力还会提出另一个条件。

非阿贝尔理论的圈动量和旋量计算保持原样，但两定向的群矩阵次序不同，
分别带$\operatorname{Tr}_R(T^aT^bT^c)$和
$\operatorname{Tr}_R(T^aT^cT^b)$。前面的反射计算表明，偶宇称分子的两图
相反，奇宇称分子的两图相同。因此群因子分别组合为

<span id="eq:c75-even-odd-group-traces"></span>

$$
\begin{aligned}
\frac12\operatorname{Tr}_R([T^a,T^b]T^c)
 &=\frac{i}{2}f^{abd}\operatorname{Tr}_R(T^dT^c)
  =\frac{i}{2}T(R)f^{abc},\\
B_R^{abc}
 &\equiv\frac12\operatorname{Tr}_R(\{T^a,T^b\}T^c).
\end{aligned}
\tag{75.36}
$$

第一行的循环次序等价于两图迹之差。它与树级三胶子顶角具有相同的反对称
群结构，参与通常的顶角重整化。迹已把内部表示指标完全缩并，
最后只剩标量群系数$iT(R)f^{abc}/2$。
第二行则是第70节的三次完全对称迹。
对于第70节所用的$SU(N\ge3)$归一，

<span id="eq:c75-anomaly-coefficient"></span>

$$
B_R^{abc}=A(R)d^{abc},\qquad
d^{abc}=B_{\mathbf N}^{abc},\qquad A(\mathbf N)=1 .
\tag{75.37}
$$

这里的$d$由含$1/2$的迹定义；基本表示反对易子中$T^c$的系数则为$4d^{abc}$，见[第70节](/posts/srednicki-70/#c70-cubic)。
一般群或直积群应直接保留$B_R^{abc}$；一个$A(R)$乘固定$d$
的写法只适用于相应不变三次张量空间是一维的情况。

两定向的奇群因子之和为$2B_R$，而U(1)单位电荷的两个定向也给因子2，
所以在式[（75.33）](#eq:c75-consistent-anomaly)中用$\sum_iB_{R_i}^{abc}$
替换单位电荷因子即可。于是必要的局域抵消条件为

<span id="eq:c75-nonabelian-cancellation"></span>

$$
\begin{gathered}
\sum_i B_{R_i}^{abc}=0
\quad\text{对所有 }a,b,c;
\\
\sum_iA(R_i)=0
\quad\text{在固定非零 }d\text{ 的情形}.
\end{gathered}
\tag{75.38}
$$

非阿贝尔完整顶角的纵向恒等式还含低点函数和鬼项；
这里追踪的是带$\varepsilon$的奇宇称破缺，它不能由通常的偶宇称反项抵消。
共轭表示的生成元是$T_{\bar R}^a=-(T_R^a)^T$。
将三个负号和矩阵转置带入完全对称迹，得到

<span id="eq:c75-conjugate-cancellation"></span>

$$
B_{\bar R}^{abc}=-B_R^{abc},\qquad
A(\bar R)=-A(R),\qquad
R\simeq\bar R\ \Longrightarrow\ B_R^{abc}=0 .
\tag{75.39}
$$

最后一步用了迹在相似变换下不变。因此实表示和伪实表示的局域三角反常都为零；
它们在整体规范变换下的行为则还要另看。SU(2)的不可约表示均与其共轭等价，
故所有这些表示的三次对称迹都消失。SU(N)基本表示在$N\ge3$时
则采用式[（75.37）](#eq:c75-anomaly-coefficient)的归一，其三次迹非零。

对于SO(N)，仍须逐个表示检查三次迹。SO(6)就有带局域反常的表示。
为区分SO(6)及其自旋覆盖群，先说明这两个群的关系。SU(4)作用在$\Lambda^2\mathbf4$上，
并保持反线性映射
$(Jw)_{ij}=\epsilon_{ijkl}w_{kl}^*/2$。
它满足$J^2=1$，固定子空间是一个带正定诱导内积的六维实空间。
所以SU(4)在此给出SO(6)变换。该映射的核由
$\lambda_i\lambda_j=1$（所有$i<j$）确定，其中$\lambda_i$是SU(4)元素的
特征值；这迫使所有$\lambda_i$同为$+1$或同为$-1$。
两群李代数的维数都是15，非平凡作用在简单李代数上忠实，因而

<span id="eq:c75-so6-cover"></span>

$$
SO(6)\simeq SU(4)/\{\mathbf1,-\mathbf1\}.
\tag{75.40}
$$

SU(4)的对称二阶表示$\operatorname{Sym}^2\mathbf4=\mathbf{10}$
使$-\mathbf1$作用为正，故确实下降为SO(6)表示。
取嘉当生成元$H=\operatorname{diag}(1,1,1,-3)$，对称二阶张量的权重是
$h_i+h_j$、$i\le j$：六个为2，三个为$-2$，一个为$-6$。因此

<span id="eq:c75-so6-counterexample"></span>

$$
\operatorname{Tr}_{\mathbf4}H^3=3-27=-24,\qquad
\operatorname{Tr}_{\mathbf{10}}H^3
 =6(2)^3+3(-2)^3+(-6)^3=-192 .
\tag{75.41}
$$

非零三次迹已经证明这个SO(6)表示有局域规范反常；
在SU(4)的归一下还有$A(\mathbf{10})=8$。
实际构造理论时，用式[（75.38）](#eq:c75-nonabelian-cancellation)逐项检查表示，
就能把这类群论例外包括进去。

<span id="c75-global"></span>

## 混合引力反常与整体规范反常

若把理论放在引力背景中，同一个费米圈可以接两个引力顶角和一个规范顶角。
两个引力顶角不作用于内部表示指标，因而圈上的内部群迹只剩
$\operatorname{Tr}_R T^a$。对半单李代数，每个生成元可写成交换子的线性组合，
交换子的迹为零，所以这种混合反常的群系数消失。
U(1)生成元却是$Q\mathbf1$，必须另要求

<span id="eq:c75-gravity-condition"></span>

$$
\mathcal A_{U(1)\text{--gravity}^2}
 \ \propto\ \sum_i d(R_i)Q_i=0 .
\tag{75.42}
$$

这里$d(R_i)$是该外尔场在其他内部表示中的维数；若所有场都是内部单态，
条件就简化为$\sum_iQ_i=0$。
式[（75.35）](#eq:c75-chiral-charge-example)因此只消去了纯规范立方反常，
其一次和$-6$仍会在耦合引力时造成障碍。
局部反项可以改变混合破缺落在哪一条沃德恒等式上；物理要求是规范变换与
背景坐标变换都能一致实现。本节只需其表示系数，不展开含能动张量的完整三角核。

还有一种障碍在微扰三角图中看不到。即使所有局域三次迹为零，
费米积分在一个不能连续缩回恒等变换的规范变换下仍可能改变符号。
这称为整体规范反常。对普通四维自旋时空上的SU(2)，
非平凡整体变换的费米相位由
$\sum_i2T(j_i)$的奇偶性决定，$T(\mathbf2)=1/2$；
这一拓扑结果见Wang、Wen和Witten的[第2.2—2.3节，尤其式（2.9）](https://arxiv.org/pdf/1810.00844v4#page=10)。相应条件为

<span id="eq:c75-su2-global-condition"></span>

$$
\sum_i2T(j_i)=0\pmod2,\qquad
2T(j)=\frac23j(j+1)(2j+1).
\tag{75.43}
$$

群指标的数值可由$T(j)=\operatorname{Tr}_j(T^3)^2
=\sum_{m=-j}^jm^2=j(j+1)(2j+1)/3$直接算出；
费米积分相位与这个奇偶性的联系则由上引拓扑结果给出。
基本双重态给$2T=1$，故双重态的个数必须为偶数。
但$j=3/2$给$2T=10$，虽然也是伪实表示，却不贡献这种普通SU(2)反常。
所以每个多重态的贡献按$2T(j)$的奇偶性计数。
更一般的整体条件取决于规范群的全局形式及所允许的背景。

本节已经求出一圈三角的局域反常和表示抵消条件。
将这一条件推广到更多外腿和更高圈，还需要一致性关系与全阶消除定理。
[第77节的一致性计算](/posts/srednicki-77/#c77-consistent)从二次项确定更多背景场的局域结构，
[全阶消除定理](/posts/srednicki-77/#c77-comparison)在明确的可重整、微扰可幺正条件下
保证存在保持规范沃德恒等式的减除方案。它不排除刚才单列的整体障碍，
直积群还会出现混合三角，下面逐一求出这些条件。

<span id="c75-product-group"></span>

## 直积群的反常抵消

考虑一个同时具有非阿贝尔与U(1)规范对称性的理论，每个左手外尔场都带有两类量子数：非阿贝尔表示$R_i$和阿贝尔电荷$Q_i$。因而三角图的外线既可以全属于同一个规范群，也可以来自不同的规范群。求无反常条件的关键，就是把这些可能的外线组合都列入同一个群迹，再对所有独立的左手场求和。

记非阿贝尔规范势为$A_\mu^a$，阿贝尔规范势为$B_\mu$，相应耦合为$g$和$g_1$。取协变导数
<span id="eq:c75-ex-covariant-derivative"></span>

$$
D_\mu\psi_i=
 \left(\partial_\mu-igA_\mu^aT_i^a
                     -ig_1B_\mu Q_i\mathbf1_i\right)\psi_i,
\qquad d_i=\dim R_i .
\tag{75.44}
$$

$T_i^a$是$R_i$空间中的厄米生成元，$\mathbf1_i$是该空间的单位矩阵。指标$i$计数独立的左手外尔多重态；若同一表示有若干份，每一份都须计入。同一个手征圈已包含该场的粒子和反粒子。

<span id="c75-product-triangles"></span>

### 四种三角图的群迹

以$A,B,C$表示包括两类规范方向在内的指标，并定义
<span id="eq:c75-ex-combined-generators"></span>

$$
t_i^a=T_i^a,\qquad t_i^0=Q_i\mathbf1_i .
\tag{75.45}
$$

这里的$0$是阿贝尔群指标，不是时空指标。由式[（75.36）](#eq:c75-even-odd-group-traces)的两定向迹相加，同一左手三角图的反常部分乘以下列群因子：
<span id="eq:c75-ex-symmetric-trace"></span>

$$
\begin{aligned}
\mathcal A^{ABC}
 &=\frac12\sum_i\operatorname{Tr}_{R_i}
               \bigl(\{t_i^A,t_i^B\}t_i^C\bigr)\\
 &=\frac12\sum_i\left[
       \operatorname{Tr}_{R_i}(t_i^At_i^Bt_i^C)
      +\operatorname{Tr}_{R_i}(t_i^Bt_i^At_i^C)\right].
\end{aligned}
\tag{75.46}
$$

迹的循环性使这个张量对三个指标完全对称。两个有向圈的群因子相加，给出反对易子；定义中的$1/2$使单分量单位电荷的群因子为$\tfrac12\{1,1\}\,1=1$。所有场都是左手场，所以它们乘同一个手征运动学核，表示系数直接相加。三个顶角的耦合常数则按外线种类给出$g^3$、$g^2g_1$、$gg_1^2$或$g_1^3$。消去局域微扰规范反常，要求各个独立的$\mathcal A^{ABC}$为零。

先取三条非阿贝尔外线。直接得到
<span id="eq:c75-ex-nonabelian-cubic"></span>

$$
\mathcal A^{abc}
 =\frac12\sum_i\operatorname{Tr}_{R_i}
                   \bigl(\{T_i^a,T_i^b\}T_i^c\bigr)=0 .
\tag{75.47}
$$

这就是纯非阿贝尔反常的条件。若对所考察的简单群可以沿第70节写成共同的三阶不变量$d^{abc}$，每个表示的群迹为$A(R_i)d^{abc}$，那么它简化为$\sum_iA(R_i)=0$。原始的张量条件更一般：如果某个群没有这种非零的三阶对称迹，它自动满足这一条件；如果非阿贝尔部分含多个简单因子，就须分别使用相应的生成元。

再取两条非阿贝尔外线和一条阿贝尔外线。阿贝尔生成元与所有$T_i^a$对易，故
<span id="eq:c75-ex-mixed-two-nonabelian"></span>

$$
\begin{aligned}
\mathcal A^{ab0}
 &=\frac12\sum_iQ_i\operatorname{Tr}_{R_i}
                    (T_i^aT_i^b+T_i^bT_i^a)\\
 &=\sum_iQ_i\operatorname{Tr}_{R_i}(T_i^aT_i^b).
\end{aligned}
\tag{75.48}
$$

两个迹相等，因而恰好消去$1/2$。对一个简单因子，在第70节所固定的生成元归一中，$\operatorname{Tr}_{R_i}(T_i^aT_i^b)=T(R_i)\delta^{ab}$，于是这个混合反常要求
<span id="eq:c75-ex-mixed-index-condition"></span>

$$
\sum_iQ_iT(R_i)=0 .
\tag{75.49}
$$

二次迹系数$T(R_i)$决定这一混合反常。即使某个非阿贝尔表示为实表示，令纯非阿贝尔反常为零，带电的这个多重态仍可能对式[（75.49）](#eq:c75-ex-mixed-index-condition)有贡献。

第三种组合是一条非阿贝尔外线和两条阿贝尔外线。此时
<span id="eq:c75-ex-mixed-one-nonabelian"></span>

$$
\begin{aligned}
\mathcal A^{a00}
 &=\frac12\sum_i\operatorname{Tr}_{R_i}
          \bigl(\{T_i^a,Q_i\mathbf1_i\}Q_i\mathbf1_i\bigr)\\
 &=\sum_iQ_i^2\operatorname{Tr}_{R_i}T_i^a .
\end{aligned}
\tag{75.50}
$$

对半单的非阿贝尔部分，这个表达式逐个多重态为零。理由是矩阵对易子的迹为零，而每个非阿贝尔简单因子都由其对易子张成：对易子张成的子空间由雅可比恒等式构成一个非零理想，简单代数中这样的理想就是全代数。因此，每个生成元的迹都为零，半单代数作为这些因子的直和也具有同样的性质。这解释了为什么通常列反常抵消条件时没有再列一个独立的$GU(1)^2$条件。若规范群的李代数还带有阿贝尔中心，则中心方向须保留式[（75.50）](#eq:c75-ex-mixed-one-nonabelian)。

最后取三条阿贝尔外线。单位矩阵的迹给出表示维数，因此
<span id="eq:c75-ex-abelian-cubic"></span>

$$
\mathcal A^{000}
 =\frac12\sum_i\operatorname{Tr}_{R_i}
                (2Q_i^3\mathbf1_i)
 =\sum_i d_iQ_i^3=0 .
\tag{75.51}
$$

维数$d_i$来自内部简并度：一个$d_i$维非阿贝尔多重态含有$d_i$个电荷同为$Q_i$的外尔分量，每个分量都能在阿贝尔三角圈中传播。

于是，不预先假定生成元是否无迹时，四类群方向给出的条件完整写成
<span id="eq:c75-ex-local-conditions"></span>

$$
\begin{gathered}
\frac12\sum_i\operatorname{Tr}_{R_i}
                     \bigl(\{T_i^a,T_i^b\}T_i^c\bigr)=0,\\
\sum_iQ_i\operatorname{Tr}_{R_i}(T_i^aT_i^b)=0,\qquad
\sum_iQ_i^2\operatorname{Tr}_{R_i}T_i^a=0,\\
\sum_i d_iQ_i^3=0 .
\end{gathered}
\tag{75.52}
$$

对于简单的非阿贝尔群，第二个条件就是式[（75.49）](#eq:c75-ex-mixed-index-condition)，第三个条件自动成立。当$G$本身是多个简单群的乘积时，迹必须在整个多重态空间中取。例如$R_i=r_i\otimes s_i$，而$T^a$只作用于第一个因子，则
<span id="eq:c75-ex-spectator-multiplicity"></span>

$$
\begin{aligned}
\operatorname{Tr}_{r_i\otimes s_i}
       [(T_{r_i}^a\otimes\mathbf1)
        (T_{r_i}^b\otimes\mathbf1)]
 &=\dim(s_i)T(r_i)\delta^{ab},\\
\dim R_i&=\dim(r_i)\dim(s_i).
\end{aligned}
\tag{75.53}
$$

因此，检查第一个群的混合反常时，另一个表示的维数成为它的重数。若两条非阿贝尔外线分别属于不同的简单因子，群迹分解成两个生成元迹的乘积，也就为零。

一个狄拉克场给出直接的检验。把它改写成两个左手场后，它们的表示与电荷分别为$(R,Q)$和$(\overline R,-Q)$。由于
<span id="eq:c75-ex-conjugate-representation"></span>

$$
T_{\overline R}^a=-(T_R^a)^{\mathsf T},\qquad
T(\overline R)=T(R),\qquad
\dim\overline R=\dim R,
\tag{75.54}
$$

共轭表示的三次对称迹带一个负号，二次迹则保持不变。于是纯非阿贝尔条件由两个相反的三次迹抵消，混合条件由$QT(R)-QT(R)$抵消，纯阿贝尔条件由$dQ^3+d(-Q)^3$抵消。这与非手征狄拉克理论的规范反常相消一致。

<span id="c75-product-gravity-global"></span>

### 引力背景和整体条件

与背景引力相容还要满足式[（75.42）](#eq:c75-gravity-condition)的$\sum_i d_iQ_i=0$。狄拉克共轭对的两项为$dQ+d(-Q)=0$，而电荷$+2$与八个$-1$的例子仍给$-6$。这一条件与纯规范三次迹的条件分别检查。

对允许的大规范变换，独立左手场的费米积分相乘，总相位也相乘。若$G$中有一个$SU(2)$因子，且四维时空带有通常的自旋结构，式[（75.43）](#eq:c75-su2-global-condition)给单个同位旋$j_i$多重态的相位$(-1)^{2T(j_i)}$。设该场在其他群因子中的表示维数乘积为$n_i$，就有$n_i$份相同的$SU(2)$表示，因而

<span id="eq:c75-ex-global-multiplicity"></span>

$$
\prod_i(-1)^{n_i\,2T(j_i)}=1
\quad\Longleftrightarrow\quad
\sum_i n_i\,2T(j_i)=0\pmod2 .
\tag{75.55}
$$

例如，另带三维内部表示的一个$SU(2)$基本双重态给$3\times 2T(1/2)=3$，与三个双重态一样贡献奇数。所有这些重数都来自对整个内部表示空间取迹，与式[（75.53）](#eq:c75-ex-spectator-multiplicity)的计数相同。

<span id="c75-source-reference"></span>

---

[← 第 74 节](/posts/srednicki-74/) · [章节地图](/srednicki/) · [第 76 节 →](/posts/srednicki-76/)
