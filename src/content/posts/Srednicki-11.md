---
title: 'Srednicki §11 截面与衰变率'
date: 2026-09-14
category: 笔记
tags: [物理, 量子场论, Srednicki]
series: 'Srednicki QFT'
srednickiSections: [11]
hideFromHome: true
draft: false
---

<span id="c11"></span>

上一节已经得到散射振幅。要与实验比较，还需算出有多少粒子进入指定的角度范围，或一批不稳定粒子在单位时间内有多少发生衰变。前一种测量由截面描述，后一种由衰变率描述。从两个粒子散射为两个粒子的过程出发，先确定运动学，再把振幅平方与态的归一化、末态相空间及入射通量结合起来，最后用于 $\varphi^3$ 理论的角分布和总截面。

<span id="c11-kinematics"></span>

## 两体运动学

将入射四动量记为 $k_1,k_2$，出射四动量记为 $k_1',k_2'$。为了使运动学结果以后也能用于其他过程，暂且允许四条外腿的质量不同，并取正能量：

<span id="eq:c11-shell-conservation"></span>

$$
k_1+k_2=k_1'+k_2',\qquad
k_i^2=-m_i^2,\quad k_j'^2=-m_j'^2,\qquad k_i^0,k_j'^0>0.
\tag{11.1}
$$

在质心系（center-of-mass frame，CM）中，$\mathbf k_1=-\mathbf k_2$、$\mathbf k_1'=-\mathbf k_2'$。把入射方向选为 $+z$，再记 $p=|\mathbf k_1|$、$p'=|\mathbf k_1'|$，则初态只剩一个连续参数，也可用总能量 $E_1+E_2$ 表示。对于没有自旋的粒子，绕入射轴转动不改变初态，所以出射角分布只须依赖极角 $\theta$。

为使结果便于在不同参考系之间使用，引入三个Mandelstam变量：

<span id="eq:c11-mandelstam"></span>

$$
\begin{aligned}
s&=-(k_1+k_2)^2=-(k_1'+k_2')^2,\\
t&=-(k_1-k_1')^2=-(k_2-k_2')^2,\\
u&=-(k_1-k_2')^2=-(k_2-k_1')^2.
\end{aligned}
\tag{11.2}
$$

每行的两种写法都由四动量守恒联系起来。例如 $k_1-k_1'=k_2'-k_2$，平方后右边的整体负号便消失。在CM系，$s=(E_1+E_2)^2$，因此 $\sqrt s$ 就是总能量。

先用它求入射动量大小 $p$。由 $E_2=\sqrt s-E_1$ 及两个质量壳关系之差 $E_2^2-E_1^2=m_2^2-m_1^2$，得到

<span id="eq:c11-cm-energies"></span>

$$
s-2\sqrt s\,E_1=m_2^2-m_1^2,\qquad
E_1=\frac{s+m_1^2-m_2^2}{2\sqrt s},\quad
E_2=\frac{s+m_2^2-m_1^2}{2\sqrt s}.
\tag{11.3}
$$

能量确定以后，再用 $p^2=E_1^2-m_1^2$ 求动量。结果中反复出现的质量多项式可记为Källén函数：

<span id="eq:c11-kallen"></span>

$$
\begin{aligned}
\lambda(a,b,c)&=a^2+b^2+c^2-2ab-2ac-2bc,\\
p^2&=\frac{(s+m_1^2-m_2^2)^2-4sm_1^2}{4s}
=\frac{\lambda(s,m_1^2,m_2^2)}{4s}.
\end{aligned}
\tag{11.4}
$$

入射动量因此已由总能量与两质量确定。出射端仍有同一总能量 $\sqrt s$，因此把 $m_1,m_2$ 换成 $m_1',m_2'$，同样得到

<span id="eq:c11-in-out-radii"></span>

$$
p=\frac{\sqrt{\lambda(s,m_1^2,m_2^2)}}{2\sqrt s},
\qquad
p'=\frac{\sqrt{\lambda(s,m_1'^2,m_2'^2)}}{2\sqrt s}.
\tag{11.5}
$$

根号中的函数可分解为 $\lambda(s,m_a^2,m_b^2)=[s-(m_a+m_b)^2][s-(m_a-m_b)^2]$。正能两粒子的总能量要求 $\sqrt s\ge m_a+m_b$，这便是物理阈值；虽然根式在 $s\le(m_a-m_b)^2$ 也可为实数，那一支却不满足正能总和的条件。实际散射还须同时满足出射端的阈值。

接着看角度。用 $(-+++)$ 度规展开 $t$，得到

<span id="eq:c11-t-angle"></span>

$$
t=m_1^2+m_1'^2-2E_1E_1'
+2|\mathbf k_1|\,|\mathbf k_1'|\cos\theta.
\tag{11.6}
$$

这个展开没有使用CM条件，因而在任意参考系都成立，只须将能量、动量和夹角取在同一参考系。在CM中，一旦固定 $s$，各能量和 $p,p'$ 也随之确定，变化的便只有 $\cos\theta$。

三个Mandelstam变量还满足一条关系。展开各自的平方后，含 $k_1$ 的交叉项合为 $2k_1\cdot(-k_2+k_1'+k_2')=2k_1^2=-2m_1^2$，因此

<span id="eq:c11-stu-sum"></span>

$$
s+t+u=m_1^2+m_2^2+m_1'^2+m_2'^2.
\tag{11.7}
$$

两体运动学只需要其中两个独立变量，例如 $s,t$。这也使[上一节三个树图](/posts/srednicki-10/#c10-momentum)的结果更紧凑：回到四条外腿质量均为 $m$ 的 $\varphi^3$ 理论，树级振幅为

<span id="eq:c11-tree-amplitude"></span>

$$
\begin{aligned}
\mathcal T_{\rm tree}
&=g^2\Bigg[
\frac1{(k_1+k_2)^2+m^2-i0}
+\frac1{(k_1-k_1')^2+m^2-i0}\\
&\hspace{6em}+\frac1{(k_1-k_2')^2+m^2-i0}\Bigg]\\
&=g^2\left[\frac1{m^2-s}+\frac1{m^2-t}+\frac1{m^2-u}\right].
\end{aligned}
\tag{11.8}
$$

第二行取在物理弹性区 $s\ge4m^2$、$t,u\le0$；当 $m>0$ 时，三个内线极点都不在这个区域内，便可省去边界记号。完整振幅还含 $O(g^4)$ 的圈修正。前面的不同质量推广只涉及运动学，使用这里的具体三道振幅时，已经回到同一种实标量粒子。

在许多实验中，一个入射粒子原先静止，使用固定靶系（fixed-target frame，FT）更方便。令 $k_2=(m_2,\mathbf0)$，其中 $m_2>0$，展开总四动量平方便有

<span id="eq:c11-fixed-target"></span>

$$
\begin{aligned}
s&=m_1^2+m_2^2+2m_2E_{1,\rm FT},\\
E_{1,\rm FT}&=\frac{s-m_1^2-m_2^2}{2m_2},\\
p_{\rm FT}
&=\sqrt{E_{1,\rm FT}^2-m_1^2}
=\frac{\sqrt{\lambda(s,m_1^2,m_2^2)}}{2m_2}.
\end{aligned}
\tag{11.9}
$$

把这里的入射动量与CM的式[（11.5）](#eq:c11-in-out-radii)比较，两式根号相同而分母不同，于是得到

<span id="eq:c11-ft-cm-bridge"></span>

$$
m_2p_{\rm FT}=p\sqrt s.
\tag{11.10}
$$

这个关系将在后面把固定靶系的通量分母换成不变量。

<span id="c11-rate"></span>

## 从平面波振幅到跃迁率

运动学确定了哪些末态可能出现，发生指定跃迁的概率则还需由振幅和态的范数求出。采用大盒与长时间的办法，取盒边长 $L$，体积 $V=L^3$，实验时长记为 $\tau$。现在允许两个入射粒子产生 $n$ 个出射粒子，并先让各末态动量落在可分辨的小区间内。按上一节的定义，连通散射部分为

<span id="eq:c11-amplitude-definition"></span>

$$
S_{fi}^{\rm conn}
=(2\pi)^4\delta^4(K_{\rm in}-K_{\rm out})\,i\mathcal T,
\qquad
K_{\rm in}=k_1+k_2,\quad K_{\rm out}=\sum_{j=1}^nk_j'.
\tag{11.11}
$$

入射束中未散射的部分已在第10节分开，此处计算的是指定跃迁。有限盒中不同末态彼此正交，量子力学的概率规则要求先把初、末动量态化为单位归一化，因而

<span id="eq:c11-transition-probability"></span>

$$
P_{i\to f}=\frac{|S_{fi}^{\rm conn}|^2}
{\langle i|i\rangle\langle f|f\rangle}.
\tag{11.12}
$$

分母来自相对论动量态的范数。分子先在有限的 $\tau,L$ 下计算，再对末态区间求和；无限时空中的守恒 delta 由这个极限产生。

先处理时间方向。能量差 $\omega$ 在有限时间窗中产生

<span id="eq:c11-time-window"></span>

$$
F_\tau(\omega)=\int_{-\tau/2}^{\tau/2}dt\,e^{i\omega t}
=\frac{2\sin(\omega\tau/2)}{\omega},\qquad F_\tau(0)=\tau.
\tag{11.13}
$$

虽然 $F_\tau$ 本身趋向 $2\pi\delta(\omega)$，求单位时间的概率所需的却是 $|F_\tau|^2/\tau$。为了求这个极限，取光滑且迅速衰减的函数 $f(\omega)$，记 $\widehat f(u)=\int d\omega\,e^{i\omega u}f(\omega)/(2\pi)$。将模平方写成两个时间积分，再用时间差 $u=t-t'$ 作变量；固定时间差后，可用的区间长度是 $\tau-|u|$，所以

<span id="eq:c11-window-weak-limit"></span>

$$
\begin{aligned}
\int\frac{d\omega}{2\pi}\,
f(\omega)\frac{|F_\tau(\omega)|^2}{\tau}
&=\frac1\tau\int_{-\tau/2}^{\tau/2}dt\,dt'\,\widehat f(t-t')\\
&=\int_{-\tau}^{\tau}du
\left(1-\frac{|u|}{\tau}\right)\widehat f(u)
\ \longrightarrow\ \int_{-\infty}^{\infty}du\,\widehat f(u)
=f(0).
\end{aligned}
\tag{11.14}
$$

因为 $\widehat f$ 可积，括号中的权重又始终介于0与1之间，最后的极限可以移入积分。这就得到末态能量积分中所需的分布极限 $|F_\tau|^2/\tau\to2\pi\delta(\omega)$。

空间的三个方向各作同样的有限窗计算。令 $W_{\tau,L}(Q)=\int_{\rm window}d^4x\,e^{iQx}$，时间相位的负号在模平方中没有影响，于是

<span id="eq:c11-four-window-limit"></span>

$$
\frac{|W_{\tau,L}(Q)|^2}{V\tau}
\ \longrightarrow\ (2\pi)^4\delta^4(Q).
\tag{11.15}
$$

这个分布极限通常简写成 $\big[(2\pi)^4\delta^4(Q)\big]^2
=(2\pi)^4\delta^4(Q)\,V\tau$。若保持周期空间盒，空间积分给 $V\delta_{\mathbf n_{\rm in},\mathbf n_{\rm out}}$；Kronecker符号的平方等于自身，再以 $\delta_{\mathbf n_{\rm in},\mathbf n_{\rm out}}
\to(2\pi)^3\delta^3(\mathbf Q)/V$ 换回连续记号，
同样留下上述一个 $V$。

取足够大的盒子，使宽度约为 $1/\tau$ 的能量区间内含有许多末态模式。观察时间长于微观振荡时间，而当前微扰阶内的跃迁概率仍小；此时末态积分后随 $\tau$ 线性增长的系数给出跃迁率，振幅模平方写成

<span id="eq:c11-squared-amplitude"></span>

$$
|S_{fi}^{\rm conn}|^2
\ \longrightarrow\
V\tau(2\pi)^4\delta^4(K_{\rm in}-K_{\rm out})|\mathcal T|^2.
\tag{11.16}
$$

接着求初、末态的范数。周期盒的动量为 $\mathbf k=2\pi\mathbf n/L$，原来的连续归一化转为 $\langle\mathbf k_{\mathbf n}|\mathbf k_{\mathbf m}\rangle
=2E_{\mathbf n}V\,\delta_{\mathbf n\mathbf m}$。两个不同入射模式及 $n$ 个不同出射模式便分别给出

<span id="eq:c11-box-norms"></span>

$$
\langle k|k\rangle=2EV,\qquad
\langle i|i\rangle=4E_1E_2V^2,\qquad
\langle f|f\rangle=\prod_{j=1}^n(2E_j'V).
\tag{11.17}
$$

把湮灭算符逐个移过产生算符时，不同模式之间的收缩为零，只留下每个模式自身的 $2EV$。若同一种粒子有 $r$ 个占据同一离散模式，则相应范数为 $\langle0|a^r(a^\dagger)^r|0\rangle=r!(2EV)^r$。这些重合动量在通常的连续积分中组成零测集；稍后使用Fock空间完备关系时，也会将它们的阶乘统一包括进去。

现在把式[（11.16）](#eq:c11-squared-amplitude)及这些范数代入跃迁概率，再除以 $\tau$，得到指定离散末态的率：

<span id="eq:c11-discrete-rate"></span>

$$
\dot P_f=
\frac{V(2\pi)^4\delta^4(K_{\rm in}-K_{\rm out})|\mathcal T|^2}
{4E_1E_2V^2\prod_{j=1}^n(2E_j'V)}.
\tag{11.18}
$$

测量所接受的末态不是单个精确动量，而是一个动量区间。盒内每个允许动量占据的三维格子体积为 $(2\pi/L)^3$，因此在大盒极限下，对区间内模式求和就成为

<span id="eq:c11-mode-density"></span>

$$
\sum_{\mathbf n_j'}\longrightarrow
\frac{V}{(2\pi)^3}\int d^3k_j',
\qquad
\frac1{2E_j'V}\frac{V\,d^3k_j'}{(2\pi)^3}
=d\widetilde k_j'.
\tag{11.19}
$$

每条出射腿的态密度消去其范数中的 $V$，留下正能不变测度。对全部出射腿作同样处理，得到

<span id="eq:c11-continuum-rate"></span>

$$
d\dot P=
\frac{|\mathcal T|^2}{4E_1E_2V}
(2\pi)^4\delta^4(K_{\rm in}-K_{\rm out})
\prod_{j=1}^n d\widetilde k_j',
\qquad
d\widetilde k_j'=\frac{d^3k_j'}{(2\pi)^3\,2E_j'}.
\tag{11.20}
$$

尚存的 $1/V$ 表示盒内仅有一个入射粒子和一个靶粒子：体积越大，两者相遇的机会越少。截面正是要将这种入射粒子稀疏程度除去，留下过程本身的散射强度。

<span id="c11-flux"></span>

## 入射通量与不变截面

先在固定靶系定义截面。靶粒子静止，入射粒子的数密度为 $1/V$，速率为 $v=p_{\rm FT}/E_1$。于是入射通量 $j_{\rm in}=v/V$ 就是每单位时间穿过单位面积的粒子数。按 $d\dot P=j_{\rm in}d\sigma$ 定义截面，再用式[（11.20）](#eq:c11-continuum-rate)的率除以通量，得到

<span id="eq:c11-ft-cross-section"></span>

$$
d\sigma
=\frac{|\mathcal T|^2}{4m_2p_{\rm FT}}\,
d{\rm LIPS}_n(K),\qquad
d{\rm LIPS}_n(K)\equiv
(2\pi)^4\delta^4\!\left(K-\sum_{j=1}^nk_j'\right)
\prod_{j=1}^n d\widetilde k_j'.
\tag{11.21}
$$

这里 $K=k_1+k_2$，LIPS是Lorentz不变相空间（Lorentz-invariant phase space）的缩写。它将各出射粒子的可用动量态与总四动量守恒合在一起；目前仍给每条出射腿不同标签，相同粒子带来的重复计数稍后处理。

相空间的不变性可以直接从测度看出。将第3节的正能测度改写为

<span id="eq:c11-invariant-shell-measure"></span>

$$
d\widetilde k=
\frac{d^4k}{(2\pi)^3}\,\theta(k^0)\delta(k^2+m^2).
\tag{11.22}
$$

对能量积分时，正根是 $k^0=E_{\mathbf k}$，delta宗量在根处的导数绝对值为 $2E_{\mathbf k}$，因此右边恢复原来的三动量测度。正时向Lorentz变换保持质量壳和 $\theta(k^0)$，四维体积元与总动量delta的Jacobian又都是1，所以整个 $d{\rm LIPS}_n$ 保持不变。

通量分母也可用不变量表示。由 $k_1\cdot k_2=(m_1^2+m_2^2-s)/2$，有

<span id="eq:c11-invariant-flux"></span>

$$
\mathcal F\equiv\sqrt{(k_1\cdot k_2)^2-m_1^2m_2^2}
=\frac{\sqrt{\lambda(s,m_1^2,m_2^2)}}2
=p\sqrt s=m_2p_{\rm FT}.
\tag{11.23}
$$

于是固定靶系的分母也由初态的Lorentz不变量确定，截面便写成

<span id="eq:c11-general-cross-section"></span>

$$
d\sigma=\frac{|\mathcal T|^2}{4\mathcal F}\,d{\rm LIPS}_n(K)
=\frac{|\mathcal T|^2}{4p\sqrt s}\,d{\rm LIPS}_n(K).
\tag{11.24}
$$

在其他参考系，沿用这个由固定靶测量确定的不变截面。与式[（11.20）](#eq:c11-continuum-rate)比较，所需的通量为 $\mathcal F/(E_1E_2V)$。若用各粒子的速度 $\mathbf v_i=\mathbf k_i/E_i$ 表示，其中的速度因子满足

<span id="eq:c11-flux-velocity"></span>

$$
\begin{aligned}
v_{\rm M}^2
&=\frac{\mathcal F^2}{E_1^2E_2^2}
=(1-\mathbf v_1\cdot\mathbf v_2)^2
-(1-v_1^2)(1-v_2^2)\\
&=|\mathbf v_1-\mathbf v_2|^2
-|\mathbf v_1\times\mathbf v_2|^2.
\end{aligned}
\tag{11.25}
$$

第一行代入了 $m_i^2/E_i^2=1-v_i^2$，第二行再使用叉积平方恒等式。在FT系，这个因子退化为入射粒子的速率；在CM系，它为 $p/E_1+p/E_2$，表示两束相向而行的粒子所给的通量。它与某一粒子静止系中测得的相对速率有区别，后者还要再除以 $1-\mathbf v_1\cdot\mathbf v_2$。

将各部分的量纲合在一起，也能看清截面为何是面积。$n$ 条出射测度及总delta的质量维数为 $2n-4$，上一节得到 $2\to n$ 振幅的维数为 $2-n$，而 $[\mathcal F]=2$，所以 $[d\sigma]=2(2-n)+(2n-4)-2=-2$。

<span id="c11-two-body"></span>

## 两体相空间的积分

为了实际求出角分布，现在取 $n=2$。相空间不变性允许选择最方便的总动量 $K=(\sqrt s,\mathbf0)$ 来积分。两条末态测度贡献 $(2\pi)^{-6}$ 与 $1/(4E_1'E_2')$，总delta则贡献 $(2\pi)^4$，因而有

<span id="eq:c11-two-body-before"></span>

$$
d{\rm LIPS}_2
=\frac{\delta(E_1'+E_2'-\sqrt s)\,
\delta^3(\mathbf k_1'+\mathbf k_2')}
{4(2\pi)^2E_1'E_2'}\,d^3k_1'\,d^3k_2'.
\tag{11.26}
$$

先积掉 $d^3k_2'$。空间delta令 $\mathbf k_2'=-\mathbf k_1'$，这一步线性消元的Jacobian为1，只剩一个三动量积分。将其径向变量记为 $r=|\mathbf k_1'|$，而以 $p'$ 表示随后被能量守恒选出的半径，则

<span id="eq:c11-radial-phase-space"></span>

$$
\begin{aligned}
E_1'(r)&=\sqrt{r^2+m_1'^2},\qquad
E_2'(r)=\sqrt{r^2+m_2'^2},\\
f(r)&=E_1'(r)+E_2'(r)-\sqrt s,\\
d{\rm LIPS}_2
&=\frac{r^2\,dr\,d\Omega_{\rm CM}}
{4(2\pi)^2E_1'(r)E_2'(r)}\,\delta(f(r)).
\end{aligned}
\tag{11.27}
$$

这里用了 $d^3k_1'=r^2dr\,d\Omega_{\rm CM}$，其中 $d\Omega_{\rm CM}=\sin\theta\,d\theta\,d\phi$。阈值以上有 $f(0)<0$，而 $f(r)$ 在 $r>0$ 时单调增加，最终成为正值，所以恰有一个正根，正是式[（11.5）](#eq:c11-in-out-radii)给出的 $p'$。

要用能量delta完成径向积分，还须计入它的换元Jacobian。在简单根 $r_*$ 的邻域令 $y=f(r)$，由普通变量代换得到

$$
\int dr\,h(r)\delta(f(r))=\frac{h(r_*)}{|f'(r_*)|}.
$$

有多个简单根时，将各根邻域的贡献相加即可。这里仅有一个正根，其导数为

<span id="eq:c11-energy-jacobian"></span>

$$
f'(p')=\frac{p'}{E_1'}+\frac{p'}{E_2'}
=\frac{p'(E_1'+E_2')}{E_1'E_2'}
=\frac{p'\sqrt s}{E_1'E_2'}>0.
\tag{11.28}
$$

将导数代回径向积分，分母中的 $E_1'E_2'$ 完全消去，径向测度中的一个 $p'$ 也被消去，于是得到

<span id="eq:c11-two-body-evaluated"></span>

$$
d{\rm LIPS}_2=\frac{p'}{16\pi^2\sqrt s}\,d\Omega_{\rm CM},
\qquad
\int d{\rm LIPS}_2=\frac{p'}{4\pi\sqrt s}
=\frac{\sqrt{\lambda(s,m_1'^2,m_2'^2)}}{8\pi s}.
\tag{11.29}
$$

全角积分带来的 $4\pi$ 就是 $\int_0^{2\pi}d\phi\int_0^\pi\sin\theta\,d\theta$。两个出射粒子都无质量且 $s>0$ 时，积分为 $1/(8\pi)$；若存在正的两体阈值，可用相空间则从阈值上方趋于零。正好在阈值处，$p'=0$ 使简单根条件失效，应从已经积完的结果取单侧极限。

将这个相空间因子与入射通量结合，微分截面为

<span id="eq:c11-cm-differential"></span>

$$
\frac{d\sigma}{d\Omega_{\rm CM}}
=\frac1{64\pi^2s}\frac{p'}p\,|\mathcal T|^2.
\tag{11.30}
$$

这个动量比的两端具有不同来源：出射可用态数贡献 $p'$，入射通量则贡献 $1/p$。弹性等质量过程里二者相消；在入射静止阈值处，也须先取 $p>0$ 的截面，再求极限，不能先除以已经为零的通量。

还可以把角分布写成不变量的微分。固定 $s$ 时，式[（11.6）](#eq:c11-t-angle)中的 $p,p',E_1,E_1'$ 都不变。令 $c_\theta=\cos\theta$，便有 $t=t_0+2pp'c_\theta$，其中 $t_0=m_1^2+m_1'^2-2E_1E_1'$。本节的标量分布绕入射轴对称，先作方位角积分得 $2\pi$，再用 $t$ 代替 $c_\theta$，得到

<span id="eq:c11-t-differential"></span>

$$
\begin{aligned}
dt&=2pp'\,dc_\theta,\\
\frac{d\sigma}{dt}
&=\frac{2\pi}{2pp'}\frac{d\sigma}{d\Omega_{\rm CM}}
=\frac{|\mathcal T|^2}{64\pi s p^2}
=\frac{|\mathcal T|^2}{16\pi\lambda(s,m_1^2,m_2^2)}.
\end{aligned}
\tag{11.31}
$$

这里已作完方位角积分。从 $\theta=0\to\pi$ 换成 $c_\theta=1\to-1$ 时，$d c_\theta=-\sin\theta\,d\theta$ 的负号由交换上下限消去。若分布还依赖方位角，便应保留完整的 $\int d\phi\,d\sigma/d\Omega$。

<span id="c11-identical"></span>

## 其它参考系与相同粒子

在其他参考系，同一个不变微分截面仍可用来求角分布，只是角度换元不再如此简单。FT系的出射动量大小也依赖散射角，因此求导时要连同这个依赖一起处理。记总四动量 $K=(\mathcal E,0,0,P)$，其中 $\mathcal E=E_{1,\rm FT}+m_2$、$P=p_{\rm FT}$。第一出射粒子写成 $k_1'=(e,q\mathbf n)$，取 $e=\sqrt{q^2+m_1'^2}$、$c=\mathbf n\cdot\hat{\mathbf z}$；第二粒子的质量壳条件 $(K-k_1')^2=-m_2'^2$ 便给出

<span id="eq:c11-ft-outgoing-derivative"></span>

$$
\mathcal E e-Pqc=\frac{s+m_1'^2-m_2'^2}{2},\qquad
\frac{dq}{dc}=\frac{Pq}{\mathcal E q/e-Pc}.
\tag{11.32}
$$

第二式由第一式作隐函数微分得到，适用于分母非零的分支。随后对式[（11.6）](#eq:c11-t-angle)求导，必须保留 $q(c)$ 的变化，因而

<span id="eq:c11-ft-angular-jacobian"></span>

$$
\begin{aligned}
\frac{dt}{dc}
&=2Pq+2\left(Pc-\frac{E_{1,\rm FT}q}{e}\right)\frac{dq}{dc}
=\frac{2m_2q}{e}\frac{dq}{dc},\\
\frac{d\sigma}{d\Omega_{\rm FT}}
&=\frac1{2\pi}\sum_r
\left.\frac{d\sigma}{dt}\right|_r
\left|\frac{dt}{dc}\right|_r.
\end{aligned}
\tag{11.33}
$$

第一行最后一步使用 $Pq=(\mathcal E q/e-Pc)dq/dc$ 及 $\mathcal E-E_{1,\rm FT}=m_2$。若指定角度对应多个正能且 $q>0$ 的运动学分支，要将各支相加；不同分支的 $t$ 变化方向可能相反，所以Jacobian取绝对值。CM系中 $p'$ 固定的简式，由此换成了实验室角度所需的完整导数。

还有一种重复需要处理：至今末态动量都按有序标签积分，但相同粒子的标签交换并不产生新态。对同一种玻色粒子，简写 $a_j^\dagger=a^\dagger(\mathbf k_j')$，便有 $a_1^\dagger a_2^\dagger|0\rangle=a_2^\dagger a_1^\dagger|0\rangle$。更一般地，这种粒子的 $n$ 粒子子空间满足

<span id="eq:c11-identical-completeness"></span>

$$
1_n=\frac1{n!}\int\prod_{j=1}^n d\widetilde k_j'\,
|k_1',\ldots,k_n'\rangle
\langle k_1',\ldots,k_n'|.
\tag{11.34}
$$

可将右边作用于任意 $n$ 粒子态来理解这个阶乘。CCR给出 $n!$ 种排列的delta乘积，各动量测度消去相应的 $(2\pi)^3 2E$，而每种排列得到的Fock态都相同。因此前面的 $1/n!$ 恰好使结果回到原态。有限盒内若有重合模式，其多重收缩也由相应阶乘计入，所以这个完备关系同样适用。

对每种粒子分别消去标签重复，若第 $a$ 种在末态出现 $n_a$ 次，所需的除数及总截面为

<span id="eq:c11-final-state-factor"></span>

$$
S_{\rm fin}=\prod_a n_a!,\qquad
\sigma=\frac1{S_{\rm fin}}\int d\sigma.
\tag{11.35}
$$

这个因子修正的是末态积分对同一物理态的重复计数，各费曼图内部的对称因子则早已计入振幅。相同粒子的各道振幅也已经先相加，因此其干涉仍包含在 $|\mathcal T|^2$ 中。两个入射模式由实验预先指定，不会因为粒子种类相同而再增加一个初态 $2!$ 除数。

由此，两个出射粒子的总截面可按角度或按不变量积分，写成

<span id="eq:c11-total-integrals"></span>

$$
\begin{aligned}
\sigma
&=\frac1{S_{\rm fin}}\int d\Omega_{\rm CM}\,
  \frac{d\sigma}{d\Omega_{\rm CM}}
=\frac{2\pi}{S_{\rm fin}}\int_{-1}^{1}dc_\theta\,
  \frac{d\sigma}{d\Omega_{\rm CM}}\\
&=\frac1{S_{\rm fin}}\int_{t_{\min}}^{t_{\max}}dt\,\frac{d\sigma}{dt},
\qquad t_{\min,\max}=t_0\mp2pp'.
\end{aligned}
\tag{11.36}
$$

两末态粒子相同时取 $S_{\rm fin}=2$，可以区分时取1。如果用一个不重复的半球来标记相同粒子，也可只在该区域积分而不除2；选择全立体角时则要保留这个因子，两种办法表示同一组物理末态。

<span id="c11-angular-limits"></span>

## 实标量例子的角分布

现在把一般公式用于式[（11.8）](#eq:c11-tree-amplitude)的 $\varphi^3$ 振幅。四条外腿质量相同，CM系各粒子的能量都是 $\sqrt s/2$，且 $p'=p=\sqrt{s-4m^2}/2$。用 $c=\cos\theta$ 表示角度，两个交换道的不变量写成

<span id="eq:c11-equal-mass-angle"></span>

$$
t=-\frac{s-4m^2}{2}(1-c),\qquad
u=-\frac{s-4m^2}{2}(1+c).
\tag{11.37}
$$

以下记 $a=m^2>0$。先从非相对论区域看角分布，此时 $x=(s-4a)/a=4p^2/m^2\ll1$。将树幅的三个分母各自用这个小参数表示，就有

<span id="eq:c11-nr-start"></span>

$$
\frac{a\mathcal T_{\rm tree}}{g^2}
=-\frac1{3+x}
+\frac1{1+x(1-c)/2}
+\frac1{1+x(1+c)/2}.
\tag{11.38}
$$

逐项使用几何级数，常数项合为 $-1/3+1+1=5/3$，一次项合为 $1/9-(1-c)/2-(1+c)/2=-8/9$，二次项为 $-1/27+[(1-c)^2+(1+c)^2]/4=25/54+c^2/2$。提出共同常数 $5/3$，便得到

<span id="eq:c11-nr-amplitude"></span>

$$
\mathcal T_{\rm tree}
=\frac{5g^2}{3a}
\left[1-\frac8{15}x+
\frac5{18}\left(1+\frac{27}{25}c^2\right)x^2+O(x^3)\right].
\tag{11.39}
$$

在 $|c|\le1$ 的整个角域内，两个交换道的展开参数都不超过 $x$，所以这里的低能展开可以一致使用。角度首次出现在 $p^4/m^4$ 阶，说明足够慢的粒子具有近似各向同性的微分截面。

高能情况有所不同。令 $y=a/s\ll1$，并记 $A_\pm=(1\mp c)/2$，同一个树幅变为

<span id="eq:c11-ur-start"></span>

$$
\frac{s\mathcal T_{\rm tree}}{g^2}
=-\frac1{1-y}
+\frac1{A_++y(1-4A_+)}
+\frac1{A_-+y(1-4A_-)}.
\tag{11.40}
$$

先固定角度，并要求 $y\ll\min(1-c,1+c)$，便可对各分母展开。利用 $A_+^{-1}+A_-^{-1}=4/(1-c^2)$、$A_+^{-2}+A_-^{-2}=8(1+c^2)/(1-c^2)^2$，三个常数项合为 $-1+4/(1-c^2)$，一次项合为 $-1+16/(1-c^2)-8(1+c^2)/(1-c^2)^2$，整理得到

<span id="eq:c11-ur-amplitude"></span>

$$
\begin{aligned}
\mathcal T_{\rm tree}
&=\frac{g^2}{s}
\left[\frac{3+c^2}{1-c^2}
+y\frac{7-22c^2-c^4}{(1-c^2)^2}+O(y^2)\right]\\
&=\frac{g^2}{s\sin^2\theta}
\left[3+\cos^2\theta
-\left(\frac{(3+\cos^2\theta)^2}{\sin^2\theta}-16\right)y
+O(y^2)\right].
\end{aligned}
\tag{11.41}
$$

最后一行使用了 $7-22c^2-c^4=16(1-c^2)-(3+c^2)^2$。这个余项估计适用于避开 $c=\pm1$ 的固定角区间。

靠近前向时，角度本身也小，便应保留完整的 $t$ 道分母。由 $1-\cos\theta=\theta^2/2+O(\theta^4)$，有

<span id="eq:c11-forward-peak"></span>

$$
m^2-t=a+\frac{s-4a}{4}\theta^2+O(s\theta^4),\qquad
\mathcal T_{\rm tree}
=\frac{g^2}{a+s\theta^2/4}+O(g^2/s)
\quad\bigl(\theta=O(\sqrt{a/s})\bigr).
\tag{11.42}
$$

角宽因而随 $m/\sqrt s$ 缩小，非零质量 $m$ 则限制了峰顶；后向由 $u$ 道产生同样的尖峰。高能散射于是集中在两个相反方向。求总截面时必须把这两小片角域也包括进去，式[（11.41）](#eq:c11-ur-amplitude)的固定角展开不能直接积到端点。

<span id="c11-total"></span>

## 总截面的完整积分

因此先在物理 $t$ 区间积分完整树幅，再从结果取能量极限。为将总截面化为有理函数积分，令

<span id="eq:c11-total-substitution"></span>

$$
D=s-4a,\qquad b=s-3a=a+D,\qquad
h=s-2a=a+b,\qquad q=-\frac1{s-a},\qquad z=a-t.
\tag{11.43}
$$

当 $t$ 从 $-D$ 增至0时，$z$ 从 $b$ 减至 $a$。用 $dt=-dz$ 交换上下限后，积分区间为 $a\le z\le b$，另一交换道的分母则为 $m^2-u=h-z$，于是

<span id="eq:c11-total-rational-integral"></span>

$$
\begin{aligned}
\mathcal T_{\rm tree}&=g^2\left(q+\frac1z+\frac1{h-z}\right),\\
\sigma_{\rm tree}
&=\frac{g^4}{32\pi sD}\,I,\qquad
I=\int_a^b dz\left(q+\frac1z+\frac1{h-z}\right)^2.
\end{aligned}
\tag{11.44}
$$

这里分母的32来自式[（11.31）](#eq:c11-t-differential)中的 $64\pi sp^2=16\pi sD$，再乘两个相同出射粒子的 $2!$。

为把全部干涉项保留下来，将被积函数的平方分成四组。常数项及两个传播分母的平方项先给出

<span id="eq:c11-total-square-terms"></span>

$$
\begin{aligned}
\int_a^b q^2\,dz&=q^2(b-a)=q^2D,\\
\int_a^b\left[\frac1{z^2}+\frac1{(h-z)^2}\right]dz
&=\left[-\frac1z+\frac1{h-z}\right]_a^b
=2\left(\frac1a-\frac1b\right).
\end{aligned}
\tag{11.45}
$$

上下端点满足 $h-a=b$、$h-b=a$，所以两个平方项的积分相同。接着处理含一个 $q$ 的交叉项；由 $\int dz[1/z+1/(h-z)]=\log z-\log(h-z)$，得到

<span id="eq:c11-total-linear-cross"></span>

$$
\int_a^b2q\left[\frac1z+\frac1{h-z}\right]dz
=4q\log\frac ba.
\tag{11.46}
$$

余下的是两个交换道之间的交叉项。先作部分分式，再用刚才的对数积分：

<span id="eq:c11-total-exchange-cross"></span>

$$
\frac1{z(h-z)}=\frac1h\left(\frac1z+\frac1{h-z}\right),
\qquad
\int_a^b\frac{2\,dz}{z(h-z)}=\frac4h\log\frac ba.
\tag{11.47}
$$

两组交叉项的对数系数合为 $4(q+1/h)=4a/[(s-a)(s-2a)]$。将四组结果全部相加，便得到总截面：

<span id="eq:c11-total-closed"></span>

$$
\begin{aligned}
\sigma_{\rm tree}
=\frac{g^4}{32\pi s(s-4a)}
\Bigg[&
\frac2a+\frac{s-4a}{(s-a)^2}-\frac2{s-3a}\\
&+\frac{4a}{(s-a)(s-2a)}
\log\frac{s-3a}{a}\Bigg],\qquad a=m^2.
\end{aligned}
\tag{11.48}
$$

在 $s>4a$ 时，原积分普通收敛。展开后的各项虽未必分别为正，其和却等于式[（11.44）](#eq:c11-total-rational-integral)中的实函数平方积分，因此总截面非负。阈值附近若直接数值代入，宜将 $2/a-2/b$ 合写为 $2D/(ab)$，并将对数写为 $\log(1+D/a)$，以避免大数相消。

非相对论极限也可以从全角一致的式[（11.39）](#eq:c11-nr-amplitude)直接求出。保留到 $x$ 的一次阶，振幅平方与微分截面中的 $1/s$ 分别为

<span id="eq:c11-nr-cross-input"></span>

$$
|\mathcal T_{\rm tree}|^2
=\frac{25g^4}{9a^2}\left[1-\frac{16}{15}x+O(x^2)\right],
\qquad
\frac1s=\frac1{4a}\left[1-\frac x4+O(x^2)\right].
\tag{11.49}
$$

这一阶没有角依赖，全角积分给出 $4\pi$，相同末态再除以2。因此，微分截面前的因子合为 $4\pi/(2\cdot64\pi^2s)$，总截面为

<span id="eq:c11-nr-total"></span>

$$
\begin{aligned}
\sigma_{\rm tree}
&=\frac{25g^4}{1152\pi a^3}
\left[1-\left(\frac{16}{15}+\frac14\right)x+O(x^2)\right]\\
&=\frac{25g^4}{1152\pi m^6}
\left[1-\frac{79}{60}\frac{s-4m^2}{m^2}
+O\!\left(\frac{(s-4m^2)^2}{m^4}\right)\right].
\end{aligned}
\tag{11.50}
$$

截面在 $p\downarrow0$ 有有限极限，因为相空间和通量各自趋零时，它们的动量因子恰好相消。

高能极限则从已经积完的式[（11.48）](#eq:c11-total-closed)展开，以保留前、后向角域的贡献。平方常数项为 $(s-4a)/(s-a)^2=1/s+O(a/s^2)$，两个平方项为 $2/a-2/s+O(a/s^2)$，对数项为 $O(a\log(s/a)/s^2)$，因此

<span id="eq:c11-ur-total-input"></span>

$$
I=\frac2a-\frac1s+O\!\left(\frac a{s^2}\log\frac sa\right),
\qquad
\frac1{s(s-4a)}=\frac1{s^2}
\left[1+\frac{4a}s+O(a^2/s^2)\right].
\tag{11.51}
$$

两式相乘，首个相对修正为 $(4-1/2)a/s$，于是得到

<span id="eq:c11-ur-total"></span>

$$
\sigma_{\rm tree}
=\frac{g^4}{16\pi m^2s^2}
\left[1+\frac72\frac{m^2}s
+O\!\left(\frac{m^4}{s^2}\log\frac{s}{m^2}\right)\right].
\tag{11.52}
$$

这个主项也可以由前、后向峰的形状理解。在式[（11.42）](#eq:c11-forward-peak)中取 $\sqrt{a/s}\ll\theta_0\ll1$，两个峰的贡献相同，恰好抵消全角末态积分中的 $1/2!$。一个峰的方位角积分给 $2\pi$，径向小角积分则为

<span id="eq:c11-peak-integral"></span>

$$
\int_0^{\theta_0}\frac{\theta\,d\theta}{(a+s\theta^2/4)^2}
=\frac2s\left(\frac1a-\frac1{a+s\theta_0^2/4}\right)
=\frac2{sa}\,[1+o(1)].
\tag{11.53}
$$

再乘 $2\pi g^4/(64\pi^2s)$，就得到 $g^4/(16\pi as^2)$。固定角区域的微分截面只有 $O(g^4/s^3)$，因此主导总截面的是角域逐渐收窄的前、后向峰。

以上角分布保留树级 $O(g^2)$ 振幅，截面则保留其平方的 $O(g^4)$。振幅中省去的 $O(g^4)$ 项与树幅干涉后，给出截面的 $O(g^6)$ 修正；低能参数 $p^2/m^2$ 或高能参数 $m^2/s$ 的展开，是在这个固定耦合阶内另作的近似。

<span id="c11-decay"></span>

## 单粒子的衰变率

弱相互作用下，单粒子态向多粒子态的跃迁率给出领先衰变宽度。以自由哈密顿量的单粒子态为初态，衰变相互作用使它的占据概率逐渐减少；第25节将通过传播子的圈修正描述这个不稳定态。

取自由哈密顿量 $H_0$ 的单粒子态 $|A\rangle$，将引起衰变的相互作用作为微扰。对于单顶点衰变，一阶演化已给出领先振幅。在相互作用绘景中，它为

<span id="eq:c11-decay-golden-rule"></span>

$$
\langle f|U_I|A\rangle^{(1)}
=-i\langle f|H_I(0)|A\rangle
\int_{-\tau/2}^{\tau/2}dt\,e^{i(E_f-E_A)t}.
\tag{11.54}
$$

时间相位由 $H_I(t)=e^{iH_0t}H_I(0)e^{-iH_0t}$ 确定。对上式取模平方，除以 $\tau$，再使用式[（11.14）](#eq:c11-window-weak-limit)，便得到能量守恒因子 $2\pi\delta(E_f-E_A)$ 乘相互作用矩阵元平方，即黄金规则。空间积分、外态归一化和末态求和仍按本节前面的步骤处理。

相对于两个入射粒子的计算，范数只须换成一粒子范数：

<span id="eq:c11-differential-decay"></span>

$$
\langle A|A\rangle=2E_AV,\qquad
d\Gamma_{\rm frame}
=\frac{V|\mathcal T_{A\to f}|^2}{2E_AV}\,
d{\rm LIPS}_n(k_A)
=\frac{|\mathcal T_{A\to f}|^2}{2E_A}\,
d{\rm LIPS}_n(k_A).
\tag{11.55}
$$

末尾的 $V$ 在此直接相消，因为计算的是单个粒子在单位时间内的衰变概率，无须再除以束流通量。取静止系宽度远小于粒子质量，并在微观相关时间之后、初态显著耗尽之前测量，便得到前面所用的恒定跃迁率。

最后对全部末态积分，并按相同粒子的阶乘消去有序标签，得到

<span id="eq:c11-total-decay"></span>

$$
\begin{aligned}
\Gamma_{\rm frame}
&=\frac1{2E_A S_{\rm fin}}\int
|\mathcal T_{A\to f}|^2\,d{\rm LIPS}_n(k_A),\\
\Gamma_0&=\frac1{2m_A S_{\rm fin}}\int
|\mathcal T_{A\to f}|^2\,d{\rm LIPS}_n(k_A).
\end{aligned}
\tag{11.56}
$$

第二式取在初始粒子的静止系，$-k_A^2=m_A^2$。振幅平方和相空间共同构成不变量，改变参考系后只有前面的能量分母变化，因此

<span id="eq:c11-time-dilation"></span>

$$
\Gamma_{\rm frame}=\frac{m_A}{E_A}\Gamma_0.
\tag{11.57}
$$

同一关系还可由固有时 $d\tau_{\rm proper}=(m_A/E_A)dt$ 理解：单位固有时的衰变概率相同，运动粒子在单位坐标时间内经历的固有时较短，衰变率因而降低到静止系率的 $m_A/E_A$ 倍，寿命则增加到 $E_A/m_A$ 倍。

衰变振幅有 $n+1$ 条外腿，质量维数为 $3-n$。结合 $[d{\rm LIPS}_n]=2n-4$ 和 $[E_A]=1$，得到 $[\Gamma]=2(3-n)+(2n-4)-1=1$，在自然单位中正是时间的倒数。两个具体例子可以看出顶点系数与末态计数怎样共同确定衰变率。

<span id="c11-two-decays"></span>

## 两种标量衰变的计算

先取两个实标量场，相互作用为 $\mathcal L_1=gAB^2$，质量满足 $m_A>2m_B$。外部的两个 $B$ 可以与顶点中的两个场以 $2!$ 种方式收缩，因此顶点因子为 $2ig$，树级振幅为 $\mathcal T_{A\to BB}=2g$。两体相空间已经在式[（11.29）](#eq:c11-two-body-evaluated)积出，代入 $s=m_A^2$ 得到

<span id="eq:c11-real-decay"></span>

$$
\begin{aligned}
\beta_B&=\sqrt{1-\frac{4m_B^2}{m_A^2}},&
\int d{\rm LIPS}_2&=\frac{\beta_B}{8\pi},\\
\Gamma_{A\to BB}^{\rm tree}
&=\frac{1}{2m_A}\frac{1}{2!}\,(2g)^2\frac{\beta_B}{8\pi}
=\frac{g^2}{8\pi m_A}\sqrt{1-\frac{4m_B^2}{m_A^2}}.
\end{aligned}
\tag{11.58}
$$

这里 $2!$ 出现在两处：顶点中的收缩数给振幅乘2，相同末态的积分给概率除2。振幅先取模平方，所以这两个因子最后留下一个2。

再取实标量 $\varphi$ 与复标量 $\chi$，相互作用为 $\mathcal L_1=g\varphi\chi^\dagger\chi$，且 $m_\varphi>2m_\chi$。粒子与反粒子各对应一个场，顶点为 $ig$。末态的两种电荷可区分，积分遍历一次物理末态即得到

<span id="eq:c11-complex-decay"></span>

$$
\Gamma_{\varphi\to\chi\bar\chi}^{\rm tree}
=\frac{1}{2m_\varphi}\,g^2\frac{1}{8\pi}
\sqrt{1-\frac{4m_\chi^2}{m_\varphi^2}}
=\frac{g^2}{16\pi m_\varphi}
\sqrt{1-\frac{4m_\chi^2}{m_\varphi^2}}.
\tag{11.59}
$$

两个过程的振幅均与出射方向无关，所以在母粒子静止系中各向同性。接近两体阈值时，出射动量和可用相空间同时缩小，两种宽度都正比于相应的 $\beta$。

---

[← 第 10 节](/posts/srednicki-10/) · [章节地图](/srednicki/) · [第 12 节 →](/posts/srednicki-12/)
