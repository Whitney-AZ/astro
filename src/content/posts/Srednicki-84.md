---
title: 'Srednicki §84 规范对称性的自发破缺'
date: 2026-09-14
category: 笔记
tags: [物理, 量子场论, Srednicki]
series: 'Srednicki QFT'
srednickiSections: [84]
hideFromHome: true
draft: false
---

<span id="c84"></span>

在[第32节](/posts/srednicki-32/#c32)，复标量场沿势能谷底的运动给出了一个无质量的戈德斯通玻色子。现在把同一个模型中的相位变换变为规范对称性。标量势仍然有一圈极小值，但各点的相位已经可以独立改变。我们将看到，原来的角向自由度成为有质量规范场的纵向偏振；势的径向起伏则仍是一个标量粒子。这样得到规范场质量的办法称为希格斯机制（Higgs mechanism）。

本节先在标量电动力学中完成这个计算，再把质量项写成适用于任意表示的矩阵，最后考察$SU(N)$、$SO(N)$和$SU(5)$。所用质量均指经典真空附近、标准动能归一下的树级质量；它们的量子修正和规范固定将在后续章节讨论。

<span id="c84-higgs"></span>

## 角向自由度怎样进入规范场

取一个复标量场$\varphi$，其拉格朗日量为

<span id="eq:c84-abelian-theory"></span>

$$
\begin{aligned}
\mathcal L
 & =-(D^\mu\varphi)^\dagger D_\mu\varphi
   -V(\varphi)-\frac14F^{\mu\nu}F_{\mu\nu},\\
D_\mu&=\partial_\mu-igA_\mu,\qquad
F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu,\\
V(\varphi)
 &=m^2\varphi^\dagger\varphi
   +\frac{\lambda}{4}(\varphi^\dagger\varphi)^2 .
\end{aligned}
\tag{84.1}
$$

这里以$g$表示规范耦合，因为我们暂且把这个理论用作说明机制的例子。为了使四次势有下界，取$\lambda>0$；又取$m^2<0$，使$\varphi=0$成为不稳定的驻点。记$r^2=2\varphi^\dagger\varphi$，则

<span id="eq:c84-vacuum-radius"></span>

$$
\begin{aligned}
V(r)&=\frac12m^2r^2+\frac{\lambda}{16}r^4,\\
\frac{dV}{dr}
 &=r\left(m^2+\frac{\lambda}{4}r^2\right),\\
v^2&=-\frac{4m^2}{\lambda},\qquad
\left.\frac{d^2V}{dr^2}\right|_{r=v}
 =-2m^2>0 .
\end{aligned}
\tag{84.2}
$$

因此经典极小值满足$|\varphi|=v/\sqrt2$，其中$v>0$。用一个常数相位变换选取实的真空代表，便得到所选真空期望值（vacuum expectation value，VEV）。在这个代表附近，径向和角向起伏可以写成两个实场：

<span id="eq:c84-polar-potential"></span>

$$
\begin{aligned}
\varphi(x)&=\frac{v+\rho(x)}{\sqrt2}e^{-i\chi(x)/v},\\
V(\varphi)
 &=-\frac{\lambda v^4}{16}
   +\frac{\lambda v^2}{4}\rho^2
   +\frac{\lambda v}{4}\rho^3
   +\frac{\lambda}{16}\rho^4 .
\end{aligned}
\tag{84.3}
$$

展开时的线性项为$v(m^2+\lambda v^2/4)\rho$，由极值条件消失；二次项为$(m^2/2+3\lambda v^2/8)\rho^2=\lambda v^2\rho^2/4$。其中$-\lambda v^4/16$是常数真空能；在这里的平直时空场方程与散射计算中，可以将它减去。角场$\chi$完全不出现在势中，这正是第32节中无质量模的来源。

把极坐标代入协变导数，逐项求导得

<span id="eq:c84-polar-kinetic"></span>

$$
\begin{aligned}
D_\mu\varphi
 &=\frac{e^{-i\chi/v}}{\sqrt2}
   \left[\partial_\mu\rho
    -i(v+\rho)\left(\frac{\partial_\mu\chi}{v}+gA_\mu\right)\right],\\
-(D^\mu\varphi)^\dagger D_\mu\varphi
 &=-\frac12\partial^\mu\rho\,\partial_\mu\rho
   -\frac12(v+\rho)^2
       \left(\frac{\partial^\mu\chi}{v}+gA^\mu\right)
       \left(\frac{\partial_\mu\chi}{v}+gA_\mu\right).
\end{aligned}
\tag{84.4}
$$

两个交叉项的系数分别是$+i$和$-i$；实标量及阿贝尔规范场可交换，这两项正好相消。因此角场只通过$\partial_\mu\chi+gvA_\mu$出现。角场与规范场通过这一组合混合。

<span id="c84-unitary"></span>

## 幺正规范与有质量矢量粒子

由式[（84.1）](#eq:c84-abelian-theory)的协变导数，规范变换应取

<span id="eq:c84-unitary-transformation"></span>

$$
\begin{aligned}
\varphi'&=e^{-ig\Gamma}\varphi,\qquad
A'_\mu=A_\mu-\partial_\mu\Gamma,\\
\rho'&=\rho,\qquad \chi'=\chi+gv\Gamma,\\
\Gamma&=-\frac{\chi}{gv}:
\qquad \chi'=0,\qquad
\mathcal A_\mu\equiv A'_\mu
=A_\mu+\frac{\partial_\mu\chi}{gv}.
\end{aligned}
\tag{84.5}
$$

例如把前两行代入$\partial_\mu\chi'+gvA'_\mu$，含$\partial_\mu\Gamma$的两项直接抵消。又因为偏导数可交换，$\mathcal A_\mu$与$A_\mu$有相同的场强。在$v+\rho\ne0$且相位光滑的真空邻域，可以用这次变换令角场处处为零；这就是幺正规范（unitary gauge）。场的零点或非平凡绕行需要另选坐标片。

把式[（84.3）](#eq:c84-polar-potential)和式[（84.4）](#eq:c84-polar-kinetic)合起来，减去常数真空能，得到

<span id="eq:c84-unitary-lagrangian"></span>

$$
\begin{aligned}
\mathcal L
 &=-\frac14\mathcal F_{\mu\nu}\mathcal F^{\mu\nu}
   -\frac12\partial^\mu\rho\,\partial_\mu\rho
   -\frac12g^2(v+\rho)^2\mathcal A^\mu\mathcal A_\mu\\
 &\quad-\frac{\lambda v^2}{4}\rho^2
   -\frac{\lambda v}{4}\rho^3
   -\frac{\lambda}{16}\rho^4 .
\end{aligned}
\tag{84.6}
$$

这给出了幺正规范中的动能与相互作用。质量项必须与四维$(-,+,+,+)$约定下的$-M^2\mathcal A^\mu\mathcal A_\mu/2$和$-m_\rho^2\rho^2/2$比较，所以

<span id="eq:c84-abelian-masses"></span>

$$
\begin{aligned}
M^2&=g^2v^2,\qquad
m_\rho^2=\frac{\lambda v^2}{2}=-2m^2,\\
\mathcal L_{\rho\mathcal A}
 &=-g^2v\rho\,\mathcal A^\mu\mathcal A_\mu
   -\frac12g^2\rho^2\mathcal A^\mu\mathcal A_\mu .
\end{aligned}
\tag{84.7}
$$

取$g>0$时，第一式给出$M=gv$。两个质量平方都为正，且量纲均为2；留下的三次、四次项又确定了径向粒子与矢量粒子的耦合。这些耦合与质量来自同一项协变动能，并非独立加入的参数。

角场不再出现在式[（84.6）](#eq:c84-unitary-lagrangian)中，物理自由度却没有减少。只看规范场的自由二次项，变分给出

<span id="eq:c84-longitudinal-state"></span>

$$
\begin{aligned}
\partial_\mu\mathcal F^{\mu\nu}-M^2\mathcal A^\nu&=0,\\
M^2\partial_\nu\mathcal A^\nu&=0,\qquad
(\partial^2-M^2)\mathcal A^\nu=0,\\
p^2&=-M^2,\qquad p_\mu\varepsilon^\mu=0,\\
\varepsilon_L^\mu(p)
 &=\left(\frac{|\mathbf p|}{M},
          \frac{E_{\mathbf p}}{M}\widehat{\mathbf p}\right),
\qquad E_{\mathbf p}^2=|\mathbf p|^2+M^2 .
\end{aligned}
\tag{84.8}
$$

第二行的第一个式子由第一行再取散度得到：反对称场强与对称的两次偏导收缩为零。对$M\ne0$，四个分量因此满足一个约束，留下三个自旋态。其中两个可选为空间横向偏振；上式所列第三个满足$p\cdot\varepsilon_L=0$及$\varepsilon_L^2=1$，空间部分沿$\mathbf p$，故称纵向状态。在静止系中则可沿任意第三个空间轴取单位偏振。

原来无质量规范场的两个自旋态，加上复标量的两个实自由度，如今成为有质量规范场的三个自旋态和一个径向标量。角场提供了增加的纵向状态。使规范场这样得到质量的标量通常称为希格斯场。若令$g\to0$，应回到式[（84.4）](#eq:c84-polar-kinetic)；那时角场重新独立传播。幺正规范的变量变换含$1/g$，在该极限退化。

这里所谓规范对称性的“自发破缺”，是按所选真空代表展开时的通用说法。局域规范变换联系的是同一物理配置的不同描述。若对整个规范轨道作不变平均，一个带电场的平均值必满足

<span id="eq:c84-gauge-orbit-average"></span>

$$
\langle\varphi(x)\rangle
 =e^{-i\alpha(x)}\langle\varphi(x)\rangle
\quad\hbox{对所有 }\alpha(x),
\qquad \langle\varphi(x)\rangle=0 .
\tag{84.9}
$$

非零$v/\sqrt2$是固定取向后用来组织计算的背景；从它得到的粒子质量和自由度计数才是这里关心的物理结果。第32节的戈德斯通论证使用作用于物理态的整体连续对称性；这里的局域轨道平均则体现了规范描述的冗余。

<span id="c84-mass-matrix"></span>

## 一般表示中的质量平方矩阵

推广到非阿贝尔群时，改变的只是标量所带的内部指标。设$\varphi_i$处于表示$R$中，$i=1,\ldots,d(R)$，生成元$T_R^a$为厄米矩阵。允许规范群有多个直积因子，把与生成元$a$相伴的耦合记作$g_a$；同一简单因子内这些耦合相同。取

<span id="eq:c84-general-background"></span>

$$
\begin{aligned}
(D_\mu\varphi)_i
 &=\partial_\mu\varphi_i
   -i\sum_a g_aA_\mu^a(T_R^a)_i{}^j\varphi_j,\\
\langle\varphi_i\rangle&=\frac{v_i}{\sqrt2}.
\end{aligned}
\tag{84.10}
$$

向量$v_i$由势的极小值决定；规范变换可改变其取向而不改变势能。本节先假定已经选定一个这样的极小值。为了求规范场质量，只需在协变动能中把标量换成常数背景，取出二次于$A_\mu^a$的项：

<span id="eq:c84-mass-extraction"></span>

$$
\begin{aligned}
\mathcal L_{\rm mass}
 &=-\frac12\sum_{a,b}g_ag_bA_\mu^aA^{b\mu}
       v^\dagger T_R^aT_R^b v\\
 &=-\frac14\sum_{a,b}g_ag_bA_\mu^aA^{b\mu}
       v^\dagger\{T_R^a,T_R^b\}v\\
 &=-\frac12\sum_{a,b}(M^2)_{ab}A_\mu^aA^{b\mu}.
\end{aligned}
\tag{84.11}
$$

第二行是在求和中交换$a,b$后取平均；$A_\mu^aA^{b\mu}$对交换对称，反对称的生成元乘积因而不贡献。比较最后一行，得到适用于多个规范因子的质量矩阵：

<span id="eq:c84-mass-gram"></span>

$$
(M^2)_{ab}
 =\frac12g_ag_bv^\dagger\{T_R^a,T_R^b\}v
 =g_ag_b\,\operatorname{Re}
       \bigl[(T_R^av)^\dagger(T_R^bv)\bigr].
\tag{84.12}
$$

反对易子是厄米矩阵，所以质量平方矩阵为实对称矩阵。若表示是实的，可以用实标量并选纯虚、反对称的厄米生成元。这时$v_i$直接等于实场的真空值，动能却多一个$1/2$：

<span id="eq:c84-real-normalization"></span>

$$
\begin{aligned}
\langle\varphi_i\rangle&=v_i,\qquad
\mathcal L_{\rm kin}=-\frac12(D_\mu\varphi)^T D^\mu\varphi,\\
\left.\mathcal L_{\rm kin}\right|_v
 &=-\frac12\sum_{a,b}g_ag_bA_\mu^aA^{b\mu}
       (T_R^av)^\dagger(T_R^bv).
\end{aligned}
\tag{84.13}
$$

这里$D_\mu\varphi$为实向量，因为$-iT_R^a$为实矩阵。把它当作复向量取厄米内积与转置内积相同。真空中的$\sqrt2$和动能中的$1/2$正好补偿，式[（84.12）](#eq:c84-mass-gram)因此仍然适用。动能与真空值的归一共同确定质量系数。

质量矩阵还有一个直接的几何含义。任取实系数$x_a$，由式[（84.12）](#eq:c84-mass-gram)得

<span id="eq:c84-positive-mass"></span>

$$
\sum_{a,b}x_a(M^2)_{ab}x_b
 =\left\|\sum_a g_ax_aT_R^av\right\|^2\ge0 .
\tag{84.14}
$$

右边是规范变换沿背景轨道移动的长度平方。因此质量平方不可能为负，而零质量组合恰好对应不移动真空的生成元。对于实对称半正定矩阵，先作正交对角化，二次型是各非负本征值乘坐标平方之和；二次型为零等价于向量处于矩阵的核。于是

<span id="eq:c84-unbroken-kernel"></span>

$$
\begin{aligned}
x\in\ker M^2
 &\ \Longleftrightarrow\
 \left(\sum_a g_ax_aT_R^a\right)v=0,\\
Xv=Yv=0&\ \Longrightarrow\ [X,Y]v=0 .
\end{aligned}
\tag{84.15}
$$

第二行证明未破缺生成元在对易运算下封闭，从而构成稳定群的李代数。各$g_a$非零时，零质量本征向量与这组生成元一一对应。在一般基底中，应把$T_Rv=0$的判据用于生成元的线性组合，并先对角化质量矩阵。

一个有用的例子是带两个单位阿贝尔荷的复标量。若其背景为$v/\sqrt2$，便有

<span id="eq:c84-two-abelian-matrix"></span>

$$
M^2=v^2
\begin{pmatrix}
g_1^2&g_1g_2\\
g_1g_2&g_2^2
\end{pmatrix},
\qquad
\det(M^2-zI)=z\bigl[z-v^2(g_1^2+g_2^2)\bigr].
\tag{84.16}
$$

两个对角元都非零，但一个本征值仍为零。实际质量本征场为

<span id="eq:c84-two-abelian-eigenstates"></span>

$$
\begin{aligned}
B_\mu&=\frac{g_1A_\mu^1+g_2A_\mu^2}
                  {\sqrt{g_1^2+g_2^2}},
& M_B&=v\sqrt{g_1^2+g_2^2},\\
C_\mu&=\frac{-g_2A_\mu^1+g_1A_\mu^2}
                  {\sqrt{g_1^2+g_2^2}},
& M_C&=0 .
\end{aligned}
\tag{84.17}
$$

这是一个正交变换，所以规范场的标准二次动能保持不变。将逆变换代入$g_1A_\mu^1+g_2A_\mu^2$，$C_\mu$的系数消失，质量项只剩$-v^2(g_1^2+g_2^2)B_\mu B^\mu/2$。虽然两个原始场的对角质量项均非零，混合之后仍有一个无质量本征态。

未破缺群也组织着有质量粒子的多重态。设$h$保持背景不变，$R(h)v=v$。规范场经伴随变换后，$\sum_a g_aA^aT_R^av$只是左乘幺正矩阵$R(h)$，所以式[（84.14）](#eq:c84-positive-mass)的长度不变。规范动能也在该变换下不变，故质量矩阵与稳定群的作用可交换。一个固定质量的本征空间因而构成未破缺群的表示。在没有等价表示混合的不可约块内，若存在两个不同质量本征值，它们的本征空间便是两个非平凡不变子空间，与不可约性矛盾。因此该块的质量矩阵只能正比于单位矩阵。这是舒尔引理在此处的具体用法，也说明为何能够由一个矩阵元求出整个多重态的质量。

<span id="c84-fundamental"></span>

## 基本表示的两个例子

先考虑$SU(N)$的复基本表示，$N\ge2$。任一非零复向量都可以补成一组标准正交基，所以存在幺正变换把$v_i$转到末分量。若这个变换的行列式不是1，再调整一个与末分量正交的基向量的相位，就能使行列式为1而不改变已经选好的末分量。因此可取$v_i=v\delta_{iN}$，$v>0$。保持这个向量不变的$SU(N)$矩阵必为$\operatorname{diag}(h,1)$，其中$h\in SU(N-1)$。

用$E_{ij}$表示仅第$i$行、第$j$列为1的矩阵。与末分量相连的生成元及余下的一个对角生成元可选为

<span id="eq:c84-su-broken-generators"></span>

$$
\begin{aligned}
X_i&=\frac12(E_{iN}+E_{Ni}),&
Y_i&=\frac12(-iE_{iN}+iE_{Ni}),
\qquad i=1,\ldots,N-1,\\
H&=\frac{\operatorname{diag}(1,\ldots,1,-(N-1))}
                {\sqrt{2N(N-1)}} .
\end{aligned}
\tag{84.18}
$$

每个$X_i,Y_i$的平方在第$i$和第$N$个对角位置各给$1/4$，所以平方的迹是$1/2$；$H$的平方迹为$[(N-1)+(N-1)^2]/[2N(N-1)]=1/2$。不同矩阵的迹内积为零。这三类生成元因而都具有相同的半迹归一。

令$e_i$为标准单位向量，作用于背景的结果是

<span id="eq:c84-su-generator-actions"></span>

$$
X_i(ve_N)=\frac v2e_i,\qquad
Y_i(ve_N)=-\frac{iv}{2}e_i,\qquad
H(ve_N)=-v\sqrt{\frac{N-1}{2N}}e_N .
\tag{84.19}
$$

不同$i$的像彼此正交；同一$i$的$X_i,Y_i$内积为纯虚数，取实部后也为零；$H$的像只在末分量上。因此式[（84.12）](#eq:c84-mass-gram)已在这组基底中对角化，给出

<span id="eq:c84-su-fundamental-masses"></span>

$$
\begin{aligned}
M_X^2=M_Y^2&=\frac14g^2v^2
 &&\text{共 }2(N-1)\text{ 个实矢量场},\\
M_H^2&=\frac{N-1}{2N}g^2v^2
 &&\text{共 }1\text{ 个实矢量场},\\
n_{\rm broken}
 &=(N^2-1)-\bigl[(N-1)^2-1\bigr]=2N-1 .
\end{aligned}
\tag{84.20}
$$

未破缺的$SU(N-1)$生成元全部位于左上块，故作用于$ve_N$时为零，其规范场无质量。为了看清重矢量的表示，把前两类实场组合为

<span id="eq:c84-su-heavy-representation"></span>

$$
W_\mu^i=\frac{A_{\mu,X_i}-iA_{\mu,Y_i}}{\sqrt2},
\qquad
A_\mu\supset
\begin{pmatrix}
0&W_\mu/\sqrt2\\
W_\mu^\dagger/\sqrt2&0
\end{pmatrix},
\qquad W_\mu\longmapsto hW_\mu .
\tag{84.21}
$$

最后的变换直接来自$A_\mu\mapsto\operatorname{diag}(h,1)A_\mu\operatorname{diag}(h^\dagger,1)$。因此$W_\mu$是一个复的$SU(N-1)$基本多重态，其共轭不是另一组独立实场。$H$与该子群的所有矩阵对易，相应矢量场是单态。对$N=2$，未破缺的$SU(1)$是平凡群，三个矢量质量都为$gv/2$；一个复二重态并没有留下额外的无质量$U(1)$规范场。

再考虑$SO(N)$的实基本表示。实正交变换同样可把背景转到$ve_N$，保持它不变的群为$SO(N-1)$。选择

<span id="eq:c84-so-fundamental-mass"></span>

$$
\begin{aligned}
T_i&=-i(E_{iN}-E_{Ni}),\qquad i=1,\ldots,N-1,\\
T_i(ve_N)&=-iv e_i,\qquad
\operatorname{Tr}T_iT_j=2\delta_{ij},\\
(M^2)_{ij}&=g^2v^2\delta_{ij},\qquad M=gv .
\end{aligned}
\tag{84.22}
$$

这里用的是式[（84.13）](#eq:c84-real-normalization)的实场动能，生成元的非零矩阵元也由SU例中的$1/2$改为1；两点都要保留，才能得到质量$gv$。共有$N-1$个破缺方向，数目也等于$N(N-1)/2-(N-1)(N-2)/2$。

若记这些实矢量为$B_\mu^i$，则在$h\in SO(N-1)$下，

<span id="eq:c84-so-heavy-representation"></span>

$$
\operatorname{diag}(h,1)T_i\operatorname{diag}(h^T,1)
 =\sum_jh_{ji}T_j,\qquad
B_\mu^j\longmapsto\sum_i h_{ji}B_\mu^i .
\tag{84.23}
$$

它们组成未破缺群的实基本表示。特别是$N=3$时，剩下的是平面转动群$SO(2)$。平面转角相加与单位复数相乘相同，给出$SO(2)\simeq U(1)$；把两个实重矢量组合为$B_\mu^1+iB_\mu^2$，就得到在该$U(1)$下带一个单位旋转荷的复场。

<span id="c84-adjoint"></span>

## 伴随表示与矩阵动能的归一

对$SU(N)$的实伴随标量，逐个处理$N^2-1$个分量不如把它们合成矩阵方便。沿[第70节](/posts/srednicki-70/#c70)的半迹生成元定义

<span id="eq:c84-adjoint-kinetic"></span>

$$
\begin{aligned}
\Phi&=\varphi^aT^a,\qquad
\operatorname{Tr}T^aT^b=\frac12\delta^{ab},\\
D_\mu\Phi&=\partial_\mu\Phi-ig[A_\mu,\Phi],\\
\mathcal L_{\rm kin}
 &=-\frac12(D_\mu\varphi)^a(D^\mu\varphi)^a
  =-\operatorname{Tr}(D_\mu\Phi D^\mu\Phi),\\
V&=\langle\Phi\rangle=v^aT^a .
\end{aligned}
\tag{84.24}
$$

$\varphi^a$为实数，故$\Phi$是无迹厄米矩阵；它按$\Phi\mapsto U\Phi U^\dagger$变换。动能的最后一个等号由两生成元的迹直接给出。因此矩阵动能的系数为$-1$。

记$C_a=[T^a,V]$。常数背景的协变导数为$-igA_\mu^aC_a$，代入上式得到

<span id="eq:c84-adjoint-mass"></span>

$$
\begin{aligned}
\left.\mathcal L_{\rm kin}\right|_V
 &=g^2 A_\mu^aA^{b\mu}\operatorname{Tr}(C_aC_b)\\
 &=\frac{g^2}{2}A_\mu^aA^{b\mu}
                 \operatorname{Tr}\{C_a,C_b\},\\
(M^2)_{ab}
 &=-g^2\operatorname{Tr}\{[T^a,V],[T^b,V]\}.
\end{aligned}
\tag{84.25}
$$

第一行的正号来自原动能的负号与$(-i)^2=-1$相乘；与$-M^2_{ab}A_\mu^aA^{b\mu}/2$比较时，再产生质量公式中的负号。虽然最后的迹前面有负号，质量平方仍为正，因为$C_a^\dagger=-C_a$。

还可直接与分量公式比较，以检查这一系数。若$[T^a,T^c]=if^{acd}T^d$，伴随生成元为$(T_{\rm adj}^a)^d{}_c=-if^{adc}$，于是

<span id="eq:c84-adjoint-component-check"></span>

$$
\begin{aligned}
C_a&=(T_{\rm adj}^av)^dT^d,\\
(T_{\rm adj}^av)^\dagger(T_{\rm adj}^bv)
 &=2\operatorname{Tr}(C_a^\dagger C_b),\\
g^2\operatorname{Re}
\bigl[(T_{\rm adj}^av)^\dagger(T_{\rm adj}^bv)\bigr]
 &=-g^2\operatorname{Tr}(C_aC_b+C_bC_a).
\end{aligned}
\tag{84.26}
$$

第二行利用了同一半迹归一，第三行又用了$C_a^\dagger=-C_a$及复共轭后交换两矩阵。这恰好还原式[（84.12）](#eq:c84-mass-gram)，并独立于直接展开矩阵动能的办法。

另一种矩阵场归一把动能写为$-\tfrac12\operatorname{Tr}(D\Phi_{\rm lit})^2$。下标$\mathrm{lit}$区分这套替代变量，其与标准实分量的关系为

<span id="eq:c84-adjoint-source-conversion"></span>

$$
\begin{aligned}
(M_{\rm lit}^2)_{ab}
 &=-\frac{g^2}{2}
       \operatorname{Tr}\{[T^a,V_{\rm lit}],[T^b,V_{\rm lit}]\},\\
\Phi_{\rm lit}&=\sqrt2\,\Phi,\qquad V_{\rm lit}=\sqrt2\,V,\\
-\operatorname{Tr}(D_\mu\Phi D^\mu\Phi)
 &=-\frac12\operatorname{Tr}
          (D_\mu\Phi_{\rm lit}D^\mu\Phi_{\rm lit}) .
\end{aligned}
\tag{84.27}
$$

第一行采用替代动能系数，背景也相应记为$V_{\rm lit}$。后两行的场重标度使它与标准实分量动能一致；若改变动能系数却保持同一个矩阵背景，质量平方就会少一半。以下沿用标准实分量动能，并在$SU(5)$例子中展示这两套变量的转换。

<span id="c84-centralizer"></span>

## 由真空本征值求未破缺群

厄米矩阵$V$可以被幺正变换对角化。若该变换不在$SU(N)$中，给整个变换乘一个相位即可把行列式调到1；这个相位在$UVU^\dagger$中相消，不影响对角化。设$V$有$k$个不同的本征值，按大小排列为$v_1<\cdots<v_k$，重数分别为$N_1,\ldots,N_k$。于是

<span id="eq:c84-adjoint-eigenblocks"></span>

$$
\begin{aligned}
V&=\operatorname{diag}(v_1I_{N_1},\ldots,v_kI_{N_k}),\\
\sum_{i=1}^kN_i&=N,\qquad
\sum_{i=1}^kN_iv_i=0,\\
[X,V]_{rs}&=(V_{ss}-V_{rr})X_{rs}.
\end{aligned}
\tag{84.28}
$$

最后一行已经给出全部未破缺生成元：只有属于同一本征值块的矩阵元可以非零。对于有限变换，$UV=VU$同样要求$U$保持每个本征子空间，所以稳定群由块对角幺正矩阵构成，并须保持整体行列式为1：

<span id="eq:c84-centralizer-group"></span>

$$
\begin{aligned}
H&=S\bigl(U(N_1)\times\cdots\times U(N_k)\bigr),\\
\mathfrak h
 &=\bigoplus_{i=1}^k\mathfrak{su}(N_i)
       \ \oplus\ \mathfrak u(1)^{\,k-1},\\
\dim H&=\sum_iN_i^2-1,\qquad
n_{\rm broken}=N^2-\sum_iN_i^2
                  =2\sum_{i<j}N_iN_j .
\end{aligned}
\tag{84.29}
$$

记号$S$表示各块行列式的乘积为1。各块内部的无迹厄米矩阵产生$\mathfrak{su}(N_i)$；块上的常数对角矩阵还有$k$个实参数$\theta_i$，但无迹条件$\sum_iN_i\theta_i=0$去掉一个，因此剩下$k-1$个阿贝尔方向。只有两块时才留下一个$U(1)$方向；一般情况下必须保留全部$k-1$个独立块相位。

例如取$SU(3)$的$V=v\,\operatorname{diag}(-1,0,1)$，三个本征值都不同。其未破缺矩阵是

<span id="eq:c84-three-block-example"></span>

$$
U=\operatorname{diag}
       \bigl(e^{i\theta_1},e^{i\theta_2},
                         e^{-i(\theta_1+\theta_2)}\bigr),
\qquad H\simeq U(1)\times U(1).
\tag{84.30}
$$

两个独立相位各对应一个与$V$对易的生成元，共同构成质量矩阵的核。

在共同匹配尺度上，各未破缺因子的规范耦合仍为$g$。这一点在继承相同生成元归一的基底上可以直接从协变导数看出：原来的矩阵$gA_\mu^aT^a$限制到未破缺子代数时，并不多出新的系数。对一个阿贝尔方向，若把半迹生成元$T=cY$改用数值更方便的荷矩阵$Y$表示，则

<span id="eq:c84-abelian-coupling-conversion"></span>

$$
-ig B_\mu T=-igc B_\mu Y
             \equiv -ig_YB_\mu Y,\qquad g_Y=cg .
\tag{84.31}
$$

这只是生成元与耦合之间的归一转换，规范场$B_\mu$的标准动能保持原样。树级匹配之后，低能不同规范因子的轻粒子内容可以不同，其耦合随后按各自的贝塔函数运行。

<span id="c84-su5"></span>

## SU(5)的轻重矢量多重态

现在取两块背景

<span id="eq:c84-su5-background"></span>

$$
\begin{aligned}
V&=vY,\qquad
Y=\operatorname{diag}
          \left(-\frac13,-\frac13,-\frac13,\frac12,\frac12\right),\\
\operatorname{Tr}Y^2
 &=3\left(\frac13\right)^2+2\left(\frac12\right)^2=\frac56,\\
T^{24}&=cY,\qquad
\frac12=\operatorname{Tr}(T^{24})^2=\frac56c^2,
\qquad c=\sqrt{\frac35}.
\end{aligned}
\tag{84.32}
$$

这里$v$是所列对角矩阵的共同系数；在标准实伴随分量中，背景向量的长度平方为$v^av^a=2\operatorname{Tr}V^2=5v^2/3$。它不等于前面基本表示例中按向量长度定义的$v^2$，每个例子的质量都应从其实际背景计算。

稳定群的李代数为$\mathfrak{su}(3)\oplus\mathfrak{su}(2)\oplus\mathfrak u(1)$，有$8+3+1=12$个生成元；另有$24-12=12$个破缺方向。求局部场的表示时，$SU(3)\times SU(2)\times U(1)$的李代数记号已经足够。若还要确定全局群，式[（84.29）](#eq:c84-centralizer-group)给出$S(U(3)\times U(2))$，与直接积之间有一个有限中心商：

<span id="eq:c84-su5-global-group"></span>

$$
\begin{aligned}
(h_3,h_2,z)&\longmapsto
       \operatorname{diag}(z^{-2}h_3,z^3h_2),\\
z^6=1,\quad h_3=z^2I_3,\quad h_2=z^{-3}I_2
 &\quad\Longrightarrow\quad \operatorname{diag}(z^{-2}h_3,z^3h_2)=I_5,\\
S(U(3)\times U(2))
 &\simeq\bigl[SU(3)\times SU(2)\times U(1)\bigr]/\mathbb Z_6 .
\end{aligned}
\tag{84.33}
$$

第一行的像的行列式恒为1。反过来，给定两块幺正矩阵且其行列式乘积为1，选$z^6$为第一块行列式的逆，就可把两块分别化为行列式为1的$h_3,h_2$，所以该映射满射。第二行恰有六个核元素，给出最后的商。这个有限商不改变这里的生成元数目和质量矩阵。

用三个标签依次标明$SU(3)$表示、$SU(2)$表示和$Y=T^{24}/c$的荷。基本五维向量的前三个分量只受$SU(3)$作用，后两个只受$SU(2)$作用，因此

<span id="eq:c84-su5-fundamental-branch"></span>

$$
\mathbf5\longrightarrow
   (\mathbf3,\mathbf1,-\tfrac13)
   \oplus(\mathbf1,\mathbf2,+\tfrac12).
\tag{84.34}
$$

反基本表示通过复共轭变换，因而SU表示取共轭，阿贝尔相位的号相反。$SU(2)$的共轭二重态与二重态等价：将一般矩阵写成
$U=\bigl(\begin{smallmatrix}a&b\\-b^*&a^*\end{smallmatrix}\bigr)$，$|a|^2+|b|^2=1$，直接相乘可得$\epsilon U^*\epsilon^{-1}=U$，其中$\epsilon=\bigl(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\bigr)$。因此反基本表示分解为

<span id="eq:c84-su5-antifundamental-branch"></span>

$$
\overline{\mathbf5}\longrightarrow
   (\overline{\mathbf3},\mathbf1,+\tfrac13)
   \oplus(\mathbf1,\mathbf2,-\tfrac12).
\tag{84.35}
$$

$SU(3)$的基本表示与反基本表示不等价，故式中仍须保留$\overline{\mathbf3}$。$U(1)$的分支标签使用$Y$，相应耦合为$g_Y=\sqrt{3/5}\,g$；半迹生成元$T^{24}$的本征值则还含因子$c$。

为了求伴随表示，考虑基本向量与反基本向量的张量积。其元素正好是任意$5\times5$矩阵$X$，变换为$X\mapsto UXU^\dagger$。矩阵可唯一分解为无迹部分和单位矩阵部分：

<span id="eq:c84-endomorphism-decomposition"></span>

$$
X=\left(X-\frac{\operatorname{Tr}X}{5}I_5\right)
       +\frac{\operatorname{Tr}X}{5}I_5,\qquad
\mathbf5\otimes\overline{\mathbf5}
       =\mathbf{24}\oplus\mathbf1 .
\tag{84.36}
$$

两部分在共轭变换下分别保持，维数为24和1。这使伴随表示的分解可以通过张量积逐块完成。将$X$写成$3+2$分块，四种块的变换为

<span id="eq:c84-su5-block-transform"></span>

$$
\begin{aligned}
X&=\begin{pmatrix}A&B\\C&D\end{pmatrix},\\
A&\mapsto h_3Ah_3^\dagger,&
D&\mapsto h_2Dh_2^\dagger,\\
B&\mapsto e^{-5i\alpha/6}h_3Bh_2^\dagger,&
C&\mapsto e^{+5i\alpha/6}h_2Ch_3^\dagger .
\end{aligned}
\tag{84.37}
$$

这里有限阿贝尔变换取$e^{i\alpha Y}$。例如右上块的行带荷$-1/3$，列的共轭带荷$-1/2$，故总荷为$-5/6$；左下块同理为$+5/6$。$A$分解为八维无迹矩阵和一维迹，$D$分解为三维无迹矩阵和一维迹；两个非对角块各有$3\times2=6$个复维数。利用$SU(2)$二重态的共轭等价，再从两个中性单态中去掉整体单位矩阵，便得到

<span id="eq:c84-su5-adjoint-branch"></span>

$$
\begin{aligned}
\mathbf{24}\longrightarrow\;
 &(\mathbf8,\mathbf1,0)
 \oplus(\mathbf1,\mathbf3,0)
 \oplus(\mathbf1,\mathbf1,0)\\
 &\oplus(\mathbf3,\mathbf2,-\tfrac56)
 \oplus(\overline{\mathbf3},\mathbf2,+\tfrac56).
\end{aligned}
\tag{84.38}
$$

留下的中性单态可用$Y$表示，确实无迹。右边维数之和为$8+3+1+6+6=24$，所有阿贝尔荷也由行荷减列荷得到。这给出了伴随表示的完整分解。

对厄米的规范场矩阵，$C=B^\dagger$，所以最后两个共轭表示合起来描述十二个实重矢量，或等价的六个复矢量分量。前三项与$V$对易，仍为无质量场；后两项连接不同本征值块，必定有质量。右上块是$\mathbf3$和$\mathbf2$的外张量积，在直接积群下不可约；它有非零阿贝尔荷，也不会与左下块发生保持该荷的质量混合。稳定群不变性因而要求这六个复分量质量相同，共轭场具有同一质量。

这里的不可约性也可以从矩阵指标看出。若一个算符与全部$SU(3)$作用对易，固定其两个SU(2)指标后，每个$3\times3$块都须为单位矩阵的倍数：与所有对角相位对易先消去非对角元，再与两坐标间的转动对易使三个对角元相等。因此它只能为$I_3\otimes K$。再要求与全部$SU(2)$作用对易，同样使$K$成为$I_2$的倍数。若存在真不变子空间，其正交投影会与这些幺正变换对易，却既不是0也不是单位矩阵，这与上述结果矛盾。由此得出的简并并不需要预先知道共同质量的数值。

<span id="c84-su5-mass"></span>

## 一个矩阵元决定共同质量

选连接第1与第4个分量的半迹生成元

<span id="eq:c84-su5-mass-commutator"></span>

$$
\begin{aligned}
T^4&=\frac12(E_{14}+E_{41}),\\
[T^4,V]&=\frac{5v}{12}(E_{14}-E_{41}),\\
[T^4,V]^2&=-\frac{25v^2}{144}(E_{11}+E_{44}),\\
\operatorname{Tr}[T^4,V]^2&=-\frac{25v^2}{72}.
\end{aligned}
\tag{84.39}
$$

第二行用到了两个对角元的差$v/2-(-v/3)=5v/6$，再乘生成元中的$1/2$。第三行可由$E_{ij}E_{kl}=\delta_{jk}E_{il}$直接得到：两项自身的平方为零，两个交叉乘积分别给$-E_{11}$和$-E_{44}$。因此标准实分量归一下，

<span id="eq:c84-su5-heavy-mass"></span>

$$
\begin{aligned}
M^2&=-2g^2\operatorname{Tr}[T^4,V]^2
        =\frac{25}{36}g^2v^2,
&M&=\frac56gv,\\
M_{\rm lit}^2
   &=-g^2\operatorname{Tr}[T^4,V_{\rm lit}]^2
        =\frac{25}{72}g^2v_{\rm lit}^2,
&M_{\rm lit}&=\frac{5}{6\sqrt2}gv_{\rm lit}.
\end{aligned}
\tag{84.40}
$$

第一行来自式[（84.25）](#eq:c84-adjoint-mass)。第二行显示替代动能系数在相同数值矩阵背景下给出的质量，因而相差一个$\sqrt2$。要让两套变量描述同一背景，应按式[（84.27）](#eq:c84-adjoint-source-conversion)同时转换真空值：

<span id="eq:c84-su5-mass-conversion"></span>

$$
V_{\rm lit}=\sqrt2\,V,\qquad
v_{\rm lit}=\sqrt2\,v,\qquad
\frac{5}{6\sqrt2}gv_{\rm lit}=\frac56gv .
\tag{84.41}
$$

两种写法这时表示同一物理质量。动能与背景的重标度共同保持质量不变。

对任意连接前三行与后两列的生成元，背景本征值之差都为$5v/6$，上面的矩阵乘法完全相同；另外一种纯虚非对角生成元也有相同平方迹。因此十二个实重矢量全有式[（84.40）](#eq:c84-su5-heavy-mass)第一行的质量，与表示理论的简并结论一致。取$v\to0$时所有这些质量归零，完整的$SU(5)$规范对称性恢复；选择非零$v$后，哪些规范粒子有质量、如何组成剩余群的多重态，都已由背景及协变动能决定。

<span id="c84-vacuum-potential"></span>

## 伴随势怎样选择真空

上面的质量谱以给定背景为出发点。现在求出能选择该背景的标量势。取$m^2<0$，记$m_\Phi^2=-m^2>0$，并施加$\Phi\mapsto-\Phi$对称性：
<span id="eq:c84-adjoint-potential"></span>

$$
\mathcal V(\Phi)=-\frac{m_\Phi^2}{2}\operatorname{Tr}\Phi^2
 +\frac{\lambda_1}{4}\operatorname{Tr}\Phi^4
 +\frac{\lambda_2}{4}(\operatorname{Tr}\Phi^2)^2,
\qquad \Phi^\dagger=\Phi,\quad\operatorname{Tr}\Phi=0.
\tag{84.42}
$$

这是带该对称性的四维可重整多项式势；$\Phi\mapsto-\Phi$排除了三次项。真空的本征值分布由下面的极小化决定。

### 先把大小和方向分开

厄米矩阵能被幺正矩阵对角化。对角化矩阵再乘一个共同相位便可令行列式为1，共轭作用并不改变，所以用$SU(N)$共轭不会遗漏任何矩阵方向。对非零$\Phi$写
<span id="eq:c84-radial-direction"></span>

$$
\Phi=\rho U\operatorname{diag}(x_1,\ldots,x_N)U^\dagger,
\qquad \rho^2=\operatorname{Tr}\Phi^2,\qquad
\sum_i x_i=0,\quad\sum_i x_i^2=1.
\tag{84.43}
$$

$\rho$表示矩阵的迹范数；沿特定$Y$方向写成$\Phi=vY$时，$v$则是那个矩阵的系数。令$F(x)=\sum_i x_i^4$和$D(x)=\lambda_1F(x)+\lambda_2$，固定方向后的势为
<span id="eq:c84-radial-minimum"></span>

$$
\begin{aligned}
\mathcal V(\rho,x)&=-\frac{m_\Phi^2}{2}\rho^2+\frac{D(x)}4\rho^4,\\
\frac{\partial\mathcal V}{\partial\rho}&=\rho[-m_\Phi^2+D(x)\rho^2],\\
\rho_{\min}^2(x)&=\frac{m_\Phi^2}{D(x)},\qquad
\mathcal V_{\min}(x)=-\frac{(m_\Phi^2)^2}{4D(x)},
\qquad D(x)>0.
\end{aligned}
\tag{84.44}
$$

非零解处的径向二阶导数是$2m_\Phi^2>0$。两个四次不变量的方向部分分别为$A(x)=F(x)$、$B(x)=(\sum_i x_i^2)^2=1$。

若某一方向$D<0$，四次项使势沿$\rho\to\infty$无下界；即使$D=0$，负的二次项也仍使势无下界。所以有下界要求每个方向均有$D>0$。反过来，满足两个约束的方向集合是紧集，连续的$D$若处处正就有一个统一的正下界，四次项便能控制所有方向，故这一条件也充分。

最后，在有下界的情形，
<span id="eq:c84-energy-monotonicity"></span>

$$
\frac{d}{dD}\left[-\frac{(m_\Phi^2)^2}{4D}\right]
 =\frac{(m_\Phi^2)^2}{4D^2}>0.
\tag{84.45}
$$

所以$D$最小的方向给出最低势能，特别当$\lambda_1>0$时，问题变成在迹零、单位范数的约束下最小化四次和$F$。

### 驻点至多有三种本征值

两个约束的梯度$(1,\ldots,1)$和$x$线性独立；否则各$x_i$相同，由迹零只能全为零，与单位范数矛盾。因此在驻点可用两个拉格朗日乘子。对$\lambda_1\ne0$，把常数吸收入乘子后，有
<span id="eq:c84-stationary-cubic"></span>

$$
4x_i^3-2\sigma x_i-\tau=0,\qquad
P(z)=4z^3-2\sigma z-\tau.
\tag{84.46}
$$

每个实际本征值都是同一个三次多项式的根，所以至多有三种值。三种根全被占用时，它们之和为零，因为没有$z^2$项；只占用两根时，根和关系仍包括第三个未占用的根。

三值驻点结论需要$\lambda_1\ne0$。若$\lambda_1=0$、$\lambda_2>0$，势与所有归一方向无关，例如$N=5$时
<span id="eq:c84-lambda-zero-counterexample"></span>

$$
X=\frac1{\sqrt{10}}\operatorname{diag}(-2,-1,0,1,2)
\tag{84.47}
$$

有五个不同本征值，却仍是一个真空方向。

### 排除三值的最低点

现在取$\lambda_1,\lambda_2>0$，并先令$N\ge4$。约束空间紧，$F$一定取得绝对最小值。在三值驻点处，下面将构造满足约束的下降方向。

设三个不同本征值为$a<b<c$，重数分别为$r,s,t$。因为它们是$P$的全部根，$P(z)=4(z-a)(z-b)(z-c)$。记$\delta_1=b-a>0$、$\delta_2=c-b>0$，则
<span id="eq:c84-root-derivatives"></span>

$$
\begin{aligned}
P'(a)&=4\delta_1(\delta_1+\delta_2),\\
P'(b)&=-4\delta_1\delta_2,\\
P'(c)&=4\delta_2(\delta_1+\delta_2).
\end{aligned}
\tag{84.48}
$$

取满足切向约束$\sum_i z_i=\sum_i x_i z_i=0$的向量，沿曲线
<span id="eq:c84-constrained-curve"></span>

$$
x_i(\eta)=\frac{x_i+\eta z_i}{\sqrt{1+\eta^2\sum_jz_j^2}}
\tag{84.49}
$$

变化。这条曲线始终迹零、范数为1，且$x_i'(0)=z_i$、$x_i''(0)=-x_i\sum_jz_j^2$。用驻点方程和两个约束，有$4\sum_i x_i^4=2\sigma$，因此
<span id="eq:c84-constrained-second-variation"></span>

$$
\begin{aligned}
\left.\frac{d^2F}{d\eta^2}\right|_0
 &=\sum_i12x_i^2z_i^2
       -4\sum_i x_i^4\sum_jz_j^2\\
 &=\sum_i(12x_i^2-2\sigma)z_i^2
  =\sum_iP'(x_i)z_i^2.
\end{aligned}
\tag{84.50}
$$

第一导数为零；若这个二阶导数为负，驻点便不可能是最低点。

若$s\ge2$，只在两个等于$b$的位置取$z=+1,-1$，其余为零。两个切向约束都满足，二阶导数为$2P'(b)=-8\delta_1\delta_2<0$。因此最低点的中间本征值最多只能出现一次。

剩下$s=1$。对三个组内的每个位置分别取
<span id="eq:c84-three-group-tangent"></span>

$$
z_a=\frac{\delta_2}{r},\qquad
z_b=-(\delta_1+\delta_2),\qquad
z_c=\frac{\delta_1}{t}.
\tag{84.51}
$$

其分量和为$\delta_2-(\delta_1+\delta_2)+\delta_1=0$，与$x$的内积为$\delta_2(a-b)+\delta_1(c-b)=0$，故仍是允许方向。把三个重数都带入式[（84.50）](#eq:c84-constrained-second-variation)，得到
<span id="eq:c84-three-value-descent"></span>

$$
\begin{aligned}
F''(0)
 &=\frac{\delta_2^2}{r}P'(a)
   +(\delta_1+\delta_2)^2P'(b)+\frac{\delta_1^2}{t}P'(c)\\
 &=-4\delta_1\delta_2(\delta_1+\delta_2)
 \left[\delta_2\left(1-\frac1r\right)
             +\delta_1\left(1-\frac1t\right)\right].
\end{aligned}
\tag{84.52}
$$

当$N\ge4$时，$r+t=N-1\ge3$，至少一个重数大于1，所以括号严格正，二阶导数严格负。至此两种三值情形都被排除了。一个值又不能同时满足迹零和单位范数，故最低点一定恰有两个不同本征值。

### 比较两值的重数与未破缺群

设正本征值$a$有$k$个，负本征值$b$有$N-k$个。先解两个约束：
<span id="eq:c84-two-eigenvalues"></span>

$$
\begin{gathered}
ka+(N-k)b=0,\qquad ka^2+(N-k)b^2=1,\\
a=\sqrt{\frac{N-k}{Nk}},\qquad
b=-\sqrt{\frac{k}{N(N-k)}}.
\end{gathered}
\tag{84.53}
$$

代入四次和，便有
<span id="eq:c84-multiplicity-minimum"></span>

$$
F(k)=ka^4+(N-k)b^4
 =\frac{(N-k)^2}{N^2k}+\frac{k^2}{N^2(N-k)}
 =\frac{N}{k(N-k)}-\frac3N.
\tag{84.54}
$$

要使它最小，须使$k(N-k)$最大，也就是使两个重数尽可能接近。因此偶数$N$取$k=N/2$；奇数$N\ge5$取$k=(N\pm1)/2$，并有
<span id="eq:c84-sharp-fourth-moment"></span>

$$
F_{\min}=\begin{cases}
1/N,&N\text{为偶数},\\[2pt]
(N^2+3)/[N(N^2-1)],&N\ge5\text{为奇数}.
\end{cases}
\tag{84.55}
$$

保持这两个不同本征值块的群为$S(U(k)\times U(N-k))$。[中心化子计算](#c84-centralizer)已说明其李代数为$su(k)\oplus su(N-k)\oplus u(1)$。其全局群由这两个幺正块及总行列式约束确定。

$N=2$时，迹约束直接给两个相反本征值，上述偶数答案仍成立。$N=3$则是一个特殊情况：由$x+y+z=0$和$x^2+y^2+z^2=1$，
<span id="eq:c84-three-dimensional-flat-directions"></span>

$$
xy+yz+zx=-\frac12,\qquad
x^2y^2+y^2z^2+z^2x^2=\frac14,\qquad
x^4+y^4+z^4=\frac12.
\tag{84.56}
$$

第二个等式用$(xy+yz+zx)^2$展开，其中$2xyz(x+y+z)=0$；第三个等式再展开平方和的平方。所有归一方向因而简并。$\operatorname{diag}(-1,0,1)/\sqrt2$只留下$U(1)^2$，而$\operatorname{diag}(-1,-1,2)/\sqrt6$才留下$2+1$块的群。因此$N=3$时并非所有真空都具有$2+1$块结构；式[（84.52）](#eq:c84-three-value-descent)在$r=s=t=1$时恰好为零，也反映了这一退化。

### SU(5)的真空深度

取$N=5$，两种不同的重数组合给$F(1)=13/20$、$F(2)=7/30$，最低的是$2+3$。用本节的
$Y=\operatorname{diag}(-1/3,-1/3,-1/3,1/2,1/2)$表示该方向，有
<span id="eq:c84-su5-traces"></span>

$$
\operatorname{Tr}Y^2=\frac56,\qquad
\operatorname{Tr}Y^4=\frac{35}{216},\qquad
\frac{\operatorname{Tr}Y^4}{(\operatorname{Tr}Y^2)^2}=\frac7{30}.
\tag{84.57}
$$

由$\rho^2=5v^2/6$，径向解为
<span id="eq:c84-su5-vacuum-and-depth"></span>

$$
v^2=\frac{36m_\Phi^2}{7\lambda_1+30\lambda_2},\qquad
\Phi_{\min}=\pm vUYU^\dagger,\qquad
\mathcal V_{\min}=-\frac{15(m_\Phi^2)^2}{2(7\lambda_1+30\lambda_2)}.
\tag{84.58}
$$

正负两支由$\Phi\mapsto-\Phi$联系；由于两个块重数不同，它们不是同一个$SU(5)$共轭轨道。每支都留下$S(U(3)\times U(2))$。这个势同时确定真空方向和长度，也给出[第97节标量势](/posts/srednicki-97/#c97-potential)所需的真空。

---

[← 第 83 节](/posts/srednicki-83/) · [章节地图](/srednicki/) · [第 85 节 →](/posts/srednicki-85/)
