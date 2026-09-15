---
title: 'Srednicki §32 连续对称性的自发破缺'
date: 2026-09-14
category: 笔记
tags: [物理, 量子场论, Srednicki]
series: 'Srednicki QFT'
srednickiSections: [32]
hideFromHome: true
draft: false
---

<span id="c32"></span>

实标量的反射对称性把两个真空互换；连续对称性破缺时，最低能量的场值则组成一条连续轨道。让场值沿这条轨道缓慢地随空间变化，不会增加势能，只需付出梯度能。因此波长越长，激发能量就可以越低。这提示我们，连续的真空族应当伴随无质量的激发。本节先在复标量模型中求出这种Goldstone玻色子，说明它的无质量性怎样由对称性维持，再把结果推广到$N$个实标量。

以下在四维洛伦兹不变真空中讨论连续的整体内部对称性，取$\lambda>0$。为分清树级展开与量子真空，将树级幅度记为$v_0$，含圈修正的一点函数幅度记为$v$。

<span id="c32-u1"></span>

## 最低点组成的圆

从第22节的复标量模型出发。其拉格朗日量及整体相位变换为

<span id="eq:c32-u1-model"></span>

$$
\mathcal L=-\partial^\mu\varphi^\dagger\partial_\mu\varphi
-m^2\varphi^\dagger\varphi
-\frac{\lambda}{4}(\varphi^\dagger\varphi)^2,\qquad
\varphi\longmapsto e^{-i\alpha}\varphi .
\tag{32.1}
$$

共轭场取得相反相位，而$\alpha$是常数，导数不作用于相位，所以动能与势的每一项都保持不变。现在把质量平方取为负值，寻找新的最低点。由于势只依赖场的模，令$r^2=2\varphi^\dagger\varphi$，可把它配方为

<span id="eq:c32-minimum-circle"></span>

$$
V(r)=\frac12m^2r^2+\frac{\lambda}{16}r^4
=\frac{\lambda}{16}(r^2-v_0^2)^2
-\frac{\lambda v_0^4}{16},\qquad
v_0^2=-\frac{4m^2}{\lambda}>0 .
\tag{32.2}
$$

比较配平方前后的二次项，就确定了$v_0^2$。这里出现的系数是4；上一节单实场的四次项取$\lambda/24$，相应系数则是6，两者来自耦合定义的不同。在允许均匀场的边界条件下，梯度能非负，使平方项为零并取空间上均匀的相位，就得到最低能量配置

<span id="eq:c32-phase-orbit"></span>

$$
\varphi_\theta=\frac{v_0}{\sqrt2}e^{-i\theta},
\qquad \theta\in\mathbb R/(2\pi\mathbb Z),\qquad
\theta\longmapsto\theta+\alpha .
\tag{32.3}
$$

U(1)把这些最低点彼此联系起来，势只依赖半径，沿圆的角向移动因而不需要势能。这里保留$1/\sqrt2$的归一，是为了在$\varphi=(\varphi_1+i\varphi_2)/\sqrt2$中让两个实场分别具有$-\frac12(\partial\varphi_i)^2$的动能。

量子论中的选相仍沿第30节的次序进行：先用一个很小的定向源选出方向，再取空间体积无穷，最后撤去源。在破缺相中，由此定义的真空族及其序参量为

<span id="eq:c32-quantum-vacua"></span>

$$
\langle\theta|\varphi(x)|\theta\rangle
=\frac v{\sqrt2}e^{-i\theta}.
\tag{32.4}
$$

这里定义的是精确幅度$v$，其树级值才是$v_0$。不同相具有不同的宏观平均场；只要平均区域扩大时涨落趋于零，第30节的柯西–施瓦茨论证就说明两相正交。连续破缺的涨落中包含无质量模，它们的远距离关联须重新估计。下面将从[无质量模展开](#c32-charge-limit)求出平滑平均场方差的 $R^{-2}$ 行为。相位的周期也须同时保留，所谓不同相是指$\theta$模$2\pi$不等。

<span id="c32-cartesian"></span>

## 直角坐标中的两种激发

要看真空附近有哪些粒子，先选$\theta=0$，把两个实涨落场写成

<span id="eq:c32-cartesian"></span>

$$
\varphi=\frac1{\sqrt2}(v_0+a+ib),\qquad
2\varphi^\dagger\varphi=(v_0+a)^2+b^2 .
\tag{32.5}
$$

此处$a,b$是实场。把这个表达式代回动能，两个虚交叉项相消，留下各自标准归一的实场动能。势中的平方则按涨落场展开为

<span id="eq:c32-cartesian-square"></span>

$$
\begin{aligned}
\relax[(v_0+a)^2+b^2-v_0^2]^2
&=(2v_0a+a^2+b^2)^2\\
&=4v_0^2a^2+4v_0a(a^2+b^2)+(a^2+b^2)^2.
\end{aligned}
\tag{32.6}
$$

将各项乘上$\lambda/16$并连同动能代回拉格朗日量，得到

<span id="eq:c32-cartesian-lagrangian"></span>

$$
\begin{aligned}
\mathcal L={}&-\frac12(\partial a)^2-\frac12(\partial b)^2
-\frac12M_0^2a^2\\
&-\frac{\lambda v_0}{4}a(a^2+b^2)
-\frac{\lambda}{16}(a^2+b^2)^2,\qquad
M_0^2=\frac{\lambda v_0^2}{2}=-2m^2 .
\end{aligned}
\tag{32.7}
$$

二次项直接区分了两种激发：$a$沿径向偏离最低圆，会受到势的恢复力；$b$沿切向运动，二次势为零，所以两者的树级质量分别为$M_0$和0。这个切向实场$b$就是直角坐标中的Goldstone场。

展开式也给出二者的相互作用，但从单项式读顶角时还要计入相同场的排列。例如$a^3$项乘$3!$，$ab^2$项只乘$2!$，而$a^2b^2$项乘$2!2!$，相应顶角为

<span id="eq:c32-cartesian-vertices"></span>

$$
\begin{aligned}
iV_{aaa}&=-\frac{3i\lambda v_0}{2},&
iV_{abb}&=-\frac{i\lambda v_0}{2},\\
iV_{aaaa}=iV_{bbbb}&=-\frac{3i\lambda}{2},&
iV_{aabb}&=-\frac{i\lambda}{2}.
\end{aligned}
\tag{32.8}
$$

这些顶角将用于比较不同的场坐标。特别是$abb$顶角允许径向激发衰变成两个无质量粒子，因此这里的$M_0$是树质量；含更高阶修正的径向激发应按第25节用共振的复极点描述。

<span id="c32-polar"></span>

## 极坐标使平坦方向显明

直角坐标已给出无质量场，极坐标则能把它与最低圆的角向运动直接对应起来。在圆附近的一个局部坐标片内，取$r=v_0+\rho>0$，场及其导数为

<span id="eq:c32-polar-derivative"></span>

$$
\varphi=\frac{v_0+\rho}{\sqrt2}e^{-i\chi/v_0},\qquad
\partial_\mu\varphi=
\frac{e^{-i\chi/v_0}}{\sqrt2}
\left[\partial_\mu\rho-i\left(1+\frac{\rho}{v_0}\right)\partial_\mu\chi\right].
\tag{32.9}
$$

导数与其共轭相乘时，径向导数和角向导数之间的虚交叉项相消；势依然只取决于半径。将两部分合并，得到

<span id="eq:c32-polar-lagrangian"></span>

$$
\begin{aligned}
\mathcal L={}&-\frac12(\partial\rho)^2
-\frac12\left(1+\frac{\rho}{v_0}\right)^2(\partial\chi)^2\\
&-\frac12M_0^2\rho^2
-\frac{\lambda v_0}{4}\rho^3-\frac{\lambda}{16}\rho^4 .
\end{aligned}
\tag{32.10}
$$

二次项给出的两种树质量与直角坐标相同，而势中完全没有$\chi$，平坦方向因而显明。原来的U(1)变换在这组坐标中成为

<span id="eq:c32-shift-symmetry"></span>

$$
\rho\longmapsto\rho,\qquad
\chi\longmapsto\chi+v_0\alpha,\qquad
\chi\sim\chi+2\pi v_0 .
\tag{32.11}
$$

位移幅度中的$v_0$来自角坐标的定义：指数中的$\chi/v_0$须增加相位参数$\alpha$，因此$\chi$增加$v_0\alpha$。$\chi$的质量维数为1，而$\alpha$无量纲，二者的量纲也由$v_0$联系。

角场虽然不出现在势中，仍会通过动能同径向场相互作用。展开角向动能的平方，两个相互作用项为

<span id="eq:c32-derivative-interactions"></span>

$$
\mathcal L_{\rho\chi}
=-\frac{\rho}{v_0}\partial_\mu\chi\,\partial^\mu\chi
-\frac{\rho^2}{2v_0^2}\partial_\mu\chi\,\partial^\mu\chi .
\tag{32.12}
$$

取$e^{ikx}$的逆傅里叶展开，两个导数贡献$-k_1\cdot k_2$。再对两个相同的$\chi$求导，得到$2!$；第二项还含两个$\rho$，另给$2!$。把这些因子与拉格朗日量系数相乘，以全部动量流入顶点的约定，得到

<span id="eq:c32-derivative-vertices"></span>

$$
iV_{\rho\chi\chi}=\frac{2i}{v_0}k_1\cdot k_2,\qquad
iV_{\rho\rho\chi\chi}=\frac{2i}{v_0^2}k_1\cdot k_2 .
\tag{32.13}
$$

用这些含动量的顶角，可以与直角坐标中的计算比较：设两条无质量腿的动量为$p_1,p_2$，径向树级运动学要求$(p_1+p_2)^2=-M_0^2$，于是$p_1\cdot p_2=-M_0^2/2$。第一个顶角因而化为

<span id="eq:c32-polar-cartesian-check"></span>

$$
\frac{2i}{v_0}p_1\cdot p_2
=-\frac{iM_0^2}{v_0}=-\frac{i\lambda v_0}{2},
\tag{32.14}
$$

它与直角坐标的$abb$顶角相等；两条$b$与$\chi$在线性关系中各有一个负号，相乘后也抵消了。这个例子说明，顶角在不同参数化下虽然看起来不同，代入相应运动学并比较同一激发时仍可对应。

<span id="c32-redefinition"></span>

### 换元时场、测度与物理量

为进一步说明这种对应，先写出两种坐标之间的精确关系：

<span id="eq:c32-coordinate-map"></span>

$$
a=(v_0+\rho)\cos(\chi/v_0)-v_0,\qquad
b=-(v_0+\rho)\sin(\chi/v_0).
\tag{32.15}
$$

在真空附近，其线性部分是$a=\rho$、$b=-\chi$，所以两种参数化具有相同的二次动能归一。非线性部分还会改变路径积分测度，对坐标关系逐项求导，局部雅可比矩阵为

<span id="eq:c32-jacobian"></span>

$$
\frac{\partial(a,b)}{\partial(\rho,\chi)}
=
\begin{pmatrix}
\cos\vartheta&-(r/v_0)\sin\vartheta\\
-\sin\vartheta&-(r/v_0)\cos\vartheta
\end{pmatrix},
\qquad
\det=-\frac r{v_0},\quad\vartheta=\frac{\chi}{v_0}.
\tag{32.16}
$$

行列式的绝对值是$1+\rho/v_0$，它与$\chi$无关。因此，在有限调节的路径积分中作此换元，须带入$\prod_x(1+\rho(x)/v_0)$。把这个乘积写成指数，会得到只依赖$\rho$的局部测度项；维数正则化中相应的形式系数$\delta^{(d)}(0)=\int d^dk/(2\pi)^d$按无尺度约定为零，用其他调节时则须保留该调节下的换元因子。在$r=0$处极坐标退化，所以固定真空附近的微扰只使用$r>0$的坐标片。

场重新定义前后的粒子质量和散射幅，可以用LSZ公式联系起来。可逆局部换元若同时作用于拉格朗日量、测度和算符插入，路径积分描述的仍是同一理论，谱中的能量与稳定粒子壳也就相同。不同插值场可以具有不同的单粒子重叠；这些重叠在多点函数的单粒子极点处逐腿出现，LSZ再按所用场的极点留数把它们除去，留下同一个物理散射幅。对于径向共振，则比较同一稳定态散射函数中的复极点。式[（32.14）](#eq:c32-polar-cartesian-check)展示的是这种对应的树级例子。

<span id="c32-goldstone"></span>

## 圈修正后的无质量方向

接下来考虑量子修正是否会给角场产生质量。先用式[（32.13）](#eq:c32-derivative-vertices)考察带两条外部$\chi$线的1PI图：每条外线进入顶角时都带一个外动量，所以相应自能具有$k_\mu k_\nu I^{\mu\nu}(k)$的形式。在保持常数位移对称性的调节和减除下，反项也不能含无导数的$\chi^2$项。保留这些动量因子并控制零动量极限，就得到

<span id="eq:c32-goldstone-selfenergy"></span>

$$
\boldsymbol\Delta_\chi(k^2)=\frac1{k^2-\Pi_\chi(k^2)-i0},
\qquad \Pi_\chi(0)=0 .
\tag{32.17}
$$

外动量因子保留到积分和减除完成后，再取受控的红外极限。对于本节的四维弱耦合破缺相，如果低动量二次项具有$k^2-\Pi_\chi(k^2)=K_\chi k^2+o(k^2)$的形式，并满足$0<K_\chi<\infty$，那么传播子就在原点有一个无质量简单极点，其留数为$\mathcal R_\chi=K_\chi^{-1}$。这把没有质量项与传播的无质量粒子联系起来。

同一结论也可以从量子作用量的对称性推导，不必逐图追踪外线。[第21节的变量替换](/posts/srednicki-21/#c21-symmetry)表明，在保持U(1)的测度和相容边界下，有

<span id="eq:c32-gamma-symmetry"></span>

$$
\Gamma[e^{-i\alpha}\varphi]=\Gamma[\varphi].
\tag{32.18}
$$

对于恒定场，量子作用量满足$\Gamma=-\int U$，所以真空使$\Gamma$驻定，并使$U$取最低能量。将对称性作用于这个势，就能得到沿真空轨道的约束。

现在在$\theta=0$的真空附近写平均场$\varphi=(v+\bar a+i\bar b)/\sqrt2$。无穷小U(1)变换给$\delta\bar a=\alpha\bar b$、$\delta\bar b=-\alpha(v+\bar a)$，代入势的不变性，便有

<span id="eq:c32-u1-potential-identity"></span>

$$
\bar b\,U_a-(v+\bar a)U_b=0.
\tag{32.19}
$$

要读出切向曲率，对$\bar b$求导，再令$\bar a=\bar b=0$，可得$U_a-vU_{bb}=0$。精确真空已经满足一点条件$U_a=0$，所以

<span id="eq:c32-transverse-curvature"></span>

$$
U_{bb}(v)=0\qquad(v\ne0).
\tag{32.20}
$$

这里正是利用了真空的一点函数归零，才把沿对称轨道的变化转成零曲率方向。若仍在未经修正的树驻点代入圈势，一点项会留下来，也就漏掉了上一节讨论的真空位移。

<span id="c32-ward-pole"></span>

### 守恒流中的无质量极点

除了考察曲率，还可以通过守恒流寻找与角向激发相耦合的物理态。[第22节](/posts/srednicki-22/)的流为 $j^\mu=-i\varphi^\dagger\overleftrightarrow{\partial^\mu}\varphi$。代入极坐标，记 $r=v_0+\rho$，两个乘积分别给出

<span id="eq:c32-current-products"></span>

$$
\begin{aligned}
\varphi^\dagger\partial^\mu\varphi
&=\frac r2\partial^\mu r-\frac{ir^2}{2v_0}\partial^\mu\chi,\\
(\partial^\mu\varphi^\dagger)\varphi
&=\frac r2\partial^\mu r+\frac{ir^2}{2v_0}\partial^\mu\chi.
\end{aligned}
$$

相减后径向导数消失，再乘 $-i$ 得到

<span id="eq:c32-polar-current"></span>

$$
j^\mu=-\frac{(v_0+\rho)^2}{v_0}\partial^\mu\chi,
\qquad
j^0=v_0\pi_\chi,\qquad
\pi_\chi=\left(1+\frac\rho{v_0}\right)^2\dot\chi.
$$

其中 $\pi_\chi$ 是正则动量。由等时正则对易子，有限支撑荷在局部插入处满足 $[Q,\chi]=-iv_0$。因此第22节的 Ward 恒等式用于角场时，接触项正比于位移幅度 $v_0$；相应的流—场关联函数及恒等式为

<span id="eq:c32-local-ward"></span>

$$
C^\mu_{j\chi}(k)=
\int d^4x\,e^{-ikx}\langle0|\mathrm Tj^\mu(x)\chi(0)|0\rangle,
\qquad
\partial_\mu\langle\mathrm Tj^\mu(x)\chi(0)\rangle
=-iv_0\delta^4(x).
\tag{32.21}
$$

流本身守恒，但微分时间序乘积时还会对时间序阶跃函数求导，留下上面的接触项。在傅里叶变换中分部积分，$\int e^{-ikx}\partial_\mu C^\mu=i k_\mu C^\mu(k)$，因此恒等式成为

<span id="eq:c32-longitudinal-ward"></span>

$$
k_\mu C^\mu_{j\chi}(k)=-v_0 .
\tag{32.22}
$$

在洛伦兹不变真空中，这个矢量—标量关联函数的矢量结构只能由$k^\mu$组成。与外动量收缩后既然要给出非零常数，纵向系数就须包含$1/k^2$奇性；关于$k$的局部多项式接触项本身不能提供这个极点。

为了识别它所代表的态，沿第13节在两算符之间插入物理态的谱展开。普通无质量极点的留数来自零质量单粒子态。将流矩阵元写成$\langle k|j^\mu(x)|0\rangle=ifk^\mu e^{-ikx}$，用常数$f$表示流与粒子的耦合强度。选择态的相位使$c_\chi=\langle k|\chi(0)|0\rangle>0$，关联函数的极点部分就为

<span id="eq:c32-current-pole-residue"></span>

$$
C^\mu_{j\chi}(k)\sim
-f c_\chi\frac{k^\mu}{k^2-i0},\qquad
f c_\chi=v_0 .
\tag{32.23}
$$

这个负号也与树级关系$j^\mu=-v_0\partial^\mu\chi$及$\langle\mathrm T\chi\chi\rangle=\boldsymbol\Delta_\chi/i$相符。恒等式由此把非零破缺幅度与非零的流—粒子耦合联系起来；如果有几个简并无质量态，则右式应由各态的重叠之和代替。在本节单一 U(1) 方向的弱耦合粒子描述中，$c_\chi^2=\mathcal R_\chi$，于是

<span id="eq:c32-decay-constant-normalization"></span>

$$
f=\frac{v_0}{\sqrt{\mathcal R_\chi}}
=v_0\left(1-\frac12\delta\mathcal R_\chi+\cdots\right),
\qquad \mathcal R_\chi=1+\delta\mathcal R_\chi+\cdots.
$$

树级流只需保留 $-v_0\partial^\mu\chi$。取通常归一的单粒子态，使 $\langle k|\chi(x)|0\rangle=e^{-ikx}$，便有 $\langle k|j^\mu(x)|0\rangle=iv_0k^\mu e^{-ikx}$，即 $f_{\rm tree}=v_0$。这里“衰变常数”表示流与粒子的耦合强度。对流矩阵元取散度，守恒性又给出 $fk^2=0$，所以非零的 $f$ 所耦合的这一粒子无质量。

圈修正中的流是按同一荷归一重整化的复合算符，其有限顶角与场留数一起满足 Ward 恒等式。角坐标中 $v_0$ 是定义 $\chi/v_0$ 的参数尺度；若作有限重标度 $\chi'=c\chi$，位移幅度与单粒子重叠都乘 $c$，它们的比值 $f$ 保持不变。改用直角场 $b$ 时，变分含 $-(v_0+a)$，接触项则由精确真空幅度 $v=v_0+\langle a\rangle$ 决定。

<span id="c32-charge-limit"></span>

## 破缺荷与宏观平均场

荷怎样联系不同相，可以先在指数和对易子有定义的共同域上计算。由 $[Q,\varphi]=-\varphi$，令 $F(\alpha)=e^{-i\alpha Q}\varphi e^{i\alpha Q}$，有

<span id="eq:c32-charge-exponential"></span>

$$
F'(\alpha)=-ie^{-i\alpha Q}[Q,\varphi]e^{i\alpha Q}=iF(\alpha),
\qquad F(0)=\varphi,
\qquad F(\alpha)=e^{i\alpha}\varphi.
$$

记 $U(\alpha)=e^{-i\alpha Q}$。作用后的态具有一点函数

<span id="eq:c32-charge-vacuum-orbit"></span>

$$
\langle\theta|U^\dagger\varphi U|\theta\rangle
=e^{-i\alpha}\langle\theta|\varphi|\theta\rangle
=\frac v{\sqrt2}e^{-i(\theta+\alpha)}.
$$

因此对称变换把 $\theta$ 相送到 $\theta+\alpha$ 相。如果自伴荷可作用于真空，且 $Q|0\rangle=0$，则 $\langle[Q,\varphi]\rangle=0$，与 $\langle[Q,\varphi]\rangle=-v/\sqrt2\ne0$ 矛盾。通常的记号 $Q|0\rangle\ne0$ 就表达了破缺对称性改变真空。

无限体积时，这个记号还涉及荷的极限。若不同角度的纯相正交，那么任意非零的小 $\alpha$ 都给 $\|U(\alpha)|0\rangle-|0\rangle\|^2=2$。这条真空轨道不强连续，因而不能由单相空间内的通常自伴荷指数生成。可以保留有限支撑荷，直接计算它在局部算符上的作用。

在四维自由 Goldstone 近似中，荷的极限与平均场的涨落都能由模展开求出。取实光滑紧支撑函数 $h$，使它在原点邻域等于 1，定义 $h_R(\mathbf x)=h(\mathbf x/R)$ 及

<span id="eq:c32-smeared-charge"></span>

$$
Q_R=v_0\int d^3x\,h_R(\mathbf x)\dot\chi(0,\mathbf x),
\qquad
\chi(x)=\int\frac{d^3k}{(2\pi)^3\,2|\mathbf k|}
\left(a_{\mathbf k}e^{ikx}+a^\dagger_{\mathbf k}e^{-ikx}\right).
$$

作用于真空时只留下产生项，时间导数给 $+i|\mathbf k|$。再用 $[a_{\mathbf k},a^\dagger_{\mathbf k'}]=(2\pi)^3\,2|\mathbf k|\delta^3(\mathbf k-\mathbf k')$，得到

<span id="eq:c32-charge-norm"></span>

$$
\begin{aligned}
\|Q_R|0\rangle\|^2
&=\frac{v_0^2}{2}\int\frac{d^3k}{(2\pi)^3}
 |\mathbf k|\,|\widetilde h_R(\mathbf k)|^2\\
&=\frac{v_0^2R^2}{2}\int\frac{d^3q}{(2\pi)^3}
 |\mathbf q|\,|\widetilde h(\mathbf q)|^2.
\end{aligned}
$$

第二步用 $\widetilde h_R(\mathbf k)=R^3\widetilde h(R\mathbf k)$，再令 $\mathbf q=R\mathbf k$。两个傅里叶幅度给 $R^6$，动量测度和能量分别给 $R^{-3}$、$R^{-1}$，最终留下 $R^2$。

若改为归一化的空间平均，取实光滑紧支撑函数 $g$ 满足 $\int d^3x\,g=1$，定义 $\bar\chi_R=R^{-3}\int d^3x\,g(\mathbf x/R)\chi(0,\mathbf x)$。相同的收缩不再含时间导数，所得方差为

<span id="eq:c32-mean-field-variance"></span>

$$
\operatorname{Var}(\bar\chi_R)
=\frac1{2R^2}\int\frac{d^3q}{(2\pi)^3}
 \frac{|\widetilde g(\mathbf q)|^2}{|\mathbf q|}
\longrightarrow0.
$$

两个积分的低动量径向测度分别为 $q^3dq$ 与 $q\,dq$，高动量则由平滑函数的傅里叶衰减控制。因此全空间荷作用于真空的范数增长，宏观平均场却越来越集中。在线性涨落近似下，直角场的平均值由有质量径向模和上述角模组成，两者的方差都趋于零；不同相的非零序参量差再通过 [第30节的重叠界](/posts/srednicki-30/#eq:c30-orthogonality-bound)给出正交性。

对完整理论的破缺判据，可以固定局部插入，取经适当时空平滑的截断荷，再考察 $\lim_{R\to\infty}\langle[Q_R,\varphi(x)]\rangle=-\langle\varphi(x)\rangle\ne0$。这一局部作用是守恒流与序参量的联系；上面的自由模计算则具体展示了它怎样与荷范数的红外增长共存。

<span id="c32-nonabelian"></span>

## SO(N)模型的破缺与残余群

复标量的例子有一个独立的角向方向；多个实场可以产生更多方向。取$N\ge2$个实场，考虑

<span id="eq:c32-son-model"></span>

$$
\mathcal L=-\frac12\partial^\mu\varphi_i\partial_\mu\varphi_i
-V(\varphi),\qquad
V=\frac12m^2\varphi_i\varphi_i
+\frac{\lambda}{16}(\varphi_i\varphi_i)^2 .
\tag{32.24}
$$

本段重复指标从1到$N$求和。每个内部坐标平面的旋转各有一个生成元；对每对$r<s$，沿用第24节的厄米生成元，写成

<span id="eq:c32-son-generators"></span>

$$
(T^{rs})_{ij}=-i\delta_{ir}\delta_{js}
+i\delta_{is}\delta_{jr},\qquad
\delta\varphi_i=-i\theta^aT^a_{ij}\varphi_j .
\tag{32.25}
$$

这些矩阵纯虚且反对称，共有$N(N-1)/2$个，$a$就是按上述指标对排列的编号。令$t^a=-iT^a$，则$t^a$为实反对称矩阵；由$\varphi_i t^a_{ij}\varphi_j=0$可知场的范数不变，同理动能也不变，所以式[（32.24）](#eq:c32-son-model)具有SO($N$)对称性。

寻找最低点及其小涨落，需要势的一、二阶导数：

<span id="eq:c32-son-hessian"></span>

$$
\begin{aligned}
V_i&=\left(m^2+\frac{\lambda}{4}\varphi_\ell\varphi_\ell\right)\varphi_i,\\
V_{ij}&=\left(m^2+\frac{\lambda}{4}\varphi_\ell\varphi_\ell\right)\delta_{ij}
+\frac{\lambda}{2}\varphi_i\varphi_j .
\end{aligned}
\tag{32.26}
$$

当$m^2<0$时，最低向量的长度固定为$v_0^2=-4m^2/\lambda$，方向则任意。SO($N$)可以把任何这样的方向转到最后一根坐标轴，故选$v_i=v_0\delta_{iN}$。把它代入二阶导数，最低点的质量矩阵为

<span id="eq:c32-son-masses"></span>

$$
\mathcal M^2_{ij}=\frac{\lambda}{2}v_i v_j
=M_0^2\delta_{iN}\delta_{jN}.
\tag{32.27}
$$

矩阵只有径向本征值$M_0^2$非零，另有$N-1$个横向零本征值。要看这些零模如何对应对称变换，计算真空期望值的变化：

<span id="eq:c32-vev-transformation"></span>

$$
\delta v_i=-i\theta^aT^a_{ij}v_j
=-i\theta^aT^a_{iN}v_0 .
\tag{32.28}
$$

若$T^av\ne0$，相应变换改变真空，这个方向的生成元称为破缺生成元；若$T^av=0$，则是未破缺的。在上述标准基中，两种作用分别为

<span id="eq:c32-broken-basis"></span>

$$
t^{rN}v=-v_0e_r\quad(r=1,\ldots,N-1),\qquad
t^{rs}v=0\quad(r<s<N).
\tag{32.29}
$$

第一组在末轴与各横向轴之间旋转真空，恰好给出质量矩阵的$N-1$个独立零方向；第二组只在前$N-1$个分量内部旋转，组成$\mathfrak{so}(N-1)$。其生成元数目为

<span id="eq:c32-unbroken-count"></span>

$$
\frac{N(N-1)}2-(N-1)=\frac{(N-1)(N-2)}2 .
\tag{32.30}
$$

有限变换也给出同一个残余群。满足$Rv=v$的正交矩阵只能写成$R=\operatorname{diag}(O,1)$；再由$\det R=1$，可得$O\in{\rm SO}(N-1)$。因此这个群的作用具体保留了最后一个分量，其生成元数目也与刚才的计数一致。

选相时沿第 $N$ 方向加入小源，并取保持 SO($N-1$) 的体积极限，剩余群便同时保持真空和序参量。由 [第24节的荷代数](/posts/srednicki-24/) $[\varphi_i,Q^a]=T^a_{ij}\varphi_j$，在荷可作用于真空且真空荷取零时，有

<span id="eq:c32-charge-order-parameter"></span>

$$
Q^a|0\rangle=0\quad\Longrightarrow\quad
(T^av)_i=\langle0|[\varphi_i,Q^a]|0\rangle=0.
$$

对于这里的残余群，$U_h|0\rangle=|0\rangle$ 反过来给出其生成元湮灭真空。破缺的 $rN$ 方向则改变序参量，在无限体积中按前面的局部截断荷判据理解。

下面把残余对称性直接写进涨落场的拉格朗日量。将势配平方、略去场无关常数，再令$\varphi_N=v_0+\rho$、$\varphi_r=\pi_r$，其中$r=1,\ldots,N-1$，得到

<span id="eq:c32-son-shifted"></span>

$$
\begin{aligned}
\mathcal L&=-\frac12(\partial\rho)^2-\frac12(\partial\pi_r)^2-V(\rho,\pi),\\
V(\rho,\pi)
&=\frac{\lambda}{16}(2v_0\rho+\rho^2+\pi_r\pi_r)^2\\
&=\frac{\lambda v_0^2}{4}\rho^2
+\frac{\lambda v_0}{4}\rho(\rho^2+\pi_r\pi_r)
+\frac{\lambda}{16}(\rho^2+\pi_r\pi_r)^2.
\end{aligned}
\tag{32.31}
$$

平方中的二次项、交叉项和四次项，分别产生第三行的$1/4,1/4,1/16$。在残余群下，$\rho$是标量，$\pi_r$是向量，而横向指标始终通过$\pi_r\pi_r$收缩，所以SO($N-1$)在平移后的拉格朗日量中仍然显明。同时，$\pi_r$没有二次势，正对应前面数出的$N-1$个Goldstone场。它们仍有相互作用，例如四价顶角为

<span id="eq:c32-goldstone-quartic"></span>

$$
iV_{\pi_r\pi_s\pi_t\pi_u}
=-\frac{i\lambda}{2}
(\delta_{rs}\delta_{tu}+\delta_{rt}\delta_{su}+\delta_{ru}\delta_{st}).
\tag{32.32}
$$

这个系数由对$(\pi_r\pi_r)^2$作四次微分得到：三种指标配对各有8种排列，乘上原来的$-i\lambda/16$即可。取$N=2$时，只剩一个横向场，顶角退回$b^4$的$-3i\lambda/2$。

<span id="c32-counting"></span>

## Goldstone计数的量子形式

上述质量零模与破缺方向的对应，只依赖势的对称性及真空条件，可以用于包含圈修正的有效势。在选定的量子真空附近，用实平均场$\phi_i$表示它，连续内部对称性要求

<span id="eq:c32-general-potential-identity"></span>

$$
U_i(\phi)t^a_{ij}\phi_j=0.
\tag{32.33}
$$

为了得到二次涨落的关系，对$\phi_k$求导。导数既作用于势的一阶导数，也作用于变换中的场，两项都须保留：

<span id="eq:c32-differentiated-identity"></span>

$$
U_{ki}(\phi)t^a_{ij}\phi_j+U_i(\phi)t^a_{ik}=0.
\tag{32.34}
$$

在量子真空中满足$U_i(v)=0$，第二项因而消失，剩下

<span id="eq:c32-quantum-null-directions"></span>

$$
\mathcal M^2_{ki}r_i^a=0,\qquad
\mathcal M^2_{ki}=U_{ki}(v),\qquad r_i^a=t^a_{ij}v_j .
\tag{32.35}
$$

每个改变真空的独立群方向，由此都是质量曲率矩阵的零方向。还须通过动能把这些方向归一为传播模：若低动量二次核为$-\Gamma^{(2)}=\mathcal M^2+Kk^2+\cdots$，且$K$正定，作涨落场变换$\eta=K^{-1/2}\zeta$即可归一动能，质量矩阵同时成为$K^{-1/2}\mathcal M^2K^{-1/2}$。这是可逆的变换，零空间的维数保持不变，因此仍有同样数目的无质量粒子；其物理极点也可以用前面的守恒流论证识别。

计数时只应取这些方向中线性独立的部分。线性映射$t\mapsto tv$把李代数$\mathfrak g$送到真空轨道的切空间，其核就是保持$v$不变的子代数$\mathfrak h$。由秩—零度定理，

<span id="eq:c32-goldstone-count"></span>

$$
N_{\rm Goldstone}=\dim\mathfrak g-\dim\mathfrak h
=\dim(G/H).
\tag{32.36}
$$

这里得到的是对称性所要求的无质量方向数，额外的偶然零模应另计。不同生成元的非零线性组合也可能改变$v$，但不会因此增加独立方向。对于本节的SO($N$)模型，$G/H={\rm SO}(N)/{\rm SO}(N-1)$就是最低球面，其维数为$N-1$，与显式平移所得的场数一致。在保持整体内部对称性、采用正确真空驻点及非退化物理动能的四维洛伦兹不变标量理论中，这便是Goldstone定理的计数。

---

[← 第 31 节](/posts/srednicki-31/) · [章节地图](/srednicki/) · [第 33 节 →](/posts/srednicki-33/)
