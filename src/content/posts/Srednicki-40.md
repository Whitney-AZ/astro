---
title: 'Srednicki §40 宇称、时间反演与电荷共轭'
date: 2026-09-14
category: 笔记
tags: [物理, 量子场论, Srednicki]
series: 'Srednicki QFT'
srednickiSections: [40]
hideFromHome: true
draft: false
---

<span id="c40"></span>

[第 23 节](/posts/srednicki-23/#c23)给出了标量场的离散变换。旋量场还带有自旋指标，坐标反向时需要同时变换场的分量。将宇称、时间反演和电荷共轭作用于[第 39 节](/posts/srednicki-39/#c39)的粒子模式，再代回场展开，可以求出这些分量变换的矩阵，并据此判断双线性相互作用项的对称性。

模式相位沿用第 38 节，先取有质量的四分量狄拉克场；所选变换也保持马约拉纳条件。记$\mathcal P,\mathcal T$为坐标矩阵，$P,T,C$为态空间算符，$\mathcal C$为数值电荷共轭矩阵。

<span id="c40-parity"></span>

## 从宇称的模式相位求场矩阵

先回想连续洛伦兹变换的情形。与恒等变换相连的场矩阵由旋量生成元确定，其形式为

<span id="eq:c40-continuous"></span>

$$
\begin{gathered}
U(\Lambda)^{-1}\Psi(x)U(\Lambda)
=D(\Lambda)\Psi(\Lambda^{-1}x),\\
\Lambda^\mu{}_\nu=\delta^\mu{}_\nu+\delta\omega^\mu{}_\nu,\qquad
D(\Lambda)=I_4+\frac i2\delta\omega_{\mu\nu}S^{\mu\nu},\\
S^{\mu\nu}=\frac i4[\gamma^\mu,\gamma^\nu].
\end{gathered}
\tag{40.1}
$$

由于反对称参数的两个指标都求和，无穷小矩阵中带有$1/2$；这些生成元已在第36节用左右外尔块求出。宇称却不与恒等变换连续相连，无法通过选取这些连续参数得到，因此还要另行确定它的场矩阵。定义

<span id="eq:c40-parity-ansatz"></span>

$$
\mathcal P=\operatorname{diag}(1,-1,-1,-1)=\mathcal P^{-1},
\quad P=U(\mathcal P),\qquad
P^{-1}\Psi(x)P=D(\mathcal P)\Psi(\mathcal Px).
\tag{40.2}
$$

可以先考察接连作用两次宇称的结果。$P$为幺正算符，再次作用时数值矩阵可原样提出，因此

<span id="eq:c40-parity-square"></span>

$$
P^{-2}\Psi(x)P^2
=D(\mathcal P)P^{-1}\Psi(\mathcal Px)P
=D(\mathcal P)^2\Psi(x).
\tag{40.3}
$$

两次宇称的效果由此归结为场矩阵的平方。本节选择两次宇称后可观测量恢复原状：对厄米可观测标量，这要求场本身恢复；费米场的局部可观测量则含偶数个奇场，单个场同时取负仍使它们不变，所以也允许$D(\mathcal P)^2=-I_4$。这个负号对应费米宇称$(-1)^F$在奇场上的作用。若理论还有内部对称性，可以将宇称与内部变换组合，获得其他相位约定；以下选择狄拉克场和马约拉纳场共用的一套变换。

相位之外，模式的动量和自旋标签由生成元的变换决定。[第23节](/posts/srednicki-23/#c23)给出的关系为$P^{-1}\mathbf P P=-\mathbf P$、$P^{-1}\mathbf J P=\mathbf J$。动量反向而静止自旋轴不变，因而在不附加转动的标准推动基中，可以取

<span id="eq:c40-parity-modes"></span>

$$
\begin{aligned}
P^{-1}b_s^\dagger(\mathbf p)P&=\eta\,b_s^\dagger(-\mathbf p),\\
P^{-1}d_s^\dagger(\mathbf p)P&=\eta\,d_s^\dagger(-\mathbf p),
\qquad |\eta|=1.
\end{aligned}
\tag{40.4}
$$

这一选择可从静止系理解。宇称与所有转动对易，所以在不可约的自旋二分之一空间上只留下一个共同相位；再利用推动前后的动量反向关系，将它延伸到任意$\mathbf p$。对粒子和反粒子暂取相同的$\eta$，便使$d=b$在变换后仍成立。两次作用还要求$\eta^2=\pm1$，具体哪种相位与局部场变换相容，则要将它代回场展开来确定。为此写出场的模式展开：

<span id="eq:c40-expansion"></span>

$$
\Psi(x)=\sum_s\int\widetilde{dp}\,
\left[b_s(\mathbf p)u_s(\mathbf p)e^{ipx}
+d_s^\dagger(\mathbf p)v_s(\mathbf p)e^{-ipx}\right],
\qquad px=-\omega_{\mathbf p}t+\mathbf p\cdot\mathbf x.
\tag{40.5}
$$

先对[（40.4）](#eq:c40-parity-modes)第一行取伴随，湮灭算符的相位便为$\eta^*$。由于$P$幺正，$u,v$和傅里叶指数保持原样。接着令积分变量$\mathbf p\mapsto-\mathbf p$，将模式算符的动量重新写回原方向；$d^3p$的绝对雅可比行列式为1，$\omega_{\mathbf p}$也不变，因此测度保持不变。变换及换元的两步展开为

<span id="eq:c40-parity-expansion"></span>

$$
\begin{aligned}
P^{-1}\Psi(x)P
&=\sum_s\int\widetilde{dp}\,
\left[\eta^*b_s(-\mathbf p)u_s(\mathbf p)e^{ipx}
+\eta d_s^\dagger(-\mathbf p)v_s(\mathbf p)e^{-ipx}\right]\\
&=\sum_s\int\widetilde{dp}\,
\left[\eta^*b_s(\mathbf p)u_s(-\mathbf p)e^{ip\mathcal Px}
+\eta d_s^\dagger(\mathbf p)v_s(-\mathbf p)e^{-ip\mathcal Px}\right].
\end{aligned}
\tag{40.6}
$$

现在模式算符已有原来的动量标签，剩下的是把反向动量的旋量也写回原来的旋量基。[第38节的动量反向关系](/posts/srednicki-38/#c38-discrete)正适用于此处：

<span id="eq:c40-parity-spinors"></span>

$$
u_s(-\mathbf p)=\beta u_s(\mathbf p),\qquad
v_s(-\mathbf p)=-\beta v_s(\mathbf p),\qquad
\beta=\begin{pmatrix}0&I_2\\I_2&0\end{pmatrix}.
\tag{40.7}
$$

将这两式代入并提出$\beta$，两条频率支的系数分别成为$\eta^*$和$-\eta$。要用同一个局部矩阵变换完整的场，这两个系数必须相等，即$\eta^*=-\eta$。结合单位模条件，相位只能取$\pm i$；选择$\eta=-i$，便得到

<span id="eq:c40-parity-field"></span>

$$
P^{-1}\Psi(x)P=i\beta\Psi(\mathcal Px),\qquad
D(\mathcal P)=i\beta,\qquad D(\mathcal P)^2=-I_4.
\tag{40.8}
$$

另一选择$\eta=i$给出场矩阵$-i\beta$。共同相位的要求来自我们对狄拉克场和马约拉纳场的统一处理；若只讨论一般狄拉克场，也可给两类产生算符分别指定$\eta_b,\eta_d$。这时重复刚才的两频率匹配，得到

<span id="eq:c40-parity-general-phase"></span>

$$
D(\mathcal P)=a\beta,\qquad
a=\eta_b^*=-\eta_d,\qquad \eta_b\eta_d=-1.
\tag{40.9}
$$

例如$\eta_b=1,\eta_d=-1$对应$D(\mathcal P)=\beta$。共同的虚相位因此是本节为保持马约拉纳条件所作的选择，而粒子与反粒子的相位乘积始终为$-1$，与这一选择无关。这个不变的乘积直接决定了粒子反粒子对的内禀宇称。

<span id="c40-pair-parity"></span>

### 费米子对的宇称

为看清内禀宇称和轨道运动如何合在一起，考虑质心静止的双粒子态：

<span id="eq:c40-pair-state"></span>

$$
|\phi;s,s'\rangle
=\int\widetilde{dp}\,\phi(\mathbf p)
b_s^\dagger(\mathbf p)d_{s'}^\dagger(-\mathbf p)|0\rangle,
\qquad \phi(-\mathbf p)=(-1)^\ell\phi(\mathbf p).
\tag{40.10}
$$

最后一个条件表示相对运动有确定宇称。对给定相对轨道角动量$\ell$的波函数，将$\phi$展开为球谐函数后，这一条件来自$Y_{\ell m}(-\widehat{\mathbf p})=(-1)^\ell Y_{\ell m}(\widehat{\mathbf p})$。再取宇称不变的真空$P|0\rangle=P^{-1}|0\rangle=|0\rangle$，逐个变换产生算符并保持它们的原次序，得到

<span id="eq:c40-pair-parity"></span>

$$
\begin{aligned}
P^{-1}|\phi;s,s'\rangle
&=\eta_b\eta_d\int\widetilde{dp}\,\phi(\mathbf p)
b_s^\dagger(-\mathbf p)d_{s'}^\dagger(\mathbf p)|0\rangle\\
&=-\int\widetilde{dp}\,\phi(-\mathbf p)
b_s^\dagger(\mathbf p)d_{s'}^\dagger(-\mathbf p)|0\rangle\\
&=-(-1)^\ell|\phi;s,s'\rangle.
\end{aligned}
\tag{40.11}
$$

第二行将两个内禀相位的乘积写成负号，并换了积分变量；整个过程保持产生算符的原次序。因此费米子与反费米子的$S$波对子宇称为负，$P$波对子宇称为正；在宇称守恒的湮灭过程中，末态必须具有同样的总宇称。对同一马约拉纳粒子的对子，$\eta^2=-1$给出相同规则，同时轨道与自旋波函数还要合成全同费米子的反对称态：自旋单态反对称，允许偶$\ell$；自旋三重态对称，允许奇$\ell$。

对于两个电子，若也采用同一$\eta=-i$，则得到负的内禀相位乘积。同荷扇区的这个相位会随[（40.9）](#eq:c40-parity-general-phase)的约定改变；至于两电子不能直接湮灭为总电荷为零的末态，则由第39节的电荷守恒决定。

<span id="c40-parity-weyl"></span>

### 拆成两个外尔场

场矩阵还能说明宇称对手征性的作用。写成$\Psi=(\chi_a,\xi^{\dagger\dot a})^T$，由于$\beta$交换上下块，相应分量式为

<span id="eq:c40-parity-weyl"></span>

$$
P^{-1}\chi_a(x)P=i\xi^{\dagger\dot a}(\mathcal Px),\qquad
P^{-1}\xi^{\dagger\dot a}(x)P=i\chi_a(\mathcal Px).
\tag{40.12}
$$

两种指标的位置在这里由$\beta$的块映射对应。要写出其余两个带伴随的分量，先取厄米共轭，将$i$变成$-i$，再用反对称张量$\epsilon$升降指标。具体记$E=(\epsilon_{ab})$、$E^{-1}=-E$：第一式的伴随为$P^{-1}\chi^\dagger_{\rm down}P=-i\xi^{\rm up}$，左乘$E^{-1}$并用$(E^{-1})^2=-I_2$，右侧成为$+i\xi_{\rm down}$；第二式的伴随左乘$E$则给出$-iE\chi^\dagger_{\rm down}
=i\chi^{\dagger{\rm up}}$。升降指标的这个负号使两式恢复相同的相位，得到另两条分量变换：

<span id="eq:c40-parity-weyl-adjoint"></span>

$$
P^{-1}\chi^{\dagger\dot a}(x)P=i\xi_a(\mathcal Px),\qquad
P^{-1}\xi_a(x)P=i\chi^{\dagger\dot a}(\mathcal Px).
\tag{40.13}
$$

这些分量关系表明，宇称将左手场换成右手场，也将右手场换成左手场。若代入$\chi=\xi$，四式仍彼此相容，故所选宇称变换保持马约拉纳条件。

<span id="c40-time"></span>

## 时间反演中的复共轭与自旋反向

接着考虑时间坐标反向。同样先写出坐标变换和待定的场矩阵：

<span id="eq:c40-time-ansatz"></span>

$$
\mathcal T=\operatorname{diag}(-1,1,1,1)=\mathcal T^{-1},
\quad T=U(\mathcal T),\qquad
T^{-1}\Psi(x)T=D(\mathcal T)\Psi(\mathcal Tx).
\tag{40.14}
$$

态空间的实现$T$为反幺正算符，第23节已用正能谱解释了这一点。相应生成元关系为$T^{-1}\mathbf P T=-\mathbf P$、$T^{-1}\mathbf J T=-\mathbf J$。此时动量与自旋都反向，所以取模式变换

<span id="eq:c40-time-modes"></span>

$$
\begin{aligned}
T^{-1}b_s^\dagger(\mathbf p)T&=\zeta_s b_{-s}^\dagger(-\mathbf p),\\
T^{-1}d_s^\dagger(\mathbf p)T&=\zeta_s d_{-s}^\dagger(-\mathbf p),
\qquad |\zeta_s|=1.
\end{aligned}
\tag{40.15}
$$

由于自旋标签也发生变化，相位可以依赖$s$。取伴随后，湮灭算符仍带相位$\zeta_s^*$；此外，反幺正性还使数值旋量$u,v$逐分量取复共轭，并将$e^{\pm ipx}$变成$e^{\mp ipx}$，算符乘积的次序则保持不变。先实施这些操作，再同时换积分变量$\mathbf p\mapsto-\mathbf p$和求和变量$s\mapsto-s$，便得到

<span id="eq:c40-time-expansion"></span>

$$
\begin{aligned}
T^{-1}\Psi(x)T
&=\sum_s\int\widetilde{dp}\,
\left[\zeta_s^*b_{-s}(-\mathbf p)u_s^*(\mathbf p)e^{-ipx}
+\zeta_s d_{-s}^\dagger(-\mathbf p)v_s^*(\mathbf p)e^{ipx}\right]\\
&=\sum_s\int\widetilde{dp}\,
\left[\zeta_{-s}^*b_s(\mathbf p)u_{-s}^*(-\mathbf p)e^{ip\mathcal Tx}
+\zeta_{-s}d_s^\dagger(\mathbf p)v_{-s}^*(-\mathbf p)e^{-ip\mathcal Tx}\right].
\end{aligned}
\tag{40.16}
$$

这里坐标反向与指数共轭一起恢复了原来的两条频率支。例如第一项原有$e^{i\omega t-i\mathbf p\cdot\mathbf x}$，换变量后成为$e^{i\omega t+i\mathbf p\cdot\mathbf x}=e^{ip\mathcal Tx}$。接下来只需把复共轭旋量写回原基，这要用[第38节](/posts/srednicki-38/#c38-discrete)在固定静止相位下求得的关系：

<span id="eq:c40-time-spinors"></span>

$$
u_{-s}^*(-\mathbf p)=-sB u_s(\mathbf p),\qquad
v_{-s}^*(-\mathbf p)=-sB v_s(\mathbf p),\qquad B=\mathcal C\gamma_5.
\tag{40.17}
$$

选$\zeta_s=s$，则$\zeta_{-s}=-s$，每条频率支中的两个自旋因子相乘都给$(-s)^2=1$。于是可以提出同一个场矩阵：

<span id="eq:c40-time-field"></span>

$$
T^{-1}\Psi(x)T=B\Psi(\mathcal Tx),\qquad
B=\mathcal C\gamma_5
=\begin{pmatrix}-E&0\\0&-E\end{pmatrix}.
\tag{40.18}
$$

若取$\zeta_s=-s$，矩阵就相应变为$-B$。上式的显式块结构来自$\mathcal C=\operatorname{diag}(E,-E)$和$\gamma_5=\operatorname{diag}(-I_2,I_2)$。由于$E$为实反对称矩阵，且$E^2=-I_2$，可得$B^*=B$、$B^\dagger=-B=B^{-1}$。

现在再接连作用两次时间反演。第二次作用还要共轭第一次留下的数值矩阵或模式相位，因而有

<span id="eq:c40-time-square"></span>

$$
\begin{aligned}
T^{-2}\Psi(x)T^2
&=D(\mathcal T)^*D(\mathcal T)\Psi(x)=-\Psi(x),\\
T^{-2}b_s^\dagger(\mathbf p)T^2
&=\zeta_s^*\zeta_{-s}b_s^\dagger(\mathbf p)
=-b_s^\dagger(\mathbf p).
\end{aligned}
\tag{40.19}
$$

第一行的矩阵乘积已代入所选的$D(\mathcal T)=B$。一般情况下，第二次反幺正变换必须先共轭第一次留下的矩阵；这里$B$为实矩阵，才可将这一乘积简化为普通平方。两次$T$在一费米子态上给出负号，而在偶费米子可观测量上仍为正。这个平方号也不能用反幺正算符的整体相位消去，因为$(e^{i\alpha}T)^2=e^{i\alpha}e^{-i\alpha}T^2=T^2$。

<span id="c40-time-weyl"></span>

### 时间反演的外尔指标

将四分量式拆开时，$B$的上块为$E^{-1}$，作用于$\chi_{\rm down}$便将其升成$\chi^{\rm up}$；下块也为$E^{-1}$，但它作用的场已经是$\xi^{\dagger{\rm up}}$，再升一次就得到$-\xi^\dagger_{\rm down}$。这样，两个块分别给出

<span id="eq:c40-time-weyl"></span>

$$
T^{-1}\chi_a(x)T=\chi^a(\mathcal Tx),\qquad
T^{-1}\xi^{\dagger\dot a}(x)T=-\xi^\dagger_{\dot a}(\mathcal Tx).
\tag{40.20}
$$

其余两式仍由取伴随和升降指标得到。第一式取伴随后左乘$E^{-1}$，会出现$(E^{-1})^2=-I_2$；第二式取伴随后左乘$E$，再用$-E=E^{-1}$整理，便得到

<span id="eq:c40-time-weyl-adjoint"></span>

$$
T^{-1}\chi^{\dagger\dot a}(x)T=-\chi^\dagger_{\dot a}(\mathcal Tx),\qquad
T^{-1}\xi_a(x)T=\xi^a(\mathcal Tx).
\tag{40.21}
$$

时间反演在这套表示中保持每个外尔块的手征性，改变的是自旋分量及其$\epsilon$排列。取$\chi=\xi$时，两组关系仍一致，因此马约拉纳条件也在时间反演下保持。

<span id="c40-bilinears"></span>

## 双线性量的宇称和时间反演

确定场本身的变换以后，就可以研究它构成的相互作用项。常见的费米子部分形如$\bar\Psi A\Psi$，其中$A$为数值矩阵；为了组成厄米的拉格朗日量，先用第38节的矩阵伴随判断它的厄米性：

<span id="eq:c40-hermitian-bilinear"></span>

$$
(\bar\Psi A\Psi)^\dagger
=\Psi^\dagger A^\dagger\beta\Psi
=\bar\Psi\,\bar A\,\Psi,\qquad
\bar A=\beta A^\dagger\beta.
\tag{40.22}
$$

因此以下选取$\bar A=A$的矩阵。在已建立的克利福德矩阵中，$I_4,i\gamma_5,\gamma^\mu,\gamma^\mu\gamma_5,S^{\mu\nu}$都满足这个条件。例如$\overline{\gamma_5}=-\gamma_5$，赝标量要乘$i$才成为厄米量；而轴矢量中有$\overline{\gamma^\mu\gamma_5}=-\gamma_5\gamma^\mu=\gamma^\mu\gamma_5$，已经满足所需的伴随关系。

同一点的场乘积也需有确定含义：在经典作用量中，以下双线性量由格拉斯曼场相乘；在自由量子场中，则统一用福克正规序定义，公式中省去冒号。按照这一约定，交换两个奇场时可直接取负号。若使用未经减除的同点算符，第39节的CAR还会产生接触项；后面的电荷共轭计算将把这项写出。

<span id="c40-bilinear-parity"></span>

### 宇称

先对[（40.8）](#eq:c40-parity-field)取伴随，再右乘$\beta$，就能把场与伴随场的宇称变换合在一起：

<span id="eq:c40-bilinear-parity-map"></span>

$$
\begin{aligned}
P^{-1}\bar\Psi(x)P
&=(i\beta\Psi(\mathcal Px))^\dagger\beta
=-i\bar\Psi(\mathcal Px)\beta,\\
P^{-1}(\bar\Psi A\Psi)(x)P
&=\bar\Psi(\mathcal Px)\,\beta A\beta\,\Psi(\mathcal Px).
\end{aligned}
\tag{40.23}
$$

场与伴随场的相位相乘为$(-i)i=1$，所以双线性量的变换只取决于$\beta A\beta$。使用$\beta^2=I_4$、$\{\beta,\gamma^i\}=0$和$\{\beta,\gamma_5\}=0$逐项移动矩阵，六类矩阵的结果为

<span id="eq:c40-parity-matrices"></span>

$$
\begin{array}{c|rrrrrr}
A&I_4&i\gamma_5&\gamma^0&\gamma^i&\gamma^0\gamma_5&\gamma^i\gamma_5\\ \hline
\beta A\beta&I_4&-i\gamma_5&\gamma^0&-\gamma^i&
-\gamma^0\gamma_5&\gamma^i\gamma_5
\end{array}
\tag{40.24}
$$

最后一项移动$\gamma^0$时经过两次反交换，两个负号相消，所以轴矢量的空间部分保持正号。为使双线性量的名称与变换生成元区别开，记$\mathscr S=\bar\Psi\Psi$、$\mathscr P=\bar\Psi i\gamma_5\Psi$、$V^\mu=\bar\Psi\gamma^\mu\Psi$、$A_5^\mu=\bar\Psi\gamma^\mu\gamma_5\Psi$。将分量式合起来，得到四类双线性量的宇称变换：

<span id="eq:c40-parity-bilinears"></span>

$$
\begin{aligned}
P^{-1}\mathscr S(x)P&=\mathscr S(\mathcal Px),&
P^{-1}\mathscr P(x)P&=-\mathscr P(\mathcal Px),\\
P^{-1}V^\mu(x)P&=\mathcal P^\mu{}_\nu V^\nu(\mathcal Px),&
P^{-1}A_5^\mu(x)P&=-\mathcal P^\mu{}_\nu A_5^\nu(\mathcal Px).
\end{aligned}
\tag{40.25}
$$

这四类量分别称为标量、赝标量、矢量和轴矢量。矢量的时间分量不变、空间分量反号，与电荷密度和电流的变换相同；轴矢量的空间分量则保持不变，角动量就是这种例子。因此“轴矢量宇称为奇”说的是除几何指标矩阵$\mathcal P$外还有一个负号，实际各分量的符号仍由这两部分共同决定。

<span id="c40-bilinear-time"></span>

### 时间反演

求时间反演时同样先变换伴随场。$B$与$\beta$对易，且$B^\dagger=B^{-1}$，所以由[（40.18）](#eq:c40-time-field)得到

<span id="eq:c40-bilinear-time-map"></span>

$$
\begin{aligned}
T^{-1}\bar\Psi(x)T
&=\bar\Psi(\mathcal Tx)\beta B^\dagger\beta
=\bar\Psi(\mathcal Tx)B^{-1},\\
T^{-1}(\bar\Psi A\Psi)(x)T
&=\bar\Psi(\mathcal Tx)\,B^{-1}A^*B\,\Psi(\mathcal Tx),
\qquad B^{-1}=\gamma_5\mathcal C^{-1}.
\end{aligned}
\tag{40.26}
$$

其中$A^*$来自反幺正性，计算时要先处理这个复共轭。由$\mathcal C^{-1}\gamma^\mu\mathcal C=-(\gamma^\mu)^T$及$\mathcal C^2=-I_4$，得到$\mathcal C^{-1}(\gamma^\mu)^T\mathcal C=-\gamma^\mu$。又因为$(\gamma^0)^\dagger=\gamma^0$、$(\gamma^i)^\dagger=-\gamma^i$，所以$(\gamma^0)^*=(\gamma^0)^T$、$(\gamma^i)^*=-(\gamma^i)^T$。先将复共轭换成转置，再用电荷共轭矩阵的恒等式，就有

<span id="eq:c40-time-gamma"></span>

$$
\begin{aligned}
B^{-1}(\gamma^0)^*B
&=\gamma_5(-\gamma^0)\gamma_5=\gamma^0,\\
B^{-1}(\gamma^i)^*B
&=\gamma_5\gamma^i\gamma_5=-\gamma^i,\\
B^{-1}\gamma_5^*B&=\gamma_5.
\end{aligned}
\tag{40.27}
$$

最后一式使用了$\gamma_5$为实矩阵且与$\mathcal C$对易的性质。复共轭之后的相似变换保持矩阵乘法次序，因此可将刚才的结果用于乘积，得到

<span id="eq:c40-time-axial"></span>

$$
\begin{aligned}
B^{-1}(i\gamma_5)^*B&=-i\gamma_5,\\
B^{-1}(\gamma^0\gamma_5)^*B&=\gamma^0\gamma_5,\\
B^{-1}(\gamma^i\gamma_5)^*B&=-\gamma^i\gamma_5.
\end{aligned}
\tag{40.28}
$$

六个分量号由此确定。其中赝标量的负号来自$i^*=-i$，而非$\gamma_5$本身的变换。将这些分量式重新组成四维量，得到

<span id="eq:c40-time-bilinears"></span>

$$
\begin{aligned}
T^{-1}\mathscr S(x)T&=\mathscr S(\mathcal Tx),&
T^{-1}\mathscr P(x)T&=-\mathscr P(\mathcal Tx),\\
T^{-1}V^\mu(x)T&=-\mathcal T^\mu{}_\nu V^\nu(\mathcal Tx),&
T^{-1}A_5^\mu(x)T&=-\mathcal T^\mu{}_\nu A_5^\nu(\mathcal Tx).
\end{aligned}
\tag{40.29}
$$

可见时间反演使电荷密度保持不变、电流反向；轴矢量的空间分量也反向，正与自旋的时间反演相符。宇称下自旋不变，时间反演下自旋反向，这一物理区别也体现在两组轴矢量变换式中。

<span id="c40-charge"></span>

## 电荷共轭与费米场的换序

还要考察交换粒子与反粒子后的双线性量。数值旋量满足$\mathcal C\bar u_s^T=v_s$、$\mathcal C\bar v_s^T=u_s$，因此对场展开取狄拉克伴随、转置并乘$\mathcal C$，得到$\Psi^C=\sum_s\int\widetilde{dp}
[d_su_s e^{ipx}+b_s^\dagger v_s e^{-ipx}]$。它与原场的区别正是两套模式互换，所以选取幺正算符$C$交换$b$与$d$而不附加相位，便有

<span id="eq:c40-charge-field"></span>

$$
C^{-1}\Psi(x)C=\mathcal C\bar\Psi(x)^T,\qquad
C^{-1}\bar\Psi(x)C=\Psi(x)^T\mathcal C.
\tag{40.30}
$$

伴随场的第二式可从第一式直接得到。写出$\Psi^C=\mathcal C\beta\Psi^{\dagger T}$后，其狄拉克伴随为$\overline{\Psi^C}=\Psi^T\beta\mathcal C^\dagger\beta
=\Psi^T\mathcal C$，这里使用了$\beta\mathcal C=-\mathcal C\beta$。由于$C$幺正，双线性量中的数值矩阵$A$保持原样。将两个场的变换代入，并显式写出旋量指标，依次得到

<span id="eq:c40-charge-ordering"></span>

$$
\begin{aligned}
C^{-1}(\bar\Psi A\Psi)C
&=\Psi^T\mathcal C A\mathcal C\bar\Psi^T\\
&=\Psi_\alpha(\mathcal C A\mathcal C)_{\alpha\beta}\bar\Psi_\beta\\
&=-\bar\Psi_\beta
(\mathcal C A\mathcal C)_{\alpha\beta}\Psi_\alpha\\
&=-\bar\Psi\,\mathcal C^T A^T\mathcal C^T\Psi.
\end{aligned}
\tag{40.31}
$$

第三行交换一次奇场，产生负号；最后一行只是将同一个数值矩阵按转置后的指标次序重写。若使用未经正规序的等时算符，第三行还要加上$(\mathcal C A\mathcal C)_{\alpha\beta}
\{\Psi_\alpha,\bar\Psi_\beta\}
=(\mathcal C A\mathcal C)_{\alpha\beta}\beta_{\alpha\beta}\delta^3(\mathbf0)$。本节的正规序复合量已减去相应真空收缩，所以换序后恰为所写的第三行；自由真空在$C$下不变，也保证这一减除与电荷共轭相容。

接着使用$\mathcal C^T=\mathcal C^{-1}=-\mathcal C$整理两边的共轭矩阵，便将双线性量的变换化为

<span id="eq:c40-charge-map"></span>

$$
C^{-1}(\bar\Psi A\Psi)(x)C
=\bar\Psi(x)\,\mathcal C^{-1}A^T\mathcal C\,\Psi(x).
\tag{40.32}
$$

与时间反演相比，这里出现的是转置：它反转矩阵乘积的次序，却保持数值$i$不变。利用$\gamma_5^T=\gamma_5$及其与$\mathcal C$的对易性，逐项计算可得

<span id="eq:c40-charge-matrices"></span>

$$
\begin{aligned}
\mathcal C^{-1}I_4^T\mathcal C&=I_4,&
\mathcal C^{-1}(i\gamma_5)^T\mathcal C&=i\gamma_5,\\
\mathcal C^{-1}(\gamma^\mu)^T\mathcal C&=-\gamma^\mu,&
\mathcal C^{-1}(\gamma^\mu\gamma_5)^T\mathcal C
&=\gamma_5(-\gamma^\mu)=\gamma^\mu\gamma_5.
\end{aligned}
\tag{40.33}
$$

最后一项先因转置成为$\gamma_5^T(\gamma^\mu)^T$，再反交换一次恢复原顺序，所以轴矢量得到正号。于是四类双线性量的电荷共轭性质为

<span id="eq:c40-charge-bilinears"></span>

$$
C^{-1}\mathscr S C=\mathscr S,\qquad
C^{-1}\mathscr P C=\mathscr P,\qquad
C^{-1}V^\mu C=-V^\mu,\qquad
C^{-1}A_5^\mu C=A_5^\mu.
\tag{40.34}
$$

矢量流为奇，正好对应$b^\dagger$与$d^\dagger$交换后电荷反号。对马约拉纳场则有$\Psi^C=\Psi$、$\overline{\Psi^C}=\bar\Psi$，任何由同一个场构成的双线性量都在此$C$实现下不变。矢量双线性量又必须满足[（40.34）](#eq:c40-charge-bilinears)的奇变换，两个条件合起来要求

<span id="eq:c40-majorana-vector"></span>

$$
\bar\Psi_M\gamma^\mu\Psi_M=0.
\tag{40.35}
$$

这个零结果也可从场的代数直接看出。第36节已知$(\mathcal C\gamma^\mu)^T
=\mathcal C\gamma^\mu$为对称矩阵，而$\bar\Psi_M\gamma^\mu\Psi_M
=\Psi_M^T\mathcal C\gamma^\mu\Psi_M$中的两个奇场相同；交换它们并重命名指标，表达式成为自身的负值。因此同一马约拉纳场没有前章狄拉克荷所对应的矢量流。若双线性量的两端属于不同马约拉纳种类，交换场时也交换了种类，混合矢量便不必为零。

<span id="c40-tensors"></span>

## 张量与赝张量

记

$$
F^{\mu\nu}=\bar\Psi S^{\mu\nu}\Psi,\qquad
\widetilde F^{\mu\nu}=\bar\Psi iS^{\mu\nu}\gamma_5\Psi,\qquad
S^{\mu\nu}=\frac i4[\gamma^\mu,\gamma^\nu].


$$

两者在$\mu,\nu$下均反对称。第38节的$\bar S=S$和$\bar\gamma_5=-\gamma_5$给
$\overline{iS\gamma_5}=i\gamma_5S=iS\gamma_5$，
其中$\gamma_5$通过两枚$\gamma$矩阵，故与$S$对易。
因此两个量均厄米，并沿正文使用格拉斯曼乘积或同一个正规序复合量定义。

宇称的矩阵规则为$A\mapsto\beta A\beta$。
把单位矩阵$\beta^2$插在两枚$\gamma$之间，便有

$$
\begin{aligned}
\beta S^{\mu\nu}\beta
&=\frac i4[\beta\gamma^\mu\beta,\beta\gamma^\nu\beta]
=\mathcal P^\mu{}_\rho\mathcal P^\nu{}_\sigma S^{\rho\sigma},\\
\beta(iS^{\mu\nu}\gamma_5)\beta
&=-\mathcal P^\mu{}_\rho\mathcal P^\nu{}_\sigma
iS^{\rho\sigma}\gamma_5.
\end{aligned}


$$

第二行另用$\beta\gamma_5\beta=-\gamma_5$。
所以$F^{0i}$在宇称下反号、$F^{ij}$不变，赝张量则相反；
这给出它们的几何张量与赝张量性质。

时间反演规则为$A\mapsto B^{-1}A^*B$。
[（40.27）](#eq:c40-time-gamma)可合写成$B^{-1}(\gamma^\mu)^*B=-\mathcal T^\mu{}_\rho\gamma^\rho$。
现在生成元中的$i$也要共轭，所以

$$
\begin{aligned}
B^{-1}(S^{\mu\nu})^*B
&=-\frac i4
[B^{-1}(\gamma^\mu)^*B,B^{-1}(\gamma^\nu)^*B]\\
&=-\mathcal T^\mu{}_\rho\mathcal T^\nu{}_\sigma S^{\rho\sigma},\\
B^{-1}(iS^{\mu\nu}\gamma_5)^*B
&=(-i)\left[-\mathcal T^\mu{}_\rho\mathcal T^\nu{}_\sigma
S^{\rho\sigma}\right]\gamma_5\\
&=\mathcal T^\mu{}_\rho\mathcal T^\nu{}_\sigma
iS^{\rho\sigma}\gamma_5.
\end{aligned}


$$

第二种量有两个$i$，反幺正共轭在这一步产生两个负号。
于是$F^{0i}$为时间反演偶、$F^{ij}$为奇；赝张量的分量号相反。

电荷共轭使用转置，数值$i$不变，但
$[\gamma^\mu,\gamma^\nu]^T
=-[(\gamma^\mu)^T,(\gamma^\nu)^T]$。
代入$\mathcal C^{-1}(\gamma^\mu)^T\mathcal C=-\gamma^\mu$，

$$
\begin{aligned}
\mathcal C^{-1}(S^{\mu\nu})^T\mathcal C
&=-\frac i4[-\gamma^\mu,-\gamma^\nu]=-S^{\mu\nu},\\
\mathcal C^{-1}(iS^{\mu\nu}\gamma_5)^T\mathcal C
&=i(\mathcal C^{-1}\gamma_5^T\mathcal C)
(\mathcal C^{-1}(S^{\mu\nu})^T\mathcal C)\\
&=-i\gamma_5S^{\mu\nu}=-iS^{\mu\nu}\gamma_5.
\end{aligned}


$$

因此两个双线性量都为$C$奇。各项结果可以写成一张表；
其中每个变换后的场取相应的$\mathcal Px,\mathcal Tx,x$，
几何矩阵的两个指标分别作用于原来的$\mu,\nu$：

| 双线性量                | $P$                                                                      | $T$                                                                      | $C$                      |
| ----------------------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------ |
| $F^{\mu\nu}$            | $+\mathcal P^\mu{}_\rho\mathcal P^\nu{}_\sigma F^{\rho\sigma}$           | $-\mathcal T^\mu{}_\rho\mathcal T^\nu{}_\sigma F^{\rho\sigma}$           | $-F^{\mu\nu}$            |
| $\widetilde F^{\mu\nu}$ | $-\mathcal P^\mu{}_\rho\mathcal P^\nu{}_\sigma\widetilde F^{\rho\sigma}$ | $+\mathcal T^\mu{}_\rho\mathcal T^\nu{}_\sigma\widetilde F^{\rho\sigma}$ | $-\widetilde F^{\mu\nu}$ |

两种量的三个额外符号相乘都为正，再用每个指标上的$\mathcal P\mathcal T=-I$，
得到

$$
\Theta^{-1}F^{\mu\nu}(x)\Theta=F^{\mu\nu}(-x),\qquad
\Theta^{-1}\widetilde F^{\mu\nu}(x)\Theta=\widetilde F^{\mu\nu}(-x).


$$

两个量都有两个矢量指标，因而均为CPT偶。
最后令$\Psi=\Psi_M$为同一个马约拉纳场。
场本身在所选$C$下不变，两个双线性量却都为$C$奇，因此它们都为零。
也可由刚才的电荷共轭矩阵式得到$A^T\mathcal C=-\mathcal C A$，故
$(\mathcal C A)^T=-A^T\mathcal C=\mathcal C A$；
用这个对称矩阵缩并$\Psi_M^T$与$\Psi_M$，
与[（40.35）](#eq:c40-majorana-vector)一样在交换后等于自身的负值。
对不同马约拉纳种类$i,j$，相应关系只给
$\bar\Psi_i A\Psi_j=-\bar\Psi_j A\Psi_i$，
并不要求每个非对角种类分量为零。

<span id="c40-cpt"></span>

## CPT及有导数的局部项

最后把三个变换组合起来，记$\Theta=CPT$，它仍为反幺正算符。依次组合[（40.25）](#eq:c40-parity-bilinears)、[（40.29）](#eq:c40-time-bilinears)、[（40.34）](#eq:c40-charge-bilinears)，并使用$\mathcal P^\mu{}_\nu\mathcal T^\nu{}_\rho=-\delta^\mu{}_\rho$，得到

<span id="eq:c40-cpt-four"></span>

$$
\begin{aligned}
\Theta^{-1}\mathscr S(x)\Theta&=\mathscr S(-x),&
\Theta^{-1}\mathscr P(x)\Theta&=\mathscr P(-x),\\
\Theta^{-1}V^\mu(x)\Theta&=-V^\mu(-x),&
\Theta^{-1}A_5^\mu(x)\Theta&=-A_5^\mu(-x).
\end{aligned}
\tag{40.36}
$$

例如矢量的额外$C$号与$T$号相消，剩下$\mathcal P\mathcal T=-I_4$；轴矢量的额外$P$号与$T$号也相消，留下同一个负矩阵。因此在CPT下，标量和赝标量具有相同的号，矢量和轴矢量也具有相同的号。刚才求出的反对称张量和赝张量在CPT下均为偶。这样，变换号与矢量指标数的奇偶性联系起来。

要把这一规律用于一般双线性量，先要说明这些类型已经穷尽四分量矩阵的可能性。所需的完备基为

<span id="eq:c40-clifford-basis"></span>

$$
I_4,\quad i\gamma_5,\quad
\gamma^\mu,\quad\gamma^\mu\gamma_5,\quad
S^{\mu\nu}\quad(\mu<\nu).
\tag{40.37}
$$

按上下$2\times2$块展开，就能看清它们如何张成任意矩阵。$I_4,\gamma_5$的组合给出上下块各自的单位矩阵，再利用

$$
S^{ij}=\frac12\epsilon^{ijk}
\begin{pmatrix}\sigma_k&0\\0&\sigma_k\end{pmatrix},\qquad
S^{i0}=\frac i2
\begin{pmatrix}\sigma_i&0\\0&-\sigma_i\end{pmatrix},
$$

可分别选出上下块的三个泡利矩阵，共得到八个对角块基。$\gamma^\mu$与$\gamma^\mu\gamma_5$的和、差则分别留下上右块或下左块，每块都含$(I_2,\boldsymbol\sigma)$的四个独立矩阵，又给出八个基。这16个矩阵线性独立，张成全部$4\times4$复矩阵；赝张量也能用上述对角块展开，不再增加独立基。因此一般双线性量都可分解为这些标量、矢量和张量类型。

<span id="c40-cpt-derivatives"></span>

### 先保留两个场的位置

还须把[（40.36）](#eq:c40-cpt-four)推广到含导数项。导数在时空反向下变号，此外还要跟踪它作用于哪一个场，以及显式$i$的变换。为同时保留这些信息，先把两个场放在不同点，再求局部极限。由[（40.8）](#eq:c40-parity-field)、[（40.18）](#eq:c40-time-field)、[（40.30）](#eq:c40-charge-field)组合得到$\Theta^{-1}\Psi(x)\Theta=-i\gamma_5\Psi^{\dagger T}(-x)$；其中$P$所给的$-i$在最后一次$T$作用时变成$+i$，再用$\mathcal C\beta\mathcal C=\beta$及$\beta\gamma_5\beta=-\gamma_5$，便得到这个总号。取伴随后还有$\Theta^{-1}\bar\Psi(x)\Theta=i\Psi^T(-x)\gamma_5\beta$。将两式用于$B_A(x,y)=:\bar\Psi(x)A\Psi(y):$，得到

<span id="eq:c40-cpt-bilocal"></span>

$$
\begin{aligned}
\Theta^{-1}B_A(x,y)\Theta
&=:\Psi^T(-x)\gamma_5\beta A^*\gamma_5\Psi^{\dagger T}(-y):\\
&=-:\Psi^\dagger(-y)\gamma_5 A^\dagger\beta\gamma_5\Psi(-x):\\
&=:\bar\Psi(-y)\gamma_5\bar A\gamma_5\Psi(-x):.
\end{aligned}
\tag{40.38}
$$

第二行交换两个奇场并转置中间矩阵；第三行先代入$\Psi^\dagger=\bar\Psi\beta$，再用$\beta\gamma_5=-\gamma_5\beta$抵消换序的负号。若$A$为[（40.37）](#eq:c40-clifford-basis)中带$n$个矢量指标的基矩阵，则$\gamma_5\bar A\gamma_5=(-1)^n\bar A$。另一方面，$B_A(-x,-y)^\dagger
=:\bar\Psi(-y)\bar A\Psi(-x):$，因此[（40.38）](#eq:c40-cpt-bilocal)正是$(-1)^n B_A(-x,-y)^\dagger$。位置互换已经包含在整个双线性量的厄米共轭中，后面求导时可以沿用这一对应。

现在令$r$个导数作用于第一个位置，$s$个导数作用于第二个位置，最后才取$x=y=z$。将这两串导数略记为$\partial_x^{(r)}\partial_y^{(s)}$，定义$Q_A(z)=[\partial_x^{(r)}\partial_y^{(s)}B_A(x,y)]_{x=y=z}$。对[（40.38）](#eq:c40-cpt-bilocal)两边求导，每次坐标反向都由链式法则给出一个负号，于是

<span id="eq:c40-cpt-derivative-monomial"></span>

$$
\Theta^{-1}Q_A(z)\Theta
=(-1)^{n+r+s}Q_A^\dagger(-z).
\tag{40.39}
$$

右边的厄米共轭既包含矩阵伴随，也把每串导数放到原来相应的伴随场上，所以导数位置的信息仍然保留。取一般厄米组合$O=cQ_A+c^*Q_A^\dagger$时，还须变换系数。反幺正性给出$\Theta^{-1}c\Theta=c^*$，故

<span id="eq:c40-cpt-hermitian"></span>

$$
\Theta^{-1}O(z)\Theta
=(-1)^{n+r+s}
\left[c^*Q_A^\dagger(-z)+cQ_A(-z)\right]
=(-1)^{n+r+s}O(-z).
\tag{40.40}
$$

指标计数规律由此适用于厄米量：中间的非厄米项与其伴随配对后，系数的复共轭正好使整个组合恢复原状，只留下指标数决定的符号。作为含导数的例子，定义

<span id="eq:c40-derivative-example"></span>

$$
K^{\mu\nu}
=\frac i2\bar\Psi\gamma^\mu\overleftrightarrow{\partial^\nu}\Psi
=\frac i2\left[
\bar\Psi\gamma^\mu\partial^\nu\Psi
-(\partial^\nu\bar\Psi)\gamma^\mu\Psi\right].
\tag{40.41}
$$

方括号内两项互为伴随，它们的差为反厄米量。在[（40.39）](#eq:c40-cpt-derivative-monomial)中取$n=1,r+s=1$，括号变成其伴随，即原括号的负值；外面的$i$又被反幺正变换取负，两者相消。因而$K^{\mu\nu}(x)\mapsto K^{\mu\nu}(-x)$，正符合二阶张量的CPT规律。

<span id="c40-cpt-action"></span>

### 从局部项到作用量

要讨论完整的拉格朗日量，还需加入玻色场。对标量和矢量场，可以选择相应的离散相位，使组合变换为

<span id="eq:c40-cpt-bosons"></span>

$$
\Theta^{-1}\phi(x)\Theta=\phi^\dagger(-x),\qquad
\Theta^{-1}A^\mu(x)\Theta=-A^{\mu\dagger}(-x).
\tag{40.42}
$$

标量沿第23节[（23.35）](/posts/srednicki-23/#eq:c23-charge-preserving-time)取保持荷的$T_q$实现，并选$P^{-1}\phi(x)P=\phi(\mathcal Px)$、$C^{-1}\phi C=\phi^\dagger$，三者组合便得[（40.42）](#eq:c40-cpt-bosons)第一式。矢量在这里作为带一个洛伦兹指标的玻色场使用；厄米实场可去掉伴随符号，复场则同时变换到共轭种类，各阶导数继续按链式法则处理。

局部项若含偶数个旋量，可先将它们两两配对，再用[（40.37）](#eq:c40-clifford-basis)分解。不同种类的配对也满足[（40.38）](#eq:c40-cpt-bilocal)，因为右边的厄米共轭同时交换两端的种类。对不含狄拉克伴随的配对，用$\bar\Psi^{\,C}=\Psi^T\mathcal C$可改写成同样的双线性形式；由$\Psi^C=\mathcal C\beta\Psi^{\dagger T}$及$\mathcal C\beta\gamma_5=-\gamma_5\mathcal C\beta$，可见$\Psi^C$也服从同一个$\Theta$场变换，这种改写因而保持所得规则。在经典格拉斯曼多项式中，或同一个完整正规序的量子单项式中，交换两个偶配对须作四次奇场交换，总号为正。所以多个配对与玻色因子的乘积也服从[（40.39）](#eq:c40-cpt-derivative-monomial)的总指标计数，其任意厄米组合再按[（40.40）](#eq:c40-cpt-hermitian)变换。

洛伦兹标量最后将所有指标缩并。度规每次消去两个指标，$\epsilon$每次消去四个指标，都不改变总数的奇偶性；$\epsilon$在全时空反向下也带四个负号。因此，由这些场、有限阶导数和常数系数组成的局部厄米洛伦兹标量满足

<span id="eq:c40-cpt-action"></span>

$$
\Theta^{-1}\mathcal L(x)\Theta=\mathcal L(-x),\qquad
\Theta^{-1}S\Theta
=\int d^4x\,\mathcal L(-x)
=\int d^4y\,\mathcal L(y)=S.
\tag{40.43}
$$

最后一步令$y=-x$，四维积分的绝对雅可比行列式为1，便从局部拉氏量的变换得到作用量不变。上述局部厄米洛伦兹标量的作用量因而保持CPT。

以自由狄拉克作用量为例，先将动能写为$i\bar\Psi\gamma^\mu\overleftrightarrow{\partial_\mu}\Psi/2$。它与原来的$i\bar\Psi\gamma^\mu\partial_\mu\Psi$相差$i\partial_\mu(\bar\Psi\gamma^\mu\Psi)/2$，在所取边界条件下积分为零。前者是[（40.41）](#eq:c40-derivative-example)的缩并，质量项则是[（40.36）](#eq:c40-cpt-four)的标量，因此两项均保持CPT。实标量耦合$g\phi\bar\Psi\Psi$也为偶；在四维，由$[\phi]=1$、$[\Psi]=3/2$可得$[g]=0$。若$\phi$在$P,T$下都为偶，实系数的$\phi\bar\Psi i\gamma_5\Psi$却破坏单独的$P$和$T$，而这两次负号在CPT中相消。这个例子说明，组合对称性可以在单独的离散对称性破坏时仍然成立。

在满足维特曼条件的量子场论中，这一结论还有算符形式：场是正定希尔伯特空间上的协变算符值缓增分布，具有共同不变稠密定义域和循环的庞加莱不变真空；能动量谱位于闭未来光锥内，场满足与自旋相应的类空局域性。由此存在保持真空的反幺正 CPT 算符，将场变到时空反向后的共轭场。这里不要求$C,P,T$各自都是对称性。

解析证明利用正能谱建立真空关联函数的管域解析性，再借复洛伦兹变换实现$x\mapsto-x$；类空局域性允许在约斯特点反转场序，厄米共轭给出所需的反幺正变换。证明见 [Greenberg，_Why is CPT fundamental?_，第 3–5 节](https://arxiv.org/pdf/hep-ph/0309309v1#page=6)。该文采用$(+,-,-,-)$度规，因而其中$e^{-iq\cdot x_{\rm G}}$对应本节的$e^{iq\cdot x}$。

---

[← 第 39 节](/posts/srednicki-39/) · [章节地图](/srednicki/) · [第 41 节 →](/posts/srednicki-41/)
