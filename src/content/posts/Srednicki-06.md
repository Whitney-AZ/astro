---
title: 'Srednicki §6 量子力学中的路径积分'
date: 2026-09-14
category: 笔记
tags: [物理, 量子场论, Srednicki]
series: 'Srednicki QFT'
srednickiSections: [6]
hideFromHome: true
draft: false
---

<span id="c06"></span>

将演化分成短时间段，在每两段之间插入完备态，传播振幅便化为对中间位置、动量的积分。连续切片的记号就是路径积分；在各时刻加入算符，还会自然产生LSZ公式中的时间序乘积。先考虑一维量子力学，取 $\hbar=1$，哈密顿量为

<span id="eq:c06-hamiltonian"></span>

$$
H=K+V(Q),\qquad K=\frac{P^2}{2m},\qquad [Q,P]=i,\qquad m>0.
\tag{6.1}
$$

所求的是粒子从 $t'$ 时刻的位置 $q'$ 传播到 $t''$ 时刻的位置 $q''$ 的振幅。记总时间为 $T=t''-t'>0$，在薛定谔绘景中它就是演化算符的矩阵元：

<span id="eq:c06-propagation-kernel"></span>

$$
\mathcal K(q'',t'';q',t')
=\langle q''|e^{-iHT}|q'\rangle.
\tag{6.2}
$$

位置本征态 $|q\rangle$ 按 $\langle q|q'\rangle=\delta(q-q')$ 归一化，因而 $\mathcal K$ 是传播算符在位置表象中的积分核：用它对初始位置积分，便得到初态波函数的时间演化。

<span id="c06-slices"></span>

## 在中间时刻插入完备态

也可以在海森堡绘景中描述同一振幅。位置算符随时间变为 $Q(t)=e^{iHt}Qe^{-iHt}$，它在各时刻的本征态以及这些态之间的重叠为

<span id="eq:c06-instantaneous-states"></span>

$$
|q,t\rangle=e^{iHt}|q\rangle,\qquad
Q(t)|q,t\rangle=q|q,t\rangle,
\qquad
\langle q'',t''|q',t'\rangle=\mathcal K(q'',t'';q',t').
\tag{6.3}
$$

验证第二式时，只需将 $Q(t)$ 作用在所定义的态上：相邻的 $e^{-iHt}e^{iHt}$ 相消后，留下 $e^{iHt}Q|q\rangle$，便可使用位置本征值方程。第三式则将末态取厄米共轭，再合并两个演化指数。这里随 $t$ 改变的是 $Q(t)$ 的本征基底；海森堡绘景中的物理态矢仍保持不变。

现在把传播时间 $T$ 分成 $N+1$ 段，令 $\delta t=T/(N+1)$、$q_0=q'$、$q_{N+1}=q''$。每到一个中间时刻，就在相邻演化算符之间插入一次 $1=\int_{-\infty}^{+\infty}dq_j\,|q_j\rangle\langle q_j|$。对所有中间位置求和，传播振幅便精确地分解为

<span id="eq:c06-completeness-slicing"></span>

$$
\mathcal K
=\int\prod_{j=1}^{N}dq_j
\prod_{j=0}^{N}
\langle q_{j+1}|e^{-iH\delta t}|q_j\rangle .
\tag{6.4}
$$

上式对 $N$ 个内部位置积分，含有 $N+1$ 个短时传播因子；两个端点已由初、末态固定。切片本身没有引入近似，它只是把长时间演化拆成了可以反复使用的同一个短时问题。

要在短时间内分别处理动能和势能，就须控制忽略二者不对易性所产生的误差。记 $A=-iK\delta t$、$B=-iV\delta t$，把指数展开到二阶：

<span id="eq:c06-bch-expansion"></span>

$$
\begin{aligned}
e^Ae^B&=1+A+B+\tfrac12A^2+AB+\tfrac12B^2+O(\delta t^3),\\
e^{A+B}&=1+A+B+\tfrac12A^2+\tfrac12(AB+BA)+\tfrac12B^2
+O(\delta t^3).
\end{aligned}
\tag{6.5}
$$

两行相减，乘积展开比整体展开多出 $\tfrac12[A,B]$，所以在这一阶应补上一个对易子：
$e^{A+B}=e^Ae^B e^{-\frac12[A,B]+O(\delta t^3)}$。
这给出Baker–Campbell–Hausdorff展开在二阶的形式。由于 $[A,B]=-(\delta t)^2[K,V]$，把 $e^{-iH\delta t}$ 写成分解的乘积 $e^{-iK\delta t}e^{-iV\delta t}$ 时，两者从二阶起才有差异。

对有界算符或有限截断，单段误差的累积可以由以下恒等式估计：

<span id="eq:c06-product-error"></span>

$$
F^M-U^M=\sum_{j=0}^{M-1}F^{M-1-j}(F-U)U^j,
\quad
F=e^{-iK\delta t}e^{-iV\delta t},\quad U=e^{-iH\delta t}.
\tag{6.6}
$$

若单段满足 $\|F-U\|\leq C(\delta t)^2$，利用各幺正因子的范数为一，$M=N+1$段的总误差便不超过 $CT\delta t$，随切片变细而消失。

连续坐标中的动能 $K=P^2/(2m)$是无界算符。对有界实势 $V$，可以转到相互作用绘景来证明切片乘积在每个态上的收敛。令 $V_I(t)=e^{iKt}Ve^{-iKt}$、$h=T/M$，有

<span id="eq:c06-trotter-interaction"></span>

$$
e^{iKT}\bigl(e^{-iKh}e^{-iVh}\bigr)^M
=e^{-ihV_I((M-1)h)}\cdots e^{-ihV_I(h)}e^{-ihV_I(0)}.
$$

将右侧按 $V$的幂展开，第 $n$阶在 $M\to\infty$时趋于

$$
(-i)^n\int_{0<t_n<\cdots<t_1<T}
 dt_1\cdots dt_n\,V_I(t_1)\cdots V_I(t_n).
$$

这是强连续函数的黎曼和；同一切片重复选取的贡献随 $h$趋于零。第 $n$阶的范数由 $(T\|V\|)^n/n!$控制，因此可以逐阶取极限，再对 $n$求和。所得的Dyson级数正是 $e^{iKT}e^{-i(K+V)T}$。这就证明了有界实势下的切片极限。以下用切片表示路径积分；涉及更一般势能时，取相应哈密顿量的自伴实现和收敛的切片处方。

分开动能和势能之后，每一段就容易计算了。在两者之间插入 $1=\int dp\,|p\rangle\langle p|$，让动能作用在动量本征态上，让势能作用在位置本征态上；两个算符分别成为普通数，剩下的只有位置与动量态的重叠：

<span id="eq:c06-short-kernel"></span>

$$
\begin{aligned}
\langle q_{j+1}|e^{-iK\delta t}e^{-iV\delta t}|q_j\rangle
&=\int dp_j\,
e^{-i\delta t\,p_j^2/(2m)-i\delta t\,V(q_j)}
\langle q_{j+1}|p_j\rangle\langle p_j|q_j\rangle\\
&=\int\frac{dp_j}{2\pi}
\exp\!\left\{ip_j(q_{j+1}-q_j)
-i\delta t\,H(p_j,q_j)\right\}.
\end{aligned}
\tag{6.7}
$$

这里的 $1/(2\pi)$ 来自两份 $\langle q|p\rangle=(2\pi)^{-1/2}e^{ipq}$。式[（6.7）](#eq:c06-short-kernel)精确给出了分解后乘积的核；用它表示原来的 $e^{-iH\delta t}$，则须采用刚才讨论的短时近似。把各段的这些普通积分连接起来，就能用位置和动量变量代替算符演化。

<span id="c06-weyl"></span>

## Weyl排序与中点处方

在连接各段之前，还要说明更一般的 $H(P,Q)$ 应怎样处理。由于 $P,Q$ 不对易，经典函数中相同的乘积可以给出不同的量子算符；例如 $PQ=QP-i$，选取 $PQ$、$QP$ 或二者的平均便有不同含义。因此，必须先规定排序，才能谈论相应的路径积分。这里采用Weyl排序（Weyl ordering），从经典函数 $H(p,q)$ 的傅里叶表示定义量子算符。引入辅助积分变量 $u,v$，定义

<span id="eq:c06-weyl-definition"></span>

$$
H_W(P,Q)
=\int\frac{du\,dv}{(2\pi)^2}
e^{iuP+ivQ}
\int dp\,dq\,e^{-iup-ivq}H(p,q).
\tag{6.8}
$$

这一式规定了量子化时的算符次序；对于多项式，傅里叶积分按分布理解。我们接着求它的位置表象核，看看这种排序对短时积分提出了什么要求。

由于 $[iuP,ivQ]=iuv$ 是常数，BCH展开中的高阶嵌套对易子消失，且对称分解 $e^{iuP+ivQ}=e^{ivQ/2}e^{iuP}e^{ivQ/2}$ 左右两侧产生的常数项恰好相消。在位置表象中，$P=-i\partial_q$ 使 $e^{iuP}\psi(q)=\psi(q+u)$，所以平移算符的核为 $\delta(q_2-q_1+u)$。再乘上两端的位置相位，得到

<span id="eq:c06-weyl-exponential"></span>

$$
\langle q_2|e^{iuP+ivQ}|q_1\rangle
=e^{iv(q_1+q_2)/2}\delta(q_2-q_1+u).
\tag{6.9}
$$

将这个核代回式[（6.8）](#eq:c06-weyl-definition)，先作 $u$ 积分，delta函数令 $u=-(q_2-q_1)$；再作 $v$ 积分，两个位置相位与傅里叶相位合并后令 $q=(q_1+q_2)/2$。于是

<span id="eq:c06-weyl-kernel"></span>

$$
\langle q_2|H_W|q_1\rangle
=\int\frac{dp}{2\pi}\,
e^{ip(q_2-q_1)}
H\!\left(p,\frac{q_1+q_2}{2}\right).
\tag{6.10}
$$

由此可见，Weyl排序把经典函数的位置变量放在短时间段的中点。例如对于 $H(p,q)=pq$，式[（6.8）](#eq:c06-weyl-definition)的混合二阶项给出 $H_W=(PQ+QP)/2=-i(q\partial_q+\tfrac12)$；其中 $1/2$ 来自对 $q$ 的求导，正是排序所留下的量子修正。

把 $e^{-iH_W\delta t}$ 展开到一阶，再代入式[（6.10）](#eq:c06-weyl-kernel)，就得到短时相空间核。其位置取值应为 $\bar q_j=(q_{j+1}+q_j)/2$，而不再是原先端点分解中的 $q_j$。将各段相乘，得到

<span id="eq:c06-phase-slicing"></span>

$$
\mathcal K
=\lim_{N\to\infty}
\int\left[\prod_{j=1}^{N}dq_j\right]
\left[\prod_{j=0}^{N}\frac{dp_j}{2\pi}\right]
\exp\!\left\{
i\sum_{j=0}^{N}
\left[p_j(q_{j+1}-q_j)
-\delta t\,H(p_j,\bar q_j)\right]\right\}.
\tag{6.11}
$$

这里采用Weyl排序对应的中点处方。式[（6.10）](#eq:c06-weyl-kernel)给出哈密顿量的精确核，短时指数则保留到所需的一阶，再按式[（6.11）](#eq:c06-phase-slicing)取极限。对于 $P^2/(2m)+V(Q)$，也可使用式[（6.7）](#eq:c06-short-kernel)的端点处方；在两种切片都收敛到该哈密顿量的势能范围内，它们给出同一传播核。含有动量、位置混合项时，切片中的位置取值随算符排序确定。

引入每段的差分速度 $\dot q_j=(q_{j+1}-q_j)/\delta t$ 后，指数中的求和就有了相空间作用量 $\int dt\,[p\dot q-H]$ 的形式。于是式[（6.11）](#eq:c06-phase-slicing)可以用更便于观察物理内容的记号写成

<span id="eq:c06-phase-path-integral"></span>

$$
\mathcal K
=\int_{q(t')=q'}^{q(t'')=q''}\mathcal Dq\,\mathcal Dp\,
\exp\!\left\{
i\int_{t'}^{t''}dt\,[p(t)\dot q(t)-H(p(t),q(t))]
\right\}.
\tag{6.12}
$$

这就是相空间路径积分。位置路径的两端固定，而每一段的动量都要积分。记号 $\mathcal Dq\,\mathcal Dp$ 指刚才定义的切片测度，$\dot q$ 也由相邻切点的差分给出。每组中间位置和动量贡献一个由作用量决定的相位；将这些相位振幅相加，才得到从指定初态到末态的传播振幅。

<span id="c06-gaussian"></span>

## 从相空间积分到位置路径积分

对式[（6.1）](#eq:c06-hamiltonian)中的哈密顿量，每段的 $p_j$ 都只出现在二次式中，因此可以先做完全部动量积分，留下只含位置路径的表示。实时间下的高斯积分带有振荡相位，我们先从收敛的积分确定它的数值和平方根分支。取 $\operatorname{Re}a>0$，定义 $I(a,b)=\int dp\,e^{-ap^2+ibp}/(2\pi)$。先令 $b=0$，把不含 $1/(2\pi)$ 的一维积分平方，改写为二维平面积分，再使用极坐标：

$$
\left(\int_{-\infty}^{\infty}dp\,e^{-ap^2}\right)^2
=2\pi\int_0^\infty dr\,r e^{-ar^2}=\frac{\pi}{a}.
$$

由于积分绝对收敛，可以交换积分并作上述换元。平方根取在正实 $a$ 上为正、向整个右半平面连续延拓的分支。对于一般实 $b$，无需重新计算二重积分：对 $\int dp\,\partial_p e^{-ap^2+ibp}=0$ 分部积分，便得到 $\partial_b I=-bI/(2a)$。解这个一阶方程，并以刚才 $b=0$ 的结果定出常数，就有

<span id="eq:c06-complex-gaussian"></span>

$$
I(a,b)=\frac1{\sqrt{4\pi a}}\exp\!\left(-\frac{b^2}{4a}\right).
\tag{6.13}
$$

所需的振荡积分可以从右半平面趋近得到。令 $a=\eta+i\delta t/(2m)$，保持 $\eta>0$ 时先完成积分，最后取 $\eta\downarrow0$。由于 $\delta t>0$，沿这条路径得到

<span id="eq:c06-fresnel"></span>

$$
\int\frac{dp}{2\pi}
\exp\!\left[-\frac{i\delta t}{2m}p^2+ip\Delta q\right]
=\left(\frac{m}{2\pi i\delta t}\right)^{1/2}
\exp\!\left[\frac{im(\Delta q)^2}{2\delta t}\right],
\quad i^{-1/2}=e^{-i\pi/4}.
\tag{6.14}
$$

左边的实时间积分按这个收敛因子的极限理解，右边平方根的相位也由同一极限确定。因此，逐段积掉 $p_j$ 时，指数和前因子都必须保留。将它们代回切片表达式，得到位置空间的路径积分：

<span id="eq:c06-configuration-slicing"></span>

$$
\begin{aligned}
\mathcal K
=\lim_{N\to\infty}
\left(\frac{m}{2\pi i\delta t}\right)^{(N+1)/2}
\int\prod_{j=1}^{N}dq_j\,
\exp\!\left\{
i\sum_{j=0}^{N}\delta t
\left[\frac m2\left(\frac{q_{j+1}-q_j}{\delta t}\right)^2
-V(q_j^\star)\right]\right\}.
\end{aligned}
\tag{6.15}
$$

这里 $q_j^\star=q_j$ 表示先前的端点分解，$q_j^\star=\bar q_j$ 则表示适用时的Weyl中点处方。每段高斯积分贡献一个平方根，所以总前因子的指数为 $(N+1)/2$；内部位置只有 $N$ 个，并不改变动量积分的个数。把这些因子收入位置路径测度，可以记为

<span id="eq:c06-configuration-measure"></span>

$$
\mathcal Dq
=\lim_{N\to\infty}
\left(\frac{m}{2\pi i\delta t}\right)^{(N+1)/2}
\prod_{j=1}^{N}dq_j,\qquad
L(\dot q,q)=\frac m2\dot q^2-V(q),
\tag{6.16}
$$

$\mathcal Dq$包含各段高斯积分的前因子，并与指数一起按切片取极限。下面计算自由粒子时，将看到这些前因子怎样保证相邻时间段正确合成。

指数中的拉格朗日量也可直接从每段的代数看出。将动量二次式完成平方：

<span id="eq:c06-legendre-square"></span>

$$
p\dot q-\frac{p^2}{2m}-V
=-\frac1{2m}(p-m\dot q)^2+\frac m2\dot q^2-V.
\tag{6.17}
$$

高斯积分消去了第一项中的动量变量，留下的正是在驻点 $p=m\dot q$ 处的指数。这个驻点满足关系 $\dot q=\partial H/\partial p$，因而剩余部分与经典力学中消去动量所得到的拉格朗日量相同。由于指数对 $p$ 恰为二次式，这里完成的是整个高斯积分，无须另作驻相近似。

这一步也说明了推广时应保留哪些因子。若 $H(p,q)=\tfrac12a(q)p^2+b(q)p+c(q)$ 且 $a(q)>0$，仍可完成平方，得到

<span id="eq:c06-general-quadratic"></span>

$$
p_*=\frac{\dot q-b(q)}{a(q)},\qquad
L=\frac{[\dot q-b(q)]^2}{2a(q)}-c(q),
\qquad
\text{每段前因子}=\frac1{\sqrt{2\pi i\delta t\,a(\bar q_j)}}.
\tag{6.18}
$$

若 $a$ 随位置变化，高斯前因子也随路径变化，必须留在测度内。至于 $a=0$ 的情形，动量只以一次幂出现，相应积分成为

$$
\int\frac{dp}{2\pi}\,e^{i\delta t\,p(\dot q-b)}
=\delta(\delta t(\dot q-b)),
$$

这个积分约束路径满足 $\dot q=b(q)$。因此，非退化的动量二次项给出高斯积分，一次项则给出delta约束。

<span id="c06-free-kernel"></span>

## 自由粒子的传播核

取 $V=0$，把剩下的 $q_j$积分逐个做完。将一个时间段的核记作

<span id="eq:c06-free-step"></span>

$$
K_\tau(x,y)
=\left(\frac{m}{2\pi i\tau}\right)^{1/2}
\exp\!\left[\frac{im(x-y)^2}{2\tau}\right],
\qquad \tau>0.
\tag{6.19}
$$

积分一个中间位置，就相当于合并它两侧的传播时间。因此先计算 $\int dq\,K_\tau(x,q)K_\sigma(q,y)$。把两个指数中的平方合在一起，并围绕共同的平方中心整理：

<span id="eq:c06-free-completing-square"></span>

$$
\frac{(x-q)^2}{\tau}+\frac{(q-y)^2}{\sigma}
=\frac{\tau+\sigma}{\tau\sigma}
\left(q-\frac{\sigma x+\tau y}{\tau+\sigma}\right)^2
+\frac{(x-y)^2}{\tau+\sigma}.
\tag{6.20}
$$

第一项包含待积的中间位置，第二项只依赖固定端点。对第一项取式[（6.14）](#eq:c06-fresnel)在 $\Delta q=0$ 时的复共轭，并去掉测度中的 $1/(2\pi)$，便可积分带正号的二次相位，得到 $\sqrt{2\pi i\tau\sigma/[m(\tau+\sigma)]}$。这个因子与原先两个核的前因子相乘，化为 $\sqrt{m/[2\pi i(\tau+\sigma)]}$；再与剩下的端点相位合并，便得到时间相加的核：

<span id="eq:c06-free-composition"></span>

$$
\int dq\,K_\tau(x,q)K_\sigma(q,y)=K_{\tau+\sigma}(x,y).
\tag{6.21}
$$

上述平方和平移可以先在收敛积分中完成：令 $\tau\to\tau(1-i\epsilon)$、$\sigma\to\sigma(1-i\epsilon)$，其中 $\epsilon>0$。由于两段时间乘以同一个因子，平方中心 $(\sigma x+\tau y)/(\tau+\sigma)$ 仍为实数，积分又绝对收敛，所以直接平移实变量即可。最后取 $\epsilon\downarrow0$，平方根始终沿式[（6.14）](#eq:c06-fresnel)规定的分支趋近。

这条合成规则可以连续使用。先积 $q_1$，把前两段合为 $2\delta t$；再积 $q_2$，把合成的时间延长为 $3\delta t$。依此积掉所有内部位置，最终只剩总时间 $T=(N+1)\delta t$：

<span id="eq:c06-free-full"></span>

$$
\mathcal K_0(q'',t'';q',t')
=\left(\frac{m}{2\pi iT}\right)^{1/2}
\exp\!\left[\frac{im(q''-q')^2}{2T}\right].
\tag{6.22}
$$

自由粒子的短时核本来就是精确的，因此任意有限切片数都会给出这个结果。其指数等于连接两端点的匀速经典路径的作用量，而围绕这条路径的所有偏离已经通过高斯积分汇入前因子。经典路径在结果中格外醒目，正是因为偏离它的二次作用量可以完整积分。

自由哈密顿量在动量表象中对角化，还提供了一条更直接的算法。只插入一次动量完备态，而不作时间切片：

<span id="eq:c06-free-momentum-check"></span>

$$
\begin{aligned}
\langle q''|e^{-iP^2T/(2m)}|q'\rangle
&=\int\frac{dp}{2\pi}\,
e^{-iTp^2/(2m)+ip(q''-q')}\\
&=\left(\frac{m}{2\pi iT}\right)^{1/2}
e^{im(q''-q')^2/(2T)}.
\end{aligned}
\tag{6.23}
$$

最后一行仍使用刚才的高斯积分，所得的核与逐段合成完全相同。若恢复 $\hbar$，每段的作用量相位应除以 $\hbar$，同时 $\langle q|p\rangle$ 的归一化变为 $(2\pi\hbar)^{-1/2}$，因而

<span id="eq:c06-free-units"></span>

$$
\mathcal K_0
=\left(\frac{m}{2\pi i\hbar T}\right)^{1/2}
\exp\!\left[\frac{im(q''-q')^2}{2\hbar T}\right].
\tag{6.24}
$$

这个核具有逆长度量纲，与初态波函数对 $dq'$ 积分后，得到量纲相同的末态波函数。它也满足零时间的初始条件：在 $T\to0$ 的分布极限中，动量表示退回 $\int dp\,e^{ip(q''-q')/\hbar}/(2\pi\hbar)=\delta(q''-q')$，于是传播算符恢复为单位算符。

<span id="c06-insertions"></span>

## 在路径上插入算符

传播核已经包含了初、末态之间的整个演化。若要计算其中某一时刻的位置矩阵元，只需在该时刻把演化分开，再插入位置算符。考虑矩阵元 $\langle q'',t''|Q(t_1)|q',t'\rangle$，其中 $t'<t_1<t''$；转回薛定谔绘景，它写为

<span id="eq:c06-q-insertion"></span>

$$
\langle q'',t''|Q(t_1)|q',t'\rangle
=\langle q''|e^{-iH(t''-t_1)}
Qe^{-iH(t_1-t')}|q'\rangle.
\tag{6.25}
$$

让 $t_1$ 落在一个切点上，在 $Q$ 两边各插入位置完备态。由于 $\langle q_+|Q|q_-\rangle=q_-\delta(q_+-q_-)$，delta函数把两侧位置认作同一个切点，两次积分合为一次，并留下 $q(t_1)$。其余切片的计算不变，所以只须在原来的路径积分中多乘一个位置因子：

<span id="eq:c06-path-insertion"></span>

$$
\langle q'',t''|Q(t_1)|q',t'\rangle
=\int\mathcal Dp\,\mathcal Dq\,q(t_1)e^{iS},
\qquad
S=\int_{t'}^{t''}dt\,[p\dot q-H].
\tag{6.26}
$$

对两个插入，若 $t_1<t_2$，切开演化便有 $e^{-iH(t''-t_2)}Qe^{-iH(t_2-t_1)}Qe^{-iH(t_1-t')}$。较晚的算符自然位于左边。若 $t_2<t_1$，两个算符在演化链中的位置便对调；但路径中的普通数 $q(t_1)q(t_2)$ 不因交换而改变。因此，无论两个时刻的先后如何，同一个路径积分给出的都是

<span id="eq:c06-time-ordering"></span>

$$
\int\mathcal Dp\,\mathcal Dq\,q(t_1)q(t_2)e^{iS}
=\langle q'',t''|T\{Q(t_1)Q(t_2)\}|q',t'\rangle.
\tag{6.27}
$$

时间排序因而来自演化算符的合成次序。增加更多插入时，仍按各时刻切开演化区间，逐次插入完备态，每次留下一个 $q(t_j)$。上一节LSZ公式所需要的时间序关联函数，正好具有这种结构。

若插入动量，就在相应的短时核中使用动量完备态，留下 $p_j$。不同时间的 $Q$ 和 $P$ 仍按演化次序排列；落在同一切片内的乘积，则由已经选定的Weyl中点处方解释。例如同一时刻的 $pq$ 对应 $(PQ+QP)/2$。相空间中的普通乘积，只有连同这项切片约定，才确定了相应的算符乘积。

<span id="c06-functional"></span>

## 用外源生成这些插入

我们不必为每一组插入重新组织完备态求和。只要在作用量中加入一个任意的外源，再对它求导，就能从指数中取出所需的位置或动量因子。为此，先引入泛函导数（functional derivative）：若 $\mathcal F[f]$ 依赖于整个函数 $f(t)$，其导数由任意小变化 $\delta f$ 下的一阶变化定义：

<span id="eq:c06-functional-definition"></span>

$$
\mathcal F[f+\delta f]-\mathcal F[f]
=\int dt\,\frac{\delta\mathcal F}{\delta f(t)}\delta f(t)
+O(\delta f^2).
\tag{6.28}
$$

最简单的例子是 $\mathcal F[f]=f(t_2)$。把它的变化写成 $\delta f(t_2)=\int dt_1\,\delta(t_1-t_2)\delta f(t_1)$，再与定义比较，就得到

<span id="eq:c06-functional-delta"></span>

$$
\frac{\delta f(t_2)}{\delta f(t_1)}
=\delta(t_1-t_2).
\tag{6.29}
$$

其余求导规则与普通微分相同。两个泛函相乘时，各自变化后保留一阶项便得到乘积法则，复合依赖也给出链式法则；例如 $\delta\int dt\,a(t)f(t)^2/\delta f(s)=2a(s)f(s)$。

切片形式则直接说明了delta函数的归一化。离散变量满足 $\delta\mathcal F=\sum_j(\partial\mathcal F/\partial f_j)\delta f_j$，而式[（6.28）](#eq:c06-functional-definition)中的积分化为黎曼和时，每一项还带有时间步长。比较两者，得到

<span id="eq:c06-functional-lattice"></span>

$$
\frac{\delta}{\delta f(t_j)}
\ \longleftrightarrow\
\frac1{\delta t}\frac{\partial}{\partial f_j},
\qquad
\delta(t_j-t_k)\ \longleftrightarrow\
\frac{\delta_{jk}}{\delta t}.
\tag{6.30}
$$

泛函导数中的 $1/\delta t$ 正好补偿作用量求和中的 $\delta t$，所以从切片形式到连续记号不会多出时间步长。

现在加入两种指定的外源，令 $H_{f,h}(t)=H-f(t)Q-h(t)P$。其中 $f$ 是作用在位置上的通常外力，$h$ 与动量耦合。哈密顿量在作用量中带负号，因此这两个源项进入相空间指数时都取正号：

<span id="eq:c06-source-kernel"></span>

$$
\mathcal K[f,h]
=\int\mathcal Dp\,\mathcal Dq\,
\exp\!\left\{
iS+i\int_{t'}^{t''}dt\,[f(t)q(t)+h(t)p(t)]
\right\}.
\tag{6.31}
$$

对外源求一次导数，指数便带下 $iq$ 或 $ip$。为了直接得到插入因子，记 $D_f(t)=i^{-1}\delta/\delta f(t)$、$D_h(t)=i^{-1}\delta/\delta h(t)$，分别求一次位置源导数、两次位置源导数以及一次动量源导数，得到

<span id="eq:c06-source-differentiation"></span>

$$
\begin{aligned}
D_f(t_1)\mathcal K[f,h]
&=\int\mathcal Dp\,\mathcal Dq\,q(t_1)e^{iS+i\int(fq+hp)},\\
D_f(t_1)D_f(t_2)\mathcal K[f,h]
&=\int\mathcal Dp\,\mathcal Dq\,q(t_1)q(t_2)e^{iS+i\int(fq+hp)},\\
D_h(t_1)\mathcal K[f,h]
&=\int\mathcal Dp\,\mathcal Dq\,p(t_1)e^{iS+i\int(fq+hp)}.
\end{aligned}
\tag{6.32}
$$

先完成所需次数的微分，再令 $f=h=0$，作用量便回到原来没有外力的理论，而取出的因子仍留在积分中。结合刚才对时间排序的推导，这些关系可统一写成

<span id="eq:c06-generated-insertions"></span>

$$
\langle q'',t''|T\{Q(t_1)\cdots P(s_1)\cdots\}|q',t'\rangle
=
\left.
D_f(t_1)\cdots D_h(s_1)\cdots\mathcal K[f,h]
\right|_{f=h=0}.
\tag{6.33}
$$

插入时刻分离时，右边生成通常的时间序乘积；同一切片内的乘积按中点规则解释。积掉动量以后，动量源的二阶导数会产生一个接触项，可以直接算出来。

仍取 $H=p^2/(2m)+V(q)$，在保留非零 $h$ 的情况下，对 $p(\dot q+h)-p^2/(2m)$ 完成平方。动量积分给出

<span id="eq:c06-momentum-source-integrated"></span>

$$
\mathcal K[f,h]
=\int\mathcal Dq\,
\exp\!\left\{i\int dt
\left[\frac m2(\dot q+h)^2-V(q)+fq\right]\right\}.
\tag{6.34}
$$

现在作用一次 $D_h$，会从指数中带下 $m(\dot q+h)$；再求一次导数时，既作用于指数，也作用于前一因子中的 $h$。两部分都保留，然后令外源为零，便有

<span id="eq:c06-momentum-contact"></span>

$$
\left.D_h(t_1)D_h(t_2)\mathcal K[f,h]\right|_0
=\int\mathcal Dq\,
\left[m^2\dot q(t_1)\dot q(t_2)-im\delta(t_1-t_2)\right]e^{iS_L}.
\tag{6.35}
$$

这里 $S_L=\int dt\,L$。第二项中的 $-i$ 来自 $1/i$；在切片上，正是 $D_{h,j}=1/(i\delta t)\,\partial_{h_j}$ 再次作用于 $mh_j$ 所产生的项。因此，积掉动量后计算 $PP$ 插入，除了速度乘积，还必须包括这个接触项。若只需要 $Q$ 的关联函数，则可从一开始取 $h=0$，避免引入动量源。

<span id="c06-vacuum"></span>

## 用长时间演化选出基态

前面一直把初、末位置固定。如果改为指定初态波函数 $\psi_{\rm in}$ 和末态波函数 $\psi_{\rm out}$，只要将传播核乘以 $\psi_{\rm out}^*(q'')\psi_{\rm in}(q')$，再对两个端点积分即可。场论中需要的是真空之间的关联函数；对应到这里，就要选择两端为基态，并把初、末时间移向无穷远。

要实现这个选择，假定 $H$ 有唯一、可归一化的基态 $|0\rangle$，将能量零点平移到 $E_0=0$，其余能谱非负。先把位置本征态按能量本征态展开，得到

<span id="eq:c06-energy-resolution"></span>

$$
|q',t'\rangle
=\sum_n\psi_n(q')^*e^{iE_nt'}|n\rangle,
\qquad \psi_n(q)=\langle q|n\rangle .
\tag{6.36}
$$

式中的求和表示离散能谱，连续部分相应改写为谱积分。置 $H\to(1-i\epsilon)H$，其中 $\epsilon>0$，再写 $t'=-T$，各能量分量便带有 $e^{-iE_nT}e^{-\epsilon E_nT}$。保持 $\epsilon$固定并令 $T\to\infty$，正能量部分受到指数压制，零能基态则保留下来。

为了在可归一化的态上实行这一投影，先用边界波函数 $\chi$ 对 $q'$ 涂抹。只要它与基态的重叠 $c_0=\langle0|\chi\rangle\ne0$，就得到

<span id="eq:c06-ground-projection"></span>

$$
e^{-iHT-\epsilon HT}|\chi\rangle
\longrightarrow c_0|0\rangle .
\tag{6.37}
$$

若存在能隙 $\Delta>0$，基态正交分量的范数至多为 $e^{-\epsilon\Delta T}\|\chi-c_0|0\rangle\|$，衰减速度由能隙直接控制。即使没有能隙，只要指定的零能本征态确实存在，对正能谱上的平方范数积分使用支配收敛，也得到同一投影结论。基态若有简并，则保留的是整个零能子空间。

末端的左矢同样含有 $\langle\chi_{\rm out}|e^{-iHT-\epsilon HT}$，长时间极限留下 $\langle\chi_{\rm out}|0\rangle\langle0|$。因此，可以用与基态重叠非零的简单边界态来准备真空，而不必预先求出基态波函数。前面整条直线上的自由粒子没有可归一化基态，其传播核仍然成立，但不适用这一步基态投影。

令外源只在有限时间区间内非零，使两端足够长的演化负责选择基态。将采用上述收敛处方、边界态为 $\chi_{\rm in},\chi_{\rm out}$ 的振幅记为 $\mathcal A_{T,\epsilon}[f,h]$；除以同样边界条件下的零源振幅，便得到归一化的真空生成泛函：

<span id="eq:c06-vacuum-normalization"></span>

$$
Z[f,h]
=\lim_{\epsilon\downarrow0}\lim_{T\to\infty}
\frac{\mathcal A_{T,\epsilon}[f,h]}
{\mathcal A_{T,\epsilon}[0,0]},
\qquad Z[0,0]=1.
\tag{6.38}
$$

分子和分母具有相同的两端重叠常数，取比值后这些常数消去。先在 $\epsilon>0$时取长时间极限选出基态，再令 $\epsilon\downarrow0$，便恢复有限插入区间内的实时间演化。

将端点因子和零源归一化收入测度，便得到简洁的路径积分形式：

<span id="eq:c06-vacuum-functional"></span>

$$
Z[f,h]
=\mathcal N\int\mathcal Dp\,\mathcal Dq\,
\exp\!\left\{
i\int_{-\infty}^{+\infty}dt
[p\dot q-(1-i\epsilon)H+fq+hp]
\right\},
\tag{6.39}
$$

常数 $\mathcal N$ 由 $Z[0,0]=1$ 确定，$\epsilon$ 的极限按前式理解。至此，式[（6.33）](#eq:c06-generated-insertions)中的两端态已换成真空；对 $Z$ 作源导数，就能统一产生所有真空时间序关联函数。

<span id="c06-perturbation"></span>

## 将相互作用改写成微分算符

路径积分把所求的关联函数收入同一个生成泛函，但一般相互作用的积分还不能直接做出。为进行微扰计算，将哈密顿量分成 $H=H_0+H_1$，其中 $H_0$ 可解，$H_1$ 按小耦合展开。先保留有限切片和同一边界处方，把相互作用对应的指数展开：

<span id="eq:c06-interaction-expansion"></span>

$$
e^{-i\int dt\,H_1(p,q)}
=\sum_{r=0}^{\infty}\frac{(-i)^r}{r!}
\prod_{\ell=1}^{r}\int dt_\ell\,H_1(p(t_\ell),q(t_\ell)).
\tag{6.40}
$$

每项中的 $p(t_\ell)$ 可以由 $D_h(t_\ell)$ 从外源指数取出，$q(t_\ell)$ 则由 $D_f(t_\ell)$ 取出。因此，各项中的相互作用因子都能按同一展开改写为源导数；把导数移到路径积分之外，再将级数合回指数，得到

<span id="eq:c06-perturbation-operator"></span>

$$
\mathcal Z[f,h]
=\exp\!\left[-i\int dt\,H_1(D_h(t),D_f(t))\right]
Z_0[f,h].
\tag{6.41}
$$

这里的 $Z_0$ 是可解理论的生成泛函，暂时仍保留有限的初、末时间。微分指数按 $H_1$ 的幂逐阶作用，完成源导数与下面的零源归一化后，再取式 [（6.38）](#eq:c06-vacuum-normalization) 的极限。同一切片内的导数乘积采用与原 $H_1$ 的Weyl符号相同的处方。上式为简洁省略了 $\epsilon$；恢复长时间极限时，两部分哈密顿量必须采用同一个收敛处方。

还要处理相互作用对归一化的改变。微分指数作用于 $Z_0$ 后，零源值一般会变化，所以即使原先 $Z_0[0,0]=1$，仍须重新取比值：

<span id="eq:c06-perturbative-normalization"></span>

$$
Z[f,h]=\frac{\mathcal Z[f,h]}{\mathcal Z[0,0]}.
\tag{6.42}
$$

这一步所需的常数也可收入测度。它在微扰展开中有明确的作用：分母消去与外部插入无关的真空贡献，使生成泛函保持规定的零源值。

例如取 $H_1=\lambda Q^4/4!$，将式[（6.41）](#eq:c06-perturbation-operator)保留到 $\lambda$ 的一次项。对于一组由源导数产生的插入 $\mathcal O$，把分子和分母分别展开，再取二者之比，得到

<span id="eq:c06-vacuum-subtraction"></span>

$$
\begin{aligned}
\langle T\mathcal O\rangle
={}&\langle T\mathcal O\rangle_0
-\frac{i\lambda}{4!}\int dt\,
\bigl[
\langle T\{\mathcal O Q_0(t)^4\}\rangle_0\\
&\hspace{9em}
-\langle T\mathcal O\rangle_0\langle Q_0(t)^4\rangle_0
\bigr]+O(\lambda^2).
\end{aligned}
\tag{6.43}
$$

下标0表示矩阵元按 $H_0$ 计算。方括号中的第二个乘积来自分母展开 $(1+\lambda a)^{-1}=1-\lambda a+O(\lambda^2)$，恰好减去与 $\mathcal O$ 无关的真空插入。这样，每一阶需要计算什么就确定了：按相互作用顶点的次数展开，再求可解理论中相应的矩阵元。

若 $H_1$ 只依赖 $q$，所求的又只是 $Q$ 的关联函数，便可以令 $h=0$。进一步，若 $H$ 对 $p$ 至多二次，且二次项系数为非零常数，则按前面的高斯积分消去动量，得到 $L=L_0+L_1$、$L_1(q)=-H_1(q)$。微扰公式于是化为拉格朗日形式：

<span id="eq:c06-lagrangian-perturbation"></span>

$$
\begin{aligned}
\mathcal Z[f]
&=\exp\!\left[i\int dt\,L_1(D_f(t))\right]Z_0[f],\\
Z_0[f]
&=\mathcal N_0\int\mathcal Dq\,
\exp\!\left\{i\int dt\,[L_0(\dot q,q)+f(t)q(t)]\right\},
\qquad
Z[f]=\frac{\mathcal Z[f]}{\mathcal Z[0]}.
\end{aligned}
\tag{6.44}
$$

指数中的 $-iH_1$ 因而改写为 $+iL_1$，因为这里 $L_1=-H_1$。计算关联函数的步骤现在已经确定：先求可解系统在任意外源下的生成泛函，再以源导数逐次加入相互作用，并除去零源值。下一节选择谐振子，具体完成其中的第一步。

---

[← 第 5 节](/posts/srednicki-05/) · [章节地图](/srednicki/) · [第 7 节 →](/posts/srednicki-07/)
