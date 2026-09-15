---
title: 'Srednicki §70 群表示'
date: 2026-09-14
category: 笔记
tags: [物理, 量子场论, Srednicki]
series: 'Srednicki QFT'
srednickiSections: [70]
hideFromHome: true
draft: false
---

<span id="c70"></span>

上一节已使同一个规范场同任意物质多重态耦合。不同多重态所含的分量数可以不同，生成元也可以是不同大小的矩阵，但它们必须满足同一组对易关系。计算散射振幅时，这些矩阵沿物质线相乘；闭合物质线又使矩阵乘积成为迹。因此，除了知道群的名称，我们还需要知道所用表示怎样分解，以及各种生成元乘积给出什么群因子。

这里的表示空间取有限维复空间，生成元取厄米矩阵。先讨论半单规范代数，在需要单一迹指标的地方取一个简单因子；对于非简单的$SO(4)$，将直接用标准生成元计算总迹。时空约定仍沿上一节，本节的主要运算则全在内部表示空间中进行。

<span id="c70-conjugate"></span>

## 表示及其复共轭

记表示为$R$，其维数为$D(R)$。在固定的李代数基下，它们满足
<span id="eq:c70-representation"></span>

$$
\begin{aligned}
\relax [T_R^a,T_R^b]&=if^{abc}T_R^c,
& (T_R^a)^\dagger&=T_R^a,\\
U_R(\theta)&=\exp(-i\theta^aT_R^a),
&a&=1,\ldots,D(A).
\end{aligned}
\tag{70.1}
$$

$A$将表示伴随表示，其维数就是生成元的数目。这里的相位参数已包含耦合：同上一节比较，$\theta^a_{70}=g\theta^a_{69}$。改变表示时保持$f^{abc}$不变，不能独立把某一表示的全部生成元再乘任意常数。群原来由哪些矩阵定义，那组矩阵就称为基本表示或定义表示；例如$SU(N)$的定义空间为$N$维。

半单李代数的生成元无迹。为证明这一点，先说明简单性的含义：一个线性子空间若与代数中任意元素取交换子后仍留在该子空间，就称为理想；没有非零真理想的非阿贝尔代数称为简单代数。对简单代数，无迹性可以从对易关系得到：由$[Z,[X,Y]]=[[Z,X],Y]+[X,[Z,Y]]$，所有交换子的线性包络是非零理想，简单性使它等于整个代数，因而每个生成元都是交换子的线性组合。矩阵交换子的迹为零，故$\operatorname{Tr}T_R^a=0$。半单代数逐个简单因子应用这个论证。若规范群另含$U(1)$，相应电荷矩阵一般有非零迹，后面用到无迹性的计算便须保留其附加项。

现在对对易关系取复共轭。由于$f^{abc}$为实，右端的$i$变号，因此共轭表示定义为
<span id="eq:c70-conjugate-representation"></span>

$$
\begin{aligned}
T_{\bar R}^a&:=-(T_R^a)^*,\\
\relax [T_{\bar R}^a,T_{\bar R}^b]
&=[T_R^a,T_R^b]^*
=-if^{abc}(T_R^c)^*
=if^{abc}T_{\bar R}^c,\\
U_{\bar R}(\theta)&=U_R(\theta)^*.
\end{aligned}
\tag{70.2}
$$

负号使共轭后的矩阵仍满足原来的李代数。若能选一组基，使全部$T_R^a$都是纯虚矩阵，那么$T_{\bar R}^a=T_R^a$，群矩阵$U_R$便是实矩阵，称为实表示。若$R$与$\bar R$酉等价，却不存在这样的实基，则称为伪实表示；若两者不等价，则称为复表示。判定时必须使用同一个基变换处理全部生成元。

一个很方便的排除法来自谱。若$R\simeq\bar R$，任意实线性组合$H=h_aT_R^a$必须同$-H^*$酉等价。$H$厄米，其本征值为实，因此这些本征值必须在变号后保持同样的重数。对$SU(N\ge3)$的基本表示，取
<span id="eq:c70-complex-spectrum"></span>

$$
H=\operatorname{diag}(1,1,-2,0,\ldots,0),\qquad
\operatorname{spec}(-H)=\{-1,-1,2,0,\ldots,0\}.
\tag{70.3}
$$

两套谱不同，故基本表示为复表示。这里不要求$H$本身是归一化基中的某一个生成元，只须它是厄米无迹矩阵。谱不配对足以排除自共轭；谱配对本身尚未构造出一组共同的交织矩阵。

$SU(2)$的情况不同。取$T^a=\sigma^a/2$及$V=\sigma_2$，泡利矩阵给出
<span id="eq:c70-su2-intertwiner"></span>

$$
\begin{aligned}
V^{-1}\sigma_1V&=-\sigma_1,&
V^{-1}\sigma_2V&=\sigma_2,&
V^{-1}\sigma_3V&=-\sigma_3,\\
-(T^a)^*&=V^{-1}T^aV,&
VV^*&=-\mathbf1_2.
\end{aligned}
\tag{70.4}
$$

第一行正好对应$\sigma_1,\sigma_3$为实、$\sigma_2$为纯虚的性质，证明双重态同其共轭等价。还要证明它不能换成实基，才能断定它是伪实表示。下面的论证也解释了实与伪实的区别。

暂取不可约表示，即不存在被全部生成元保持的非零真子空间。若$-(T^a)^*=V^{-1}T^aV$，其中$V$酉，令$K$表示逐分量复共轭，定义反线性算符$\mathcal J=VK$。关系$T^aV=-V(T^a)^*$连同$i$在复共轭下变号，保证$\mathcal JU_R=U_R\mathcal J$。因此$\mathcal J^2$是同全部生成元对易的线性算符。由[第33节已证明的舒尔引理](/posts/srednicki-33/#c33-classification)，它在不可约空间为标量：
<span id="eq:c70-real-pseudoreal-sign"></span>

$$
\begin{aligned}
\mathcal J^2&=VV^*=c\mathbf1,& |c|&=1,\\
\mathcal J\mathcal J^2&=c^*\mathcal J,
&\mathcal J^2\mathcal J&=c\mathcal J,\\
c&=\pm1,&V^T&=cV.
\end{aligned}
\tag{70.5}
$$

第二行的两边都是$\mathcal J^3$，所以$c=c^*$。最后的转置关系由$VV^*=c\mathbf1$右乘$V^T$得到。若换用另一酉交织矩阵，对应反线性算符之比与群作用对易，仍只能是相位，不能改变$\mathcal J^2$的符号。

当$c=+1$时，任意向量可以写成
<span id="eq:c70-real-fixed-basis"></span>

$$
v=\frac{v+\mathcal Jv}{2}
 +i\frac{v-\mathcal Jv}{2i}.
\tag{70.6}
$$

右边两个分式都被$\mathcal J$固定。固定向量之间的内积为实，可以用实系数的格拉姆—施密特过程选出正交基。在这组基中$\mathcal J$就是普通共轭，同它对易的群矩阵为实，生成元则为纯虚反对称矩阵。当$c=-1$时，上述实基不可能存在；同时$V$非退化且反对称，$\det V=\det V^T=(-1)^{D(R)}\det V$便要求维数为偶数。式[（70.4）](#eq:c70-su2-intertwiner)的$c=-1$遂证明$SU(2)$双重态伪实。$SO(N)$的向量表示从开始就可以使用纯虚反对称生成元，因而为实表示。对于可约表示，这一分类应逐个不可约块使用，不能只凭某个交织矩阵不等于单位矩阵就断言整个表示伪实。

<span id="c70-adjoint"></span>

## 由结构常数构造伴随表示

把结构常数排成矩阵，定义
<span id="eq:c70-adjoint-definition"></span>

$$
(T_A^a)^{bc}:=-if^{abc},\qquad
(T_A^a)^\dagger=T_A^a,\qquad
-(T_A^a)^*=T_A^a.
\tag{70.7}
$$

第69节已由循环迹证明$f$实且完全反对称，所以这些矩阵厄米，并给出实表示。还须检验它们是否满足同一李代数，这正是雅可比恒等式的作用。对任意三个矩阵$X,Y,Z$，分别展开
<span id="eq:c70-matrix-jacobi"></span>

$$
\begin{aligned}
\relax [[X,Y],Z]&=XYZ-YXZ-ZXY+ZYX,\\
\relax [[Y,Z],X]&=YZX-ZYX-XYZ+XZY,\\
\relax [[Z,X],Y]&=ZXY-XZY-YZX+YXZ.
\end{aligned}
\tag{70.8}
$$

相加时每一种有序乘积恰好出现一次正项和一次负项，故总和为零。再取$X=T^a,Y=T^b,Z=T^c$，两次使用李括号产生$i^2=-1$。右乘$T^e$并取定义表示的迹，得到
<span id="eq:c70-structure-jacobi"></span>

$$
\begin{aligned}
0&=\operatorname{Tr}([[T^a,T^b],T^c]T^e)
 +\operatorname{Tr}([[T^b,T^c],T^a]T^e)\\
&\quad+\operatorname{Tr}([[T^c,T^a],T^b]T^e)\\
&=-\kappa\bigl(f^{abd}f^{dce}
 +f^{bcd}f^{dae}+f^{cad}f^{dbe}\bigr),\\
&\hspace{12mm}\operatorname{Tr}(T^dT^e)=\kappa\delta^{de}.
\end{aligned}
\tag{70.9}
$$

除去非零的$\kappa$，便得到结构常数的雅可比恒等式。对$SU(N)$基本表示，$\kappa=1/2$。这个证明只用到迹形式非退化，不依赖$1/2$这个特定数值。对$SO(N)$基本表示取$\kappa=2$时，同样可用。

为了核对伴随矩阵的指标，把雅可比中的顺序取为$a,c,b$，再利用$f$反对称，便有
<span id="eq:c70-adjoint-bracket"></span>

$$
\begin{aligned}
-f^{abd}f^{cde}+f^{cbd}f^{ade}
&=f^{acd}f^{dbe},\\
(-if^{abd})(-if^{cde})-(-if^{cbd})(-if^{ade})
&=if^{acd}(-if^{dbe}),\\
(T_A^a)^{bd}(T_A^c)^{de}-(T_A^c)^{bd}(T_A^a)^{de}
&=if^{acd}(T_A^d)^{be}.
\end{aligned}
\tag{70.10}
$$

第二行的左边用了$(-i)^2=-1$，右边用了$i(-i)=1$；第三行的求和指标$d$恰好连接前一矩阵的列与后一矩阵的行。因此$[T_A^a,T_A^c]=if^{acd}T_A^d$。规范场的内部标签本身可以按这个表示变换，因而伴随表示会反复出现。

<span id="c70-index"></span>

## 迹指标与二次卡西米尔量

两个生成元的迹把表示的信息压缩成一个简单群因子。先令$q_R^{ab}=\operatorname{Tr}_R(T_R^aT_R^b)$。厄米性和循环迹使它为实对称矩阵；在交换子中插入生成元，再作迹循环，有
<span id="eq:c70-invariant-trace"></span>

$$
\begin{aligned}
0&=\operatorname{Tr}_R[T_R^c,T_R^aT_R^b]\\
&=i f^{cad}q_R^{db}+i f^{cbd}q_R^{ad}.
\end{aligned}
\tag{70.11}
$$

这说明$q_R$在伴随变换下不变。在已经选定的正交生成元基中，它与全部伴随矩阵对易，因此它的本征子空间都是李代数的理想。对简单代数只可能有一个本征值，于是定义迹指标$T(R)$：
<span id="eq:c70-trace-index"></span>

$$
\operatorname{Tr}_R(T_R^aT_R^b)=T(R)\delta^{ab}.
\tag{70.12}
$$

非平凡表示的$T(R)>0$，因为至少有一个非零厄米生成元，其平方迹严格为正。各表示的$T(R)$通常不同，不能再一律取为基本表示的数值。对于几个简单因子的直积，式[（70.11）](#eq:c70-invariant-trace)只要求每个因子内部各有一个系数，须分别命名这些指标。

[上一节](/posts/srednicki-69/#c69-quadratic-casimir)已证明二次组合$\mathcal C_R=\sum_aT_R^aT_R^a$与全部生成元对易：收缩中的矩阵反对易子关于$a,c$对称，$f^{abc}$则反对称。现在进一步假定$R$不可约。$\mathcal C_R$厄米，它的每个本征空间又因对易性而被所有生成元保持，所以只容许一个本征值。定义二次卡西米尔量$C(R)$，并取迹，得到
<span id="eq:c70-casimir-index"></span>

$$
\begin{aligned}
\mathcal C_R&=C(R)\mathbf1_{D(R)},\\
\operatorname{Tr}_R\mathcal C_R
&=\sum_a T(R)\delta^{aa}=T(R)D(A),\\
\operatorname{Tr}_R\mathcal C_R
&=C(R)\operatorname{Tr}_R\mathbf1=C(R)D(R),\\
T(R)D(A)&=C(R)D(R).
\end{aligned}
\tag{70.13}
$$

这个关系说明两个维数各在数什么：$D(A)$数生成元，$D(R)$数表示分量。若去掉不可约条件，对易性并不足以使算符成为数倍单位矩阵。例如$SU(2)$的$R=1\oplus2$：
<span id="eq:c70-reducible-casimir-example"></span>

$$
\mathcal C_{1\oplus2}
=\operatorname{diag}(0,3/4,3/4),\qquad
T(1\oplus2)=\tfrac12.
\tag{70.14}
$$

它与每个生成元对易，却不是数倍单位矩阵。对一般直和应在每个不可约块分别使用$C(R_\alpha)$，总迹为$T(R)D(A)=\sum_\alpha C(R_\alpha)D(R_\alpha)$。若各块恰有相同本征值，当然仍可用一个共同的$C$。

下面将用直积分解计算两族常用的群因子：在$SU(N)$基本归一$T(N)=1/2$下求出$T(A)=N$，在$SO(N)$基本归一$T(N)=2$下求出$T(A)=2N-4$。两族的基本归一始终分别保留。

<span id="c70-products"></span>

## 直和与直积

前面已用到不可约性。现在看可约表示为什么能够同时分块。设$W$是全部生成元的共同不变子空间，对$v\in W^\perp,w\in W$，厄米性给$\langle w,T_R^av\rangle=\langle T_R^aw,v\rangle=0$，所以$W^\perp$也不变。选取这两个子空间的正交基，就把所有生成元同时写成两个对角块。递归使用这一过程，有限维表示便分解成不可约直和。对两块的情形，
<span id="eq:c70-direct-sum"></span>

$$
\begin{aligned}
T_{R_1\oplus R_2}^a&=
\begin{pmatrix}T_{R_1}^a&0\\0&T_{R_2}^a\end{pmatrix},\\
D(R_1\oplus R_2)&=D(R_1)+D(R_2),\\
T(R_1\oplus R_2)&=T(R_1)+T(R_2).
\end{aligned}
\tag{70.15}
$$

最后一式来自乘积仍按相同两块分开、迹按块相加。两块可以具有不同维数和表示类型。

两个分别按$R_1,R_2$变换的量相乘时，两个指标都要变换，空间便是直积$R_1\otimes R_2$。用$i,j$标记第一个空间、$I,J$标记第二个空间，从有限变换展开一次项：
<span id="eq:c70-product-generator"></span>

$$
\begin{aligned}
U_1\otimes U_2
&=\mathbf1-i\theta^a
 (T_1^a\otimes\mathbf1_2+\mathbf1_1\otimes T_2^a)
 +O(\theta^2),\\
(T_{R_1\otimes R_2}^a)_{iI,jJ}
&=(T_1^a)_{ij}\delta_{IJ}+\delta_{ij}(T_2^a)_{IJ},\\
D(R_1\otimes R_2)&=D_1D_2,
\qquad D_r:=D(R_r).
\end{aligned}
\tag{70.16}
$$

作用于不同因子的两个矩阵对易，所以两次乘积的交叉交换子为零，余下$[T_1^a,T_1^b]\otimes\mathbf1+\mathbf1\otimes[T_2^a,T_2^b]=if^{abc}T_{R_1\otimes R_2}^c$，仍是同一个李代数。

取两个直积生成元的乘积，并利用$\operatorname{Tr}_{12}(X\otimes Y)=\operatorname{Tr}_1X\operatorname{Tr}_2Y$，四项分别给
<span id="eq:c70-product-index"></span>

$$
\begin{aligned}
\operatorname{Tr}_{12}(T^aT^b)
={}&D_2\operatorname{Tr}_1(T_1^aT_1^b)
 +D_1\operatorname{Tr}_2(T_2^aT_2^b)\\
&+\operatorname{Tr}_1T_1^a\operatorname{Tr}_2T_2^b
 +\operatorname{Tr}_1T_1^b\operatorname{Tr}_2T_2^a,\\
T(R_1\otimes R_2)
={}&T(R_1)D(R_2)+D(R_1)T(R_2).
\end{aligned}
\tag{70.17}
$$

第二行的两个单生成元迹由无迹性消失，因而得到最后一行的乘积指标公式。这也指出含阿贝尔电荷时需要修改的位置。

<span id="c70-invariant-tensors"></span>

## 上下指标与不变张量

为了识别直积中的不变子空间，引入上下内部指标。约定$\varphi_i$属于$R$，厄米共轭写成$\varphi^{\dagger i}$；生成元的行指标在下、列指标在上。它们的变换为
<span id="eq:c70-conjugate-indices"></span>

$$
\begin{aligned}
\varphi_i'&=(\delta_i{}^j-i\theta^a(T_R^a)_i{}^j)\varphi_j
 +O(\theta^2),\\
(T_{\bar R}^a)^i{}_j&=-(T_R^a)_j{}^i,\\
\varphi^{\dagger i\prime}
&=\varphi^{\dagger i}-i\theta^a(T_{\bar R}^a)^i{}_j
 \varphi^{\dagger j}+O(\theta^2)\\
&=\varphi^{\dagger i}+i\theta^a(T_R^a)_j{}^i
 \varphi^{\dagger j}+O(\theta^2).
\end{aligned}
\tag{70.18}
$$

第二行用厄米性把复共轭改写成转置。有限变换下$\varphi^\dagger\varphi$成为$\varphi^\dagger U_R^\dagger U_R\varphi$，故保持不变。若逐项使用上式，两项相位贡献也相消；只须重命名求和指标，不交换场的次序，因此费米场也没有额外的交换号。

把$\delta_i{}^j$本身看作一个双指标对象，每个指标都按所属表示变换，便有
<span id="eq:c70-invariant-delta"></span>

$$
\begin{aligned}
\delta_i{}^j&\longmapsto
(U_R)_i{}^k(U_{\bar R})^j{}_l\delta_k{}^l\\
&=(U_R)_i{}^k\delta_k{}^l(U_R^{-1})_l{}^j
=\delta_i{}^j.
\end{aligned}
\tag{70.19}
$$

这称为不变张量。单位矩阵在共轭变换下保持不变，因此它把$R$与$\bar R$的一对指标收缩成标量。

一个按$R\otimes\bar R$变换的量可以排成矩阵$M_i{}^j$，其变换为$M\mapsto U_RMU_R^{-1}$，也就是表示空间上的线性映射空间$\operatorname{End}(V_R)$。其中单位矩阵张成的一维子空间不变，群在它上面始终取数值1，生成元取零。这就是单态，所以
<span id="eq:c70-singlet"></span>

$$
R\otimes\bar R=1\oplus\cdots,\qquad T_1^a=0.
\tag{70.20}
$$

对不可约$R$，舒尔引理进一步说明所有同群作用对易的矩阵都与单位矩阵成正比，所以这里的单态只有一份。对可约$R$可能有更多不变矩阵，省略项就可能含更多单态。

生成元本身也给出不变张量，但它有三个指标：$(T_R^b)_i{}^j$的$i,j$分别属于$R,\bar R$，$b$属于伴随表示。同时变换这三个指标，一次变化为
<span id="eq:c70-generator-tensor"></span>

$$
\begin{aligned}
\delta(T_R^b)_i{}^j=-i\theta^a\bigl[&
(T_R^a)_i{}^k(T_R^b)_k{}^j
 +(T_{\bar R}^a)^j{}_l(T_R^b)_i{}^l\\
&+(T_A^a)^{bc}(T_R^c)_i{}^j\bigr] .
\end{aligned}
\tag{70.21}
$$

把共轭的负转置和伴随的$-if$代入，括号成为
<span id="eq:c70-generator-invariance"></span>

$$
(T_R^aT_R^b)_i{}^j-(T_R^bT_R^a)_i{}^j
-if^{abc}(T_R^c)_i{}^j=0.
\tag{70.22}
$$

因此，非零生成元组成的不变向量使$R\otimes\bar R\otimes A$含有单态。这里把$b$也一起变换了；固定某一个$T_R^b$只受物质空间共轭作用时，它仍会同其余生成元混合。

进一步要判断$R\otimes\bar R$是否含有伴随表示，必须构造出相应的不变子空间。直接在$\operatorname{End}(V_R)$中使用生成元的张成空间便能做到。令
<span id="eq:c70-adjoint-embedding"></span>

$$
\begin{aligned}
\iota:\mathfrak g_{\mathbb C}&\longrightarrow\operatorname{End}(V_R),\\
X=X^a t_a&\longmapsto X^aT_R^a,\\
\delta(X^bT_R^b)
&=-i\theta^c[T_R^c,X^bT_R^b]
=\theta^cf^{cba}X^bT_R^a,\\
\delta X^a&=-i\theta^c(T_A^c)^{ab}X^b.
\end{aligned}
\tag{70.23}
$$

这里$t_a$为复化代数的一组基，取$[t_a,t_b]=if^{abc}t_c$；它对应紧实形式中$-it_a$的实基。第二、三行用$f^{cba}=-f^{cab}$，说明$\iota$把伴随变换映成矩阵共轭变换。其核是理想：若$\iota(X)=0$，则$\iota([Y,X])=[\iota(Y),\iota(X)]=0$。对简单代数的非平凡表示，核既不能是全代数，只能为零。实基上的单射复线性延拓后仍单射，因为厄米矩阵的复线性关系可分成实部与虚部的两组实线性关系。

这样找到的$D(A)$维子空间确实与伴随表示等价。它由无迹矩阵组成，与单位矩阵正交；再利用完全可约性取它们的不变正交补，便得到
<span id="eq:c70-adjoint-inclusion"></span>

$$
R\otimes\bar R=1\oplus A\oplus\cdots
\quad\text{（简单代数，非平凡 }R\text{）}.
\tag{70.24}
$$

平凡表示$R=1$显然不满足这个结论。若有几个简单因子，只能保证包含在$R$中作用非零的那些伴随因子。非平凡性和简单因子的限制保证了上述嵌入为单射。

<span id="c70-su-factors"></span>

## SU(N)的分解与群因子

对$SU(N)$的基本表示，刚才的分解尤其简单。$N\times N$矩阵空间有$N^2$维，而单位矩阵与$N^2-1$个无迹生成元已经构成一组完整基。由$\operatorname{Tr}(T^aT^b)=\delta^{ab}/2$投影任意复矩阵$M$，得到
<span id="eq:c70-su-decomposition"></span>

$$
M=\frac{\operatorname{Tr}M}{N}\mathbf1
 +2\sum_aT^a\operatorname{Tr}(T^aM),\qquad
N\otimes\bar N=1\oplus A.
\tag{70.25}
$$

系数$1/N$使第一项的迹等于$\operatorname{Tr}M$，系数2则补偿基本迹的$1/2$。第一个投影为单态，第二个投影为伴随，二者已经耗尽维数，因而分解中没有其余项。

比较$M_l{}^k$在两边的系数，还得到一个有用的补充恒等式：
<span id="eq:c70-su-completeness"></span>

$$
\sum_a(T^a)_i{}^j(T^a)_k{}^l
=\frac12\left(\delta_i{}^l\delta_k{}^j
-\frac1N\delta_i{}^j\delta_k{}^l\right).
\tag{70.26}
$$

它就是同一投影的分量写法，常用来计算内部指标收缩。令$k=j$并求和，第一项给$N\delta_i{}^l$，第二项给$\delta_i{}^l/N$，于是$\sum_aT^aT^a=(N^2-1)\mathbf1/(2N)$。它同式[（70.13）](#eq:c70-casimir-index)给出的基本卡西米尔一致。

现在可以求伴随表示的迹指标。负复共轭不改变二次迹，故$T(\bar N)=T(N)=1/2$。对式[（70.25）](#eq:c70-su-decomposition)分别应用直积及直和迹公式，得
<span id="eq:c70-su-indices"></span>

$$
\begin{aligned}
T(N\otimes\bar N)&=N\,T(N)+N\,T(\bar N)=N,\\
T(1\oplus A)&=T(1)+T(A)=T(A),\\
T(A)&=C(A)=N,\qquad C(N)=\frac{N^2-1}{2N}.
\end{aligned}
\tag{70.27}
$$

伴随的$C(A)=T(A)$来自两侧表示维数同为$D(A)$。另一条路线是限制到只作用于前两个分量的$SU(2)$子群。先用$-i\epsilon^{abc}$直接算三重态的迹为$2\delta^{ab}$，三重态的迹具体为$\sum_{c,d}(-i\epsilon^{acd})(-i\epsilon^{bdc})=\sum_{c,d}\epsilon^{acd}\epsilon^{bcd}=2\delta^{ab}$：$a=b$时有两种非零排列，$a\ne b$时没有共同的非零指标对。再取$m=N-2$，在已知$N\otimes\bar N=1\oplus A$中展开$(2\oplus m1)\otimes(2\oplus m1)$，得到
<span id="eq:c70-su-subgroup-index"></span>

$$
A\big|_{SU(2)}=3\oplus2m\,2\oplus m^2\,1,\qquad
T(A)=2+2m\cdot\frac12=N.
\tag{70.28}
$$

这里用到的$2\otimes2=1\oplus3$在下面用双指标张量写出；也可直接沿[第33节的角动量合成](/posts/srednicki-33/#c33-rotations)取两个自旋$1/2$。其中两个交叉积各给$m$个二重态，$2\otimes\bar2$给一个三重态与一个单态；扣除原$SU(N)$的迹单态后，剩下$m^2$个子群单态。维数核对为$3+4m+m^2=N^2-1$。子群生成元在基本空间中保持原来的归一，按其各不变块求迹就能读出同一群指标。

<span id="c70-so-factors"></span>

## 实表示的平方与SO(N)

当$R$同其共轭等价时，可把$R\otimes\bar R$改写成$R\otimes R$。对于实表示，先选出纯虚厄米基，便有$T^T=-T$。双下指标的$\delta_{ij}$在两个相同表示作用下变为
<span id="eq:c70-real-delta"></span>

$$
\begin{aligned}
\delta_{ij}'&=\delta_{ij}-i\theta^a
 \bigl((T_R^a)_{ij}+(T_R^a)_{ji}\bigr)+O(\theta^2)\\
&=\delta_{ij}+O(\theta^2).
\end{aligned}
\tag{70.29}
$$

有限变换就是$U\delta U^T=\delta$，所以这是一条精确的不变关系。其单态落在对称平方中。若改用一般酉基，不变张量也要随基变换，不一定仍具有数值$\delta_{ij}$的外形。

对$SO(N)$向量的平方，任意矩阵$X_{ij}$可以明确分成
<span id="eq:c70-so-projections"></span>

$$
\begin{aligned}
(P_1X)_{ij}&=\frac{\delta_{ij}}N X_{kk},\\
(P_AX)_{ij}&=\frac12(X_{ij}-X_{ji}),\\
(P_SX)_{ij}&=\frac12(X_{ij}+X_{ji})-\frac{\delta_{ij}}N X_{kk},\\
X&=P_1X+P_AX+P_SX.
\end{aligned}
\tag{70.30}
$$

指标互换与取迹都同正交变换相容，因此每一部分各自变换。直接再施一次投影可知$P_r^2=P_r$；在不同部分之间投影为零。反对称矩阵按$X\mapsto OXO^T=OXO^{-1}$变换，与正交代数的伴随作用相同。对称部分减去一个迹后满足$X_{ij}=X_{ji}$及$X_{ii}=0$，将这一表示记作$S$，便有
<span id="eq:c70-so-decomposition"></span>

$$
\begin{aligned}
N\otimes N&=1_{\rm S}\oplus A_{\rm A}\oplus S_{\rm S},\\
D(A)&=\frac{N(N-1)}2,\qquad
D(S)=\frac{N(N+1)}2-1.
\end{aligned}
\tag{70.31}
$$

下标$\mathrm S,\mathrm A$说明交换两个向量指标时的对称性，不是另一个群标签。维数分别来自上三角或含对角的上三角元素计数，三部分之和仍为$N^2$。这先给出三个自然不变子空间；低秩群中还要留意进一步分解，例如在四维内部欧氏空间，定义$(*X)_{ij}=\epsilon_{ijkl}X_{kl}/2$，双重对偶满足$*^2X=X$。于是$X_\pm=(X\pm*X)/2$分别满足$*X_\pm=\pm X_\pm$，各由三个分量确定；对偶又与$SO(4)$作用相容。这就将六维伴随分成两块三维不变表示。

这里使用的正交生成元可具体取成$T^{rs}=-i(E_{rs}-E_{sr})$、$r<s$，其中$E_{rs}$只有第$r$行第$s$列为1。利用$E_{rs}E_{tu}=\delta_{st}E_{ru}$，相同生成元的平方迹为2，不同生成元的内积为零，故基本指标为2。要算伴随指标，限制到前三个分量的$SO(3)$，写$m=N-3$，则$N$变成$3\oplus m1$。反对称平方分成三个来源：前三指标之间的$\Lambda^2 3\simeq3$，前三区与每个其余分量组成的$m$个三重态，以及其余指标之间的$m(m-1)/2$个单态。因此
<span id="eq:c70-so-index"></span>

$$
\begin{aligned}
A\big|_{SO(3)}&=(m+1)\,3\oplus\frac{m(m-1)}2\,1,\\
T_{SO(N)}(A)&=2(m+1)=2N-4,\qquad N\ge3.
\end{aligned}
\tag{70.32}
$$

三维$\epsilon_{ijk}$将反对称二阶张量映为向量，而$SO(3)$向量生成元为$-i\epsilon^{abc}$，所以每个三重态贡献指标2。这个分支的维数为$3(m+1)+m(m-1)/2=N(N-1)/2$。还可直接在反对称平方中计算全迹。令$\mathsf P(v\otimes w)=w\otimes v$、$P_-=(1-\mathsf P)/2$，则

<span id="eq:c70-so-exchange-trace"></span>

$$
\begin{aligned}
\operatorname{Tr}_{N\otimes N}[\mathsf P(X\otimes Y)]
 &=\sum_{ij}X_{ji}Y_{ij}=\operatorname{Tr}_N(XY),\\
\mathcal T^a&=T^a\otimes1+1\otimes T^a,\\
\operatorname{Tr}_{A}(\mathcal T^a\mathcal T^b)
 &=\tfrac12\bigl[2N\operatorname{Tr}(T^aT^b)
                  -4\operatorname{Tr}(T^aT^b)\bigr]\\
 &=(N-2)\operatorname{Tr}_N(T^aT^b)=2(N-2)\delta^{ab}.
\end{aligned}
\tag{70.53}
$$

不含交换算符的迹中，两项交叉项由生成元无迹而消失；含交换算符时，四项都成为同一个二次迹。$P_-$与$\mathcal T^a$对易，投影后的迹就是反对称子空间的总迹。这一计算也适用于$SO(4)$的完整伴随空间。

这些数值都随最初生成元的尺度而定。如果全体表示统一改成$T'^a=sT^a$，对易关系给$f'=sf$，而二次迹及卡西米尔给$T'(R)=s^2T(R)$、$C'(R)=s^2C(R)$。例如把这里的SO生成元缩小一半，基本指标才变成$1/2$，伴随指标同时变成$(N-2)/2$；计算规范作用时还要相应保持$gA^aT^a$。只有把这些变化同时实施，才是在比较两种归一下的同一计算。

<span id="c70-epsilon"></span>

## 伪实表示与反对称单态

实表示的单态由对称双线性型给出。伪实表示也同其共轭等价，但相应不变张量为反对称型。这个区别可从前面的$V$直接看出。关系$T^aV=-V(T^a)^T$使
<span id="eq:c70-bilinear-type"></span>

$$
U_RVU_R^T=V,\qquad V^T=cV,\qquad c=\pm1.
\tag{70.33}
$$

因而$V$本身是$R\otimes R$中的不变向量。对不可约表示，若还有一个线性独立的非零交织矩阵$W$，$WV^{-1}$就会同全部生成元对易，与舒尔引理矛盾；所以不变双线性型只有一个方向。实型的$c=+1$把单态放进对称平方，伪实型的$c=-1$把它放进反对称平方。不变双线性型的唯一性因而需要不可约条件。

基本表示还有一个直接可写的不变张量。令$\epsilon_{i_1\cdots i_N}$为完全反对称符号，它在$N$个$SU(N)$矩阵作用下变为
<span id="eq:c70-epsilon-determinant"></span>

$$
U_{i_1}{}^{j_1}\cdots U_{i_N}{}^{j_N}
\epsilon_{j_1\cdots j_N}
=(\det U)\epsilon_{i_1\cdots i_N}
=\epsilon_{i_1\cdots i_N}.
\tag{70.34}
$$

第一步可由行列式的定义看出：左边对$i_1,\ldots,i_N$反对称，而完全反对称的$N$阶张量只有一个独立分量；取这组指标为$1,\ldots,N$时，其比例系数正是行列式。第二步才用$\det U=1$。反基本表示同样有上指标的完全反对称不变量，因为$\det U^*=1$。

对$SU(2)$，取内部符号$\epsilon^{12}=\epsilon_{21}=1$、$\epsilon^{21}=\epsilon_{12}=-1$。这些分量号与第34节的书写形式相同，但内部指标与旋量指标属于各自独立的空间。矩阵形式为
<span id="eq:c70-internal-epsilon"></span>

$$
E=(\epsilon_{ij})=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
E^{-1}=(\epsilon^{ij})=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\qquad
\epsilon^{ik}\epsilon_{kj}=\delta^i_j.
\tag{70.35}
$$

$UEU^T=E$说明反对称平方是一维单态。剩下的对称平方由$e_1e_1$、$(e_1e_2+e_2e_1)/\sqrt2$、$e_2e_2$张成。把$T^a\otimes1+1\otimes T^a$作用于这三个基向量，得到
<span id="eq:c70-su2-square"></span>

$$
\begin{gathered}
T^3_{\rm sym}=\operatorname{diag}(1,0,-1),\qquad
T^+_{\rm sym}=\sqrt2
\begin{pmatrix}0&1&0\\0&0&1\\0&0&0\end{pmatrix},\\
2\otimes2=1_{\rm A}\oplus3_{\rm S}.
\end{gathered}
\tag{70.36}
$$

这里$T^+=T^1+iT^2$，降算符是它的厄米共轭。三个权重为$1,0,-1$，并由升降算符连通，所以对称部分正是自旋1的三重态，也就是伴随表示。这就是式[（70.28）](#eq:c70-su-subgroup-index)所用的具体分解。

同一个$\epsilon$还可把下指标改写成上指标。由$UEU^T=E$得$E^{-1}U=U^{-T}E^{-1}=U^*E^{-1}$，所以
<span id="eq:c70-epsilon-raising"></span>

$$
\varphi^i:=\epsilon^{ij}\varphi_j,\qquad
\varphi^{i\prime}=(U^*)^i{}_j\varphi^j.
\tag{70.37}
$$

这个升指标关系说明，同一组场分量经固定的线性变换，改按共轭表示书写。它与$\varphi^{\dagger i}=(\varphi_i)^\dagger$是两种操作；伪实性使两种表示等价，并不把复共轭变成线性运算。

<span id="c70-cubic"></span>

## 三重迹与异常系数

二重迹给出不变的$\delta^{ab}$，三重迹则把结构常数和另一种完全对称张量带入计算。先将李括号与另一个生成元相乘后取迹：
<span id="eq:c70-f-trace"></span>

$$
\begin{aligned}
-i\operatorname{Tr}_R(T_R^a[T_R^b,T_R^c])
&=-i\,i f^{bcd}\operatorname{Tr}_R(T_R^aT_R^d)\\
&=T(R)f^{bca}=T(R)f^{abc}.
\end{aligned}
\tag{70.38}
$$

迹中的共轭矩阵首尾相消，因此它给出三个伴随指标的不变张量。选择$T(R)\ne0$的表示便得到$f^{abc}$的不变性。也可在式[（70.21）](#eq:c70-generator-tensor)中取$R=A$，用$T_A=-if$直接得到同一结论；它对应雅可比恒等式的张量形式。

把交换子换成反对易子，定义
<span id="eq:c70-symmetric-trace"></span>

$$
\begin{aligned}
B_R^{abc}&:=\frac12\operatorname{Tr}_R
 \bigl(T_R^a\{T_R^b,T_R^c\}\bigr)\\
&=\frac12\left[\operatorname{Tr}_R(T_R^aT_R^bT_R^c)
 +\operatorname{Tr}_R(T_R^aT_R^cT_R^b)\right].
\end{aligned}
\tag{70.39}
$$

$b,c$交换不变，循环迹又使$a,b$交换后仍为同样两项，所以$B_R$完全对称。对其取复共轭会倒转每项的矩阵次序，迹循环把两项互换，因此$B_R$为实。它的不变性也可逐项写出：
<span id="eq:c70-cubic-invariance"></span>

$$
\begin{aligned}
&f^{dae}B_R^{ebc}+f^{dbe}B_R^{aec}+f^{dce}B_R^{abe}\\
&\hspace{12mm}=-\frac i2\operatorname{Tr}_R
 [T_R^d,T_R^a\{T_R^b,T_R^c\}]=0.
\end{aligned}
\tag{70.40}
$$

右边交换子按乘积法则展开正好给出左边三种指标的变化，其迹为零。

不同表示的三次对称迹能否写成一个固定张量$d^{abc}$乘系数$A(R)$，取决于不变三次张量空间的维数。为回答这个问题，先取$SU(N\ge3)$。令$H=h_aT_N^a$为基本表示中的无迹厄米矩阵，在任意表示中定义
<span id="eq:c70-invariant-cubic-polynomial"></span>

$$
P_R(H):=\operatorname{Tr}_R\bigl[(h_aT_R^a)^3\bigr].
\tag{70.41}
$$

这是关于$H$的三次齐次多项式，在$H\mapsto UHU^{-1}$下不变。厄米矩阵可以酉对角化，把对角化矩阵乘一个公共相位即可使其行列式为1，所以只须考察$H=\operatorname{diag}(h_1,\ldots,h_N)$、$\sum_i h_i=0$。任意对角元置换也可以在$SU(N)$中实现：若置换矩阵的行列式为$-1$，乘一个与对角矩阵对易的对角相位矩阵加以补偿。因此$P_R$在这些对角元上是对称三次多项式。

三次单项式只有三种指标重复方式：$h_i^3$、$h_i^2h_j$和$h_ih_jh_k$。若先用$h_i-\sum_jh_j/N$把函数延拓到独立的$h_i$，便可按这三类对称单项式求和，再限制回无迹平面。在这个平面上，
<span id="eq:c70-cubic-polynomial-basis"></span>

$$
\begin{aligned}
s_3&:=\sum_i h_i^3,\\
\sum_{i\ne j}h_i^2h_j
&=\sum_i h_i^2\left(\sum_jh_j-h_i\right)=-s_3,\\
0=\left(\sum_i h_i\right)^3
&=s_3+3\sum_{i\ne j}h_i^2h_j
 +6\sum_{i<j<k}h_ih_jh_k,\\
\sum_{i<j<k}h_ih_jh_k&=\frac13s_3.
\end{aligned}
\tag{70.42}
$$

所以只剩一个独立方向$s_3=P_N(H)$。当$N\ge3$，取对角元$(1,1,-2,0,\ldots)$得到$s_3=-6$，它不恒为零。于是存在唯一的比例系数$A(R)$，使$P_R=A(R)P_N$。

还须从相同矩阵的三次方恢复三个独立指标。设$X,Y,Z$为基本空间的三个无迹厄米矩阵，用相同系数映入$R$，展开$P_R(sX+tY+uZ)$。含$stu$的项有六种有序乘积，迹循环把它们分成两组，每组三项，因此
<span id="eq:c70-cubic-polarization"></span>

$$
B_R(X,Y,Z)=\left.\frac16
 \frac{\partial^3}{\partial s\,\partial t\,\partial u}
 P_R(sX+tY+uZ)\right|_{s=t=u=0}.
\tag{70.43}
$$

这个极化公式把对角化得到的比例推广到全部对称指标。取基本表示的三次对称迹作为基准，定义
<span id="eq:c70-anomaly-coefficient"></span>

$$
\begin{gathered}
d^{abc}:=B_N^{abc},\qquad B_R^{abc}=A(R)d^{abc},\\
A(N)=1\quad(SU(N),\ N\ge3).
\end{gathered}
\tag{70.44}
$$

$A(R)$称为异常系数。这个名称预示它在后面的三角图计算中所起的作用；到这里我们建立的是表示论恒等式。

定义[（70.39）](#eq:c70-symmetric-trace)含三次迹前的$1/2$。把基本反对易子代入式[（70.25）](#eq:c70-su-decomposition)，其单位矩阵投影为$\delta^{ab}/N$，生成元投影则为$2\operatorname{Tr}(T^c\{T^a,T^b\})=4d^{abc}$，因此
<span id="eq:c70-d-normalization"></span>

$$
\{T^a,T^b\}=\frac{\delta^{ab}}N\mathbf1+4d^{abc}T^c.
\tag{70.45}
$$

若以右边生成元的系数另定义$d_{\rm alt}^{abc}$，就有$d_{\rm alt}=4d$，两种记号在比较公式时须作这个转换。一个直接的检验来自$SU(3)$中归一化的对角生成元：
<span id="eq:c70-su3-cubic-example"></span>

$$
\begin{aligned}
T^8&=\frac1{2\sqrt3}\operatorname{diag}(1,1,-2),\\
d^{888}&=\operatorname{Tr}\bigl[(T^8)^3\bigr]
=\frac{1+1-8}{(2\sqrt3)^3}
=-\frac1{4\sqrt3}.
\end{aligned}
\tag{70.46}
$$

这里的迹作用于矩阵三次方。它同时核对了基本$A=1$与式[（70.45）](#eq:c70-d-normalization)中的4。

共轭表示的生成元是负转置，三个生成元给出三个负号。转置使次序倒转，再用循环迹，得
<span id="eq:c70-conjugate-anomaly"></span>

$$
\begin{aligned}
B_{\bar R}^{abc}
&=-\frac12\operatorname{Tr}_R
 \bigl(\{T_R^b,T_R^c\}T_R^a\bigr)
=-B_R^{abc},\\
A(\bar R)&=-A(R).
\end{aligned}
\tag{70.47}
$$

若$R$实或伪实，酉等价又要求$B_{\bar R}=B_R$，所以三次对称迹为零。直和则按块分别取迹，给$B_{R_1\oplus R_2}=B_{R_1}+B_{R_2}$，从而
<span id="eq:c70-sum-anomaly"></span>

$$
A(R_1\oplus R_2)=A(R_1)+A(R_2).
\tag{70.48}
$$

对直积仍使用式[（70.16）](#eq:c70-product-generator)。三个生成元相乘共有八项，两项完全来自一个因子，其余六项在某个因子上只含一个生成元。将这六项也写出，总迹为
<span id="eq:c70-product-cubic-trace"></span>

$$
\begin{aligned}
\operatorname{Tr}_{12}(T^aT^bT^c)
={}&D_2\operatorname{Tr}_1(T_1^aT_1^bT_1^c)
 +D_1\operatorname{Tr}_2(T_2^aT_2^bT_2^c)\\
&+\operatorname{Tr}_1(T_1^aT_1^b)\operatorname{Tr}_2T_2^c
 +\operatorname{Tr}_1(T_1^aT_1^c)\operatorname{Tr}_2T_2^b\\
&+\operatorname{Tr}_1(T_1^bT_1^c)\operatorname{Tr}_2T_2^a
 +\operatorname{Tr}_1T_1^a\operatorname{Tr}_2(T_2^bT_2^c)\\
&+\operatorname{Tr}_1T_1^b\operatorname{Tr}_2(T_2^aT_2^c)
 +\operatorname{Tr}_1T_1^c\operatorname{Tr}_2(T_2^aT_2^b).
\end{aligned}
\tag{70.49}
$$

后三行全由无迹性消失。将第一行同$b,c$互换的结果相加再除以2，便得到直积的异常系数：
<span id="eq:c70-product-anomaly"></span>

$$
A(R_1\otimes R_2)=A(R_1)D(R_2)+D(R_1)A(R_2).
\tag{70.50}
$$

式[（70.48）](#eq:c70-sum-anomaly)、[（70.50）](#eq:c70-product-anomaly)必须使用同一个固定非零$d$。对其它群，需先确定其不变三次张量空间，不能只凭有复表示就任选一个$A=1$。

$SU(2)$可以直接沿刚才的多项式论证处理。对角元只有$(h,-h)$，群共轭可把$h$换成$-h$，故不变多项式必须是$h$的偶函数；三次齐次性却要求它是奇函数，于是
<span id="eq:c70-su2-cubic-zero"></span>

$$
P_R(H)=0,\qquad B_R^{abc}=0
\quad\text{（任意有限维 }SU(2)\text{ 表示）}.
\tag{70.51}
$$

第二个结论再由极化得到。对这种情形，约定$A(R)=0$。表示的实性也能说明这一点。沿第33节已经构造的角动量基$|j,m\rangle$，令反线性算符
<span id="eq:c70-su2-reality"></span>

$$
\mathcal J_j|j,m\rangle=(-1)^{j-m}|j,-m\rangle,\qquad
\mathcal J_j^2=(-1)^{2j}\mathbf1.
\tag{70.52}
$$

对$J_3$，翻转$m$立即给$\mathcal J_jJ_3=-J_3\mathcal J_j$；对升降算符，$J_+|j,m\rangle=\sqrt{(j-m)(j+m+1)}|j,m+1\rangle$中的实系数在$m\mapsto-m$后对应$J_-$，而相邻$m$的相位差为负，故$\mathcal J_jJ_+=-J_-\mathcal J_j$。结合反线性对$i$的变号，三个$J_a$均满足$\mathcal J_jJ_a=-J_a\mathcal J_j$，其群变换与$\mathcal J_j$对易。所以整数$j$为实型，半整数$j$为伪实型，各不可约块的三次迹都为零；直和仍为零。

利用交换投影，可以进一步求出带两个基本指标的表示的二次与三次群因子。随后将同一连接作用于复合场，便得到协变乘积法则与比安基恒等式。

<span id="c70-two-index"></span>

## 两个基本指标的SU(N)表示

把$N\otimes N$分为对称平方$\mathcal S$与反对称平方$\mathcal A$。这里用花体字母$\mathcal A$区别于伴随表示$A$。在矩阵分量$X_{ij}$上，$P_\pm=(1\pm\mathsf P)/2$分别取对称与反对称部分。由$\operatorname{Tr}\mathsf P=N$可得
<span id="eq:c70-two-index-dimensions"></span>

$$
N\otimes N=\mathcal S\oplus\mathcal A,\qquad
D(\mathcal S)=\frac{N(N+1)}2,\qquad
D(\mathcal A)=\frac{N(N-1)}2.
\tag{70.54}
$$

对称部分包括$N$个对角元及$N(N-1)/2$对非对角元，反对称部分只有后者。沿式[（70.53）](#eq:c70-so-exchange-trace)的迹计算，使用基本归一$\operatorname{Tr}(T^aT^b)=\delta^{ab}/2$，得到
<span id="eq:c70-two-index-quadratic"></span>

$$
\begin{aligned}
\operatorname{Tr}_{P_\pm}(\mathcal T^a\mathcal T^b)
 &=\tfrac12(2N\pm4)\operatorname{Tr}_N(T^aT^b),\\
T(\mathcal S)&=\frac{N+2}2,\qquad
T(\mathcal A)=\frac{N-2}2.
\end{aligned}
\tag{70.55}
$$

也可限制到只作用于前两个分量的$SU(2)$子群计算。令$n=N-2$，基本表示限制为$2\oplus n1$，对称与反对称平方分别成为
<span id="eq:c70-two-index-su2-branching"></span>

$$
\begin{aligned}
\mathcal S\big|_{SU(2)}
 &=3\oplus n2\oplus\frac{n(n+1)}2\,1,\\
\mathcal A\big|_{SU(2)}
 &=1\oplus n2\oplus\frac{n(n-1)}2\,1,\\
T(\mathcal S)&=2+\frac n2,\qquad
T(\mathcal A)=\frac n2.
\end{aligned}
\tag{70.56}
$$

第一项来自前两个指标的平方，第二项来自一个指标在二重态、另一个在单态，最后一项来自单态空间的平方。$P_\pm$已经把交叉积的两个次序合为一份，所以二重态的重数都是$n$。

取$N=3$，一个反对称张量只有三个分量。用行列式不变张量作线性映射，
<span id="eq:c70-su3-antisymmetric-conjugate"></span>

$$
\begin{aligned}
w^i&=\frac12\epsilon^{ijk}X_{jk},\qquad
X_{jk}=\epsilon_{ijk}w^i,\qquad \epsilon^{123}=\epsilon_{123}=1,\\
w^{i\prime}
 &=\frac12\epsilon^{ijk}U_j{}^lU_k{}^mX_{lm}
 =(U^{-1})_n{}^i w^n=(U^*)^i{}_n w^n,\\
\mathcal A_{SU(3)}&\simeq\bar3,\qquad A(\bar3)=-1.
\end{aligned}
\tag{70.57}
$$

第一行的逆映射来自$\epsilon^{ijk}\epsilon_{ljk}=2\delta^i_l$。第二行把第三个$U$补进三阶行列式，再用$\det U=1$消去，故三个反对称分量按反基本表示变换。

三次迹也能由同一个交换投影求出。令$H=h_aT_N^a$无迹，$\mathcal H=H\otimes1+1\otimes H$。展开其三次方，未插入$\mathsf P$时混合项含$\operatorname{Tr}H$而消失；插入后，系数$1,3,3,1$都乘$\operatorname{Tr}H^3$，于是
<span id="eq:c70-two-index-cubic-projection"></span>

$$
\begin{aligned}
\operatorname{Tr}_{N\otimes N}\mathcal H^3
 &=2N\operatorname{Tr}_NH^3,\\
\operatorname{Tr}_{N\otimes N}(\mathsf P\mathcal H^3)
 &=(1+3+3+1)\operatorname{Tr}_NH^3,\\
\operatorname{Tr}_{P_\pm}\mathcal H^3
 &=(N\pm4)\operatorname{Tr}_NH^3.
\end{aligned}
\tag{70.58}
$$

对$N\ge3$用极化公式恢复三个独立生成元，就有
<span id="eq:c70-two-index-anomalies"></span>

$$
A(\mathcal S)=N+4,\qquad A(\mathcal A)=N-4.
\tag{70.59}
$$

按$SU(3)$子群也能重得此结果。先由$3\otimes3=\bar3\oplus6$与直积异常系数求出$A(6)=6-A(\bar3)=7$。再令$n=N-3$，两种平方限制为
<span id="eq:c70-two-index-su3-branching"></span>

$$
\begin{aligned}
\mathcal S\big|_{SU(3)}&=6\oplus n3\oplus\frac{n(n+1)}2\,1,\\
\mathcal A\big|_{SU(3)}&=\bar3\oplus n3\oplus\frac{n(n-1)}2\,1,\\
A(\mathcal S)&=7+n=N+4,\qquad
A(\mathcal A)=-1+n=N-4.
\end{aligned}
\tag{70.60}
$$

嵌入生成元在其余基本分量上为零，故$SU(N)$的基本三次迹限制到这个子群后，正好是同一归一的$SU(3)$基本三次迹。各块异常系数可以直接相加。$N=2$时，三次迹对所有表示均为零，适用的是式[（70.51）](#eq:c70-su2-cubic-zero)的约定。

<span id="c70-covariant-products"></span>

## 协变导数的分配法则

### 对直积场求导

直积生成元是两种作用之和：
第一项只改变$\varphi_i$的指标，第二项只改变$\chi_I$的指标。
把它代入$D_\mu=\partial_\mu-igA_\mu^aT^a$，保持场的次序为$\varphi\chi$，
便有
<span id="eq:c70-ex-5-product-rule"></span>

$$
\begin{aligned}
\relax [D_\mu(\varphi\chi)]_{iI}
={}&\partial_\mu(\varphi_i\chi_I)\\
&-igA_\mu^a
 \left[(T_{R_1}^a)_i{}^j\delta_I{}^J
       +\delta_i{}^j(T_{R_2}^a)_I{}^J\right]\varphi_j\chi_J\\
={}&\left[\partial_\mu\varphi_i
     -igA_\mu^a(T_{R_1}^a)_i{}^j\varphi_j\right]\chi_I\\
&+\varphi_i\left[\partial_\mu\chi_I
     -igA_\mu^a(T_{R_2}^a)_I{}^J\chi_J\right]\\
={}&(D_\mu\varphi)_i\chi_I+\varphi_i(D_\mu\chi)_I .
\end{aligned}
\tag{70.61}
$$

普通导数先按乘积法则产生两项，
连接矩阵的两项恰好分别补成两个协变导数。
这里$D_\mu$是偶导数，不改变$\varphi\chi$的排列，
因而这一推导本身没有额外的格拉斯曼交换号。

### 收缩成单态后的导数

取$\varphi_i$属于$R$，其厄米共轭$\varphi^{\dagger i}$属于$\overline R$。
共轭表示的生成元带负转置：
<span id="eq:c70-ex-5-conjugate-derivative"></span>

$$
\begin{aligned}
(T_{\overline R}^a)^i{}_j&=-(T_R^a)_j{}^i,\\
(D_\mu\varphi^\dagger)^i
&=\partial_\mu\varphi^{\dagger i}
   +igA_\mu^a(T_R^a)_j{}^i\varphi^{\dagger j},\\
(D_\mu\varphi)_i
&=\partial_\mu\varphi_i
   -igA_\mu^a(T_R^a)_i{}^j\varphi_j .
\end{aligned}
\tag{70.62}
$$

于是
<span id="eq:c70-ex-5-singlet-derivative"></span>

$$
\begin{aligned}
(D_\mu\varphi^\dagger)^i\varphi_i
 +\varphi^{\dagger i}(D_\mu\varphi)_i
={}&\partial_\mu(\varphi^{\dagger i}\varphi_i)\\
&+igA_\mu^a
 \left[(T_R^a)_j{}^i\varphi^{\dagger j}\varphi_i
       -\varphi^{\dagger i}(T_R^a)_i{}^j\varphi_j\right]\\
={}&\partial_\mu(\varphi^{\dagger i}\varphi_i).
\end{aligned}
\tag{70.63}
$$

最后一步只把第一项中的虚指标$i,j$互换，
矩阵元为普通数，两个场的相对次序始终不变。
从表示角度看，这就是乘积法则在$\overline R\otimes R$上的应用，
再用不变的克罗内克符号投影到单态。
单态生成元为零，故投影后的协变导数成为普通导数。

<span id="c70-bianchi"></span>

## 比安基恒等式

在一个光滑的局部规范片中，先将场强看作矩阵值函数
$F_{\mu\nu}=F_{\mu\nu}^aT^a$，
并让微分算符作用于任意光滑测试多重态$h(x)$。
对易子$[D_\rho,F_{\mu\nu}]$是算符对易子；
把$D_\rho=\partial_\rho-igA_\rho$实际作用到$F_{\mu\nu}h$上，
有
<span id="eq:c70-ex-6-commutator-derivative"></span>

$$
\begin{aligned}
\relax [D_\rho,F_{\mu\nu}]h
&=\partial_\rho(F_{\mu\nu}h)-igA_\rho F_{\mu\nu}h
  -F_{\mu\nu}(\partial_\rho h-igA_\rho h)\\
&=\bigl[\partial_\rho F_{\mu\nu}
        -ig(A_\rho F_{\mu\nu}-F_{\mu\nu}A_\rho)\bigr]h\\
&=(D_\rho^{\rm ad}F_{\mu\nu})h .
\end{aligned}
\tag{70.64}
$$

含$\partial_\rho h$的两项相消，剩下的正是作用于场强的伴随协变导数。
把矩阵对易子再展开为结构系数，并代入
$(T_A^a)_{cb}=-if^{acb}$，得到
<span id="eq:c70-ex-6-adjoint-components"></span>

$$
\begin{aligned}
(D_\rho^{\rm ad}F_{\mu\nu})^c
&=\partial_\rho F_{\mu\nu}^c
   +g f^{abc}A_\rho^aF_{\mu\nu}^b\\
&=\partial_\rho F_{\mu\nu}^c
   -igA_\rho^a(T_A^a)_{cb}F_{\mu\nu}^b .
\end{aligned}
\tag{70.65}
$$

第二行中$(-i)(-i)=-1$，
再用$f^{acb}=-f^{abc}$，便恢复第一行的正号。
伴随导数的分量号由此与矩阵对易子一致。

微分算符的复合满足结合律，因而具有雅可比恒等式。
为看清这里使用的只是结合律，将三个嵌套对易子展开：
<span id="eq:c70-ex-6-operator-jacobi"></span>

$$
\begin{aligned}
\mathcal J
:={}&[D_\mu,[D_\nu,D_\rho]]
 +[D_\nu,[D_\rho,D_\mu]]
 +[D_\rho,[D_\mu,D_\nu]]\\
={}&D_\mu D_\nu D_\rho-D_\mu D_\rho D_\nu
    -D_\nu D_\rho D_\mu+D_\rho D_\nu D_\mu\\
&+D_\nu D_\rho D_\mu-D_\nu D_\mu D_\rho
    -D_\rho D_\mu D_\nu+D_\mu D_\rho D_\nu\\
&+D_\rho D_\mu D_\nu-D_\rho D_\nu D_\mu
    -D_\mu D_\nu D_\rho+D_\nu D_\mu D_\rho=0 .
\end{aligned}
\tag{70.66}
$$

六种有序的三算符乘积各出现一次正号和一次负号，
其相消不要求两个$D$彼此对易。
场强的定义$F_{\nu\rho}=(i/g)[D_\nu,D_\rho]$
等价于$[D_\nu,D_\rho]=-igF_{\nu\rho}$。
将其代入上式，再用式[（70.64）](#eq:c70-ex-6-commutator-derivative)，
得到
<span id="eq:c70-ex-6-bianchi"></span>

$$
\begin{aligned}
0&=-ig\bigl(D_\mu^{\rm ad}F_{\nu\rho}
          +D_\nu^{\rm ad}F_{\rho\mu}
          +D_\rho^{\rm ad}F_{\mu\nu}\bigr),\\
0&=(D_\mu F_{\nu\rho})^a
  +(D_\nu F_{\rho\mu})^a
  +(D_\rho F_{\mu\nu})^a .
\end{aligned}
\tag{70.67}
$$

在第二行先按$g\ne0$消去公共系数，再比较线性无关的生成元；
其分量表达式也连续延伸到$g=0$。
这一恒等式由连接和场强的定义对任意光滑规范势成立，
表达的是场强各分量之间的几何约束，它在施加运动方程之前便已成立。

---

[← 第 69 节](/posts/srednicki-69/) · [章节地图](/srednicki/) · [第 71 节 →](/posts/srednicki-71/)
