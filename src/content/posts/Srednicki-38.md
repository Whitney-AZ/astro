---
title: 'Srednicki §38 旋量技术'
date: 2026-09-14
category: 笔记
tags: [物理, 量子场论, Srednicki]
series: 'Srednicki QFT'
srednickiSections: [38]
hideFromHome: true
draft: false
---

<span id="c38"></span>

上一节给出了场的平面波展开，其中旋量$u_s(\mathbf p)$、$v_s(\mathbf p)$的归一和相位还留有选择。现在先在静止系固定四个旋量，再把它们推动到任意动量，就能得到一套确定的基。不过，在许多计算中，真正需要的是旋量的内积或外积。这些组合的变换性质使我们可以先在静止系计算，再将结果写成协变形式，而不必每次都展开四个分量。下面由此求出归一关系、戈登恒等式和自旋求和，继而讨论固定自旋与高能极限；这些结果将用于自由场的哈密顿量，也将进入费米子散射振幅的计算。

下面沿用[上一节](/posts/srednicki-37/#c37)的平面波方程与模式展开。先取$m>0$，无质量情形随后通过固定非零动量的极限得到。本节的$u,v$都是普通数值旋量，彼此交换；场展开中的奇算符性质则由模式系数承担。

<span id="c38-rest"></span>

## 静止旋量的自旋标签和相位

从两个在壳方程$(\slashed p+m)u_s=0$、$(-\slashed p+m)v_s=0$出发。在静止系$p^\mu=(m,\mathbf0)$，斜线动量变为$\slashed p=-m\gamma^0$，所以$u$和$v$分别属于$\gamma^0$的$+1$、$-1$本征空间。将四分量列分成两个二分量块，便能直接解出上、下块之间的关系：

<span id="eq:c38-rest-equations"></span>

$$
\gamma^0=\begin{pmatrix}0&I_2\\I_2&0\end{pmatrix},\qquad
u(0)=\begin{pmatrix}a\\a\end{pmatrix},\qquad
v(0)=\begin{pmatrix}b\\-b\end{pmatrix}.
\tag{38.1}
$$

每个解空间都是二维的，还需要选出其中两个基矢。为使标签具有自旋意义，选择第三轴的自旋矩阵：

<span id="eq:c38-spin-matrix"></span>

$$
S_z=S^{12}=\frac i4[\gamma^1,\gamma^2]
=\frac i2\gamma^1\gamma^2
=\frac12\begin{pmatrix}\sigma_3&0\\0&\sigma_3\end{pmatrix}.
\tag{38.2}
$$

最后一个等号由 $\gamma$矩阵的外尔块相乘得到，其中用了$\sigma_1\sigma_2=i\sigma_3$。记两个二分量基矢为$e_+=(1,0)^T$、$e_-=(0,1)^T$，再取$\eta_s=Ee_s=s e_{-s}$，其中$s=\pm1$、$E=\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)$。用这组记号，静止旋量及其自旋本征值可统一写为

<span id="eq:c38-rest-spinors"></span>

$$
\begin{gathered}
u_s(0)=\sqrt m\begin{pmatrix}e_s\\e_s\end{pmatrix},
\qquad
v_s(0)=\sqrt m\begin{pmatrix}\eta_s\\-\eta_s\end{pmatrix},\\
S_z u_s(0)=\frac s2u_s(0),\qquad
S_z v_s(0)=-\frac s2v_s(0).
\end{gathered}
\tag{38.3}
$$

例如，$\eta_+=e_-$、$\eta_-=-e_+$，给出$v_+(0)=\sqrt m(0,1,0,-1)^T$和$v_-(0)=\sqrt m(-1,0,1,0)^T$。其中$\sqrt m$的归一因子和两个相对相位是对解的约定，齐次场方程本身仍允许整体缩放。这样选择相位的便利，将在后面的电荷共轭关系中显现：同一个$s$标签的$u,v$恰好配成一对。

两类列旋量的自旋本征值取相反号，是为了让对应产生算符使用相同的物理自旋标签。[第 36 节的场转动律](/posts/srednicki-36/#c36-lorentz)在静止模式上给出$[\Psi,J_z]=S_z\Psi$，而轨道转动保持$\mathbf p=0$不变。将场的模式展开代入，并分别比较两个频率的系数，得到$[b_s,J_z]=s b_s/2$、$[d_s^\dagger,J_z]=-s d_s^\dagger/2$。第一式取厄米共轭，第二式交换对易子的次序，就得到两个产生算符的自旋关系：

<span id="eq:c38-mode-spin"></span>

$$
[J_z,b_s^\dagger(0)]=\frac s2 b_s^\dagger(0),\qquad
[J_z,d_s^\dagger(0)]=\frac s2 d_s^\dagger(0).
\tag{38.4}
$$

当真空转动不变时，这两种产生算符所生粒子的自旋标签都为$s/2$。沿第三轴的非零动量也有这个性质。完整场变换律含轨道项$-i(x\partial_y-y\partial_x)\Psi$；投影到$\mathbf p=p\hat{\mathbf z}$时，傅里叶因子与$x,y$无关，分部积分给出

<span id="eq:c38-orbital-axis"></span>

$$
\int d^3x\,e^{\mp ipx}(x\partial_y-y\partial_x)\Psi
=-\int d^3x\,[(x\partial_y-y\partial_x)e^{\mp ipx}]\Psi=0.
$$

这里可先对横向衰减的矩阵元计算，再取平面波的分布极限。沿第三轴的推动又与$S_z$对易，故$u_s,v_s$仍有相同的矩阵自旋本征值；比较两频率的系数，便把[（38.4）](#eq:c38-mode-spin)推广到任意$p\hat{\mathbf z}$。一般方向的动量还会留下轨道贡献。

求旋量的内积和外积还需要带横线的行旋量。定义$\bar u=u^\dagger\beta$、$\bar v=v^\dagger\beta$。由于$\beta=\gamma^0$交换两个块，并满足$\beta^T=\beta^\dagger=\beta^{-1}=\beta$，静止行旋量为

<span id="eq:c38-rest-bars"></span>

$$
\bar u_s(0)=\sqrt m(e_s^\dagger,e_s^\dagger),\qquad
\bar v_s(0)=\sqrt m(-\eta_s^\dagger,\eta_s^\dagger).
\tag{38.5}
$$

逐个代入$e_+,e_-$和$\eta_+,\eta_-$，便得到四个行旋量；例如$\bar v_+(0)=\sqrt m(0,-1,0,1)$、$\bar v_-(0)=\sqrt m(1,0,-1,0)$。行、列的相位和归一至此一并固定，可以用同一个推动把它们送到一般动量。

<span id="c38-boost"></span>

## 推动和矩阵的狄拉克伴随

对于$p^\mu=(\omega,\mathbf p)$，选择沿$\hat{\mathbf p}$且不附加转动的推动。能量和动量大小满足$\omega=m\cosh\eta$、$|\mathbf p|=m\sinh\eta$，所以快度为$\eta=\operatorname{arsinh}(|\mathbf p|/m)$。把这一变换作用于两个频率支的静止旋量，便有

<span id="eq:c38-boost"></span>

$$
\begin{gathered}
K^j=S^{j0}=\frac i2\gamma^j\gamma^0
=\frac i2\begin{pmatrix}\sigma_j&0\\0&-\sigma_j\end{pmatrix},\\
D(\mathbf p)=e^{i\eta\hat{\mathbf p}\cdot\mathbf K},\qquad
u_s(\mathbf p)=D(\mathbf p)u_s(0),\quad
v_s(\mathbf p)=D(\mathbf p)v_s(0).
\end{gathered}
\tag{38.6}
$$

指数的方向沿用第2节的$\omega_{i0}=\eta\hat p_i$约定。要算出这个矩阵，只需用$(\hat{\mathbf p}\cdot\boldsymbol\sigma)^2=I_2$把偶次幂和奇次幂分开：偶次幂留下单位阵，奇次幂留下同一个泡利矩阵组合，两个级数分别成为双曲余弦和双曲正弦，因而

<span id="eq:c38-boost-blocks"></span>

$$
D(\mathbf p)=
\begin{pmatrix}
\cosh\frac\eta2-\hat{\mathbf p}\cdot\boldsymbol\sigma\sinh\frac\eta2&0\\
0&\cosh\frac\eta2+\hat{\mathbf p}\cdot\boldsymbol\sigma\sinh\frac\eta2
\end{pmatrix}.
\tag{38.7}
$$

每个块都是厄米矩阵，故$D^\dagger=D$；将$\eta\to-\eta$则得到逆矩阵。在$\mathbf p=0$处取$D=I_4$。还可以消去快度，将四个旋量直接写成动量分量的函数。由半角公式，

$$
\sqrt m\cosh\frac\eta2=\sqrt{\frac{\omega+m}{2}},\qquad
\sqrt m\sinh\frac\eta2=\frac{|\mathbf p|}{\sqrt{2(\omega+m)}}.
$$

记$r=\omega+m$、$p_\pm=p_x\pm ip_y$、$N_p=\sqrt{2r}$，则$\sqrt m$乘上推动的上下两块，分别成为$(rI_2-\mathbf p\cdot\boldsymbol\sigma)/N_p$和$(rI_2+\mathbf p\cdot\boldsymbol\sigma)/N_p$。将它们作用于$e_s$及$\eta_s$，得到

<span id="eq:c38-explicit-spinors"></span>

$$
\begin{gathered}
u_+(\mathbf p)=\frac1{N_p}
\begin{pmatrix}r-p_z\\-p_+\\r+p_z\\p_+\end{pmatrix},
\qquad
u_-(\mathbf p)=\frac1{N_p}
\begin{pmatrix}-p_-\\r+p_z\\p_-\\r-p_z\end{pmatrix},\\
v_+(\mathbf p)=\frac1{N_p}
\begin{pmatrix}-p_-\\r+p_z\\-p_-\\-r+p_z\end{pmatrix},
\qquad
v_-(\mathbf p)=\frac1{N_p}
\begin{pmatrix}-r+p_z\\p_+\\r+p_z\\p_+\end{pmatrix}.
\end{gathered}
$$

在$\mathbf p=0$时，$r=2m$、$N_p=2\sqrt m$，四列回到[（38.3）](#eq:c38-rest-spinors)。固定非零三动量而令$m\to0$时，分母仍然非零，因而这套基也有连续的无质量极限。

列旋量的推动已经求出，接着要确定它的带横线行如何变换。为统一处理这种伴随运算，对一般矩阵定义狄拉克伴随：

<span id="eq:c38-matrix-adjoint"></span>

$$
\bar A\equiv\beta A^\dagger\beta,\qquad
\overline{AB}=\bar B\bar A,\qquad
\overline{cA}=c^*\bar A.
\tag{38.8}
$$

在两个因子之间插入$\beta^2=I_4$，就能得到这里的乘积规则：狄拉克伴随同时反转乘积的次序，并共轭数值系数。在所用的外尔基中，$(\gamma^0)^\dagger=\gamma^0$、$(\gamma^i)^\dagger=-\gamma^i$，而$\beta$与空间 $\gamma$矩阵反对易，故有$\bar\gamma^\mu=\gamma^\mu$。再对$S^{\mu\nu}=i[\gamma^\mu,\gamma^\nu]/4$作伴随，系数$i$的共轭与对易子次序的反转各贡献一个负号，因而$\bar S^{\mu\nu}=S^{\mu\nu}$。最后，$\gamma_5^\dagger=\gamma_5$和$\{\beta,\gamma_5\}=0$给出$\bar\gamma_5=-\gamma_5$。将这些规则用于乘积，还得到以下三组自伴随组合：

<span id="eq:c38-self-adjoint-combinations"></span>

$$
\begin{aligned}
\overline{i\gamma_5}&=(-i)(-\gamma_5)=i\gamma_5,\\
\overline{\gamma^\mu\gamma_5}
&=-\gamma_5\gamma^\mu=\gamma^\mu\gamma_5,\\
\overline{i\gamma_5S^{\mu\nu}}
&=(-i)S^{\mu\nu}(-\gamma_5)=i\gamma_5S^{\mu\nu}.
\end{aligned}
\tag{38.9}
$$

最后一式还用了$\gamma_5$与两个 $\gamma$矩阵的乘积对易。对于推动生成元，特别有$\bar K^j=K^j$；将指数展开后逐项作伴随，数值系数的共轭使指数中的号反转，于是

<span id="eq:c38-boost-bars"></span>

$$
\bar D=e^{-i\eta\hat{\mathbf p}\cdot\mathbf K}=D^{-1},\qquad
\bar u_s(\mathbf p)=\bar u_s(0)D^{-1},\quad
\bar v_s(\mathbf p)=\bar v_s(0)D^{-1}.
\tag{38.10}
$$

行旋量右乘逆推动矩阵，因而把行与列缩并成$\bar u u$这类量时，两个推动矩阵会相消。行旋量也满足相应的在壳方程：对列方程取厄米共轭，再右乘$\beta$，并用$\overline{\slashed p}=\slashed p$整理矩阵次序，得到

<span id="eq:c38-bar-equations"></span>

$$
\bar u_s(\mathbf p)(\slashed p+m)=0,\qquad
\bar v_s(\mathbf p)(-\slashed p+m)=0.
\tag{38.11}
$$

<span id="c38-bilinears"></span>

## 归一、戈登恒等式和正交关系

先求同动量的标量内积。行与列之间的$D^{-1}D$相消，计算便退回已经固定的静止基。由$e_{s'}^\dagger e_s=\eta_{s'}^\dagger\eta_s=\delta_{s's}$可知，$\bar u_{s'}u_s$的上、下块给出两个同号贡献，$\bar v_{s'}v_s$给出两个负贡献，而$\bar u_{s'}v_s$和$\bar v_{s'}u_s$中的上下块相互抵消。四类内积由此成为

<span id="eq:c38-scalar-products"></span>

$$
\begin{aligned}
\bar u_{s'}(\mathbf p)u_s(\mathbf p)&=2m\delta_{s's},&
\bar v_{s'}(\mathbf p)v_s(\mathbf p)&=-2m\delta_{s's},\\
\bar u_{s'}(\mathbf p)v_s(\mathbf p)&=0,&
\bar v_{s'}(\mathbf p)u_s(\mathbf p)&=0.
\end{aligned}
\tag{38.12}
$$

接下来求带一个 $\gamma$矩阵的双线性。戈登恒等式（Gordon identity）将$\gamma^\mu$双线性改写成动量与自旋矩阵两部分，使这两种贡献各自显现出来。令$p,p'$都位于同一个质量壳上，先按克利福德代数把矩阵乘积分成反对易与对易两部分：

<span id="eq:c38-gordon-algebra"></span>

$$
\begin{aligned}
\gamma^\mu\slashed p
&=\frac12\{\gamma^\mu,\slashed p\}+\frac12[\gamma^\mu,\slashed p]
=-p^\mu-2iS^{\mu\nu}p_\nu,\\
\slashed p'\gamma^\mu
&=\frac12\{\gamma^\mu,\slashed p'\}-\frac12[\gamma^\mu,\slashed p']
=-p'^\mu+2iS^{\mu\nu}p'_\nu.
\end{aligned}
\tag{38.13}
$$

将两式相加，记$G^\mu=(p'+p)^\mu-2iS^{\mu\nu}(p'-p)_\nu$，就有$\gamma^\mu\slashed p+\slashed p'\gamma^\mu=-G^\mu$。把这个恒等式夹在$\bar u_{s'}(\mathbf p')$与$u_s(\mathbf p)$之间，右作用的$\slashed p$和左作用的$\slashed p'$都可由在壳方程换成$-m$，所以左边变为$-2m\bar u'\gamma^\mu u$。若夹在$v$旋量之间，两处则各给$+m$。分别消去等式两侧共同的负号，就得到两条戈登恒等式：

<span id="eq:c38-gordon"></span>

$$
\begin{aligned}
2m\bar u_{s'}(\mathbf p')\gamma^\mu u_s(\mathbf p)
 &=\bar u_{s'}(\mathbf p')G^\mu u_s(\mathbf p),\\
-2m\bar v_{s'}(\mathbf p')\gamma^\mu v_s(\mathbf p)
 &=\bar v_{s'}(\mathbf p')G^\mu v_s(\mathbf p).
\end{aligned}
\tag{38.14}
$$

其中，对流型的$(p'+p)^\mu$项与含动量转移的自旋项已经分开。当$p'=p$时，自旋项消失，再用[（38.12）](#eq:c38-scalar-products)的标量归一，便得到同动量关系：

<span id="eq:c38-vector-products"></span>

$$
\bar u_{s'}(\mathbf p)\gamma^\mu u_s(\mathbf p)
=\bar v_{s'}(\mathbf p)\gamma^\mu v_s(\mathbf p)
=2p^\mu\delta_{s's}.
\tag{38.15}
$$

取$\mu=0$，由$\beta\gamma^0=I_4$可知，$u_{s'}^\dagger u_s=v_{s'}^\dagger v_s=2\omega\delta_{s's}$。通常内积的范数因而保持为正；前面$\bar v v$中的负号来自伴随定义里的$\beta$。

正则量子化时还会遇到同一空间傅里叶波数的两支模式，需要求它们在反向三动量处的混合内积。其中$-\mathbf p$只反转空间动量，能量仍取$\omega>0$。由[（38.7）](#eq:c38-boost-blocks)可知$D(-\mathbf p)=D(\mathbf p)^{-1}$，再用$D^\dagger=D$，推动矩阵又一次相消，留下静止旋量的两块抵消：

<span id="eq:c38-opposite-momenta"></span>

$$
\begin{aligned}
\bar u_{s'}(\mathbf p)\gamma^0v_s(-\mathbf p)
&=u_{s'}^\dagger(0)D^\dagger(\mathbf p)D(-\mathbf p)v_s(0)\\
&=m(e_{s'}^\dagger\eta_s-e_{s'}^\dagger\eta_s)=0,\\
\bar v_{s'}(\mathbf p)\gamma^0u_s(-\mathbf p)
&=m(\eta_{s'}^\dagger e_s-\eta_{s'}^\dagger e_s)=0.
\end{aligned}
\tag{38.16}
$$

也可从[上一节的能量矩阵](/posts/srednicki-37/#eq:c37-initial-data)看出这种正交性。$h(\mathbf p)=\gamma^0\gamma^i p_i+m\gamma^0$是厄米矩阵，且$h u_s(\mathbf p)=\omega u_s(\mathbf p)$、$h v_s(-\mathbf p)=-\omega v_s(-\mathbf p)$。同一个矩阵元$u_{s'}^\dagger h v_s$从左作用和从右作用分别给$+\omega u_{s'}^\dagger v_s$与$-\omega u_{s'}^\dagger v_s$，所以$2\omega u_{s'}^\dagger v_s=0$。因$\omega>0$，混合内积为零；取伴随并反向动量就得到另一式。[第 39 节](/posts/srednicki-39/#c39)将借助这种正交性分离两套模式系数。

<span id="c38-spin-sums"></span>

## 自旋求和

计算散射概率时，往往需要对末态自旋求和，并对未极化的初态自旋取平均，由此会出现$\sum_s u_s\bar u_s$和$\sum_s v_s\bar v_s$。这里相乘的是列与行，结果是$4\times4$矩阵。仍从静止系开始：利用$\sum_s e_s e_s^\dagger=\sum_s\eta_s\eta_s^\dagger=I_2$逐块相乘，得到

<span id="eq:c38-rest-sums"></span>

$$
\begin{aligned}
\sum_su_s(0)\bar u_s(0)
&=m\begin{pmatrix}I_2&I_2\\I_2&I_2\end{pmatrix}
=m\gamma^0+mI_4,\\
\sum_sv_s(0)\bar v_s(0)
&=m\begin{pmatrix}-I_2&I_2\\I_2&-I_2\end{pmatrix}
=m\gamma^0-mI_4.
\end{aligned}
\tag{38.17}
$$

若改选一个归一的自旋基，两个基矢之间只发生幺正混合，而求和中的混合矩阵与其伴随相消。因此，对完整自旋基的求和消除了量子化轴的选择。将上述静止结果推动到一般动量时，列左乘$D$，行右乘$D^{-1}$；代入[（38.7）](#eq:c38-boost-blocks)的块矩阵相乘，便有

<span id="eq:c38-boost-gamma0"></span>

$$
\begin{aligned}
D\gamma^0D^{-1}
&=\begin{pmatrix}0&e^{-\eta\hat{\mathbf p}\cdot\boldsymbol\sigma}\\
e^{+\eta\hat{\mathbf p}\cdot\boldsymbol\sigma}&0\end{pmatrix}\\
&=\gamma^0\cosh\eta-\hat p_i\gamma^i\sinh\eta
=-\frac{\slashed p}{m}.
\end{aligned}
\tag{38.18}
$$

用这个结果代换[（38.17）](#eq:c38-rest-sums)中经推动的时间 $\gamma$矩阵，质量项保持不变，就得到协变自旋求和：

<span id="eq:c38-spin-sums"></span>

$$
\sum_su_s(\mathbf p)\bar u_s(\mathbf p)=-\slashed p+m,\qquad
\sum_sv_s(\mathbf p)\bar v_s(\mathbf p)=-\slashed p-m.
\tag{38.19}
$$

右侧矩阵的质量维数为1，与$[u]=[v]=1/2$相合。左乘相应的在壳狄拉克算符时得到零，说明其像位于所需的解空间；作用在同类旋量上时，又分别给出$+2m u_s$、$-2m v_s$，与[（38.12）](#eq:c38-scalar-products)的归一一致。因此，这些求和矩阵与相应投影矩阵之间还相差一个归一因子。

<span id="c38-polarization"></span>

## 固定自旋的协变投影

若实验指定了自旋方向，就需要从完整求和中选出单个$u_s\bar u_s$或$v_s\bar v_s$。在静止系可以直接按自旋本征值筛选，利用$S_z$写成

<span id="eq:c38-rest-projectors"></span>

$$
\frac12(1+2sS_z)u_{s'}(0)=\delta_{ss'}u_{s'}(0),\qquad
\frac12(1-2sS_z)v_{s'}(0)=\delta_{ss'}v_{s'}(0).
\tag{38.20}
$$

例如，第一式作用后的系数是$(1+ss')/2$；第二式虽然使用相反的号，但$v$列的自旋本征值也相反，因而仍给同一个系数。要把这种选择推广到一般参考系，动量和自旋量子化轴应一同推动。为此，利用[第36节](/posts/srednicki-36/#c36-chirality)定义的$\gamma_5=i\gamma^0\gamma^1\gamma^2\gamma^3=\operatorname{diag}(-I_2,I_2)$，把自旋矩阵改写为$S_z=-\gamma_5\gamma^3\gamma^0/2$。再以$z_0^\mu=(0,0,0,1)$表示静止自旋轴，以$p_0^\mu=(m,\mathbf0)$表示静止动量，上式就成为$S_z=\gamma_5\slashed z_0\slashed p_0/(2m)$。两者作同一个推动后，得到

<span id="eq:c38-transported-spin"></span>

$$
S_z(\mathbf p)\equiv D S_zD^{-1}
=\frac1{2m}\gamma_5\slashed z\slashed p,\qquad
z^\mu=\Lambda^\mu{}_\nu z_0^\nu,\qquad
z^2=1,\quad z\cdot p=0.
\tag{38.21}
$$

这个算符随静止自旋轴一起变换；经过一般方向的推动后，它与原来沿固定坐标轴定义的矩阵$S^{12}$通常不同。具体采用[（38.6）](#eq:c38-boost)的不附加转动的推动时，自旋轴变为$z^0=p_z/m$、$\mathbf z=\hat{\mathbf z}+p_z\mathbf p/[m(\omega+m)]$。空间部分由推动矩阵$I+(\cosh\eta-1)\hat{\mathbf p}\hat{\mathbf p}^T$作用于$\hat{\mathbf z}$得到，而轴的单位长度及其与动量的正交性由洛伦兹变换保持。

再让这个算符作用于两支旋量。在$u$上，[（38.21）](#eq:c38-transported-spin)最右侧的$\slashed p$给出$-m$；在$v$上则给$+m$，恰好补偿[（38.20）](#eq:c38-rest-projectors)中相反的号。于是，可以用同一个协变矩阵选择两套旋量中的自旋标签：

<span id="eq:c38-spin-projector"></span>

$$
\begin{gathered}
\Pi_s(z)=\frac12(1-s\gamma_5\slashed z),\\
\Pi_s(z)u_{s'}(\mathbf p)=\delta_{ss'}u_{s'}(\mathbf p),\qquad
\Pi_s(z)v_{s'}(\mathbf p)=\delta_{ss'}v_{s'}(\mathbf p).
\end{gathered}
\tag{38.22}
$$

由于$(\gamma_5\slashed z)^2=-\slashed z^{\,2}=z^2=1$，确有$\Pi_s^2=\Pi_s$。此外，$[\gamma_5\slashed z,\slashed p]
=\gamma_5\{\slashed z,\slashed p\}=-2(z\cdot p)\gamma_5=0$，说明自旋选择与频率支的选择相容。因而可以在[（38.19）](#eq:c38-spin-sums)的左侧乘$\Pi_s$，使完整求和只留下一个$s$：

<span id="eq:c38-polarized-sums"></span>

$$
\begin{aligned}
u_s(\mathbf p)\bar u_s(\mathbf p)
&=\frac12(1-s\gamma_5\slashed z)(-\slashed p+m),\\
v_s(\mathbf p)\bar v_s(\mathbf p)
&=\frac12(1-s\gamma_5\slashed z)(-\slashed p-m).
\end{aligned}
\tag{38.23}
$$

<span id="c38-helicity"></span>

## 极端相对论极限、螺旋度与手征

固定自旋的外积在高能时会简化，显露出自旋方向与左右手场分量的关系。先取$\mathbf p$沿正第三轴，使动量平行于原来的量子化轴。此时动量和自旋轴写为

<span id="eq:c38-collinear-axis"></span>

$$
\frac{p^\mu}{m}=(\cosh\eta,0,0,\sinh\eta),\qquad
z^\mu=(\sinh\eta,0,0,\cosh\eta).
\tag{38.24}
$$

第二式来自静止轴$(0,0,0,1)$的推动，满足$z^2=1$和$z\cdot p=0$，而轴的正负方向仍由静止初值固定。为判断高能时能否用动量近似自旋轴，先精确算出两个四矢量之差：

<span id="eq:c38-ultrarelativistic-parameter"></span>

$$
z^\mu-\frac{p^\mu}{m}=e^{-\eta}(-1,0,0,1),\qquad
e^{-\eta}=\frac{m}{\omega+|\mathbf p|}.
\tag{38.25}
$$

这个精确差式确定了近似的误差阶。在$\eta\gg1$时，可以用$\slashed p/m$近似$\slashed z$。不过，外积右侧还有在壳矩阵，应先完成矩阵乘积，再按质量展开，这样才能同时保留两支的正确符号。利用在壳条件，分别得到

<span id="eq:c38-onshell-ultrarelativistic"></span>

$$
\begin{aligned}
\frac{\slashed p}{m}(-\slashed p+m)
&=-m+\slashed p=-(-\slashed p+m),\\
\frac{\slashed p}{m}(-\slashed p-m)
&=-m-\slashed p=+(-\slashed p-m).
\end{aligned}
\tag{38.26}
$$

将这两式代回[（38.23）](#eq:c38-polarized-sums)，再相对于$\slashed p$略去质量项，就得到领先近似：

<span id="eq:c38-chiral-limit"></span>

$$
\begin{aligned}
u_s\bar u_s&=\frac12(1+s\gamma_5)(-\slashed p)+O(m),\\
v_s\bar v_s&=\frac12(1-s\gamma_5)(-\slashed p)+O(m).
\end{aligned}
\tag{38.27}
$$

两式保留了矩阵元素中$O(\omega)$的领先项，相对略去$O(m/\omega)$的部分；后者包括质量项本身，以及[（38.25）](#eq:c38-ultrarelativistic-parameter)乘到$O(\omega)$外积上产生的修正。若固定非零三动量后取$m\to0$，这些误差便趋于零。旋量也保持有限，因为静止旋量中的$\sqrt m$与推动中的$e^{\eta/2}$合成了有限的归一。在壳方程、内积及完整自旋求和因此可连续延伸到$m=0$：标量内积趋于零，通常内积仍为$2|\mathbf p|$，而[（38.27）](#eq:c38-chiral-limit)在动量与自旋轴对齐的螺旋度基中成为精确关系。

螺旋度（helicity）是粒子的角动量沿其动量方向的分量。本节依$+1/2$、$-1/2$分别称粒子为右手、左手。沿第三轴的推动与$S_z$对易，所以[（38.4）](#eq:c38-mode-spin)中两类产生算符的物理自旋标签仍是$s/2$；与之相配的$v_s$列，其矩阵自旋本征值却是$-s/2$。这一区别决定了反粒子的螺旋度怎样对应到场的手征分量。由[（38.7）](#eq:c38-boost-blocks)可直接看一个例子：

<span id="eq:c38-positive-helicity-columns"></span>

$$
u_+(\mathbf p)=
\begin{pmatrix}\sqrt{\omega-|\mathbf p|}\\0\\
\sqrt{\omega+|\mathbf p|}\\0\end{pmatrix},
\qquad
v_+(\mathbf p)=
\begin{pmatrix}0\\\sqrt{\omega+|\mathbf p|}\\
0\\-\sqrt{\omega-|\mathbf p|}\end{pmatrix}.
\tag{38.28}
$$

两列分别配在$b_+$和$d_+^\dagger$前，相应产生算符的粒子标签都为正螺旋度。但在$m\to0$时，$u_+$只留在右手外尔块，$v_+$只留在左手外尔块。由此可见，右手外尔场湮灭正螺旋度粒子、产生负螺旋度反粒子；左手外尔场的这两种螺旋度则相反。

投影式选择的是场的手征分量，产生算符的标签则指粒子螺旋度。例如，$v_-$位于右手场块，但配套的$d_-^\dagger$产生负螺旋度反粒子。对于有质量粒子，螺旋度还会随参考系改变，左右手场块则始终按$\gamma_5$定义。

<span id="c38-discrete"></span>

## 动量反向、电荷共轭和相位关系

最后，为后面的离散对称性准备几组旋量恒等式。它们都可以从已固定相位的静止旋量出发，再用推动推广。先考虑动量反向：静止系满足$\beta u_s(0)=u_s(0)$、$\beta v_s(0)=-v_s(0)$，而$\beta$与$K^j$反对易，所以有$\beta D(\mathbf p)=D(-\mathbf p)\beta$。将它用于两支旋量，逐步写出动量反向的关系：

<span id="eq:c38-momentum-reversal"></span>

$$
\begin{aligned}
u_s(-\mathbf p)&=D(-\mathbf p)u_s(0)
=\beta D(\mathbf p)\beta u_s(0)=+\beta u_s(\mathbf p),\\
v_s(-\mathbf p)&=D(-\mathbf p)v_s(0)
=\beta D(\mathbf p)\beta v_s(0)=-\beta v_s(\mathbf p).
\end{aligned}
\tag{38.29}
$$

<span id="c38-charge"></span>

### 电荷共轭配对

再考虑两种频率支之间的共轭联系。采用[第36节](/posts/srednicki-36/#c36-charge-conjugation)定义的电荷共轭矩阵$\mathcal C$：

<span id="eq:c38-charge-matrix"></span>

$$
\mathcal C=\begin{pmatrix}
0&-1&0&0\\1&0&0&0\\0&0&0&1\\0&0&-1&0
\end{pmatrix}=\operatorname{diag}(E,-E).
\tag{38.30}
$$

它的转置、厄米共轭及相似变换性质为$\mathcal C^T=\mathcal C^\dagger=\mathcal C^{-1}=-\mathcal C$、$\beta\mathcal C=-\mathcal C\beta$和$\mathcal C^{-1}\gamma^\mu\mathcal C=-(\gamma^\mu)^T$，逐块推导见[第36节](/posts/srednicki-36/#c36-charge-conjugation)。先将[（38.3）](#eq:c38-rest-spinors)、[（38.5）](#eq:c38-rest-bars)的静止行列代入，算得$\mathcal C\bar u_s(0)^T=\sqrt m(Ee_s,-Ee_s)^T=v_s(0)$；再用$E\eta_s=E^2e_s=-e_s$，就有$\mathcal C\bar v_s(0)^T=u_s(0)$。这正说明开始时的相位选择让同标签的两支旋量配成一对。

要让这一配对在推动后仍然成立，还须把共轭矩阵移过转置的推动矩阵。先对生成元计算，保持转置时的乘积次序：

<span id="eq:c38-charge-boost"></span>

$$
\begin{aligned}
\mathcal C^{-1}K^j\mathcal C
&=\frac i2(\gamma^j)^T(\gamma^0)^T
=\frac i2(\gamma^0\gamma^j)^T
=-(K^j)^T,\\
\mathcal C(D^{-1})^T\mathcal C^{-1}&=D.
\end{aligned}
\tag{38.31}
$$

将第一式代入指数的幂级数，就得到第二式；这里作的是转置，数值系数$i$保持不变。于是，对推动后的行旋量取转置，再左乘$\mathcal C$，便可把逆推动换成列所需的正向推动，得到一般动量处的共轭配对：

<span id="eq:c38-charge-pairing"></span>

$$
\begin{aligned}
\mathcal C\bar u_s(\mathbf p)^T
&=\mathcal C(D^{-1})^T\bar u_s(0)^T
=D\mathcal C\bar u_s(0)^T=v_s(\mathbf p),\\
\mathcal C\bar v_s(\mathbf p)^T
&=D\mathcal C\bar v_s(0)^T=u_s(\mathbf p).
\end{aligned}
\tag{38.32}
$$

这给出了第37节所讨论的同标签配对基。对于马约拉纳场，将此式代入[（37.38）](/posts/srednicki-37/#eq:c37-majorana-modes)，两套系数之间的约束就化为$d_s=b_s$，[第39节](/posts/srednicki-39/#c39-majorana)据此建立单套费米产生、湮灭算符。

还可以把这种配对写成单纯复共轭的形式。本基中的$\beta,\mathcal C$均为实矩阵，又有$\bar u^{T*}=\bar u^\dagger=\beta u$，所以对[（38.32）](#eq:c38-charge-pairing)逐项取复共轭，便得到纯复共轭形式：

<span id="eq:c38-complex-conjugation"></span>

$$
u_s^*(\mathbf p)=\mathcal C\beta v_s(\mathbf p),\qquad
v_s^*(\mathbf p)=\mathcal C\beta u_s(\mathbf p).
\tag{38.33}
$$

另一种联系来自手征矩阵。将$\eta_s=s e_{-s}$代入[（38.3）](#eq:c38-rest-spinors)，在静止系可得$\gamma_5u_s(0)=s v_{-s}(0)$、$\gamma_5v_s(0)=-s u_{-s}(0)$。$\gamma_5$与每个$K^j$对易，因为后者含有两个 $\gamma$矩阵；因此也与推动矩阵对易，这两条关系可以直接推广为

<span id="eq:c38-gamma5-pairing"></span>

$$
\gamma_5u_s(\mathbf p)=s v_{-s}(\mathbf p),\qquad
\gamma_5v_s(\mathbf p)=-s u_{-s}(\mathbf p).
\tag{38.34}
$$

手征矩阵的作用由此化成两支旋量之间的标签反向。再依次结合动量反向、复共轭和这一配对，就能得到时间反演所需的组合关系：

<span id="eq:c38-time-reversal-pairing"></span>

$$
\begin{aligned}
u_{-s}^*(-\mathbf p)
&=\mathcal C\beta v_{-s}(-\mathbf p)
=-\mathcal C v_{-s}(\mathbf p)
=-s\mathcal C\gamma_5u_s(\mathbf p),\\
v_{-s}^*(-\mathbf p)
&=\mathcal C\beta u_{-s}(-\mathbf p)
=+\mathcal C u_{-s}(\mathbf p)
=-s\mathcal C\gamma_5v_s(\mathbf p).
\end{aligned}
\tag{38.35}
$$

动量反向的关系将用于宇称，同标签的共轭配对将用于电荷共轭，而同时反转动量、自旋标签并取复共轭的最后一组将用于时间反演。三组关系中的相位都已由静止旋量的选择确定，后续讨论可以直接沿用。

---

[← 第 37 节](/posts/srednicki-37/) · [章节地图](/srednicki/) · [第 39 节 →](/posts/srednicki-39/)
