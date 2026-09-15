---
title: 'Srednicki §41 自旋二分之一粒子的 LSZ 约化'
date: 2026-09-14
category: 笔记
tags: [物理, 量子场论, Srednicki]
series: 'Srednicki QFT'
srednickiSections: [41]
hideFromHome: true
draft: false
---

<span id="c41"></span>

要计算自旋二分之一粒子的散射，首先仍须构造遥远过去的入态和遥远未来的出态，再将它们的内积写成场的关联函数。所需的波包散射极限已在[第5节](/posts/srednicki-05/#c05)讨论，旋量和模式归一化则沿用第38、39节。有了这些准备，我们可以逐条约化外部粒子：一阶狄拉克方程使每条外腿带上一阶微分和数值旋量，模式的反对易关系则决定交换粒子次序时的负号。

<span id="c41-packets"></span>

## 从单粒子态到波包

先考虑保持$\Psi\mapsto e^{-i\alpha}\Psi$的狄拉克理论。在动能项系数为一、相互作用不含场导数时，这个对称性给出守恒流$j^\mu=\bar\Psi\gamma^\mu\Psi$及荷$Q=\int d^3x\,j^0$。选定荷单位，使粒子荷取$+1$、反粒子荷取$-1$，两类单粒子态便可用荷标签区分。自由理论中的态由产生算符作用于真空得到，而产生算符本身又可由场的空间投影抽取。将这两层关系写在一起：
<span id="eq:c41-states-projections"></span>

$$
\begin{aligned}
|\mathbf p,s,+\rangle&=b_s^\dagger(\mathbf p)|0\rangle,
\\
|\mathbf p,s,-\rangle&=d_s^\dagger(\mathbf p)|0\rangle,\\
b_s^\dagger(\mathbf p)
&=\int d^3x\,e^{ipx}\bar\Psi(x)\gamma^0u_s(\mathbf p),\\
d_s^\dagger(\mathbf p)
&=\int d^3x\,e^{ipx}\bar v_s(\mathbf p)\gamma^0\Psi(x).
\end{aligned}
\tag{41.1}
$$

其中$b_s^\dagger$的投影由[模式反演](/posts/srednicki-39/#c39-inversion)中的$\Psi^\dagger u$改写而来，只需用$\bar\Psi\gamma^0=\Psi^\dagger$；$d_s^\dagger$的投影同样用$\bar v\gamma^0=v^\dagger$改写。投影中的四动量取正能量质量壳，$p^0=\omega_{\mathbf p}=\sqrt{\mathbf p^2+m^2}$，平面波相位为$px=-\omega_{\mathbf p}t+\mathbf p\cdot\mathbf x$。自由模式的反对易关系随即确定态的内积：
<span id="eq:c41-state-normalization"></span>

$$
\begin{aligned}
\langle\mathbf p',s',q'|\mathbf p,s,q\rangle
&=(2\pi)^3\,2\omega_{\mathbf p}\,
\delta^3(\mathbf p'-\mathbf p)\delta_{s's}\delta_{q'q},\\
\langle0|0\rangle&=1,\qquad q,q'=\pm1.
\end{aligned}
\tag{41.2}
$$

例如，计算正荷态的内积时，把湮灭算符移到右边，$b^\dagger b$项湮灭真空，只留下$\{b,b^\dagger\}$。不同荷的内积则由混合模的反对易子给出，因而为零。这样固定的动量态适合表示振幅，却尚不能描述空间中彼此分离的入射粒子；为此需要将它们叠加成波包。

波包用普通$d^3p$积分，场展开中的不变测度因子已包含在模式归一化中。允许同一个包同时包含两种自旋，定义波包算符及其内积为
<span id="eq:c41-packet-inner"></span>

$$
\begin{aligned}
B^\dagger[f]&=\sum_s\int d^3p\,f_s(\mathbf p)b_s^\dagger(\mathbf p),
\\
B[f]&=B^\dagger[f]^\dagger,\\
C(h,f)&\equiv\{B[h],B^\dagger[f]\}\\
&=(2\pi)^3\sum_s\int d^3p\,2\omega_{\mathbf p}\,
h_s(\mathbf p)^*f_s(\mathbf p).
\end{aligned}
\tag{41.3}
$$

将模式CAR代入两条动量积分，$\delta$函数消去其中一条，就得到$C(h,f)$的积分式。对于固定自旋$s_1$，选择$f_s(\mathbf p)=\delta_{ss_1}N
\exp[-(\mathbf p-\mathbf p_1)^2/(4\sigma^2)]$。
常数$N$由$C(f,f)=1$确定；其窄包展开沿用第5节式[（5.4）](/posts/srednicki-05/#eq:c05-gaussian-norm)，自旋求和在这里仅留下一个固定标签。

这个包的空间传播由自由场矩阵元$\langle0|\Psi(x)B^\dagger[f]|0\rangle
=\sum_s\int d^3p\,f_s(\mathbf p)u_s(\mathbf p)e^{ipx}$描述。将场展开代入后，只有一个$b,b^\dagger$收缩留下来，CAR中的$(2\pi)^3 2\omega$正好消去不变测度的分母。当$\sigma/\omega_1\ll1$时，可将$u_s(\mathbf p)$在包中心展开；首项为常旋量乘第5节的高斯包络，空间宽度约为$\sigma^{-1}$。这个近似舍去了相对$O(\sigma/\omega_1)$级的旋量变化，保留$u_s(\mathbf p)$的原积分则给出精确包形。

相位对动量的导数确定包中心速度$\mathbf v_1=\mathbf p_1/\omega_1$。在薛定谔图景中，同一态的动量振幅随时间乘上$e^{-i\omega_{\mathbf p}t}$，色散关系的二阶导数又使波包逐渐展宽。因此，判断远过去或远未来的粒子是否分离，须同时考虑中心运动和波包扩散。[第5节的分离论证](/posts/srednicki-05/#c05-asymptotic)可逐分量用于这里的旋量积分，因为紧动量支撑上的$u_s$光滑有界。严格构造取互不相交的速度支撑；具有不同中心的两个高斯包则描述相应的近似制备。

由这些包构造多粒子态时，还须计入费米交换。将$B[f_1]$依次移过两个产生算符，两粒子范数为
<span id="eq:c41-packet-norm"></span>

$$
\begin{aligned}
&\langle0|B[f_2]B[f_1]B^\dagger[f_1]B^\dagger[f_2]|0\rangle\\
&\quad=C(f_1,f_1)C(f_2,f_2)
-C(f_1,f_2)C(f_2,f_1)
=\det G,\qquad G_{ij}=C(f_i,f_j).
\end{aligned}
\tag{41.4}
$$

第一项来自$B[f_1]$与第一个产生算符的反对易子；产生第二项时，它先越过这个算符一次，故多一个负号。若两包相同，行列式为零，反映同一单粒子态不能被占据两次。两包各自归一且相互正交时，整个态已归一；一般在$\det G>0$时，应将产生链除以$\sqrt{\det G}$。继续按CAR递推，更多粒子的范数便成为更高阶格拉姆行列式。把$b^\dagger$换为$d^\dagger$可构造反粒子包，两类模式之间仍保持反对易关系，内积另带荷标签的$\delta$。

现在将式[（41.1）](#eq:c41-states-projections)右侧换成相互作用场。投影一般开始依赖时间，因而要在遥远过去和未来分别取极限，用来制备入态和出态。这里继续采用第5节的散射假设：选择稳定、孤立的质量$m$通道，插值场与它有非零重叠，并假定相应的渐近福克映射和逐腿矩阵元极限存在。以$B_{\rm in/out}$表示得到的渐近算符，归一的两粒子态可写成
<span id="eq:c41-asymptotic-states"></span>

$$
\begin{aligned}
|f_1,f_2;{\rm in}\rangle
&=(\det G_F)^{-1/2}
B_{\rm in}^\dagger[f_1]B_{\rm in}^\dagger[f_2]|0\rangle,\\
|h_1,h_2;{\rm out}\rangle
&=(\det G_H)^{-1/2}
B_{\rm out}^\dagger[h_1]B_{\rm out}^\dagger[h_2]|0\rangle.
\end{aligned}
\tag{41.5}
$$

渐近投影沿用[第5节的谱滤波与时间平均](/posts/srednicki-05/#c05-continuum)。下面先计算产生链的内积，再除以式[（41.5）](#eq:c41-asymptotic-states)中的两个范数因子。

<span id="c41-boundary"></span>

## 四种有限时间边界式

把渐近模式换成场插入的关键，是求同一投影在两个时间端点之差。约化时先采用[本节后面](#c41-overlap)的单位单粒子重叠，场如何归一化留待那里说明。先在有限的$t_-<t_+$上求投影差。简写$\int_f=\sum_s\int d^3p\,f_s(\mathbf p)$，其中$u_s,v_s,p$仍随积分变量变化。用微积分基本定理，再代入式[（41.1）](#eq:c41-states-projections)，得到
<span id="eq:c41-boundary-start"></span>

$$
\begin{aligned}
B^\dagger[f;t_-]-B^\dagger[f;t_+]
&=-\int_{t_-}^{t_+}dt\,\partial_t B^\dagger[f;t]\\
&=-\int_f\int_{t_-}^{t_+}d^4x\,e^{ipx}
\left[(\partial_0\bar\Psi)\gamma^0
-i\omega_{\mathbf p}\bar\Psi\gamma^0\right]u_s.
\end{aligned}
\tag{41.6}
$$

其中$-i\omega_{\mathbf p}$来自平面波的时间导数；此时对$\Psi$只作了求导，没有代入它的运动方程。要将时间项与空间项合并，可以先利用外部数值旋量的在壳方程：
<span id="eq:c41-on-shell-u"></span>

$$
(-\omega_{\mathbf p}\gamma^0+p_i\gamma^i+m)u_s=0,
\qquad
\omega_{\mathbf p}\gamma^0u_s=(p_i\gamma^i+m)u_s.
\tag{41.7}
$$

将它代入式[（41.6）](#eq:c41-boundary-start)，方括号作用于$u_s$后成为$(\partial_0\bar\Psi)\gamma^0
-i\bar\Psi p_i\gamma^i-im\bar\Psi$。这一步把能量换成了空间动量和质量；接下来再将空间动量写成作用于平面波的导数，并把导数移到场上：
<span id="eq:c41-space-ibp"></span>

$$
\begin{aligned}
\int d^3x\,e^{ipx}(-ip_i)\bar\Psi\gamma^i
&=-\int d^3x\,(\partial_i e^{ipx})\bar\Psi\gamma^i\\
&=\int d^3x\,e^{ipx}(\partial_i\bar\Psi)\gamma^i .
\end{aligned}
\tag{41.8}
$$

分部积分的表面项由波包条件控制：先保留Schwartz包，或采用动量空间紧支撑的光滑包，空间无穷远的项便在所取涂抹矩阵元中消失。时间端点则保留在等式左侧，正是我们要计算的投影差。现在时间与空间$\gamma$项已能合为一个狄拉克微分，因而
<span id="eq:c41-bdagger-boundary"></span>

$$
\begin{aligned}
B^\dagger[f;t_-]-B^\dagger[f;t_+]
&=i\int_f\int_{t_-}^{t_+}d^4x\,
\bar\Psi(x)\overleftarrow{\mathscr D}_x u_s\,e^{ipx},\\
\bar\Psi\overleftarrow{\mathscr D}
&\equiv i(\partial_\mu\bar\Psi)\gamma^\mu+m\bar\Psi,
\\
\mathscr D\Psi&\equiv(-i\gamma^\mu\partial_\mu+m)\Psi.
\end{aligned}
\tag{41.9}
$$

整体因子由$i(i\partial+m)=-\partial+im$确定，与式[（41.6）](#eq:c41-boundary-start)中的端点顺序相配。对自由场，伴随方程$\bar\Psi\overleftarrow{\mathscr D}=0$使右侧为零，故产生算符与时间无关。相互作用场一般不满足这个自由方程；它偏离自由演化的部分，正通过右侧积分进入端点差。

粒子出腿可由同一等式取厄米共轭得到。先用$\gamma^{\mu\dagger}\gamma^0=\gamma^0\gamma^\mu$将共轭后的矩阵整理成狄拉克伴随形式：
<span id="eq:c41-dagger-kernel"></span>

$$
\left[\bar\Psi\overleftarrow{\mathscr D}u_s\right]^\dagger
=\bar u_s\mathscr D\Psi.
\tag{41.10}
$$

例如导数项给出$-i u_s^\dagger\gamma^{\mu\dagger}\gamma^0\partial_\mu\Psi
=-i\bar u_s\gamma^\mu\partial_\mu\Psi$。整体虚数也在共轭时变号；再反转端点差，两个负号抵消，于是得到一般复波包的出腿表达式：
<span id="eq:c41-b-boundary"></span>

$$
B[f;t_+]-B[f;t_-]
=i\sum_s\int d^3p\,f_s^*
\int_{t_-}^{t_+}d^4x\,e^{-ipx}\bar u_s\mathscr D_x\Psi(x).
\tag{41.11}
$$

取伴随也把波包权函数变成$f_s^*$。对于实高斯，复共轭不改变权函数；一般出腿则须保留这里的复共轭，才能与态的内积相配。

对反粒子，从$d^\dagger$的投影开始。记波包算符为$D^\dagger[f]=\sum_s\int d^3p\,f_s d_s^\dagger$，这次所用的伴随旋量方程是$\bar v_s(-\slashed p+m)=0$，亦即$\omega_{\mathbf p}\bar v_s\gamma^0
=\bar v_s(p_i\gamma^i-m)$。质量项的号随之改变，同样的时间微分和空间分部积分给出
<span id="eq:c41-ddagger-boundary"></span>

$$
\begin{aligned}
D^\dagger[f;t_-]-D^\dagger[f;t_+]
&=-\int_f\int_{t_-}^{t_+}d^4x\,e^{ipx}
\bar v_s\bigl(\gamma^0\partial_0-ip_i\gamma^i+im\bigr)\Psi\\
&=-\int_f\int_{t_-}^{t_+}d^4x\,e^{ipx}
\bar v_s(\slashed\partial+im)\Psi\\
&=-i\int_f\int_{t_-}^{t_+}d^4x\,e^{ipx}
\bar v_s\mathscr D_x\Psi .
\end{aligned}
\tag{41.12}
$$

第一行的$-ip_i$先写成作用于指数的导数，再按式[（41.8）](#eq:c41-space-ibp)移过一次，第二行就出现了场的空间导数。这里$v$方程的质量号与粒子情形相反，最后提出的系数因而为$-i$。对这个结果取伴随并交换端点，便得到反粒子出腿：
<span id="eq:c41-d-boundary"></span>

$$
D[f;t_+]-D[f;t_-]
=-i\sum_s\int d^3p\,f_s^*
\int_{t_-}^{t_+}d^4x\,
\bar\Psi(x)\overleftarrow{\mathscr D}_x v_s\,e^{-ipx}.
\tag{41.13}
$$

四个边界式都把无量纲波包算符的差写成时空积分。例如入射$b^\dagger$这一项的量纲为$[d^3p]+[f]+[d^4x]+[\bar\Psi]+[\mathscr D]+[u]
=3-2-4+3/2+1+1/2=0$。可见，一阶狄拉克微分须与维数$1/2$的外部旋量一起出现，才能和模式投影的归一化一致。

<span id="c41-ordering"></span>

## 时间序与未散射的配对项

接着把边界式用于散射内积。按式[（41.5）](#eq:c41-asymptotic-states)选定的产生链，两入两出的矩阵元为
<span id="eq:c41-s-order"></span>

$$
S(H;F)=
\langle0|B_{\rm out}[h_2]B_{\rm out}[h_1]
B_{\rm in}^\dagger[f_1]B_{\rm in}^\dagger[f_2]|0\rangle.
\tag{41.14}
$$

出态取厄米共轭后，两个湮灭算符的次序反转。因此，交换$h_1,h_2$或$f_1,f_2$中的任意一对，整个内积都改变符号。将它改写成场的关联函数时，时间排序必须保存这种反对称性。对两个奇场，定义
<span id="eq:c41-fermionic-time-order"></span>

$$
\begin{aligned}
T\{\Psi_\alpha(x)\bar\Psi_\beta(y)\}
&=\theta(x^0-y^0)\Psi_\alpha(x)\bar\Psi_\beta(y)\\
&\quad-\theta(y^0-x^0)\bar\Psi_\beta(y)\Psi_\alpha(x).
\end{aligned}
\tag{41.15}
$$

对更多奇因子也按同一规则排序：每交换一对就乘$-1$。原来的入端点在右、出端点在左，已经依时间先后排列，故可插入$T$。随后边界式会把某条腿移到另一端点，这时新端点的位置与经过的奇因子数必须一起计入。

设$\mathcal B$包含已经插入的$r$个奇场，暂将它们的时间全部固定在$t_-$与$t_+$之间。为了约化下一条入腿，先定义包含一个待积分场的行旋量矩阵元：
<span id="eq:c41-ordered-flux"></span>

$$
\begin{aligned}
H_\alpha(x)&=
\langle\beta,{\rm out}|T\{\mathcal B\bar\Psi_\alpha(x)\}
|\alpha_{\rm in}\rangle,\\
Q_f(t)&=\sum_s\int d^3p\,f_s
\int d^3x\,H(x)\gamma^0u_s e^{ipx}.
\end{aligned}
\tag{41.16}
$$

这里$|\alpha_{\rm in}\rangle$是其余尚未约化的入态。早端点的$\bar\Psi$位于$\mathcal B$右边，无需交换；到了晚端点，它须移过$r$个奇场。因此，在相应端点极限中，$Q_f(t_-)$给出$\langle\beta|\mathcal B B_{\rm in}^\dagger[f]|\alpha_{\rm in}\rangle$，$Q_f(t_+)$则给出$(-1)^r\langle\beta|B_{\rm out}^\dagger[f]\mathcal B|\alpha_{\rm in}\rangle$。将式[（41.6）](#eq:c41-boundary-start)–[（41.9）](#eq:c41-bdagger-boundary)的运算用于整个$H(x)$，两者之差为
<span id="eq:c41-ordered-boundary"></span>

$$
\begin{aligned}
&\langle\beta|\mathcal B B_{\rm in}^\dagger[f]|\alpha_{\rm in}\rangle
-(-1)^r
\langle\beta|B_{\rm out}^\dagger[f]\mathcal B|\alpha_{\rm in}\rangle\\
&\qquad=i\sum_s\int d^3p\,f_s
\int d^4x\,H(x)\overleftarrow{\mathscr D}_x u_s e^{ipx}.
\end{aligned}
\tag{41.17}
$$

这个关系先在有限端点建立，再对矩阵元取散射极限。由于被微分的是整个时间序分布，当$x^0$经过某个插入时间时，式[（41.15）](#eq:c41-fermionic-time-order)中的阶跃函数也会给出导数项，稍后将在自由两点函数中看到它的作用。

现在取$\beta=(h_1,\ldots,h_M)$，考察晚端点一项。这里的产生算符与出射湮灭算符同属out代数，因而可以逐次使用CAR，把它移向左边的真空：
<span id="eq:c41-spectator-car"></span>

$$
\begin{aligned}
&\langle h_1,\ldots,h_M;{\rm out}|B_{\rm out}^\dagger[f]\\
&\quad=\sum_{j=1}^M(-1)^{j-1}C(h_j,f)
\langle h_1,\ldots,\widehat h_j,\ldots,h_M;{\rm out}|.
\end{aligned}
\tag{41.18}
$$

帽号表示删去相应的包。产生算符从右向左首先遇到$B[h_1]$；与第$j$个配对以前，要先越过$j-1$个湮灭算符，这就确定了求和中的符号。完全移到真空左矢旁的一项为零，沿途出现的内积项却须保留。将这个展开代回式[（41.17）](#eq:c41-ordered-boundary)，入射单腿约化便分成两部分：
<span id="eq:c41-in-reduction"></span>

$$
\begin{aligned}
&\langle\beta|\mathcal B B_{\rm in}^\dagger[f]|\alpha_{\rm in}\rangle\\
&=\sum_{j=1}^M(-1)^{r+j-1}C(h_j,f)
\langle\beta\setminus h_j|\mathcal B|\alpha_{\rm in}\rangle\\
&\quad+i\sum_s\int d^3p\,f_s\int d^4x\,
\langle\beta|T\{\mathcal B\bar\Psi(x)\}|\alpha_{\rm in}\rangle
\overleftarrow{\mathscr D}_x u_s e^{ipx}.
\end{aligned}
\tag{41.19}
$$

一部分让这条入腿与某条出腿直接配对，表示该粒子未发生散射，其余粒子仍可参与散射；另一部分将它换成场插入，继续留在关联函数中。这两种选择的递推，也将决定完整散射矩阵的结构。

对出腿改用$T\{\Psi(x)\mathcal B\}$，晚端点已在正确位置，早端点则须交换$r$次。将式[（41.11）](#eq:c41-b-boundary)用于这个矩阵元，得到
<span id="eq:c41-out-reduction"></span>

$$
\begin{aligned}
&\langle\beta|B_{\rm out}[h]\mathcal B|\alpha_{\rm in}\rangle
-(-1)^r\langle\beta|\mathcal B B_{\rm in}[h]|\alpha_{\rm in}\rangle\\
&\quad=i\sum_s\int d^3p\,h_s^*\int d^4x\,e^{-ipx}\bar u_s\mathscr D_x
\langle\beta|T\{\Psi(x)\mathcal B\}|\alpha_{\rm in}\rangle.
\end{aligned}
\tag{41.20}
$$

若先处理完全部入腿，右边的剩余入态就是真空，第二项中的$B_{\rm in}$将其湮灭；此后逐条约化出腿，只需保留积分项。每处理一条外腿，先把已有场的坐标固定在有限区间，再完成这一腿的端点极限，各层积分依此嵌套。这正是[第5节](/posts/srednicki-05/#c05-lsz)所用次序在费米场中的实现。

<span id="c41-contact"></span>

### 时间序导数的一个检验

时间序的阶跃函数为何不能略去，可以从自由场两点函数$G_0(x,y)=\langle0|T\Psi(x)\bar\Psi(y)|0\rangle$直接看出。对式[（41.15）](#eq:c41-fermionic-time-order)求$\partial_{x^0}$，两个阶跃函数的导数合成等时反对易子；其余部分由自由狄拉克方程消去。因此
<span id="eq:c41-free-contact"></span>

$$
\begin{aligned}
\mathscr D_xG_0(x,y)
&=-i\gamma^0\delta(x^0-y^0)
\langle0|\{\Psi(x),\bar\Psi(y)\}|0\rangle\\
&=-i\gamma^0\gamma^0\delta^4(x-y)
=-iI_4\delta^4(x-y),\\
G_0(x,y)\overleftarrow{\mathscr D}_y
&=-iI_4\delta^4(x-y).
\end{aligned}
\tag{41.21}
$$

最后一行改为对$y^0$求导，阶跃函数给出的号与前面相反，但左作用狄拉克导数的系数为$+i$，两者合起来仍给$-i$。将粒子外腿的$+i$乘上这个接触项，便留下单位单粒子重叠。继续约化另一端时，余下的数值旋量和平面波满足自由狄拉克方程，完整的两腿转移积分为零；自由一粒子内积则由式[（41.18）](#eq:c41-spectator-car)中的$C(h,f)$提供。由此可见，若把狄拉克微分直接移入$T$，只对场使用运动方程，就会在第一步丢掉这个非零接触项。

<span id="c41-spectators"></span>

### 配对的符号怎样汇成行列式

现在把逐腿递推合在一起。用$\mathcal R(H;F)$表示所有外腿都换成场插入后的积分，并约定$\mathcal R(\varnothing;\varnothing)=1$；这一积分中仍可包含几个互不连通的散射过程。从$f_1$开始依次使用式[（41.19）](#eq:c41-in-reduction)，每条入腿或与出腿直接配对，或成为场插入，再用式[（41.20）](#eq:c41-out-reduction)处理剩余出腿。按哪些标签被配对来归组，就得到
<span id="eq:c41-full-s-minors"></span>

$$
\begin{aligned}
S(H;F)&=
\sum_{\substack{I\subset\{1,\ldots,N\}\\
J\subset\{1,\ldots,M\}\\ |I|=|J|}}
(-1)^{\sum I+\sum J}
\det C_{J,I}\,
\mathcal R(H_{\bar J};F_{\bar I}),\\
C_{ji}&=C(h_j,f_i).
\end{aligned}
\tag{41.22}
$$

其中未被删去的标签始终保持原顺序，空行列式取一。行列式来自同一组入、出腿的所有配法，而它前面的符号还记录了这些腿在原产生链中的位置。要看清两者怎样分开，设被配对的入腿为$i_1<\cdots<i_k$，它们依次配到出腿$j_1,\ldots,j_k$。处理第$a$次配对时，此前未被配对的入腿已留下$i_a-a$个场插入；若先前删去的出腿中有$\ell_a$个编号小于$j_a$，当前这条出腿就在剩余列表的第$j_a-\ell_a$个位置。于是式[（41.19）](#eq:c41-in-reduction)累计的负号次数为
<span id="eq:c41-minor-sign"></span>

$$
\begin{aligned}
E&=\sum_{a=1}^k(i_a-a+j_a-\ell_a-1),\\
\sum_a\ell_a&=\frac{k(k-1)}2-\operatorname{inv}(j_1,\ldots,j_k),\\
E&=\sum I+\sum J-k(k+1)
+\operatorname{inv}(j_1,\ldots,j_k).
\end{aligned}
\tag{41.23}
$$

这里$\operatorname{inv}$数出出腿列表中的逆序对，而$k(k+1)$恒为偶数。固定两组标签后，对它们的全部配法求和，逆序号就组成$\det C_{J,I}$。每个部分匹配在按序约化入腿时恰好出现一次，所以不再有额外阶乘。

在所选稳定单粒子通道中，一入一出的散射矩阵等于态内积，故$\mathcal R(h;f)=0$。两入两出时，所有只余一条入腿和一条出腿的项随之消失，留下
<span id="eq:c41-two-two"></span>

$$
S(h_1,h_2;f_1,f_2)
=C_{11}C_{22}-C_{12}C_{21}
+\mathcal R(h_1,h_2;f_1,f_2).
\tag{41.24}
$$

自由理论的入、出算符相同，最后一项为零，前两项则恢复式[（41.4）](#eq:c41-packet-norm)的反对称内积。全部外腿都转移为场插入的积分是$\mathcal R$；完整散射矩阵还包含前面两项未散射配对。当入、出包之间所有直接内积均为零时，这个积分也等于该组波包的完整$S$。若只求两入两出的连通散射部分，则在积分中使用连通四点函数即可。

<span id="c41-lsz"></span>

## 四腿公式与一般外腿规则

有了波包的等式，就可以提取确定动量的振幅。窄包形式上对应$\sigma\to0$。应先对任意合适的波包建立等式，再读出乘在$\prod h^*\prod f$旁的动量分布。若始终保持高斯包的单位范数，它不会在希尔伯特空间中收敛为动量$\delta$态，分布态仍须采用式[（41.2）](#eq:c41-state-normalization)的归一化。这与[第5节的平面波极限](/posts/srednicki-05/#c05-plane-wave)完全相同。

为写出四腿积分，先固定关联函数中的场次序，并简记积分测度与相位：
<span id="eq:c41-four-point-order"></span>

$$
\begin{aligned}
G_{\alpha_{2'}\alpha_{1'}\alpha_1\alpha_2}
&=\langle0|T\{
\Psi_{\alpha_{2'}}(x_{2'})
\Psi_{\alpha_{1'}}(x_{1'})
\bar\Psi_{\alpha_1}(x_1)
\bar\Psi_{\alpha_2}(x_2)\}|0\rangle,\\
dX&=d^4x_{1'}\,d^4x_{2'}\,d^4x_1\,d^4x_2,\\
\Phi&=-p_{1'}x_{1'}-p_{2'}x_{2'}+p_1x_1+p_2x_2.
\end{aligned}
\tag{41.25}
$$

这个场次序来自刚才的逐腿约化：两条入腿先给出$\bar\Psi_1,\bar\Psi_2$，再按$1',2'$处理出腿，每次将新场放到时间序积左侧，最后便为$\Psi_{2'}\Psi_{1'}\bar\Psi_1\bar\Psi_2$。将四条边界式的系数和微分一起写出，所有外腿的转移核就是
<span id="eq:c41-four-leg"></span>

$$
\begin{aligned}
\mathcal R(1',2';1,2)
={}&i^4\int dX\,e^{i\Phi}\,
[\bar u_{1'}\mathscr D_{x_{1'}}]_{\alpha_{1'}}
[\bar u_{2'}\mathscr D_{x_{2'}}]_{\alpha_{2'}}\\
&\qquad\times
G_{\alpha_{2'}\alpha_{1'}\alpha_1\alpha_2}
[\overleftarrow{\mathscr D}_{x_1}u_1]_{\alpha_1}
[\overleftarrow{\mathscr D}_{x_2}u_2]_{\alpha_2}.
\end{aligned}
\tag{41.26}
$$

其中$u_i=u_{s_i}(\mathbf p_i)$。各狄拉克微分作用于$G$的相应坐标，外面已经写出的指数不参与这一步求导。矩阵指标的顺序由原来相乘的场决定：数值行、列旋量彼此可交换，奇场则保持式[（41.25）](#eq:c41-four-point-order)中的顺序。四个$i$分别来自四条边界差；也无需另补$(2\pi)^3 2\omega$分母，因为波包采用普通$d^3p$，模式投影的归一化已在第39节处理。要恢复完整平面波$S$，还须加上式[（41.24）](#eq:c41-two-two)的两项直接配对，并将其中的$C_{ji}$换成式[（41.2）](#eq:c41-state-normalization)的分布内积。

任意粒子数或含反粒子的过程可按同样步骤处理。保留原有外部算符的位置，依次采用四种替换：
<span id="eq:c41-four-rules"></span>

$$
\begin{aligned}
b^\dagger_{s,{\rm in}}(\mathbf p)
&\ \longmapsto\
+i\int d^4x\,\bar\Psi(x)
\overleftarrow{\mathscr D}_x u_s(\mathbf p)e^{ipx},\\
b_{s,{\rm out}}(\mathbf p)
&\ \longmapsto\
+i\int d^4x\,e^{-ipx}\bar u_s(\mathbf p)\mathscr D_x\Psi(x),\\
d^\dagger_{s,{\rm in}}(\mathbf p)
&\ \longmapsto\
-i\int d^4x\,e^{ipx}\bar v_s(\mathbf p)\mathscr D_x\Psi(x),\\
d_{s,{\rm out}}(\mathbf p)
&\ \longmapsto\
-i\int d^4x\,\bar\Psi(x)
\overleftarrow{\mathscr D}_x v_s(\mathbf p)e^{-ipx}.
\end{aligned}
\tag{41.27}
$$

这些箭头表示散射矩阵元中的约化积分，端点直接内积仍按式[（41.22）](#eq:c41-full-s-minors)保留，其中不同荷的配对为零。待外腿全部换入以后，对真空期望中的场作费米$T$排序，并让各微分作用于整个时间序分布，就得到所需的关联函数。这里入、出下标分别对应遥远过去和遥远未来的渐近算符。

<span id="c41-majorana"></span>

## 马约拉纳粒子为何有两种相同的写法

马约拉纳粒子没有独立的反粒子模式，场满足$d_s=b_s$及$\bar\Psi=\Psi^T\mathcal C$。因此，上述四条外腿规则中，两条入腿应给出同一结果，两条出腿也应相同。第38节固定的数值旋量相位给出$u_s^T\mathcal C=\bar v_s$、$v_s^T\mathcal C=\bar u_s$，可以据此直接联系两种写法。取任意可交换数值列$w$，把唯一的奇场转置，逐项得到
<span id="eq:c41-majorana-transpose"></span>

$$
\begin{aligned}
\bar\Psi\overleftarrow{\mathscr D}w
&=i(\partial_\mu\Psi^T)\mathcal C\gamma^\mu w
+m\Psi^T\mathcal Cw\\
&=i w^T(\gamma^\mu)^T\mathcal C^T\partial_\mu\Psi
+m w^T\mathcal C^T\Psi\\
&=w^T\mathcal C(i\slashed\partial-m)\Psi
=-w^T\mathcal C\mathscr D\Psi.
\end{aligned}
\tag{41.28}
$$

第二行只交换了数值旋量与一个奇场，未交换两个奇场；负号来自$\mathcal C^T=-\mathcal C$。导数项再用$(\gamma^\mu)^T\mathcal C^T=\mathcal C\gamma^\mu$，便合成最后一行的狄拉克算符。分别代入$w=u_s,v_s$，得到
<span id="eq:c41-majorana-leg-equality"></span>

$$
+i\bar\Psi\overleftarrow{\mathscr D}u_s
=-i\bar v_s\mathscr D\Psi,\qquad
-i\bar\Psi\overleftarrow{\mathscr D}v_s
=+i\bar u_s\mathscr D\Psi .
\tag{41.29}
$$

这就把式[（41.27）](#eq:c41-four-rules)的两条入腿、两条出腿分别联系起来。计算中可以选择场排列较方便的一种，但须保持这个奇插入在原乘积中的位置。马约拉纳作用量的$1/2$已在正则约束与模式归一化中处理，外部单粒子态仍采用式[（41.2）](#eq:c41-state-normalization)，所以外腿无需再乘半因子。

<span id="c41-overlap"></span>

## 相互作用场应怎样归一化

以上边界运算使用了外部数值旋量的自由方程，而相互作用场保留在关联函数中。要让场的投影在渐近极限中产生指定的粒子，还需把它与单粒子态的重叠固定下来。这些重叠中，有些由对称性要求为零，另一些则决定场的归一化。

先看真空期望。令$w=\langle0|\Psi(0)|0\rangle$，洛伦兹不变真空被$M^{\mu\nu}$湮灭，故原点的场变换关系要求
<span id="eq:c41-vacuum-zero"></span>

$$
S^{\mu\nu}w=\langle0|[\Psi(0),M^{\mu\nu}]|0\rangle=0,
\qquad
S^{12}=\frac12
\begin{pmatrix}\sigma_3&0\\0&\sigma_3\end{pmatrix}.
\tag{41.30}
$$

由于$S^{12}$可逆，立即有$w=0$；再用真空的平移不变性，便得$\langle0|\Psi(x)|0\rangle=0$。这个论证只用到了旋量的洛伦兹变换，对没有狄拉克荷标签的马约拉纳场也适用。

对于带荷单粒子态，还可用荷守恒判断哪些重叠必为零。取$Q|0\rangle=0$、$Q|p,s,q\rangle=q|p,s,q\rangle$，将$[\Psi,Q]=\Psi$及$[\bar\Psi,Q]=-\bar\Psi$放入相应矩阵元，得到
<span id="eq:c41-charge-selection"></span>

$$
\begin{aligned}
-q\,\langle p,s,q|\Psi(x)|0\rangle
&=\langle p,s,q|[\Psi(x),Q]|0\rangle
=\langle p,s,q|\Psi(x)|0\rangle,\\
-q\,\langle p,s,q|\bar\Psi(x)|0\rangle
&=\langle p,s,q|[\bar\Psi(x),Q]|0\rangle
=-\langle p,s,q|\bar\Psi(x)|0\rangle.
\end{aligned}
\tag{41.31}
$$

当$q=+1$时，第一种重叠只能为零；当$q=-1$时，第二种重叠只能为零。剩下两个允许非零的重叠，取为单位旋量归一化。连同这两个由荷守恒给出的零式，可写成
<span id="eq:c41-unit-overlaps"></span>

$$
\begin{aligned}
\langle\mathbf p,s,+|\Psi(x)|0\rangle&=0,\\
\langle\mathbf p,s,-|\Psi(x)|0\rangle&=v_s(\mathbf p)e^{-ipx},\\
\langle\mathbf p,s,+|\bar\Psi(x)|0\rangle&=\bar u_s(\mathbf p)e^{-ipx},\\
\langle\mathbf p,s,-|\bar\Psi(x)|0\rangle&=0.
\end{aligned}
\tag{41.32}
$$

这里的指数由平移协变性确定：在$\Psi(x)=e^{-iP\cdot x}\Psi(0)e^{iP\cdot x}$中，左矢是动量$p$的本征态，真空动量为零。对第三行取厄米共轭再乘$\gamma^0$，也可写成$\langle0|\Psi(x)|p,s,+\rangle=u_s e^{ipx}$，便于同自由场展开比较。

这一归一化的作用可直接从投影看出。把单位重叠代入波包产生算符的定义，得到
<span id="eq:c41-projected-overlap"></span>

$$
\begin{aligned}
\langle\mathbf q,r,+|B^\dagger[f;t]|0\rangle
&=\sum_s\int d^3p\,f_s
\int d^3x\,e^{i(p-q)x}\bar u_r(\mathbf q)\gamma^0u_s(\mathbf p)\\
&=(2\pi)^3\,2\omega_{\mathbf q}f_r(\mathbf q).
\end{aligned}
\tag{41.33}
$$

空间积分先给$(2\pi)^3\delta^3(\mathbf p-\mathbf q)$，再用$u_r^\dagger u_s=2\omega_{\mathbf q}\delta_{rs}$；在$\mathbf p=\mathbf q$处，时间相位也变成一。对$d^\dagger$用$v_r^\dagger v_s$可得同一归一化。因此，这两个非零重叠使投影的单粒子分量具有既定的包归一化，也固定了约化外腿应带的数值系数。

接下来要说明在什么条件下可以把重叠写成这种形式。记$U_s(p)=\langle0|\Psi(0)|p,s,+\rangle$、$V_s(p)=\langle p,s,-|\Psi(0)|0\rangle$。[第39节的维格纳转动](/posts/srednicki-39/#c39-wigner)给出

$$
\begin{aligned}
D(\Lambda)U_s(p)&=\sum_rU_r(\Lambda p)w_{rs}(\Lambda,p),\\
D(\Lambda)V_s(p)&=\sum_rV_r(\Lambda p)w_{rs}(\Lambda,p)^*.
\end{aligned}
$$

第二行取左矢，转动矩阵随之复共轭。在静止系，$D(R)=\operatorname{diag}(w,w)$。把两个自旋标签排成矩阵的两列，则$U$的上下两块分别满足$wA=Aw$。与$\sigma_3$对易要求$A$为对角阵，再与$\sigma_1$对易要求两个对角元相等，每块因而独立地正比于$I_2$。$V$的每块则满足$wA=Aw^*$；由$wE=Ew^*$，$AE^{-1}$与$w$对易，故该块正比于$E$。沿用第38节的$e_s,\eta_s=Ee_s$，可写成

$$
U_s(0)=\sqrt m\begin{pmatrix}ae_s\\be_s\end{pmatrix},\qquad
V_s(0)=\sqrt m\begin{pmatrix}c\eta_s\\-d\eta_s\end{pmatrix}.
$$

标准推动$L(p)$从静止动量出发时，其维格纳转动为单位矩阵。将上式乘$D(p)$，并用左右投影与$D(p)$对易，便得到正规正时洛伦兹协变性允许的通式：
<span id="eq:c41-general-overlap"></span>

$$
U_s(p)=(aP_L+bP_R)u_s(p),\qquad
V_s(p)=(cP_L+dP_R)v_s(p).
\tag{41.34}
$$

左右外尔块各有一个常数，洛伦兹协变性本身并不要求$a=b$。例如，把归一的自由场改为$\Phi=e^{i\theta\gamma_5}\Psi$，两个手征块的重叠分别乘上$e^{-i\theta}$和$e^{i\theta}$，一个整体常数就无法同时将它们变成一。要用一个整体尺度归一化，还须有进一步的条件把左右两块联系起来。

本节末尾由标量双线性量构成的实耦合四费米例，可以采用更具体的对称设置：$P,C$按第40节的方式实现，对称性和真空都不破缺，所选稳定粒子的宇称相位与插值场相容。由$P|p,s,\pm\rangle=i|-\mathbf p,s,\pm\rangle$及$P^{-1}\Psi P=i\beta\Psi$，两种矩阵元分别满足

$$
U_s(-\mathbf p)=\beta U_s(\mathbf p),\qquad
V_s(-\mathbf p)=-\beta V_s(\mathbf p).
$$

第二式的额外负号来自左矢中$i$的复共轭。在静止系，$\beta$交换上下块，第一式要求$a=b$，第二式要求$c=d$。再取$C|p,s,+\rangle=|p,s,-\rangle$，由第40节的场变换得到

$$
\begin{aligned}
V_s(p)&=\langle p,s,+|C^{-1}\Psi(0)C|0\rangle
=\mathcal C\bar U_s(p)^T,\\
\bar U_s(p)&=\bar u_s(p)(a^*P_R+b^*P_L),\\
V_s(p)&=(b^*P_L+a^*P_R)v_s(p).
\end{aligned}
$$

取狄拉克伴随时$\beta$交换左右投影，故电荷共轭联系的是$c=b^*$、$d=a^*$。合并宇称条件，得到
<span id="eq:c41-scalar-overlap-condition"></span>

$$
a=b,\qquad c=d=a^*.
\tag{41.35}
$$

把两荷态共同乘$e^{-i\arg a}$，$U_s$的系数变成$|a|$，$V_s$的系数也变成$|a|$，两态的$C$关系保持。记$R=|a|^2>0$，再令$\Psi_{\rm new}=\Psi_{\rm old}/\sqrt R$，便得到式[（41.32）](#eq:c41-unit-overlaps)。在一般仅有$U(1)$的模型中，则要保留左右块留数，或先作合适的插值场重定；这里用于联系两荷通道的$C$对称性也须另行满足。

对于已经选好单位重叠的马约拉纳场，有
<span id="eq:c41-majorana-overlaps"></span>

$$
\begin{aligned}
\langle0|\Psi(x)|0\rangle&=0,\\
\langle\mathbf p,s|\Psi(x)|0\rangle&=v_s(\mathbf p)e^{-ipx},\\
\langle\mathbf p,s|\bar\Psi(x)|0\rangle&=\bar u_s(\mathbf p)e^{-ipx}.
\end{aligned}
\tag{41.36}
$$

将第二行转置，并在右侧乘$\mathcal C$，用$v_s^T\mathcal C=\bar u_s$即可得到第三行。这里不再有两种独立的荷态。马约拉纳实条件联系场的两个频率支，左右块重叠的选择仍须与式[（41.34）](#eq:c41-general-overlap)所说明的条件相容。

<span id="c41-parameters"></span>

## 四费米例中的三个归一条件

场的重标度会相应改变拉格朗日量的系数。以四费米相互作用为例，写出
<span id="eq:c41-renormalized-lagrangian"></span>

$$
\mathcal L
=iZ\bar\Psi\slashed\partial\Psi
-Z_m m\bar\Psi\Psi
-\frac14 Z_g g(\bar\Psi\Psi)^2.
\tag{41.37}
$$

其中$m$是所选稳定粒子的物理质量，$g$由指定运动学条件下的散射量定义，具体条件在使用模型时选定。前因子$1/4$是定义$g$时采用的规范，而$Z$调到单位单粒子重叠。三类系数分别服务于质量、耦合和外腿归一化，须由相应条件确定；自由方程并不将它们预先约束成同一个数。

在保留调节的模型中，场与参数怎样一同变化可以直接写出。设原场为$\chi$，动能系数为一，质量和四费米系数为$m_0,g_0$，标量单粒子重叠为$\sqrt R$。作重标度$\chi=\sqrt R\,\Psi$后，每个双线性量带来一个$R$，因此
<span id="eq:c41-rescaling-parameters"></span>

$$
\begin{aligned}
\mathcal L
&=iR\bar\Psi\slashed\partial\Psi
-Rm_0\bar\Psi\Psi
-\frac14R^2g_0(\bar\Psi\Psi)^2,\\
Z&=R,\qquad Z_m m=Rm_0,\qquad Z_g g=R^2g_0.
\end{aligned}
\tag{41.38}
$$

物理质量$m$包含相互作用修正，故$m_0$与$m$一般不同；由散射量定义的$g$也不必等于$g_0$。若模型还保留其他有效算符，它们同样按所含场的数目重标度。

守恒流也随场定义改变。对局部相位变分$\delta\Psi=-i\alpha(x)\Psi$、$\delta\bar\Psi=+i\alpha(x)\bar\Psi$，无导数的质量项和四费米项不产生$\partial_\mu\alpha$。动能项的变分则有两部分，不含$\partial\alpha$的项彼此抵消，只剩
<span id="eq:c41-rescaled-current"></span>

$$
\delta\mathcal L
=Z(\partial_\mu\alpha)\bar\Psi\gamma^\mu\Psi,
\qquad
j^\mu=Z\bar\Psi\gamma^\mu\Psi.
\tag{41.39}
$$

在这个受调节的一阶拉氏量中，正则动量为$iZ\Psi^\dagger$，约束消元相应给出$\{\Psi_\alpha(\mathbf x),\Psi_\beta^\dagger(\mathbf y)\}
=Z^{-1}\delta_{\alpha\beta}\delta^3(\mathbf x-\mathbf y)$。将它与流中的系数一起代入，并作相容的真空减除，荷对场的生成作用为
<span id="eq:c41-rescaled-charge"></span>

$$
\begin{aligned}
Q&=Z\int d^3y\,\Psi^\dagger(\mathbf y)\Psi(\mathbf y),\\
[Q,\Psi_\alpha(\mathbf x)]
&=-Z\int d^3y\,Z^{-1}\delta^3(\mathbf x-\mathbf y)
\Psi_\alpha(\mathbf y)
=-\Psi_\alpha(\mathbf x).
\end{aligned}
\tag{41.40}
$$

两处重标度因子抵消，故式[（41.31）](#eq:c41-charge-selection)中的荷选择关系保持不变。如果相互作用还包含场导数，它们也须通过局部相位变分贡献于守恒流。

在四维，$[\Psi]=3/2$，从而$[(\bar\Psi\Psi)^2]=6$、$[g]=-2$。按[第18节的计幂](/posts/srednicki-18/#c18)与[第29节的有效理论](/posts/srednicki-29/#c29)，高阶修正会产生更多高维及导数算符。因此，式[（41.37）](#eq:c41-renormalized-lagrangian)适合作为有截止或已指定低能展开阶数的归一化例子，更高阶项各有相应的反项系数。在这个范围内，质量、耦合及场归一条件确定后，散射计算便归结为求$\langle0|T\{\Psi\cdots\bar\Psi\cdots\}|0\rangle$。下一节从自由费米子传播子开始建立计算这些关联函数的工具。

---

[← 第 40 节](/posts/srednicki-40/) · [章节地图](/srednicki/) · [第 42 节 →](/posts/srednicki-42/)
