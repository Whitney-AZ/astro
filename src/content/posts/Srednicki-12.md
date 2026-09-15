---
title: 'Srednicki §12 在 ℏ = c = 1 下的量纲分析'
date: 2026-09-14
category: 笔记
tags: [物理, 量子场论, Srednicki]
series: 'Srednicki QFT'
srednickiSections: [12]
hideFromHome: true
draft: false
---

<span id="c12"></span>

前面的散射计算已经表明，振幅和截面都带有确定的质量量纲。量纲还会影响耦合在不同能量下怎样进入微扰展开，并帮助我们选择接下来研究的理论。为此，先明确自然单位如何换算，再把作用量、场和耦合的量纲推广到一般 $d$ 维时空，最后转向六维立方理论。

<span id="c12-units"></span>

## 自然单位省去了哪些单位

光速使时间可以用长度表示，Planck常数又将长度与逆质量联系起来。选定一个能量单位 $E_0$ 后，与它相配的质量、长度和时间单位便可取为

<span id="eq:c12-natural-scales"></span>

$$
M_0=\frac{E_0}{c^2},\qquad
L_0=\frac{\hbar c}{E_0},\qquad
T_0=\frac{\hbar}{E_0}.
\tag{12.1}
$$

用这一组单位表示物理量时，$c$ 和 $\hbar$ 的数值都成为1。能量、质量和动量可以统一按能量的幂计数，长度和时间则按逆能量计数。把粒子质量写成GeV，就是这种记法；恢复普通单位后，相应的质量单位是GeV$/c^2$。

恢复单位的办法也可一般地写出。设物理量的机械量纲为 $M^aL^bT^r$，分别代入 $M=E/c^2$、$L=\hbar c/E$、$T=\hbar/E$，得到

<span id="eq:c12-unit-restoration"></span>

$$
M^aL^bT^r
\ \sim\ E^{a-b-r}\hbar^{b+r}c^{b-2a},
\qquad [A]=a-b-r.
\tag{12.2}
$$

这里 $\sim$ 表示量纲关系，$[A]$ 定义为自然单位中的质量幂指数。反过来换回普通单位时，须先知道 $A$ 代表哪个物理量，才能选定 $\hbar,c$ 的幂。例如能量、动量和质量虽然都有 $[A]=1$，恢复单位后却分别是 $E$、$E/c$ 和 $E/c^2$；同样，宽度换成每秒衰变率要用 $\Gamma/\hbar$，四维截面换成普通面积要用 $(\hbar c)^2\sigma$。

方括号记录的是幂指数，所以乘积满足 $[AB]=[A]+[B]$，商则对应指数相减。按 $x^0=ct$ 的坐标约定，所有 $x^\mu$ 都是长度，因而有

<span id="eq:c12-basic-dimensions"></span>

$$
[m]=1,\qquad [x^\mu]=-1,\qquad
[\partial_\mu]=1,\qquad [d^dx]=-d.
\tag{12.3}
$$

导数的维数由 $\partial_\mu x^\nu=\delta_\mu{}^\nu$ 确定：右边无量纲，导数恰好抵消坐标的长度维数。积分元 $d^dx$ 则由 $d$ 个长度微元相乘而成。这里 $d$ 表示时空维数，空间本身有 $d-1$ 维。

<span id="c12-field"></span>

## 从作用量求场的维数

有了坐标和导数的维数，就可以从拉氏量求场的维数。考虑具有标准动能的实标量理论：

<span id="eq:c12-polynomial-lagrangian"></span>

$$
\mathcal L=
-\frac12\partial^\mu\varphi\,\partial_\mu\varphi
-\frac12m^2\varphi^2
-\sum_{n=3}^N\frac{g_n}{n!}\varphi^n.
\tag{12.4}
$$

这里的多项式相互作用带负号。若与此前的 $+g\varphi^3/3!$ 表示同一相互作用，并保持时空维数和场归一化相同，应取 $g_3=-g$；两种记号于是分别给出 $-ig_3$ 与 $+ig$ 顶点，耦合的量纲相同。

决定量纲的起点是作用量在路径积分中的位置。写出作用量和生成泛函：

<span id="eq:c12-action-source"></span>

$$
S=\int d^dx\,\mathcal L,\qquad
Z[J]=\mathcal N\int\mathcal D\varphi\,
\exp\!\left[i\int d^dx\,(\mathcal L+J\varphi)\right].
\tag{12.5}
$$

其中 $\mathcal N$ 沿第6节取为使零源泛函归一的常数。要确定各项的单位，只须考察指数：恢复普通单位后，指数应写成 $iS_{\rm phys}/\hbar$。指数宗量必须无量纲，因而在 $\hbar=1$ 的记法中

<span id="eq:c12-action-dimension"></span>

$$
[S]=0,\qquad 0=[d^dx]+[\mathcal L]=-d+[\mathcal L],
\qquad [\mathcal L]=d.
\tag{12.6}
$$

物理作用量仍以作用量为单位，此处为零的是它在自然单位中的质量维数。

拉氏量的所有项必须具有同一维数。标准动能含两个导数，贡献2，两个场贡献 $2[\varphi]$，而系数 $-1/2$ 无量纲，因此

<span id="eq:c12-field-dimension"></span>

$$
2+2[\varphi]=d,\qquad [\varphi]=\frac{d-2}{2}.
\tag{12.7}
$$

质量项的维数也为 $[m^2\varphi^2]=2+(d-2)=d$，恰好与动能相同。外源项同样要求 $[J]+[\varphi]=d$，所以

<span id="eq:c12-source-dimension"></span>

$$
[J]=\frac{d+2}{2}.
\tag{12.8}
$$

由标准两导数动能这样确定的维数，称为工程维数（engineering dimension）或正则维数（canonical dimension）。它依赖场的归一化：若把场再乘一个有量纲的常数，动能系数也随之改变，计算时就要把这个系数的维数包括进去。量子关联函数的实际尺度变化还可能出现对数和反常维数（anomalous dimension），后面的重整化计算将说明它们怎样产生。

<span id="c12-couplings"></span>

## 耦合常数的维数

相互作用项含 $n$ 个场，共贡献 $n(d-2)/2$，而 $n!$ 只是无量纲的组合因子。要求每一项仍具有拉氏量的维数，便得到

<span id="eq:c12-coupling-dimension"></span>

$$
[g_n]+n[\varphi]=d,\qquad
[g_n]=d-\frac n2(d-2).
\tag{12.9}
$$

对立方项取三个场，有

<span id="eq:c12-cubic-dimension"></span>

$$
[g_3]=d-\frac32(d-2)=\frac{6-d}{2}.
\tag{12.10}
$$

在 $d=4$ 时，立方耦合有一个质量单位，与第9至11节的计算一致；在 $d=6$ 时，它成为无量纲量。用同一个公式计算其他幂次，可以直接比较两种时空维数中的结果：

| 相互作用    | $d=4$ 中的耦合维数 | $d=6$ 中的耦合维数 |
| ----------- | -----------------: | -----------------: |
| $\varphi^3$ |                $1$ |                $0$ |
| $\varphi^4$ |                $0$ |               $-2$ |
| $\varphi^5$ |               $-1$ |               $-4$ |
| $\varphi^6$ |               $-2$ |               $-6$ |

含导数的局部相互作用也按相同方式计数。若一项含 $n$ 个场、总计 $r$ 个导数，系数记为 $g_{n,r}$，则

<span id="eq:c12-derivative-coupling"></span>

$$
[g_{n,r}]=d-r-\frac n2(d-2).
\tag{12.11}
$$

例如 $\varphi(\partial\varphi)^2$ 在四维中有三个场和两个导数，其系数维数为 $4-2-3=-1$。四维中可把这一项写为 $c_1\varphi(\partial\varphi)^2/\Lambda$，其中 $c_1$ 无量纲，$\Lambda$ 具有质量量纲。

<span id="c12-high-energy"></span>

## 高能处真正参与展开的参数

耦合的维数影响它怎样进入振幅。为此分别考察耦合质量维数为正、负和零的情形。令硬能量尺度为 $Q=\sqrt s$，耦合维数为 $\kappa=[g]$；用能量的适当幂消去单位后，参与比较的无量纲参数为

<span id="eq:c12-dimensionless-coupling"></span>

$$
\widehat g(Q)=gQ^{-\kappa}=g\,s^{-[g]/2}.
\tag{12.12}
$$

若主要尺度是非零质量 $m$，也可以用 $gm^{-\kappa}$。应选择哪一个比值，取决于传播子中实际流过的动量，而不能只看总入射能量。

振幅自身带有的质量幂也要先提出。对只含 $\varphi^n$ 顶点的一幅连通图，设外腿数为 $N_{\rm ext}$、内线数为 $I$、顶点数为 $V$、圈数为 $\ell$。线端计数与生成树的圈数关系分别给出 $nV=2I+N_{\rm ext}$、$\ell=I-V+1$。把顶点、圈测度和传播子的维数相加，就有

<span id="eq:c12-amplitude-dimension"></span>

$$
\begin{aligned}
{}[\mathcal T_{N_{\rm ext}}]
&=V[g_n]+d\ell-2I\\
&=d+(d-2)I+V([g_n]-d)\\
&=d-\frac{N_{\rm ext}}2(d-2).
\end{aligned}
\tag{12.13}
$$

最后一步代入 $2I=nV-N_{\rm ext}$ 和式[（12.9）](#eq:c12-coupling-dimension)，全部 $V$ 项相消，所以同一外腿数的图无论处于哪一阶，都有相同的振幅维数。

对于只含 $m,g$ 的树幅，在固定角度的硬运动学区域，便可将量纲关系写成

<span id="eq:c12-amplitude-scaling-form"></span>

$$
\mathcal T_{N_{\rm ext}}
=Q^{\,d-N_{\rm ext}(d-2)/2}
F\!\left(\widehat g(Q),\frac mQ,\frac ts\right).
\tag{12.14}
$$

前面的能量幂由量纲固定，函数 $F$ 的具体形式则由动力学计算决定。若理论还有其他质量或耦合，就须加入相应的无量纲比值；使用调节尺度 $\Lambda$ 时，也要保留 $\Lambda/Q$。第11节的四维树幅就是一个例子：远离前、后向的角域以 $g^2/s$ 为小量，前向峰附近的交换过程却仍受 $m^2-t$ 控制。

先将 $g$ 的数值固定，只考察这种工程能量幂。若 $\kappa=-p<0$，定义 $\Lambda_g=|g|^{-1/p}$，就有

<span id="eq:c12-negative-dimension-scale"></span>

$$
|\widehat g(Q)|=|g|Q^p=\left(\frac Q{\Lambda_g}\right)^p.
\tag{12.15}
$$

在 $Q\ll\Lambda_g$ 时，无量纲参数可以很小；随着能量升至 $\Lambda_g$ 附近，这种微扰小量便不再存在。这一性质与负维耦合的微扰不可重整化性相联系，详细论证见[第18节](/posts/srednicki-18/#c18)。

从图的幂次计数也能看出问题的来源。暂时去掉各顶点的系数，只数积分在大动量下的幂，得到表面发散度

<span id="eq:c12-superficial-degree-bridge"></span>

$$
\omega=d\ell-2I
=d-\frac{N_{\rm ext}}2(d-2)-V[g_n].
\tag{12.16}
$$

这里先限于无导数顶点，并将所有独立圈动量同时放大；只有部分动量变大的子区域，还须分别检查。若 $[g_n]<0$，固定外腿数时 $\omega$ 会随顶点数增加，因而允许出现越来越高次的外动量局部项。原有有限个相互作用项通常不足以吸收所有阶的短距离贡献，第18节将由实际圈积分确定所需反项，第29节再讨论怎样按有效理论组织它们。

要求任意高阶精度时，一般需要不断增加输入参数。若只要求固定低能精度，可以按算符维数截断。例如六维实标量满足 $[\varphi]=2$，保留维数不超过 $D_{\max}$ 的局部项，就要求 $2n+r\le D_{\max}$。非负整数 $n,r$ 只有有限种取值，每种对应的有限多个Lorentz指标也只有有限种收缩，因此在固定截断内只需有限个系数。提高精度时再依次加入更高维项，便形成第29节的低能展开。

若 $\kappa>0$，则固定硬运动学区域中的 $\widehat g(Q)$ 随能量升高而减小。若 $\kappa=0$，便有 $\widehat g=g$，其尺度依赖由量子修正的对数项决定；后面的重整化计算将求出这些对数。

<span id="c12-six"></span>

## 从这里开始的六维理论

因此，接下来主要研究 $d=6$ 的 $\varphi^3$ 理论。此时有五个空间方向，工程维数为

<span id="eq:c12-six-dimensions"></span>

$$
[\mathcal L]=6,\qquad [\varphi]=2,\qquad
[J]=4,\qquad [g_3]=0.
\tag{12.17}
$$

这个选择保留了最简单的三价顶点，同时使耦合无量纲，因而适合用来展开后续重整化计算。

时空维数改变以后，模式归一化和积分测度也要一同改变。将正能模式及傅里叶表示延伸到 $d$ 维，得到

<span id="eq:c12-dimensional-measures"></span>

$$
\begin{aligned}
\langle\mathbf k|\mathbf q\rangle
&=(2\pi)^{d-1}2E_{\mathbf k}\,
\delta^{d-1}(\mathbf k-\mathbf q),\\
d\widetilde k&=\frac{d^{d-1}k}{(2\pi)^{d-1}2E_{\mathbf k}},
\qquad
\Delta(x)=\int\frac{d^dk}{(2\pi)^d}
\frac{e^{ikx}}{k^2+m^2-i0}.
\end{aligned}
\tag{12.18}
$$

这里仍沿用第3、8节的归一化，只是每个空间方向各提供一个动量delta及相应积分。位置传播核因此有 $[\Delta(x)]=d-2$，动量核仍为质量平方的倒数。由式[（12.13）](#eq:c12-amplitude-dimension)，六维四腿振幅的维数为 $-2$。

第11节相空间中 $16\pi^2$ 等具体系数来自三维空间的球坐标积分，继续适用于其四维问题；六维问题则要重新计算五维空间的角度积分。即使暂未完成这些积分，仍可先确定可观测量的量纲：$n$ 体相空间的维数为 $n(d-2)-d$，分别与两入射幅及通量、单入射幅及能量分母结合，得到

<span id="eq:c12-observable-dimensions"></span>

$$
\begin{aligned}
{}[\sigma]
&=2\left[d-\frac{n+2}{2}(d-2)\right]
+n(d-2)-d-2=2-d,\\
[\Gamma]
&=2\left[d-\frac{n+1}{2}(d-2)\right]
+n(d-2)-d-1=1.
\end{aligned}
\tag{12.19}
$$

所以六维截面的量纲是长度的四次方，衰变率仍是时间的倒数。四维截面的常用换算可以从 $\hbar c$ 直接算出。取国际单位制中的 $h=6.62607015\times10^{-34}\,\mathrm{J\,s}$、$c=299792458\,\mathrm{m/s}$，再用 $\hbar=h/(2\pi)$、$1\,\mathrm{GeV}=1.602176634\times10^{-10}\,\mathrm J$ 和 $1\,\mathrm{fm}=10^{-15}\,\mathrm m$，便有

<span id="eq:c12-numerical-conversion"></span>

$$
\begin{aligned}
\hbar c&=0.1973269804\ldots\;\mathrm{GeV\,fm},\\
1\,\mathrm{GeV}^{-1}&=0.1973269804\ldots\;\mathrm{fm},\\
1\,\mathrm{GeV}^{-2}&=0.0389379372\ldots\;\mathrm{fm}^2
=0.389379372\ldots\;\mathrm{mb}.
\end{aligned}
\tag{12.20}
$$

末行用了 $1\,\mathrm{mb}=10^{-31}\,\mathrm m^2=0.1\,\mathrm{fm}^2$。因此，把以 $\mathrm{GeV}^{-2}$ 算出的四维截面乘 $0.389379372\ldots$，就得到以毫靶恩表示的数值。衰变宽度则用 $\hbar=6.582119569\ldots\times10^{-25}\,\mathrm{GeV\,s}$ 换成寿命：$\tau=\hbar/\Gamma$。

---

[← 第 11 节](/posts/srednicki-11/) · [章节地图](/srednicki/) · [第 13 节 →](/posts/srednicki-13/)
