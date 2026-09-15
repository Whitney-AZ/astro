---
title: 'Srednicki §21 量子作用量'
date: 2026-09-14
category: 笔记
tags: [物理, 量子场论, Srednicki]
series: 'Srednicki QFT'
srednickiSections: [21]
hideFromHome: true
draft: false
---

<span id="c21"></span>

第19节已经说明，把完整传播子和各个1PI顶角合成树图，就能得到原理论的完整连通振幅。这使我们想到，可以把这些核作为系数，组成一个新的作用量，使它的树级费曼规则直接产生上述结果。这个泛函称为量子作用量（quantum action）；原理论的圈修正已经收入它的系数，因此由它求出的运动方程也会包含量子效应。下面先从完整核写出这个泛函，再通过树图计数和驻相计算，求出它与连通生成泛函$W[J]$的关系。这样便能进一步确定量子运动方程中的场究竟代表什么。

<span id="c21-kernels"></span>

## 从完整核写出作用量

仍以六维立方理论为例，不过本节的泛函运算与具体维数无关，因而把测度统一写成$d$维。先固定傅里叶变换及其逆变换：
<span id="eq:c21-fourier"></span>

$$
\widetilde\varphi(k)=\int d^dx\,e^{-ikx}\varphi(x),
\qquad
\varphi(x)=\int\frac{d^dk}{(2\pi)^d}\,
 e^{ikx}\widetilde\varphi(k).
\tag{21.1}
$$

为使新的作用量产生所需的图规则，把[第19节已经构造的完整核](/posts/srednicki-19/#c19-effective-action)按场的幂次排在一起，定义
<span id="eq:c21-quantum-action-kernels"></span>

$$
\begin{aligned}
\Gamma[\varphi]
={}&-\frac12\int\frac{d^dk}{(2\pi)^d}\,
 \widetilde\varphi(-k)
 [k^2+m^2-\Pi(k^2)]\widetilde\varphi(k)\\
&+\sum_{n\ge3}\frac1{n!}
 \int\prod_{a=1}^n\frac{d^dk_a}{(2\pi)^d}\,
 (2\pi)^d\delta^d\!\left(\sum_a k_a\right)\\
&\hspace{27mm}\times V_n(k_1,\ldots,k_n)
 \prod_{a=1}^n\widetilde\varphi(k_a).
\end{aligned}
\tag{21.2}
$$

这里已经用既定的真空条件去掉常数项和一次项；逆核的边界仍沿用费曼处方，暂不显写$i0$。二次项决定传播子，其符号必须与所需的完整图线相容：若高斯作用量写成$\frac12\varphi K\varphi$，[第6节的高斯积分](/posts/srednicki-06/#c06-gaussian)给出的收缩为$iK^{-1}$。令它等于完整图线$\boldsymbol\Delta/i$，便要求$K=-\boldsymbol\Delta^{-1}$。

式[（21.2）](#eq:c21-quantum-action-kernels)据此使用负二次核，动量测度与式[（21.1）](#eq:c21-fourier)对应。高点项取正号，以产生此前定义的$iV_n$顶角。

高点系数中的$1/n!$会被场因子的排列数消去，留下图规则所需的$iV_n$。要把这一步写清楚，先约定动量泛函导数的测度：
<span id="eq:c21-functional-measure"></span>

$$
\begin{aligned}
\delta F&=\int\frac{d^dp}{(2\pi)^d}\,
 \frac{\delta F}{\delta\widetilde\varphi(p)}
 \delta\widetilde\varphi(p),\\
\frac{\delta\widetilde\varphi(k)}
 {\delta\widetilde\varphi(p)}
&=(2\pi)^d\delta^d(k-p).
\end{aligned}
\tag{21.3}
$$

将$n$次微分分别分配给$n$个场因子，共有$n!$种方式。同种标量的$V_n$对外腿置换对称，所以这些项全都相等，正好消去作用量中的阶乘。每次微分产生的delta函数又消去一个动量积分，最后只剩总动量守恒的delta函数：
<span id="eq:c21-vertex-derivatives"></span>

$$
\left.
\frac{\delta^n\Gamma}
 {\delta\widetilde\varphi(p_1)\cdots
  \delta\widetilde\varphi(p_n)}
\right|_{\varphi=0}
=(2\pi)^d\delta^d\!\left(\sum_a p_a\right)
 V_n(p_1,\ldots,p_n),\qquad n\ge3.
\tag{21.4}
$$

在$e^{i\Gamma}$的展开中，这个系数再乘上$i$，便成为完整顶角。于是$\Gamma$的二次项和高点项分别给出所需的完整传播子与完整顶角，它的树图规则也就与前面的全核装配一致。由于$V_n$本身已经含有原理论各阶的圈修正，这里的树图仍然包含原理论的量子效应。

<span id="c21-loop-counting"></span>

## 用一个辅助参数挑出树图

为了把这个图的关系写成泛函关系，先回到原理论的源积分。用$\chi$记路径积分变量，把源与场的配对简记为$\langle J,\chi\rangle=\int d^dx\,J(x)\chi(x)$，则
<span id="eq:c21-original-generator"></span>

$$
Z[J]=\int\mathcal D\chi\,
 e^{iS[\chi]+i\langle J,\chi\rangle}
=e^{iW[J]},\qquad W[J]=-i\log Z[J].
\tag{21.5}
$$

测度中包含零源归一常数，因此$Z[0]=1$、$W[0]=0$。第9节的连通指数关系告诉我们，$W$生成连通源图。现在将积分中的原作用量换成刚定义的量子作用量，另构造一个辅助积分：
<span id="eq:c21-auxiliary-generator"></span>

$$
Z_\Gamma[J]
=\int\mathcal D\chi\,
 e^{i\Gamma[\chi]+i\langle J,\chi\rangle}
=e^{iW_\Gamma[J]}.
\tag{21.6}
$$

这个辅助积分的连通图以完整核作为顶角和内线。[第19节的桥树分解](/posts/srednicki-19/#c19-trees)表明，只取其中的树图，就已经得到原理论的全部连通图；再在完整核之间添加圈，会把已有的量子修正再次计入。因此，要恢复原生成泛函，我们需要从$W_\Gamma$中选出树部分。

选择树图可以通过计数圈数来完成。将指数中的$\Gamma+\langle J,\chi\rangle$除以一个无量纲参数$\hbar$，定义
<span id="eq:c21-hbar-generator"></span>

$$
\begin{aligned}
Z_{\Gamma,\hbar}[J]
&=\mathcal N_\hbar
 \int\mathcal D\chi\,
 \exp\!\left[\frac{i}{\hbar}
       \bigl(\Gamma[\chi]+\langle J,\chi\rangle\bigr)\right],\\
Z_{\Gamma,\hbar}[J]&=e^{iW_{\Gamma,\hbar}[J]}.
\end{aligned}
\tag{21.7}
$$

其中$\mathcal N_\hbar$仍使零源值归一为1。改变$\hbar$时，各个完整核保持固定，所以这个参数只记录完整核之间新组成的辅助图有多少圈。它的幂次可以从每条线和每个顶点直接读出：二次核变成$K/\hbar$，其逆多出$\hbar$，因而每条传播线贡献一个$\hbar$；每个相互作用顶角和每个源顶点则各贡献$\hbar^{-1}$。对一幅连通图，记全部传播线数为$P$、相互作用顶点数为$V$、一价源顶点数为$E$，总因子就是
<span id="eq:c21-hbar-weight"></span>

$$
\hbar^{P-V-E}.
\tag{21.8}
$$

现在把这个幂次改写为圈数。连同源端点，图中共有$V+E$个顶点，连接它们的一棵生成树含有$V+E-1$条边。其余每条边都在树上增加一个独立圈，因此
<span id="eq:c21-euler-with-sources"></span>

$$
L=P-(V+E)+1,\qquad P-V-E=L-1.
\tag{21.9}
$$

同一关系也可以通过计数独立内动量得到。对含有相互作用顶点的连通图，扣去$E$条外线后还有$P-E$条内线；$V$个顶角的守恒条件中，有一个只给出整体动量守恒，所以真正约束内动量的条件少一个，留下的独立内动量数便是$(P-E)-(V-1)$。这就与图的圈数相等。最简单的双源图需要单独说明：两个源直接由一条自由线连接时，$P=1,E=2,V=0$，因而不能把$P-E$当作内线数；上面的生成树计数没有这个限制，式[（21.9）](#eq:c21-euler-with-sources)仍给出$L=0$。

按圈数归并所有连通图，得到
<span id="eq:c21-hbar-expansion"></span>

$$
W_{\Gamma,\hbar}
=\hbar^{-1}W_{\Gamma,0}
 +W_{\Gamma,1}
 +\hbar W_{\Gamma,2}+\cdots.
\tag{21.10}
$$

树图正是这个展开的最低幂系数，因此原理论的连通生成泛函为
<span id="eq:c21-tree-coefficient"></span>

$$
W[J]=W_{\Gamma,0}[J]
=\bigl[\hbar W_{\Gamma,\hbar}[J]\bigr]_{\hbar^0}.
\tag{21.11}
$$

方括号表示取$\hbar$的常数系数。式[（21.7）](#eq:c21-hbar-generator)将辅助积分的指数定义为$iW_{\Gamma,\hbar}$，其中没有另提出$1/\hbar$，所以选择树项时要先乘上$\hbar$。在形式微扰中，式[（21.11）](#eq:c21-tree-coefficient)可以直接按阶数实施：先依圈数整理各项，再取所需系数即可。

<span id="c21-stationary-phase"></span>

## 驻相计算与量子运动方程

图的计数已经告诉我们应取哪一项；要把它算成泛函的表达式，可用驻相法求出同一个$\hbar^{-1}$系数。把指数中的泛函记为
<span id="eq:c21-stationary-functional"></span>

$$
F_J[\chi]=\Gamma[\chi]+\langle J,\chi\rangle.
\tag{21.12}
$$

在选定真空附近，取满足原来边界条件的驻相场$\varphi_J$。它使上式的一次变分为零，因而满足
<span id="eq:c21-quantum-field-equation"></span>

$$
\left.\frac{\delta\Gamma}{\delta\chi(x)}
 \right|_{\chi=\varphi_J}
=-J(x)
\tag{21.13}
$$

这就是量子运动方程。对每个给定的源，先由这个方程确定驻点，再考察它附近的涨落。

为写清驻相前因子，先用有限模式调节把路径积分化成普通多变量积分，并选择二次涨落核可逆的驻点分支。设模式数为$N$，作变元替换$\chi=\varphi_J+\sqrt\hbar\,\eta$。这个缩放使二次涨落项不再带辅助参数；由于驻点处的一次变分为零，指数依次展开为
<span id="eq:c21-stationary-expansion"></span>

$$
\begin{aligned}
\frac{i}{\hbar}F_J[\chi]
={}&\frac{i}{\hbar}F_J[\varphi_J]
 +\frac i2\,\eta_a H_{J,ab}\eta_b\\
&+\frac{i\sqrt\hbar}{3!}
 \Gamma^{(3)}_{J,abc}\eta_a\eta_b\eta_c
 +O(\hbar),\\
H_{J,ab}&=\Gamma^{(2)}_{ab}[\varphi_J].
\end{aligned}
\tag{21.14}
$$

重复指标在有限模式下表示求和，去掉调节后还包含位置积分。变元替换给出的Jacobian是$\hbar^{N/2}$，二次高斯积分则产生$\det(-iH_J)^{-1/2}$，其相位沿原费曼轮廓连续确定。接着展开三次及更高次的涨落项：三次项的一次贡献为奇高斯矩，积分消失；三次项的平方和四次项都从相对$O(\hbar)$开始。最后除以零源积分，公共的$\hbar^{N/2}$与源无关常数相消，留下
<span id="eq:c21-stationary-determinant"></span>

$$
\begin{aligned}
Z_{\Gamma,\hbar}[J]
={}&\exp\!\left\{\frac{i}{\hbar}
 [F_J[\varphi_J]-F_0[\varphi_0]]\right\}\\
&\times
 \left[\frac{\det(-iH_J)}{\det(-iH_0)}\right]^{-1/2}
 [1+O(\hbar)].
\end{aligned}
\tag{21.15}
$$

取$\log Z$以后，行列式前因子从$\hbar^0$阶开始出现，而我们所需的是$\hbar^{-1}$项，因而只须保留指数中的驻点值。再用既定真空归一条件$\varphi_0=0$、$\Gamma[0]=0$，将式[（21.11）](#eq:c21-tree-coefficient)与式[（21.15）](#eq:c21-stationary-determinant)中的系数相比，便得到
<span id="eq:c21-forward-legendre"></span>

$$
W[J]=\Gamma[\varphi_J]+\int d^dx\,J(x)\varphi_J(x).
\tag{21.16}
$$

因此，指定真空及轮廓附近的形式涨落展开中，树系数由量子作用量和源项在驻点上的值共同给出。

<span id="c21-mean-field"></span>

## 驻相场就是源产生的平均场

现在来确定驻相场的物理意义。对原生成泛函求一次源导数，会插入$\chi(x)$并带来一个$i$。再与$W=-i\log Z$中的系数相乘，就得到归一化的一点函数：
<span id="eq:c21-mean-path-integral"></span>

$$
\frac{\delta W[J]}{\delta J(x)}
=\frac{\int\mathcal D\chi\,\chi(x)
 e^{iS[\chi]+i\langle J,\chi\rangle}}
 {\int\mathcal D\chi\,
 e^{iS[\chi]+i\langle J,\chi\rangle}}.
\tag{21.17}
$$

将这个路径积分写成算符语言，它就是归一化的真空到真空（in-out）插入：
<span id="eq:c21-in-out-mean"></span>

$$
\frac{\delta W[J]}{\delta J(x)}
=
\frac{\langle0|\mathrm T\{
 \widehat\varphi(x)e^{i\int J\widehat\varphi}\}|0\rangle}
 {\langle0|\mathrm T e^{i\int J\widehat\varphi}|0\rangle}.
\tag{21.18}
$$

零源时，上式回到原真空的一点函数；保留有限源时，则给出该源产生的数值平均场。由于这里计算的是真空到真空插入，这个平均场一般可以是复数。

同一个源导数还可以从式[（21.16）](#eq:c21-forward-legendre)求出。这里$\Gamma$通过驻相场$\varphi_J$间接依赖$J$，而$\int J\varphi_J$同时具有显式的源依赖和通过场产生的间接依赖。对这三处依次求导，得到
<span id="eq:c21-chain-rule-cancellation"></span>

$$
\begin{aligned}
\frac{\delta W}{\delta J(x)}
={}&\int d^dy\,
 \frac{\delta\Gamma}{\delta\varphi_J(y)}
 \frac{\delta\varphi_J(y)}{\delta J(x)}
 +\varphi_J(x)\\
&+\int d^dy\,J(y)
 \frac{\delta\varphi_J(y)}{\delta J(x)}\\
={}&\varphi_J(x)
 +\int d^dy\,
 \left[\frac{\delta\Gamma}{\delta\varphi_J(y)}+J(y)\right]
 \frac{\delta\varphi_J(y)}{\delta J(x)}\\
={}&\varphi_J(x).
\end{aligned}
\tag{21.19}
$$

最后一行中，两个积分项的公共系数由驻点方程变为零。这一相消表明，驻相场正是式[（21.17）](#eq:c21-mean-path-integral)中由原理论求得的平均场。这也给出了量子运动方程的含义：$\Gamma$的变分方程描述的是包含量子涨落效应的平均场。

若在选定的可逆分支上反解$\varphi=\delta W/\delta J$，便可把源看成场的泛函，记为$J_\varphi$。将它代入式[（21.16）](#eq:c21-forward-legendre)，就把源与场的角色对换，写成Legendre变换：
<span id="eq:c21-inverse-legendre"></span>

$$
\Gamma[\varphi]
=W[J_\varphi]-\int d^dx\,J_\varphi(x)\varphi(x),
\qquad
\frac{\delta\Gamma}{\delta\varphi(x)}=-J_\varphi(x).
\tag{21.20}
$$

局部逆可以逐阶求出。把位置和分量并入一个指标，在参考源 $J_*$ 附近记 $\xi=J-J_*$、$\eta=\varphi-\varphi_*$，源映射的展开为

<span id="eq:c21-local-source-series"></span>

$$
\eta_a=\mathcal G_{*,ab}\xi_b
+\frac12W^{(3)}_{*,abc}\xi_b\xi_c+O(\xi^3),\qquad
\mathcal G_* = W^{(2)}[J_*].
$$

设 $K_* = \mathcal G_*^{-1}$，线性阶给 $\xi=K_*\eta$。把它代入二次项，再乘 $K_*$ 消去二次余量，得到

<span id="eq:c21-inverse-source-series"></span>

$$
\xi_a=K_{*,ab}\eta_b
-\frac12K_{*,ad}W^{(3)}_{*,def}
 K_{*,eb}K_{*,fc}\eta_b\eta_c+O(\eta^3).
$$

更高阶按同样方式递推：已知低阶逆以后，第 $r$ 阶未知项只经线性核 $\mathcal G_*$ 出现；若已知项留下余量 $R_r$，该阶逆就是 $-K_*R_r$。这在核可逆的分支上唯一确定了形式级数。

再直接变分 Legendre 表达式，随场变化的源也要一起变分：

<span id="eq:c21-inverse-legendre-variation"></span>

$$
\begin{aligned}
\delta\Gamma
&=\left\langle\frac{\delta W}{\delta J_\varphi},\delta J_\varphi\right\rangle
 -\langle\delta J_\varphi,\varphi\rangle
 -\langle J_\varphi,\delta\varphi\rangle\\
&=-\langle J_\varphi,\delta\varphi\rangle.
\end{aligned}
$$

第一项的 $\delta W/\delta J_\varphi=\varphi$，恰好消去第二项，留下式[（21.20）](#eq:c21-inverse-legendre)的负源。这一符号与源项 $+\langle J,\chi\rangle$ 及 $Z=e^{iW}$ 的约定相配。

<span id="c21-hessian"></span>

## 二点核的逆与高点顶角

Legendre关系还使我们能从平均场对源的响应读出完整传播子。先定义这个响应核：
<span id="eq:c21-response-hessian"></span>

$$
\mathcal G_J(x,y)
=\frac{\delta\varphi_J(x)}{\delta J(y)}
=\frac{\delta^2W}{\delta J(x)\delta J(y)}.
\tag{21.21}
$$

对归一化的一点函数再求一次源导数，分子的导数给出二点插入，分母的导数则扣去两个一点函数的乘积。这正好留下连通二点函数，因此
<span id="eq:c21-connected-hessian"></span>

$$
\begin{aligned}
\mathcal G_J(x,y)
&=i\bigl[
 \langle\mathrm T\widehat\varphi(x)\widehat\varphi(y)\rangle_J
 -\varphi_J(x)\varphi_J(y)\bigr]\\
&=iG_{c,J}(x,y).
\end{aligned}
\tag{21.22}
$$

在零源真空中，$G_{c,0}=\boldsymbol\Delta/i$，所以$\mathcal G_0=\boldsymbol\Delta$；平均场的线性响应由完整传播子决定。另一方面，对量子运动方程[（21.13）](#eq:c21-quantum-field-equation)求源导数，链式法则将量子作用量的二次变分与这个响应核相连：
<span id="eq:c21-inverse-hessian"></span>

$$
\int d^dz\,
 \Gamma^{(2)}(x,z;\varphi_J)\mathcal G_J(z,y)
=-\delta^d(x-y).
\tag{21.23}
$$

因此$\Gamma^{(2)}=-\mathcal G_J^{-1}$。如果改用时间序连通二点函数来写，同一关系就是$\Gamma^{(2)}G_{c,J}=i$。在零源下转到动量空间，并提出整体动量守恒的delta函数，便有
<span id="eq:c21-negative-quadratic-kernel"></span>

$$
\Gamma^{(2)}(k)
=-\widetilde{\boldsymbol\Delta}^{-1}(k^2)
=-[k^2+m^2-\Pi(k^2)].
\tag{21.24}
$$

这与本节开头按图线规则确定的负二次核一致：完整传播子描述场对源的响应，量子作用量的二次变分则给出这个响应的负逆核。

自由场可以把这种关系写得更具体。[第8节的源积分](/posts/srednicki-08/#c08-fourier)已给出$W_0[J]=\frac12\langle J,\Delta_0J\rangle$。求一次源导数得到$\varphi=\Delta_0J$，反解为$J=D\varphi$，其中$D=-\partial^2+m^2$。将这个源代入Legendre变换，两项分别成为
<span id="eq:c21-free-legendre"></span>

$$
\Gamma_0[\varphi]
=\frac12\langle D\varphi,\Delta_0D\varphi\rangle
 -\langle D\varphi,\varphi\rangle
=-\frac12\langle\varphi,D\varphi\rangle.
\tag{21.25}
$$

对最后一式分部积分，就回到自由Klein–Gordon作用量。自由理论中没有相互作用引起的圈修正，因而量子作用量与经典作用量一致，也显示了这里Legendre变换的符号如何与动能项相配。

继续对式[（21.23）](#eq:c21-inverse-hessian)求导，就能得到高点关系。一次源导数若作用在$\Gamma^{(2)}$上，会通过平均场的响应产生$\Gamma^{(3)}\mathcal G$；若作用在$\mathcal G$上，则产生$W^{(3)}$。将所得等式两边乘以相应逆核，解出三次源导数，便有
<span id="eq:c21-three-point-tree"></span>

$$
W^{(3)}_{ijk}
=\mathcal G_{ia}\mathcal G_{jb}\mathcal G_{kc}
 \Gamma^{(3)}_{abc}.
\tag{21.26}
$$

这里用重复指标表示对相应时空点积分。再求一次源导数，它可以落在三个外部 $\mathcal G$ 的任一个上，也可以落在 $\Gamma^{(3)}$ 上。利用 $\delta\mathcal G_{ia}/\delta J_l=W^{(3)}_{ial}$ 和 $\delta\varphi_d/\delta J_l=\mathcal G_{dl}$，四项分别为

$$
\begin{aligned}
W^{(4)}_{ijkl}
={}&W^{(3)}_{ial}\mathcal G_{jb}\mathcal G_{kc}\Gamma^{(3)}_{abc}\\
&+\mathcal G_{ia}W^{(3)}_{jbl}\mathcal G_{kc}\Gamma^{(3)}_{abc}\\
&+\mathcal G_{ia}\mathcal G_{jb}W^{(3)}_{kcl}\Gamma^{(3)}_{abc}\\
&+\mathcal G_{ia}\mathcal G_{jb}\mathcal G_{kc}\Gamma^{(4)}_{abcd}\mathcal G_{dl}.
\end{aligned}
$$

在前三项中代入式[（21.26）](#eq:c21-three-point-tree)，再统一积分指标，就能提出四条外部传播核：

$$
\begin{aligned}
W^{(4)}_{ijkl}
&=\mathcal G_{ia}\mathcal G_{jb}\mathcal G_{kc}\mathcal G_{ld}\,\mathcal K_{abcd},\\
\mathcal K_{abcd}
&=\Gamma^{(4)}_{abcd}
 +\Gamma^{(3)}_{abe}\mathcal G_{ef}\Gamma^{(3)}_{fcd}\\
&\quad+\Gamma^{(3)}_{ace}\mathcal G_{ef}\Gamma^{(3)}_{fbd}
 +\Gamma^{(3)}_{ade}\mathcal G_{ef}\Gamma^{(3)}_{fbc}.
\end{aligned}
$$

后三项是两个三点核由一条完整内线相连的三个交换道，每项的系数都是一。它们与四点 1PI 核一起，重建了前面通过图分解得到的全核树规则。

<span id="c21-derivative-expansion"></span>

## 导数展开与有效势

量子作用量以完整核为系数，通常不再是局部多项式。例如二点核中的$\Pi(k^2)$含有对数，傅里叶变换后会把不同位置的场联系起来。不过，若只关心变化缓慢的场，而且所用完整核在小外动量附近解析，就可以先按外动量展开，再将动量因子换成场的导数。在具有质量隙的微扰真空附近，最近的奇点限制了这个展开的尺度，因而场变化的典型动量须小于该尺度。

对单个实标量，洛伦兹不变性允许的最低项不含导数，下一阶含有两个导数。看似独立的$A(\varphi)\Box\varphi$项也可通过分部积分归并，因为
<span id="eq:c21-two-derivative-reduction"></span>

$$
\int d^dx\,A(\varphi)\Box\varphi
=-\int d^dx\,A'(\varphi)
 \partial_\mu\varphi\,\partial^\mu\varphi
\tag{21.27}
$$

这里的表面项由所用边界条件消去。这样，两个导数的各种写法可以合为一个系数函数，导数展开便写成
<span id="eq:c21-derivative-expansion"></span>

$$
\Gamma[\varphi]
=\int d^dx\left[
 -U(\varphi)
 -\frac12 Z(\varphi)\,
  \partial_\mu\varphi\,\partial^\mu\varphi
 +O(\partial^4)\right].
\tag{21.28}
$$

其中$U$和$Z$是场值的普通函数，而$\Gamma$是把这些函数及场的导数在整个时空上积分后得到的泛函。$O(\partial^4)$包括四个及更多导数的各种允许组合；做低动量近似时，可以按所需精度保留相应阶数。

导数展开的最低项具有直接的物理用途。令场在时空中处处相同，所有导数项就消失；先在有限时空体积下除去整体体积，再取相应极限，便可由式[（21.2）](#eq:c21-quantum-action-kernels)读出量子势，也称有效势（effective potential）：
<span id="eq:c21-potential-zero-momentum"></span>

$$
U(\varphi)
=\frac12[m^2-\Pi(0)]\varphi^2
 -\sum_{n\ge3}\frac{V_n(0,\ldots,0)}{n!}\varphi^n.
\tag{21.29}
$$

这里沿用一点函数为零的真空附近展开。最低阶取$V_3=g$，更高的$V_n$为零，于是$U_{\rm tree}=\frac12m^2\varphi^2-g\varphi^3/6$，恰好回到原拉格朗日量中的势能。高阶修正则通过零动量处的完整顶角进入这个函数。

二导数项在零场处的系数也可从同一个二点核读出。将它在$k^2=0$附近展开，得到
<span id="eq:c21-two-point-gradient-expansion"></span>

$$
k^2+m^2-\Pi(k^2)
=m^2-\Pi(0)+[1-\Pi'(0)]k^2+O(k^4).
\tag{21.30}
$$

把常数项与动量二次项分别同导数展开中的势项和动能项相比，就有
<span id="eq:c21-zero-field-coefficients"></span>

$$
U''(0)=m^2-\Pi(0),\qquad Z(0)=1-\Pi'(0).
\tag{21.31}
$$

这里的$Z(\varphi)$是导数展开的场依赖系数，与拉格朗日量中用于重整化的常数$Z_\varphi$不同。此前的单位留数条件是在$k^2=-m^2$处规定$\Pi'(-m^2)=0$，而导数展开采用零动量处的导数，因此$Z(0)$通常不等于1。

最后把这一近似下的量子运动方程写出。对式[（21.28）](#eq:c21-derivative-expansion)作一次变分，势项产生$-U'\delta\varphi$，动能项则分别从系数和场导数的变化产生$-\frac12Z'(\partial\varphi)^2\delta\varphi$与$-Z\partial^\mu\varphi\,\partial_\mu\delta\varphi$。对后一项分部积分，并沿用消去表面项的边界条件，得到
<span id="eq:c21-gradient-field-equation"></span>

$$
\frac{\delta\Gamma}{\delta\varphi}
=-U'(\varphi)+Z(\varphi)\Box\varphi
 +\frac12Z'(\varphi)(\partial\varphi)^2
 +O(\partial^4).
\tag{21.32}
$$

当源和场都取恒定值时，各个导数项消失，量子运动方程便化为
<span id="eq:c21-constant-source-equation"></span>

$$
U'(\varphi_J)=J.
\tag{21.33}
$$

零源时，有效势的驻点给出均匀真空的候选值，其稳定性由相应涨落决定。[第30节](/posts/srednicki-30/#c30)和[第31节](/posts/srednicki-31/#c31)将用有效势讨论自发对称性破缺。为此，先求出对称变换与背景平移对量子作用量的作用。

<span id="c21-symmetry"></span>

## 线性对称性如何传到量子作用量

设多分量场作可逆线性变换 $\chi\mapsto R\chi$，作用量、正则化测度及积分边界均在该变换下不变。用核记法定义转置，使源场配对满足

<span id="eq:c21-source-transpose"></span>

$$
\begin{aligned}
(R\chi)_a(x)&=\int d^dy\,R_{ab}(x,y)\chi_b(y),\\
(R^TJ)_a(x)&=\int d^dy\,J_b(y)R_{ba}(y,x),\\
\langle R^TJ,\chi\rangle&=\langle J,R\chi\rangle.
\end{aligned}
$$

在路径积分中令 $\eta=R\chi$，源的变换便可还原为积分变量的变换：

<span id="eq:c21-symmetric-generator"></span>

$$
\begin{aligned}
Z[R^TJ]
&=\int\mathcal D\chi\,e^{iS[\chi]+i\langle J,R\chi\rangle}\\
&=\int\mathcal D\eta\,e^{iS[\eta]+i\langle J,\eta\rangle}
=Z[J],\\
W[R^TJ]&=W[J].
\end{aligned}
$$

最后一行取由 $Z[0]=1$ 连续固定的同一对数分支。对源求导，链式法则给 $R\varphi[R^TJ]=\varphi[J]$。将 $R$ 换成 $R^{-1}$，便知平均场变为 $R\varphi$ 所需的源是 $R^{-T}J_\varphi$。于是

<span id="eq:c21-effective-symmetry"></span>

$$
\begin{aligned}
J_{R\varphi}&=R^{-T}J_\varphi,\\
\Gamma[R\varphi]
&=W[R^{-T}J_\varphi]
 -\langle R^{-T}J_\varphi,R\varphi\rangle\\
&=W[J_\varphi]-\langle J_\varphi,\varphi\rangle
=\Gamma[\varphi].
\end{aligned}
$$

所以量子作用量继承作用量和测度共同具有的线性对称性。若 $R$ 含有导数，转置还包括分部积分产生的符号。例如无穷小平移 $R=1+a^\mu\partial_\mu$ 在消去表面项后给 $R^T=1-a^\mu\partial_\mu$；以上关系也就按同一无穷小阶成立。

<span id="c21-background"></span>

## 绕给定背景展开

给定背景场 $\bar\varphi$，把积分变量 $\chi$ 取为相对于背景的涨落，并让源与它耦合：

<span id="eq:c21-background-generator"></span>

$$
Z[J;\bar\varphi]=e^{iW[J;\bar\varphi]}
=\int\mathcal D\chi\,
 e^{iS[\chi+\bar\varphi]+i\langle J,\chi\rangle}.
$$

各背景使用相同归一化，场的平移保持积分域和相容的真空边界。令 $\eta=\chi+\bar\varphi$，则测度不变，而源项中多出 $-\langle J,\bar\varphi\rangle$：

<span id="eq:c21-background-shift"></span>

$$
\begin{aligned}
Z[J;\bar\varphi]&=e^{-i\langle J,\bar\varphi\rangle}Z[J;0],\\
W[J;\bar\varphi]&=W[J;0]-\langle J,\bar\varphi\rangle,\\
\varphi=\frac{\delta W[J;\bar\varphi]}{\delta J}
&=\frac{\delta W[J;0]}{\delta J}-\bar\varphi.
\end{aligned}
$$

因此同一个源在零背景理论中产生的平均场为 $\varphi+\bar\varphi$。在固定背景下做 Legendre 变换，源项与背景项合并为总平均场的配对：

<span id="eq:c21-background-action"></span>

$$
\begin{aligned}
J_{\varphi;\bar\varphi}&=J_{\varphi+\bar\varphi;0},\\
\Gamma[\varphi;\bar\varphi]
&=W[J_{\varphi;\bar\varphi};0]
 -\langle J_{\varphi;\bar\varphi},\varphi+\bar\varphi\rangle\\
&=\Gamma[\varphi+\bar\varphi;0].
\end{aligned}
$$

特别地，$\Gamma[0;\bar\varphi]=\Gamma[\bar\varphi;0]$。围绕背景计算而令平均涨落为零，所得就是总平均场取该背景值时的量子作用量，这为计算有效势提供了另一种展开方式。

---

[← 第 20 节](/posts/srednicki-20/) · [章节地图](/srednicki/) · [第 22 节 →](/posts/srednicki-22/)
