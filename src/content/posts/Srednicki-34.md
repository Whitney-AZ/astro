---
title: 'Srednicki §34 左手和右手旋量场'
date: 2026-09-14
category: 笔记
tags: [物理, 量子场论, Srednicki]
series: 'Srednicki QFT'
srednickiSections: [34]
hideFromHome: true
draft: false
---

<span id="c34"></span>

上一节找到了两种最简单的非标量表示：$(2,1)$和$(1,2)$。它们在空间转动下都是自旋$1/2$，各有两个分量，推动的作用却不同。要用这样的场描述物理，首先需要把变换矩阵具体写出，再弄清旋量指标如何共轭、升降和缩并。这些指标运算也将给出旋量与矢量之间的联系，使我们能回到上一节的二阶张量，将六个反对称分量进一步分成两个互不混合的三维部分。

以下沿用$(-,+,+,+)$度规、$K_i=M^{i0}$及[第 33 节](/posts/srednicki-33/)的分量变换方向。

<span id="c34-left"></span>

## 左手场的转动和推动

先考虑左手旋量场，也称左手外尔场（left-handed Weyl field），记为$\psi_a(x)$，其中$a=1,2$。在场的变换矩阵中，下标$a$标记行，求和指标$b$标记列。有限变换、群乘法和无穷小展开分别为
<span id="eq:c34-left-law"></span>

$$
\begin{gathered}
U(\Lambda)^{-1}\psi_a(x)U(\Lambda)
=L_a{}^b(\Lambda)\psi_b(\Lambda^{-1}x),\qquad
L(\Lambda'\Lambda)=L(\Lambda')L(\Lambda),\\
L(1+\omega)=I+\frac i2\omega_{\mu\nu}S_L^{\mu\nu}+O(\omega^2),
\qquad S_L^{\mu\nu}=-S_L^{\nu\mu}.
\end{gathered}
\tag{34.1}
$$

群乘法的次序沿用[（33.7）](/posts/srednicki-33/#eq:c33-composition-calculation)的逐次变换结果。将$U(1+\omega)=I+i\omega_{\mu\nu}M^{\mu\nu}/2$代入，等式左边的一阶变化是$i\omega_{\mu\nu}[\psi_a,M^{\mu\nu}]/2$。右边除矩阵变化外，还有宗量变化$-\omega^\rho{}_{\sigma}x^\sigma\partial_\rho\psi_a$。利用$\omega_{\mu\nu}$反对称，将后者写成$\omega_{\mu\nu}(x^\mu\partial^\nu-x^\nu\partial^\mu)\psi_a/2$，比较系数得到
<span id="eq:c34-left-commutator"></span>

$$
[\psi_a(x),M^{\mu\nu}]
=\mathcal L^{\mu\nu}\psi_a(x)+(S_L^{\mu\nu})_a{}^b\psi_b(x),
\qquad\mathcal L^{\mu\nu}=-i(x^\mu\partial^\nu-x^\nu\partial^\mu).
\tag{34.2}
$$

第一项仍是标量场已有的轨道作用，新增的内容在第二项的分量矩阵中。为将两者分开，先把场取在时空原点，使轨道项消失。再用$M^{ij}=\epsilon_{ijk}J_k$，转动生成元的作用便成为
<span id="eq:c34-origin-spin"></span>

$$
\epsilon_{ijk}[\psi_a(0),J_k]=(S_L^{ij})_a{}^b\psi_b(0).
\tag{34.3}
$$

左手场的两个分量只组成一个自旋$1/2$表示，因此可以选择通常的角动量基底，使$J_i$的分量矩阵为$\sigma_i/2$。这里的三个泡利矩阵是
<span id="eq:c34-pauli"></span>

$$
\sigma_1=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
\sigma_2=\begin{pmatrix}0&-i\\i&0\end{pmatrix},\quad
\sigma_3=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
\tag{34.4}
$$

它们的乘法决定了随后转动、推动及指标转换中的矩阵运算。逐项相乘得到$\sigma_i^2=I$、$\sigma_1\sigma_2=i\sigma_3$及其循环式，不同矩阵反向相乘时变号。将这些结果写成统一的指标形式，有
<span id="eq:c34-pauli-products"></span>

$$
\sigma_i\sigma_j=\delta_{ij}I+i\epsilon_{ijk}\sigma_k,
\quad [\sigma_i,\sigma_j]=2i\epsilon_{ijk}\sigma_k,
\quad \{\sigma_i,\sigma_j\}=2\delta_{ij}I.
\tag{34.5}
$$

将这组自旋矩阵代入原点处的角动量变换式，便得到空间生成元：
<span id="eq:c34-left-rotation-generator"></span>

$$
S_L^{ij}=\frac12\epsilon_{ijk}\sigma_k.
\tag{34.6}
$$

例如，$S_L^{12}=\sigma_3/2$的两个对角元为$+1/2,-1/2$，非对角元为零。这里两类指标各有作用：时空指标$12$先选出六个生成元中的一个，旋量指标$a,b$再选出这个矩阵中的某个元素。

推动矩阵由左手表示的另一项特征确定：第二个角动量因子平凡，即$\bar N_i=0$。于是由$J_i=N_i+\bar N_i$、$K_i=i(N_i-\bar N_i)$可得$K_i=iJ_i$，从而
<span id="eq:c34-left-boost-generator"></span>

$$
S_L^{i0}=\frac i2\sigma_i,\qquad S_L^{0i}=-\frac i2\sigma_i.
\tag{34.7}
$$

至此六个矩阵都已写出。它们满足洛伦兹代数的原因也可直接从泡利矩阵乘法看出：转动之间的关系$[J_i,J_j]=i\epsilon_{ijk}J_k$由泡利矩阵对易式给出，转动与推动之间有$[J_i,iJ_j]=i\epsilon_{ijk}(iJ_k)$，两个推动之间则有$[iJ_i,iJ_j]=-i\epsilon_{ijk}J_k$。最后一个负号来自两个虚数因子。用$S_L^{ij}=\epsilon_{ijk}J_k$、$S_L^{i0}=K_i$重新组合时空指标，混合类与两推动类分别为

<span id="eq:c34-index-algebra"></span>

$$
\begin{aligned}
[S_L^{ij},S_L^{k0}]
&=i\epsilon_{ijr}\epsilon_{rks}K_s
=i(\delta_{ik}S_L^{j0}-\delta_{jk}S_L^{i0}),\\
[S_L^{i0},S_L^{j0}]&=-i\epsilon_{ijk}J_k=-iS_L^{ij}.
\end{aligned}
$$

第二行的负号正是四维代数中的$g^{00}=-1$。纯空间类先算出$[S_L^{ij},S_L^{kl}]=i\epsilon_{ijr}\epsilon_{kls}\epsilon_{rst}J_t=i(\epsilon_{kli}J_j-\epsilon_{klj}J_i)$，再将$J$换回$S_L$，结果为$i(\delta_{ik}S_L^{jl}-\delta_{jk}S_L^{il}-\delta_{il}S_L^{jk}+\delta_{jl}S_L^{ik})$。这三类穷尽六个生成元的对易关系，恢复[（33.13）](/posts/srednicki-33/#eq:c33-lorentz-algebra)。

有了生成元，有限转动和推动可以通过指数求出。设$\hat{\mathbf n}$为单位矢量，泡利矩阵乘法给出$(\hat{\mathbf n}\cdot\boldsymbol\sigma)^2=I$。因此泡利矩阵组合的偶次幂都成为单位矩阵，奇次幂都剩下该组合；将两类项分别求和，得到
<span id="eq:c34-finite-left"></span>

$$
\begin{aligned}
L_{\rm rot}(\theta)&=e^{-i\theta\hat{\mathbf n}\cdot\boldsymbol\sigma/2}
=I\cos\frac\theta2-i\hat{\mathbf n}\cdot\boldsymbol\sigma\sin\frac\theta2,\\
L_{\rm boost}(\eta)&=e^{-\eta\hat{\mathbf n}\cdot\boldsymbol\sigma/2}
=I\cosh\frac\eta2-\hat{\mathbf n}\cdot\boldsymbol\sigma\sinh\frac\eta2.
\end{aligned}
\tag{34.8}
$$

推动指数中的负号来自$+i\eta_iK_i$与$K_i=i\sigma_i/2$相乘。转动的三角函数与推动的双曲函数分别体现了这两种变换的区别：转动矩阵幺正，推动矩阵是正定厄米矩阵，而二者的行列式都为1。

<span id="c34-right"></span>

## 共轭场及点指标

左手场的厄米共轭仍有两个分量，但其变换矩阵会随之改变。为把共轭场的指标同原场区别开，对每个分量取共轭后在指标上加点，定义
<span id="eq:c34-dotted-definition"></span>

$$
[\psi_a(x)]^\dagger=\psi^\dagger_{\dot a}(x),\qquad
\dot a=\dot1,\dot2.
\tag{34.9}
$$

将[（34.1）](#eq:c34-left-law)逐分量取厄米共轭，并利用$U$的幺正性，共轭后的场变换为
<span id="eq:c34-right-law"></span>

$$
U^{-1}\psi^\dagger_{\dot a}(x)U
=L_a{}^b(\Lambda)^*\psi^\dagger_{\dot b}(\Lambda^{-1}x)
\equiv R_{\dot a}{}^{\dot b}(\Lambda)
\psi^\dagger_{\dot b}(\Lambda^{-1}x).
\tag{34.10}
$$

所以，两个下点分量组成的列按$R=L^*$变换。这里每个矩阵元各自取复共轭，行和列的位置保持不变。由于$(L'L)^*=L'^*L^*$，连续两次变换仍给出$R(\Lambda'\Lambda)=R(\Lambda')R(\Lambda)$，乘法次序同左手表示相同。再将右手矩阵写成$R=I+i\omega_{\mu\nu}S_R^{\mu\nu}/2$，同左手展开的复共轭比较：实参数$\omega$保持不变，而$i$变号，故生成元之间满足
<span id="eq:c34-right-generators"></span>

$$
S_R^{\mu\nu}=-(S_L^{\mu\nu})^*,\qquad
J_{R,i}=-\frac12\sigma_i^*,\qquad K_{R,i}=\frac i2\sigma_i^*.
\tag{34.11}
$$

这时$N_{R,i}=0$、$\bar N_{R,i}=-\sigma_i^*/2$，非平凡作用由第二个角动量因子给出。后一组矩阵仍满足角动量代数，是自旋$1/2$的一组等价矩阵。因此共轭场属于$(1,2)$表示，称为右手外尔场。

生成元关系中的负号也可以从算符共轭的次序看出。先在原点写出右手场的对易式，再逐分量取厄米共轭：
<span id="eq:c34-adjoint-commutator"></span>

$$
\begin{aligned}
\relax[\psi^\dagger_{\dot a},M^{\mu\nu}]
&=(S_R^{\mu\nu})_{\dot a}{}^{\dot b}\psi^\dagger_{\dot b},\\
[M^{\mu\nu},\psi_a]&=\bigl[(S_R^{\mu\nu})_{\dot a}{}^{\dot b}\bigr]^*\psi_b.
\end{aligned}
\tag{34.12}
$$

由于$(AB-BA)^\dagger=B^\dagger A^\dagger-A^\dagger B^\dagger$，共轭使对易子的次序反转。把第二行左边改回$[\psi_a,M^{\mu\nu}]$时便产生负号，与[（34.2）](#eq:c34-left-commutator)比较后正是[（34.11）](#eq:c34-right-generators)。在一般$x$处，场的宗量也随变换改变，恢复同一个轨道项即可。

<span id="c34-epsilon"></span>

## 两个左手指标与不变的反对称符号

知道单个旋量指标的变换后，可以仿照上一节的张量分解，考虑带两个左手指标的场$C_{ab}$，并问它的四个分量能否分成各自独立变换的部分。暂时省略时空宗量，每个指标各作用一个左手变换矩阵：
<span id="eq:c34-two-left"></span>

$$
C'_{ab}=L_a{}^cL_b{}^dC_{cd},\qquad C'=LCL^T.
\tag{34.13}
$$

交换两个指标与施行变换可以按任意次序进行，所以对称部分和反对称部分各自封闭。这个分解也可从角动量合成看出：两个自旋$1/2$的乘积包含一个自旋0和一个自旋1。取相应的归一基为
<span id="eq:c34-singlet-triplet"></span>

$$
\frac{|12\rangle-|21\rangle}{\sqrt2};\qquad
|11\rangle,\quad\frac{|12\rangle+|21\rangle}{\sqrt2},\quad|22\rangle.
\tag{34.14}
$$

用总生成元$J_3=\sigma_3/2\otimes I+I\otimes\sigma_3/2$作用，后三态的权重依次为$1,0,-1$，总降算符以系数$\sqrt2$依次将它们相连；第一态则同时被总升、降算符和$J_3$消去，因此是单态。两个左手因子的推动都是$iJ$，所以这两部分在推动下也各自封闭，得到洛伦兹分解$(2,1)\otimes(2,1)=(1,1)_{\rm A}\oplus(3,1)_{\rm S}$。

这个唯一的反对称单态可以用一个固定的反对称矩阵表示。二维反对称矩阵只有一个独立分量，因此只须选定它的归一化。取矩阵及其逆为
<span id="eq:c34-epsilon-matrices"></span>

$$
E=(\epsilon_{ab})=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
E^{-1}=(\epsilon^{ab})=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
\tag{34.15}
$$

要让这个固定符号代表标量方向，它必须在两个指标同时变换后保持不变。左手生成元无迹，因而它们的指数及指数的乘积都有行列式1。将左手矩阵写成一般二阶形式$L=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)$，直接作矩阵乘法得到
<span id="eq:c34-epsilon-invariance"></span>

$$
LEL^T=
\begin{pmatrix}0&bc-ad\\ad-bc&0\end{pmatrix}
=(\det L)E=E.
\tag{34.16}
$$

在指标记号中，不变性写为$L_a{}^cL_b{}^d\epsilon_{cd}=\epsilon_{ab}$。于是沿这个不变反对称方向的系数只按标量变换，其余部分对称。相应分解和两个部分的表达式为
<span id="eq:c34-two-spinor-projections"></span>

$$
C_{ab}=\epsilon_{ab}D+G_{ab},\qquad
D=\frac12(C_{21}-C_{12})=-\frac12\epsilon^{ab}C_{ab},\qquad
G_{ab}=\frac12(C_{ab}+C_{ba}).
\tag{34.17}
$$

变换时，反对称部分的标量系数$D$只改变宗量，对称部分$G$则有三个分量，组成$(3,1)$表示。这里$\epsilon$在两个指标同时变换下保持不变，所起的作用类似于度规恒等式$\Lambda_\mu{}^\rho\Lambda_\nu{}^\sigma g_{\rho\sigma}=g_{\mu\nu}$：不变的双指标符号可以用来联系上、下两种指标位置。

<span id="c34-indices"></span>

## 升降指标及缩并的次序

既然反对称符号及其逆都已确定，就可以用它们定义旋量指标的升降。先将[（34.15）](#eq:c34-epsilon-matrices)中的矩阵相乘，有
<span id="eq:c34-epsilon-inverse"></span>

$$
\epsilon_{ab}\epsilon^{bc}=\delta_a{}^c,\qquad
\epsilon^{ab}\epsilon_{bc}=\delta^a{}_c.
\tag{34.18}
$$

互逆关系保证了升起再降下能够恢复原分量。因此规定
<span id="eq:c34-raising"></span>

$$
\psi^a=\epsilon^{ab}\psi_b,\qquad
\psi_a=\epsilon_{ab}\psi^b;\qquad
\psi^1=\psi_2,\quad\psi^2=-\psi_1.
\tag{34.19}
$$

先升再降确实给出$\epsilon_{ab}\epsilon^{bc}\psi_c=\psi_a$。上下指标的$\epsilon$作为矩阵互为逆，数值上的符号恰好相反；此外，它的两个指标交换时也会变号。将同一个升指标操作改写成几种等价形式，可以看清这一点：
<span id="eq:c34-epsilon-order"></span>

$$
\psi^a=\epsilon^{ab}\psi_b
=-\epsilon^{ba}\psi_b=-\psi_b\epsilon^{ba}=\psi_b\epsilon^{ab}.
\tag{34.20}
$$

$\epsilon$是数值常量，可以移到场的任意一侧；这里出现的负号都来自它自身的指标交换。两个场缩并时也有相应规则：保持场的乘法次序，只改变缩并指标的上、下位置，得到
<span id="eq:c34-contraction-sign"></span>

$$
\begin{aligned}
\psi^a\chi_a
&=\epsilon^{ab}\psi_b\chi_a
=-\psi_b\epsilon^{ba}\chi_a=-\psi_b\chi^b\\
&=\psi_2\chi_1-\psi_1\chi_2.
\end{aligned}
\tag{34.21}
$$

这次缩并中的负号同样来自$\epsilon$的反对称性，两个场的先后次序始终相同。

右手指标采用相同的归一化，即$\epsilon^{\dot1\dot2}=\epsilon_{\dot2\dot1}=+1$。由$R=L^*$及矩阵$E$为实数，左手不变式的共轭给出$RER^T=E$，所以刚才的升降与缩并步骤将无点指标逐一换成点指标后仍然成立。例如$\psi^{\dagger\dot1}=\psi^\dagger_{\dot2}$、$\psi^{\dagger\dot2}=-\psi^\dagger_{\dot1}$。

同一个右手场改用上点分量列时，变换矩阵也随基底改变。将升降矩阵放在原变换的两侧，上点列按
<span id="eq:c34-right-raised"></span>

$$
R_{\rm up}=E^{-1}L^*E=(L^\dagger)^{-1}
\tag{34.22}
$$

变换。最后一个等号来自$L^TEL=E$的共轭形式；这里$L^TEL=E$仍由同一个二维行列式恒等式得到。又因为$E^{-1}\sigma_i^*E=-\sigma_i$，上点基底中的生成元成为$J_{R,i}=\sigma_i/2$、$K_{R,i}=-i\sigma_i/2$，同第33节按两个角动量因子选出的基底一致。因此，下点列用$L^*$，上点列用$(L^\dagger)^{-1}$，是同一个右手场采用不同分量基底的写法。下一节将进一步固定缩并顺序，引入更简便的无指标记号。

<span id="c34-sigma"></span>

## 旋量与四矢量之间的字典

将一个无点指标与一个点指标组合，得到$(2,1)\otimes(1,2)=(2,2)$。上一节已将这个表示认作四矢量，因而两种指标体系之间应当存在可逆的对应。用单位矩阵和三个泡利矩阵把四矢量写成二阶矩阵：
<span id="eq:c34-vector-dictionary"></span>

$$
X_{a\dot a}=\sigma^\mu_{a\dot a}A_\mu,\qquad
\sigma^\mu=(I,\boldsymbol\sigma),\qquad
X=-A^0I+\mathbf A\cdot\boldsymbol\sigma.
\tag{34.23}
$$

例如$\sigma^3_{1\dot1}=1$、$\sigma^3_{2\dot2}=-1$，另外两个矩阵元为零，点指标与无点指标在这里分别标记列与行。四个矩阵$I,\sigma_i$线性独立，因此能从矩阵恢复四矢量的每个分量。利用$\operatorname{tr}\sigma_i=0$、$\operatorname{tr}(\sigma_i\sigma_j)=2\delta_{ij}$分别取迹，得到
<span id="eq:c34-vector-inverse"></span>

$$
A^0=-\frac12\operatorname{tr}X,\qquad
A^i=\frac12\operatorname{tr}(\sigma_iX).
\tag{34.24}
$$

这给出了字典的逆。不过，要将它用作两种表示之间的对应，还须使两边的洛伦兹变换相容。两个下旋量指标的变换为$X'=LXR^T=LXL^\dagger$；分别将[（34.8）](#eq:c34-finite-left)中的转动和推动展开到一阶，就有
<span id="eq:c34-sigma-infinitesimal-check"></span>

$$
\begin{aligned}
\delta_R X&=-\frac i2\theta_i[\sigma_i,X]
=(\boldsymbol\theta\times\mathbf A)\cdot\boldsymbol\sigma,\\
\delta_B X&=-\frac12\eta_i\{\sigma_i,X\}
=-(\boldsymbol\eta\cdot\mathbf A)I
 +A^0\boldsymbol\eta\cdot\boldsymbol\sigma.
\end{aligned}
\tag{34.25}
$$

按单位矩阵和泡利矩阵的系数比较，第一式给出$\delta A^0=0$、$\delta\mathbf A=\boldsymbol\theta\times\mathbf A$，即通常的空间转动；第二式给出$\delta A^0=\boldsymbol\eta\cdot\mathbf A$、$\delta A^i=\eta_iA^0$，即所用的正非对角推动。两种指标体系中的生成元作用相同，取指数并相乘后，对整个连通群的作用也相同。上述泡利矩阵乘法已经证明当前字典的相容性；[下一节](/posts/srednicki-35/#c35)将进一步整理$\sigma$矩阵的乘积与缩并恒等式。

由此也能理解为什么把字典中的$\sigma$称为不变符号：分量同时按两种指标体系变换，对应关系保持不变。从表示论看，这正是乘积$(2,1)\otimes(1,2)\otimes(2,2)$含有单态的含义。第三个因子可借助不变度规与其对偶表示相认，因此这个单态对应于将前两个因子的乘积与四矢量相连的映射。

<span id="c34-double-cover"></span>

### 有限变换的双覆盖

矩阵字典不仅联系无穷小生成元，也能说明上一节提到的旋量双值性。先令$A^\mu$为实数，则$X$厄米，其行列式等于四矢量闵氏长度平方的相反数：
<span id="eq:c34-determinant-norm"></span>

$$
\det X=(A^0)^2-\mathbf A^2=-g_{\mu\nu}A^\mu A^\nu.
\tag{34.26}
$$

任意$L\in SL(2,\mathbb C)$将$X$变为$LXL^\dagger$后，矩阵仍厄米且行列式不变，所以它诱导了保持洛伦兹度规的实线性变换。为确定这些变换所在的连通分支，对矩阵作极分解$L=PV$，其中$P$正定厄米、$V$幺正；行列式为1又给出$P=e^{\mathbf h\cdot\boldsymbol\sigma}$、$V\in SU(2)$。整个矩阵空间由$\mathbb R^3\times S^3$参数化，是连通、单连通的，诱导的洛伦兹变换便始终位于恒等元所在的固有正时分支。

这个构造也包含了所有固有正时变换。任意这样的$\Lambda$将$(1,0,0,0)$变成未来单位类时矢量；选一次推动将原时间轴送到这个矢量，再用该推动的逆作用于$\Lambda$，剩下的变换保持时间轴，因而只能是空间SO(3)转动。式[（34.8）](#eq:c34-finite-left)已经给出任意方向的推动和转动，所以每个固有正时变换都能由某个$L$实现。

最后确定哪些旋量矩阵会给出相同的四矢量变换。若$LXL^\dagger=X$对每个厄米$X$都成立，先令$X=I$，可知$L$幺正；再令$X=\sigma_i$，可知$L$与三个泡利矩阵都对易。与$\sigma_3$对易要求矩阵为对角形，与$\sigma_1$对易又要求两个对角元相等，因此$L=cI$。再用$\det L=1$，只剩$c=\pm1$。故每个$\Lambda$恰有$L$和$-L$两个原像；前面的记号$L(\Lambda)$包含对原像的选择，连续变换的群复合须在同一覆盖群中进行。转动$2\pi$恰好从$I$走到$-I$，第33节得到的$(-1)^{2(n+n')}$就是这个核在任意不可约块上的作用；它等于1时，表示才能下降到原洛伦兹群。

<span id="c34-invariants"></span>

## 不变张量与二阶张量的完全分解

若若干表示的乘积含有单态，沿这个不变方向的固定分量就给出一个不变张量。前面的$\epsilon$代表反对称单态，$\sigma$则联系两种指标体系。用这些工具考察两个四矢量的乘积，可以先分别合成它们的无点指标和点指标，得到
<span id="eq:c34-vector-square"></span>

$$
\begin{aligned}
(2,2)\otimes(2,2)
&=(1\oplus3,\,1\oplus3)\\
&=(1,1)_{\rm S}\oplus(1,3)_{\rm A}
 \oplus(3,1)_{\rm A}\oplus(3,3)_{\rm S}.
\end{aligned}
\tag{34.27}
$$

第一行是分别对两个SU(2)因子使用$2\otimes2=1_{\rm A}\oplus3_{\rm S}$。交换两个矢量时，无点指标和点指标会同时交换：两个反对称单态的负号相乘为正，两个对称三重态也给正号，只有一个因子反对称的两项则给负号。因此第二行的S、A分别标记整个矢量交换下的对称性与反对称性。

其中的对称单态由$g^{\mu\nu}$张成。把它同第33节的分解$B^{\mu\nu}=A^{\mu\nu}+S^{\mu\nu}+g^{\mu\nu}T/4$相比，就可认出$T\in(1,1)$、$S\in(3,3)$以及$A\in(3,1)\oplus(1,3)$。对称张量的四个对角元受一个迹条件约束，留下3个独立分量，再加6个非对角分量，共有9个，正与$(3,3)$的维数相符。

要将反对称的六个分量实际拆开，还需要另一个不变符号。四个四矢量的完全反对称乘积只有一个独立分量，在固有洛伦兹变换下构成单态。将相应的Levi-Civita符号（Levi-Civita symbol）归一化为$\epsilon^{0123}=+1$，任意两个指标交换时变号，有重复指标时为零。降下四个指标时恰好遇到一个时间度规负号，所以$\epsilon_{0123}=-1$。它在变换下的性质由行列式的展开给出：
<span id="eq:c34-epsilon-four-invariance"></span>

$$
\Lambda^\mu{}_{\alpha}\Lambda^\nu{}_{\beta}
\Lambda^\rho{}_{\gamma}\Lambda^\sigma{}_{\delta}
\epsilon^{\alpha\beta\gamma\delta}
=(\det\Lambda)\epsilon^{\mu\nu\rho\sigma}.
\tag{34.28}
$$

左边在四个自由指标中完全反对称，只能正比于$\epsilon$。取$(\mu,\nu,\rho,\sigma)=(0,1,2,3)$，求和中的24项恰好组成$\det\Lambda$，于是得到上式的比例系数。固有变换的行列式为1，故$\epsilon$在这些变换下不变。利用它可以定义对偶运算，从反对称张量中取出刚才找到的两个三维部分。

<span id="c34-generator-duality"></span>

## 左右手生成元的对偶性质

左右手生成元已经同时带有旋量指标与一对反对称时空指标，因而适合用来联系对称旋量和反对称张量。先把$S_L^{\mu\nu}$的旋量指标降为两个下指标，再写出两个上指标的形式；依[（34.19）](#eq:c34-raising)逐指标操作，得到
<span id="eq:c34-generator-spinor-indices"></span>

$$
(S_L^{\mu\nu})_{ab}
=\epsilon_{bc}(S_L^{\mu\nu})_a{}^c,\qquad
(S_L^{\mu\nu})^{ab}
=\epsilon^{ac}(S_L^{\mu\nu})_c{}^b.
\tag{34.29}
$$

泡利矩阵无迹，因此$\epsilon^{ab}(S_L^{\mu\nu})_{ab}
=(S_L^{\mu\nu})_a{}^a=0$。这还限制了两个旋量指标的对称性：二维矩阵的反对称部分只能写成$c\epsilon_{ab}$，同$\epsilon^{ab}$缩并给出$-2c$，所以$c=0$，降指标后的矩阵对$a,b$对称。再将两指标同时升起，对称性仍保持；$S_R$同样无迹，因而也得到两个点指标对称的矩阵。

旋量指标的性质确定以后，再考察那一对反对称时空指标。对任意反对称张量，定义对偶运算
<span id="eq:c34-hodge-definition"></span>

$$
(\star A)^{\mu\nu}=\frac12\epsilon^{\mu\nu\rho\sigma}A_{\rho\sigma}.
\tag{34.30}
$$

将左右手生成元代入这一运算，就能区分二者对应的张量部分。先把[（34.6）](#eq:c34-left-rotation-generator)–[（34.7）](#eq:c34-left-boost-generator)中的左手矩阵代入，按含时间指标与纯空间指标两类计算：
<span id="eq:c34-left-duality-check"></span>

$$
\begin{aligned}
(\star S_L)^{i0}
&=-\frac12\epsilon_{ijk}S_L^{jk}=-\frac12\sigma_i=iS_L^{i0},\\
(\star S_L)^{ij}
&=\epsilon^{ijk0}(S_L)_{k0}
=(-\epsilon_{ijk})(-i\sigma_k/2)=iS_L^{ij}.
\end{aligned}
\tag{34.31}
$$

这里空间缩并使用三维欧氏$\epsilon_{ijk}$，而降低时间指标给出$(S_L)_{k0}=-S_L^{k0}$。两类计算包含全部六个独立时空指标对，所以可以合写为协变形式，并同时给出右手结果：
<span id="eq:c34-generator-duality"></span>

$$
S_L^{\mu\nu}=-\frac i2\epsilon^{\mu\nu\rho\sigma}(S_L)_{\rho\sigma},
\qquad
S_R^{\mu\nu}=+\frac i2\epsilon^{\mu\nu\rho\sigma}(S_R)_{\rho\sigma}.
\tag{34.32}
$$

右手式由左手式逐项复共轭，再用$S_R=-S_L^*$得到。特别取一对分量，有$S_L^{10}=+iS_L^{23}$。

<span id="c34-spinor-twoform"></span>

## 对称旋量怎样成为自对偶张量

生成元的两个旋量指标对称，两个时空指标反对称，因而可以将一个对称左手场$G_{ab}$映成反对称张量。定义
<span id="eq:c34-spinor-twoform-map"></span>

$$
G^{\mu\nu}=(S_L^{\mu\nu})^{ab}G_{ab}.
\tag{34.33}
$$

所得张量对$\mu,\nu$反对称，并由[（34.32）](#eq:c34-generator-duality)满足$G=-i\star G$，也就是$\star G=iG$。具有这一性质的复二形式称为自对偶（self-dual）。

为了把这个线性映射认作两种表示之间的对应，还要说明它保持洛伦兹变换。先考察生成元在群共轭下怎样变换。由$L(\Lambda)^{-1}L(1+\omega)L(\Lambda)
=L(\Lambda^{-1}(1+\omega)\Lambda)$比较$\omega_{\mu\nu}$的系数，得到
<span id="eq:c34-generator-adjoint-action"></span>

$$
L^{-1}S_L^{\mu\nu}L
=\Lambda^\mu{}_{\rho}\Lambda^\nu{}_{\sigma}S_L^{\rho\sigma}.
\tag{34.34}
$$

其中$\omega'_{\rho\sigma}=\omega_{\mu\nu}
\Lambda^\mu{}_{\rho}\Lambda^\nu{}_{\sigma}$，两边指标正好如此排列。
升起首指标后，生成元矩阵成为$E^{-1}S_L^{\mu\nu}$，而反对称符号的不变性给出$L^TE^{-1}=E^{-1}L^{-1}$。因此，将$G'_{ab}=L_a{}^cL_b{}^dG_{cd}$代入[（34.33）](#eq:c34-spinor-twoform-map)，两个变换矩阵可移到缩并系数上，成为
<span id="eq:c34-twoform-intertwining"></span>

$$
L^T(E^{-1}S_L^{\mu\nu})L
=E^{-1}(L^{-1}S_L^{\mu\nu}L)
=\Lambda^\mu{}_{\rho}\Lambda^\nu{}_{\sigma}E^{-1}S_L^{\rho\sigma}.
\tag{34.35}
$$

右边恰好是二阶张量所需的两个洛伦兹矩阵，因此映出的$G^{\mu\nu}$按二阶张量变换。

还可将这个对应逐分量反解，以确认三个旋量分量都保留在张量中。令$G_{11}=u$、$G_{12}=G_{21}=v$、$G_{22}=w$，将[（34.15）](#eq:c34-epsilon-matrices)和泡利矩阵代入缩并，三个含时间指标的分量为
<span id="eq:c34-twoform-components"></span>

$$
G^{10}=\frac i2(u-w),\qquad
G^{20}=-\frac12(u+w),\qquad G^{30}=-iv.
\tag{34.36}
$$

其余分量由自对偶条件$G^{i0}=\frac i2\epsilon_{ijk}G^{jk}$确定。三个旋量分量可反解为$u=-iG^{10}-G^{20}$、$w=iG^{10}-G^{20}$、$v=iG^{30}$，所以任意自对偶二形式都唯一对应于一个对称左手旋量。

右手对应可以由同一映射的共轭得到。对[（34.33）](#eq:c34-spinor-twoform-map)取厄米共轭时，由于升指标所用的$\epsilon^{ab}$为实数，升指标与共轭可以按任意次序进行。于是得到
<span id="eq:c34-conjugate-twoform"></span>

$$
G^{\dagger\mu\nu}
=-(S_R^{\mu\nu})^{\dot a\dot b}G^\dagger_{\dot a\dot b},\qquad
G^\dagger=+i\star G^\dagger,\quad
\star G^\dagger=-iG^\dagger.
\tag{34.37}
$$

映射系数前的负号来自$S_R=-S_L^*$，对偶关系中的$i$则因共轭而变号。这个三维空间属于$(1,3)$表示，称为反自对偶（anti-self-dual）部分。

<span id="c34-projectors"></span>

## 两个投影与六分量的重建

现在可以反过来，从任意反对称$A^{\mu\nu}$出发，求出它的自对偶与反自对偶部分。为构造相应投影，先计算连续作两次对偶的作用$\star^2$。这里需要两个四维反对称符号的缩并。

先只缩并一个指标。若$(\mu,\nu,\rho)$或$(\alpha,\beta,\gamma)$有重复指标，乘积为零；若两组三指标不是同一个集合，也找不到一个$\sigma$同时补齐两个反对称符号。只有两组是同一集合的不同排列时，唯一的剩余$\sigma$才贡献一项，其符号为两种排列的相对符号乘$-1$，其中负号由$\epsilon^{0123}\epsilon_{0123}=-1$确定。因此结果是负的三阶克罗内克行列式：

<span id="eq:c34-one-epsilon-contraction"></span>

$$
\begin{aligned}
\epsilon^{\mu\nu\rho\sigma}\epsilon_{\alpha\beta\gamma\sigma}
={}&-\delta^\mu{}_{\alpha}\delta^\nu{}_{\beta}\delta^\rho{}_{\gamma}
-\delta^\mu{}_{\beta}\delta^\nu{}_{\gamma}\delta^\rho{}_{\alpha}
-\delta^\mu{}_{\gamma}\delta^\nu{}_{\alpha}\delta^\rho{}_{\beta}\\
&+\delta^\mu{}_{\beta}\delta^\nu{}_{\alpha}\delta^\rho{}_{\gamma}
+\delta^\mu{}_{\alpha}\delta^\nu{}_{\gamma}\delta^\rho{}_{\beta}
+\delta^\mu{}_{\gamma}\delta^\nu{}_{\beta}\delta^\rho{}_{\alpha}.
\end{aligned}
$$

令$\gamma=\rho$并求和，第一、第四项各带因子$\delta^\rho{}_{\rho}=4$，其余四项各消去一个求和指标。两种自由指标排列的系数分别合成$-4+1+1=-2$和$4-1-1=2$，得到
<span id="eq:c34-two-epsilon-contraction"></span>

$$
\epsilon^{\mu\nu\rho\sigma}\epsilon_{\alpha\beta\rho\sigma}
=-2(\delta^\mu{}_{\alpha}\delta^\nu{}_{\beta}
    -\delta^\mu{}_{\beta}\delta^\nu{}_{\alpha}).
\tag{34.38}
$$

再令$\beta=\nu$并求和，还可得到$\epsilon^{\mu\nu\rho\sigma}\epsilon_{\alpha\nu\rho\sigma}=-2(4-1)\delta^\mu{}_{\alpha}=-6\delta^\mu{}_{\alpha}$。两个、三个缩并指标的系数绝对值分别是$2!$、$3!$，对应补齐剩余指标的排列数。将二指标缩并式用于连续两次对偶，再利用原张量的反对称性，得到
<span id="eq:c34-hodge-square"></span>

$$
\begin{aligned}
(\star^2 A)^{\mu\nu}
&=\frac14\epsilon^{\mu\nu\rho\sigma}
\epsilon_{\rho\sigma\alpha\beta}A^{\alpha\beta}\\
&=-\frac12(A^{\mu\nu}-A^{\nu\mu})=-A^{\mu\nu}.
\end{aligned}
\tag{34.39}
$$

因此在复数域中，对偶算符的本征值为$+i,-i$。将任意二形式分别投影到这两个本征空间，可以使用
<span id="eq:c34-duality-projectors"></span>

$$
P_+=\frac12(I-i\star),\qquad P_-=\frac12(I+i\star),\qquad
P_\pm^2=P_\pm,\quad P_+P_-=0,\quad P_++P_-=I.
\tag{34.40}
$$

这些确为互补投影。例如$(I-i\star)^2=I-2i\star-\star^2=2(I-i\star)$给出幂等性，$(I-i\star)(I+i\star)=I+\star^2=0$则给出两投影的乘积为零。又因为$\star$只由洛伦兹不变的$g$和$\epsilon$组成，它同固有洛伦兹变换可交换，所以两个投影的像空间分别保持不变。

进一步令$A$厄米。此时$\star$的系数为实数，投影所得的两部分互为厄米共轭，分解便可写为
<span id="eq:c34-hermitian-decomposition"></span>

$$
\begin{aligned}
G^{\mu\nu}=(P_+A)^{\mu\nu}
&=\frac12A^{\mu\nu}-\frac i4\epsilon^{\mu\nu\rho\sigma}A_{\rho\sigma},\\
G^{\dagger\mu\nu}=(P_-A)^{\mu\nu}
&=\frac12A^{\mu\nu}+\frac i4\epsilon^{\mu\nu\rho\sigma}A_{\rho\sigma},\\
A^{\mu\nu}&=G^{\mu\nu}+G^{\dagger\mu\nu}.
\end{aligned}
\tag{34.41}
$$

对于一般复$A$，两个投影仍然适用，但两部分不必互为厄米共轭；上述共轭关系使用了原张量的厄米性。

用三维分量写出这一分解，还能直接看到两种手征部分在推动下的区别。暂记$E_i=A^{i0}$、$B_i=\epsilon_{ijk}A^{jk}/2$，对偶及两个投影就成为
<span id="eq:c34-three-vector-duality"></span>

$$
\star:(\mathbf E,\mathbf B)\longmapsto(-\mathbf B,\mathbf E),\qquad
G^{i0}=\frac12(E_i+iB_i),\qquad
G^{\dagger i0}=\frac12(E_i-iB_i).
\tag{34.42}
$$

一阶推动作用于原反对称张量，给出$\delta A^{i0}=\eta_jA^{ij}$和$\delta A^{jk}=-\eta_jE_k+\eta_kE_j$。分别代入这两组三维分量的定义，得到
<span id="eq:c34-three-vector-boost"></span>

$$
\delta\mathbf E=\boldsymbol\eta\times\mathbf B,\qquad
\delta\mathbf B=-\boldsymbol\eta\times\mathbf E,\qquad
\delta(\mathbf E\pm i\mathbf B)
=\mp i\boldsymbol\eta\times(\mathbf E\pm i\mathbf B).
\tag{34.43}
$$

两组三分量在转动下都是自旋1，推动却分别对应$K_i=+iJ_i$和$K_i=-iJ_i$，因此它们正是$(3,1)$与$(1,3)$表示。对原来的六个实分量，这种写法给出三个复分量及其共轭；在复数域上，两种手征部分各自不可约。

<span id="c34-symmetric-spinors"></span>

## 用对称旋量表示任意自旋

二指标对称旋量的构造可以推广。考虑带$N$个无点指标和$M$个点指标的场，并要求无点指标之间完全对称、点指标之间也完全对称。先看无点部分：每个指标有两个取值，完全对称性使一个分量只由其中取值为2的指标数$r$决定。$r=0,1,\ldots,N$，所以共有$N+1$个独立分量。

在自旋$1/2$的通常基底中，将含$r$个低权因子的不同张量积相加并归一化，记为$|r\rangle$。总角动量是每个因子角动量之和。每个高权因子贡献$+1/2$，每个低权因子贡献$-1/2$，故

<span id="eq:c34-symmetric-ladder"></span>

$$
J_3|r\rangle=\left(\frac N2-r\right)|r\rangle,
\qquad
J_-|r\rangle=\sqrt{(r+1)(N-r)}\,|r+1\rangle.
$$

第二式也可直接数出：每个含$r$个低权因子的乘积有$N-r$个可降的因子；降后每种$r+1$个低权因子的乘积被数到$r+1$次。结合两侧归一化因子$\binom Nr^{-1/2}$和$\binom N{r+1}^{-1/2}$，系数成为$(r+1)\sqrt{\binom N{r+1}/\binom Nr}=\sqrt{(r+1)(N-r)}$。这一条从最高权$N/2$出发的降链占满全部$N+1$维空间，因而就是不可约的自旋$N/2$表示。

点指标部分先按[（34.22）](#eq:c34-right-raised)换到通常的自旋基底，再作同样的计算，得到另一个因子上的自旋$M/2$。由[第 33 节的张量积不可约性](/posts/srednicki-33/#c33)可知，分别完全对称的旋量对应

<span id="eq:c34-symmetric-representation"></span>

$$
(2n+1,2n'+1)=(N+1,M+1),\qquad
n=\frac N2,\quad n'=\frac M2,
\qquad \dim=(N+1)(M+1).
$$

$N=M=1$给出四矢量，$(N,M)=(2,0)$和$(0,2)$给出刚才的两种三维二形式。取$N=0$或$M=0$时，相应角动量因子为单态。

---

[← 第 33 节](/posts/srednicki-33/) · [章节地图](/srednicki/) · [第 35 节 →](/posts/srednicki-35/)
