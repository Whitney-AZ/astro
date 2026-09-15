---
title: 'Srednicki §7 谐振子的路径积分'
date: 2026-09-14
category: 笔记
tags: [物理, 量子场论, Srednicki]
series: 'Srednicki QFT'
srednickiSections: [7]
hideFromHome: true
draft: false
---

<span id="c07"></span>

谐振子的作用量是二次型，加入线性外力以后，路径积分仍可通过完成平方求出。由此得到外源的生成泛函，再对外源求导，便得到任意多个位置算符的时间序关联函数。

<span id="c07-oscillator"></span>

## 加入外源并积掉动量

考虑谐振子的哈密顿量

<span id="eq:c07-hamiltonian"></span>

$$
H=\frac{P^2}{2m}+\frac12m\omega^2Q^2,
\qquad [Q,P]=i,\qquad m>0,\quad\omega>0.
\tag{7.1}
$$

先取 $\hbar=1$。将外源 $f(t)$ 与位置耦合，哈密顿量便增加 $-f(t)Q$，因而作用量中的对应项为 $+f(t)q(t)$。我们所求的是外力作用前后都处在基态的振幅，所以沿用上一节的基态边界处方。记 $\alpha=1-i\epsilon_0$，其中 $\epsilon_0>0$，真空生成泛函写为

<span id="eq:c07-phase-functional"></span>

$$
Z[f]=\mathcal N_{\epsilon_0}
\int\mathcal Dp\,\mathcal Dq\,
\exp\!\left\{i\int dt\left[
p\dot q-\alpha\left(\frac{p^2}{2m}
+\frac12m\omega^2q^2\right)+fq\right]\right\}.
\tag{7.2}
$$

时间积分从 $-\infty$ 延伸到 $+\infty$，按式[（6.38）](/posts/srednicki-06/#eq:c06-vacuum-normalization)所规定的长时间极限理解；外源先取为光滑且仅在有限时间内非零，使两端的长时间演化负责选择基态。常数 $\mathcal N_{\epsilon_0}$ 由 $Z[0]=1$ 确定。谐振子的基态能量为 $\omega/2$，无源演化本来还带有相应能量相位；除以同一无源振幅后，这个相位和端点重叠常数一并消去，剩下的 $Z[f]$ 才只反映外力的作用。

动量仍只出现在二次式中，可以先逐个时间片完成平方：

<span id="eq:c07-momentum-square"></span>

$$
p\dot q-\frac{\alpha p^2}{2m}
=-\frac{\alpha}{2m}
\left(p-\frac{m\dot q}{\alpha}\right)^2
+\frac{m\dot q^2}{2\alpha}.
\tag{7.3}
$$

第一项用第6节的 高斯 积分处理，每段给出 $\sqrt{m/(2\pi i\alpha\delta t)}$。余下的速度项与势能、外源项共同组成位置路径的作用量：

<span id="eq:c07-configuration-functional"></span>

$$
Z[f]=\mathcal N'_{\epsilon_0}\int\mathcal Dq\,e^{iS_{\epsilon_0}[q,f]},
\qquad
S_{\epsilon_0}[q,f]=\int dt\left[
\frac{m}{2\alpha}\dot q^2
-\frac{\alpha m\omega^2}{2}q^2+fq\right].
\tag{7.4}
$$

动量积分产生的常数已收入归一化测度。若只保留决定收敛方向的一阶虚部，可使用展开 $1/(1-i\epsilon_0)=1+i\epsilon_0+O(\epsilon_0^2)$。由上式可见，动能和势能在 $S_{\epsilon_0}$ 中的虚部都为正，进入 $e^{iS_{\epsilon_0}}$ 后都给出衰减。以下令 $m=1$ 以简化记号；恢复质量时，无源二次作用量整体乘 $m$，二点位置关联则带有 $m^{-1}$。

<span id="c07-fourier"></span>

## 在频域完成平方

位置积分的困难在于时间导数把相邻时刻的变量联系起来。对时间平移不变的二次作用量，傅里叶变换可以把这部分关系对角化，使每个频率单独进入二次核。定义傅里叶变换为

<span id="eq:c07-fourier"></span>

$$
\widetilde q(E)=\int dt\,e^{iEt}q(t),
\qquad
q(t)=\int\frac{dE}{2\pi}\,e^{-iEt}\widetilde q(E),
\tag{7.5}
$$

外源 $f$也作同一变换。实路径满足 $\widetilde q(-E)=\widetilde q(E)^*$，实外源也有相同关系。可先在有限区间用实的正弦、余弦模式积分，再取连续频率极限。变换产生的常数Jacobian与外源无关，在零源归一化中消去。

把两份傅里叶积分代入作用量，每次时间微分带来 $-iE$，两次微分便给出 $-EE'$。外源项再通过交换哑变量写成对称形式，就有

<span id="eq:c07-double-fourier"></span>

$$
\begin{aligned}
S_{\epsilon_0}
=\frac12\int dt\int\frac{dE\,dE'}{(2\pi)^2}
e^{-i(E+E')t}\bigg[
&\left(-\frac{EE'}{\alpha}-\alpha\omega^2\right)
\widetilde q(E)\widetilde q(E')\\
&+\widetilde f(E)\widetilde q(E')
+\widetilde f(E')\widetilde q(E)
\bigg].
\end{aligned}
\tag{7.6}
$$

括号中的两份源项积分相等，所以外面的 $1/2$ 恰好使总系数仍为 $fq$ 的系数。动能系数在这里仍保留精确的 $1/\alpha$。

全部时间依赖现在集中在一个指数中。先用 $\int dt\,e^{-i(E+E')t}=2\pi\delta(E+E')$ 作时间积分，再积掉 $E'$。delta函数令 $E'=-E$，于是导数产生的 $-EE'$ 化为正的 $E^2$。频域作用量因而为

<span id="eq:c07-frequency-action"></span>

$$
S_{\epsilon_0}
=\frac12\int\frac{dE}{2\pi}
\left[
A_{\epsilon_0}(E)\widetilde q(E)\widetilde q(-E)
+\widetilde f(E)\widetilde q(-E)
+\widetilde f(-E)\widetilde q(E)
\right],
\tag{7.7}
$$

其中每个频率所对应的二次核为

<span id="eq:c07-regulated-kernel"></span>

$$
\begin{aligned}
A_{\epsilon_0}(E)
&=\frac{E^2}{\alpha}-\alpha\omega^2
=\frac{E^2-\alpha^2\omega^2}{\alpha}\\
&=E^2-\omega^2
+i\epsilon_0(E^2+\omega^2)+O(\epsilon_0^2).
\end{aligned}
\tag{7.8}
$$

这个核的零点在 $E=\alpha\omega$ 和 $E=-\alpha\omega$：正频率根位于实轴下方，负频率根位于上方。由于 $\omega>0$，一阶虚部的系数 $E^2+\omega^2$ 处处为正。这提示我们用同方向的常数正虚部表示极点边界处方。将常数调节量另记为

<span id="eq:c07-i0-kernel"></span>

$$
A_\eta(E)=E^2-\omega^2+i\eta,\qquad \eta>0,
\tag{7.9}
$$

后面的积分先在有限调节下进行，最后取 $\eta\downarrow0$。这里 $\epsilon_0$ 是无量纲的哈密顿量乘子，而 $\eta$ 具有频率平方的量纲；它们所指定的实轴边界值方向相同。求出Green函数后，便能直接看到两种处方如何趋于同一个结果。

频率二次型已经对角化，接着平移变量，以消去外源产生的一次项：

<span id="eq:c07-shift"></span>

$$
\widetilde x(E)=\widetilde q(E)
+\frac{\widetilde f(E)}{A_\eta(E)}.
\tag{7.10}
$$

因为 $A_\eta$ 是偶函数，将两份 $\widetilde x$ 相乘时，二次项、两份交叉项和源平方项依次为

<span id="eq:c07-square-expansion"></span>

$$
\begin{aligned}
A_\eta\widetilde x(E)\widetilde x(-E)
={}&A_\eta\widetilde q(E)\widetilde q(-E)
+\widetilde f(E)\widetilde q(-E)
+\widetilde f(-E)\widetilde q(E)\\
&+\frac{\widetilde f(E)\widetilde f(-E)}{A_\eta}.
\end{aligned}
\tag{7.11}
$$

把最后多出的一项移到另一边，原作用量就可写成

<span id="eq:c07-completed-action"></span>

$$
S_\eta[q,f]
=\frac12\int\frac{dE}{2\pi}
A_\eta(E)\widetilde x(E)\widetilde x(-E)
-\frac12\int\frac{dE}{2\pi}
\frac{\widetilde f(E)\widetilde f(-E)}{A_\eta(E)}.
\tag{7.12}
$$

外源平方项前的负号，正是完成平方后减去多出项的结果。它已不含待积变量，可以作为整体从路径积分中提出；余下的积分则具有无源作用量的形式。

<span id="c07-complex-gaussian"></span>

### 复高斯积分

有限 $\eta$使完成平方中的平移量成为复数。相应的高斯积分可以直接在实模式上通过分部积分求出。

取有限个实模式组成坐标列向量 $q$，其二次核为复对称矩阵 $A$，并要求 $\operatorname{Im}A$ 正定。定义

<span id="eq:c07-finite-gaussian"></span>

$$
I(J)=\int_{\mathbb R^N}d^Nq\,
\exp\!\left(\frac i2q^TAq+iJ^Tq\right).
\tag{7.13}
$$

二次项给出的负实部使积分在无穷远衰减，因此对 $q_j$ 分部积分时没有边界贡献。由此得到积分与其源导数之间的关系：

<span id="eq:c07-gaussian-ibp"></span>

$$
0=i\int d^Nq\,(Aq+J)_j
e^{\,iq^TAq/2+iJ^Tq},
\qquad
\frac{\partial I}{\partial J_j}
=-i(A^{-1}J)_j I.
\tag{7.14}
$$

这里 $A$ 必可逆：若 $Av=0$，便有 $v^\dagger(\operatorname{Im}A)v=0$，而正定性要求 $v=0$。于是可沿 $J=sJ_0$ 从 $s=0$ 积到1。上一式的微分关系成为 $dI(sJ_0)/ds=-is(J_0^TA^{-1}J_0)I(sJ_0)$，解得

<span id="eq:c07-gaussian-ratio"></span>

$$
\frac{I(J)}{I(0)}
=\exp\!\left(-\frac i2J^TA^{-1}J\right).
\tag{7.15}
$$

归一化分母 $I(0)\ne0$ 也可由第6节的一维高斯积分确定。令 $B=\operatorname{Im}A>0$，先作 $q=B^{-1/2}y$，使衰减部分成为单位二次型，再用实正交变换对角化 $B^{-1/2}(\operatorname{Re}A)B^{-1/2}$。无源积分便分解为若干个 $\int dy\,e^{-(1-i\lambda)y^2/2}$，每个因子都非零；这些变换的Jacobian也都与 $J$ 无关。

式[（7.15）](#eq:c07-gaussian-ratio)直接从实积分上的分部积分得到源因子，在原来的积分轮廓上确定了完成平方的结果。对同一个有限模式截断取有源、无源积分的比值，再作所规定的路径积分极限，得到

<span id="eq:c07-frequency-functional"></span>

$$
Z[f]=\exp\!\left[
\frac i2\int\frac{dE}{2\pi}
\frac{\widetilde f(E)\widetilde f(-E)}
{-E^2+\omega^2-i0}\right].
\tag{7.16}
$$

所有无源高斯因子都由 $Z[0]=1$ 消去。因此，要得到外力依赖，只需求出二次核的逆；无穷多个模式共同产生的行列式不必先单独计算。

<span id="c07-green"></span>

## 回到时间变量：Green 函数

为了对不同时刻的外力求导，将两份 $\widetilde f$ 重新写成时间积分。指数中先出现 $e^{iE(t-t')}$，而分母是 $E$ 的偶函数，作 $E\to-E$ 后便得到时间表示：

<span id="eq:c07-time-functional"></span>

$$
\begin{aligned}
Z[f]&=\exp\!\left[
\frac i2\int dt\,dt'\,f(t)G(t-t')f(t')\right],\\
G_\eta(\tau)&=\int\frac{dE}{2\pi}
\frac{e^{-iE\tau}}{-E^2+\omega^2-i\eta},
\qquad G(\tau)=\lim_{\eta\downarrow0}G_\eta(\tau).
\end{aligned}
\tag{7.17}
$$

核 $G$ 把两个时刻的外源联系起来，同时也是运动方程的Green函数（Green function）。对其频域表达式作用 $\partial_\tau^2+\omega^2-i\eta$，产生的因子恰好抵消分母，留下

<span id="eq:c07-green-equation-regulated"></span>

$$
(\partial_\tau^2+\omega^2-i\eta)G_\eta(\tau)
=\int\frac{dE}{2\pi}e^{-iE\tau}
=\delta(\tau).
\tag{7.18}
$$

取边界极限即得 $(\partial_\tau^2+\omega^2)G=\delta$。微分方程的齐次解由基态边界条件选定，在频域中对应刚才的极点处方。

先令

<span id="eq:c07-poles"></span>

$$
\Omega=\sqrt{\omega^2-i\eta},\qquad
\operatorname{Re}\Omega>0,\quad\operatorname{Im}\Omega<0.
\tag{7.19}
$$

分母分解为 $-(E-\Omega)(E+\Omega)$，两个简单极点分居实轴下方和上方。若写 $E=u+iv$，便有 $|e^{-iE\tau}|=e^{v\tau}$，所以 $\tau>0$ 时应在下半平面闭合，$\tau<0$ 时应在上半平面闭合。在相应半圆上，指数的模不超过一，而分母随半径平方增长，圆弧积分的绝对值至多为常数乘 $R/R^2$，当 $R\to\infty$ 时消失。

为明确围道方向的符号，可从平面Green公式得到所需的留数规则。若 $F=u+iv$ 在某区域解析，Cauchy–Riemann关系 $u_x=v_y$、$u_y=-v_x$ 使 $\oint F\,dz$ 对应的两个面积积分均为零。区域中若有简单极点，先挖去极点附近的小圆，剩余区域仍可用这个结论。设极点为 $z_0$，附近有 $F(z)=r/(z-z_0)+O(1)$；在逆时针小圆上令 $z=z_0+\rho e^{i\theta}$，奇异项贡献 $\int_0^{2\pi}ir\,d\theta=2\pi i r$，有界余项则随 $\rho\to0$ 消失。因此逆时针外轮廓给出 $+2\pi i$ 乘所包围的留数，顺时针取相反号。对于 $F=N/D$ 且 $D$ 只有简单零点的情形，留数为 $N(z_0)/D'(z_0)$。

现在应用到频率积分。$\tau>0$ 时所包围的是下半平面的 $+\Omega$，留数为 $-e^{-i\Omega\tau}/(2\Omega)$。再计入顺时针的负号，便有

<span id="eq:c07-contour-positive"></span>

$$
G_\eta(\tau>0)
=-i\left(-\frac{e^{-i\Omega\tau}}{2\Omega}\right)
=\frac{i}{2\Omega}e^{-i\Omega\tau}.
\tag{7.20}
$$

当 $\tau<0$ 时，围道包围上半平面的 $-\Omega$，其留数为 $e^{i\Omega\tau}/(2\Omega)$；这次方向为逆时针，因此

<span id="eq:c07-contour-negative"></span>

$$
G_\eta(\tau<0)
=i\frac{e^{i\Omega\tau}}{2\Omega}.
\tag{7.21}
$$

两支在原点连续，$\tau=0$ 时圆弧积分也仍然消失。将它们合并并取 $\eta\downarrow0$，就得到Green函数：

<span id="eq:c07-green-result"></span>

$$
G(\tau)=\frac{i}{2\omega}e^{-i\omega|\tau|}.
\tag{7.22}
$$

前面精确的哈密顿量处方也可作同样处理。若从式[（7.8）](#eq:c07-regulated-kernel)出发，分母为 $-A_{\epsilon_0}(E)$，留数计算给出 $i e^{-i\alpha\omega|\tau|}/(2\omega)$。在 $\epsilon_0\downarrow0$ 时，它趋于式[（7.22）](#eq:c07-green-result)，说明先前把正权重收入无穷小量没有改变这里的边界值。

Green方程中的delta源来自原点处的导数跳变。在 $\tau\ne0$ 处，两支指数都满足齐次振子方程；原点两侧的函数值和导数则为

<span id="eq:c07-derivative-jump"></span>

$$
G(0^+)=G(0^-)=\frac{i}{2\omega},
\qquad
G'(0^+)=\frac12,\qquad G'(0^-)=-\frac12.
\tag{7.23}
$$

取任意光滑紧支撑测试函数 $h$，在两条半轴上各分部积分两次。$G$ 连续，因此乘 $h'(0)$ 的两项边界贡献相消；乘 $h(0)$ 的项则为 $[G'(0^+)-G'(0^-)]h(0)=h(0)$。其余积分由齐次方程消去，留下

<span id="eq:c07-green-distribution"></span>

$$
\int d\tau\,G(\tau)[h''(\tau)+\omega^2h(\tau)]
=h(0),\qquad
(\partial_\tau^2+\omega^2)G(\tau)=\delta(\tau).
\tag{7.24}
$$

所以 $\delta$ 源来自一阶导数的跳变，其系数恰为一。Green函数在正时间支取正频率、负时间支取负频率；这与算符时间排序的关系，接下来由外源微分直接给出。

<span id="c07-correlators"></span>

## 从生成泛函求关联函数

所求外源泛函已经完全确定。使用第6节的插入公式，任意阶时间序关联函数为

<span id="eq:c07-generated-correlator"></span>

$$
\langle0|TQ(t_1)\cdots Q(t_n)|0\rangle
=\left.
\prod_{a=1}^{n}\frac1i\frac{\delta}{\delta f(t_a)}
Z[f]\right|_{f=0}.
\tag{7.25}
$$

每个 $1/i$ 抵消对 $e^{i\int fq}$ 求导时带下的因子。为看清连续微分怎样产生关联函数，先记

<span id="eq:c07-source-shorthand"></span>

$$
B[f]=\frac12\int dt\,dt'\,f(t)G(t-t')f(t'),
\qquad
F_s=\int dt\,G(s-t)f(t),\qquad
D_s=\frac1i\frac{\delta}{\delta f(s)}.
\tag{7.26}
$$

由于 $G(\tau)=G(-\tau)$，对 $B$ 中两份 $f$ 分别求导所得的两项相等，恰好抵消 $1/2$。再求一次导数时，它既作用于刚产生的源因子，也作用于整个指数，于是

<span id="eq:c07-two-derivatives"></span>

$$
D_sZ=F_sZ,\qquad
D_rD_sZ=
\left[\frac1iG(s-r)+F_sF_r\right]Z.
\tag{7.27}
$$

只有完成微分后再取 $f=0$，才会保留下所求插入。此时全部 $F_s$ 消失，得到二点函数

<span id="eq:c07-two-point"></span>

$$
C(t,t')\equiv\langle0|TQ(t)Q(t')|0\rangle
=\frac1iG(t-t')
=\frac1{2\omega}e^{-i\omega|t-t'|}.
\tag{7.28}
$$

因此，本节的约定是 $G=iC$。第5节所用的 $G_2$ 直接表示场的时间序矩阵元，对应这里的 $C$，与这里称为Green函数的 $G$ 相差一个因子。于是 $(\partial_t^2+\omega^2)C(t,t')=-i\delta(t-t')$，与前面由时间序微分得到的接触项一致。

再增加两个插入，只需继续微分同一个表达式，并保留那些最终可能在零源处成为常数的项。第三次导数为

<span id="eq:c07-three-derivatives"></span>

$$
D_uD_rD_sZ
=\left[
\frac{G(s-r)F_u+G(u-s)F_r+G(u-r)F_s}{i}
+F_uF_rF_s
\right]Z.
\tag{7.29}
$$

第四次导数作用于前三项各自的 $F$ 时，各产生一份常数；若作用于 $Z$，或作用于三次 $F$ 项，则仍至少留下两份源，零源处都不贡献。所以四点函数只含三项：

<span id="eq:c07-four-point"></span>

$$
\begin{aligned}
\langle0|TQ(t_1)Q(t_2)Q(t_3)Q(t_4)|0\rangle
=\frac1{i^2}\big[
&G(t_1-t_2)G(t_3-t_4)\\
+{}&G(t_1-t_3)G(t_2-t_4)\\
+{}&G(t_1-t_4)G(t_2-t_3)
\big].
\end{aligned}
\tag{7.30}
$$

每一项都是两份二点函数 $C$ 的乘积，分别对应四个插入的配对 $(12)(34)$、$(13)(24)$ 和 $(14)(23)$。四点计算中出现的这一结构，可以直接推广到任意偶数个插入。

<span id="c07-pairings"></span>

## 任意阶的配对公式

从源指数展开最容易看清一般系数。$B[f]$ 每次含有两份源，所以 $Z=e^{iB}$ 只有源的偶数次幂；奇数次求导无法在 $f=0$ 留下常数，奇数点基态关联因此为零。若有 $2n$ 个插入，则只有下面这一项能在全部微分后留下无源结果：

<span id="eq:c07-pairing-term"></span>

$$
\frac1{n!}\left(\frac i2\right)^n
\prod_{a=1}^{n}\int dt_a\,dt'_a\,
f(t_a)G(t_a-t'_a)f(t'_a).
\tag{7.31}
$$

将 $2n$ 个不同标号的导数分配到 $2n$ 份源上，共有 $(2n)!$ 种方式。不过，一组相同的无序配对会在这些分配中反复出现：每对内两位置的交换给 $2^n$，这 $n$ 对在二次因子之间的交换又给 $n!$。同一配对因而重复 $2^n n!$ 次，正好抵消指数展开的分母。再计入每次源导数的 $1/i$，总相位为 $i^{-2n}i^n=i^{-n}$，便得到任意偶数点的配对公式：

<span id="eq:c07-all-pairings"></span>

$$
\langle0|TQ(t_1)\cdots Q(t_{2n})|0\rangle
=\sum_{\mathcal P}\prod_{(a,b)\in\mathcal P}C(t_a,t_b)
=\frac1{i^n}\sum_{\mathcal P}
\prod_{(a,b)\in\mathcal P}G(t_a-t_b).
\tag{7.32}
$$

其中 $\mathcal P$ 只遍历不重复的两两配对，其总数为

<span id="eq:c07-pair-count"></span>

$$
N_{2n}=\frac{(2n)!}{2^n n!}=(2n-1)!!.
\tag{7.33}
$$

同一个数也可逐步构造出来：先给标号1选伙伴，有 $2n-1$ 种选择；其余 $2n-2$ 个标号再配对，便满足递推关系 $N_{2n}=(2n-1)N_{2n-2}$，初值为 $N_0=1$。

这说明谐振子基态的全部时间序位置关联，都由一个二点函数决定。若所有插入时刻相同，每个配对给出相同的等时二点值，于是

<span id="eq:c07-equal-time-moments"></span>

$$
\langle0|Q^{2n}|0\rangle
=(2n-1)!!\left(\frac1{2\omega}\right)^n,
\qquad
\langle0|Q^{2n+1}|0\rangle=0.
\tag{7.34}
$$

例如 $\langle Q^2\rangle=1/(2\omega)$、$\langle Q^4\rangle=3/(4\omega^2)$，正好是基态高斯波函数的矩。

## 升降算符与基态跃迁概率

升降算符给出同一结果的算符表示。恢复质量 $m$，取

<span id="eq:c07-ladder"></span>

$$
Q(t)=\frac{a e^{-i\omega t}+a^\dagger e^{i\omega t}}{\sqrt{2m\omega}},
\qquad [a,a^\dagger]=1,\qquad a|0\rangle=0.
$$

对 $t>t'$，展开两个 $Q$以后只有 $aa^\dagger$项的真空期望非零，因而

$$
\langle0|Q(t)Q(t')|0\rangle
=\frac{e^{-i\omega(t-t')}}{2m\omega}\langle0|aa^\dagger|0\rangle
=\frac{e^{-i\omega(t-t')}}{2m\omega}.
$$

时间排序把指数中的时间差改成绝对值，即恢复式[（7.28）](#eq:c07-two-point)。对四个已按时间排序的算符，最左端只留下湮灭部分；将它向右移，每经过一个产生部分都带下相应的二点收缩。它可以依次与其余三个算符配对，剩下两个再取真空期望，恰好得到式[（7.30）](#eq:c07-four-point)的三项。

生成泛函还直接给出外力撤去后仍留在基态的概率。对实外力，将式[（7.22）](#eq:c07-green-result)代入指数，恢复 $m$后有

<span id="eq:c07-ground-survival"></span>

$$
\begin{aligned}
\log Z[f]
&=-\frac1{4m\omega}\int dt\,dt'\,
 f(t)f(t')e^{-i\omega|t-t'|},\\
\log|Z[f]|^2
&=-\frac1{2m\omega}\int dt\,dt'\,
 f(t)f(t')\cos\bigl(\omega(t-t')\bigr).
\end{aligned}
$$

余弦是偶函数，因此第二行已去掉绝对值。再用实外力的 $\widetilde f(-\omega)=\widetilde f(\omega)^*$，两次时间积分分离为

$$
\int dt\,dt'\,f(t)f(t')e^{i\omega(t-t')}
=\widetilde f(\omega)\widetilde f(-\omega)
=|\widetilde f(\omega)|^2.
$$

于是

$$
P_{0\to0}=|Z[f]|^2
=\exp\!\left[-\frac{|\widetilde f(\omega)|^2}{2m\omega}\right].
$$

只有外力在振子频率 $\omega$处的傅里叶分量改变最终的基态概率；其余分量可以改变振幅相位。恢复 $\hbar$时，指数的分母为 $2m\hbar\omega$。[下一节](/posts/srednicki-08/)将把这个二次型积分和配对结构推广到自由标量场。

---

[← 第 6 节](/posts/srednicki-06/) · [章节地图](/srednicki/) · [第 8 节 →](/posts/srednicki-08/)
