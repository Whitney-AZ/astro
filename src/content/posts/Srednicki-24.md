---
title: 'Srednicki §24 非阿贝尔对称性'
date: 2026-09-14
category: 笔记
tags: [物理, 量子场论, Srednicki]
series: 'Srednicki QFT'
srednickiSections: [24]
hideFromHome: true
draft: false
---

<span id="c24"></span>

前两节的两个实标量场可以在内部平面上转动，而拉格朗日量保持不变。若增加到三个或更多场，就有不同的转动平面，先作哪一次转动也会影响结果。这种次序上的区别是非阿贝尔对称性的主要特征。下面仍从标量模型出发，把内部转动写成无穷小矩阵，求出这些矩阵的代数，再说明同一代数怎样由诺特荷实现。随后推广到复场，构造酉群的生成元，并重新考察复场写法所显示的对称性是否已经包含模型的全部连续对称性。

仍采用四维正则标量，内部指标以欧氏内积收缩，时空指标则使用洛伦兹度规。

<span id="c24-real"></span>

## 从两实场推广到$N$个实场

先回到前两节的两实场模型。由于$\varphi=(\varphi_1+i\varphi_2)/\sqrt2$，复场范数等于两实场平方和的一半，原来的$\lambda(\varphi^\dagger\varphi)^2/4$就成为$\lambda(\varphi_1^2+\varphi_2^2)^2/16$。保留这个系数，把内部指标扩大到$i=1,\ldots,N$，便得到$N$实场模型：
<span id="eq:c24-real-model"></span>

$$
\mathcal L
=-\frac12\partial^\mu\varphi_i\partial_\mu\varphi_i
-\frac12m^2\varphi_i\varphi_i
-\frac{\lambda}{16}(\varphi_i\varphi_i)^2.
\tag{24.1}
$$

各个分量具有共同的质量，四次相互作用只依赖$r^2=\sum_i\varphi_i^2$，所以拉氏密度没有选出特殊的内部方向。在四维中，$[\varphi_i]=1$、$[m]=1$、$[\lambda]=0$，动能、质量项和四次项的质量维数均为4。

将$\varphi$看成实场列向量，这种内部各向同性提示我们作不依赖时空的正交变换：
<span id="eq:c24-so-action"></span>

$$
\varphi\longmapsto R\varphi,\qquad
R^{\mathsf T}R=I,\qquad\det R=1.
\tag{24.2}
$$

这些矩阵组成特殊正交群$SO(N)$。由于$R$是常数，导数也按同一矩阵变换，即$\partial_\mu(R\varphi)=R\partial_\mu\varphi$。所以场的平方和与导数的内积分别变为
<span id="eq:c24-quadratic-invariants"></span>

$$
\begin{aligned}
(R\varphi)^{\mathsf T}(R\varphi)&=\varphi^{\mathsf T}R^{\mathsf T}R\varphi=r^2,\\
\partial^\mu(R\varphi)^{\mathsf T}\partial_\mu(R\varphi)
&=\partial^\mu\varphi^{\mathsf T}R^{\mathsf T}R\partial_\mu\varphi
=\partial^\mu\varphi_i\partial_\mu\varphi_i.
\end{aligned}
\tag{24.3}
$$

质量项正比于$r^2$，四次势正比于它的平方，因而连同动能一起保持不变。这个计算只使用了正交条件，尚未使用$\det R=1$，所以完整的正交对称性实际上是$O(N)$。

要在连续转动之外增加离散反射，可以先考虑所有场同时变号。这个操作能否增加一个分支，要看$N$的奇偶。比较全体变号与单轴反射的行列式：
<span id="eq:c24-reflection-branches"></span>

$$
\det(-I_N)=(-1)^N,\qquad
F=\operatorname{diag}(-1,1,\ldots,1),\qquad\det F=-1.
\tag{24.4}
$$

当$N$为偶数时，$-I_N$已经属于$SO(N)$，再把它加入并不会增加新分支。对任意$N$都适用的选择是单轴反射$F$：若$O$是负行列式的正交矩阵，$FO$便有正行列式，于是$O=F(FO)$。这样，完整的正交群可写成$O(N)=SO(N)\cup FSO(N)$。以下着重研究其中与恒等元相连的部分。

为什么$SO(N)$中的每一个矩阵都能由平面转动连续得到，也可以直接说明。先在第1轴与其他轴构成的平面中依次转动，把第一列这个单位向量的末尾分量逐个消去，最后使它成为第一坐标向量。由于其余列与第一列正交，它们的第一行元素也全为零，剩下的变换就在一个$SO(N-1)$块内。逐列重复这个过程，最终的一维块由行列式为1固定为$+1$。反向施加刚才的平面转动，就恢复了任意给定的$R$；每一步的角度都可从零连续增加，因而整个矩阵也与恒等元连续相连。

<span id="c24-lie"></span>

## 无穷小变换与李代数

要描述所有这些连续转动，先求单位元附近允许的变化。写成$R=I+\theta+O(\theta^2)$，代入正交条件并保留一次项，有
<span id="eq:c24-orthogonal-tangent"></span>

$$
R^{\mathsf T}R
=I+\theta^{\mathsf T}+\theta+O(\theta^2),
\qquad \theta^{\mathsf T}=-\theta.
\tag{24.5}
$$

$\theta$为实矩阵，因为原来的$R$为实；反对称性又使其对角元为零，下三角由上三角决定。因此上三角的$N(N-1)/2$个实数，就是独立的无穷小转动参数。

为了把这些方向与量子理论中的厄米生成元对应起来，选择一组纯虚厄米矩阵来表示实反对称变化。令矩阵单位$E_{rs}$只有第$r$行、第$s$列的元素为1，其余为零，定义
<span id="eq:c24-so-basis"></span>

$$
T^{rs}=-i(E_{rs}-E_{sr}),\quad r<s,
\qquad
(T^{rs})^\dagger=T^{rs},\quad
(T^{rs})^{\mathsf T}=-T^{rs}.
\tag{24.6}
$$

每个矩阵的上三角只有一个$-i$，对应的下三角为$+i$，正好对应一个转动平面。利用矩阵单位的乘法$E_{ij}E_{kl}=\delta_{jk}E_{il}$，可以求出这些基矩阵的迹内积：
<span id="eq:c24-trace-normalization"></span>

$$
\operatorname{Tr}(T^{rs}T^{uv})
=2(\delta_{ru}\delta_{sv}-\delta_{rv}\delta_{su})
=2\delta^{ab},
\tag{24.7}
$$

最后一步把两组上三角位置分别编号为$a,b$。相同位置的矩阵平方在两个对角元上各给1，不同位置的乘积则没有迹贡献，因此这是一组迹正交基。每个允许的$\theta$都能唯一展开为
<span id="eq:c24-generator-coordinates"></span>

$$
\theta=-i\theta^aT^a,\qquad
\theta^a=\frac i2\operatorname{Tr}(T^a\theta).
\tag{24.8}
$$

在第一式两边乘$T^a$并取迹，便得到第二式的投影系数。这里要分清$\theta_{rs}$这个矩阵元素与$\theta^a$这个基底系数；按照式[（24.6）](#eq:c24-so-basis)给定的符号，同一位置有$\theta^{(rs)}=-\theta_{rs}$。

有了无穷小生成元，还须考察连续作两个转动时发生什么。两个转动的先后差别由群交换子给出。按$R'^{-1}R^{-1}R'R$的次序，令$A=-i\theta^aT^a$、$B=-i\theta'^bT^b$，把$R=e^A$、$R'=e^B$连同各自的逆矩阵逐次展开，得到
<span id="eq:c24-group-commutator"></span>

$$
\begin{aligned}
R'^{-1}R^{-1}R'R
&=I+BA-AB+O(3)\\
&=I+\theta^a\theta'^b[T^a,T^b]+O(3).
\end{aligned}
\tag{24.9}
$$

这里$O(3)$表示两个小角参数的总次数至少为3。四个因子相乘时，所有一次项和纯$A^2,B^2$项都相消，最先留下的是每种参数各出现一次的混合项。这个乘积仍在$SO(N)$内，故其领先变化也必须满足式[（24.5）](#eq:c24-orthogonal-tangent)的实反对称条件。再乘以负的虚数单位，$-i[T^a,T^b]$便属于原来的厄米基所张成的空间，因此可写为
<span id="eq:c24-lie-algebra"></span>

$$
[T^a,T^b]=if^{abc}T^c.
\tag{24.10}
$$

这些实数$f^{abc}$称为结构系数（structure constants），上面的对易关系规定了生成元的李代数（Lie algebra）。按照式[（24.9）](#eq:c24-group-commutator)的乘法次序，混合项对应的新转动参数为$\theta''{}^c=-f^{abc}\theta^a\theta'^b$，所以结构系数定量描述了两种无穷小转动不对易时产生的第三种转动。

要从具体矩阵中求出结构系数，只需在对易关系两边乘$T^d$取迹。使用已经选定的迹归一化2，就得到
<span id="eq:c24-structure-trace"></span>

$$
f^{abd}=-\frac i2\operatorname{Tr}([T^a,T^b]T^d).
\tag{24.11}
$$

对易子使结构系数在交换$a,b$时变号，其余指标的性质则由迹的循环性确定：
<span id="eq:c24-cyclic-structure"></span>

$$
\operatorname{Tr}([T^a,T^b]T^c)
=\operatorname{Tr}(T^a[T^b,T^c])
=\operatorname{Tr}([T^b,T^c]T^a),
\tag{24.12}
$$

所以$f^{abc}=f^{bca}$。循环置换不变与前两个指标反对称相结合，便使任意两个指标互换都改变符号。生成元的厄米性还保证结构系数为实数：记$z=\operatorname{Tr}([T^a,T^b]T^c)$，取复共轭并将矩阵次序反转，有
<span id="eq:c24-structure-reality"></span>

$$
z^*=\operatorname{Tr}\bigl(T^c[T^a,T^b]^\dagger\bigr)
=-\operatorname{Tr}\bigl(T^c[T^a,T^b]\bigr)=-z.
\tag{24.13}
$$

于是$z$纯虚，式[（24.11）](#eq:c24-structure-trace)中的$-iz/2$为实。这里完全反对称的三指标形式与所选的迹正交基相配；迹内积同时给生成元标签规定了内部度规。

若结构系数全为零，各个生成元互相对易，其指数也就互相对易，所以由它们生成的连通群是阿贝尔群（Abelian group）。$U(1)$和$SO(2)$各自只有一个生成元，必然属于这种情形。若存在不对易的生成元，群便是非阿贝尔群（non-Abelian group）。本节最先遇到的例子是$SO(3)$。

<span id="c24-so3"></span>

## $SO(3)$及守恒荷的实现

三个内部方向的转动可以用列维–奇维塔符号统一表示。取$\epsilon^{123}=1$，并定义
<span id="eq:c24-so3-generators"></span>

$$
(T^a)_{ij}=-i\epsilon^{aij},\qquad a,i,j=1,2,3.
\tag{24.14}
$$

要确定它们的代数，先把两个生成元相乘，缩并共同的矩阵指标：
<span id="eq:c24-so3-product"></span>

$$
\begin{aligned}
(T^aT^b)_{ij}
&=-\sum_k\epsilon^{aik}\epsilon^{bkj}
=\sum_k\epsilon^{aik}\epsilon^{bjk}\\
&=\delta^{ab}\delta^{ij}-\delta^{aj}\delta^{ib}.
\end{aligned}
\tag{24.15}
$$

最后一步的缩并可以按非零项逐一理解。若$(a,i)$或$(b,j)$这一对中有相等的指标，两边都为零；否则每个反对称符号只在第三个不同指标处非零。两组无序指标对不同时，没有共同的非零求和项；两组相同且方向一致时给$+1$，方向相反时给$-1$，这正由右边两个delta乘积之差表示。

在乘积结果中交换$a,b$再相减，共同的对角项消去，留下
<span id="eq:c24-so3-commutator"></span>

$$
\begin{aligned}
\relax[T^a,T^b]_{ij}
&=\delta^{ai}\delta^{bj}-\delta^{aj}\delta^{bi}\\
&=\epsilon^{abc}\epsilon^{cij}
=i\epsilon^{abc}(T^c)_{ij}.
\end{aligned}
\tag{24.16}
$$

由此读出$f^{abc}=\epsilon^{abc}$。同一乘积也确定了归一化：在式[（24.15）](#eq:c24-so3-product)中令$i=j$求和，结果是$3\delta^{ab}-\delta^{ab}=2\delta^{ab}$，与本节的迹内积一致。当$N\ge3$时，只转动前三个分量就已经包含这组不对易生成元，因此$SO(N)$也为非阿贝尔群。

这些矩阵对易关系怎样体现在场的量子变换中，可以由诺特荷求出。把提出转动参数后的场变分$\delta_a\varphi_i=-iT^a_{ij}\varphi_j$代入第22节的诺特公式，得到
<span id="eq:c24-noether-real"></span>

$$
j^{a\mu}=i\partial^\mu\varphi_iT^a_{ij}\varphi_j,
\qquad
Q^a=-i\int d^3x\,\Pi_iT^a_{ij}\varphi_j.
\tag{24.17}
$$

流的时间分量中，$\partial^0\varphi_i=-\Pi_i$给出了荷前的负号。对势求导时，$\partial(r^2)^2/\partial\varphi_i=4r^2\varphi_i$，场方程因而为$\Box\varphi_i=(m^2+\lambda r^2/4)\varphi_i$。代入流的散度后，只出现$\varphi_iT^a_{ij}\varphi_j$和$\partial^\mu\varphi_iT^a_{ij}\partial_\mu\varphi_j$这两种内部缩并。场的乘积在内部指标下对称，生成元反对称，故两项都为零。

沿用第22节关于总荷的共同调节、边界和定义域条件，正则对易关系进一步给出这些荷在场上的作用：
<span id="eq:c24-charge-representation"></span>

$$
\begin{gathered}
\relax[\varphi_i,Q^a]=T^a_{ij}\varphi_j,\qquad
[Q^a,Q^b]=if^{abc}Q^c,\\
U(\theta)^{-1}\varphi U(\theta)=e^{-i\theta^aT^a}\varphi.
\end{gathered}
\tag{24.18}
$$

这里 $U(\theta)=e^{-i\theta^aQ^a}$。第一式的收缩是

<span id="eq:c24-field-charge-contraction"></span>

$$
[\varphi_\ell(\mathbf x),Q^a]
=-i\int d^3y\,i\delta_{\ell i}\delta^3(\mathbf x-\mathbf y)
 T^a_{ij}\varphi_j(\mathbf y)
=T^a_{\ell j}\varphi_j(\mathbf x).
$$

荷之间的对易子也可直接计算。先把空间分成有限个体积为 $v$ 的单元，令 $q_{\ell i}=\sqrt v\,\varphi_i(\mathbf x_\ell)$、$p_{\ell i}=\sqrt v\,\Pi_i(\mathbf x_\ell)$，则 $[q_{\ell i},p_{m j}]=i\delta_{\ell m}\delta_{ij}$，而 $Q^a=-i\sum_\ell p_{\ell i}T^a_{ij}q_{\ell j}$。不同单元的变量对易，同一单元内有

<span id="eq:c24-bilinear-charge-algebra"></span>

$$
\begin{aligned}
\relax[p_iq_j,p_kq_l]
&=p_ip_kq_jq_l+i\delta_{jk}p_iq_l
 -p_kp_iq_lq_j-i\delta_{il}p_kq_j\\
&=i\delta_{jk}p_iq_l-i\delta_{il}p_kq_j,\\
L(A)&=\sum_\ell p_{\ell i}A_{ij}q_{\ell j},\qquad
[L(A),L(B)]=iL(AB-BA),\\
[Q^a,Q^b]&=-iL([T^a,T^b])
=f^{abc}L(T^c)=if^{abc}Q^c.
\end{aligned}
$$

两个四算符乘积相消，余下两次正则收缩恰好组成矩阵对易子。$T^{a*}=-T^a$ 及 $\operatorname{Tr}T^a=0$ 还给 $(Q^a)^\dagger=Q^a+\sum_\ell\operatorname{Tr}T^a=Q^a$，所以这些荷为厄米算符。连续总荷采用上述共同调节与定义域下的极限。

最后令 $F(s)=e^{is\theta^aQ^a}\varphi e^{-is\theta^aQ^a}$。场与荷的对易关系使 $F'(s)=-i\theta^aT^aF(s)$，初值为 $F(0)=\varphi$，解得 $F(s)=e^{-is\theta^aT^a}\varphi$。取 $s=1$ 就得到式[（24.18）](#eq:c24-charge-representation)中的有限变换。内部矩阵的代数由守恒荷实现；这些荷彼此不对易，通常也就不能同时对角化。

还应把这里的参数方向与第22节的平面旋转对应起来。当$N=2$时，本节$T^{12}$的指数为
<span id="eq:c24-so2-conversion"></span>

$$
e^{-i\vartheta T^{12}}
=\begin{pmatrix}\cos\vartheta&-\sin\vartheta\\
                 \sin\vartheta&\cos\vartheta\end{pmatrix},
\qquad
\vartheta=-\alpha,\quad Q^{12}=-Q_{22}.
\tag{24.19}
$$

它与第22节的复相位$e^{-i\alpha}$描述同一组平面转动，只是角度方向相反。角参数与诺特荷同时变号，就使$\vartheta Q^{12}=\alpha Q_{22}$保持不变，因而态空间中的有限变换也一致。

<span id="c24-unitary"></span>

## 复多重态与特殊酉群

现在把场换成$N$个复标量，并使拉氏密度依赖它们的共同范数：
<span id="eq:c24-complex-model"></span>

$$
\mathcal L
=-\partial^\mu\varphi^\dagger\partial_\mu\varphi
-m^2\varphi^\dagger\varphi
-\frac{\lambda}{4}(\varphi^\dagger\varphi)^2.
\tag{24.20}
$$

$\varphi$为列向量，$\varphi^\dagger$为行向量，因此在常数酉矩阵作用下，两者分别从左、右接受变换：
<span id="eq:c24-unitary-action"></span>

$$
\varphi\longmapsto U\varphi,\qquad
\varphi^\dagger\longmapsto\varphi^\dagger U^\dagger,
\qquad U^\dagger U=I,
\tag{24.21}
$$

范数成为$\varphi^\dagger U^\dagger U\varphi$，动能在两个导数之间也出现同一个$U^\dagger U$，所以各项都回到原来的形式。复场范数的不变性由此引出了酉群。

酉矩阵的行列式满足$|\det U|=1$，可写成$\det U=e^{i\beta}$。若把这个相位从矩阵中提出来，余下的部分就有单位行列式。具体地，选择实数$\theta$使$e^{-iN\theta}=\det U$，再定义$\widetilde U=e^{i\theta}U$，便有
<span id="eq:c24-unitary-phase"></span>

$$
U=e^{-i\theta}\widetilde U,\qquad
\widetilde U^\dagger\widetilde U=I,\qquad
\det\widetilde U=1.
\tag{24.22}
$$

单位行列式的酉矩阵称为特殊酉矩阵（special unitary matrix），组成$SU(N)$。两个这样的矩阵相乘仍为酉矩阵，行列式仍是1；逆矩阵也保持这两个条件，所以它们构成群。

分解式[（24.22）](#eq:c24-unitary-phase)表明，每个酉变换都能分离出整体相位，但这种分离有重复：$\theta$有$N$种相差$2\pi/N$的选择。为了确定整体相位与特殊酉部分怎样共同组成酉群，引入乘法映射并求它的核：
<span id="eq:c24-unitary-quotient"></span>

$$
\begin{aligned}
F:U(1)\times SU(N)&\longrightarrow U(N),\qquad F(z,V)=zV,\\
\ker F&=\{(z,z^{-1}I_N):z^N=1\},\\
U(N)&\simeq[U(1)\times SU(N)]/\mathbb Z_N.
\end{aligned}
\tag{24.23}
$$

上面的相位分解保证第一行的映射满射。若$zV=I$，则$V=z^{-1}I$；同时$\det V=1$又要求$z^N=1$，所以第二行恰好列出了全部核元素。表示同一个$U$的不同参数组，正是相差这些核元素的参数组，故全局群关系中须除去这个共同的有限中心。有限离散核在单位元附近没有切向方向，因而本节所需的局部李代数分解仍为$\mathfrak u(N)=\mathfrak u(1)\oplus\mathfrak{su}(N)$。

接下来求特殊酉部分的生成元。在单位元附近写成$\widetilde U=I-i\theta^aT^a+O(\theta^2)$，先展开酉条件：
<span id="eq:c24-su-hermiticity"></span>

$$
\widetilde U^\dagger\widetilde U
=I+i\theta^a[(T^a)^\dagger-T^a]+O(\theta^2),
\qquad (T^a)^\dagger=T^a.
\tag{24.24}
$$

一次项给出生成元的厄米性，单位行列式则继续约束它们的迹。直接从行列式的排列定义看，恒等排列给出$\prod_i(1+\epsilon A_{ii})=1+\epsilon\sum_iA_{ii}+O(\epsilon^2)$；任何非恒等排列都至少使用两个非对角元，因而不会贡献一次项。于是
<span id="eq:c24-traceless-condition"></span>

$$
\det(I+\epsilon A)=1+\epsilon\operatorname{Tr}A+O(\epsilon^2),
\qquad \operatorname{Tr}T^a=0.
\tag{24.25}
$$

这个条件也可以用矩阵对数来推导。令$A=e^{-iH}$，其中$H$厄米，可以通过谱分解将其对角化。若本征值为$h_i$，指数矩阵的本征值就是$e^{-ih_i}$，所以$\det e^{-iH}=e^{-i\sum_i h_i}=e^{-i\operatorname{Tr}H}$。在单位元附近，两边取从零连续延伸的同一对数分支，便得到$\ln\det A=\operatorname{Tr}\ln A$；其一次展开与式[（24.25）](#eq:c24-traceless-condition)相同。

<span id="c24-basis"></span>

## 构造$SU(N)$的一组归一生成元

确定了厄米、无迹两个条件之后，就可以数出生成元并构造一组基。一个厄米$N\times N$矩阵有$N$个实对角元和$N(N-1)/2$个任意复上三角元，下三角由厄米性固定；无迹条件再去掉一个实自由度，故所需空间的实维数为$N^2-1$。

先把非对角部分分成两族。第一族采用式[（24.6）](#eq:c24-so-basis)中的$A_{rs}=-i(E_{rs}-E_{sr})$，第二族取实对称矩阵$S_{rs}=E_{rs}+E_{sr}$，两族均令$r<s$。矩阵单位的乘法给出
<span id="eq:c24-offdiagonal-bases"></span>

$$
\begin{aligned}
\operatorname{Tr}(A_{rs}A_{uv})
&=\operatorname{Tr}(S_{rs}S_{uv})
=2\delta_{ru}\delta_{sv},\\
\operatorname{Tr}(A_{rs}S_{uv})&=0.
\end{aligned}
\tag{24.26}
$$

同一位置的矩阵平方都为$E_{rr}+E_{ss}$，两族之间的交叉积迹为$-i+i=0$，不同位置的乘积则没有对角贡献。因此每一族都有$N(N-1)/2$个彼此正交的矩阵，两族之间也正交。

剩下的是无迹的对角部分。先列出连续若干个1、随后一个负数、其余为零的条目；要求平方迹与前两族相同，就确定其归一化系数。所得矩阵为
<span id="eq:c24-diagonal-basis"></span>

$$
D_n=\sqrt{\frac{2}{n(n+1)}}\,
\operatorname{diag}(\underbrace{1,\ldots,1}_{n},-n,0,\ldots,0),
\quad n=1,\ldots,N-1.
\tag{24.27}
$$

在乘归一化系数之前，矩阵的迹为$n-n=0$，平方迹为$n+n^2=n(n+1)$，故所取系数使$\operatorname{Tr}D_n^2=2$。两个不同对角基也互相正交：若$n<m$，未归一矩阵相乘后的迹为$n-n=0$，因为前$n$项各给1，第$n+1$项给$-n$，而其余项在较短的矩阵中均为零。因此$\operatorname{Tr}(D_nD_m)=2\delta_{nm}$。对角矩阵与非对角矩阵相乘没有对角贡献，迹也为零。

将三族的数目相加，得到
<span id="eq:c24-su-dimension"></span>

$$
\frac{N(N-1)}2+\frac{N(N-1)}2+(N-1)=N^2-1.
\tag{24.28}
$$

这些矩阵彼此正交且范数非零，因而线性独立；数目又等于整个厄米无迹空间的维数，所以它们构成完备基。前面通过对易子和迹提取结构系数的方法，现在可以直接用于$SU(N)$。

最小的例子是$SU(2)$。按$\sigma^1,\sigma^2,\sigma^3$的次序写出泡利矩阵：
<span id="eq:c24-pauli"></span>

$$
\sigma^1=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
\sigma^2=\begin{pmatrix}0&-i\\i&0\end{pmatrix},\quad
\sigma^3=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
\tag{24.29}
$$

它们正是上述构造中的$(S_{12},A_{12},D_1)$。三个矩阵的平方都等于$I$；相乘有$\sigma^1\sigma^2=\operatorname{diag}(i,-i)=i\sigma^3$，反序相乘则给$-i\sigma^3$。另两组按循环次序相乘也有相同的结构，故
<span id="eq:c24-su2-factor"></span>

$$
[\sigma^a,\sigma^b]=2i\epsilon^{abc}\sigma^c,
\qquad \operatorname{Tr}(\sigma^a\sigma^b)=2\delta^{ab}.
\tag{24.30}
$$

在本节的迹归一化2下，结构系数因此为$2\epsilon^{abc}$。若把生成元整体减半，取$t^a=\sigma^a/2$，相应的两种关系就变成
<span id="eq:c24-su2-rescaling"></span>

$$
[t^a,t^b]=i\epsilon^{abc}t^c,\qquad
\operatorname{Tr}(t^at^b)=\frac12\delta^{ab}.
\tag{24.31}
$$

这种归一化改变还要与参数配合：为表示同一个有限变换，角参数须增为原来的两倍，相应的诺特荷则减半，使角乘生成元、角乘荷均保持原值。因此，结构系数的整体因子随基底归一化一起改变。

有限转动还可以区分这两个群。例如$e^{-i2\pi\sigma^3/2}=-I_2$，而$SO(3)$的三阶矩阵在转过$2\pi$后已成为$I_3$。所以相同形式的无穷小对易关系，还须结合具体矩阵的有限变换来使用。

<span id="c24-enhancement"></span>

## 从复场写法看更大的实对称性

有了酉群的构造，再回到最初的复场模型。式[（24.20）](#eq:c24-complex-model)实际上还有更多的连续对称性。要看见它们，把每个复场拆为两个实分量：
<span id="eq:c24-complex-to-real"></span>

$$
\varphi_j=\frac{\varphi_{j1}+i\varphi_{j2}}{\sqrt2},
\qquad
\sum_j\varphi_j^\dagger\varphi_j
=\frac12\sum_j(\varphi_{j1}^2+\varphi_{j2}^2).
\tag{24.32}
$$

动能中的两种交叉项相消，得到两份系数为$-1/2$的实动能；四次项中的范数平方再带来因子$1/4$，使其系数成为$-\lambda/16$。所以整个拉氏密度恰好是式[（24.1）](#eq:c24-real-model)的$2N$实分量版本，完整的正交对称性为$O(2N)$，其中的连续部分为$SO(2N)$。

原来直接看出的$U(N)$正是这个连续群的一个子群。为把嵌入写清，暂将实部和虚部分别排列成$q=(\varphi_{11},\ldots,\varphi_{N1},\varphi_{12},\ldots,\varphi_{N2})^{\mathsf T}$。若复矩阵写为$U=A+iB$，对实分量的作用便是
<span id="eq:c24-unitary-real-embedding"></span>

$$
q\longmapsto R(U)q,\qquad
R(U)=\begin{pmatrix}A&-B\\B&A\end{pmatrix}.
\tag{24.33}
$$

展开$U^\dagger U=I$，实部给出$A^{\mathsf T}A+B^{\mathsf T}B=I$，虚部给出$A^{\mathsf T}B=B^{\mathsf T}A$；代入实矩阵的块乘积，就有$R(U)^{\mathsf T}R(U)=I$。还须确定其行列式的符号。把$q$换成复化的坐标$(\varphi,\varphi^*)$后，$R(U)$相似于$\operatorname{diag}(U,U^*)$，所以
<span id="eq:c24-embedding-determinant"></span>

$$
\det R(U)=\det U\,(\det U)^*=1,
\qquad U(N)\subset SO(2N).
\tag{24.34}
$$

这个嵌入既保持实范数，也保持选定的复线性结构；一般的$SO(2N)$转动只要求实范数不变，因此还可能包含混合场与共轭场的变换。数出这些额外方向，两个群的维数差为
<span id="eq:c24-extra-directions"></span>

$$
N(2N-1)-N^2=N(N-1).
\tag{24.35}
$$

可见，$N\ge2$时存在额外的连续变换；$N=1$时维数差为零，回到已经熟悉的$U(1)\simeq SO(2)$。以$N=2$为例，只让两个实部相互转动，虚部保持不动。取$\delta\varphi_{11}=-\beta\varphi_{21}$、$\delta\varphi_{21}=\beta\varphi_{11}$，改写回复场便得到
<span id="eq:c24-extra-rotation-example"></span>

$$
\delta\varphi_1=-\frac\beta2(\varphi_2+\varphi_2^\dagger),
\qquad
\delta\varphi_2=\frac\beta2(\varphi_1+\varphi_1^\dagger).
\tag{24.36}
$$

这个转动保持所有实分量的平方和，但含有$\varphi^\dagger$，所以它超出了对复列向量$\varphi$作$U(2)$线性变换的范围。它说明额外对称性来自拉氏密度对全部实分量的同等对待，而复场写法只直接显示了其中保持复线性的一部分。

<span id="c24-symplectic"></span>

## 保持辛形式的变换

同一计数方法也适用于反对称双线性形式。取实矩阵 $S$ 保持

<span id="eq:c24-symplectic-form"></span>

$$
S\eta S^{\mathsf T}=\eta,\qquad
\eta=\begin{pmatrix}0&I_N\\-I_N&0\end{pmatrix},\qquad
\eta^{\mathsf T}=-\eta,\quad\eta^2=-I_{2N}.
$$

这些矩阵组成实辛群 $\operatorname{Sp}(2N,\mathbb R)$。令 $S=I+X+O(X^2)$，展开到一次阶，再将 $X$ 分块，得到

<span id="eq:c24-symplectic-blocks"></span>

$$
\begin{aligned}
X\eta+\eta X^{\mathsf T}&=0,\qquad
X=\begin{pmatrix}a&b\\c&d\end{pmatrix},\\
X\eta+\eta X^{\mathsf T}
&=\begin{pmatrix}-b+b^{\mathsf T}&a+d^{\mathsf T}\\
 -d-a^{\mathsf T}&c-c^{\mathsf T}\end{pmatrix}.
\end{aligned}
$$

因此 $a$ 任意、$b,c$ 对称、$d=-a^{\mathsf T}$。每个这样的 $X$ 都能产生群内曲线，因为

$$
\frac d{dt}(e^{tX}\eta e^{tX^{\mathsf T}})
=e^{tX}(X\eta+\eta X^{\mathsf T})e^{tX^{\mathsf T}}=0,
$$

而 $t=0$ 时初值为 $\eta$。所以独立生成元数正是这些自由矩阵元的总数：

<span id="eq:c24-symplectic-dimension"></span>

$$
\dim_{\mathbb R}\operatorname{Sp}(2N,\mathbb R)
=N^2+2\frac{N(N+1)}2=N(2N+1).
$$

例如 $N=1$ 时，直接相乘给 $S\eta S^{\mathsf T}=(\det S)\eta$，故 $\operatorname{Sp}(2,\mathbb R)=\operatorname{SL}(2,\mathbb R)$，具有三个生成元。由保持条件找出无穷小矩阵、求对易子、再构造其场论实现的方法，还将在[非阿贝尔规范理论](/posts/srednicki-69/#c69)和[群表示](/posts/srednicki-70/#c70)中继续使用。

---

[← 第 23 节](/posts/srednicki-23/) · [章节地图](/srednicki/) · [第 25 节 →](/posts/srednicki-25/)
