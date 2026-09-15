---
title: 'Srednicki §69 非阿贝尔规范理论'
date: 2026-09-14
category: 笔记
tags: [物理, 量子场论, Srednicki]
series: 'Srednicki QFT'
srednickiSections: [69]
hideFromHome: true
draft: false
---

<span id="c69"></span>

量子电动力学的物质场在每一点作相位变换，电磁势则作相应的改变，使协变导数与物质场一起变换。第24节已经遇到另一类内部对称性：一个变换可以把多重态的不同分量混合起来，而且两个变换的先后次序通常不能交换。现在把这种整体对称性也推广为局域对称性。所需的规范势不再是一个实函数，而是一组实函数组成的矩阵；矩阵之间的不对易性还会使规范场产生自身的相互作用。

先从整体对称的物质拉格朗日量出发，构造协变导数及场强，再用量子色动力学说明各个指标的物理意义。时空度规仍为$(-,+,+,+)$。本节的$g$是非阿贝尔规范耦合，暂不加入重整化因子；它与前面带符号的电子电荷$e$分别定义。

<span id="c69-local-symmetry"></span>

## 从整体变换到局域变换

设$\phi_i$是一个含$N$个分量的标量或旋量多重态，物质拉格朗日量在
<span id="eq:c69-global-multiplet"></span>

$$
\phi_i(x)\longmapsto U_{ij}\phi_j(x),\qquad
U^\dagger U=\mathbf1,\qquad \det U=1
\tag{69.1}
$$

下不变，其中$U$与$x$无关。这是特殊酉群$SU(N)$的整体对称性；若场为实，$U$取实正交矩阵，便得到特殊正交群$SO(N)$的相应构造。“特殊”在这里指行列式等于1。内部矩阵不作用于时空指标，也不作用于旋量指标。

如果让$U$依赖于$x$，普通导数多出一项：
<span id="eq:c69-local-derivative"></span>

$$
\partial_\mu\phi'
=U\partial_\mu\phi+(\partial_\mu U)\phi .
\tag{69.2}
$$

动能中的这项不能由原来的整体对称性消去。引入协变导数$D_\mu$，要求它满足
<span id="eq:c69-covariance-requirement"></span>

$$
D'_\mu\phi'=UD_\mu\phi,\qquad
D'_\mu=UD_\mu U^\dagger .
\tag{69.3}
$$

第二式是微分算符等式：右端的$D_\mu$也作用在$U^\dagger$上。这一要求规定了新引入的规范场怎样补偿式[（69.2）](#eq:c69-local-derivative)中的附加项。

先回顾阿贝尔情形。沿第58节，取$U=e^{-ie\Gamma(x)}$及$D_\mu=\partial_\mu-ieA_\mu$。对任意测试场$h$展开右端，
<span id="eq:c69-abelian-connection"></span>

$$
\begin{aligned}
UD_\mu U^\dagger h
&=U\partial_\mu(U^\dagger h)-ieUA_\mu U^\dagger h\\
&=\partial_\mu h+
 [U(\partial_\mu U^\dagger)-ieUA_\mu U^\dagger]h,\\
A'_\mu&=UA_\mu U^\dagger+\frac{i}{e}U\partial_\mu U^\dagger .
\end{aligned}
\tag{69.4}
$$

比较第二行与$(\partial_\mu-ieA'_\mu)h$就确定了最后一行的系数。此时各量可交换，$UA_\mu U^\dagger=A_\mu$，而$U\partial_\mu U^\dagger=ie\,\partial_\mu\Gamma$，因此
<span id="eq:c69-abelian-shift"></span>

$$
A'_\mu=A_\mu-\partial_\mu\Gamma .
\tag{69.5}
$$

这与第54节的电磁势变换相同。接下来的构造保留式[（69.3）](#eq:c69-covariance-requirement)，只把其中的相位和势改为内部矩阵。

<span id="c69-generators"></span>

## 生成元与本节的归一

以$SU(N)$、$N\ge2$为例。在单位矩阵附近写成
<span id="eq:c69-infinitesimal-generators"></span>

$$
\begin{aligned}
U&=\mathbf1-ig\theta^aT^a+O(\theta^2),\\
U^\dagger U
&=\mathbf1+ig\theta^a(T^{a\dagger}-T^a)+O(\theta^2),\\
\det U&=1-ig\theta^a\operatorname{Tr}T^a+O(\theta^2).
\end{aligned}
\tag{69.6}
$$

实参数$\theta^a$可独立选择，故酉性与行列式条件分别要求$T^{a\dagger}=T^a$和$\operatorname{Tr}T^a=0$。一个厄米矩阵有$N$个实对角分量和$N(N-1)$个实非对角分量，去掉一个迹条件后剩$N^2-1$个独立方向。因此生成元指标$a$取$1,\ldots,N^2-1$，矩阵指标$i,j$仍取$1,\ldots,N$。耦合$g$被放进指数，是本节的归一选择。

两个厄米无迹生成元的对易子反厄米且无迹，所以$-i[T^a,T^b]$还可在同一实基中展开。这就定义实结构系数：
<span id="eq:c69-lie-bracket"></span>

$$
[T^a,T^b]=if^{abc}T^c,\qquad
f^{abc}\in\mathbb R,\qquad f^{abc}=-f^{bac}.
\tag{69.7}
$$

如果这些系数不全为零，变换次序便会影响结果。另一方面，厄米矩阵上的$\operatorname{Tr}(XY)$是实的正定内积，因而可以用正交化及统一缩放选择
<span id="eq:c69-trace-normalization"></span>

$$
\operatorname{Tr}(T^aT^b)=\frac12\delta^{ab}.
\tag{69.8}
$$

采用这个基本表示归一，便能进一步确定结构系数的反对称性。先将式[（69.7）](#eq:c69-lie-bracket)两端右乘$T^c$并取迹，再利用迹的循环性，得到
<span id="eq:c69-structure-antisymmetry"></span>

$$
\begin{aligned}
\frac{i}{2}f^{abc}
&=\operatorname{Tr}([T^a,T^b]T^c)\\
&=\operatorname{Tr}(T^aT^bT^c-T^aT^cT^b)\\
&=\operatorname{Tr}(T^a[T^b,T^c])
 =\frac{i}{2}f^{bca}.
\end{aligned}
\tag{69.9}
$$

循环置换不变，再与前两指标反对称结合，便知任意两个指标交换都使$f^{abc}$变号。

这里须与第24节使用过的基相接。对同一组$SU(N)$矩阵，那里的迹归一为2，故本节可取
<span id="eq:c69-normalization-conversion"></span>

$$
T_{69}^a=\frac12T_{24}^a,\qquad
f_{69}^{abc}=\frac12f_{24}^{abc}.
\tag{69.10}
$$

第二个关系来自把第一个关系代入对易子：左边缩小为原来的$1/4$，右边的生成元缩小为$1/2$，结构系数还须缩小$1/2$。比较相同的实际变换时，应保持整个相位矩阵不变，即$\theta_{24}^aT_{24}^a=g\theta_{69}^aT_{69}^a$；规范势也应按$gA_\mu^aT^a$这一乘积比较。

例如$SU(2)$取$T^a=\sigma^a/2$。利用已知的泡利关系，直接得到
<span id="eq:c69-su2-example"></span>

$$
\begin{aligned}
\relax [T^a,T^b]
&=\frac14[\sigma^a,\sigma^b]
 =\frac{i}{2}\epsilon^{abc}\sigma^c
 =i\epsilon^{abc}T^c,\\
\operatorname{Tr}(T^aT^b)&=\frac14(2\delta^{ab})
 =\frac12\delta^{ab}.
\end{aligned}
\tag{69.11}
$$

所以本节的$SU(2)$结构系数为$\epsilon^{abc}$。后面换用不同的物质表示时，保持的正是这一组已固定的结构系数。

<span id="c69-connection"></span>

## 矩阵规范势与物质场

现在把$A_\mu$取为厄米无迹矩阵。定义
<span id="eq:c69-matrix-connection"></span>

$$
\begin{aligned}
D_\mu&=\partial_\mu\mathbf1-igA_\mu,\qquad
(D_\mu\phi)_j=\partial_\mu\phi_j-ig(A_\mu)_{jk}\phi_k,\\
A'_\mu&=UA_\mu U^\dagger+\frac{i}{g}U\partial_\mu U^\dagger,\\
U(x)&=\exp[-ig\Gamma^a(x)T^a].
\end{aligned}
\tag{69.12}
$$

$\Gamma^a$为实的有限参数。先取$g\ne0$解释这组含$1/g$的式子，最后的分量关系则有连续的零耦合极限。

有限指数的写法可从酉矩阵的对角化理解。在一个时空点，写$U=W\operatorname{diag}(e^{-i\alpha_j})W^\dagger$。行列式为1给$\sum_j\alpha_j=2\pi n$；把其中一个$\alpha_j$减去$2\pi n$，不会改变$U$，却使相位之和变为零。因此$W\operatorname{diag}(\alpha_j)W^\dagger$是厄米无迹矩阵，可展开为$g\Gamma^aT^a$。当$U$随$x$变化时，我们在光滑的参数片内使用这个表示；不同片上的变换再按群乘法连接。

式[（69.12）](#eq:c69-matrix-connection)的变换保持$A_\mu$所需的矩阵性质。由$\partial_\mu(UU^\dagger)=0$，
<span id="eq:c69-connection-reality"></span>

$$
\begin{aligned}
\relax [U(\partial_\mu U^\dagger)]^\dagger
&=(\partial_\mu U)U^\dagger=-U\partial_\mu U^\dagger,\\
\operatorname{Tr}(U\partial_\mu U^\dagger)
&=\partial_\mu\log\det U^\dagger=0 .
\end{aligned}
\tag{69.13}
$$

所以非齐次项乘$i/g$后厄米且无迹；齐次项的相应性质由酉共轭保持。更直接地，在实际物质场上计算
<span id="eq:c69-covariant-derivative-proof"></span>

$$
\begin{aligned}
D'_\mu(U\phi)
&=\partial_\mu(U\phi)
 -ig\left(UA_\mu U^\dagger+\frac{i}{g}U\partial_\mu U^\dagger\right)U\phi\\
&=U\partial_\mu\phi+(\partial_\mu U)\phi
 -igUA_\mu\phi+U(\partial_\mu U^\dagger)U\phi\\
&=U(\partial_\mu-igA_\mu)\phi .
\end{aligned}
\tag{69.14}
$$

第二行最后一项等于$-(\partial_\mu U)\phi$，恰好抵消普通导数的附加项。这个展开保持了内部矩阵的次序。先作$U$再作$V$时，导数按$(VU)D_\mu(VU)^\dagger$变换，故这种规则也与群乘法一致。

协变导数已经构造出来，物质动能便容易处理。复标量及狄拉克多重态分别有
<span id="eq:c69-matter-kinetic-invariance"></span>

$$
\begin{aligned}
-(D'_\mu\phi')^\dagger D'^\mu\phi'
&=-(D_\mu\phi)^\dagger U^\dagger U D^\mu\phi,\\
i\bar\Psi'\gamma^\mu D'_\mu\Psi'
&=i\bar\Psi U^\dagger\gamma^\mu U D_\mu\Psi
 =i\bar\Psi\gamma^\mu D_\mu\Psi .
\end{aligned}
\tag{69.15}
$$

$U$只作用内部指标，因此与$\gamma^\mu$对易；伴随旋量按$\bar\Psi'=\bar\Psi U^\dagger$变换。质量项$m^2\phi^\dagger\phi$、$m\bar\Psi\Psi$中的两个矩阵也直接相消。若物质有质量矩阵$M$，相应条件是$U^\dagger MU=M$。它允许不同的、彼此不被规范变换混合的多重态具有不同质量。对实$SO(N)$标量，改用实内积并保留实场动能和质量项的$1/2$即可。

更一般的物质密度也可逐项作协变化：先把整体不变密度写成由不变内部张量缩并的场与导数乘积，再把每个导数换为$D$。每一个$D_\mu\phi$都按$\phi$本身的规则变换，缩并时各个$U$便消去。遇到多重导数时也按原次序逐层替换。不同导数次序之差会产生下面要定义的场强，因此还可有其它规范不变相互作用；上述构造给出了本节所需的物质拉格朗日量。

<span id="c69-curvature"></span>

## 场强与规范场的相互作用

物质动能已能与规范场耦合，但还需要规范场自己的动能。阿贝尔情形以反对称导数构造场强；矩阵情形中，更方便的起点是两个协变导数的对易子。对同一测试多重态$h$，
<span id="eq:c69-double-derivative"></span>

$$
\begin{aligned}
D_\mu D_\nu h
={}&\partial_\mu\partial_\nu h
 -ig(\partial_\mu A_\nu)h-igA_\nu\partial_\mu h\\
&-igA_\mu\partial_\nu h-g^2A_\mu A_\nu h .
\end{aligned}
\tag{69.16}
$$

减去$\mu,\nu$互换后的表达式，二阶普通导数相消，所有含$\partial h$的一阶项也成对相消，留下
<span id="eq:c69-derivative-commutator"></span>

$$
\begin{aligned}
\relax [D_\mu,D_\nu]h
=\bigl\{-ig(\partial_\mu A_\nu-\partial_\nu A_\mu)
        -g^2[A_\mu,A_\nu]\bigr\}h .
\end{aligned}
\tag{69.17}
$$

右端只把一个矩阵乘在$h$上。因此定义场强为这个对易子的矩阵系数：
<span id="eq:c69-field-strength"></span>

$$
F_{\mu\nu}:=\frac{i}{g}[D_\mu,D_\nu]
=\partial_\mu A_\nu-\partial_\nu A_\mu-ig[A_\mu,A_\nu].
\tag{69.18}
$$

它是反对称的时空张量，同时是厄米无迹的内部矩阵。最后一项来自导数中两个$-igA$的乘积，不能在非阿贝尔理论中略去。

场强的变换无需再逐项展开所有$\partial U$。对任意$h$，先用$D'_\nu h=UD_\nu(U^\dagger h)$，再用式[（69.14）](#eq:c69-covariant-derivative-proof)，便有$D'_\mu D'_\nu h=UD_\mu D_\nu(U^\dagger h)$。两种次序相减给
<span id="eq:c69-curvature-covariance"></span>

$$
[D'_\mu,D'_\nu]=U[D_\mu,D_\nu]U^\dagger,\qquad
F'_{\mu\nu}=UF_{\mu\nu}U^\dagger .
\tag{69.19}
$$

非阿贝尔场强因而按共轭规则协变，通常不保持原矩阵不变。不过，两个场强相乘并取迹时，中间的$U^\dagger U$先相消，余下的$U,U^\dagger$再由迹循环消去：
<span id="eq:c69-kinetic-trace-invariance"></span>

$$
\operatorname{Tr}(F'^{\mu\nu}F'_{\mu\nu})
=\operatorname{Tr}(UF^{\mu\nu}F_{\mu\nu}U^\dagger)
=\operatorname{Tr}(F^{\mu\nu}F_{\mu\nu}).
\tag{69.20}
$$

于是选择局域动能$-\operatorname{Tr}(F^{\mu\nu}F_{\mu\nu})/2$。这是具有通常二次导数项的杨—米尔斯动力学；规范不变性容许这个选择，整体系数则按下面的分量动能归一来定。

为了看清独立场的数目和相互作用，按生成元基展开$A_\mu$与$F_{\mu\nu}$。同一迹投影同时给出它们的分量：
<span id="eq:c69-component-projections"></span>

$$
\begin{aligned}
A_\mu&=A_\mu^aT^a,&
2\operatorname{Tr}(A_\mu T^b)
 &=2A_\mu^a\operatorname{Tr}(T^aT^b)=A_\mu^b,\\
F_{\mu\nu}&=F_{\mu\nu}^aT^a,&
2\operatorname{Tr}(F_{\mu\nu}T^b)&=F_{\mu\nu}^b .
\end{aligned}
\tag{69.21}
$$

因为所展开的矩阵厄米，分量均为实数。将两个$A$的展开代入式[（69.18）](#eq:c69-field-strength)，
<span id="eq:c69-component-curvature"></span>

$$
\begin{aligned}
F_{\mu\nu}^cT^c
={}&(\partial_\mu A_\nu^c-\partial_\nu A_\mu^c)T^c
 -igA_\mu^aA_\nu^b[T^a,T^b]\\
={}&\bigl(\partial_\mu A_\nu^c-\partial_\nu A_\mu^c
         +gf^{abc}A_\mu^aA_\nu^b\bigr)T^c,\\
F_{\mu\nu}^c
={}&\partial_\mu A_\nu^c-\partial_\nu A_\mu^c
   +gf^{abc}A_\mu^aA_\nu^b .
\end{aligned}
\tag{69.22}
$$

非线性项的正号是$(-i)(i)=+1$的结果。最后一行可由基的线性无关性读出，也可再乘$T^c$取迹得到。动能中的两个基矩阵给另一个$1/2$：
<span id="eq:c69-component-kinetic-term"></span>

$$
\begin{aligned}
\mathcal L_{\rm kin}
&=-\frac12F^{a\mu\nu}F_{\mu\nu}^b\operatorname{Tr}(T^aT^b)\\
&=-\frac14F^{a\mu\nu}F_{\mu\nu}^a .
\end{aligned}
\tag{69.23}
$$

时空指标在这里照常求和，系数$1/4$已经包含了所选迹归一。

记场强中不含耦合的一次部分为$f_{0\mu\nu}^c=\partial_\mu A_\nu^c-\partial_\nu A_\mu^c$。把式[（69.22）](#eq:c69-component-curvature)平方，二次、三次和四次场项分别为
<span id="eq:c69-gauge-self-interactions"></span>

$$
\begin{aligned}
\mathcal L_{\rm kin}
={}&-\frac14f_0^{c\mu\nu}f_{0\mu\nu}^c
 -\frac g2 f^{abc}f_0^{c\mu\nu}A_\mu^aA_\nu^b\\
&-\frac{g^2}{4}f^{abc}f^{dec}
 A_\mu^aA_\nu^bA^{d\mu}A^{e\nu}.
\end{aligned}
\tag{69.24}
$$

交叉项在平方中出现两次，故三次项的系数为$-g/2$；四次项直接来自两个非线性场强。两个相互作用的系数由同一个$g$和同一个规范动能固定。这是非阿贝尔理论与电磁场的一个主要区别。

甚至空间常量势也能显示这种区别。例如取$SU(2)$、$A_1=uT^1$、$A_2=vT^2$，其它分量为零，$u,v$为实常数。普通导数全部消失，但
<span id="eq:c69-constant-noncommuting-field"></span>

$$
F_{12}=-iguv[T^1,T^2]=guvT^3=-F_{21},\qquad
\mathcal L_{\rm kin}=-\frac12g^2u^2v^2 .
\tag{69.25}
$$

最后一式用了$F_{12}$和$F_{21}$各贡献一次，以及$\operatorname{Tr}[(T^3)^2]=1/2$。它也可直接由式[（69.24）](#eq:c69-gauge-self-interactions)的四次项得到。四维的量纲相应为$[A]=1$、$[F]=2$、$[g]=0$，三类场项都具有质量维数4。

<span id="c69-groups-positivity"></span>

## 规范群与能量的正性

这一构造也适用于其它群。对$SO(N)$，取实反对称矩阵$L^a$并令$T^a=iL^a$，便仍有$T^{a\dagger}=T^a$；指数$e^{-ig\Gamma^aT^a}=e^{g\Gamma^aL^a}$为实正交矩阵。此时$A_\mu=A_\mu^aT^a$是纯虚、反对称的厄米矩阵。非齐次项中的$U\partial_\mu U^T$为实反对称，乘$i/g$后恰好也有同样性质。这样就能保持全部协变导数和场强的$i$号。

除了酉群和正交群，还有紧致辛群及五个例外群。这里的$Sp(2N)$指
<span id="eq:c69-compact-symplectic"></span>

$$
USp(2N)=
\{\,U\in U(2N):U^TJU=J\,\},\qquad
J=\begin{pmatrix}0&\mathbf1_N\\-\mathbf1_N&0\end{pmatrix}.
\tag{69.26}
$$

它也常记作$Sp(N)$，与[第24节](/posts/srednicki-24/#c24-symplectic)取实矩阵的$Sp(2N,\mathbb R)$不同。五个例外群分别记为$G_2$、$F_4$、$E_6$、$E_7$和$E_8$。这些系列来自紧致简单李代数的分类：根系与简单代数的对应见 Etingof 讲义的[定理23.7](https://ocw.mit.edu/courses/18-755-lie-groups-and-lie-algebras-ii-spring-2024/mit18_755_s24_lec_full.pdf#page=124)、[推论24.4](https://ocw.mit.edu/courses/18-755-lie-groups-and-lie-algebras-ii-spring-2024/mit18_755_s24_lec_full.pdf#page=133)，紧实形式见[第41.1节](https://ocw.mit.edu/courses/18-755-lie-groups-and-lie-algebras-ii-spring-2024/mit18_755_s24_lec_full.pdf#page=219)。一般连通紧李群可写成一个环面与单连通紧半单群之积，再除以有限中心子群，见[推论43.6](https://ocw.mit.edu/courses/18-755-lie-groups-and-lie-algebras-ii-spring-2024/mit18_755_s24_lec17.pdf#page=3)。规范场动力学还要求内部二次型具有正性，下面从能量推导这一条件。

对本节的厄米生成元，定义内部二次型$q_{ab}=2\operatorname{Tr}(T^aT^b)$。若$v^a$是不全为零的实系数，$X=v^aT^a$便是非零厄米矩阵，所以
<span id="eq:c69-positive-trace-form"></span>

$$
v^aq_{ab}v^b=2\operatorname{Tr}(X^2)
=2\sum_j\lambda_j(X)^2>0 .
\tag{69.27}
$$

基的线性无关性保证$X\ne0$，厄米性保证本征值实。迹的循环性还给$q$在共轭变换下不变；式[（69.8）](#eq:c69-trace-normalization)所选的基就是$q_{ab}=\delta_{ab}$。这使规范动能的各个内部方向具有相同的正常号。

能量中的这个号可由正则计算看清。暂取一般非退化不变实对称型$q$，考虑$\mathcal L=-q_{ab}F^{a\mu\nu}F_{\mu\nu}^b/4$，不加入物质场。沿第54节定义$E_i^a=-F_{0i}^a$、$B_i^a=\epsilon_{ijk}F_{jk}^a/2$。再定义作用于内部矩阵的伴随协变导数，
<span id="eq:c69-electric-kinetic-form"></span>

$$
\begin{aligned}
D_i^{\rm ad}X&=\partial_iX-ig[A_i,X],\\
(D_i^{\rm ad}X)^c&=\partial_iX^c+gf^{abc}A_i^aX^b,\\
F_{0i}&=\dot A_i-D_i^{\rm ad}A_0,\\
\mathcal L&=\frac12q_{ab}F_{0i}^aF_{0i}^b
 -\frac14q_{ab}F_{ij}^aF_{ij}^b .
\end{aligned}
\tag{69.28}
$$

下时间指标使$F^{0i}=-F_{0i}$，而$(0i)$与$(i0)$各出现一次，于是电场二次项为正。正则动量及勒让德变换为
<span id="eq:c69-gauge-hamiltonian"></span>

$$
\begin{aligned}
\pi_a^i&=\frac{\partial\mathcal L}{\partial\dot A_i^a}
 =q_{ab}F_{0i}^b,\qquad \pi_a^0=0,\\
H&=\int d^3x\left[
 \frac12q^{ab}\pi_a^i\pi_b^i
 +\frac14q_{ab}F_{ij}^aF_{ij}^b
 +\pi_a^i(D_i^{\rm ad}A_0)^a\right].
\end{aligned}
\tag{69.29}
$$

$q^{ab}$为$q_{ab}$的逆矩阵。最后一项来自$\dot A_i=F_{0i}+D_i^{\rm ad}A_0$。为处理它，采用周期边界或足够快的空间衰减。普通导数可作分部积分，而$q$的不变性给$q([A,X],Y)=-q(X,[A,Y])$，因此交换子部分也有相同的负号：
<span id="eq:c69-gauss-positive-energy"></span>

$$
\begin{aligned}
\int d^3x\,q_{ab}F_{0i}^b(D_i^{\rm ad}A_0)^a
&=-\int d^3x\,A_0^a q_{ab}(D_i^{\rm ad}F_{0i})^b,\\
\mathcal G_a&:=q_{ab}(D_i^{\rm ad}F_{0i})^b=0,\\
H\big|_{\mathcal G=0}
&=\frac12\int d^3x\,q_{ab}
 (\mathbf E^a\cdot\mathbf E^b+\mathbf B^a\cdot\mathbf B^b).
\end{aligned}
\tag{69.30}
$$

对$A_0$变分时，$\delta F_{0i}=-D_i^{\rm ad}\delta A_0$；代入$\delta S$再作第一行的分部积分，就得到$\delta S=\int d^4x\,\delta A_0^a\mathcal G_a$。因而第二行是高斯约束，它在哈密顿量中以$-A_0^a\mathcal G_a$出现。第三行还用了$F_{ij}^aF_{ij}^b=2\mathbf B^a\cdot\mathbf B^b$。因此$q$正定时，满足约束的规范场能量非负。

如果$q$有负方向$t^a$，可把势限制在一个生成元方向，$A_\mu^a=t^a a_\mu$。所有内部对易子都为零，场方程及高斯约束便退为麦克斯韦形式。选择一个非零横向波包并把其振幅乘$\lambda$，就有
<span id="eq:c69-negative-kinetic-direction"></span>

$$
H[\lambda a]
=\frac{\lambda^2q(t,t)}2
 \int d^3x\,(\mathbf E^2+\mathbf B^2)
\longrightarrow-\infty
\quad (|\lambda|\longrightarrow\infty).
\tag{69.31}
$$

沿这一族满足约束的场构型，能量可以趋于负无穷。在普通杨—米尔斯动力学中，所需条件是内部李代数具有正定不变型。紧致规范群提供这种结构；但仅由局部动能不能确定全局群的拓扑。例如$\mathbb R\times SU(2)$与$U(1)\times SU(2)$具有相同的局部代数，前者不紧致，仍可取阿贝尔与$SU(2)$的正常动能之和。

<span id="c69-qcd"></span>

## 量子色动力学中的色与味

一个具体例子是量子色动力学（quantum chromodynamics，QCD）。规范群取$SU(3)$，每个狄拉克夸克场有三个被规范变换混合的分量，称为色。此外还有六个味标签：上$u$、下$d$、奇$s$、粲$c$、底或美$b$、顶或真$t$。色是内部量子数的名称；同一味的三个色分量组成一个基本表示，不同味则给六个这样的多重态。

用小写$i,j=1,2,3$记色，大写$I$记味。展开色求和后，拉格朗日量为
<span id="eq:c69-qcd-lagrangian"></span>

$$
\begin{aligned}
(D_\mu)_{ij}
&=\delta_{ij}\partial_\mu-igA_\mu^aT^a_{ij},
 \qquad a=1,\ldots,8,\\
\mathcal L_{\rm QCD}
&=\sum_I\left[
 i\bar\Psi_{iI}\gamma^\mu(D_\mu)_{ij}\Psi_{jI}
 -m_I\bar\Psi_{iI}\Psi_{iI}\right]
 -\frac14F^{a\mu\nu}F_{\mu\nu}^a .
\end{aligned}
\tag{69.32}
$$

规范变换只混合同一$I$的色分量。质量矩阵在色空间是单位矩阵，在味空间则是$\operatorname{diag}(m_I)$，故不同味的质量并不破坏色规范对称性。各$m_I$是模型的经验参数。例如，取上、下夸克几个MeV及顶夸克178GeV作为历史教学量级，就能看出不同味的质量可以相差很大。

展开协变导数便读出夸克与规范场的相互作用：
<span id="eq:c69-quark-gluon-interaction"></span>

$$
\begin{aligned}
i\bar\Psi_{iI}\gamma^\mu(D_\mu)_{ij}\Psi_{jI}
&=i\bar\Psi_{iI}\slashed\partial\Psi_{iI}\\
&\quad+gA_\mu^a\bar\Psi_{iI}\gamma^\mu T^a_{ij}\Psi_{jI}.
\end{aligned}
\tag{69.33}
$$

正号由$i(-ig)=+g$给出。内部指标$a$有八个取值，因此有八个规范场，称为胶子。在这个未破缺理论的微扰展开中，它们的二次项是八份无质量自旋一场的动能，而三、四胶子相互作用来自式[（69.24）](#eq:c69-gauge-self-interactions)。胶子和夸克的强相互作用都由同一个$g$控制；带色场怎样形成物理强子，属于随后对该理论动力学的研究。

夸克还带有电荷，
<span id="eq:c69-quark-electric-charges"></span>

$$
Q_u=Q_c=Q_t=\frac23|e|,\qquad
Q_d=Q_s=Q_b=-\frac13|e|.
\tag{69.34}
$$

本节暂略电磁耦合，专门研究色规范场。这里使用$|e|$表示电荷单位，与先前电子电荷$e<0$的约定相接。

<span id="c69-representations"></span>

## 同一规范场怎样作用于不同表示

以上先让物质场按基本表示变换，但规范场的分量不应因物质多重态的维数不同而重新定义。为此引入一般表示$R$。用$D(R)$表示其维数，选取满足同一李代数的厄米矩阵$T_R^a$，即
<span id="eq:c69-general-representation"></span>

$$
\begin{aligned}
\relax [T_R^a,T_R^b]&=if^{abc}T_R^c,\qquad \phi_R'=U_R\phi_R,\\
D_{R\mu}&=\partial_\mu\mathbf1_{D(R)}-igA_\mu^aT_R^a .
\end{aligned}
\tag{69.35}
$$

这里$R$是表示的名称，$D(R)$是一个整数；它们都不是求和指标。$U_R$由式[（69.12）](#eq:c69-matrix-connection)中的$T^a$换为$T_R^a$得到。李代数矩阵首先规定局部变换；若指定了一个全局群，还要求矩阵满足它的全局识别。例如$\sigma^a/2$满足旋转代数，但$\exp(-i2\pi\sigma^3/2)=-\mathbf1$，所以它给$SU(2)$表示，却不能把$SO(3)$中等于恒等变换的$2\pi$转动表示为恒等矩阵。

剩下的关键是证明各表示可以共用同一组$A_\mu^a$。在基本表示中取$U=\mathbf1-ig\theta^aT^a$，规范势的一次变化为
<span id="eq:c69-universal-component-law"></span>

$$
\begin{aligned}
\delta A_\mu
&=-(\partial_\mu\theta^a)T^a
 -ig\theta^a A_\mu^b[T^a,T^b],\\
\delta A_\mu^c
&=-\partial_\mu\theta^c+gf^{abc}\theta^aA_\mu^b .
\end{aligned}
\tag{69.36}
$$

第一行的导数项来自$(i/g)U\partial_\mu U^\dagger$，其系数为$(i/g)(ig)=-1$；第二项用对易关系给$+gf$。第二行只含已固定的结构系数与场分量。把它乘以任意表示的$T_R^c$，便重新组合成同一矩阵变换式，因此$D'_{R\mu}=U_RD_{R\mu}U_R^\dagger$对各个物质表示同时成立。[下面](#c69-finite-components)沿有限参数积分，将这一结果写成收敛的矩阵指数级数。

这一步先在基本表示中比较系数。若某个物质表示不忠实，它的生成元可能线性相关，仅从该表示中的矩阵方程未必能反解全部$A_\mu^a$；平凡表示$T_R^a=0$就是最简单的例子。共同分量仍由式[（69.36）](#eq:c69-universal-component-law)变换，只是这个物质场没有相应耦合。不同表示的$\operatorname{Tr}_R(T_R^aT_R^b)$也不必等于基本表示的$\delta^{ab}/2$。保持同一李代数基以后，各表示的差别进入它们的生成元矩阵，而规范场及其变换规律已经统一。

同一组结构系数还给出与全部生成元对易的二次组合。先求有限规范变换，再构造这个将在下一节使用的二次卡西米尔算符。

<span id="c69-finite-components"></span>

## 有限规范变换的分量形式

有限变换可以由刚才的无穷小结果沿参数积分得到。
考虑
$U_R(s,x)=\exp[-igs\Gamma^a(x)T_R^a]$，$0\le s\le1$，
其中$\Gamma^a(x)$在这个积分过程中固定。
相邻两个$s$之间的变换参数为$\theta^a=ds\,\Gamma^a$。
在每个时空点定义只作用于生成元标签的实矩阵$\mathcal M$，则
<span id="eq:c69-ex-1-finite-flow"></span>

$$
\begin{aligned}
\mathcal M^c{}_b(x)&=g f^{abc}\Gamma^a(x),\\
\frac{dA_\mu^c(s,x)}{ds}
&=\mathcal M^c{}_b(x)A_\mu^b(s,x)-\partial_\mu\Gamma^c(x),\\
A_\mu^c(0,x)&=A_\mu^c(x).
\end{aligned}
\tag{69.37}
$$

为求解这个方程，从左边乘$e^{-s\mathcal M}$，
用矩阵指数的导数消掉含$A_\mu(s)$的齐次项。
沿$s$从0积分到1后得到
<span id="eq:c69-ex-1-finite-components"></span>

$$
\begin{aligned}
\frac{d}{ds}\bigl[e^{-s\mathcal M}A_\mu(s)\bigr]
&=-e^{-s\mathcal M}\partial_\mu\Gamma,\\
A'_\mu
&=e^{\mathcal M}A_\mu
  -\int_0^1ds\,e^{(1-s)\mathcal M}\partial_\mu\Gamma,\\
\int_0^1ds\,e^{(1-s)\mathcal M}
&=\sum_{n=0}^\infty\frac{\mathcal M^n}{(n+1)!}.
\end{aligned}
\tag{69.38}
$$

这一式中的$A_\mu$是具有分量$A_\mu^c$的列向量；
相应的表示空间矩阵仍记作$A_{R\mu}=A_\mu^aT_R^a$。
有限变换同样只依赖$f^{abc}$，所以在所选指数参数片中也与物质表示无关。
末行由有限维矩阵指数的绝对收敛级数逐项积分得到，
用到了$\int_0^1(1-s)^n ds=1/(n+1)$。
这一表达式不要求$\mathcal M$可逆，故也适用于有零特征值的情形。
若结构系数全为零，它立即退回
$A_\mu'=A_\mu-\partial_\mu\Gamma$，
与第58节的$D=\partial-ieA$约定相符。

用这些分量构造的每个$D_{R\mu}$都满足
$D'_{R\mu}=U_RD_{R\mu}U_R^\dagger$。
因此$F_{R\mu\nu}=(i/g)[D_{R\mu},D_{R\nu}]$满足同样的齐次共轭变换；
微分算符及内部矩阵的次序始终保持不变。
这正是不同表示的物质场能共同耦合到同一非阿贝尔规范场的原因。

<span id="c69-quadratic-casimir"></span>

## 二次卡西米尔算符

现在在任意表示中记二次组合为
$C_R=\sum_aT_R^aT_R^a$。
对每一项使用$[AB,C]=A[B,C]+[A,C]B$，
保持矩阵次序，有
<span id="eq:c69-ex-2-casimir-commutator"></span>

$$
\begin{aligned}
\relax [C_R,T_R^b]
&=\sum_a\left\{
 T_R^a[T_R^a,T_R^b]+[T_R^a,T_R^b]T_R^a\right\}\\
&=i\sum_{a,c}f^{abc}
       \left(T_R^aT_R^c+T_R^cT_R^a\right).
\end{aligned}
\tag{69.39}
$$

括号内的矩阵组合在$a,c$交换时不变，结构系数却变号。
把同一双重和在$a,c$互换后的写法与原写法取平均，便得
<span id="eq:c69-ex-2-casimir-central"></span>

$$
[C_R,T_R^b]
=\frac{i}{2}\sum_{a,c}
   (f^{abc}+f^{cba})
   \left(T_R^aT_R^c+T_R^cT_R^a\right)=0 .
\tag{69.40}
$$

这一对易关系也适用于可约表示。
这个二次组合通常称为二次卡西米尔算符；
它与所有内部生成元对易的原因，是生成元指标上的对称缩并与结构系数的反对称性。
若改用没有正交归一的生成元基，二次缩并也须同时改用该基的不变内积的逆矩阵；
单独保留不加权的$\sum_aT^aT^a$便不再是同一个算符。

---

[← 第 68 节](/posts/srednicki-68/) · [章节地图](/srednicki/) · [第 70 节 →](/posts/srednicki-70/)
