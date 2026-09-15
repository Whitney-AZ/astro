---
title: 'Srednicki §4 自旋–统计定理'
date: 2026-09-14
category: 笔记
tags: [物理, 量子场论, Srednicki]
series: 'Srednicki QFT'
srednickiSections: [4]
hideFromHome: true
draft: false
---

<span id="c04"></span>

上一节通过实标量场的正则量子化得到了自由玻色子的哈密顿量。现在直接从粒子的产生、湮灭算符出发，分别采用对易关系和反对易关系，尝试加入局域、洛伦兹不变的相互作用。相互作用的时间排序会将这个要求转化为类空分离处的对易条件，并由此选出玻色统计。

<span id="c04-free"></span>

## 自由模式与两支频率场

沿用第3节的 $c=\hbar=1$、$g=(-,+,+,+)$、
$\omega_{\mathbf k}=\sqrt{\mathbf k^2+m^2}$和
$d\widetilde k=d^3k/[(2\pi)^3 2\omega_{\mathbf k}]$。为了在同一计算中比较两种统计，记
$[A,B]_\sigma=AB-\sigma BA$，以 $\sigma=+1$表示CCR、$\sigma=-1$表示CAR。取自由哈密顿量和模式代数为

<span id="eq:c04-free"></span>

$$
\begin{gathered}
H_0=\int d\widetilde k\,\omega_{\mathbf k}a^\dagger_{\mathbf k}a_{\mathbf k},\\
[a_{\mathbf k},a_{\mathbf q}]_\sigma
=[a^\dagger_{\mathbf k},a^\dagger_{\mathbf q}]_\sigma=0,\qquad
[a_{\mathbf k},a^\dagger_{\mathbf q}]_\sigma
=(2\pi)^3 2\omega_{\mathbf k}\delta^3(\mathbf k-\mathbf q).
\end{gathered}
\tag{4.1}
$$

真空由所有 $a$湮灭。在有限盒中，$H_0=\sum_\alpha\omega_\alpha b^\dagger_\alpha b_\alpha$；玻色占据数为非负整数，费米占据数为0或1，因而两种选择都给出 $H_0\geq0$。这里直接规定了正规序的哈密顿量，与第3节在CAR下化为常数的对称排序 $H_{\rm sym}$是不同的选择。

要由这些模式组成场，先求它们的时间依赖。时间演化由 $H_0$的普通对易子决定：玻色情形沿用第3节，费米情形则使用恒等式
$[AB,C]=A\{B,C\}-\{A,C\}B$。取 $A=a^\dagger_{\mathbf q}$、$B=a_{\mathbf q}$后，第一项因 $\{a,a\}=0$消失，第二项保留前面的负号。积分掉归一化delta，两种统计都给出

<span id="eq:c04-evolution-comm"></span>

$$
[H_0,a_{\mathbf k}]=-\omega_{\mathbf k}a_{\mathbf k},\qquad
[H_0,a^\dagger_{\mathbf k}]=+\omega_{\mathbf k}a^\dagger_{\mathbf k}.
\tag{4.2}
$$

于是海森堡算符满足
$\frac{d}{dt}(e^{iH_0t}a_{\mathbf k}e^{-iH_0t})
=-i\omega_{\mathbf k}(e^{iH_0t}a_{\mathbf k}e^{-iH_0t})$。以 $a_{\mathbf k}$为初值，解得相位 $e^{-i\omega t}$；产生算符则取相反相位。将这些模式乘以空间平面波并按不变测度积分，便得到两支频率场：

<span id="eq:c04-frequency-parts"></span>

$$
\begin{aligned}
\varphi^+(x)&=\int d\widetilde k\,a_{\mathbf k}e^{ikx},\\
\varphi^-(x)&=\int d\widetilde k\,a^\dagger_{\mathbf k}e^{-ikx}
=\varphi^+(x)^\dagger,\qquad
\varphi=\varphi^++\varphi^-.
\end{aligned}
\tag{4.3}
$$

这里 $\varphi^+$ 含时间因子 $e^{-i\omega t}$，$\varphi^-$ 含 $e^{+i\omega t}$；两者的上标分别标记正、负频率。海森堡方程由偶算符 $H_0$ 的普通对易子生成，对两种统计都具有式[（4.2）](#eq:c04-evolution-comm)的形式。

两支频率场的变换可以从[上一节的模式变换](/posts/srednicki-03/#eq:c03-mode-lorentz)求出。那一步只用到标量变换律、不变测度和正负频率的分离，对两种统计都适用。把 $U^{-1}a(\mathbf k)U=a(\Lambda^{-1}\mathbf k)$ 代入第一份积分，再令 $k=\Lambda q$，得到

<span id="eq:c04-part-covariance"></span>

$$
U^{-1}\varphi^+(x)U
=\int d\widetilde q\,a(\mathbf q)e^{i(\Lambda q)x}
=\varphi^+(\Lambda^{-1}x).
\tag{4.4}
$$

取共轭便得到 $\varphi^-$的相同变换律。这里仍只作正规正时变换，以保持正能质量壳；$\Lambda^{-1}\mathbf k$表示四动量在壳变换后的空间部分。两支频率分量各为标量，所以它们的同点函数也可构成标量密度。这提供了构造相互作用密度的办法，但标量性还没有决定不同地点的相互作用怎样相容。要考察微观因果性（microcausality），须进一步比较类空分离处的算符次序。

<span id="c04-dyson"></span>

## 时间排序怎样引出类空对易条件

相互作用使这个问题通过时间排序显现出来。我们先在有限时间区间内导出含时微扰论的演化公式。令 $H=H_0+H_1$，把自由演化移入算符，定义相互作用绘景态
$|\psi_I(t)\rangle=e^{iH_0t}|\psi_S(t)\rangle$。求导时，指数给出的 $-H_0$项与薛定谔方程中的自由项抵消，留下

<span id="eq:c04-interaction-picture"></span>

$$
i\partial_t|\psi_I(t)\rangle=H_I(t)|\psi_I(t)\rangle,\qquad
H_I(t)=e^{iH_0t}H_1e^{-iH_0t}.
\tag{4.5}
$$

取 $H_1=\int d^3x\,\mathcal H_1(\mathbf x,0)$，其中密度是两频率场的厄米函数，暂取不含时间导数的相互作用。对其中每个场因子同时作共轭变换，便得到由 $\varphi^\pm(\mathbf x,t)$ 写出的同一个函数。这就是相互作用绘景中的密度 $\mathcal H_I(x)$。

演化算符满足初值 $U_I(t_0,t_0)=1$。将微分方程从初始时刻积分，得
$U_I(t,t_0)=1-i\int_{t_0}^t dt_1H_I(t_1)U_I(t_1,t_0)$。再用同一方程替换右侧的 $U_I$，便按相互作用的次数逐步展开，前两阶为

<span id="eq:c04-dyson-iterate"></span>

$$
\begin{aligned}
U_I(t,t_0)=1
&-i\int_{t_0}^t dt_1H_I(t_1)\\
&+(-i)^2\int_{t_0}^t dt_1\int_{t_0}^{t_1}dt_2\,
H_I(t_1)H_I(t_2)+\cdots .
\end{aligned}
\tag{4.6}
$$

每次迭代都把一个较早的演化放入已有积分，所以外面的时间不早于内面的时间，较晚的算符自动位于左边。第 $n$阶的积分域为
$t\geq t_1\geq\cdots\geq t_n\geq t_0$。整个时间立方体除去重合边界后，可分成 $n!$个这样的排列域；引入时间排序符号 $T$，把各域的算符都排成相同次序，就可改写为

<span id="eq:c04-dyson"></span>

$$
U_I(t,t_0)=
\sum_{n=0}^{\infty}\frac{(-i)^n}{n!}
\int_{t_0}^{t}dt_1\cdots dt_n\,
T[H_I(t_1)\cdots H_I(t_n)].
\tag{4.7}
$$

时间序指数中的 $1/n!$ 由此来自排列域的数目。场论微扰计算逐阶使用这个展开。对远过去制备、远未来探测的散射态，跃迁振幅写为 $\langle f|U_I(+\infty,-\infty)|i\rangle$；[下一节](/posts/srednicki-05/)将具体构造这些态的约化公式。

现在可以问：另一惯性系的观察者会不会把同一批相互作用排成不同次序？二阶项已经包含了全部关键。相互作用密度是物理偶算符，在两个非重合点上，时间排序为

<span id="eq:c04-time-order-two"></span>

$$
\begin{aligned}
T_t[\mathcal H_I(x)\mathcal H_I(y)]
={}&\theta(t_x-t_y)\mathcal H_I(x)\mathcal H_I(y)\\
&+\theta(t_y-t_x)\mathcal H_I(y)\mathcal H_I(x).
\end{aligned}
\tag{4.8}
$$

改用另一惯性系的时间函数 $\bar t$，密度的标量变换本身不造成差别，可能改变的是两个阶跃函数。将两种排序相减，得到

<span id="eq:c04-time-order-difference"></span>

$$
(T_t-T_{\bar t})[\mathcal H_I(x)\mathcal H_I(y)]
=\bigl[\theta(t_x-t_y)-\theta(\bar t_x-\bar t_y)\bigr]
[\mathcal H_I(x),\mathcal H_I(y)].
\tag{4.9}
$$

决定阶跃函数能否改变的是两点的间隔。若 $z=x-y$为类时向量，满足 $|\mathbf z|<|z^0|$，则对任意 $|\mathbf v|<1$，
$z'^0=\gamma(z^0-\mathbf v\cdot\mathbf z)$保持 $z^0$的符号。若为类空向量，则可选择沿 $\mathbf z$的速度，使它跨过 $|\mathbf v|=|z^0|/|\mathbf z|<1$，从而颠倒两点的时间次序。按本节度规，类时为 $z^2<0$，类空为 $z^2>0$。

因此，只有类空分离的点对会在两种排序中交换位置。要求

<span id="eq:c04-density-locality"></span>

$$
[\mathcal H_I(x),\mathcal H_I(y)]=0
\quad\text{当 }(x-y)^2>0
\tag{4.10}
$$

就能消去这种次序翻转在二阶造成的差别。更高阶也可逐对处理：把目标排序中的第一个点依次移过挡在它前面的点，再对余下序列重复。每次交换的都是两套时间序中次序相反的点对，而这种点对必为类空，所以类空对易性使非重合点处的每一阶时间排序都与参考系无关。

这给出构造局域相互作用的条件：密度在类空分离处普通对易。对于费米场，类空反对易的场构成偶数次复合量后，也可以满足同一个条件。我们下面求出标量模式构成的场能否具有所需的交换性质；重合点的乘积在后面的重整化计算中处理。

<span id="c04-kernel"></span>

## 正频率核的积分

现在回到两支频率场，计算决定其类空局域性的括号。同频率的两项由模式代数直接给零；混合括号则留下

<span id="eq:c04-wightman"></span>

$$
\begin{aligned}
\relax[\varphi^+(x),\varphi^-(y)]_\sigma
&=\int d\widetilde k\,d\widetilde q\,
e^{ikx-iqy}[a_{\mathbf k},a^\dagger_{\mathbf q}]_\sigma\\
&=\int d\widetilde k\,e^{ik(x-y)}\equiv W_+(x-y).
\end{aligned}
\tag{4.11}
$$

delta先积掉 $\mathbf q$，其归一化恰好消去 $d\widetilde q$的分母，因而只剩一份不变测度。这个正频两点核（positive-frequency two-point kernel）也等于所选真空的
$\langle0|\varphi(x)\varphi(y)|0\rangle$，因为真空期望只保留湮灭算符在左、产生算符在右的项。

第3节已证明测度不变，所以 $W_+$在正规正时变换下是标量。对于类空的 $z=x-y$，可以选取 $z'^0=0$的参考系，令 $r=\sqrt{z^2}>0$，把计算化为等时的三维积分。沿 $\mathbf z$取极轴后，角积分为
$2\pi\int_{-1}^1d\mu\,e^{ikr\mu}=4\pi\sin(kr)/(kr)$，于是

<span id="eq:c04-radial"></span>

$$
C(r)\equiv W_+(z)
=\frac1{4\pi^2r}\int_0^\infty dk\,
\frac{k\sin(kr)}{\sqrt{k^2+m^2}}.
\tag{4.12}
$$

式[（4.12）](#eq:c04-radial)是振荡积分，按傅里叶分布的意义取极限。在 $r>0$ 处，可以把它化为一个收敛的参数积分来求值。先用 Gamma 函数的积分表示改写平方根的倒数：

<span id="eq:c04-inverse-sqrt"></span>

$$
\frac1{2\sqrt{\mathbf k^2+m^2}}
=\frac1{2\sqrt\pi}\int_0^\infty ds\,s^{-1/2}
e^{-s(\mathbf k^2+m^2)}.
\tag{4.13}
$$

令 $u=s(\mathbf k^2+m^2)$，右侧积分即为
$\Gamma(1/2)/[2\sqrt\pi\sqrt{\mathbf k^2+m^2}]$，利用 $\Gamma(1/2)=\sqrt\pi$ 就得到左侧。先把 $s$ 限制在 $[\epsilon,R]$，交换积分次序后，三个动量方向分别给出高斯积分：

$$
\begin{aligned}
\int\frac{dk_j}{2\pi}e^{-sk_j^2+ik_jz_j}
&=\frac{e^{-z_j^2/(4s)}}{\sqrt{4\pi s}},\\
\int\frac{d^3k}{(2\pi)^3}e^{-s\mathbf k^2+i\mathbf k\cdot\mathbf z}
&=(4\pi s)^{-3/2}e^{-r^2/(4s)}.
\end{aligned}
$$

第一式通过配方 $-sk_j^2+ik_jz_j=-s(k_j-iz_j/2s)^2-z_j^2/4s$ 得到，第二式是三个方向的乘积。乘上式[（4.13）](#eq:c04-inverse-sqrt)中的 $s^{-1/2}/(2\sqrt\pi)$，便有

<span id="eq:c04-heat-kernel"></span>

$$
C(r)=\frac1{16\pi^2}\int_0^\infty\frac{ds}{s^2}
\exp\left(-m^2s-\frac{r^2}{4s}\right),\qquad r>0.
\tag{4.14}
$$

对 $r\geq r_0>0$，积分下端由 $s^{-2}e^{-r_0^2/(4s)}$ 控制，上端由 $s^{-2}$ 控制，两端都可积。因此可以取 $\epsilon\to0$、$R\to\infty$，得到类空分离处的两点核。

为了把积分化为便于求极限的形式，令 $v=r^2/(4s)$。由
$ds/s^2=-4\,dv/r^2$，并交换积分上下限，得到

<span id="eq:c04-v-integral"></span>

$$
C(r)=\frac1{4\pi^2r^2}\int_0^\infty dv\,
e^{-v-(mr)^2/(4v)}.
\tag{4.15}
$$

在 $m>0$时，进一步令 $z=mr$、$v=(z/2)e^u$，所以
$dv=(z/2)e^u du$，指数化为 $-z\cosh u$。将正、负 $u$半轴的贡献配对，便有

<span id="eq:c04-bessel-evaluation"></span>

$$
\begin{aligned}
\int_0^\infty dv\,e^{-v-z^2/(4v)}
&=\frac z2\int_{-\infty}^{\infty}du\,e^u e^{-z\cosh u}\\
&=z\int_0^\infty du\,\cosh u\,e^{-z\cosh u}
\equiv zK_1(z).
\end{aligned}
\tag{4.16}
$$

这里引入了修正 Bessel 函数的积分表示 $K_\nu(z)=\int_0^\infty e^{-z\cosh u}\cosh(\nu u)\,du$，当前取指标 $\nu=1$。

也可以直接从积分确认它是哪一支Bessel函数。在 $z>0$处求两次导数，组合
$z^2K_1''+zK_1'-(z^2+1)K_1$的被积函数可整理为全导数：

<span id="eq:c04-bessel-ode-check"></span>

$$
-z\frac{d}{du}\left(\sinh u\cosh u\,e^{-z\cosh u}\right)
-\frac{d}{du}\left(\sinh u\,e^{-z\cosh u}\right).
\tag{4.17}
$$

在下限处，两项都含 $\sinh0=0$，在无穷远又都受指数压制，故积分为零，函数满足一阶指标的修正Bessel方程。还须用大参数行为选定其中的解：当 $z$很大时，主导区域为 $u=O(z^{-1/2})$。代入
$\cosh u=1+u^2/2+O(u^4)$和 $u=w/\sqrt z$，得到
$K_1(z)\sim e^{-z}z^{-1/2}\int_0^\infty e^{-w^2/2}dw
=\sqrt{\pi/(2z)}e^{-z}$，正是通常的衰减归一化。积分及其导数由 $e^{-z\cosh u}$控制；大参数估计时可以先限制小 $u$区域，外部因 $\cosh u>1$而有更强的指数压制。

将这些结果代回两点核，得到完整表达式及其零质量极限：

<span id="eq:c04-kernel-final"></span>

$$
C_m(r)=\frac{m}{4\pi^2r}K_1(mr),\quad m>0;\qquad
C_0(r)=\frac1{4\pi^2r^2},\quad r>0.
\tag{4.18}
$$

在式[（4.15）](#eq:c04-v-integral)中，被积函数由 $e^{-v}$ 支配，所以可将 $m\to0$ 移入积分，只剩 $\int_0^\infty e^{-v}dv=1$，这直接给出零质量结果。同一个正积分表示还说明，对所有 $r>0$、$m\geq0$，都有 $C(r)>0$。它的质量维数为 2，与两场乘积一致；在大 $mr$ 时虽按指数衰减，在任何有限类空距离上仍为正。

<span id="c04-lambda"></span>

## 哪些线性场组合可以局域

类空分离时可转到等时参考系，因而 $W_+(z)=W_+(-z)=C(r)$。另一方面，两种统计的换序规律统一为 $[B,A]_\sigma=-\sigma[A,B]_\sigma$，所以反向混合括号为

<span id="eq:c04-reversed-bracket"></span>

$$
[\varphi^-(x),\varphi^+(y)]_\sigma=-\sigma C(r),\qquad
[\varphi^\pm(x),\varphi^\pm(y)]_\sigma=0.
\tag{4.19}
$$

单独的正、负频率部分既然有非零的混合核，仅凭它们都是标量，还不能保证任意厄米相互作用密度满足式[（4.10）](#eq:c04-density-locality)。一个可能的办法是把两支混合起来，让正向和反向核抵消。为此取单种模式的线性组合

<span id="eq:c04-lambda-definition"></span>

$$
\varphi_\lambda=\varphi^++\lambda\varphi^-,
\qquad
\varphi_\lambda^\dagger=\varphi^-+\lambda^*\varphi^+.
\tag{4.20}
$$

要同时检验场与自身以及与共轭场的局域性，将两个括号都逐项展开。同频率项为零，混合项则带着各自的系数，得到

<span id="eq:c04-lambda-test"></span>

$$
\begin{aligned}
\relax[\varphi_\lambda(x),\varphi_\lambda^\dagger(y)]_\sigma
&=C(r)+|\lambda|^2[-\sigma C(r)]
=(1-\sigma|\lambda|^2)C(r),\\
[\varphi_\lambda(x),\varphi_\lambda(y)]_\sigma
&=\lambda C(r)+\lambda[-\sigma C(r)]
=\lambda(1-\sigma)C(r).
\end{aligned}
\tag{4.21}
$$

两种统计的差别现在清楚了。对CCR，第二式自动为零，第一式因 $C(r)>0$而要求 $|\lambda|=1$。对CAR，第一式却是 $(1+|\lambda|^2)C(r)>0$，任何复 $\lambda$都无法消去；取 $\lambda=0$也只能令第二式为零。因此，在这种单种正能标量模式的线性构造中，玻色统计可以给出场及其共轭的类空分次局域关系，费米统计则不能。

玻色情形剩余的选择只是一项常相位。对允许的 $\lambda=e^{i\alpha}$，令
$\chi=e^{-i\alpha/2}\varphi_\lambda$，得到

<span id="eq:c04-rephase"></span>

$$
\chi=e^{-i\alpha/2}\varphi^++e^{i\alpha/2}\varphi^-,
\qquad \chi^\dagger=\chi.
\tag{4.22}
$$

定义新模式 $b=e^{-i\alpha/2}a$、
$b^\dagger=e^{i\alpha/2}a^\dagger$后，混合括号中的相位相消，代数不变，$\chi$就是由 $b,b^\dagger$构造的标准实场。反过来，旧模式由 $a=e^{i\alpha/2}b$表达。因此，这个常相位可完全吸收入模式定义。

对所得玻色实场，$[\chi(x),\chi(y)]=C(r)-C(r)=0$。用正规乘积定义同点多项式后，反复使用乘积对易法则便得类空分离处 $[:\!\chi(x)^n\!:,:\!\chi(y)^l\!:]=0$。因此可以用这些局域多项式构造满足式[（4.10）](#eq:c04-density-locality)的相互作用密度。

类空两点函数 $W_+(z)$ 描述真空相关，局域扰动的响应则由对易子控制。例如取类空分离区域中的有界自伴可观测量 $A,B$，由 $[A,B]=0$ 得

$$
\frac{d}{d\epsilon}\left(e^{-i\epsilon B}Ae^{i\epsilon B}\right)
=-ie^{-i\epsilon B}[B,A]e^{i\epsilon B}=0.
$$

因此 $e^{-i\epsilon B}Ae^{i\epsilon B}=A$：在 $B$ 所在区域施加这个扰动，$A$ 的测量结果保持不变。真空的类空相关与局域响应的因果性由两个不同的量描述。

<span id="c04-scope"></span>

## 自旋与统计

对本节的正能标量模式，类空局域性要求采用对易关系，并将正、负频率部分以模为一的相对系数组合。吸收一个常相位以后，所得就是上一节的厄米实标量场。

还可以从等时场的厄米性看出，把全部正则括号换成反对易子会发生什么。若要求任意空间点对满足 $\{\varphi(\mathbf x,t),\varphi(\mathbf y,t)\}=0$，用实测试函数积分得到厄米算符 $\Phi_f$，则

$$
2\Phi_f^2=\{\Phi_f,\Phi_f\}=0,
\qquad
\|\Phi_f|\psi\rangle\|^2
=\langle\psi|\Phi_f^2|\psi\rangle=0.
$$

正定内积因而迫使 $\Phi_f$ 为零。非平凡的厄米标量场应当采用上一节的正则对易关系。

四维相对论局域场论中的一般自旋–统计定理，将这一联系推广到具有正定态空间、不变真空和正能量谱的协变场。用 $j=0,1$ 分别表示玻色、费米的交换奇偶性，其结论为

<span id="eq:c04-imported-theorem"></span>

$$
(-1)^j=(-1)^{2s}.
\tag{4.23}
$$

整数自旋对应玻色统计，半整数自旋对应费米统计。本节从正频率核出发得到了自旋零的结果；[第37节](/posts/srednicki-37/)的旋量量子化将具体展示半整数自旋场中的统计选择。

---

[← 第 3 节](/posts/srednicki-03/) · [章节地图](/srednicki/) · [第 5 节 →](/posts/srednicki-05/)
