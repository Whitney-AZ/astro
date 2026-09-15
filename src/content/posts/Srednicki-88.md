---
title: 'Srednicki §88 标准模型：轻子部分'
date: 2026-09-14
category: 笔记
tags: [物理, 量子场论, Srednicki]
series: 'Srednicki QFT'
srednickiSections: [88]
hideFromHome: true
draft: false
---

<span id="c88"></span>

上一节确定了电弱规范场和Higgs场的相互作用。现在加入轻子。电子、缪子和陶子各有一个相应的中微子；三组粒子的电荷与弱相互作用相同，带电粒子的质量却不同。我们先研究其中一组，看看规范对称性如何决定它的相互作用，再把结果推广到三代。这样得到的理论既能描述轻子与$W$、$Z$的耦合，也能在低能极限下给出熟悉的费米弱相互作用。

<span id="c88-fields"></span>

## 一代轻子的规范表示与质量

轻子不带颜色，因此只需写出它们在$SU(2)\times U(1)$下的表示。一代轻子的独立左手Weyl场为
<span id="eq:c88-left-fields"></span>

$$
\ell_i\sim(\mathbf2,-\tfrac12),\qquad
\bar e\sim(\mathbf1,+1),\qquad
\ell=\begin{pmatrix}\nu\\e\end{pmatrix}.
\tag{88.1}
$$

这里$\bar e$是一个场的名字，横线不表示$e$的复共轭。它与$e$是独立的左手场，随后将由$e$和$\bar e^\dagger$组成描述电子的狄拉克场。暂时保留这种两分量记法，是因为规范变换对每个左手场的作用最容易从表示读出。

对双重态取$T^a=\sigma^a/2$，协变导数及动能便为
<span id="eq:c88-kinetic"></span>

$$
\begin{aligned}
(D_\mu\ell)_i
 &=\partial_\mu\ell_i-ig_2A_\mu^a(T^a)_i{}^j\ell_j
   +\frac{i g_1}{2}B_\mu\ell_i,\\
D_\mu\bar e&=\partial_\mu\bar e-i g_1B_\mu\bar e,\\
\mathcal L_{\rm kin}
 &=i\ell^{\dagger i}\bar\sigma^\mu(D_\mu\ell)_i
   +i\bar e^\dagger\bar\sigma^\mu D_\mu\bar e.
\end{aligned}
\tag{88.2}
$$

双重态和单态承担不同的弱表示；作空间反射把左手场变成右手场时，这些表示不能彼此配成同一种规范多重态。这正是本模型的手征性，其具体表现将是$W$只耦合到电子的左手分量。

一个不含导数的Weyl质量项必须把两个左手场缩并成洛伦兹标量，同时也成为规范单态。可供选择的三个表示乘积是
<span id="eq:c88-mass-forbidden"></span>

$$
\begin{aligned}
(\mathbf2,-\tfrac12)\otimes(\mathbf2,-\tfrac12)
 &=(\mathbf1,-1)\oplus(\mathbf3,-1),\\
(\mathbf2,-\tfrac12)\otimes(\mathbf1,+1)
 &=(\mathbf2,+\tfrac12),\\
(\mathbf1,+1)\otimes(\mathbf1,+1)
 &=(\mathbf1,+2).
\end{aligned}
\tag{88.3}
$$

第一种乘积虽然含$SU(2)$单态，其超荷却不是零；其余两种也不含$(\mathbf1,0)$。所以规范对称性禁止裸的轻子质量。Higgs场参与后，可以构造一个新的规范单态。

上一节的Higgs双重态$\varphi$处于$(\mathbf2,-1/2)$。它与$\ell$的超荷之和是$-1$，恰好被$\bar e$的超荷抵消；两个双重态用反对称张量缩并，就得到
<span id="eq:c88-yukawa-invariant"></span>

$$
\begin{aligned}
(\mathbf2,-\tfrac12)\otimes(\mathbf2,-\tfrac12)
 \otimes(\mathbf1,+1)
 &=(\mathbf1,0)\oplus(\mathbf3,0),\\
\mathcal L_{\rm Yuk}
 &=-y\epsilon^{ij}\varphi_i\ell_j\bar e
   -y^*(\epsilon^{ij}\varphi_i\ell_j\bar e)^\dagger .
\end{aligned}
\tag{88.4}
$$

内部指标取$\epsilon^{12}=+1$，两个Weyl场的旋量指标则按第35节的约定缩并。因为$[\varphi]=1$、$[\ell]=[\bar e]=3/2$，这个项的量纲正好是4，$y$为无量纲的汤川耦合。

还可以证明，这些项已经穷尽了所取场内容的可重整相互作用。洛伦兹标量必须含偶数个旋量因子。含四个或更多费米场的局域算符至少具有量纲6；含两个费米场的量纲已是3，因此在量纲不超过4时，只能再乘一个标量，或加一个导数，也可以什么都不加。最后一种已经被式[（88.3）](#eq:c88-mass-forbidden)排除。一个导数必须与左场及其共轭组成的矢量双线性收缩，给出的正是式[（88.2）](#eq:c88-kinetic)；裸的$A_\mu$不能单独产生另一项规范不变量，而是按协变导数的固定系数组合进去。对于含一个标量的项，两个左场的超荷依次为$-1,+1/2,+2$；乘超荷$-1/2$的$\varphi$或超荷$+1/2$的$\varphi^\dagger$，只有$\ell\bar e\varphi$的总超荷为零。它在弱群下也只有一个反对称单态缩并。加上厄米共轭后，式[（88.4）](#eq:c88-yukawa-invariant)因此就是唯一的这类相互作用。两费米场乘场强的项已有量纲5，不在这里采用的可重整化拉格朗日量内。

选取幺正规范$\varphi=(v+H,0)^T/\sqrt2$，则$\epsilon^{ij}\varphi_i\ell_j=(v+H)e/\sqrt2$。若起初$y=|y|e^{i\delta}$，作恒定重定义$\bar e_{\rm old}=e^{-i\delta}\bar e_{\rm new}$，动能不变，汤川耦合变成$|y|$。以下已作这一相位选择，并仍以$y\ge0$记它。于是
<span id="eq:c88-yukawa-unitary"></span>

$$
\mathcal L_{\rm Yuk}
 =-\frac{y}{\sqrt2}(v+H)(e\bar e+\bar e^\dagger e^\dagger).
\tag{88.5}
$$

按照[狄拉克场的两Weyl组成](/posts/srednicki-36/#c36-two-weyl)，定义
<span id="eq:c88-electron-dirac"></span>

$$
\mathcal E=\begin{pmatrix}e\\\bar e^\dagger\end{pmatrix},\qquad
\bar{\mathcal E}\mathcal E=e\bar e+\bar e^\dagger e^\dagger,
\qquad m_e=\frac{yv}{\sqrt2}.
\tag{88.6}
$$

电子的自由项与Higgs耦合随即写成
<span id="eq:c88-electron-higgs"></span>

$$
\mathcal L_{e,H}
 =i\bar{\mathcal E}\slashed\partial\mathcal E
   -m_e\bar{\mathcal E}\mathcal E
   -\frac{m_e}{v}H\bar{\mathcal E}\mathcal E .
\tag{88.7}
$$

这里动能的两分量展开包含$i\bar e\sigma^\mu\partial_\mu\bar e^\dagger$；分部积分后，再将两个奇场交换次序，就恢复$i\bar e^\dagger\bar\sigma^\mu\partial_\mu\bar e$。两种写法的作用量只相差边界项。质量项说明电子的质量来自Higgs真空值，而最后一项又把电子与物理Higgs的耦合固定为$m_e/v$。场$e$与数值耦合$e>0$使用同一字母；四分量场改写成$\mathcal E$以后，两者也就容易区分。

汤川项没有给$\nu$留下质量。对于这一无质量左Weyl场，可以定义马约拉纳四分量记法，也可以只显示它的左块：
<span id="eq:c88-neutrino-embedding"></span>

$$
\begin{aligned}
\mathcal N&=\begin{pmatrix}\nu\\\nu^\dagger\end{pmatrix},\qquad
\mathcal N_L=P_L\mathcal N=\begin{pmatrix}\nu\\0\end{pmatrix},
\qquad P_L=\frac{1-\gamma_5}{2},\\
i\bar{\mathcal N}_L\slashed\partial\mathcal N_L
 &=i\nu^\dagger\bar\sigma^\mu\partial_\mu\nu .
\end{aligned}
\tag{88.8}
$$

$\mathcal N_L$的四个位置中只有两个独立分量，所以这种写法仍描述原来的左Weyl场。它使中微子流可以与电子流采用同一套$\gamma$矩阵运算。

下表沿用中译本的三代轻子质量；中微子的零质量则属于本节没有独立右中微子、只保留可重整算符的模型。

| 轻子                | 质量（MeV） | 电荷（以正$e$为单位） |
| ------------------- | ----------: | --------------------: |
| 电子$e$             |     $0.511$ |                  $-1$ |
| 电子中微子$\nu_e$   |         $0$ |                   $0$ |
| 缪子$\mu$           |     $105.7$ |                  $-1$ |
| 缪子中微子$\nu_\mu$ |         $0$ |                   $0$ |
| 陶子$\tau$          |      $1777$ |                  $-1$ |
| 陶中微子$\nu_\tau$  |         $0$ |                   $0$ |

<span id="c88-currents"></span>

## 从协变导数到带电流和中性流

为了读出与物理规范场的耦合，把式[（88.2）](#eq:c88-kinetic)中的$A^a,B$换成上一节的$W^\pm,Z,A$。其中带电部分直接给出
<span id="eq:c88-charged-connection"></span>

$$
g_2(A_\mu^1T^1+A_\mu^2T^2)
 =\frac{g_2}{\sqrt2}
 \begin{pmatrix}0&W_\mu^+\\W_\mu^-&0\end{pmatrix}.
\tag{88.9}
$$

它将双重态的上下分量互换，所以$W$顶角把电子与中微子相连。单态$\bar e$没有这样的顶角。

对中性部分使用$A^3=c_WZ+s_WA$、$B=-s_WZ+c_WA$，以及$e=g_2s_W=g_1c_W>0$，有
<span id="eq:c88-neutral-connection"></span>

$$
\begin{aligned}
g_2A_\mu^3T^3+g_1B_\mu Y
 &=eA_\mu(T^3+Y)
   +eZ_\mu\left(\frac{c_W}{s_W}T^3-\frac{s_W}{c_W}Y\right)\\
 &=eA_\mu Q+\frac{e}{s_Wc_W}Z_\mu(T^3-s_W^2Q),
 \qquad Q=T^3+Y .
\end{aligned}
\tag{88.10}
$$

第二行把$Y=Q-T^3$代入，$T^3$的系数于是成为$(c_W^2+s_W^2)/(s_Wc_W)$。光子前面的生成元$Q$就给出电荷，而$Z$还区分弱同位旋。

在原来的三个左手场上，这些生成元的本征值分别是
<span id="eq:c88-left-charges"></span>

$$
\begin{array}{c|rrr}
 &\nu&e&\bar e\\ \hline
T^3&+\tfrac12&-\tfrac12&0\\
Y&-\tfrac12&-\tfrac12&+1\\
Q&0&-1&+1
\end{array}.
\tag{88.11}
$$

从这里转成电子的四分量记法时，要对右块$\bar e^\dagger$取共轭表示：它的超荷是$-1$，不是$\bar e$的$+1$。因此作用于$\mathcal E$的生成元为
<span id="eq:c88-dirac-charges"></span>

$$
T^3_{\mathcal E}=-\frac12P_L,\qquad
Y_{\mathcal E}=-\frac12P_L-P_R,\qquad
Q_{\mathcal E}=-P_L-P_R=-I_4.
\tag{88.12}
$$

电子的左右分量有相同电荷，光子耦合是纯矢量的；它们的弱同位旋不同，$Z$耦合则含手征投影。具体地，电子与中微子的中性连接为
<span id="eq:c88-physical-connections"></span>

$$
\begin{aligned}
C_\mu^{\mathcal E}
 &=-eA_\mu+\frac{e}{s_Wc_W}Z_\mu
       \left(-\frac12P_L+s_W^2\right),\\
C_\mu^{\mathcal N_L}
 &=\frac{e}{2s_Wc_W}Z_\mu .
\end{aligned}
\tag{88.13}
$$

特别是电子没有右手带电弱流，中微子没有光子顶角。

动能$i\bar\Psi\gamma^\mu(\partial_\mu-iC_\mu)\Psi$中的相互作用带正号，因为$i(-i)=+1$。把系数相同的项合在一起，得到
<span id="eq:c88-lepton-currents"></span>

$$
\begin{aligned}
\mathcal L_{\rm gauge,lep}
 &=\frac{g_2}{\sqrt2}(W_\mu^+J^{\mu-}+W_\mu^-J^{\mu+})
   +\frac{e}{s_Wc_W}Z_\mu J_Z^\mu+eA_\mu J_{\rm EM}^\mu,\\
J^{\mu+}&=\bar{\mathcal E}_L\gamma^\mu\mathcal N_L,
\qquad J^{\mu-}=\bar{\mathcal N}_L\gamma^\mu\mathcal E_L,\\
J_3^\mu&=\frac12\bar{\mathcal N}_L\gamma^\mu\mathcal N_L
        -\frac12\bar{\mathcal E}_L\gamma^\mu\mathcal E_L,\\
J_{\rm EM}^\mu&=-\bar{\mathcal E}\gamma^\mu\mathcal E,
\qquad J_Z^\mu=J_3^\mu-s_W^2J_{\rm EM}^\mu .
\end{aligned}
\tag{88.14}
$$

这里$\bar{\mathcal E}_L=\bar{\mathcal E}P_R$，且$P_R\gamma^\mu=\gamma^\mu P_L$，所以把左投影放到两个端点或只放到$\gamma$矩阵右侧是等价的。$J^+$和$J^-$互为厄米共轭，分别同$W^-$、$W^+$配对；电磁流前的负号给出电子的物理电荷$-e$。

<span id="c88-fermi"></span>

## 低能极限与费米常数

在远低于$M_W,M_Z$的动量转移下，重矢量传播只跨越很短的距离。若保留树级耦合的最低阶，同时展开外部不变量与重质量平方之比，就可以用局域四费米相互作用表示单个$W$或$Z$的交换。忽略重场动能后的相关拉格朗日量为
<span id="eq:c88-heavy-current-action"></span>

$$
\begin{aligned}
\mathcal L_{\rm heavy}
={}&-M_W^2W_\mu^+W^{\mu-}-\frac12M_Z^2Z_\mu Z^\mu\\
&+c\,(W_\mu^+J^{\mu-}+W_\mu^-J^{\mu+})+d\,Z_\mu J_Z^\mu,
\qquad c=\frac{g_2}{\sqrt2},\quad d=\frac{e}{s_Wc_W}.
\end{aligned}
\tag{88.15}
$$

因为各流都是两个奇场的乘积，它们彼此作偶量运算。配方可将重场依赖完全收进平方：
<span id="eq:c88-heavy-completing-square"></span>

$$
\begin{aligned}
\mathcal L_{\rm heavy}
={}&-M_W^2\left(W_\mu^+-\frac{c}{M_W^2}J_\mu^+\right)
             \left(W^{\mu-}-\frac{c}{M_W^2}J^{\mu-}\right)\\
&-\frac{M_Z^2}{2}\left(Z_\mu-\frac{d}{M_Z^2}J_{Z\mu}\right)
                  \left(Z^\mu-\frac{d}{M_Z^2}J_Z^\mu\right)\\
&+\frac{c^2}{M_W^2}J_\mu^+J^{\mu-}
 +\frac{d^2}{2M_Z^2}J_{Z\mu}J_Z^\mu .
\end{aligned}
\tag{88.16}
$$

对$W^\pm,Z$变分所得的代数方程正是令两个平方中的括号为零。代回后剩下最后一行；中性场是实场，质量项中的$1/2$也因此留在它的有效作用系数里。

利用$M_Z=M_W/c_W$及$e=g_2s_W$，两个系数相同。使用上一节定义的费米常数，有
<span id="eq:c88-fermi-matching"></span>

$$
\begin{aligned}
G_F&=\frac{g_2^2}{4\sqrt2M_W^2}
    =\frac{1}{\sqrt2v^2},\\
\mathcal L_{\rm eff}
 &=\frac{g_2^2}{2M_W^2}J_\mu^+J^{\mu-}
   +\frac{e^2}{2s_W^2c_W^2M_Z^2}J_{Z\mu}J_Z^\mu\\
 &=2\sqrt2G_F\left(J_\mu^+J^{\mu-}+J_{Z\mu}J_Z^\mu\right).
\end{aligned}
\tag{88.17}
$$

也可以直接从树图看出符号：每个规范顶角含$ic$，实际内部线的低能首项为$-ig_{\mu\nu}/M_W^2$，故两个顶角和一条线的乘积给$+ic^2g_{\mu\nu}/M_W^2$，与$i\mathcal L_{\rm eff}$一致。传播函数$\Delta\simeq g/M_W^2$还须除以$i$才是内部线因子。

略去的重场动能会产生带两个额外导数的算符，其系数为$g^2/M_V^4$，对这里振幅的相对修正为外部不变量除以$M_V^2$；圈图则属于更高的耦合阶数。由于$[G_F]=-2$，一个能标$E$下的无量纲弱振幅含有$G_FE^2$，这也说明了低能弱作用的抑制从何而来。中微子与电子的散射可同时检验式[（88.17）](#eq:c88-fermi-matching)中的带电流和中性流；这里先计算缪子衰变。

<span id="c88-generations"></span>

## 三代质量基

为恢复三个轻子族，给$\ell$和$\bar e$增加代指标$I=1,2,3$。规范场不作用于代空间，所以动能仍是代对角的，而汤川耦合可以把两种场的任意两代相连：
<span id="eq:c88-three-generation-action"></span>

$$
\begin{aligned}
\mathcal L_{\rm kin}
 &=\sum_I\left[i\ell_I^\dagger\bar\sigma^\mu D_\mu\ell_I
        +i\bar e_I^\dagger\bar\sigma^\mu D_\mu\bar e_I\right],\\
\mathcal L_{\rm Yuk}
 &=-\sum_{I,J}y_{IJ}\epsilon^{ij}\varphi_i\ell_{jI}\bar e_J
   +\mathrm{h.c.}
\end{aligned}
\tag{88.18}
$$

$y$是一般复$3\times3$矩阵。选择怎样的代基只是一种场变量的选择；问题是能否在保持动能标准归一的同时，将质量项化为对角。

将旧场与新场的关系明确写为
<span id="eq:c88-generation-rotations"></span>

$$
\ell_{iI}=L_{IJ}\ell'_{iJ},\qquad
\bar e_I=\bar E_{IJ}\bar e'_J,
\qquad L^\dagger L=\bar E^\dagger\bar E=I_3.
\tag{88.19}
$$

由于规范协变导数在代空间与这两个恒定矩阵对易，动能中的系数分别化为$L^\dagger L$和$\bar E^\dagger\bar E$。汤川项却含两个未共轭左场，因此它的系数为
<span id="eq:c88-yukawa-transformation"></span>

$$
\sum_{I,J}y_{IJ}L_{IK}\bar E_{JL}
 =(L^Ty\bar E)_{KL}.
\tag{88.20}
$$

两个左手场均未共轭，故第一矩阵以$L^T$出现。

具体构造这两个旋转，可先对正半定厄米矩阵$y^\dagger y$取正交归一本征基$v_I$，本征值记为$d_I^2\ge0$。对$d_I>0$，令$u_I=yv_I/d_I$；它们满足
<span id="eq:c88-singular-vectors"></span>

$$
u_I^\dagger u_J
 =\frac{v_I^\dagger y^\dagger yv_J}{d_Id_J}=\delta_{IJ},
\qquad yv_I=d_Iu_I.
\tag{88.21}
$$

对于零本征值，$yv_I=0$，再把已有$u_I$补成整个空间的正交归一基即可。以$U,V$分别收集$u_I,v_I$，便得到奇异值分解$y=UdV^\dagger$。取
<span id="eq:c88-yukawa-diagonal"></span>

$$
L=U^*,\qquad\bar E=V,
\qquad L^Ty\bar E=U^\dagger yV=d
 =\operatorname{diag}(d_1,d_2,d_3).
\tag{88.22}
$$

这样质量项与Higgs耦合同时对角化，三个带电轻子质量为$m_I=d_Iv/\sqrt2$。零奇异值对应无质量带电轻子，满秩$y$则给三个正质量。

同一个$L$同时旋转双重态的中微子和带电左场，故带电流中的代系数也是$L^\dagger L=I_3$。中性流同理保持对角。由于本模型的中微子尚无质量项，没有另一套质量对角化条件迫使它们采用不同的左旋转。因此我们可以把三个质量本征态依次命名为电子、缪子和陶子，并把与它们相连的中微子命名为$\nu_e,\nu_\mu,\nu_\tau$。三代流就是式[（88.14）](#eq:c88-lepton-currents)逐代求和。

这里构造的是标准模型的轻子扇区。它与第75节的量子规范一致性条件相容，要靠上一节同时列出的夸克参加反常相消。例如一代左轻子的$Y^3$与$SU(2)^2Y$系数分别为
<span id="eq:c88-lepton-anomaly"></span>

$$
2(-\tfrac12)^3+1^3=\frac34,\qquad
(-\tfrac12)T(\mathbf2)=-\frac14.
\tag{88.23}
$$

三色夸克给出$3[2(1/6)^3+(-2/3)^3+(1/3)^3]=-3/4$和$3(1/6)T(\mathbf2)=+1/4$，恰好抵消；两部分的超荷和也分别为零。每代还有三个夸克双重态加一个轻子双重态，共四个，满足[第75节的整体$SU(2)$条件](/posts/srednicki-75/#c75-global)。因此本节的轻子作用量与夸克部分共同组成规范反常相消的标准模型。

<span id="c88-muon"></span>

## 缪子衰变与费尔兹变换

现在考虑$\mu^-\to e^-\bar\nu_e\nu_\mu$。记电子、缪子的狄拉克场为$\mathcal E,\mathcal M$，相应中微子的左手四分量场为$\mathcal N_{eL},\mathcal N_{\mu L}$。对这个过程，只需保留带电流中的两代：
<span id="eq:c88-two-family-currents"></span>

$$
\begin{aligned}
J^{\mu+}
 &=\bar{\mathcal E}_L\gamma^\mu\mathcal N_{eL}
   +\bar{\mathcal M}_L\gamma^\mu\mathcal N_{\mu L},\\
J^{\mu-}
 &=\bar{\mathcal N}_{eL}\gamma^\mu\mathcal E_L
   +\bar{\mathcal N}_{\mu L}\gamma^\mu\mathcal M_L .
\end{aligned}
\tag{88.24}
$$

中性流在质量基中不改变代，因而不能把一个缪子变成一个电子。带电流乘积却含有所需的交叉项：
<span id="eq:c88-muon-operator"></span>

$$
\mathcal L_{\mu\to e}
 =2\sqrt2G_F
 (\bar{\mathcal E}\gamma^\mu P_L\mathcal N_e)
 (\bar{\mathcal N}_\mu\gamma_\mu P_L\mathcal M).
\tag{88.25}
$$

完整有效作用中还含它的厄米共轭；它们分别提供相应的共轭通道。只取一个交叉项并不使式[（88.25）](#eq:c88-muon-operator)的系数再乘2。

<figure>
  <img src="/images/srednicki/88-muon.svg" alt="缪子经虚 W 玻色子衰变为电子和两个中微子" style="width: min(100%, 680px); height: auto;" loading="lazy" />
</figure>

图中入射缪子的动量为$p_1$，出射$\nu_\mu,\bar\nu_e,e^-$的动量依次为$p'_1,p'_2,p'_3$。内部$W$携带$q=p_1-p'_1=p'_2+p'_3$；低能近似把两顶点之间的传播收缩成式[（88.25）](#eq:c88-muon-operator)的局域顶点。实线箭头表示费米子流向，因此出射反中微子的箭头与其物理动量相反。

先把两个矢量流改写成两个标量双线性，这会使后面的自旋迹很短。所需的费尔兹变换（Fierz transformation）可以直接由Pauli矩阵的完备性得到。将任意$2\times2$矩阵展开为单位矩阵与三个Pauli矩阵，并用$\operatorname{tr}(\sigma_i\sigma_j)=2\delta_{ij}$取出系数，得到分量恒等式
<span id="eq:c88-pauli-kernel"></span>

$$
\begin{aligned}
\sum_{i=1}^3(\sigma_i)_{ab}(\sigma_i)_{cd}
 &=2\delta_{ad}\delta_{bc}-\delta_{ab}\delta_{cd},\\
\sum_{\mu=0}^3\eta_\mu(\bar\sigma^\mu)_{ab}(\bar\sigma^\mu)_{cd}
 &=2(\delta_{ad}\delta_{bc}-\delta_{ab}\delta_{cd})
 =-2U_{ac}U_{bd},
\end{aligned}
\tag{88.26}
$$

其中$\eta=(-1,1,1,1)$、$\bar\sigma^\mu=(I,-\boldsymbol\sigma)$，$U=\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)$是上指标旋量反对称张量的数值矩阵。时间分量的负号与三个空间分量相加，恰好产生第二行中的第二个$-\delta_{ab}\delta_{cd}$。

把第二行乘到四个奇场上。原来的分量次序是$\chi_1^\dagger\chi_2\chi_3^\dagger\chi_4$；将$\chi_2$移过$\chi_3^\dagger$，给出一个负号。再用既定的缩并次序$\chi_2\chi_4=-\chi_2^TU\chi_4$，可逐步写成
<span id="eq:c88-weyl-fierz"></span>

$$
\begin{aligned}
(\chi_1^\dagger\bar\sigma^\mu\chi_2)
(\chi_3^\dagger\bar\sigma_\mu\chi_4)
 &=-2U_{ac}U_{bd}
   \chi_{1a}^\dagger\chi_{2b}\chi_{3c}^\dagger\chi_{4d}\\
 &=2(\chi_1^\dagger U\chi_3^{\dagger T})
      (\chi_2^TU\chi_4)\\
 &=-2(\chi_1^\dagger\chi_3^\dagger)(\chi_2\chi_4).
\end{aligned}
\tag{88.27}
$$

两套分量指标在此只按矩阵位置列出；最后一行恢复第35节的无指标旋量缩并。这给出了所需的四奇场重排恒等式。

对于左分量为$\chi_i$的四分量场，$\Psi^C=\mathcal C\bar\Psi^T$、$\mathcal C=\operatorname{diag}(-U,U)$给出$\bar\Psi_1P_R\Psi_3^C=\chi_1^\dagger U\chi_3^{\dagger T}$，以及$\overline{\Psi_4^C}P_L\Psi_2=\chi_4^T(-U)\chi_2=\chi_2\chi_4$。最后一个等号同时使用反对称矩阵与奇场交换。因而
<span id="eq:c88-dirac-fierz"></span>

$$
(\bar\Psi_1\gamma^\mu P_L\Psi_2)
(\bar\Psi_3\gamma_\mu P_L\Psi_4)
 =-2(\bar\Psi_1P_R\Psi_3^C)
       (\overline{\Psi_4^C}P_L\Psi_2).
\tag{88.28}
$$

依次取$(\Psi_1,\Psi_2,\Psi_3,\Psi_4)=(\mathcal E,\mathcal N_e,\mathcal N_\mu,\mathcal M)$，两个标量双线性是偶量，可互换位置，于是式[（88.25）](#eq:c88-muon-operator)化为两个标量双线性的乘积：
<span id="eq:c88-muon-scalar-operator"></span>

$$
\mathcal L_{\mu\to e}
 =-4\sqrt2G_F
 (\overline{\mathcal M^C}P_L\mathcal N_e)
 (\bar{\mathcal E}P_R\mathcal N_\mu^C).
\tag{88.29}
$$

这里$\overline{\mathcal M^C}$是电荷共轭场的狄拉克伴随，而不是未取伴随的列。

<span id="c88-spin-sum"></span>

## 振幅的端点次序和自旋求和

采用第11节的$S$矩阵约定，连通项为$(2\pi)^4\delta^4(p_f-p_i)i\mathcal T$。为了固定费米外态的共同相位，取
<span id="eq:c88-fock-order"></span>

$$
\begin{aligned}
|i\rangle&=b_\mu^\dagger(p_1)|0\rangle,\\
|f\rangle&=b_e^\dagger(p'_3)d_{\nu_e}^\dagger(p'_2)
             b_{\nu_\mu}^\dagger(p'_1)|0\rangle .
\end{aligned}
\tag{88.30}
$$

将式[（88.25）](#eq:c88-muon-operator)展开成产生湮灭算符后，所需的模次序就是$b_e^\dagger d_{\nu_e}^\dagger b_{\nu_\mu}^\dagger b_\mu$，与此末态相匹配。因此直接的两个流振幅为
<span id="eq:c88-direct-amplitude"></span>

$$
\mathcal T
 =2\sqrt2G_F
 [\bar u_3'\gamma^\mu P_Lv_2']
 [\bar u_1'\gamma_\mu P_Lu_1].
\tag{88.31}
$$

采用标量算符时，相应的模次序是$b_\mu d_{\nu_e}^\dagger b_e^\dagger b_{\nu_\mu}^\dagger$。把$b_\mu$移到最右边需三次交换，再把两个最左产生算符换成式[（88.30）](#eq:c88-fock-order)的次序需一次交换，总号仍为正。所以两个场算符表达式给出相同的外态相位。

也可直接对普通复数外旋量验证这一点。令$a,b,c,d$分别为$u_1,u'_3,u'_1,v'_2$的左块。由式[（88.26）](#eq:c88-pauli-kernel)，以及数值旋量之间的可交换性，有
<span id="eq:c88-external-fierz"></span>

$$
\begin{aligned}
V&=(\bar u_3'\gamma^\mu P_Lv_2')
   (\bar u_1'\gamma_\mu P_Lu_1)
   =2(a^TUd)(b^\dagger Uc^*),\\
S&=(u_1^T\mathcal CP_Lv_2')
   (\bar u_3'P_R\mathcal C\bar u_1^{\prime T})
   =-(a^TUd)(b^\dagger Uc^*),\qquad V=-2S .
\end{aligned}
\tag{88.32}
$$

这个负号取决于写出的电荷共轭端点次序：对普通列有$a^T(-U)d=-d^T(-U)a$。式[（88.30）](#eq:c88-fock-order)固定的场次序使两种表达式具有同一个共同相位。

按第38节的相位取$v_1=\mathcal C\bar u_1^T$、$v'_1=\mathcal C\bar u_1^{\prime T}$，并用$\bar v_1=u_1^T\mathcal C$，同一个衰变振幅便可写成
<span id="eq:c88-scalar-amplitude"></span>

$$
\begin{aligned}
\mathcal T
 &=-4\sqrt2G_F
  (u_1^T\mathcal CP_Lv_2')
  (\bar u_3'P_R\mathcal C\bar u_1^{\prime T})\\
 &=-4\sqrt2G_F(\bar v_1P_Lv_2')(\bar u_3'P_Rv_1').
\end{aligned}
\tag{88.33}
$$

$v_1$和$v'_1$是在这条矩阵链中重新表示入射缪子和出射缪子中微子的电荷共轭列；图中的实际粒子和动量保持式[（88.30）](#eq:c88-fock-order)的指定。

求复共轭时，矩阵乘积次序反转。对于任何数值矩阵$A$，有$(\bar uAv)^*=\bar v\,\bar A u$，其中$\bar A=\beta A^\dagger\beta$。由于$\beta\gamma_5\beta=-\gamma_5$，$\overline{P_L}=P_R$、$\overline{P_R}=P_L$，故
<span id="eq:c88-conjugate-amplitude"></span>

$$
\mathcal T^*
 =-4\sqrt2G_F(\bar v_2'P_Rv_1)(\bar v_1'P_Lu_3').
\tag{88.34}
$$

电子自旋和中微子的实际末态均须求和，初态缪子的两个自旋则作平均。采用$\sum_su_s\bar u_s=-\slashed p+m$、$\sum_sv_s\bar v_s=-\slashed p-m$，得到
<span id="eq:c88-two-traces"></span>

$$
\begin{aligned}
\langle|\mathcal T|^2\rangle
={}&16G_F^2\,
 \operatorname{tr}\!\left[
 (-\slashed p_1-m_\mu)P_L(-\slashed p'_2)P_R\right]\\
&\times\operatorname{tr}\!\left[
 (-\slashed p'_3+m_e)P_R(-\slashed p'_1)P_L\right].
\end{aligned}
\tag{88.35}
$$

系数$16=(4\sqrt2)^2/2$已含初态平均。形式上可以在中微子的四分量完备式中求和两个旋量标签，因为端点的$P_L,P_R$自行投去不参与此左Weyl场的另一支；没有另一个末态平均因子。

现在利用$P_L\slashed p=\slashed pP_R$。第一条迹中的两个动量负号相乘为正，质量项只有一个$\gamma$矩阵而为零；其余部分是$\operatorname{tr}(\slashed p_1\slashed p'_2P_R)$。含$\gamma_5$的两$\gamma$迹为零，无$\gamma_5$的一半迹则为$-2p_1\cdot p'_2$。第二条同样计算：
<span id="eq:c88-traces-evaluated"></span>

$$
\begin{aligned}
\operatorname{tr}[(-\slashed p_1-m_\mu)P_L(-\slashed p'_2)P_R]
 &=\frac12\operatorname{tr}(\slashed p_1\slashed p'_2)
 =-2p_1\cdot p'_2,\\
\operatorname{tr}[(-\slashed p'_3+m_e)P_R(-\slashed p'_1)P_L]
 &=\frac12\operatorname{tr}(\slashed p'_3\slashed p'_1)
 =-2p'_1\cdot p'_3 .
\end{aligned}
\tag{88.36}
$$

这里使用$\{\gamma^\mu,\gamma^\nu\}=-2g^{\mu\nu}$，所以每条两$\gamma$迹带负内积。将它们相乘，便得到自旋平均模平方：
<span id="eq:c88-amplitude-squared"></span>

$$
\boxed{\langle|\mathcal T|^2\rangle
 =64G_F^2(p_1\cdot p'_2)(p'_1\cdot p'_3).}
\tag{88.37}
$$

未来指向的这些动量在$(-+++)$度规下给出非正的两个内积，因此模平方非负。电子质量虽在迹中显式消失，仍通过$p_3^{\prime2}=-m_e^2$影响运动学和积分区域。先用两条矢量流直接复算这个结果，再进行相空间积分。

<span id="c88-direct-traces"></span>

## 直接计算两条矢量流的迹

保留式[（88.31）](#eq:c88-direct-amplitude)的两流形式，令$P=p_1$、$r=p'_1$、$q=p'_2$、$k=p'_3$。这一小节用$q$表示出射反中微子的动量。在$P^2=-m_\mu^2$、$k^2=-m_e^2$、$r^2=q^2=0$下，将振幅与复共轭相乘，作末态和及初态平均，得到
<span id="eq:x88-direct-traces"></span>

$$
\begin{aligned}
\langle|\mathcal T|^2\rangle
=4G_F^2\,
&\operatorname{tr}\!\left[
 (-\slashed k+m_e)\gamma^\mu P_L(-\slashed q)\gamma^\nu P_L\right]\\
{}\times&\operatorname{tr}\!\left[
 (-\slashed r)\gamma_\mu P_L(-\slashed P+m_\mu)\gamma_\nu P_L\right].
\end{aligned}
\tag{88.44}
$$

伴随顶角仍为$\gamma^\nu P_L$，因为$\overline{\gamma^\nu P_L}=P_R\gamma^\nu=\gamma^\nu P_L$。系数$4=(2\sqrt2)^2/2$含有初态的两自旋平均。

将每条迹中的投影移到最右边。显式质量项含三个$\gamma$矩阵，带或不带$\gamma_5$的迹都为零。因此所需的通式可写成
<span id="eq:x88-chiral-tensor"></span>

$$
\begin{aligned}
T^{\mu\nu}(a,b)
 &:=\operatorname{tr}(\slashed a\gamma^\mu\slashed b\gamma^\nu P_L)\\
 &=2\left[a^\mu b^\nu+a^\nu b^\mu-g^{\mu\nu}(a\cdot b)
           -i\varepsilon^{\mu\nu\rho\sigma}a_\rho b_\sigma\right].
\end{aligned}
\tag{88.45}
$$

取$\varepsilon^{0123}=+1$，这个式子由[第47节](/posts/srednicki-47/)的四$\gamma$迹逐项得到：普通迹为$4[a^\mu b^\nu+a^\nu b^\mu-g^{\mu\nu}(a\cdot b)]$；含$\gamma_5$的迹是$-4i\varepsilon^{\rho\mu\sigma\nu}a_\rho b_\sigma=+4i\varepsilon^{\mu\nu\rho\sigma}a_\rho b_\sigma$。乘$P_L=(1-\gamma_5)/2$后，反对称部分便带式[（88.45）](#eq:x88-chiral-tensor)的$-i$。

分别记方括号中的对称部分为$S^{\mu\nu}(a,b)$，反对称实张量为$F^{\mu\nu}(a,b)=\varepsilon^{\mu\nu\rho\sigma}a_\rho b_\sigma$。对称张量与反对称张量的交叉收缩为零。其余两部分逐项计算为
<span id="eq:x88-symmetric-antisymmetric-contraction"></span>

$$
\begin{aligned}
S^{\mu\nu}(a,b)S_{\mu\nu}(c,d)
 &=2(a\cdot c)(b\cdot d)+2(a\cdot d)(b\cdot c)\\
 &\quad-4(a\cdot b)(c\cdot d)+4(a\cdot b)(c\cdot d)\\
 &=2[(a\cdot c)(b\cdot d)+(a\cdot d)(b\cdot c)],\\
F^{\mu\nu}(a,b)F_{\mu\nu}(c,d)
 &=-2[(a\cdot c)(b\cdot d)-(a\cdot d)(b\cdot c)].
\end{aligned}
\tag{88.46}
$$

最后一式使用$\varepsilon^{\mu\nu\rho\sigma}\varepsilon_{\mu\nu\alpha\beta}=-2(\delta^\rho_\alpha\delta^\sigma_\beta-\delta^\rho_\beta\delta^\sigma_\alpha)$；负号来自洛伦兹度规行列式，因收缩两个指标而有$2!$。两条迹各有系数2，两个反对称项相乘又给$(-i)^2=-1$，所以
<span id="eq:x88-chiral-contraction"></span>

$$
\begin{aligned}
T^{\mu\nu}(a,b)T_{\mu\nu}(c,d)
 &=4(SS-FF)\\
 &=16(a\cdot c)(b\cdot d).
\end{aligned}
\tag{88.47}
$$

代入$(a,b,c,d)=(k,q,r,P)$，再乘式[（88.44）](#eq:x88-direct-traces)的$4G_F^2$，就得到式[（88.37）](#eq:c88-amplitude-squared)。对称部分原本含两种动量配对，反对称部分消去其中一种；费尔兹变换把这次相消提前并入了两个标量流。

<span id="c88-width"></span>

## 三体相空间与总宽度

为了积分式[（88.37）](#eq:c88-amplitude-squared)，将$p'_1$与$p'_3$先组成一个具有可变不变质量的对子。记$P=p_1$、$m=m_\mu$、$r=p'_1+p'_3$、$s=-r^2$。在本小节令三个末态质量均为零。三个粒子的相空间可以分解为
<span id="eq:c88-phase-space-factorization"></span>

$$
d\Phi_3(P;p'_1,p'_2,p'_3)
 =\frac{ds}{2\pi}\,
   d\Phi_2(P;p'_2,r)\,d\Phi_2(r;p'_1,p'_3),
\qquad 0\le s\le m^2 .
\tag{88.38}
$$

这里的$1/(2\pi)$可由原始测度直接追踪。先插入对$r$的四维delta函数，使内层带有$(2\pi)^4\delta^4(r-p'_1-p'_3)$，同时留下$d^4r/(2\pi)^4$；在它的未来类时支撑上再插入$\int_0^\infty ds\,\delta(r^2+s)=1$。对$r^0>0$作壳积分，因$|\partial(r^2+s)/\partial r^0|=2r^0$，有
<span id="eq:c88-pair-shell-measure"></span>

$$
\frac{d^4r}{(2\pi)^4}\,ds\,
 \theta(r^0)\delta(r^2+s)
 =\frac{ds}{2\pi}\,
   \frac{d^3\mathbf r}{(2\pi)^3\,2\sqrt{\mathbf r^2+s}}.
\tag{88.39}
$$

右侧正是外层两体相空间所需的对子测度。

[第11节已求出的两体相空间](/posts/srednicki-11/#c11-two-body)在母粒子静止系中等于$|\mathbf k|/(4\pi M)$。外层是一粒无质量粒子与一个质量$\sqrt s$的对子，$|\mathbf k|=(m^2-s)/(2m)$；内层是对子衰变成两个无质量粒子，$|\mathbf k_*|=\sqrt s/2$。因此两次角积分分别为
<span id="eq:c88-three-body-measure"></span>

$$
\Phi_2(P;0,\sqrt s)=\frac{m^2-s}{8\pi m^2},\qquad
\Phi_2(r;0,0)=\frac1{8\pi},\qquad
 d\Phi_3\big|_{\rm angles}
 =\frac{m^2-s}{128\pi^3m^2}\,ds .
\tag{88.40}
$$

式[（88.37）](#eq:c88-amplitude-squared)的两个内积恰好只依赖$s$。由$r=P-p'_2$和$r=p'_1+p'_3$分别平方，得到
<span id="eq:c88-pair-invariants"></span>

$$
\begin{aligned}
-s&=-m^2-2P\cdot p'_2,
 &P\cdot p'_2&=-\frac{m^2-s}{2},\\
-s&=2p'_1\cdot p'_3,
 &p'_1\cdot p'_3&=-\frac{s}{2},\\
\langle|\mathcal T|^2\rangle
 &=16G_F^2s(m^2-s).
\end{aligned}
\tag{88.41}
$$

被积函数于是与刚才积掉的两个方向均无关。三个末态粒子的种类不同，不需相同粒子阶乘。按[单粒子衰变的归一](/posts/srednicki-11/#c11-decay)，静止系宽度还须除以$2m$，所以
<span id="eq:c88-width-integral"></span>

$$
\begin{aligned}
\Gamma_\mu
 &=\frac1{2m}\int d\Phi_3\,\langle|\mathcal T|^2\rangle\\
 &=\frac{G_F^2}{16\pi^3m^3}
      \int_0^{m^2}ds\,s(m^2-s)^2,\\
\int_0^{m^2}ds\,s(m^2-s)^2
 &=\left[\frac{m^4s^2}{2}-\frac{2m^2s^3}{3}
                      +\frac{s^4}{4}\right]_0^{m^2}
 =\frac{m^8}{12}.
\end{aligned}
\tag{88.42}
$$

最后得到总宽度：
<span id="eq:c88-muon-width"></span>

$$
\boxed{\Gamma_\mu=\frac{G_F^2m_\mu^5}{192\pi^3}},
\qquad m_e=0\quad\text{（树级）}.
\tag{88.43}
$$

$G_F^2$的量纲为$-4$，因此$m_\mu^5$使宽度具有能量量纲。它来自振幅中的四次动量、三体测度和初态归一的共同组合。

<span id="c88-electron-mass"></span>

## 保留电子质量的积分

式[（88.37）](#eq:c88-amplitude-squared)的自旋迹已经保留了$m_e$。继续使用$r=p'_1+p'_3$，内层对子现在包含质量分别为零和$m_e$的两个粒子，因而
<span id="eq:c88-massive-pair"></span>

$$
\begin{aligned}
m_e^2&\le s\le m_\mu^2,\\
P\cdot p'_2&=-\frac{m_\mu^2-s}{2},\qquad
p'_1\cdot p'_3=-\frac{s-m_e^2}{2},\\
\Phi_2(r;0,m_e)&=\frac{s-m_e^2}{8\pi s},\\
\langle|\mathcal T|^2\rangle
 &=16G_F^2(m_\mu^2-s)(s-m_e^2).
\end{aligned}
\tag{88.48}
$$

内层动量大小为$(s-m_e^2)/(2\sqrt{s})$，除以$4\pi\sqrt{s}$就给第三行。外层两体测度保持式[（88.40）](#eq:c88-three-body-measure)的形式。将两个测度和模平方相乘，得到
<span id="eq:c88-massive-width-integral"></span>

$$
\begin{aligned}
\Gamma_\mu^{(0)}
 &=\frac{G_F^2}{16\pi^3m_\mu^3}
 \int_{m_e^2}^{m_\mu^2}ds\,
 \frac{(m_\mu^2-s)^2(s-m_e^2)^2}{s}\\
 &=\frac{G_F^2m_\mu^5}{16\pi^3}
 \int_\rho^1 dz\,\frac{(1-z)^2(z-\rho)^2}{z},
 \qquad \rho=\frac{m_e^2}{m_\mu^2},\quad z=\frac{s}{m_\mu^2}.
\end{aligned}
\tag{88.49}
$$

被积函数中的$1/z$来自内层的有质量两体测度。展开分子后，可以逐项积分：
<span id="eq:c88-massive-antiderivative"></span>

$$
\begin{aligned}
\frac{(1-z)^2(z-\rho)^2}{z}
 &=z^3-2(1+\rho)z^2+(1+4\rho+\rho^2)z
       -2\rho(1+\rho)+\frac{\rho^2}{z},\\
\int_\rho^1 dz\,\frac{(1-z)^2(z-\rho)^2}{z}
 &=\left[\frac{z^4}{4}-\frac{2(1+\rho)z^3}{3}
 +\frac{(1+4\rho+\rho^2)z^2}{2}
 -2\rho(1+\rho)z+\rho^2\log z\right]_\rho^1\\
 &=\frac{1-8\rho+8\rho^3-\rho^4-12\rho^2\log\rho}{12}.
\end{aligned}
\tag{88.50}
$$

因此有限电子质量的结果为
<span id="eq:c88-massive-width"></span>

$$
\Gamma_\mu^{(0)}
 =\frac{G_F^2m_\mu^5}{192\pi^3}f(\rho),\qquad
f(\rho)=1-8\rho+8\rho^3-\rho^4-12\rho^2\log\rho.
\tag{88.51}
$$

当$\rho\to0$时，$\rho^2\log\rho\to0$，恢复无质量电子的宽度。取中译本表中的$m_e=0.511$ MeV、$m_\mu=105.7$ MeV，得$\rho\simeq2.34\times10^{-5}$、$f(\rho)\simeq0.999813$。这个修正来自积分区域及两体测度的变化。

中译本列出的$G_F=1.166\times10^{-5}\,\mathrm{GeV}^{-2}$由缪子寿命提取，其中还计入QED辐射修正。上面求出的是$m_\mu^2/M_W^2\ll1$时的树级宽度；将相应修正一同纳入寿命公式，才能以实验寿命确定$G_F$，再匹配到电弱理论的参数。

---

[← 第 87 节](/posts/srednicki-87/) · [章节地图](/srednicki/) · [第 89 节 →](/posts/srednicki-89/)
