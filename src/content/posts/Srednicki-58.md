---
title: 'Srednicki §58 旋量电动力学'
date: 2026-09-14
category: 笔记
tags: [物理, 量子场论, Srednicki]
series: 'Srednicki QFT'
srednickiSections: [58]
hideFromHome: true
draft: false
---

<span id="c58"></span>

前两节已经知道怎样描述自由光子，以及电磁场怎样响应给定的电流。现在让电子本身
产生这个电流，便得到旋量电动力学（spinor electrodynamics），也就是含一个带电
狄拉克场的量子电动力学（quantum electrodynamics，QED）。引入相互作用之后，
电子场和电磁场的规范变换必须配合起来；由此可以将拉氏量写成规范不变的形式，
并把已有的两类传播子组合成计算散射所需的费曼规则。
“量子电动力学”也可指电磁场与其他种类的带电量子场相互作用；这里用“旋量”
指出所选的物质场是狄拉克场。

<span id="c58-current"></span>

## 电子电流与相互作用

狄拉克场在整体相位变换下的守恒流已经在[第36节](/posts/srednicki-36/#c36)得到。
乘上电子电荷，就成为电磁场的源。这里以$e$表示电子电荷，它本身带负号：
<span id="eq:c58-charge-current"></span>

$$
\begin{aligned}
j^\mu&=e\bar\Psi\gamma^\mu\Psi,\qquad
j^0=e\Psi^\dagger\Psi,\\
Q&=\int d^3x\,{:j^0:}=e(N_b-N_d),\\
[Q,b_s^\dagger(p)]&=e\,b_s^\dagger(p),\qquad
[Q,d_s^\dagger(p)]=-e\,d_s^\dagger(p).
\end{aligned}
\tag{58.1}
$$

第二式用了$\bar\Psi=\Psi^\dagger\gamma^0$和$(\gamma^0)^2=1$。
把模式展开代入空间积分，平面波给出动量$\delta$函数，旋量归一抵消
模式测度中的$2\omega_{\mathbf p}$，两种频率之间的交叉项则由旋量正交性消失。
[第39节](/posts/srednicki-39/#c39-charge)已逐项完成这个计算，并将$dd^\dagger$正规序为
$-d^\dagger d$，减去真空荷后得到粒子数之差$N_b-N_d$。
现在只需乘上$e$，故$b^\dagger$所产生的电子带电荷$e$，
$d^\dagger$所产生的正电子带电荷$-e$。
采用亥维赛–洛伦兹单位制并令$\hbar=c=1$，低能在壳电荷的数值例可取
$e\simeq-0.302822$，精细结构常数为$\alpha_{\rm em}=e^2/(4\pi)\simeq1/137.036$。
在壳方案与$\overline{\mathrm{MS}}$方案的区别将在第62、63和66节讨论。
第45节若以正的电荷单位表示电子电荷，这里的$e$便是那个单位的负值。

取电流与势的局部线性耦合$j^\mu A_\mu$，与自由作用量相加，得到
<span id="eq:c58-lagrangian"></span>

$$
\begin{aligned}
\mathcal L&=\mathcal L_0+\mathcal L_1,\\
\mathcal L_0&=-\frac14F^{\mu\nu}F_{\mu\nu}
 +i\bar\Psi\gamma^\mu\partial_\mu\Psi-m\bar\Psi\Psi,\\
\mathcal L_1&=eA_\mu\bar\Psi\gamma^\mu\Psi .
\end{aligned}
\tag{58.2}
$$

四维作用量无量纲，两个动能项分别给出$[A]=1$和$[\Psi]=3/2$，
于是$[j]=3$、$[e]=0$。电流与电磁势的耦合具有正确的质量维数。
电流是厄米矢量，$e$为实数，故相互作用也为厄米。本节先求树级结果，
拉氏量中的场归一因子与反项暂时省略。

这里遇到一个前两节没有的问题。给定的外电流可以事先要求满足
$\partial_\mu J^\mu=0$，电子电流的守恒却是运动方程的结果。
为了看清所用条件，暂将两个狄拉克方程的左端写为
<span id="eq:c58-current-divergence"></span>

$$
\begin{aligned}
\mathcal E&=(i\gamma^\mu\partial_\mu
                    +e\gamma^\mu A_\mu-m)\Psi,\\
\overline{\mathcal E}
 &=i(\partial_\mu\bar\Psi)\gamma^\mu
       -e\bar\Psi\gamma^\mu A_\mu+m\bar\Psi,\\
\overline{\mathcal E}\Psi+\bar\Psi\mathcal E
 &=i(\partial_\mu\bar\Psi)\gamma^\mu\Psi
     +i\bar\Psi\gamma^\mu\partial_\mu\Psi\\
 &=i\partial_\mu(\bar\Psi\gamma^\mu\Psi),\\
\partial_\mu j^\mu
 &=-ie\bigl(\overline{\mathcal E}\Psi+\bar\Psi\mathcal E\bigr).
\end{aligned}
\tag{58.3}
$$

两个质量项相消，两个含$A_\mu$的项也相消；计算始终保持$\bar\Psi$在左、
$\Psi$在右。满足$\mathcal E=\overline{\mathcal E}=0$时电流自然守恒。
路径积分还要对不满足这些方程的场构型积分，因而不能把每个构型中的$j$
都当作前两节的守恒外源来处理。解决这一问题，需要同时考察两种场的变换。

<span id="c58-covariant"></span>

## 局域相位与协变导数

为电子场配上一个随位置变化的相位。令$\Gamma(x)$为实函数，
取
<span id="eq:c58-joint-transformation"></span>

$$
A'_\mu=A_\mu-\partial_\mu\Gamma,\qquad
\Psi'=u\Psi,\qquad
\bar\Psi'=\bar\Psi u^{-1},\qquad
u(x)=e^{-ie\Gamma(x)} .
\tag{58.4}
$$

相位是格拉斯曼偶数，与场分量和$\gamma$矩阵对易，所以$j'{}^\mu=j^\mu$，
质量项也不变。动能中却有导数作用到相位，利用
$\partial_\mu u=-ie(\partial_\mu\Gamma)u$，恰得到相互作用所需要的一项：
<span id="eq:c58-local-cancellation"></span>

$$
\begin{aligned}
i\bar\Psi'\gamma^\mu\partial_\mu\Psi'
 &=i\bar\Psi u^{-1}\gamma^\mu
       \bigl[(\partial_\mu u)\Psi+u\partial_\mu\Psi\bigr]\\
 &=i\bar\Psi\gamma^\mu\partial_\mu\Psi
       +j^\mu\partial_\mu\Gamma,\\
j'{}^\mu A'_\mu
 &=j^\mu A_\mu-j^\mu\partial_\mu\Gamma .
\end{aligned}
\tag{58.5}
$$

新增的两项在每一点相消。这个抵消直接发生在拉氏量中，无须使用场方程。
又因为偏导可交换，$F'_{\mu\nu}=F_{\mu\nu}$，麦克斯韦项也保持原样。
因此完整作用量对于任意平滑局域相位都具有规范不变性。

将含$A_\mu$的项与普通导数放在一起，拉氏量可以写得更简洁：
<span id="eq:c58-covariant-lagrangian"></span>

$$
D_\mu=\partial_\mu-ieA_\mu,\qquad
\mathcal L=-\frac14F^{\mu\nu}F_{\mu\nu}
                +\bar\Psi(i\gamma^\mu D_\mu-m)\Psi .
\tag{58.6}
$$

$D_\mu$称为协变导数（covariant derivative）。这个名称的含义是，
它作用后的旋量与原旋量具有同一个局域相位。为验证这一点，将$D'_\mu$
作用于任意旋量函数$uf$：
<span id="eq:c58-covariant-action"></span>

$$
\begin{aligned}
D'_\mu(uf)
 &=\bigl(\partial_\mu-ieA_\mu+ie\partial_\mu\Gamma\bigr)(uf)\\
 &=u\partial_\mu f-ie(\partial_\mu\Gamma)uf
        -ieA_\mu uf+ie(\partial_\mu\Gamma)uf\\
 &=uD_\mu f .
\end{aligned}
\tag{58.7}
$$

取$f=\Psi$，就确定了协变导数作用于电子场的变换。由于这个等式对任意$f$成立，还可以把变换规律
写成算符等式：
<span id="eq:c58-operator-transformation"></span>

$$
D'_\mu=uD_\mu u^{-1},\qquad
D'_\mu\Psi'=uD_\mu u^{-1}u\Psi=uD_\mu\Psi .
\tag{58.8}
$$

这里的乘积按从右到左作用。例如$uD_\mu u^{-1}$作用到$f$时，$D_\mu$要微分
整个$u^{-1}f$；其乘积法则包含$\partial_\mu f$。这样便完整保留了微分算符，
同时自动计入相位的导数。

协变导数还把电磁场强包含在自身的代数中。连续作用两次，先保留各个导数项：
<span id="eq:c58-double-covariant-derivative"></span>

$$
\begin{aligned}
D_\mu D_\nu f
={}&\partial_\mu\partial_\nu f
 -ie(\partial_\mu A_\nu)f-ieA_\nu\partial_\mu f\\
 &-ieA_\mu\partial_\nu f-e^2A_\mu A_\nu f .
\end{aligned}
\tag{58.9}
$$

交换$\mu,\nu$后相减，二阶偏导消去，两项含$\partial f$的交叉项也消去。
由于电磁势的乘法可交换，最后的$e^2$项同样消失。因此
<span id="eq:c58-field-strength-commutator"></span>

$$
[D_\mu,D_\nu]f=-ieF_{\mu\nu}f,\qquad
[D^\mu,D^\nu]=-ieF^{\mu\nu},\qquad
F^{\mu\nu}=\frac{i}{e}[D^\mu,D^\nu] .
\tag{58.10}
$$

最后一式按非零电荷使用；第一式连同$e=0$的自由极限仍然成立。
对易子经过相减已经不含作用于$f$的导数，右边就是乘以局部函数的算符。
利用式[（58.8）](#eq:c58-operator-transformation)，立刻得到
<span id="eq:c58-field-strength-invariance"></span>

$$
\begin{aligned}
\relax[D'{}^\mu,D'{}^\nu]
 &=u[D^\mu,D^\nu]u^{-1},\\
F'{}^{\mu\nu}
 &=uF^{\mu\nu}u^{-1}=F^{\mu\nu}.
\end{aligned}
\tag{58.11}
$$

这条途径与直接变换电磁势得到同一个场强不变性，并解释了场强为什么能由
两个协变导数的对易子表示。

现在可以回过头来理解引入电磁场的理由。自由狄拉克作用量在整体变换
<span id="eq:c58-global-phase"></span>

$$
\Psi\longmapsto e^{-i\theta}\Psi,\qquad
\bar\Psi\longmapsto\bar\Psi e^{i\theta},\qquad \theta=\text{常数}
\tag{58.12}
$$

下不变，这是整体$U(1)$对称性。若允许$\theta=e\Gamma(x)$随位置变化，
普通导数会多出相位梯度。引入按式[（58.4）](#eq:c58-joint-transformation)变换的
$A_\mu$，并把$\partial_\mu$替换为$D_\mu$，就能抵消这个梯度。
于是局域$U(1)$对称性将光子与电子的相互作用联系到了一起。
把整体对称性提升为局域对称性的这一做法，称为规范化（gauging）。

<span id="c58-gauge-fixing"></span>

## 联合路径积分与费曼规范

有了逐构型成立的规范不变性，就可以处理联合路径积分中的冗余。
先沿上一节的思路消去一个规范坐标，再对不同规范条件作加权平均，
从而求出费曼规范的传播子。第71节将把这一方法用于非阿贝尔理论。

先不加外源。在选定边界并除去规范算符零模之后，可以局部写
$A_\mu=A_{T\mu}+\partial_\mu\chi$，再取$\Gamma=\chi$，将势变为$A_T$。
同时令$\Psi_T=e^{-ie\chi}\Psi$、$\bar\Psi_T=\bar\Psi e^{ie\chi}$，
作用量就化为$S[A_T,\bar\Psi_T,\Psi_T]$。按照[第44节](/posts/srednicki-44/#c44)的配对奇测度，
有限组变量的线性代换给出逆行列式。记$U=e^{ie\chi}$，则
<span id="eq:c58-paired-berezin"></span>

$$
\begin{aligned}
\Psi&=U\Psi_T,\qquad \bar\Psi=\bar\Psi_TU^{-1},\\
d\Psi\,d\bar\Psi
 &=(\det U)^{-1}(\det U^{-1})^{-1}
          d\Psi_T\,d\bar\Psi_T
  =d\Psi_T\,d\bar\Psi_T .
\end{aligned}
\tag{58.13}
$$

两个相位雅可比因子相消，表明沿规范轨道同时改变三种场，不产生额外的费米测度因子。
将这个有限代数用于场积分时，取保留局域矢量$U(1)$且与边界相容的共同调节定义。
局域相位乘法会混合傅里叶模式，因而简单删去任意一部分模式未必保留上述变换；
相容性须在调节定义中实现。

规范体积的分离可以直接使用[第57节](/posts/srednicki-57/#c57-measure)已经证明的实变量$\delta$恒等式。
取$\mathcal F[A]=\partial^\mu A_\mu$、$\mathcal M=-\partial^2$，在除去零模的
有限规范参数空间有
<span id="eq:c58-gauge-delta-identity"></span>

$$
\begin{aligned}
\mathcal F[A^\Gamma]&=\mathcal F[A]+\mathcal M\Gamma,\\
1&=|\det{}'\mathcal M|
       \int d\Gamma\,\delta\bigl(\mathcal F[A^\Gamma]-f\bigr).
\end{aligned}
\tag{58.14}
$$

第二行来自变量代换$y=\mathcal F[A]+\mathcal M\Gamma-f$，
其雅可比因子为$|\det{}'\mathcal M|$。把它插入零源积分，随后同时变换
$A,\Psi,\bar\Psi$，作用量与测度保持不变，只留下同一个规范体积。
$\mathcal M$与这些场无关，因此它的行列式也只是一个公共因子。
它们都在归一化中消去，留下固定$\mathcal F[A]=f$的积分。

还可以不选某一个$f$，而对它作高斯平均。权重取
$\exp[-i\int d^4x\,f^2/(2\xi)]$，于是$\delta$函数直接给出
<span id="eq:c58-gauge-average"></span>

$$
\begin{aligned}
&\int Df\,\delta\bigl(\mathcal F[A]-f\bigr)
       \exp\!\left[-\frac{i}{2\xi}\int d^4x\,f(x)^2\right]\\
&\hspace{15mm}
 =\exp\!\left[-\frac{i}{2\xi}\int d^4x\,
                         (\partial^\mu A_\mu)^2\right],\\
\mathcal L_{\rm gf}&=-\frac1{2\xi}(\partial^\mu A_\mu)^2 .
\end{aligned}
\tag{58.15}
$$

共同归一化所含的$f$积分不依赖场。这里的高斯按第57节的真空解析积分路径
理解；也可以先在$\xi>0$的欧氏积分中平均，再作相同的解析延拓。
这样定义了规范参数$\xi$。它只改变积分中规范自由度的权重。

将这一项加入光子二次作用量。在傅里叶空间，
$(\partial\cdot A)(k)=ik^\mu A_\mu(k)$，另一因子携带$-k$，
所以它们的乘积为$k^\mu k^\nu A_\mu(-k)A_\nu(k)$，从而
<span id="eq:c58-gauge-fixed-kernel"></span>

$$
\begin{aligned}
S_{\gamma,\xi}
 &=-\frac12\int\frac{d^4k}{(2\pi)^4}\,
      A_\mu(-k)M_\xi^{\mu\nu}(k)A_\nu(k),\\
M_\xi^{\mu\nu}(k)
 &=k^2g^{\mu\nu}-(1-\xi^{-1})k^\mu k^\nu,\\
M_1^{\mu\nu}(k)&=k^2g^{\mu\nu}.
\end{aligned}
\tag{58.16}
$$

取$\xi=1$便是费曼规范。原来妨碍求逆的$k^\mu k^\nu$项
完全消去，四个分量可以按第57节给出的共同高斯处方积分。
由于$g^{\mu\nu}g_{\nu\rho}=\delta^\mu{}_\rho$，非类光处的逆核就是
$g_{\mu\nu}/k^2$。具体应用上一节的模式积分时，取四个方向的符号
$(-1,1,1,1)$，负范数方向沿相同复路径积分，各零源行列式在比值中消去，
再将标量分母取为共同的$k^2-i0$。
因而费曼规范核来自规范固定后的二次作用量。计算电子场的关联函数时，
不必再把式[（58.3）](#eq:c58-current-divergence)当作对每个积分变量的约束。

<span id="c58-generating-functional"></span>

## 相互作用生成泛函

在已经固定的规范中加入源，取源项的次序为
<span id="eq:c58-source-order"></span>

$$
\mathcal L_{\rm source}
   =J^\mu A_\mu+\bar\eta\Psi+\bar\Psi\eta .
\tag{58.17}
$$

$J^\mu$是偶源，$\eta,\bar\eta$是相互独立的格拉斯曼奇源。
这些源用来取得指定分量的格林函数，故此处可任意取值。
规范已在加源以前固定，后续求导不会用到守恒外源的限制。

自由费米高斯沿第43、44节，光子高斯用
式[（58.16）](#eq:c58-gauge-fixed-kernel)。两者独立，归一生成泛函相乘：
<span id="eq:c58-free-generator"></span>

$$
\begin{aligned}
Z_0[\bar\eta,\eta,J]
 ={}&\exp\!\left[
 i\int d^4x\,d^4y\,\bar\eta(x)S(x-y)\eta(y)\right]\\
 &\times\exp\!\left[
 \frac i2\int d^4x\,d^4y\,J^\mu(x)\Delta_{\mu\nu}(x-y)J^\nu(y)\right],\\
S(x-y)&=\int\frac{d^4p}{(2\pi)^4}\,
 e^{ip(x-y)}\frac{-\slashed p+m}{p^2+m^2-i0},\\
\Delta_{\mu\nu}(x-y)&=\int\frac{d^4k}{(2\pi)^4}\,
 e^{ik(x-y)}\frac{g_{\mu\nu}}{k^2-i0}.
\end{aligned}
\tag{58.18}
$$

光子核带下指标，与两个上指标的$J$缩并；
它的$1/2$来自实场二次型的对称性。费米二次型的两个源彼此独立，因而没有
这个半因子。继续沿用$S=i\langle\mathrm T\Psi\bar\Psi\rangle_0$和
$\Delta_{\mu\nu}=i\langle\mathrm TA_\mu A_\nu\rangle_0$。
求逆时先用同一可逆调节核，随后取所写的费曼边界值。

把$\exp[i\int\mathcal L_1]$展开，就可以用源导数代替其中的场。
由式[（58.17）](#eq:c58-source-order)的排列，三个替换依次为
<span id="eq:c58-field-insertions"></span>

$$
A_\mu\ \longleftrightarrow\ \frac1i\frac{\delta}{\delta J^\mu},
\qquad
\bar\Psi_a\ \longleftrightarrow\ i\frac{\delta^L}{\delta\eta_a},
\qquad
\Psi_b\ \longleftrightarrow\ \frac1i\frac{\delta^L}{\delta\bar\eta_b}.
\tag{58.19}
$$

中间一项的号来自左奇导数：
$\delta^L(\bar\Psi_a\eta_a)/\delta\eta_a=-\bar\Psi_a$。
它对源指数求导给$-i\bar\Psi_a$，再乘$i$才插入所需的场。
对$\bar\eta$求导时不必越过另一个奇量，所以最后一项的系数是$1/i$。
普通的$J^\mu$导数则插入$A_\mu$。

保持相互作用中$\bar\Psi_a(\gamma^\mu)_{ab}\Psi_b$的顺序，得到
<span id="eq:c58-interacting-generator"></span>

$$
\begin{aligned}
\mathscr V={}&\exp\!\left[
 ie\int d^4w\,
 \left(\frac1i\frac{\delta}{\delta J^\mu(w)}\right)
 \left(i\frac{\delta^L}{\delta\eta_a(w)}\right)
 (\gamma^\mu)_{ab}
 \left(\frac1i\frac{\delta^L}{\delta\bar\eta_b(w)}\right)
 \right],\\
Z[\bar\eta,\eta,J]
 &=\frac{\mathscr VZ_0[\bar\eta,\eta,J]}
               {(\mathscr VZ_0)[0,0,0]},\qquad Z=e^{iW}.
\end{aligned}
\tag{58.20}
$$

导数从最右端开始作用。
零源分母使$Z[0,0,0]=1$；取对数后，完整连通分支的指数计数与第9、45节相同，
$iW=\log Z$便只保留连通图。至此，计算所需的泛函已经确定，下面从一次顶角
的实际求导读出各个图因子。

<span id="c58-vertex"></span>

## 从一次顶角求导读出图因子

先只看费米高斯，简记$Z_F=\exp(i\bar\eta S\eta)$，
并令$r_b(w)=(S\eta)_b(w)$、$\ell_a(w)=(\bar\eta S)_a(w)$。
它们都是奇量。一次$\bar\eta$导数和一次$\eta$导数分别给
$\delta^L_{\bar\eta_b}Z_F=ir_bZ_F$、
$\delta^L_{\eta_a}Z_F=-i\ell_aZ_F$。因此同一顶角内的有序求导为
<span id="eq:c58-ordered-odd-derivatives"></span>

$$
\begin{aligned}
\left(i\frac{\delta^L}{\delta\eta_a}\right)
\left(\frac1i\frac{\delta^L}{\delta\bar\eta_b}\right)Z_F
 &=i\frac{\delta^L}{\delta\eta_a}(r_bZ_F)\\
 &=\bigl[iS_{ba}(0)-r_b\ell_a\bigr]Z_F\\
 &=\bigl[iS_{ba}(0)+\ell_a r_b\bigr]Z_F .
\end{aligned}
\tag{58.21}
$$

第二行在乘积法则中用了$r_b$为奇数；最后一行把两个奇量交换次序，
使$\bar\eta$重新处于左端。这个计算与第45节的汤川顶角相同，
但现在两个旋量指标之间还要插入$\gamma^\mu$。

光子导数则给出偶量
$B_\mu(w)=\int d^4z\,\Delta_{\mu\nu}(w-z)J^\nu(z)$。
乘上$\gamma^\mu$并对顶角位置积分，式[（58.20）](#eq:c58-interacting-generator)
的一阶连通部分为
<span id="eq:c58-one-vertex-source"></span>

$$
\begin{aligned}
(iW)_{\text{一次顶角}}
={}&ie\int d^4w\,B_\mu(w)
       \int d^4x\,d^4y\,
       \bar\eta(x)S(x-w)\gamma^\mu S(w-y)\eta(y)\\
 &-e\int d^4w\,B_\mu(w)\,
                    \operatorname{tr}\!\left[\gamma^\mu S(0)\right].
\end{aligned}
\tag{58.22}
$$

第一项是一条连接两个费米源的开链，再接一条光子线。第二项把同一顶角的两个
费米端收缩在一起，是一个闭合费米圈。其系数可以逐项读为
$(-1)(ie)(1/i)=-e$：顶角给$ie$，费米传播线给$S/i$，闭圈另外带负号。
同点迹按共同调节定义；在保持电荷共轭的真空中，这个单光子项由
[下文费里定理的选择律](#c58-furry)消失。求树级顶角时只需保留第一项。

再对开链项取三个外源导数，并把源置零。$\eta$左导数越过$\bar\eta$源给一个负号，
三个场插入的数值系数为$(1/i)i(1/i)=1/i$，于是
<span id="eq:c58-three-point-function"></span>

$$
\begin{aligned}
&\langle0|\mathrm T\Psi_a(x)\bar\Psi_b(y)A_\nu(z)|0\rangle_C^{(1)}\\
&\qquad=-e\int d^4w\,
      [S(x-w)\gamma^\mu S(w-y)]_{ab}\Delta_{\mu\nu}(w-z).
\end{aligned}
\tag{58.23}
$$

这也可以写成三个自由时间序核与一个局部顶角的乘积，因为
<span id="eq:c58-amputation-factor"></span>

$$
\frac{S}{i}\,(ie\gamma^\mu)\,
           \frac{S}{i}\,\frac{\Delta_{\mu\nu}}{i}
       =-e\,S\gamma^\mu S\Delta_{\mu\nu}.
\tag{58.24}
$$

除去外传播子之后，剩下的顶角恰为$ie\gamma^\mu$。
拉氏量在该顶角含一个$A$、一个$\Psi$和一个$\bar\Psi$，没有同种场的局部阶乘。
在高阶展开中，顶角位置的标号置换抵消指数的$1/V!$，余下的同图重数按
第9节的图对称性处理。狄拉克动能只含一次$D_\mu$，所以本模型也没有
$A^2\bar\Psi\Psi$四价接触项。

还可以用一个简单的电子矩阵元确定同一顶角的整体号。沿已定的
$|p,s\rangle=b_s^\dagger(p)|0\rangle$归一，模式中的$b^\dagger b$项给
<span id="eq:c58-born-current"></span>

$$
\begin{aligned}
\langle p',s'|j^\mu(x)|p,s\rangle
 &=e\bar u_{s'}(p')\gamma^\mu u_s(p)e^{i(p-p')x},\\
\langle p',s'|S^{(1)}|p,s\rangle_A
 &=ie\int d^4x\,
    \bar u_{s'}(p')\gamma^\mu u_s(p)A_\mu(x)e^{i(p-p')x}.
\end{aligned}
\tag{58.25}
$$

这是一阶外给电磁势中的跃迁。它的$ie$直接来自$i\int jA$，
也固定了费曼图与既有福克态约定之间的共同相位。

<span id="c58-lines"></span>

## 外线、内线与矩阵链

电子的外线仍按[第45节](/posts/srednicki-45/#c45-rules)约化，
光子的外线按[第56节](/posts/srednicki-56/#c56)约化。把模式与相应单粒子态重叠，四类费米端是
<span id="eq:c58-fermion-overlaps"></span>

$$
\begin{aligned}
\langle0|\Psi(x)|e^-(p,s)\rangle
     &=u_s(p)e^{ipx},\\
\langle e^-(p,s)|\bar\Psi(x)|0\rangle
     &=\bar u_s(p)e^{-ipx},\\
\langle0|\bar\Psi(x)|e^+(p,s)\rangle
     &=\bar v_s(p)e^{ipx},\\
\langle e^+(p,s)|\Psi(x)|0\rangle
     &=v_s(p)e^{-ipx}.
\end{aligned}
\tag{58.26}
$$

因此入电子乘$u$，出电子乘$\bar u$，入正电子乘$\bar v$，出正电子乘$v$。
所有$p$都表示正能的物理动量。费米箭头约定与粒子流一致，
所以入电子的箭头指向顶角，出电子的箭头离开顶角；正电子的箭头恰好相反，
沿箭头标出的动量分别是$-p$、$-p'$。旋量$v$的宗量仍是正能$p$，
不能把箭头动量的负号另外移进$v$的宗量。

第55节的光子展开将$\varepsilon^{\mu*}$与湮灭算符相配。
沿第56节单位单光子重叠的归一，
<span id="eq:c58-photon-overlaps"></span>

$$
\begin{aligned}
\langle0|A^\mu(x)|\gamma(k,\lambda)\rangle
 &=\varepsilon_\lambda^{\mu*}(k)e^{ikx},\\
\langle\gamma(k',\lambda')|A^\mu(x)|0\rangle
 &=\varepsilon_{\lambda'}^\mu(k')e^{-ik'x}.
\end{aligned}
\tag{58.27}
$$

所以入光子乘$\varepsilon^{\mu*}$、出光子乘$\varepsilon^\mu$。
波浪线的箭头只表示动量：入射时$k$指向顶角，出射时$k'$离开顶角。
它与实费米线用来区分粒子流向的箭头作用不同。此处使用上一节的物理横向偏振；
光子内线则仍须对四维动量和全部洛伦兹指标缩并。

将外传播子约化后，内部仍保留自由时间序核。因此内线与顶角的统一字典是
<span id="eq:c58-internal-rules"></span>

$$
\begin{aligned}
C_F(p)&=\frac{\widetilde S(p)}i
  =\frac{-i(-\slashed p+m)}{p^2+m^2-i0},\\
C_{\mu\nu}(k)&=\frac{\widetilde\Delta_{\mu\nu}(k)}i
  =\frac{-ig_{\mu\nu}}{k^2-i0},\\
V^\mu&=ie\gamma^\mu .
\end{aligned}
\tag{58.28}
$$

这套字典使光子核的两个下指标分别接到两个顶角的上指标。
若把内光子线改写为上指标度规，
相邻两个顶角应同时写成$ie\gamma_\mu$、$ie\gamma_\nu$。两种写法通过度规
升降完全相等。例如一条交换光子线给出的旋量缩并含有
<span id="eq:c58-index-dictionary"></span>

$$
(\bar u_1\gamma^\mu u_2)\,g_{\mu\nu}\,
       (\bar u_3\gamma^\nu u_4)
 =(\bar u_1\gamma_\mu u_2)\,g^{\mu\nu}\,
       (\bar u_3\gamma_\nu u_4).
\tag{58.29}
$$

外偏振也必须以同样的指标规则连接，譬如入光子顶角为
$ie\gamma^\mu\varepsilon_\mu^*$。

沿一条费米线，矩阵乘法的次序由实际收缩固定。从共轭旋量的一端出发，
逆着费米箭头读到$u$或$v$端，依次写出遇到的顶角和内线。例如一条含两个
顶角的电子链为
<span id="eq:c58-matrix-chain"></span>

$$
\begin{aligned}
&\bar u_a(p')\,(ie\gamma^\nu)_{ab}
        [C_F(q)]_{bc}(ie\gamma^\mu)_{cd}u_d(p)
\\
&\qquad=\bar u(p')\,ie\gamma^\nu C_F(q)\,ie\gamma^\mu u(p).
\end{aligned}
\tag{58.30}
$$

每个重复旋量指标都连接相邻的两个因子，因而这一顺序不能任意交换。
若右端接入光子、左端接出光子，再乘
$\varepsilon_\mu^*(k)\varepsilon_\nu(k')$，便得到相应图的全部指标缩并。
把某个电子端换为正电子端时，只需按式[（58.26）](#eq:c58-fermion-overlaps)换成
相应的$v$或$\bar v$，并保持箭头动量和矩阵链的次序。

<span id="c58-trees"></span>

## 怎样组成树级散射振幅

每个QED顶角连接一条进入的费米箭头、一条离开的费米箭头及一条光子线。
给定外粒子后，按这种顶角连接所有拓扑不同的树图。树图没有闭合路径，
故所有内部动量都由外动量决定。具体地，顶角位置积分给
<span id="eq:c58-vertex-momentum"></span>

$$
\int d^4x\,e^{i(p+k-p')x}
       =(2\pi)^4\delta^4(p+k-p') .
\tag{58.31}
$$

它表示箭头向内的动量之和等于向外的动量之和。一条含$V$个顶角的连通树
有$I=V-1$条内线；$V$个顶角$\delta$函数中有一个表示总动量守恒，
其余$V-1$个恰好消去全部内动量积分。也可以切开任意一条内线：
树被分成两个连通部分，分别将其中的顶角守恒式相加，内部动量成对消去，
只剩所切内线的动量等于这一部分外动量的带号总和。这就逐条确定了全部内线动量。

计数还能说明当前近似保留到哪一阶。设外线总数为$E$，每个顶角三价，
连通图的圈数为$L=I-V+1$，则
<span id="eq:c58-tree-power"></span>

$$
3V=2I+E,\qquad
V=E-2+2L,\qquad
V_{\rm tree}=E-2 .
\tag{58.32}
$$

因此固定外线的树项带$e^{E-2}$，下一圈从$e^E$开始。
树级规则保留前者，省去圈修正及相应反项。实际大小还取决于运动学，
当后续计算出现大的对数时，单凭$|e|$较小仍不足以保证固定阶近似有效。

多条费米线的相对负号沿第45节确定。把各条箭头都画成从左到右，
固定左端外粒子的标号次序，再比较右端标号的置换；奇置换带负号。
这个规则的代数来源是有序奇源导数，或等价地，反对易的外粒子产生算符。
对两条线，固定外场次序后的两种配对总有如下结构：
<span id="eq:c58-endpoint-permutation"></span>

$$
\mathcal K_{11}\mathcal K_{22}
             -\mathcal K_{12}\mathcal K_{21}.
\tag{58.33}
$$

其中$\mathcal K_{ij}$表示从固定的共轭端$i$连到未共轭端$j$的整条旋量链，
其内部可以含$\gamma$矩阵和光子连接。第二项将两个同类端点交换一次，
故多一个负号；链内新增的偶矩阵不改变这个统计号。
端点置换确定的是同一基准下各图之间的相对号。整体相位继续沿
$b_1^\dagger d_2^\dagger|0\rangle$及同类粒子的既有福克排列，并可用
式[（58.25）](#eq:c58-born-current)固定。

将每幅图的外线、顶角、内线、指标缩并及相对统计号相乘，再对所有图求和，
得到连通散射振幅$i\mathcal T$：
<span id="eq:c58-amplitude-sum"></span>

$$
\begin{aligned}
\langle f|i\rangle_C
  &=(2\pi)^4\delta^4(P_f-P_i)\,i\mathcal T_{fi},\\
i\mathcal T_{fi}&=\sum_{\text{连通树图}}\mathcal A_{\rm graph}.
\end{aligned}
\tag{58.34}
$$

外态约化仍使用第45、56节的渐近通道与单位重叠条件。
每幅图已经包含式[（58.28）](#eq:c58-internal-rules)中的$i$，图求和以后不再另加一个$i$。

这些规则的符号还可以用纵向光子作一个代数检验。令
$\mathscr D(p)=\slashed p+m$，先取传播分母非零的动量；
克利福德关系给
$(\slashed p+m)(-\slashed p+m)=p^2+m^2$，于是
$\mathscr D(p)\widetilde S(p)=1$。取$q=p'-p$，则
<span id="eq:c58-longitudinal-identity"></span>

$$
\begin{aligned}
q_\mu\,ie\gamma^\mu
  &=ie[\mathscr D(p')-\mathscr D(p)],\\
\widetilde S(p')\slashed q\,\widetilde S(p)
  &=\widetilde S(p')\mathscr D(p')\widetilde S(p)
     -\widetilde S(p')\mathscr D(p)\widetilde S(p)\\
  &=\widetilde S(p)-\widetilde S(p'),\\
C_F(p')\,ie\slashed q\,C_F(p)
  &=e[C_F(p)-C_F(p')] .
\end{aligned}
\tag{58.35}
$$

最后一行用了$C_F=\widetilde S/i$，所以系数与顶角的正号相合。
把一个纵向光子依次接到同一条费米线的相邻位置时，右边的两项成对抵消，
只剩链的端点。电子外端满足$(\slashed p+m)u(p)=0$及
$\bar u(p')(\slashed p'+m)=0$；正电子端则满足
$(-\slashed p+m)v(p)=0$。这说明完整树图集合怎样消去外偏振中的规范方向。
最简单的一阶矩阵元直接给
$q_\mu\bar u(p')\gamma^\mu u(p)=(-m+m)\bar u(p')u(p)=0$，
与电子电流守恒相合。

上述恒等式先在非奇异动量处建立，再按共同真空处方取边界值。
若在中间保留传播子分母中的有限$\epsilon$、同时保持分子原样，则实际有
<span id="eq:c58-regulated-inverse"></span>

$$
\mathscr D(p)\widetilde S_\epsilon(p)
  =\frac{p^2+m^2}{p^2+m^2-i\epsilon}
  =1+\frac{i\epsilon}{p^2+m^2-i\epsilon}.
\tag{58.36}
$$

保留有限调节时可从共同调节的狄拉克算符及其逆核开始，沿第43节的次序取真空边界值。电磁相互作用的局域相位、传播子、
顶角和在壳旋量由此接在同一套约定上。

<span id="c58-discrete-transformations"></span>

## 电磁势与场强的离散变换

由电流的离散变换，可以确定电磁势应怎样变换，使完整拉格朗日量保持宇称、时间反演和电荷共轭对称性。先取不附加规范变换的势代表。

沿本节的电荷和度规约定，相互作用写成

<span id="eq:c58-ex-current-coupling"></span>

$$
\begin{aligned}
j^\mu(x)&=e:\bar\Psi(x)\gamma^\mu\Psi(x):,\qquad e<0,\\
A^\mu&=(A^0,\mathbf A),\qquad A_\mu=(-A^0,\mathbf A),\\
\mathcal L_{\rm int}&=j^\mu A_\mu=-\rho A^0+\mathbf j\cdot\mathbf A,
\qquad \rho=j^0.
\end{aligned}
\tag{58.37}
$$

冒号表示第40节所用的同一自由福克正规序。它使真空荷的减除与离散变换相容；
若把同点电流延拓为相互作用中的复合算符，也使用保持这些变换的共同调节与减除。
取 $x=(t,\mathbf x)$，并记

<span id="eq:c58-ex-coordinate-maps"></span>

$$
\begin{aligned}
\mathcal P&=\operatorname{diag}(1,-1,-1,-1),
&x_P&=\mathcal Px=(t,-\mathbf x),\\
\mathcal T&=\operatorname{diag}(-1,1,1,1),
&x_T&=\mathcal Tx=(-t,\mathbf x).
\end{aligned}
\tag{58.38}
$$

$P,C$是态空间的幺正算符，$T$是反幺正算符。
数值电荷共轭矩阵仍记作 $\mathcal C$，时间反演的旋量矩阵为
$B=\mathcal C\gamma_5$。在[第40节的双线性变换](/posts/srednicki-40/#c40-bilinears)中令数值矩阵为
$\gamma^\mu$，所需的矩阵恒等式为

<span id="eq:c58-ex-gamma-maps"></span>

$$
\begin{aligned}
\beta\gamma^0\beta&=\gamma^0,&
\beta\gamma^i\beta&=-\gamma^i,\\
B^{-1}(\gamma^0)^*B&=\gamma^0,&
B^{-1}(\gamma^i)^*B&=-\gamma^i,\\
\mathcal C^{-1}(\gamma^\mu)^T\mathcal C&=-\gamma^\mu.
\end{aligned}
\tag{58.39}
$$

宇称的场相位在双线性量中相消。把
$P^{-1}\Psi(x)P=i\beta\Psi(x_P)$ 和
$P^{-1}\bar\Psi(x)P=-i\bar\Psi(x_P)\beta$ 代入电流，便得到

<span id="eq:c58-ex-current-parity"></span>

$$
\begin{aligned}
P^{-1}j^\mu(x)P
&=e:\bar\Psi(x_P)\beta\gamma^\mu\beta\Psi(x_P):\\
&=\mathcal P^\mu{}_{\nu}j^\nu(x_P).
\end{aligned}
\tag{58.40}
$$

时间反演还要共轭数值矩阵，所以相应计算为

<span id="eq:c58-ex-current-time"></span>

$$
\begin{aligned}
T^{-1}j^\mu(x)T
&=e:\bar\Psi(x_T)B^{-1}(\gamma^\mu)^*B\Psi(x_T):\\
&=-\mathcal T^\mu{}_{\nu}j^\nu(x_T).
\end{aligned}
\tag{58.41}
$$

这里 $e$ 为实数，因而 $e^*=e$；但 $T^{-1}iT=-i$，
不能把作用于任意含 $i$ 的表达式的时间反演当成普通矩阵相似变换。
上两式都使电荷密度为偶、空间电流反向，坐标的反演位置则不同。

电荷共轭保持坐标不动，却交换带相反电荷的场。用
$C^{-1}\Psi C=\mathcal C\bar\Psi^T$ 和
$C^{-1}\bar\Psi C=\Psi^T\mathcal C$，先保持两个奇场的原次序，再在正规序内交换它们：

<span id="eq:c58-ex-current-charge"></span>

$$
\begin{aligned}
C^{-1}j^\mu C
&=e:\Psi^T\mathcal C\gamma^\mu\mathcal C\bar\Psi^T:\\
&=-e:\bar\Psi(\mathcal C\gamma^\mu\mathcal C)^T\Psi:\\
&=e:\bar\Psi\mathcal C^{-1}(\gamma^\mu)^T\mathcal C\Psi:
=-j^\mu.
\end{aligned}
\tag{58.42}
$$

第二行的负号来自交换一次奇场，第三行使用
$\mathcal C^T=\mathcal C^{-1}=-\mathcal C$。
同一正规序减除了未正规序交换所带的真空接触项。
$C$的幺正性意味着它既不共轭 $i$，也不把参数 $e$ 改成 $-e$。
实际反转的是电荷算符：由 $Q=e(N_b-N_d)$ 及 $C$交换 $b,d$，有
$C^{-1}QC=-Q$。

现在要求相互作用 $-\rho A^0+\mathbf j\cdot\mathbf A$ 在这三种变换下保持不变。
在宇称和时间反演下，$\rho$保持符号而 $\mathbf j$反向，故 $A^0$也须保持符号、
$\mathbf A$反向。电荷共轭使电流的四个分量都变号，势也须整体变号。
于是相应的规范代表为

<span id="eq:c58-ex-potential-transformations"></span>

$$
\begin{aligned}
P^{-1}A^\mu(x)P&=\mathcal P^\mu{}_{\nu}A^\nu(x_P),\\
T^{-1}A^\mu(x)T&=-\mathcal T^\mu{}_{\nu}A^\nu(x_T),\\
C^{-1}A^\mu(x)C&=-A^\mu(x).
\end{aligned}
\tag{58.43}
$$

例如宇称作用于耦合后，两个空间分量的负号相消；时间反演有同样的分量计算，
只需将 $x_P$换为 $x_T$。电荷共轭则使两个四矢量的负号相消：

<span id="eq:c58-ex-interaction-invariance"></span>

$$
\begin{aligned}
P^{-1}\mathcal L_{\rm int}(x)P
&=-\rho(x_P)A^0(x_P)
  +[-\mathbf j(x_P)]\cdot[-\mathbf A(x_P)]\\
&=\mathcal L_{\rm int}(x_P),\\
T^{-1}\mathcal L_{\rm int}(x)T&=\mathcal L_{\rm int}(x_T),\\
C^{-1}\mathcal L_{\rm int}(x)C&=(-j^\mu)(-A_\mu)
=\mathcal L_{\rm int}(x).
\end{aligned}
\tag{58.44}
$$

还应检查由势构成的麦克斯韦项。[第54节的场强约定](/posts/srednicki-54/#c54-tensor)给出

<span id="eq:c58-ex-field-definitions"></span>

$$
\begin{aligned}
E_i&=F^{0i}=-\partial_iA^0-\partial_t A_i,\\
B_i&=\epsilon_{ijk}\partial_jA_k,\qquad\epsilon_{123}=+1.
\end{aligned}
\tag{58.45}
$$

在宇称变换后的函数中，$\partial_i$作用于 $x_P$会产生一个负号，
而时间导数不变。以 $x'$表示变换后的自变量，逐项代入可得

<span id="eq:c58-ex-fields-parity"></span>

$$
\begin{aligned}
P^{-1}E_i(x)P
&=-\partial_i A^0(x_P)+\partial_t A_i(x_P)\\
&=\bigl[\partial'_i A^0+\partial'_{t}A_i\bigr]_{x'=x_P}
=-E_i(x_P),\\
P^{-1}B_i(x)P
&=-\epsilon_{ijk}\partial_jA_k(x_P)
=\epsilon_{ijk}\partial'_jA_k(x_P)
=B_i(x_P).
\end{aligned}
\tag{58.46}
$$

时间反演中恰好相反：空间导数不变，而 $\partial_t$作用于 $x_T$产生负号。
场强定义中的系数都是实数，反幺正性不再带来额外的数值共轭号。因此

<span id="eq:c58-ex-fields-time"></span>

$$
\begin{aligned}
T^{-1}E_i(x)T
&=-\partial_i A^0(x_T)+\partial_t A_i(x_T)\\
&=\bigl[-\partial'_i A^0-\partial'_{t}A_i\bigr]_{x'=x_T}
=E_i(x_T),\\
T^{-1}B_i(x)T
&=-\epsilon_{ijk}\partial_jA_k(x_T)
=-B_i(x_T).
\end{aligned}
\tag{58.47}
$$

电荷共轭不改变自变量，场强对势又是线性的，故

<span id="eq:c58-ex-fields-charge"></span>

$$
C^{-1}\mathbf E(x)C=-\mathbf E(x),\qquad
C^{-1}\mathbf B(x)C=-\mathbf B(x).
\tag{58.48}
$$

这些结果也给出熟悉的物理区别：电场在空间反演下是极矢量，磁场是轴矢量；
反转时间保持静电场，却反转由电流产生的磁场；把所有电荷换成相反电荷则同时
反转两种场。由于降低一个时间指标会带来负号，麦克斯韦项为

<span id="eq:c58-ex-maxwell-invariance"></span>

$$
\begin{aligned}
F^{\mu\nu}F_{\mu\nu}&=2(\mathbf B^2-\mathbf E^2),\\
\mathcal L_{\mathrm{EM}}
&=-\frac14F^{\mu\nu}F_{\mu\nu}
=\frac12(\mathbf E^2-\mathbf B^2).
\end{aligned}
\tag{58.49}
$$

三种变换都保持这两个平方，因而只把拉氏密度移到相应的 $x_P$、$x_T$或 $x$。
配合耦合项的结果和第40节的自由狄拉克变换，便得到完整作用量的对称性。

势本身仍有规范自由度。记 $R$为上述任一离散变换；在未固定规范时，
变换后的场还可作本节的联合规范变换

<span id="eq:c58-ex-gauge-representative"></span>

$$
\begin{aligned}
A_R^\mu&\longmapsto A_R^\mu-\partial^\mu\Lambda_R,
&\Psi_R&\longmapsto e^{-ie\Lambda_R}\Psi_R,\\
\delta F_R^{\mu\nu}
&=-(\partial^\mu\partial^\nu-\partial^\nu\partial^\mu)\Lambda_R=0.
\end{aligned}
\tag{58.50}
$$

这里 $\Lambda_R$是与边界条件相容的实函数。固定规范以后，只保留该规范允许的
补偿或残余变换。式[（58.43）](#eq:c58-ex-potential-transformations)选择 $\Lambda_R=0$；
它保持齐次库仑规范条件，也保持协变规范的平方项
$-(\partial_\mu A^\mu)^2/(2\xi)$：散度在 $P$下仅改坐标，
在 $T,C$下还变号，平方均不变。场强的三个变换不依赖这一规范代表选择。

<span id="c58-furry"></span>

## 费里定理

上面的变换表明，电荷共轭将每个光子场插入变成它的负值。
要据此求真空关联函数，还须选择实现这一对称性的真空。
以下取零外电磁背景的QED，令相互作用真空 $|\Omega\rangle$满足

<span id="eq:c58-ex-vacuum-assumption"></span>

$$
C|\Omega\rangle=e^{i\theta_C}|\Omega\rangle,
\qquad C^\dagger C=I.
\tag{58.51}
$$

规范固定、调节器和复合算符减除也取为与 $C$相容。
这使上面的场变换在量子理论中成立，并保证相互作用保持电荷共轭。

先直接考察时间序积。令 $A_r=A^{\mu_r}(x_r)$，
用 $\Theta_\pi$表示把置换 $\pi$中的时间排为降序的阶跃函数乘积。
所有光子场都是玻色场，时间排序不带费米交换号。由于 $C$不改变时间，
也不改变算符乘积的次序，可以在每一个已排序的乘积中逐个插入 $CC^{-1}$：

<span id="eq:c58-ex-ordered-charge"></span>

$$
\begin{aligned}
\mathrm T(A_1\cdots A_N)
&=\sum_{\pi\in S_N}\Theta_\pi
 A_{\pi(1)}\cdots A_{\pi(N)},\\
C^{-1}\mathrm T(A_1\cdots A_N)C
&=\sum_{\pi\in S_N}\Theta_\pi
 (C^{-1}A_{\pi(1)}C)\cdots(C^{-1}A_{\pi(N)}C)\\
&=(-1)^N\mathrm T(A_1\cdots A_N).
\end{aligned}
\tag{58.52}
$$

例如在时间互异处，$\Theta_\pi=\prod_{r=1}^{N-1}
\theta(x^0_{\pi(r)}-x^0_{\pi(r+1)})$。在重合位置，这个等式通过同一
$C$相容的调节及接触项定义延拓。这里 $C$为幺正，因而没有时间反演所需的
复共轭，也没有改变费曼边界值的 $i0$处方。

将式[（58.52）](#eq:c58-ex-ordered-charge)夹在真空之间，
式[（58.51）](#eq:c58-ex-vacuum-assumption)中的相位在左右两边抵消，得到

<span id="eq:c58-ex-odd-correlator"></span>

$$
\begin{aligned}
G_N^{\mu_1\cdots\mu_N}(x_1,\ldots,x_N)
&=\langle\Omega|\mathrm T(A_1\cdots A_N)|\Omega\rangle\\
&=\langle\Omega|C^{-1}\mathrm T(A_1\cdots A_N)C|\Omega\rangle\\
&=(-1)^N G_N^{\mu_1\cdots\mu_N}(x_1,\ldots,x_N).
\end{aligned}
\tag{58.53}
$$

因此奇数光子关联函数为零。其连通部分同样为零：零源归一的生成泛函满足
$Z[J]=Z[-J]$，故在 $J=0$附近的形式展开中，$-i\ln Z[J]$也只含偶数阶项。
[第56节的光子约化](/posts/srednicki-56/#c56-lsz)对每个入、出插入施加线性的偏振投影、
傅里叶积分和 $D_0=-\partial^2$。这些操作作用于零分布仍为零，
所以在该节所说明的光子渐近态和约化条件下，奇数条外光子线的连通幅为零。

还可以直接在散射态上看出这里的“奇数”为什么同时包括入射与出射光子。
将 $C^{-1}A_iC=-A_i$代入第56节的模式反解，
$C$不共轭其中的 $i$、偏振或平面波，因此两类渐近模式都满足

<span id="eq:c58-ex-photon-modes"></span>

$$
\begin{aligned}
C^{-1}a_{\lambda,{\rm in/out}}(\mathbf k)C
&=-a_{\lambda,{\rm in/out}}(\mathbf k),\\
C^{-1}a^\dagger_{\lambda,{\rm in/out}}(\mathbf k)C
&=-a^\dagger_{\lambda,{\rm in/out}}(\mathbf k).
\end{aligned}
\tag{58.54}
$$

电荷共轭不反转时间，也就不交换入、出标签。为写出 $S$矩阵，
把两组渐近态表示在同一个自由光子福克空间中，零光子态与
$|\Omega\rangle$相对应；以下 $|i\rangle,|f\rangle$均指这个共同表示中的态。
每个产生算符提供一个负号。若初态有 $N_i$个光子、末态有 $N_f$个光子，便有

<span id="eq:c58-ex-photon-state-parity"></span>

$$
\begin{aligned}
C|i\rangle&=e^{i\theta_C}(-1)^{N_i}|i\rangle,\\
C|f\rangle&=e^{i\theta_C}(-1)^{N_f}|f\rangle.
\end{aligned}
\tag{58.55}
$$

在同一个受调节理论中，电荷共轭保持相互作用哈密顿量。
由于 $C$为幺正，它也保持戴森展开中的 $-i$和时间排序，故
$C^{-1}SC=S$。于是完整散射矩阵元满足

<span id="eq:c58-ex-furry-selection"></span>

$$
\begin{aligned}
\mathcal A_{fi}=\langle f|S|i\rangle
&=\langle f|C^{-1}SC|i\rangle\\
&=\langle Cf|S|Ci\rangle
=(-1)^{N_f+N_i}\mathcal A_{fi},\\
N_f+N_i\ \text{为奇数}\quad&\Longrightarrow\quad\mathcal A_{fi}=0.
\end{aligned}
\tag{58.56}
$$

这就是费里定理（Furry's theorem）。外光子总数是 $N_i+N_f$；
完整矩阵元中的未散射内积也包括在上述证明内。
例如 $2\gamma\to3\gamma$共有五条外光子线，在这样的QED真空中其振幅为零。
若外态含电子或正电子，电荷共轭通常把它变成另一组散射态，所得关系便是
两个过程之间的关系。固定的带电介质或外电磁背景也会在 $C$下改变；
这时应比较相反背景中的响应，不能把这里的零背景选择律直接移用过去。

下一节用这些费曼规则计算电子正电子湮灭。

---

[← 第 57 节](/posts/srednicki-57/) · [章节地图](/srednicki/) · [第 59 节 →](/posts/srednicki-59/)
