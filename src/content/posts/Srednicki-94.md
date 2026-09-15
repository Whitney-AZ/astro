---
title: 'Srednicki §94 夸克与 θ 真空'
date: 2026-09-14
category: 笔记
tags: [物理, 量子场论, Srednicki]
series: 'Srednicki QFT'
srednickiSections: [94]
hideFromHome: true
draft: false
---

<span id="c94"></span>

上一节说明，纯杨–米尔斯理论的不同拓扑扇区带有相对相位$e^{in\theta}$，真空能量因而可以依赖$\theta$。加入夸克后，轴旋转能够改变$\theta$项的系数。无质量夸克没有质量相位与之比较，$\theta$便可以消去；夸克有质量时，留下的是质量相位与真空角的差。这个相对相位进入低能π介子–核子作用，并产生中子的电偶极矩。

Minkowski度规取$(-+++)$，色生成元的基本表示迹为$\operatorname{Tr}_c(t^at^b)=\delta^{ab}/2$，$\epsilon^{0123}=+1$。所需的[四个核子质量项](/posts/srednicki-83/#eq:c83-mass-original-action)已在第83节求出；下面保留它们的矩阵次序，展开非零真空角带来的新项。

<span id="c94-axial"></span>

## 轴变换怎样改变真空角

先考虑一个处在$SU(3)$基本表示的无质量狄拉克夸克。把上一节的矩阵迹化成颜色分量，得
<span id="eq:c94-massless-functional"></span>

$$
\begin{aligned}
Z(\theta)&=\int\mathcal DA\,\mathcal D\Psi\,\mathcal D\bar\Psi\,
           e^{i\int d^4x\,\mathcal L},\\
\mathcal L&=i\bar\Psi\slashed D\Psi-\frac14F^{a\mu\nu}F^a_{\mu\nu}
 -\frac{g^2\theta}{32\pi^2}\widetilde F^{a\mu\nu}F^a_{\mu\nu}.
\end{aligned}
\tag{94.1}
$$

这里暂不加费米外源，规范固定沿前章处理。经典作用量除矢量$U(1)_V$外，还有轴$U(1)_A$：前者给$\Psi$和$\bar\Psi$相反的相位，后者给它们同向的$\gamma_5$旋转。将轴变换写成变量代换，
<span id="eq:c94-axial-change"></span>

$$
\Psi_{\rm old}=e^{-i\alpha\gamma_5}\Psi,\qquad
\bar\Psi_{\rm old}=\bar\Psi e^{-i\alpha\gamma_5}.
\tag{94.2}
$$

第二式也可由第一式取伴随得到：$\gamma^0$与$\gamma_5$反对易，将指数移过$\gamma^0$后，相位再次变号。由于
$e^{-i\alpha\gamma_5}\gamma^\mu=\gamma^\mu e^{i\alpha\gamma_5}$，
常数$\alpha$使两个指数在动能中相消。

量子测度却不保持不变。[第77节的热核计算](/posts/srednicki-77/#c77-ward)已经给出两个Berezin测度的雅可比。本节只需代入基本表示的半迹：
<span id="eq:c94-jacobian"></span>

$$
\begin{aligned}
\mathcal D\Psi_{\rm old}\mathcal D\bar\Psi_{\rm old}
 &=\mathcal J_\alpha[A]\,\mathcal D\Psi\mathcal D\bar\Psi,\\
\mathcal J_\alpha[A]
 &=\exp\left[-i\frac{g^2\alpha}{16\pi^2}
              \int d^4x\,\widetilde F^{a\mu\nu}F^a_{\mu\nu}\right].
\end{aligned}
\tag{94.3}
$$

在式[（77.20）](/posts/srednicki-77/#eq:c77-regulated-jacobian)的表示迹中，半迹的$1/2$与$\epsilon FF=2\widetilde FF$的2相消，便得到上式的系数。将这个指数与式[（94.1）](#eq:c94-massless-functional)相乘，拓扑项中的$\theta$变成
<span id="eq:c94-theta-shift"></span>

$$
\theta'=\theta+2\alpha,\qquad Z(\theta)=Z(\theta+2\alpha).
\tag{94.4}
$$

$\alpha$可以任取，故无源真空泛函与$\theta$无关。比较带夸克插入的关联函数时，插入算符的相位也随变量改变；这正是第77节沃德恒等式中接触项的来源。对于这里的真空能量，没有这样的插入，结论便可直接使用。

<span id="c94-zero-modes"></span>

### 固定拓扑背景中的零模

夸克作用量是二次型，格拉斯曼积分给出行列式。沿上一节的Euclid扇区记法，
<span id="eq:c94-determinant-sectors"></span>

$$
Z(\theta)=\sum_{n\in\mathbb Z}e^{in\theta}
  \int_{\mathcal A_n}\mathcal DA\,e^{-S_{\rm YM}[A]}Z_f[A],
\qquad Z_f[A]=\det\mathscr D_E[A].
\tag{94.5}
$$

$\mathscr D_E$为延拓后的无质量狄拉克二次型，不依赖$\theta$的整体归一已吸收在测度中。若每个非零$n$背景的行列式都为零，便能直接解释刚才的$\theta$独立性。为判断这一点，在固定$A$的积分中作同一次轴代换。Euclid雅可比为$e^{2i\alpha n}$，而经典费米作用量不变，故
<span id="eq:c94-fixed-background-ward"></span>

$$
Z_f[A]=e^{2i\alpha n}Z_f[A].
\tag{94.6}
$$

当$n\ne0$时，总可以选一个使相位不等于1的$\alpha$，于是$Z_f[A]=0$。这里始终使用未归一化积分，没有除以这个正要判断是否为零的行列式。仅仅知道规范场积分后的$Z(\theta)$为常数，只能推出非零Fourier系数的总和为零；固定背景的变量代换才给出逐个背景的结论。

还可以从狄拉克谱看见这个零。沿第77节取
<span id="eq:c94-euclidean-spectrum"></span>

$$
\begin{gathered}
\Gamma^4=\gamma^0,\qquad \Gamma^i=-i\gamma^i,\qquad
\Gamma_5=\Gamma^4\Gamma^1\Gamma^2\Gamma^3=\gamma_5,\\
H_E=i\Gamma^aD_{Ea}=H_E^\dagger,\qquad
\{H_E,\Gamma_5\}=0.
\end{gathered}
\tag{94.7}
$$

先在紧致的平直Euclid空间中定义谱，例如四维环面上的光滑规范丛；非平凡丛的连接用相容的局部规范势拼接。这样没有物理边界项，谱离散，热核有定义。在非紧空间使用同一论证时，须取相应的衰减和谱边界条件。若$H_E\phi_\lambda=\lambda\phi_\lambda$，则
<span id="eq:c94-nonzero-chirality"></span>

$$
2\lambda\langle\phi_\lambda,\Gamma_5\phi_\lambda\rangle
 =\langle\phi_\lambda,\{H_E,\Gamma_5\}\phi_\lambda\rangle=0.
\tag{94.8}
$$

所以每一个非零本征态在带$\Gamma_5$的迹中贡献为零。零模子空间在$\Gamma_5$下封闭，可选手征本征基；记其正、负手征维数为$N_+,N_-$。由此
<span id="eq:c94-index"></span>

$$
\begin{aligned}
\operatorname{Tr}\left(\Gamma_5e^{-H_E^2/\mathcal M^2}\right)
 &=N_+-N_-,\\
N_+-N_-
 &=\frac{g^2}{16\pi^2}\int_Ed^4x\,
           \operatorname{Tr}_c(\widetilde F_E^{\mu\nu}F^E_{\mu\nu})
 =n.
\end{aligned}
\tag{94.9}
$$

第二行使用式[（77.19）](/posts/srednicki-77/#eq:c77-euclidean-crosscheck)的热核系数，所需的取向转换尤其重要：第77节用$\epsilon_{77}^{4123}=+1$，第93节则用$\epsilon_{93}^{1234}=+1$，故$\epsilon_{77}=-\epsilon_{93}$。该热核式前面的负号因此变成正号，再由$\epsilon FF=2\widetilde FF$得到本式。谱迹中的高能调节$\mathcal M$不改变第一行；它只是让局域系数的求值有意义。

当$n\ne0$时，至少有$|n|$个零模。沿其中一个零模展开的格拉斯曼系数没有二次作用量，因而包含$\int dc\,1=0$，这就使无质量、无插入的高斯积分消失。若关联函数插入了足够的费米场，积分可以改为$\int dc\,c=1$，零模便能被饱和。因此瞬子扇区仍能出现在含费米子的关联函数中；消失的是此处的无源行列式贡献。

<span id="c94-mass-phase"></span>

## 有质量夸克留下什么相位

现在加入质量，把一个狄拉克场写成两个左手场，
<span id="eq:c94-weyl-mass"></span>

$$
\Psi=\begin{pmatrix}\chi\\ \xi^\dagger\end{pmatrix},\qquad
\mathcal L_m=-m\chi\xi-m^*\xi^\dagger\chi^\dagger,
\qquad m=|m|e^{i\phi}.
\tag{94.10}
$$

其中$\chi$属色$\mathbf3$，$\xi$属$\bar{\mathbf3}$，所以$\chi\xi$是颜色单态。利用$\bar\Psi P_L\Psi=\chi\xi$及其共轭，
<span id="eq:c94-dirac-mass-phase"></span>

$$
\begin{aligned}
mP_L+m^*P_R
 &=|m|\left(e^{i\phi}P_L+e^{-i\phi}P_R\right)
 =|m|e^{-i\phi\gamma_5},\\
\mathcal L_m&=-|m|\bar\Psi e^{-i\phi\gamma_5}\Psi.
\end{aligned}
\tag{94.11}
$$

轴代换使$\chi_{\rm old}=e^{i\alpha}\chi$、$\xi_{\rm old}=e^{i\alpha}\xi$，故质量双线性多出$e^{2i\alpha}$。与测度的变化合起来，
<span id="eq:c94-one-flavor-invariant"></span>

$$
m'=me^{2i\alpha},\qquad \theta'=\theta+2\alpha,\qquad
m'e^{-i\theta'}=me^{-i\theta}.
\tag{94.12}
$$

选$\alpha=-\phi/2$可把质量取为正实数，拓扑项却留下$\theta-\phi$。选另一个$\alpha$把$\theta$消掉，质量便带上同一个相对相位。两者不能同时消去，除非这个差本来就是零，模$2\pi$理解。

对$N_f$个味，写$\mathcal L_m=-M_{ij}\chi_i\xi_j+\mathrm{h.c.}$。共同轴旋转作用在每一个质量矩阵元上，而测度的对数要对全部味求和，因此
<span id="eq:c94-multiflavor-invariant"></span>

$$
\begin{gathered}
M'=e^{2i\alpha}M,\qquad \theta'=\theta+2N_f\alpha,\\
\det M'=e^{2iN_f\alpha}\det M,\qquad
(\det M')e^{-i\theta'}=(\det M)e^{-i\theta},\\
\bar\theta\equiv\theta-\arg\det M .
\end{gathered}
\tag{94.13}
$$

质量项与拓扑项的号固定后，$\bar\theta$的这一定义也随之确定。质量矩阵的正奇异值仍是独立参数，总轴相位则与$\theta$合并。若有一个严格无质量味，$\arg\det M$本身无定义，应回到式[（94.4）](#eq:c94-theta-shift)，只旋转那个无质量味即可消去$\theta$。

谱结构也能核对这个相位。对非零$\lambda$，选$\{\phi_\lambda,\Gamma_5\phi_\lambda\}$为二阶子空间；其中$H_E=\lambda\sigma_3$、$\Gamma_5=\sigma_1$。略去不依赖$\phi$的常量归一，质量二次型可取
<span id="eq:c94-mass-paired-block"></span>

$$
\mathscr D_\lambda=
\begin{pmatrix}
|m|\cos\phi+i\lambda&-i|m|\sin\phi\\
-i|m|\sin\phi&|m|\cos\phi-i\lambda
\end{pmatrix},
\qquad \det\mathscr D_\lambda=\lambda^2+|m|^2.
\tag{94.14}
$$

行列式的交叉项相消，两个$\sin^2\phi$、$\cos^2\phi$项合成$|m|^2$。正、负手征零模则分别给$|m|e^{-i\phi}$、$|m|e^{i\phi}$，所以总质量相位为
<span id="eq:c94-zero-mode-mass-phase"></span>

$$
e^{-i\phi(N_+-N_-)}=e^{-in\phi},\qquad
e^{in\theta}e^{-in\phi}=e^{in(\theta-\phi)}.
\tag{94.15}
$$

这与变量代换得到的结果一致，也说明为什么质量一旦非零，原先被零模消去的真空扇区又能有贡献。

<span id="c94-alignment"></span>

## 两味低能理论的真空取向

为了计算强子效应，以下从实正的$m_u,m_d$与一个真空角$\theta$出发。对两味共同取$\alpha=-\theta/4$，显式拓扑项便消失，全部相位移入
<span id="eq:c94-two-flavor-matrix"></span>

$$
M=M_0e^{-i\theta/2},\qquad
M_0=\operatorname{diag}(m_u,m_d),\qquad m_u,m_d>0.
\tag{94.16}
$$

因此这里的$\theta$就是质量已取实基中的物理强相位。第83节给出的最低阶有效拉格朗日量现在写成
<span id="eq:c94-effective-lagrangian"></span>

$$
\begin{aligned}
\mathcal L_{\rm eff}
={}&-\frac{f_\pi^2}{4}\operatorname{Tr}(\partial^\mu U^\dagger\partial_\mu U)
    +v^3\operatorname{Tr}(MU+M^\dagger U^\dagger)\\
 &+i\bar N\slashed\partial N
    -m_N\bar N(U^\dagger P_L+UP_R)N\\
 &-\frac{i}{2}(g_A-1)\bar N\gamma^\mu
       (U\partial_\mu U^\dagger P_L+U^\dagger\partial_\mu UP_R)N
    +\delta\mathcal L_M .
\end{aligned}
\tag{94.17}
$$

其中 $P_{L,R}=(1\mp\gamma_5)/2$。把质量矩阵视为按手征变换规律变化的外参数，在无导数、只含一次 $M$ 或 $M^\dagger$ 的阶数，核子质量修正可写成四项：

$$
\begin{aligned}
\delta\mathcal L_M={}&-c_1\bar N(MP_L+M^\dagger P_R)N\\
&-c_2\bar N(U^\dagger M^\dagger U^\dagger P_L+UMUP_R)N\\
&-c_3\operatorname{Tr}(MU+M^\dagger U^\dagger)
\bar N(U^\dagger P_L+UP_R)N\\
&-c_4\operatorname{Tr}(MU-M^\dagger U^\dagger)
\bar N(U^\dagger P_L-UP_R)N.
\end{aligned}
$$

前两项直接将质量矩阵插入核子双线性，后两项先对味指标取迹，再乘核子双线性。取实系数 $c_i$ 时，各项均厄米；最后一行的两个因子各在厄米共轭下变号，因此它们的乘积也厄米。由 $[M]=1$ 和 $[\bar NN]=3$ 可知 $c_i$ 无量纲。下面代入式[（94.16）](#eq:c94-two-flavor-matrix)，并在计算 CP 奇量时保留 $\theta$ 的一次项。

展开点由真空能量的极小值确定。均匀纯介子构型的能量密度为
<span id="eq:c94-meson-potential"></span>

$$
V(U)=-v^3\operatorname{Tr}(MU+M^\dagger U^\dagger)
     =-2v^3\operatorname{Re}\operatorname{Tr}(MU).
\tag{94.18}
$$

设$t=\theta/2$、$s=m_u+m_d$、$d=m_u-m_d$。利用SU(2)矩阵的实参数形式，写$U=a_0I+ia_j\sigma^j$、$a_0^2+\boldsymbol a^2=1$，则
<span id="eq:c94-linear-vacuum-functional"></span>

$$
\operatorname{Re}\operatorname{Tr}(MU)
 =s\cos t\,a_0+d\sin t\,a_3.
\tag{94.19}
$$

右边是四维单位球面上的线性泛函。由Cauchy–Schwarz不等式，它的最大值是系数向量的长度$R$，在两向量同向时达到。因此，在$R>0$时，
<span id="eq:c94-vacuum-minimum"></span>

$$
\begin{gathered}
R(\theta)=\sqrt{m_u^2+m_d^2+2m_um_d\cos\theta},\\
a_0=\frac{s\cos t}{R},\qquad a_3=\frac{d\sin t}{R},\qquad
a_1=a_2=0,\\
U_0=\operatorname{diag}(e^{i\varphi},e^{-i\varphi}),\qquad
V_{\min}(\theta)=-2v^3R(\theta).
\end{gathered}
\tag{94.20}
$$

这个解给出对角的真空矩阵，并选定极小值的分支。代入$U_0$，势成为
<span id="eq:c94-alignment-angle"></span>

$$
\begin{aligned}
V(U_0)&=-2v^3\left[
 m_u\cos(\varphi-\theta/2)+m_d\cos(\varphi+\theta/2)\right],\\
0=\frac1{2v^3}\frac{\partial V}{\partial\varphi}
 &=s\cos t\sin\varphi-d\sin t\cos\varphi,\\
\tan\varphi&=\frac{d}{s}\tan t .
\end{aligned}
\tag{94.21}
$$

最后一行的反正切须结合上一式的$a_0,a_3$取值使用。只写$\tan\varphi$会同时包含极大分支。当$m_u=m_d$且$\theta=\pi$时，$R=0$，这一阶势退化，不能沿用唯一$U_0$的公式。以下研究$\theta=0$附近，不遇到这个退化点。

小$\theta$展开给$\varphi=d\theta/(2s)+O(\theta^3)$。两个对角元分别为
<span id="eq:c94-aligned-diagonal-expansion"></span>

$$
\begin{aligned}
(MU_0)_{11}
 &=m_u\left[1+i\left(\frac{d}{2s}-\frac12\right)\theta\right]
       +O(\theta^2)
 =m_u-i\theta\frac{m_um_d}{s}+O(\theta^2),\\
(MU_0)_{22}
 &=m_d\left[1-i\left(\frac{d}{2s}+\frac12\right)\theta\right]
       +O(\theta^2)
 =m_d-i\theta\frac{m_um_d}{s}+O(\theta^2).
\end{aligned}
\tag{94.22}
$$

两味不同的实质量留下完全相同的虚部。定义约化质量（reduced mass）
<span id="eq:c94-reduced-mass"></span>

$$
\widetilde m=\frac{m_um_d}{m_u+m_d},\qquad
Q\equiv MU_0=M_0-i\theta\widetilde m I+O(\theta^2).
\tag{94.23}
$$

任一味质量趋零时，$\widetilde m$也趋零，预示所有这里的一次强CP作用都将消失。真空能量本身是$\theta$的偶函数，需展开到二次才能看到其曲率：
<span id="eq:c94-topological-susceptibility"></span>

$$
V_{\min}(\theta)
 =-2v^3s+v^3\widetilde m\,\theta^2+O(\theta^4),
\qquad
\chi_{\rm top}\equiv V_{\min}''(0)=2v^3\widetilde m.
\tag{94.24}
$$

这个曲率称拓扑磁化率（topological susceptibility）。它稍后直接决定轴子的质量。

<span id="c94-nucleons"></span>

## 围绕新真空重写核子作用量

将$\pi^a=0$放在$U_0$处，取
<span id="eq:c94-ordered-fields"></span>

$$
\begin{gathered}
u_0^2=U_0,\qquad
u=e^{i\pi^aT^a/f_\pi},\qquad
\widetilde U=u^2,\qquad U=u_0\widetilde Uu_0,\\
N=B\mathcal N,\qquad B=u_0uP_L+u_0^\dagger u^\dagger P_R,\\
\bar N=\bar{\mathcal N}\bar B,\qquad
\bar B=\gamma^0B^\dagger\gamma^0
       =uu_0P_L+u^\dagger u_0^\dagger P_R.
\end{gathered}
\tag{94.25}
$$

$u_0$为常量，但一般不与$u(x)$对易，所以伴随场中的次序不能省略。这种对称放置把常真空因子和局部涨落分开，在质量项中尤其方便：
<span id="eq:c94-mass-block-cancellation"></span>

$$
(uu_0)U^\dagger(u_0u)
 =uu_0(u_0^\dagger u^{\dagger2}u_0^\dagger)u_0u=I,
\qquad
(u^\dagger u_0^\dagger)U(u_0^\dagger u^\dagger)=I .
\tag{94.26}
$$

因此$m_N$项成为$-m_N\bar{\mathcal N}\mathcal N$。介子动能的常量$u_0$同样在迹中相消；核子动能只对$u(x)$求导，给第83节已算出的复合场
<span id="eq:c94-composite-connections"></span>

$$
v_\mu=\frac i2\left[u^\dagger\partial_\mu u+u\partial_\mu u^\dagger\right],
\qquad
a_\mu=\frac i2\left[u^\dagger\partial_\mu u-u\partial_\mu u^\dagger\right].
\tag{94.27}
$$

消去常量因子后，动能与额外$g_A-1$项的相加逐项沿用[第83节的场重定义计算](/posts/srednicki-83/#c83-redefinition)。

剩下的一次质量项要保留矩阵次序。因为$M,u_0$同为对角矩阵，$u_0Mu_0=MU_0=Q$。令$C=uQu$，则$c_1$结构的左右手块为$(C,C^\dagger)$，$c_2$结构为$(C^\dagger,C)$。代入$P_{L,R}=(1\mp\gamma_5)/2$便得
<span id="eq:c94-two-mass-blocks"></span>

$$
\begin{aligned}
-c_1(CP_L+C^\dagger P_R)-c_2(C^\dagger P_L+CP_R)
 &=-\frac{c_+}{2}(C+C^\dagger)
   +\frac{c_-}{2}(C-C^\dagger)\gamma_5,\\
c_\pm&=c_1\pm c_2.
\end{aligned}
\tag{94.28}
$$

两个迹结构中的核子矩阵分别化成$I$及$P_L-P_R=-\gamma_5$，所以原来的$-c_4$变成$+c_4$。结合所有项，得到
<span id="eq:c94-aligned-lagrangian"></span>

$$
\begin{aligned}
\mathcal L_{\rm eff}={}&
 -\frac{f_\pi^2}{4}\operatorname{Tr}(\partial^\mu\widetilde U^\dagger
                                           \partial_\mu\widetilde U)
 +v^3\operatorname{Tr}(Q\widetilde U+Q^\dagger\widetilde U^\dagger)\\
 &+i\bar{\mathcal N}\slashed\partial\mathcal N-m_N\bar{\mathcal N}\mathcal N
  +\bar{\mathcal N}\gamma^\mu v_\mu\mathcal N
  -g_A\bar{\mathcal N}\gamma^\mu a_\mu\gamma_5\mathcal N\\
 &-\frac{c_+}{2}\bar{\mathcal N}(C+C^\dagger)\mathcal N
  +\frac{c_-}{2}\bar{\mathcal N}(C-C^\dagger)\gamma_5\mathcal N\\
 &-c_3\operatorname{Tr}(Q\widetilde U+Q^\dagger\widetilde U^\dagger)
                                      \bar{\mathcal N}\mathcal N\\
 &+c_4\operatorname{Tr}(Q\widetilde U-Q^\dagger\widetilde U^\dagger)
                                      \bar{\mathcal N}\gamma_5\mathcal N .
\end{aligned}
\tag{94.29}
$$

每一个$Q$都来自同一个质量矩阵替换。于是提取一次$\theta$项只需在$Q$中取$-i\theta\widetilde m I$，在$Q^\dagger$中取相反号：
<span id="eq:c94-cp-blocks"></span>

$$
\begin{aligned}
\delta_\theta(C+C^\dagger)
 &=-i\theta\widetilde m(\widetilde U-\widetilde U^\dagger),\\
\delta_\theta(C-C^\dagger)
 &=-i\theta\widetilde m(\widetilde U+\widetilde U^\dagger).
\end{aligned}
\tag{94.30}
$$

SU(2)矩阵的两个本征值互为共轭，故其迹为实数，
$\operatorname{Tr}(\widetilde U-\widetilde U^\dagger)=0$。这使纯介子质量项和$c_3$项的一次$\theta$贡献消失。余下
<span id="eq:c94-cp-lagrangian"></span>

$$
\begin{aligned}
\mathcal L_\theta=-i\theta\widetilde m\Big[
 &-\frac{c_+}{2}\bar{\mathcal N}
                         (\widetilde U-\widetilde U^\dagger)\mathcal N\\
 &+\frac{c_-}{2}\bar{\mathcal N}
                         (\widetilde U+\widetilde U^\dagger)\gamma_5\mathcal N\\
 &+c_4\operatorname{Tr}(\widetilde U+\widetilde U^\dagger)
                                  \bar{\mathcal N}\gamma_5\mathcal N\Big].
\end{aligned}
\tag{94.31}
$$

用$\widetilde U=e^{i\pi^a\sigma^a/f_\pi}$展开，差为$2i\pi^a\sigma^a/f_\pi+O(\pi^3)$，和为$2I+O(\pi^2)$，和的迹为$4+O(\pi^2)$。因此
<span id="eq:c94-cp-pion-coupling"></span>

$$
\begin{gathered}
\mathcal L_\theta=-i\Delta\,\bar{\mathcal N}\gamma_5\mathcal N
       -\bar g\,\pi^a\bar{\mathcal N}\sigma^a\mathcal N+\cdots,\\
\Delta=\theta\widetilde m(c_-+4c_4),\qquad
\bar g=\frac{\theta c_+\widetilde m}{f_\pi}.
\end{gathered}
\tag{94.32}
$$

这里$[\Delta]=1$，$[\bar g]=0$。第一项只是核子质量的一次赝标量相位，可以用常量场重定义移走。具体地，取
<span id="eq:c94-nucleon-phase-removal"></span>

$$
\begin{aligned}
\mathcal N_{\rm old}&=e^{-i\alpha_N\gamma_5}\mathcal N,
& \alpha_N&=\frac{\Delta}{2m_N},\\
-m_N\bar{\mathcal N}_{\rm old}\mathcal N_{\rm old}
 &=-m_N\bar{\mathcal N}\mathcal N
       +2im_N\alpha_N\bar{\mathcal N}\gamma_5\mathcal N
       +O(\Delta^2/m_N).
\end{aligned}
\tag{94.33}
$$

正的第二项恰好消去$-i\Delta$。还可以精确完成这个旋转：主质量和赝标量质量合起来，变换后的矩阵为
<span id="eq:x94-exact-nucleon-rotation"></span>

$$
\begin{aligned}
(m_N+i\Delta\gamma_5)e^{-2i\alpha_N\gamma_5}
={}&m_N\cos2\alpha_N+\Delta\sin2\alpha_N\\
 &+i\gamma_5(\Delta\cos2\alpha_N-m_N\sin2\alpha_N),\\
\tan2\alpha_N&=\frac{\Delta}{m_N},\qquad
m_{\rm phys}=\sqrt{m_N^2+\Delta^2}
=m_N+\frac{\Delta^2}{2m_N}+O(\Delta^4/m_N^3).
\end{aligned}
$$

取接近零的$\alpha_N$分支，赝标量系数消失。因为$\Delta$含一次轻夸克质量，主质量的改变从二次开始。

其余作用可按旋量矩阵分成两类。动能与$v_\mu,a_\mu$作用满足
<span id="eq:x94-kinetic-invariance"></span>

$$
e^{-i\alpha_N\gamma_5}\gamma^\mu e^{-i\alpha_N\gamma_5}
 =\gamma^\mu,\qquad
e^{-i\alpha_N\gamma_5}\gamma^\mu\gamma_5e^{-i\alpha_N\gamma_5}
 =\gamma^\mu\gamma_5,
$$

所以常量旋转严格保持这三类项。纯介子项也不变。四个质量结构则可统一写成$\bar{\mathcal N}\mathsf S\mathcal N$和$\bar{\mathcal N}\mathsf P\gamma_5\mathcal N$，其中味矩阵$\mathsf S,\mathsf P=O(M)$与$\gamma_5$对易。它们变为
<span id="eq:x94-mass-operator-variation"></span>

$$
\begin{aligned}
\bar{\mathcal N}_{\rm old}\mathsf S\mathcal N_{\rm old}
 &=\bar{\mathcal N}\mathsf S\mathcal N
 -2i\alpha_N\bar{\mathcal N}\mathsf S\gamma_5\mathcal N
 +O(\alpha_N^2M),\\
\bar{\mathcal N}_{\rm old}\mathsf P\gamma_5\mathcal N_{\rm old}
 &=\bar{\mathcal N}\mathsf P\gamma_5\mathcal N
 -2i\alpha_N\bar{\mathcal N}\mathsf P\mathcal N
 +O(\alpha_N^2M).
\end{aligned}
$$

每个新项都是$O(\alpha_NM)=O(\theta M^2/m_N)$，而$u$的展开不改变轻夸克质量的幂数。这就逐类验证了：在目前的一次质量阶，留下的主要新作用是式[（94.32）](#eq:c94-cp-pion-coupling)的第二项。若加入电磁外源下的其他局域算符，其系数也随场重定义转换。

这个顶角把赝标量$\pi$场与标量核子双线性相乘，因而为宇称奇。按第83节的时间反演变换，它也为时间反演奇；在满足CPT条件的局域洛伦兹理论中，这就是强作用中的CP奇耦合。下面将它与通常的CP偶π–核子耦合各取一次，计算电偶极矩。

<span id="c94-mass-differences"></span>

### 从重子质量差估计$c_+$

先确定新顶角中的低能常数。令$\theta=\pi^a=0$，式[（94.29）](#eq:c94-aligned-lagrangian)的$c_+$项分别给质子和中子$c_+m_u$、$c_+m_d$的质量移位，$c_3$项则给共同移位。因此
<span id="eq:c94-nucleon-mass-difference"></span>

$$
(m_p-m_n)_{\rm strong}=c_+(m_u-m_d).
\tag{94.34}
$$

采用中译本的数值$m_p-m_n=-1.3\,\mathrm{MeV}$、$m_u=1.7\,\mathrm{MeV}$、$m_d=3.9\,\mathrm{MeV}$，暂忽略电磁贡献，得到$c_+\simeq0.59$。核子质量差中的电磁部分与强作用贡献相当，所以还需用含奇夸克的重子作另一估计。

这里补出后一关系所需的三味近似。将低能重子取为味SU(3)八重态，以无迹矩阵表示：
<span id="eq:c94-baryon-octet"></span>

$$
\mathsf B=
\begin{pmatrix}
\Sigma^0/\sqrt2+\Lambda^0/\sqrt6&\Sigma^+&p\\
\Sigma^-&-\Sigma^0/\sqrt2+\Lambda^0/\sqrt6&n\\
\Xi^-&\Xi^0&-2\Lambda^0/\sqrt6
\end{pmatrix}.
\tag{94.35}
$$

这一步采用三味近似的重子分类；矩阵中的$1/\sqrt2,1/\sqrt6$使$\operatorname{Tr}(\bar{\mathsf B}\mathsf B)$给每个场通常的双线性归一。真空中$\mathsf B\mapsto V\mathsf BV^\dagger$，质量伪场$\mathsf M=\operatorname{diag}(m_u,m_d,m_s)$同样按共轭变换。无导数且一次质量的迹可把$\mathsf M$放在$\bar{\mathsf B},\mathsf B$的两种相对位置，另有单态迹项：
<span id="eq:c94-octet-mass-operators"></span>

$$
\delta\mathcal L_8
 =-b_D\operatorname{Tr}\bigl(\bar{\mathsf B}\{\mathsf M,\mathsf B\}\bigr)
  -b_F\operatorname{Tr}\bigl(\bar{\mathsf B}[\mathsf M,\mathsf B]\bigr)
  -b_0\operatorname{Tr}\mathsf M\,
                      \operatorname{Tr}(\bar{\mathsf B}\mathsf B).
\tag{94.36}
$$

这里$\bar{\mathsf B}$的味指标随矩阵伴随倒置，故$\operatorname{Tr}(\bar{\mathsf B}\mathsf M\mathsf B)$中，分量$\mathsf B_{ij}$取左指标质量$m_i$；另一种次序取$m_j$。略去所有重子相同的$b_0$项及手征极限质量，便有
<span id="eq:c94-octet-mass-components"></span>

$$
\begin{aligned}
\delta m_{ij}&=b_D(m_i+m_j)+b_F(m_i-m_j),\\
\delta m_p-\delta m_n&=(b_D+b_F)(m_u-m_d),\\
\delta m_{\Xi^0}&=(b_D+b_F)m_s+(b_D-b_F)m_d,\\
\delta m_{\Sigma^0}&=b_D(m_u+m_d).
\end{aligned}
\tag{94.37}
$$

最后一行来自矩阵中两个$\Sigma^0/\sqrt2$分量；在同位旋极限，它不与$\Lambda^0$混合。与式[（94.34）](#eq:c94-nucleon-mass-difference)匹配，$c_+=b_D+b_F$。再取$m_u=m_d=m_\ell$，得到
<span id="eq:c94-hyperon-relation"></span>

$$
m_{\Xi^0}-m_{\Sigma^0}
 =c_+(m_s-m_\ell),\qquad m_\ell=\frac{m_u+m_d}{2}.
\tag{94.38}
$$

这条估计采用最低阶SU(3)质量展开，并在较大的奇夸克质量差中忽略同位旋破缺和电磁修正。若在式[（94.37）](#eq:c94-octet-mass-components)中保留$m_u-m_d$，还会出现$(b_D-b_F)(m_d-m_u)/2$，这给出所略去的同位旋修正。

以下采用这组质量数值：
<span id="eq:c94-cplus-historical"></span>

$$
c_+\simeq
\frac{122\,\mathrm{MeV}}
     {76\,\mathrm{MeV}-(1.7+3.9)\,\mathrm{MeV}/2}
 \simeq1.67\simeq1.7.
\tag{94.39}
$$

这些示例夸克质量按$\overline{\mathrm{MS}}$方案、$\mu=2\,\mathrm{GeV}$理解。低能常数随质量的定义相应改变，而$c_+\widetilde m$才是进入当前顶角的组合。下面取$c_+=1.7$，保留这一低能估计的精度。

<span id="c94-edm"></span>

## 电偶极形状因子与两张圈图

通常的π–核子作用来自式[（94.29）](#eq:c94-aligned-lagrangian)的轴连接。将$u$展开到一次π，得到
<span id="eq:c94-derivative-pion-coupling"></span>

$$
\mathcal L_{\pi NN}
 =\frac{g_A}{f_\pi}\partial_\mu\pi^a\,
                     \bar{\mathcal N}T^a\gamma^\mu\gamma_5\mathcal N.
\tag{94.40}
$$

若两端核子在壳，可作分部积分。由$i\slashed\partial\mathcal N=m_N\mathcal N$及伴随方程，
<span id="eq:c94-pseudoscalar-pion-coupling"></span>

$$
\begin{aligned}
\partial_\mu(\bar{\mathcal N}\gamma^\mu\gamma_5\mathcal N)
 &=(\partial_\mu\bar{\mathcal N})\gamma^\mu\gamma_5\mathcal N
    -\bar{\mathcal N}\gamma_5\gamma^\mu\partial_\mu\mathcal N\\
 &=im_N\bar{\mathcal N}\gamma_5\mathcal N
    +im_N\bar{\mathcal N}\gamma_5\mathcal N
 =2im_N\bar{\mathcal N}\gamma_5\mathcal N,\\
\mathcal L_{\pi NN}
 &\longrightarrow-i\frac{g_Am_N}{f_\pi}\,
                   \pi^a\bar{\mathcal N}\sigma^a\gamma_5\mathcal N.
\end{aligned}
\tag{94.41}
$$

第二行的2抵消$T^a=\sigma^a/2$的$1/2$，分部积分给最后一行的负号。下面先用这个赝标量顶角计算，再说明在所取圈图中与导数形式的关系。

中子的电磁响应由小转移动量的顶角表示。定义
<span id="eq:c94-edm-form-factor"></span>

$$
T_{\rm EDM}
 =-2iD(q^2)\varepsilon_\mu^*(q)
             \bar u_{s'}(p')S^{\mu\nu}q_\nu i\gamma_5u_s(p),
\qquad q=p'-p.
\tag{94.42}
$$

这里的光子是外电磁探针；$D(q^2)$为CP奇形状因子（form factor）。在$q\to0$时，对应局域项
<span id="eq:c94-edm-operator"></span>

$$
\mathcal L_{\rm EDM}
 =D(0)F_{\mu\nu}\bar nS^{\mu\nu}i\gamma_5n.
\tag{94.43}
$$

将$A_\mu=\varepsilon_\mu^*e^{iqx}$代入，
$F_{\mu\nu}=i(q_\mu\varepsilon_\nu^*-q_\nu\varepsilon_\mu^*)e^{iqx}$；
利用$S^{\mu\nu}$的反对称性，两项合成$-2i\varepsilon_\mu^*S^{\mu\nu}q_\nu$。
因此式[（94.43）](#eq:c94-edm-operator)确实给出式[（94.42）](#eq:c94-edm-form-factor)的$T$，费曼图中的整个顶角再乘$i$。这与[第64节的Pauli顶角匹配](/posts/srednicki-64/#eq:c64-pauli-vertex)完全采用同一振幅约定。

为何这个算符描述电偶极矩？当前Clifford代数给
<span id="eq:c94-dual-spin-identity"></span>

$$
S^{\mu\nu}i\gamma_5
 =-\frac12\epsilon^{\mu\nu\rho\sigma}S_{\rho\sigma},
\qquad
\mathcal L_{\rm EDM}=-D(0)\widetilde F_{\mu\nu}\bar nS^{\mu\nu}n.
\tag{94.44}
$$

例如$S^{01}=i\gamma^0\gamma^1/2$，
$(\gamma^0\gamma^1)^2=1$，故
$S^{01}i\gamma_5=-i\gamma^2\gamma^3/2=-S^{23}$。
其余互补指标对由同样的反对易交换确定；交换$\mu,\nu$或$\rho,\sigma$各给一次负号，六对分量便组成上面的epsilon式。这也固定了对偶张量关系的整体负号。

对偶磁场满足$\widetilde{\mathbf B}=-\mathbf E$，所以静止电场中的第二式给
$2D(0)\mathbf E\cdot\bar n\boldsymbol S n$。第64节的非相对论归一把它变成
<span id="eq:c94-electric-dipole-energy"></span>

$$
\mathcal H_{\rm EDM}
 =-D(0)\,n_{\rm NR}^\dagger\boldsymbol\sigma\cdot\mathbf E\,n_{\rm NR},
\qquad d_n=D(0).
\tag{94.45}
$$

自旋平行、反平行于电场的能量因而相差$2d_n|\mathbf E|$。电场为极向量，自旋为轴向量，这个能量项与前面的P、T破坏相符。

现在展开带电π的味结构：
<span id="eq:c94-charged-pion-matrix"></span>

$$
\pi^a\sigma^a=
\begin{pmatrix}
\pi^0&\sqrt2\,\pi^+\\
\sqrt2\,\pi^-&-\pi^0
\end{pmatrix},
\qquad
\pi^\pm=\frac{\pi^1\mp i\pi^2}{\sqrt2}.
\tag{94.46}
$$

令$G=g_Am_N/f_\pi$，并沿式[（94.32）](#eq:c94-cp-pion-coupling)记$\bar g=\theta c_+\widetilde m/f_\pi$，则两种带电作用为
<span id="eq:c94-charged-vertices"></span>

$$
\begin{aligned}
\mathcal L_{\rm even}
 &=-i\sqrt2G\,(\pi^+\bar p\gamma_5n+\pi^-\bar n\gamma_5p),\\
\mathcal L_{\rm odd}
 &=-\sqrt2\bar g\,(\pi^+\bar pn+\pi^-\bar np),\\
iV_{\rm even}&=\sqrt2G\gamma_5,\qquad
iV_{\rm odd}=-i\sqrt2\bar g .
\end{aligned}
\tag{94.47}
$$

最后一行是$i$乘拉格朗日量系数；两个$\sqrt2$分别来自一个非对角味矩阵元。中子沿开放费米线变为质子再变回中子，光子接在带电π线上。CP奇顶角可以在左端，也可以在右端，故有两张图：

<img src="/images/srednicki/94-inline-1.svg" alt="光子接在带电π线上，CP奇顶角分别位于两端的两张圈图" style="width: 620px; max-width: 100%; height: auto;" />

叉号表示一次CP奇顶角；两图的核子箭头连续向右。
<span id="c94-edm-two-graphs"></span>

核子线是开放的，因此没有闭费米圈的负号；两种顶角位置也没有额外的对称因子。本节$e$取$\pi^+$的正电荷，若与第64节比较，则$e=-e_{\rm electron}>0$。采用两图共用的对称动量路由：
<span id="eq:c94-loop-routing"></span>

$$
\bar p=\frac{p+p'}2,\qquad
P=\ell+\bar p,\qquad
k_L=\ell+\frac q2,\qquad k_R=\ell-\frac q2 .
\tag{94.48}
$$

左、右端分别满足$p+k_L=P$、$P=p'+k_R$，光子顶角满足$k_R+q=k_L$。所以标量电磁顶角为$ie(k_L+k_R)^\mu=ie\,2\ell^\mu$。

<img src="/images/srednicki/94-inline-2.svg" alt="内部质子和两段π线的对称动量路由" style="width: 360px; max-width: 100%; height: auto;" />

两图共用的动量路由。光子动量流入，π箭头方向按正电荷流向取定。
<span id="c94-edm-routing-figure"></span>

<span id="c94-loop-reduction"></span>

## 从完整振幅到软π积分

把三条传播子的$1/i$、光子顶角和两个π–核子顶角依次相乘，先只看不含狄拉克矩阵的常数：
<span id="eq:c94-loop-prefactor"></span>

$$
\left(\frac1i\right)^3(ie)(\sqrt2G)(-i\sqrt2\bar g)
 =2ieG\bar g .
\tag{94.49}
$$

记
<span id="eq:c94-loop-denominators"></span>

$$
\begin{aligned}
\mathscr D_N&=P^2+m_N^2-i0,\\
\mathscr D_L&=k_L^2+m_\pi^2-i0,\qquad
\mathscr D_R=k_R^2+m_\pi^2-i0 .
\end{aligned}
\tag{94.50}
$$

内部质子的传播子分子为$-\slashed P+m_N$。两张图的差别只在$\gamma_5$位于它的哪一侧，因此振幅为
<span id="eq:c94-full-two-diagram-integral"></span>

$$
\begin{aligned}
iT&=2ieG\bar g\,\varepsilon_\mu^*
 \int\frac{d^4\ell}{(2\pi)^4}
 \frac{2\ell^\mu\,\bar u'\mathsf N_5u}
      {\mathscr D_N\mathscr D_L\mathscr D_R},\\
\mathsf N_5&=(-\slashed P+m_N)\gamma_5
                 +\gamma_5(-\slashed P+m_N).
\end{aligned}
\tag{94.51}
$$

这里没有提前令内部核子在壳。先用$\{\gamma^\mu,\gamma_5\}=0$，两个动量分子恰好相消：
<span id="eq:c94-two-chain-sum"></span>

$$
(-\slashed P+m_N)\gamma_5+\gamma_5(-\slashed P+m_N)
 =2m_N\gamma_5.
\tag{94.52}
$$

去掉振幅两边共同的$i$，得到
<span id="eq:c94-reduced-exact-integral"></span>

$$
T=\frac{4e\theta g_Ac_+\widetilde m m_N^2}{f_\pi^2}
 \varepsilon_\mu^*\bar u'\gamma_5u
 \int\frac{d^4\ell}{(2\pi)^4}
       \frac{2\ell^\mu}{\mathscr D_N\mathscr D_L\mathscr D_R}.
\tag{94.53}
$$

系数中的一个$m_N$来自通常π–核子顶角，另一个来自两条开放链相加。系数4已包含两个带电顶角的味因子，以及两条开放链的相加。

在这里使用赝标量顶角也可由导数形式直接检查。由于$k_L=P-p$，
<span id="eq:c94-derivative-contact-identity"></span>

$$
\slashed k_L\gamma_5
 =(\slashed P+m_N)\gamma_5
  +\gamma_5(\slashed p+m_N)-2m_N\gamma_5.
\tag{94.54}
$$

外腿在壳使中间项消失；末项是分部积分所得的赝标量顶角。第一项乘内部传播子分子，利用
$(-\slashed P+m_N)(\slashed P+m_N)=P^2+m_N^2$，
便取消内部核子分母。右端有相同的关系，剩下的接触型积分具有
<span id="eq:c94-odd-contact-integral"></span>

$$
\int\frac{d^4\ell}{(2\pi)^4}\,
 \frac{2\ell^\mu}
 {[(\ell+q/2)^2+m_\pi^2-i0][(\ell-q/2)^2+m_\pi^2-i0]}=0.
\tag{94.55}
$$

分母在$\ell\mapsto-\ell$时交换两因子，分子变号，故对称调节下积分为零。所画两图中，导数顶角与赝标量顶角的差因而消失。

现在提取$q$的一次项。等质量外腿满足
$(\slashed p+m_N)u=0$、$\bar u'(\slashed p'+m_N)=0$，因而
<span id="eq:c94-small-transfer-bilinear"></span>

$$
\begin{aligned}
\bar u'\slashed q\gamma_5u
 &=\bar u'\slashed p'\gamma_5u-\bar u'\slashed p\gamma_5u
 =-2m_N\bar u'\gamma_5u,\\
\bar u'\gamma_5u
 &=-\frac{q_\mu}{2m_N}\bar u'\gamma^\mu\gamma_5u=O(q).
\end{aligned}
\tag{94.56}
$$

这对不同的自旋标签也成立。因此先保持$m_\pi>0$，在式[（94.53）](#eq:c94-reduced-exact-integral)的其余平滑因子中取$q=0$，不会改变所求的一次项。由$p^2=p'^2=-m_N^2$及$\bar p^2=-m_N^2-q^2/4$，
<span id="eq:c94-soft-nucleon-denominator"></span>

$$
\mathscr D_N
 =2\bar p\cdot\ell+\ell^2-\frac{q^2}{4}-i0
 \longrightarrow 2p\cdot\ell-i0.
\tag{94.57}
$$

第二步进一步保留软动量$|\ell|/m_N$的领头阶。对数可在
$m_\pi\ll|\ell|\ll m_N,\Lambda_\chi$的窗口中提取，$\Lambda_\chi$为手征有效理论的高能尺度。用一个中间尺度$\mu_s$隔开软、硬区，软区给$\log(\mu_s^2/m_\pi^2)$，硬区的匹配补出不依赖小$m_\pi$的部分。重核子展开用于软区，接近$\Lambda_\chi\sim4\pi f_\pi$的贡献则归入匹配系数。

这时振幅化为
<span id="eq:c94-soft-vector-integral"></span>

$$
\begin{aligned}
T_{\rm soft}
 &=\frac{4e\theta g_Ac_+\widetilde m m_N^2}{f_\pi^2}
   \varepsilon_\mu^*\bar u'\gamma_5u\,J^\mu,\\
J^\mu&=\int\frac{d^4\ell}{(2\pi)^4}
 \frac{\ell^\mu}{p\cdot\ell-i0}\,
 \frac1{(\ell^2+m_\pi^2-i0)^2}.
\end{aligned}
\tag{94.58}
$$

吸收正的2不改变$i0$处方。下一步需要求这个矢量积分。取核子静止系$p=(m_N,\mathbf0)$，三个空间分量都对相应$\ell^i$为奇，积分为零；时间分量用分布恒等式$x/(x+i0)=1$，得到
<span id="eq:c94-vector-projection"></span>

$$
\begin{gathered}
J^i=0,\qquad
J^0=-\frac1{m_N}I_\pi,\qquad
I_\pi=\int\frac{d^4\ell}{(2\pi)^4}
                 \frac1{(\ell^2+m_\pi^2-i0)^2},\\
J^\mu=\frac{p^\mu}{p^2}I_\pi
     =-\frac{p^\mu}{m_N^2}I_\pi .
\end{gathered}
\tag{94.59}
$$

这里保持与静止系对称性相容的调节；协变写法随后恢复一般$p$。由于分母本身含一个$p\cdot\ell$，结果没有另一个$1/4$。先处理这个极点分布，再对剩余的$I_\pi$作Wick转动，可以避免把有极点的四维“角积分”误当成实球上的普通平均。

最后需要把$p^\mu\bar u'\gamma_5u$写成偶极结构。令
$P_5=\bar u'\gamma_5u$、$A_5^\mu=\bar u'\gamma^\mu\gamma_5u$。
Clifford关系$\{\gamma^\mu,\slashed p\}=-2p^\mu$及外腿方程分别给
<span id="eq:c94-gordon-commutator"></span>

$$
\begin{aligned}
\bar u'\gamma^\mu\slashed q\gamma_5u
 &=m_NA_5^\mu-2p'^\mu P_5-m_NA_5^\mu
 =-2p'^\mu P_5,\\
-\bar u'\slashed q\gamma^\mu\gamma_5u
 &=m_NA_5^\mu-m_NA_5^\mu-2p^\mu P_5
 =-2p^\mu P_5 .
\end{aligned}
\tag{94.60}
$$

两行相加就是$\bar u'[\gamma^\mu,\slashed q]\gamma_5u$。又因$S^{\mu\nu}=i[\gamma^\mu,\gamma^\nu]/4$，乘上$i/4$及右边的$i$后，有精确关系
<span id="eq:c94-axial-gordon"></span>

$$
\bar u'S^{\mu\nu}q_\nu i\gamma_5u
 =\bar p^\mu\bar u'\gamma_5u,
\qquad
p^\mu\bar u'\gamma_5u
 =\bar u'S^{\mu\nu}q_\nu i\gamma_5u+O(q^2).
\tag{94.61}
$$

第二式只用$\bar p-p=q/2$及式[（94.56）](#eq:c94-small-transfer-bilinear)。将它和式[（94.59）](#eq:c94-vector-projection)放回振幅，$m_N^2$相消，得到
<span id="eq:c94-scalar-loop-matching"></span>

$$
T_{\log}
 =-\frac{4e\theta g_Ac_+\widetilde m}{f_\pi^2}
   \varepsilon_\mu^*\bar u'S^{\mu\nu}q_\nu i\gamma_5u\,I_\pi .
\tag{94.62}
$$

现在自旋结构已与式[（94.42）](#eq:c94-edm-form-factor)相同，剩下的工作是把标量积分算完。

<span id="c94-chiral-log"></span>

## 手征对数、有限项与强CP问题

费曼分母$\ell^2+m_\pi^2-i0$的正能极点在实轴下方，负能极点在上方。按前面各圈积分所用的轮廓把$\ell^0$转到虚轴，测度给$i$，分母成为正定的$L^2+m_\pi^2$。为把保留的对数与有限项分开，暂取Euclid径向截止$L<\Lambda$：
<span id="eq:c94-wick-radial-integral"></span>

$$
I_\pi(\Lambda)
 =i\frac{2\pi^2}{(2\pi)^4}
       \int_0^\Lambda\frac{L^3\,dL}{(L^2+m_\pi^2)^2}
 =\frac{i}{16\pi^2}
       \int_0^{\Lambda^2}\frac{s\,ds}{(s+m_\pi^2)^2}.
\tag{94.63}
$$

$2\pi^2$是单位三球面的面积，$s=L^2$给$L^3dL=s\,ds/2$。将被积函数拆为
$s/(s+m_\pi^2)^2=(s+m_\pi^2)^{-1}-m_\pi^2(s+m_\pi^2)^{-2}$，
原函数与上下限评价为
<span id="eq:c94-evaluated-cutoff-integral"></span>

$$
\begin{aligned}
\int\frac{s\,ds}{(s+m_\pi^2)^2}
 &=\log\frac{s+m_\pi^2}{\mu_0^2}
                      +\frac{m_\pi^2}{s+m_\pi^2},\\
I_\pi(\Lambda)
 &=\frac{i}{16\pi^2}\left[
   \log\left(1+\frac{\Lambda^2}{m_\pi^2}\right)
   +\frac{m_\pi^2}{\Lambda^2+m_\pi^2}-1\right]\\
 &=\frac{i}{16\pi^2}
   \left[\log\frac{\Lambda^2}{m_\pi^2}-1
                     +O(m_\pi^2/\Lambda^2)\right].
\end{aligned}
\tag{94.64}
$$

原函数中的参照质量$\mu_0>0$在上下限相减时消去，定积分只留下质量比。当$m_\pi\to0$时，对数是增强的非解析部分；完整的截止积分还含有限的$-1$。改变调节或硬区匹配会改变这类解析常数，不改变当前非解析对数的系数。

比较式[（94.62）](#eq:c94-scalar-loop-matching)与式[（94.42）](#eq:c94-edm-form-factor)，$-4$乘$i/(16\pi^2)$再除以$-2i$，得到
<span id="eq:c94-edm-logarithm"></span>

$$
d_n^{\log}
 =\frac{e\theta g_Ac_+\widetilde m}{8\pi^2f_\pi^2}
                      \log\frac{\Lambda^2}{m_\pi^2}.
\tag{94.65}
$$

两条轻π传播子与软核子分母、顶角分子合在一起，给出$\int dL/L$的窗口，从而产生这两图的红外增强。顶角动量和重粒子分母共同决定积分的红外阶数。

低能拉格朗日量本身也允许式[（94.43）](#eq:c94-edm-operator)的局域系数。把同阶有限圈项和这个系数并入$d_n^{\rm loc}(\mu_s)$，更完整的写法是
<span id="eq:c94-local-edm-matching"></span>

$$
\begin{aligned}
d_n&=K_\theta\log\frac{\mu_s^2}{m_\pi^2}
       +d_n^{\rm loc}(\mu_s)+\text{高阶项},\\
K_\theta&=\frac{e\theta g_Ac_+\widetilde m}{8\pi^2f_\pi^2},
\qquad
\frac{d\,d_n^{\rm loc}}{d\log\mu_s}=-2K_\theta
       \quad\text{在当前阶次}.
\end{aligned}
\tag{94.66}
$$

尺度依赖在两项之间抵消。领头对数给出非解析部分，其余有限系数还须匹配。在下面的估计中，对数约为4.2，有限项未必小到可以忽略。

取以下数值作领头对数估计：$f_\pi=92.4\,\mathrm{MeV}$、$g_A=1.27$、$c_+=1.7$、$\widetilde m=1.2\,\mathrm{MeV}$和对数4.2，得到
<span id="eq:c94-historical-edm-value"></span>

$$
\begin{aligned}
\frac{d_n^{\log}}{e\theta}
 &\simeq\frac{1.27\times1.7\times0.0012}
               {8\pi^2(0.0924)^2}\,4.2\ \mathrm{GeV}^{-1}\\
 &\simeq0.0161\ \mathrm{GeV}^{-1}
 \simeq3.2\times10^{-16}\ \mathrm{cm}.
\end{aligned}
\tag{94.67}
$$

最后一步使用自然单位换算$\hbar c\simeq0.197327\,\mathrm{GeV\,fm}$，
即$1\,\mathrm{GeV}^{-1}\simeq1.97327\times10^{-14}\,\mathrm{cm}$。
质量只出现一次，而$f_\pi^2$在分母，故长度量纲也正确。

再用中译本引用的实验上限$|d_n|<6.3\times10^{-26}\,e\,\mathrm{cm}$，与这个主导对数估计比较，
<span id="eq:c94-historical-theta-bound"></span>

$$
|\theta|\ \lesssim\
\frac{6.3\times10^{-26}}{3.2\times10^{-16}}
 \simeq2.0\times10^{-10}.
\tag{94.68}
$$

这是在给定上限下的示例推限，依赖上述强子估计，并假定未知有限项没有显著抵消它。其意义是：QCD允许一个无量纲的强CP相位，所算出的强子响应却要求它极小。这个小参数为何如此特殊，就是强CP问题（strong CP problem）。

原书接着讨论三种机制。若有一个严格无质量的上夸克，轴重定义已足以消去$\theta$，但强子谱须由包含高阶质量项的理论解释。若基本理论施加CP，再让弱CP破坏来自自发破缺，还需计算破缺和量子修正对$\bar\theta$的影响。第三种机制把相位变成动力学场，让强作用真空能量决定它的平均值。下面具体构造这个轴子模型。

<span id="c94-axion"></span>

## Peccei–Quinn对称性与轴子

在理论中加入一对色表示为$\mathbf3,\bar{\mathbf3}$的左手Weyl场$\chi,\xi$和一个色单态复标量$\Phi$，并取
<span id="eq:x94-pq-model"></span>

$$
\mathcal L_Y=y\Phi\chi\xi+y^*\Phi^\dagger\xi^\dagger\chi^\dagger,
\qquad V=V(\Phi^\dagger\Phi).
\tag{94.69}
$$

把这个作用写成通常的负质量项时，质量参数为$-y\Phi$。

### 经典不变性与量子反常

给三场赋予PQ荷$+1,+1,-2$，常数$\alpha$的变换为
<span id="eq:x94-pq-transformation"></span>

$$
\chi\mapsto e^{i\alpha}\chi,\qquad
\xi\mapsto e^{i\alpha}\xi,\qquad
\Phi\mapsto e^{-2i\alpha}\Phi.
\tag{94.70}
$$

Yukawa项中三个相位相乘为1，其共轭同样不变。通常的协变动能只含场与其共轭，常量相位不受导数作用；$\Phi^\dagger\Phi$也不变，所以势保持不变。这证明了经典整体$U(1)_{\rm PQ}$对称性。

两个左手场可组成一个基本狄拉克场$\Psi_Q=(\chi,\xi^\dagger)^T$，其PQ变换正是
$\Psi_Q\mapsto e^{-i\alpha\gamma_5}\Psi_Q$。复标量的常量相位变换在实二维场空间中是行列式1的旋转，测度无额外相位；费米测度则给式[（94.3）](#eq:c94-jacobian)，故作PQ变量代换后，作用量参数重写为
<span id="eq:x94-pq-anomaly"></span>

$$
\theta'=\theta+2\alpha.
\tag{94.71}
$$

所以PQ是有反常的整体对称性。

### 重夸克质量和轴子相位

若势在$|\Phi|=f/\sqrt2$处最低，取$f>0$并写成极坐标，
<span id="eq:x94-heavy-quark-mass"></span>

$$
\Phi=\frac{f+\rho}{\sqrt2}e^{ia/f},\qquad
m_Q(a)=-\frac{yf}{\sqrt2}e^{ia/f},\qquad
|m_Q|=\frac{|y|f}{\sqrt2}.
\tag{94.72}
$$

第二式通过$\mathcal L_m=-m_Q\chi\xi+\mathrm{h.c.}$定义；其负号来自Yukawa项的正号。只有$y\ne0$时，新夸克才有非零质量。常量PQ变换使$a\mapsto a-2f\alpha$，径向场$\rho$不变。

先取轻夸克质量实正，把$-y$的常量相位通过一次轴重定义移入
$\theta_0=\theta-\arg(-y)$。剩下的重质量相位为$a/f$。为在固定标量背景中消去它，只对费米场作局域变量代换
<span id="eq:x94-local-heavy-rotation"></span>

$$
\chi_{\rm old}=e^{-ia/(2f)}\chi,\qquad
\xi_{\rm old}=e^{-ia/(2f)}\xi,\qquad
\alpha(x)=-\frac{a(x)}{2f}.
\tag{94.73}
$$

两个费米相位相乘消去$e^{ia/f}$。雅可比将拓扑系数改成
<span id="eq:x94-effective-axion-angle"></span>

$$
\Theta(x)=\theta_0-\frac{a(x)}f .
\tag{94.74}
$$

这个结果也可直接由不变量$\theta-\arg\det M$得到：重夸克的质量相位是$\arg(-y)+a/f$，所以减去它恰好给本式。

轴子在$\Theta$中的负号由其在$\Phi$中的正指数固定。若另定义$a_{\rm alt}=-a$，标量指数同时变成$e^{-ia_{\rm alt}/f}$，有效角便写成$\Theta=\theta_0+a_{\rm alt}/f$。两套记号给出同一物理相位；下面继续使用$a$。

由于代换是局域的，动能还产生一个导数耦合。将
$\Psi_{Q,\rm old}=e^{-i\alpha(x)\gamma_5}\Psi_Q$代入，有
<span id="eq:x94-axion-derivative-coupling"></span>

$$
i\bar\Psi_{Q,\rm old}\slashed D\Psi_{Q,\rm old}
 =i\bar\Psi_Q\slashed D\Psi_Q
  +(\partial_\mu\alpha)\bar\Psi_Q\gamma^\mu\gamma_5\Psi_Q
 =i\bar\Psi_Q\slashed D\Psi_Q
  -\frac{\partial_\mu a}{2f}j_{A,Q}^\mu.
\tag{94.75}
$$

中间的正号来自动能的$i$乘微分指数的$-i$。标量动能则直接给
<span id="eq:x94-polar-kinetic"></span>

$$
-\partial_\mu\Phi^\dagger\partial^\mu\Phi
 =-\frac12(\partial\rho)^2
  -\frac12\left(1+\frac{\rho}{f}\right)^2(\partial a)^2.
\tag{94.76}
$$

两个混合项互为相反的纯虚数，故相消。在能量远低于径向质量与$|y|f/\sqrt2$时，可以积分掉新重场；令$\rho=0$的领头阶留下标准动能$-(\partial a)^2/2$。两味强子理论中，把前面$M=M_0e^{-i\theta/2}$的$\theta$换成$\Theta(x)$。若再作随位置变化的轻场重定义，产生的导数作用也应保留；求均匀真空与零动量势时，这些导数项为零。

### 真空怎样消去强CP相位

把式[（94.74）](#eq:x94-effective-axion-angle)代入式[（94.20）](#eq:c94-vacuum-minimum)的两味真空能，
<span id="eq:x94-axion-potential"></span>

$$
V_{\rm eff}(a)
 =-2v^3
 \sqrt{(m_u+m_d)^2-4m_um_d\sin^2\frac{\Theta(a)}2}.
\tag{94.77}
$$

对于$m_u,m_d>0$，根号内的量在$\sin[\Theta/2]=0$时最大，因而势最低。局部分支可选
<span id="eq:x94-axion-minimum"></span>

$$
\Theta=0,\qquad a_*=f\theta_0,\qquad U_*=I;
\qquad a_*\ \text{按}\ 2\pi f\ \text{等价}.
\tag{94.78}
$$

这是正指数定义下的真空位置。若用$a_{\rm alt}$，同一个最低点写为$a_{{\rm alt},*}=-f\theta_0$。最低点的有效强相位为零，前面所算的CP奇π–核子顶角及其电偶极矩随之消失。这个最低点恢复了所讨论强作用的P和CP。

### 轴子质量与中性π的混合

令$a'=a-a_*$，则$\Theta=-a'/f$，并记$s=m_u+m_d$。由式[（94.24）](#eq:c94-topological-susceptibility)，
<span id="eq:x94-axion-mass-curvature"></span>

$$
\begin{aligned}
V_{\rm eff}&=V_0+v^3\widetilde m\,\frac{a'^2}{f^2}
                         +O(v^3s a'^4/f^4),\\
m_a^2&=\frac{2v^3\widetilde m}{f^2}
       \left[1+O(f_\pi^2/f^2)\right].
\end{aligned}
\tag{94.79}
$$

这里的势已经对π场取极小值。要看清这一步以及所列修正，回到尚未对齐的中性场，取$U=\exp(i\pi^0\sigma^3/f_\pi)$。将两个余弦各展开到二次，得
<span id="eq:x94-neutral-pion-axion-potential"></span>

$$
V^{(2)}=v^3\left[
 s\frac{(\pi^0)^2}{f_\pi^2}
 +\frac{s}{4}\Theta^2-d\frac{\pi^0\Theta}{f_\pi}\right],
\qquad s=m_u+m_d,\quad d=m_u-m_d .
\tag{94.80}
$$

在未移去$\pi^0$的变量中，两场的二次动能都为标准归一，故基$(a',\pi^0)$中的质量平方矩阵是
<span id="eq:x94-axion-pion-hessian"></span>

$$
\mathsf H=
\begin{pmatrix}
v^3s/(2f^2)&v^3d/(ff_\pi)\\
v^3d/(ff_\pi)&2v^3s/f_\pi^2
\end{pmatrix}
\equiv\begin{pmatrix}A&B\\B&C\end{pmatrix}.
\tag{94.81}
$$

交叉项为正，因为$\Theta=-a'/f$；对$m_u<m_d$，矩阵元$B$本身为负。两个本征质量平方为
<span id="eq:x94-exact-two-masses"></span>

$$
m_\pm^2=\frac{A+C\pm\sqrt{(C-A)^2+4B^2}}2.
\tag{94.82}
$$

当$f\gg f_\pi$时，$A/C=O(f_\pi^2/f^2)$、$B/C=O(f_\pi/f)$，展开较轻根得到
<span id="eq:x94-light-eigenvalue-expansion"></span>

$$
\begin{aligned}
m_-^2&=A-\frac{B^2}{C}+O(Cf_\pi^4/f^4)\\
 &=\frac{v^3}{2f^2}\left(s-\frac{d^2}{s}\right)
       +O(v^3s f_\pi^2/f^4)
 =\frac{2v^3m_um_d}{s f^2}
       +O(v^3s f_\pi^2/f^4).
\end{aligned}
\tag{94.83}
$$

利用$s^2-d^2=4m_um_d$便得到式[（94.79）](#eq:x94-axion-mass-curvature)。等价地，先由$\partial V^{(2)}/\partial\pi^0=0$求$\pi^0$，再代回势，就是Schur补$A-B^2/C$；重方向随轴子缓慢改变，所以轻方向的曲率由$A-B^2/C$决定。

由$m_\pi^2=2v^3s/f_\pi^2$，结果也可写成
<span id="eq:x94-axion-mass-pion-ratio"></span>

$$
m_a^2=m_\pi^2\frac{f_\pi^2}{f^2}
          \frac{m_um_d}{(m_u+m_d)^2}
          \left[1+O(f_\pi^2/f^2)\right].
\tag{94.84}
$$

在同位旋极限$d=0$，两场不混合，轻质量直接为$A$，与本式的质量比$1/4$一致。任一轻夸克质量为零时，$AC-B^2=0$，精确轻根为零，和无质量味可消去强相位的论证相合。对正质量，$A,C>0$且$AC-B^2>0$，两个小振动方向都稳定。

### 大$f$极限

固定$y$和轻强子参数，式[（94.72）](#eq:x94-heavy-quark-mass)使新夸克质量按$f$增长，而式[（94.84）](#eq:x94-axion-mass-pion-ratio)使轴子质量按$1/f$下降。在已经积分掉重夸克和径向场的有效理论中，轴子由$\Theta=\theta_0-a/f$和$\partial_\mu a/f$进入。围绕最低点，每取一个轴子涨落，就从这些函数的Taylor展开取得一个$1/f$：
<span id="eq:x94-axion-coupling-expansion"></span>

$$
\mathcal L_{\rm had}(\Theta)
 =\mathcal L_{\rm had}(0)
  -\frac{a'}f\left.\frac{\partial\mathcal L_{\rm had}}{\partial\Theta}
                       \right|_0
  +\frac{a'^2}{2f^2}
        \left.\frac{\partial^2\mathcal L_{\rm had}}{\partial\Theta^2}
                       \right|_0+\cdots.
\tag{94.85}
$$

例如前面求得的CP奇π–核子项成为
$+(c_+\widetilde m/f_\pi f)a'\pi^a\bar{\mathcal N}\sigma^a\mathcal N$，
其中一轴子顶角确有$1/f$。中性π与轴子的混合角也由
$B/C=O(f_\pi/f)$压低。低能强子作用中的轴子顶角因此在大$f$时受抑制。直接的重夸克Yukawa耦合$|m_Q|/f=|y|/\sqrt2$在固定$y$时保持常量，但这些重夸克已不在所讨论的低能自由度中。

---

[← 第 93 节](/posts/srednicki-93/) · [章节地图](/srednicki/) · [第 95 节 →](/posts/srednicki-95/)
