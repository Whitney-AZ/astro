---
title: 'Srednicki §30 自发对称性破缺'
date: 2026-09-14
category: 笔记
tags: [物理, 量子场论, Srednicki]
series: 'Srednicki QFT'
srednickiSections: [30]
hideFromHome: true
draft: false
---

<span id="c30"></span>

前面讨论实$\varphi^4$理论时，通常围绕$\varphi=0$展开，并用$\varphi\mapsto-\varphi$的对称性说明奇数场的真空期望为零。现在仍取同一个对称拉格朗日量，却让二次项改变符号。经典最低能量将落在非零场值处，原点因而不再适合作为粒子理论的展开点。围绕其中一个最低态，我们仍能建立通常的微扰论；变化在于，对称变换会把选定的真空送到另一个真空。

本节先从经典势和量子力学双阱看清真空选择的含义，再平移场以描述选定真空附近的粒子，最后用第21节的量子作用量说明：平移虽然产生了新的顶点，却不需要增加独立的重整化参数。四维中取$\lambda>0$，并用$v_0$标记树级最低点、$v$标记含圈修正的真空值，以区分两步计算。

<span id="c30-classical"></span>

## 两个经典最低点

仍从实标量的四次模型出发，写成动能减势能的形式：

<span id="eq:c30-model"></span>

$$
\mathcal L=-\frac12\partial^\mu\varphi\partial_\mu\varphi
-V(\varphi),\qquad
V(\varphi)=\frac12m^2\varphi^2+\frac{\lambda}{24}\varphi^4 .
\tag{30.1}
$$

势和动能都在场的符号反射下不变，因此保留第23节的离散对称性。在包含所需态的表示中，用幺正算符实现这一变换，并取

<span id="eq:c30-discrete-symmetry"></span>

$$
Z^{-1}\varphi(x)Z=-\varphi(x),\qquad Z^2=1 .
\tag{30.2}
$$

由$Z^2=1$可得$Z^{-1}=Z$，而幺正性又要求$Z^{-1}=Z^\dagger$，所以这个离散算符同时是厄米的。后面还会出现用字母$Z$表示的重整化常数，它们与这里作用在态空间中的对称算符是不同对象。

拉格朗日量中的参数$m^2$只是二次项的系数，可以取负值；是否能把它与粒子质量联系起来，要在确定稳定背景之后判断。令$m^2<0$，将势配成平方，便得到

<span id="eq:c30-completed-square"></span>

$$
V(\varphi)
=\frac{\lambda}{24}(\varphi^2-v_0^2)^2
-\frac{\lambda v_0^4}{24},\qquad
v_0^2=-\frac{6m^2}{\lambda},\qquad v_0>0 .
\tag{30.3}
$$

展开右边的平方，二次项为$-\lambda v_0^2\varphi^2/12=m^2\varphi^2/2$，四次项保持原系数，两个常数相消。这样写的好处是势的最低点直接由平方项确定。以下选择能量零点，将最后一个常数移去；这一平移不改变场方程和散射，若要计算绝对真空能，则仍须保留相应常数及其反项。

寻找场论的最低能量还要考虑动能和空间梯度。移去常数后，哈密顿量为

<span id="eq:c30-positive-energy"></span>

$$
H=\int d^3x\left[
\frac12\dot\varphi^2+\frac12(\boldsymbol\nabla\varphi)^2
+\frac{\lambda}{24}(\varphi^2-v_0^2)^2\right].
\tag{30.4}
$$

在连通空间中，只要边界允许均匀场，各项就能同时取到非负的最小值，对应静态的$\varphi(x)=+v_0$或$\varphi(x)=-v_0$。若在空间中拼接不同符号的区域，过渡处会产生梯度能，因而不再是这两个均匀最低态。驻点附近的局部稳定性则由势的导数读出：

<span id="eq:c30-curvatures"></span>

$$
V'(\varphi)=\varphi\left(m^2+\frac{\lambda}{6}\varphi^2\right),\qquad
V''(\varphi)=m^2+\frac{\lambda}{2}\varphi^2
\tag{30.5}
$$

原点的曲率为负，而两个最低点的曲率均为$-2m^2>0$，所以小涨落应围绕后两者展开。若$m^2>0$，原点就是唯一的经典最低点，回到前面熟悉的情形。

<span id="c30-vacuum-limit"></span>

## 双阱量子力学与体积极限

经典势有两个最低点，并不立即意味着量子理论也有两个可分别选择的基态。量子力学中的双阱提供了一个熟悉的例子。考虑单位质量粒子的哈密顿量

<span id="eq:c30-double-well"></span>

$$
H_{\rm QM}=\frac12p^2+\frac{\lambda}{24}(x^2-v_0^2)^2.
\tag{30.6}
$$

在右侧势阱附近令$x=v_0+y$，势变成$\lambda v_0^2y^2/6+\lambda v_0y^3/6+\lambda y^4/24$。保留二次项，得到简谐频率$\omega$，其中$\omega^2=\lambda v_0^2/3$；左阱有相同频率，因此两个阱附近的归一化近似波函数为

<span id="eq:c30-local-gaussians"></span>

$$
\psi_\pm(x)=\left(\frac{\omega}{\pi}\right)^{1/4}
e^{-\omega(x\mp v_0)^2/2}.
\tag{30.7}
$$

这两个高斯波包的典型宽度为$\omega^{-1/2}$。当$\omega v_0^2\gg1$时，宽度远小于中心到原点的距离，三次、四次项相对二次项分别按$|y|/v_0$和$y^2/v_0^2$受控，这就是局部简谐近似的适用条件。

即使两个波包已相隔很远，它们仍有非零重叠。将乘积中的两个指数相加，利用$(x-v_0)^2+(x+v_0)^2=2x^2+2v_0^2$，可把重叠积分化为

<span id="eq:c30-gaussian-overlap"></span>

$$
s_0=\int dx\,\psi_+(x)\psi_-(x)
=\sqrt{\frac{\omega}{\pi}}e^{-\omega v_0^2}
\int dx\,e^{-\omega x^2}
=e^{-\omega v_0^2}.
\tag{30.8}
$$

反射对称的哈密顿量会混合这两个局域态，因此在两态近似中应取偶、奇线性组合。计入非零重叠，它们的归一化形式为

<span id="eq:c30-even-odd-combinations"></span>

$$
|e\rangle=\frac{|+\rangle+|-\rangle}{\sqrt{2(1+s_0)}},
\qquad
|o\rangle=\frac{|+\rangle-|-\rangle}{\sqrt{2(1-s_0)}}.
\tag{30.9}
$$

有限双阱的精确基态确实是偶态，这可以从一维薛定谔方程看出。先将基态取为实函数，再取其绝对值，动能和势能都不会增加，因而仍达到最低能量。这个非负解若在内部某点为零，该点的一阶导数也必须为零；微分方程解的唯一性就会迫使它处处为零，与归一化矛盾，所以基态严格为正。再考察两个同能衰减解，它们的朗斯基行列式是常数，并在无穷远趋于零，故两解线性相关。反射后的正解于是只能等于原基态，基态为偶态。最低奇态的能量稍高，阱间隧穿造成这一小的能级分裂，而式[（30.9）](#eq:c30-even-odd-combinations)给出两者在深阱时的近似形式。

场论与这个有限量子力学系统的差别来自空间体积。把空间各处看作由梯度项耦合的振子，要从一个均匀最低态变到另一个，整个空间的场都要翻转，振幅便随体积受到压低。沿用上面的简谐近似，可以把体积因子具体算出来。保留固定UV调节和有限空间体积$\mathcal V$，取均匀模式$\bar\varphi$，其动能为$\mathcal V\dot{\bar\varphi}^{\,2}/2$。因此应以$q=\sqrt{\mathcal V}\,\bar\varphi$作正则坐标，均匀模的拉格朗日量为

<span id="eq:c30-volume-zero-mode"></span>

$$
L_0=\frac12\dot q^2
-\frac{\lambda}{24\mathcal V}(q^2-\mathcal Vv_0^2)^2.
\tag{30.10}
$$

均匀模的两个势阱中心位于$\pm\sqrt{\mathcal V}v_0$，随体积增加而彼此远离，但小振动频率仍是$M_0=\sqrt{\lambda v_0^2/3}$。将这一中心和频率代入式[（30.8）](#eq:c30-gaussian-overlap)，重叠便成为

<span id="eq:c30-volume-overlap"></span>

$$
s_{\mathcal V}=e^{-M_0v_0^2\mathcal V}
\ \longrightarrow\ 0\qquad(\mathcal V\to\infty).
\tag{30.11}
$$

如果在两个阱附近采用相同的场二次核，常数位移只改变零动量模，其余模式的高斯内积都为1。因此，场波泛函的重叠正由上述零模决定。指数中的$M_0v_0^2\mathcal V$是无量纲量，显示压低来自物理空间体积的增长；这里保持紫外调节固定，让物理空间体积趋于无穷。

正交性的理由还可以摆脱高斯形状，只要已有两个满足聚类条件的纯相。先固定局部UV平滑，考察区域$\mathcal R$中的平均场$\bar\varphi_{\mathcal R}=\mathcal V_{\mathcal R}^{-1}\int_{\mathcal R}d^3x\,\varphi(x)$。若两相平均值分别趋于$\pm v$、$v>0$，而各自连通的等时关联$C_\pm(r)$可积，宏观平均场的方差就满足

<span id="eq:c30-cluster-variance"></span>

$$
\operatorname{Var}_\pm(\bar\varphi_{\mathcal R})
=\frac1{\mathcal V_{\mathcal R}^2}
\int_{\mathcal R}d^3x\,d^3y\,C_\pm(x-y)
\le\frac1{\mathcal V_{\mathcal R}}\int d^3r\,|C_\pm(r)|
\longrightarrow0.
\tag{30.12}
$$

因此，区域增大时，平均场在每个相中都越来越集中于自身的期望值。将有限体积态的这两个平均值记作$v_+$、$v_-$，在$(v_+-v_-)\langle+|-\rangle$中加减同一个平均场，再用柯西–施瓦茨不等式，就能把态的重叠与这两个方差联系起来：

<span id="eq:c30-orthogonality-bound"></span>

$$
\begin{aligned}
|(v_+-v_-)\langle+|-\rangle|
&=\left|\langle+|(v_+-\bar\varphi_{\mathcal R})|-\rangle
+\langle+|(\bar\varphi_{\mathcal R}-v_-)|-\rangle\right|\\
&\le\sqrt{\operatorname{Var}_+(\bar\varphi_{\mathcal R})}
+\sqrt{\operatorname{Var}_-(\bar\varphi_{\mathcal R})}
\longrightarrow0 .
\end{aligned}
\tag{30.13}
$$

由于$v_+-v_-\to2v\ne0$，方差趋零就迫使两相的重叠趋零。这里用的是两种纯相已经存在并满足聚类条件；在本节弱耦合、远离临界点的破缺相中，有质量的小涨落正与这些条件相配。

要实际选出其中一个相，可以加入很小的恒定实源$j$。洛伦兹拉格朗日量中的$+j\varphi$对应$H_j=H-j\int d^3x\,\varphi$，所以正$j$使正相的能量较低。先作基态投影，再固定$j$取无限空间体积，最后撤去源，分别定义

<span id="eq:c30-order-of-limits"></span>

$$
v=\lim_{j\downarrow0}\lim_{\mathcal V\to\infty}
\langle\varphi\rangle_{j,\mathcal V},\qquad
-v=\lim_{j\uparrow0}\lim_{\mathcal V\to\infty}
\langle\varphi\rangle_{j,\mathcal V}.
\tag{30.14}
$$

极限次序在这里起着实质作用：若在有限对称盒中先令$j=0$，就会回到偶基态及零一点函数。也可以不用微小体源，而用固定正、负边界分别选出对应的相。

将两个真空记作$|0+\rangle,|0-\rangle$，它们满足$\langle0\pm|\varphi(x)|0\pm\rangle=\pm v$，当前弱耦合近似中有$v=v_0+\hbox{圈修正}$。对称算符互换两态时一般可带相位：若$Z|0+\rangle=e^{i\alpha}|0-\rangle$，则$Z^2=1$使反向相位为$e^{-i\alpha}$。调整负态的整体相位，即可写成$Z|0+\rangle=|0-\rangle$。这与对称真空有根本区别：若正真空在$Z$下仅乘一个相位，式[（30.2）](#eq:c30-discrete-symmetry)就会要求$v=-v$，所以$v\ne0$的真空不能单独保持反射对称性。在同时包含两相的空间中，$Z$将它们互换；限制到一个无限体积纯相时，这一变换把态送到另一相的表示。

<span id="c30-shift"></span>

## 在选定真空附近建立粒子理论

选择正真空后，把涨落场的零点移到该处，才能读出稳定粒子的质量和相互作用。先在树级取$\varphi=v_0+\rho$，常数平移保持动能不变，而势中的平方展开为

<span id="eq:c30-shift-polynomial"></span>

$$
[(v_0+\rho)^2-v_0^2]^2
=(\rho^2+2v_0\rho)^2
=\rho^4+4v_0\rho^3+4v_0^2\rho^2.
\tag{30.15}
$$

乘以$\lambda/24$就得到势的二、三、四次项。将二次项写成标准质量形式，相应拉格朗日量为

<span id="eq:c30-shifted-lagrangian"></span>

$$
\mathcal L
=-\frac12(\partial\rho)^2-\frac12M_0^2\rho^2
-\frac{\lambda v_0}{6}\rho^3-\frac{\lambda}{24}\rho^4,
\tag{30.16}
$$

这里$M_0^2=\lambda v_0^2/3=-2m^2$。识别质量时要保留二次项的归一因子：势中二次项的系数是$|m^2|$，而标准质量平方前带$1/2$，所以质量平方为$2|m^2|$。自由涨落于是满足$E_{\mathbf k}^2=\mathbf k^2+M_0^2>0$，每个模式都有实频率。若仍在原点线性化，则得到$\ddot\varphi_{\mathbf k}+(\mathbf k^2+m^2)\varphi_{\mathbf k}=0$，低于$|m^2|$的$\mathbf k^2$模式中存在指数增长解；这种不稳定性正说明原点不适合作为粒子真空。平移后还出现三价顶点$-i\lambda v_0$，四价顶点仍为$-i\lambda$；与前文正立方项的记法比较，有$g_3=-\lambda v_0$，此处$g_3$的质量维数为1。

三次项使反射对称性不再以简单的场变号显现，但原变换依然存在。在$\rho$坐标中，它成为

<span id="eq:c30-affine-symmetry"></span>

$$
Z^{-1}\rho Z=-\rho-2v_0 .
\tag{30.17}
$$

连续作用两次仍恢复$\rho$，而势中的$\rho^2(\rho+2v_0)^2$保持不变。不过，这个变换把$\rho=0$附近送到$\rho=-2v_0$附近，也就是把所选的粒子真空送到另一个最低态。作用量保持对称，而选定真空不保持它，这种情形称为自发对称性破缺（spontaneous symmetry breaking）。

计入圈修正后，平移位置也要随真空改变。定义$\rho=\varphi-v$，其中$v=\langle\varphi\rangle_+$，就应始终满足$\langle\rho\rangle_+=0$；计算上等价于一点核为零。若将重整化量子势写成$U_{\rm ren}=V+U_{1,\rm ren}+\cdots$，并展开$v=v_0+\delta v_1+\cdots$，驻点方程给出

<span id="eq:c30-vacuum-shift"></span>

$$
0=V'(v_0)+M_0^2\delta v_1+U'_{1,\rm ren}(v_0)+\cdots ,
\qquad
\delta v_1=-\frac{U'_{1,\rm ren}(v_0)}{M_0^2}.
\tag{30.18}
$$

所以配平方得到的树关系$v_0^2=-6m^2/\lambda$仅确定最低阶位置，精确的$v$还含圈修正。下一节将显式计算圈修正；这里先考察一点条件怎样联系各个反项。

<span id="c30-counterterms"></span>

## 平移后的顶点与三个独立反项

为了确定平移后各顶点之间的关系，先把三个重整化常数放回对称形式：

<span id="eq:c30-symmetric-counterterms"></span>

$$
\mathcal L=-\frac12Z_\varphi(\partial\varphi)^2
-\frac12Z_m m^2\varphi^2-\frac{Z_\lambda\lambda}{24}\varphi^4 .
\tag{30.19}
$$

在平移后的理论中，三次顶点需要重整化，它又能产生非零蝌蚪，因此乍看之下，三次项和线性项都似乎需要单独的参数。要看清它们是否独立，应先对任意常数$v$完整展开，而不预先使用树级极值关系：

<span id="eq:c30-full-shift"></span>

$$
\begin{aligned}
\mathcal L={}&-\frac12Z_\varphi(\partial\rho)^2-C_0\\
&-\left(Z_m m^2v+\frac{Z_\lambda\lambda v^3}{6}\right)\rho\\
&-\frac12\left(Z_m m^2+\frac{Z_\lambda\lambda v^2}{2}\right)\rho^2
-\frac{Z_\lambda\lambda v}{6}\rho^3
-\frac{Z_\lambda\lambda}{24}\rho^4,\\
C_0={}&\frac12Z_m m^2v^2+\frac{Z_\lambda\lambda v^4}{24}.
\end{aligned}
\tag{30.20}
$$

所有系数都来自原来的二次和四次多项式，新增的线性、三次项因而已经受同一对称结构约束。把这些关系改写成反项形式会更直观。记$A=Z_\varphi-1$、$B=Z_m-1$、$C=Z_\lambda-1$，暂在$v_0$处平移，利用$\lambda v_0^2/6=-m^2$，再减去树级式[（30.16）](#eq:c30-shifted-lagrangian)，得到场依赖反项

<span id="eq:c30-shifted-counterterm-polynomial"></span>

$$
\begin{aligned}
\mathcal L_{\rm ct}
={}&-\frac A2(\partial\rho)^2
-m^2v_0(B-C)\rho
-\frac{m^2}{2}(B-3C)\rho^2\\
&-\frac{C\lambda v_0}{6}\rho^3-\frac{C\lambda}{24}\rho^4 .
\end{aligned}
\tag{30.21}
$$

其中线性系数由$Bm^2v_0+C\lambda v_0^3/6=m^2v_0(B-C)$合并而来，二次括号则为$Bm^2+C\lambda v_0^2/2=m^2(B-3C)$，三次反项完全由四次反项的$C$确定。若改在含一圈修正的位置$v=v_0+\delta v_1$处展开，拉格朗日量的树级部分还会多出线性项$-M_0^2\delta v_1\rho$。以$U_{1,\rm loop}$表示未加反项的一圈势，将这些线性贡献合在一起，一点条件便为

<span id="eq:c30-tadpole-condition"></span>

$$
M_0^2\delta v_1+m^2v_0(B-C)+U'_{1,\rm loop}(v_0)=0 .
\tag{30.22}
$$

后两项合为$U'_{1,\rm ren}$，就恢复式[（30.18）](#eq:c30-vacuum-shift)的真空位移方程。因此$\delta v_1$是在已有参数下确定真空位置，并未引入可独立调节的三次物理耦合。

为与下一节的显式积分衔接，先写出蝌蚪图的组合因子。三价相互作用带$1/3!$，选择哪一条腿作外腿有三种方式，乘起来留下$1/2$，其余两场相互收缩。按前面的顶点和传播线相位，一点图为

<span id="eq:c30-tadpole-factor"></span>

$$
i\Gamma^{(1)}_{\rm loop}
=\frac12(-i\lambda v_0)
\int\frac{d^4k}{(2\pi)^4}\,
\frac{1}{i(k^2+M_0^2-i0)}.
\tag{30.23}
$$

这一图应与$-i[m^2v_0(B-C)+M_0^2\delta v_1]$相加为零，正与$\Gamma^{(1)}=-U'$的负号一致。积分中先保留UV调节；下一节将延拓到$d=4-\epsilon$，补入$\lambda_d=\lambda\widetilde\mu^\epsilon$，评价蝌蚪积分后再与二、三、四点图比较。

上述多项式关系说明了平移反项如何联系，而三个独立反项足够的原因，则在于原理论的局域UV结构。对四维四次图，端口计数$4V=2I+E$及圈数关系$L=I-V+1$给出

<span id="eq:c30-counterterm-power-count"></span>

$$
\omega=4L-2I=4-E .
\tag{30.24}
$$

减去所有子图发散后，二点图剩余的新发散至多是外动量的二次多项式，四点图至多是常数，更多外腿的图没有新的整体发散。再要求洛伦兹不变性及$\varphi\mapsto-\varphi$对称性，场依赖局域反项就只有$(\partial\varphi)^2$、$\varphi^2$和$\varphi^4$。这是[第18节的子图减除](/posts/srednicki-18/#c18-forest)在本模型中的应用，场无关的真空常数仍另行减去。一般$d\le4$时，$[\lambda]=4-d\ge0$，同一幂计数仍给出可重整化的范围。常数平移只是重新排列这些局域多项式，故不会增加独立UV参数。

因此，在正$m^2$区域确定的对称反项可以继续用于破缺相，例如将保持对称性的$\overline{\mathrm{MS}}$局域反项代入前面的平移多项式。但有限部分还要在适当背景下求值：背景涨落的质量平方为$\mathcal M^2(\varphi)=m^2+\lambda\varphi^2/2$，在$\pm v_0$处为正，在负$m^2$理论的原点处却为负。原点低模式的不稳定意味着，不能把围绕原点得到的有限实函数机械地延拓过去。此外，$v_0\sim\lambda^{-1/2}$，在零场顶角中加入背景会改变耦合计阶，因此逐圈计算须保留该圈完整的背景依赖。

<span id="c30-quantum-action"></span>

## 对称的量子作用量与真空方程

要把反项的联系与真空条件放在同一个对象中，就回到第21节的量子作用量。由全部1PI核组成的泛函为

<span id="eq:c30-quantum-action"></span>

$$
\begin{aligned}
\Gamma[\varphi]
={}&-\frac12\int_k\widetilde\varphi(-k)
[k^2+m^2-\Pi(k^2)]\widetilde\varphi(k)\\
&+\sum_{n\ge3}\frac1{n!}
\int_{k_1}\cdots\int_{k_n}(2\pi)^4
\delta^4\!\left(\sum_a k_a\right)\\
&\hspace{25mm}\times
V_n(k_1,\ldots,k_n)\prod_a\widetilde\varphi(k_a).
\end{aligned}
\tag{30.25}
$$

这里$\int_k=\int d^4k/(2\pi)^4$。二次核前的负号沿用第21节的勒让德变换约定；在树级，$V_4=-\lambda$，高点部分也给出负的四次项，于是$\Gamma$回到经典作用量。

在对称真空处，四价点与二价反项的端口计数满足$4V_4+2V_2=2I+E$，因此$E$必为偶数：奇数外腿的$V_n$为零，$\Gamma$是偶泛函。[第21节的线性对称性推导](/posts/srednicki-21/#c21-symmetry)在这里化为一个简单的变量替换。在保持反射的有限调节、积分域和边界下，$\chi\mapsto-\chi$的绝对雅可比为1，逐步得到

<span id="eq:c30-symmetry-inheritance"></span>

$$
Z[J]=Z[-J],\quad W[J]=W[-J],\quad
\varphi[-J]=-\varphi[J],\quad \Gamma[-\varphi]=\Gamma[\varphi].
\tag{30.26}
$$

最后一步使用了$W-\int J\varphi$在源和场同时变号时不变。若边界已经选定正相，反射也会把边界变为负相，此时等式联系的是两相对应的分支。这个换元同时使用了经典作用量与积分测度的对称性。若调节后不能同时保持相应对称，就会出现反常；本例的实场符号反射保持有限模式测度，[第75节](/posts/srednicki-75/)将讨论手征反常。

有了量子作用量，就可以用源方程确定真空。取静态源及相容的基态投影，将泛函写成导数展开形式：

<span id="eq:c30-derivative-action"></span>

$$
\Gamma[\varphi]=\int d^4x\left[
-U(\varphi)-\frac12Z(\varphi)\partial^\mu\varphi\partial_\mu\varphi
+\hbox{更多导数项}\right].
\tag{30.27}
$$

寻找平移不变真空时，平均场为常数，全部导数项消失。因此，第21节的$\delta\Gamma/\delta\varphi=-J$直接化为

<span id="eq:c30-quantum-vacuum-equation"></span>

$$
-U'(\varphi_j)=-j,\qquad U'(\varphi_j)=j,\qquad U'(v)=0 .
\tag{30.28}
$$

若零源下有多个均匀驻点，还需比较其能量，从中选出最低的相。弱耦合时，可以在两个经典最低点附近逐圈求解，得到$v=v_0+\delta v_1+\cdots$和反射后的$-v$，对称性保证两相能量相同。这里$v$是精确一点函数，配平方中的$v_0$则是它的树级近似。

量子作用量还把真空位置与粒子质量联系起来。在所选纯相中，涨落的完整逆二点核为

<span id="eq:c30-curvature-and-pole"></span>

$$
D_\rho(k^2;v)=-\Gamma_\rho^{(2)}(k;v)
=U''(v)+Z(v)k^2+O(k^4),\qquad
D_\rho(-M_{\rm pole}^2;v)=0 .
\tag{30.29}
$$

这里$U''$给出零动量曲率，$U''/Z$则是保留到二阶导数时的近似质量平方。物理质量由完整核的极点决定，一般还受到更高动量项的影响，相应留数为$[D'_\rho(-M_{\rm pole}^2;v)]^{-1}$。因此，树级从二次势识别质量的做法，到下一节计入圈修正时，要转为对完整二点核求极点。

<span id="c30-convex-potential"></span>

## 全局量子势与两相共存

上面的弱耦合计算在两个等能最低点附近分别展开，适合描述各个纯相中的涨落。若考察完整的全局勒让德势，还要把两相共存计入，所得势具有凸性。为了看清这一性质与前面双阱图像的联系，先从有限欧氏积分出发，保留正测度、有限UV调节和有限四体积$\Omega$，并采用正源记号

<span id="eq:c30-euclidean-convexity-start"></span>

$$
Z_E(j)=\int D\chi\,e^{-S_E+j\int_\Omega\chi},\qquad
w_\Omega(j)=\frac1\Omega\ln Z_E(j),\qquad
\bar\chi=\frac1\Omega\int_\Omega\chi .
\tag{30.30}
$$

这里的$j$是第29节负欧氏源的相反数。对源的每次微分都插入一个$\int_\Omega\chi$，因此对数生成函数的一阶导数是平均场，二阶导数是四体积乘以方差：

<span id="eq:c30-source-variance"></span>

$$
w_\Omega'(j)=\langle\bar\chi\rangle_j,\qquad
w_\Omega''(j)
=\Omega\left(\langle\bar\chi^2\rangle_j-\langle\bar\chi\rangle_j^2\right)\ge0.
\tag{30.31}
$$

为了把固定源的描述改写为固定平均场的描述，取完整的勒让德变换，定义全局势

<span id="eq:c30-legendre-supremum"></span>

$$
U_\Omega(\phi)=\sup_j\{j\phi-w_\Omega(j)\}.
\tag{30.32}
$$

对于每一个$j$，大括号都是$\phi$的仿射函数；对这一族函数取上确界便给出凸函数。具体地，取$0\le\theta\le1$，有

$$
\begin{aligned}
U_\Omega(\theta\phi_1+(1-\theta)\phi_2)
&=\sup_j\{\theta[j\phi_1-w_\Omega(j)]
+(1-\theta)[j\phi_2-w_\Omega(j)]\}\\
&\le\theta U_\Omega(\phi_1)+(1-\theta)U_\Omega(\phi_2).
\end{aligned}
$$

第一行中的同一个$j$，分别受第二行两个上确界约束，因而得到凸不等式。在源—场关系可微且可逆的区域，也可以直接对$\phi=w_\Omega'(j)$求导，得到$U_\Omega''=1/w_\Omega''\ge0$。

若体积极限存在，且两个端点$\pm v$具有相同最低值$U_{\min}$，凸性就进一步决定端点之间的形状。对于$0\le\theta\le1$，

<span id="eq:c30-flat-coexistence"></span>

$$
U\bigl(\theta v+(1-\theta)(-v)\bigr)
\le\theta U(v)+(1-\theta)U(-v)=U_{\min}.
\tag{30.33}
$$

另一方面，最低值的定义又给出反向不等式，所以两端之间也是平坦的最低势段。端点$\pm v$仍由$j\to0^\pm$所选出的纯相确定，中间值则可以描述两相共存；零源处的源—场映射也因此可能不可逆。局部纯相的圈展开用于计算一个选定真空附近的粒子过程，全局凸势则同时描述不同相及其共存。接下来的显式计算沿选定纯相进行，用一点条件确定$v$，并求出原对称形式的三个反项如何同时消去各图发散。

---

[← 第 29 节](/posts/srednicki-29/) · [章节地图](/srednicki/) · [第 31 节 →](/posts/srednicki-31/)
