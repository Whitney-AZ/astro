---
title: 'Srednicki §39 旋量场的正则量子化 II'
date: 2026-09-14
category: 笔记
tags: [物理, 量子场论, Srednicki]
series: 'Srednicki QFT'
srednickiSections: [39]
hideFromHome: true
draft: false
---

<span id="c39"></span>

第37节建立了场在同一时刻的反对易关系，第38节则求出了平面波展开所需的旋量，并固定了它们的归一与相位。现在要把这两部分合起来，说明量子化的旋量场怎样描述粒子。为此，先从场中提取模式系数，把场的反对易关系转化为模式算符的关系；再将哈密顿量和守恒荷写成这些算符的组合，粒子的能量及电荷便有了明确的含义。狄拉克场的这一构造完成后，再施加马约拉纳条件，就能看清粒子与反粒子的两套模式怎样合为一套。

以下沿用[第38节](/posts/srednicki-38/#c38)的旋量基和四维度规$(-,+,+,+)$。质量壳上的四动量记为$p^\mu=(\omega_{\mathbf p},\mathbf p)$，洛伦兹不变测度为$\widetilde{dp}=d^3p/[(2\pi)^3\,2\omega_{\mathbf p}]$。本节主体取$m>0$，末尾的类空局域性计算也讨论$m=0$。

<span id="c39-inversion"></span>

## 从场中提取模式算符

模式算符的运动与代数都要从场的关系出发。将第 36、37 节得到的狄拉克作用量、运动方程及等时量子化条件列在一起：

<span id="eq:c39-start"></span>

$$
\begin{gathered}
\mathcal L=i\bar\Psi\gamma^\mu\partial_\mu\Psi-m\bar\Psi\Psi,
\qquad (-i\slashed\partial+m)\Psi=0,\\
\{\Psi_\alpha(t,\mathbf x),\Psi_\beta(t,\mathbf y)\}=0,\\
\{\Psi_\alpha(t,\mathbf x),\bar\Psi_\beta(t,\mathbf y)\}
=(\gamma^0)_{\alpha\beta}\delta^3(\mathbf x-\mathbf y).
\end{gathered}
\tag{39.1}
$$

这几条关系在构造中的作用不同：运动方程来自作用量的变分，反对易关系则规定量子场的代数，是第37节已说明的量子化公设。为便于后面的投影运算，将最后一式右乘$\beta=\gamma^0$，便可写成$\{\Psi_\alpha,\Psi_\beta^\dagger\}=\delta_{\alpha\beta}\delta^3$。运动方程的平面波解则仍由上一节的两套旋量展开：

<span id="eq:c39-expansion"></span>

$$
\Psi(x)=\sum_{s=\pm1}\int\widetilde{dp}\,
\left[b_s(\mathbf p)u_s(\mathbf p)e^{ipx}
+d_s^\dagger(\mathbf p)v_s(\mathbf p)e^{-ipx}\right].
\tag{39.2}
$$

其中$u_s,v_s$是数值列，$b_s,d_s^\dagger$才是要确定代数的算符。狄拉克方程已把每个频率支的旋量限制在二维空间内，因此场的四个分量并不对应四种独立的标量模式。求模式算符时，既要分离空间动量，也要用旋量的正交性分离两条频率支。

先固定时刻，乘$e^{-ipx}$并对空间积分。$u$项产生$(2\pi)^3\delta^3(\mathbf q-\mathbf p)$，$v$项产生$(2\pi)^3\delta^3(\mathbf q+\mathbf p)$。两种$\delta$函数只约束三动量，所以后一项虽然取了反向三动量，两项能量仍同为正，留下的时间指数为$e^{i(\omega_{\mathbf p}+\omega_{-\mathbf p})t}=e^{2i\omega_{\mathbf p}t}$。保留这一相位，空间积分便给出

<span id="eq:c39-first-fourier"></span>

$$
\int d^3x\,e^{-ipx}\Psi(x)
=\frac1{2\omega_{\mathbf p}}\sum_r
\left[b_r(\mathbf p)u_r(\mathbf p)
+e^{2i\omega_{\mathbf p}t}d_r^\dagger(-\mathbf p)v_r(-\mathbf p)\right].
\tag{39.3}
$$

空间积分后还混合着两条频率支，接着左乘$u_s^\dagger(\mathbf p)=\bar u_s(\mathbf p)\gamma^0$作旋量投影。由[（38.15）](/posts/srednicki-38/#eq:c38-vector-products)、[（38.16）](/posts/srednicki-38/#eq:c38-opposite-momenta)，$u_s^\dagger u_r=2\omega_{\mathbf p}\delta_{sr}$消去第一项的测度分母并选出自旋标签，而$u_s^\dagger(\mathbf p)v_r(-\mathbf p)=0$使另一频率支消失。于是只留下

<span id="eq:c39-b-inverse"></span>

$$
b_s(\mathbf p)=\int d^3x\,e^{-ipx}\bar u_s(\mathbf p)\gamma^0\Psi(x).
\tag{39.4}
$$

湮灭算符由此表达成了场的线性投影。求它的伴随时，$\bar u\gamma^0\Psi=u^\dagger\Psi$是数值行与算符列的缩并，故$(u^\dagger\Psi)^\dagger=\Psi^\dagger u=\bar\Psi\gamma^0u$；这里只有一个奇算符因子，取伴随的反序不会产生反交换负号。若采用矩阵的狄拉克伴随记号，则用到$\bar A=\beta A^\dagger\beta$及$\overline{\gamma^0}=\gamma^0$。这样得到产生算符的反演式：

<span id="eq:c39-bdag-inverse"></span>

$$
b_s^\dagger(\mathbf p)=\int d^3x\,e^{ipx}\bar\Psi(x)\gamma^0u_s(\mathbf p).
\tag{39.5}
$$

提取$d_s^\dagger$时，使用相反的傅里叶指数，就能先选出另一条频率支所需的三动量。这时$b$项要求$\mathbf q=-\mathbf p$，$d^\dagger$项要求$\mathbf q=\mathbf p$；作同样的空间积分，得到

<span id="eq:c39-second-fourier"></span>

$$
\int d^3x\,e^{ipx}\Psi(x)
=\frac1{2\omega_{\mathbf p}}\sum_r
\left[e^{-2i\omega_{\mathbf p}t}b_r(-\mathbf p)u_r(-\mathbf p)
+d_r^\dagger(\mathbf p)v_r(\mathbf p)\right].
\tag{39.6}
$$

再左乘$v_s^\dagger$，由$v_s^\dagger v_r=2\omega\delta_{sr}$选出目标模式，由$v_s^\dagger(\mathbf p)u_r(-\mathbf p)=0$消去另一项。对所得式取伴随，就依次得到两个反演式：

<span id="eq:c39-d-inverse"></span>

$$
\begin{aligned}
d_s^\dagger(\mathbf p)
&=\int d^3x\,e^{ipx}\bar v_s(\mathbf p)\gamma^0\Psi(x),\\
d_s(\mathbf p)
&=\int d^3x\,e^{-ipx}\bar\Psi(x)\gamma^0v_s(\mathbf p).
\end{aligned}
\tag{39.7}
$$

这些反演式虽写有$t$，投影的结果却应与所选时刻无关，因为自由场的时间演化已经包含在平面波因子中。这个性质可直接由第37节的厄米矩阵$h(\mathbf p)=\gamma^0\gamma^i p_i+m\gamma^0$说明：场方程为$i\partial_t\Psi=h(-i\nabla)\Psi$，两种旋量分别满足$u_s^\dagger h(\mathbf p)=\omega u_s^\dagger$、$v_s^\dagger h(-\mathbf p)=-\omega v_s^\dagger$。对[（39.4）](#eq:c39-b-inverse)、[（39.7）](#eq:c39-d-inverse)求时间导数后，将场上的空间导数分部积分到投影因子上，平面波相位的导数便与场的时间导数相消：

<span id="eq:c39-time-independence"></span>

$$
\begin{aligned}
\partial_t b_s
&=i\omega b_s-i\int d^3x\,e^{-ipx}u_s^\dagger h(\mathbf p)\Psi=0,\\
\partial_t d_s^\dagger
&=-i\omega d_s^\dagger-i\int d^3x\,e^{ipx}v_s^\dagger h(-\mathbf p)\Psi=0.
\end{aligned}
\tag{39.8}
$$

上述分部积分可先对衰减波包进行，或在周期盒中利用边界条件消去边界项。两种投影的空间波数相反，因而第二行的矩阵为$h(-\mathbf p)$；正是相应的负本征值使该行的两个时间导数项相消。

<span id="c39-car"></span>

## 模式的反对易关系

既然模式投影不依赖时刻，计算任意两个模式的反对易子时，就可以把它们都表示成同一时刻的场，并使用[（39.1）](#eq:c39-start)。先看只含同一种场的投影：$b$、$d^\dagger$都是$\Psi$的线性组合，所以$\{\Psi,\Psi\}=0$给出$\{b,b\}=\{b,d^\dagger\}=\{d^\dagger,d^\dagger\}=0$。对这些关系取厄米共轭，又得到另外三式。将它们合写为

<span id="eq:c39-zero-cars"></span>

$$
\begin{gathered}
\{b_s(\mathbf p),b_r(\mathbf q)\}
=\{d_s(\mathbf p),d_r(\mathbf q)\}
=\{b_s(\mathbf p),d_r^\dagger(\mathbf q)\}=0,\\
\{b_s^\dagger(\mathbf p),b_r^\dagger(\mathbf q)\}
=\{d_s^\dagger(\mathbf p),d_r^\dagger(\mathbf q)\}
=\{b_s^\dagger(\mathbf p),d_r(\mathbf q)\}=0.
\end{gathered}
\tag{39.9}
$$

其中$\{d,d\}=0$来自场关系的厄米共轭，因为$d$是伴随场的投影，而非$\Psi$本身的投影。余下的反对易子要用场与伴随场之间的关系，其归一由两次空间积分决定。以下略写$\omega_{\mathbf p}=\omega_p$；将两个反演式代入，逐步积分可得

<span id="eq:c39-b-car"></span>

$$
\begin{aligned}
\{b_s(\mathbf p),b_r^\dagger(\mathbf q)\}
&=\int d^3x\,d^3y\,e^{-ipx+iqy}
u_s^\dagger(\mathbf p)\{\Psi(x),\Psi^\dagger(y)\}u_r(\mathbf q)\\
&=\int d^3x\,e^{-i(p-q)x}u_s^\dagger(\mathbf p)u_r(\mathbf q)\\
&=(2\pi)^3\delta^3(\mathbf p-\mathbf q)
e^{i(\omega_p-\omega_q)t}\,2\omega_p\delta_{sr}\\
&=(2\pi)^3\,2\omega_p\delta^3(\mathbf p-\mathbf q)\delta_{sr}.
\end{aligned}
\tag{39.10}
$$

空间$\delta$函数使两个三动量相等，因而能量也相等，剩余时间相位才化为1。如果始终采用狄拉克伴随记号，两个投影各带一个$\gamma^0$，场的反对易子再给出一个，缩并为$\bar u\gamma^0\gamma^0\gamma^0u=\bar u\gamma^0u$，三个$\gamma^0$分别来自这两次投影与场的反对易子。反粒子的计算沿同样步骤进行，只须将投影中的$u$换成$v$，并反转指数号。于是得到

<span id="eq:c39-d-car"></span>

$$
\begin{aligned}
\{d_s^\dagger(\mathbf p),d_r(\mathbf q)\}
&=(2\pi)^3\delta^3(\mathbf p-\mathbf q)
e^{-i(\omega_p-\omega_q)t}v_s^\dagger(\mathbf p)v_r(\mathbf q)\\
&=(2\pi)^3\,2\omega_p\delta^3(\mathbf p-\mathbf q)\delta_{sr}.
\end{aligned}
\tag{39.11}
$$

这个归一用的是正的$v^\dagger v=2\omega$；$\bar v v=-2m$是另一种旋量缩并，不能代入这里的投影。最后考虑$b$与$d$，两个反演式中的傅里叶指数同号，空间积分便把两个三动量固定为相反方向。保留这一动量约束，得到

<span id="eq:c39-mixed-car"></span>

$$
\begin{aligned}
\{b_s(\mathbf p),d_r(\mathbf q)\}
&=\int d^3x\,e^{-i(p+q)x}u_s^\dagger(\mathbf p)v_r(\mathbf q)\\
&=(2\pi)^3\delta^3(\mathbf p+\mathbf q)e^{2i\omega_p t}
u_s^\dagger(\mathbf p)v_r(-\mathbf p)=0.
\end{aligned}
\tag{39.12}
$$

这里$\delta$函数只反转三动量，两项能量仍相加，因而保留着时间相位。相位一直乘在混合旋量内积上，因内积为零而不再贡献。取伴随还得到$\{b^\dagger,d^\dagger\}=0$，至此两种粒子、每种两个自旋模式的代数便已确定。由$[\Psi]=3/2$及$[u]=[v]=1/2$，场展开给出$[b]=[d]=-1$；反对易子右侧的$2\omega\delta^3$也具有质量维数$-2$，与模式归一相符。

模式代数还应重现出发时的场关系。为看清旋量求和在其中的作用，把这些模CAR代回[（39.2）](#eq:c39-expansion)，再使用自旋求和式[（38.19）](/posts/srednicki-38/#eq:c38-spin-sums)。在等时分离$z=x-y=(0,\mathbf x-\mathbf y)$处，得到

<span id="eq:c39-field-car-check"></span>

$$
\begin{aligned}
\{\Psi(x),\bar\Psi(y)\}
&=\int\widetilde{dp}\,
\left[(-\slashed p+m)e^{ipz}+(-\slashed p-m)e^{-ipz}\right]\\
&=\int\frac{d^3p}{(2\pi)^3\,2\omega_p}\,
2\omega_p\gamma^0e^{i\mathbf p\cdot(\mathbf x-\mathbf y)}
=\gamma^0\delta^3(\mathbf x-\mathbf y).
\end{aligned}
\tag{39.13}
$$

第二行只在后一项作$\mathbf p\to-\mathbf p$。这样空间$\gamma$项和质量项分别相消，留下的能量因子正好消去质量壳测度的分母，重现局域的场归一。后面量子化马约拉纳场时，还会用到这一结果。

<span id="c39-hamiltonian"></span>

## 哈密顿量的四项展开

要把模式解释为粒子，还需要知道每个模式带多少能量。从[第37节](/posts/srednicki-37/#c37-dirac)的勒让德变换所得的$H=\int d^3x\,\bar\Psi(-i\gamma^i\partial_i+m)\Psi$出发，将场换成模式展开。计算时先让微分算符作用在右边的场上：对$u$项，$-i\partial_i$给出$+p_i$；对$v$项则给出$-p_i$。再分别代入两条在壳方程，就可将空间微分核化成能量因子：

<span id="eq:c39-h-operator"></span>

$$
\begin{gathered}
(\gamma^i p_i+m)u_s=\omega_p\gamma^0u_s,\qquad
(-\gamma^i p_i+m)v_s=-\omega_p\gamma^0v_s,\\
(-i\gamma^i\partial_i+m)\Psi
=\sum_s\int\widetilde{dp}\,\omega_p
\left[b_s\gamma^0u_s e^{ipx}
-d_s^\dagger\gamma^0v_s e^{-ipx}\right].
\end{gathered}
\tag{39.14}
$$

$d^\dagger$项由此带上负号，它来自负频率方程，此时还没有交换任何模式算符。接着展开左边的场，其两项为$b_r^\dagger(\mathbf q)\bar u_r(\mathbf q)e^{-iqx}$和$d_r(\mathbf q)\bar v_r(\mathbf q)e^{iqx}$，并对$r$求和、对$\widetilde{dq}$积分。与[（39.14）](#eq:c39-h-operator)相乘时保持算符的原次序，四项的空间积分分别要求$\mathbf q=\mathbf p,-\mathbf p,-\mathbf p,\mathbf p$。积掉$\widetilde{dq}$后，由$\omega_p/(2\omega_q)=1/2$得到公共半因子，于是四项展开为

<span id="eq:c39-h-four-terms"></span>

$$
\begin{aligned}
H=\frac12\sum_{s,r}\int\widetilde{dp}\,\bigl[
&b_r^\dagger(\mathbf p)b_s(\mathbf p)
u_r^\dagger(\mathbf p)u_s(\mathbf p)\\
&-b_r^\dagger(-\mathbf p)d_s^\dagger(\mathbf p)
u_r^\dagger(-\mathbf p)v_s(\mathbf p)e^{2i\omega_p t}\\
&+d_r(-\mathbf p)b_s(\mathbf p)
v_r^\dagger(-\mathbf p)u_s(\mathbf p)e^{-2i\omega_p t}\\
&-d_r(\mathbf p)d_s^\dagger(\mathbf p)
v_r^\dagger(\mathbf p)v_s(\mathbf p)\bigr].
\end{aligned}
\tag{39.15}
$$

中间两项分别含相反三动量的旋量内积，按[（38.16）](/posts/srednicki-38/#eq:c38-opposite-momenta)各自为零。另两项的内积各给$2\omega_p\delta_{sr}$，与前面的$1/2$相乘留下一个能量因子，故哈密顿量化为

<span id="eq:c39-h-unordered"></span>

$$
H=\sum_s\int\widetilde{dp}\,\omega_p
\left[b_s^\dagger(\mathbf p)b_s(\mathbf p)
-d_s(\mathbf p)d_s^\dagger(\mathbf p)\right].
\tag{39.16}
$$

这里仍保持着场展开给定的算符次序。要读出反粒子的占据数，才需要用$\{d,d^\dagger\}$把第二项的产生算符移到左边。由于$-dd^\dagger=d^\dagger d-\{d,d^\dagger\}$，反粒子的数算符也带正能量，同时留下一个负的常数。能谱的正性和真空能的负号正是在这一步同时出现的。

<span id="c39-vacuum"></span>

### 零点能和真空

先用有限模式把这个常数的含义写清楚。取体积$V$的周期盒，并保留一个关于$\mathbf p\mapsto-\mathbf p$对称的有限动量集合；连续归一中的空间$\delta$函数在离散动量上变为$V\delta_{\mathbf p\mathbf q}$。将模式归一为单位反对易关系，令

<span id="eq:c39-box-normalization"></span>

$$
\begin{gathered}
B_{s\mathbf p}=\frac{b_s(\mathbf p)}{\sqrt{2\omega_p V}},
\qquad D_{s\mathbf p}=\frac{d_s(\mathbf p)}{\sqrt{2\omega_p V}},\\
\{B_{s\mathbf p},B_{r\mathbf q}^\dagger\}
=\{D_{s\mathbf p},D_{r\mathbf q}^\dagger\}
=\delta_{sr}\delta_{\mathbf p\mathbf q},\\
\int\widetilde{dp}\ \longrightarrow\
\frac1V\sum_{\mathbf p}\frac1{2\omega_p}.
\end{gathered}
\tag{39.17}
$$

这样[（39.16）](#eq:c39-h-unordered)变为有限和$H=\sum_{s,\mathbf p}\omega_p(B^\dagger B-DD^\dagger)$。第二项换序时，每个自旋标签贡献常数$-\omega_p$，两个标签共给$-2\sum_{\mathbf p}\omega_p$。为了和标量场比较，必须使用同一质量、同一盒及同一动量调节；在这些条件下，第3节一个实标量场的零点能密度为

<span id="eq:c39-scalar-zero-point"></span>

$$
\mathcal E_0=\frac1{2V}\sum_{\mathbf p}\omega_p
\ \longrightarrow\ \frac12\int\frac{d^3p}{(2\pi)^3}\omega_p.
\tag{39.18}
$$

用这个共同的零点能密度表示刚才的常数，便将哈密顿量写为

<span id="eq:c39-dirac-zero-point"></span>

$$
H=\sum_s\int\widetilde{dp}\,\omega_p
\left[b_s^\dagger b_s+d_s^\dagger d_s\right]-4\mathcal E_0V.
\tag{39.19}
$$

连续写法中的$V=(2\pi)^3\delta^3(\mathbf0)=\int d^3x$是上述盒极限的简记。与实标量场相比，负号来自费米算符的反交换，四倍则对应粒子、反粒子各有两个自旋自由度。在当前自由平直时空模型中，可以在$\mathcal L$中加常数$\Omega_0$来选定能量零点。它不改变正则动量，所以$H$改变$-\Omega_0V$；取$\Omega_0=-4\mathcal E_0$，恰好抵消[（39.19）](#eq:c39-dirac-zero-point)的最后一项。以下$H$均采用真空能为零的这一选择。

剩下的各项都是正能量系数与数算符的乘积，而每个模式能占据多少粒子，则由反对易关系决定。对任一个归一盒模式$c$，CAR给出$c^2=(c^\dagger)^2=0$，并有

<span id="eq:c39-occupation"></span>

$$
N^2=c^\dagger c\,c^\dagger c
=c^\dagger(1-c^\dagger c)c=N,\qquad
\langle\chi|N|\chi\rangle=\|c|\chi\rangle\|^2\geq0.
\tag{39.20}
$$

数算符既是投影又为正，因此每个模式只能占据0或1个粒子。所有$\omega_p$均为正，哈密顿量的最低能态便是所有模式都空置的态：

<span id="eq:c39-vacuum"></span>

$$
b_s(\mathbf p)|0\rangle=d_s(\mathbf p)|0\rangle=0,\qquad H|0\rangle=0.
\tag{39.21}
$$

这就是所有模式都空置的福克真空。在它上面作用产生算符，会增加相应模式的能量：由$[c^\dagger c,c^\dagger]=c^\dagger$，分别得到$[H,b_s^\dagger]=\omega_p b_s^\dagger$、$[H,d_s^\dagger]=\omega_p d_s^\dagger$。再将空间平移关系$[P^i,\Psi]=i\partial_i\Psi$代入反演式，并作一次分部积分，便有$[P^i,b_s^\dagger]=p_i b_s^\dagger$及$[P^i,d_s^\dagger]=p_i d_s^\dagger$。因此在平移不变的真空上，两类产生算符都产生四动量为$p^\mu$的单粒子态。它们的归一也直接来自模式代数，例如

<span id="eq:c39-one-particle-norm"></span>

$$
\langle0|b_r(\mathbf q)b_s^\dagger(\mathbf p)|0\rangle
=(2\pi)^3\,2\omega_p\delta^3(\mathbf p-\mathbf q)\delta_{rs}.
\tag{39.22}
$$

由这些态组成的波包$\sum_s\int\widetilde{dp}\,f_s(\mathbf p)b_s^\dagger(\mathbf p)|0\rangle$具有范数$\sum_s\int\widetilde{dp}\,|f_s|^2$。构造多粒子态时，交换两个不同模式的产生算符使态变号；若两次占据同一个模式，所得态则为零。模式代数由此实现了费米统计。

自旋标签$s$仍沿第38节的静止系选择。当$\mathbf p=p\hat{\mathbf z}$时，完整角动量$J_z$的本征值为$s/2$，其轨道项的分部积分见[第 38 节的轴向计算](/posts/srednicki-38/#eq:c38-orbital-axis)。对于一般方向的$\mathbf p$，动量本身会被绕第三轴的转动改变，此时$s$表示从静止系推动得到的自旋标签。

<span id="c39-wigner"></span>

### 洛伦兹变换中的自旋混合

一般洛伦兹变换除了改变动量，也会转动自旋。令$p_\star=(m,\mathbf0)$，并记$L(p)$为[第 38 节](/posts/srednicki-38/#c38-boost)把$p_\star$送到$p$、不附加转动的标准推动。对固有正时变换$\Lambda$，定义

<span id="eq:c39-wigner-rotation"></span>

$$
W(\Lambda,p)=L(\Lambda p)^{-1}\Lambda L(p),
\qquad W(\Lambda,p)p_\star=p_\star.
$$

保持$p_\star$使这个洛伦兹矩阵的时间行、列与空间部分分开，空间块是一个$SO(3)$转动。保持参考动量的变换组成小群，这里的$W$称为维格纳转动。它表示先推动到$p$再作$\Lambda$，与直接推动到$\Lambda p$相比，静止自旋轴还多转了一次。在洛伦兹覆盖群中，用$w(\Lambda,p)\in SU(2)$表示它对二分量自旋基的作用。

由定义，$D(\Lambda)D(L(p))=D(L(\Lambda p))D(W)$。静止$u_s$的两块都是$e_s$，静止$v_s$则使用$\eta_s=Ee_s$。反对称符号不变性给出$wEw^T=E$，再利用$w^Tw^*=I$，便有$wE=Ew^*$。因此两支旋量分别满足

<span id="eq:c39-spinor-intertwiners"></span>

$$
\begin{aligned}
D(\Lambda)u_s(\mathbf p)
&=\sum_r u_r(\boldsymbol{\Lambda p})w_{rs}(\Lambda,p),\\
D(\Lambda)v_s(\mathbf p)
&=\sum_r v_r(\boldsymbol{\Lambda p})w_{rs}^*(\Lambda,p).
\end{aligned}
$$

这里$\boldsymbol{\Lambda p}$表示变换后四动量的空间部分。第一式还给出$w_{rs}=\bar u_r(\boldsymbol{\Lambda p})D(\Lambda)u_s(\mathbf p)/(2m)$。对两个变换后的旋量作狄拉克内积，利用$\bar D D=I$和$\bar u_r u_s=2m\delta_{rs}$，可直接核对$w^\dagger w=I_2$。

将这两式代入场变换$U^{-1}\Psi(x)U=D(\Lambda)\Psi(\Lambda^{-1}x)$。在右侧令$p=\Lambda q$，质量壳测度不变，且$q\cdot\Lambda^{-1}x=p\cdot x$。分别比较两条频率支的系数，得到

<span id="eq:c39-mode-lorentz-first"></span>

$$
\begin{aligned}
U^{-1}b_r(\mathbf p)U&=\sum_s w_{rs}(\Lambda,q)b_s(\mathbf q),\\
U^{-1}d_r^\dagger(\mathbf p)U
&=\sum_s w_{rs}^*(\Lambda,q)d_s^\dagger(\mathbf q),
\qquad q=\Lambda^{-1}p.
\end{aligned}
$$

第一式取伴随以后，两类产生算符的系数相同。再用$W(\Lambda^{-1},p)=W(\Lambda,q)^{-1}$及$w^{-1}=w^\dagger$，就能将它们统一写成

<span id="eq:c39-creation-lorentz"></span>

$$
\begin{aligned}
U(\Lambda)^{-1}b_s^\dagger(\mathbf p)U(\Lambda)
&=\sum_r b_r^\dagger(\boldsymbol{\Lambda^{-1}p})w_{rs}(\Lambda^{-1},p),\\
U(\Lambda)^{-1}d_s^\dagger(\mathbf p)U(\Lambda)
&=\sum_r d_r^\dagger(\boldsymbol{\Lambda^{-1}p})w_{rs}(\Lambda^{-1},p).
\end{aligned}
$$

以$b_s^\dagger|0\rangle$、$d_s^\dagger|0\rangle$分别定义$|p,s,+\rangle$、$|p,s,-\rangle$，并取洛伦兹不变真空，单粒子态便按

<span id="eq:c39-state-lorentz"></span>

$$
U(\Lambda)|p,s,q\rangle
=\sum_r|\Lambda p,r,q\rangle w_{rs}(\Lambda,p),\qquad q=\pm1
$$

变换。这里$q$重新表示荷标签。态的归一已包含$2\omega_p$，因此不另出现能量平方根。静止系绕第三轴转动时，$w=e^{-i\theta\sigma_3/2}$，动量虽然不变，态仍有自旋相位；只有$W=I$或把转动吸收到随动基的定义中，变换式才可省去自旋矩阵。

<span id="c39-charge"></span>

## 守恒荷怎样区分粒子和反粒子

两种粒子的质量和自旋相同，要区别它们，就要考察狄拉克作用量的相位对称性及其守恒荷。第36节已由$\Psi\to e^{-i\alpha}\Psi$、$\bar\Psi\to e^{i\alpha}\bar\Psi$求得诺特流。具体说来，让$\alpha$暂时依赖$x$，不含相位导数的变分相消，动能中只留下导数作用在相位上的一项：

<span id="eq:c39-charge-current"></span>

$$
\delta\mathcal L=(\partial_\mu\alpha)\bar\Psi\gamma^\mu\Psi,\qquad
j^\mu=\bar\Psi\gamma^\mu\Psi,\qquad
Q=\int d^3x\,j^0=\int d^3x\,\Psi^\dagger\Psi.
\tag{39.23}
$$

将场方程用于这个局部变分，便得$\partial_\mu j^\mu=0$；再对空间积分，若边界没有流出，$Q$就守恒。它在模式空间中的含义，可用刚才求能量的步骤来求。从[（39.15）](#eq:c39-h-four-terms)的四种空间$\delta$函数继续计算，就能得到守恒荷的模式展开。由于右场上没有能量算符，四项都带正号，积掉一个质量壳测度后留下$1/(2\omega_p)$：

<span id="eq:c39-charge-four-terms"></span>

$$
\begin{aligned}
Q=\sum_{s,r}\int\frac{\widetilde{dp}}{2\omega_p}\,\bigl[
&b_r^\dagger(\mathbf p)b_s(\mathbf p)
u_r^\dagger(\mathbf p)u_s(\mathbf p)\\
&+b_r^\dagger(-\mathbf p)d_s^\dagger(\mathbf p)
u_r^\dagger(-\mathbf p)v_s(\mathbf p)e^{2i\omega_p t}\\
&+d_r(-\mathbf p)b_s(\mathbf p)
v_r^\dagger(-\mathbf p)u_s(\mathbf p)e^{-2i\omega_p t}\\
&+d_r(\mathbf p)d_s^\dagger(\mathbf p)
v_r^\dagger(\mathbf p)v_s(\mathbf p)\bigr].
\end{aligned}
\tag{39.24}
$$

两个交叉内积仍各自为零，两个对角内积则给$2\omega_p\delta_{sr}$并消去分母。再将反粒子算符排列为数算符，得到

<span id="eq:c39-charge-normal-order"></span>

$$
\begin{aligned}
Q_{\rm raw}
&=\sum_s\int\widetilde{dp}\,[b_s^\dagger b_s+d_s d_s^\dagger]\\
&=\sum_s\int\widetilde{dp}\,[b_s^\dagger b_s-d_s^\dagger d_s]+Q_0,\\
Q_0&=2\sum_{\mathbf p}1.
\end{aligned}
\tag{39.25}
$$

常数$Q_0$在[（39.17）](#eq:c39-box-normalization)的有限盒调节下，是反粒子两个自旋模式的总数。从$Q$中减去它，不改变荷与场的对易子，因此可以采用$Q|0\rangle=0$的归一。这样守恒荷便等于粒子数减反粒子数。其普通对易子为$[Q,b_s^\dagger]=b_s^\dagger$、$[Q,d_s^\dagger]=-d_s^\dagger$，从而两类单粒子态带相反的荷：

<span id="eq:c39-charge-eigenvalues"></span>

$$
\begin{aligned}
Qb_s^\dagger(\mathbf p)|0\rangle&=+b_s^\dagger(\mathbf p)|0\rangle,\\
Qd_s^\dagger(\mathbf p)|0\rangle&=-d_s^\dagger(\mathbf p)|0\rangle.
\end{aligned}
\tag{39.26}
$$

这一荷算符也生成出发时的对称变换。由$[Q,b_s]=-b_s$与$[Q,d_s^\dagger]=-d_s^\dagger$，场展开满足$[Q,\Psi]=-\Psi$，指数化便得到原来的相位转动。哈密顿量和$Q$都是模式数算符的线性组合，所以$[H,Q]=0$；同一组模式的能量与荷可以同时确定。$Q$无量纲，$H$则多一个$\omega$，分别对应占据数之差和能量之和。在电子的量子电动力学中，$b$型与$d$型粒子分别是电子和正电子；这里的$\pm1$仍是诺特荷的单位，实际电磁荷还须乘相应耦合常数。

<span id="c39-majorana"></span>

## 马约拉纳条件与一套模式

狄拉克场允许粒子和反粒子拥有独立的模式。若要求场等于其电荷共轭，这两套系数就必须联系起来。为此从[第36节](/posts/srednicki-36/#c36-majorana)的马约拉纳拉格朗日量及实条件出发：

<span id="eq:c39-majorana-lagrangian"></span>

$$
\begin{gathered}
\mathcal L_M=\frac i2\Psi^T\mathcal C\gamma^\mu\partial_\mu\Psi
-\frac m2\Psi^T\mathcal C\Psi,\\
\Psi=\mathcal C\bar\Psi^T,\qquad \bar\Psi=\Psi^T\mathcal C.
\end{gathered}
\tag{39.27}
$$

作用量中两次奇场变分补偿了整体的$1/2$，所以运动方程仍是狄拉克方程；详细变分见[第36节](/posts/srednicki-36/#c36-majorana)。平面波基因而无需改变，要确定的是实条件怎样限制两条频率支的系数。先对[（39.2）](#eq:c39-expansion)取伴随并乘$\beta$，随后转置、左乘$\mathcal C$，得到

<span id="eq:c39-conjugate-expansion"></span>

$$
\begin{aligned}
\bar\Psi(x)
&=\sum_s\int\widetilde{dp}\,
[b_s^\dagger\bar u_s e^{-ipx}+d_s\bar v_s e^{ipx}],\\
\mathcal C\bar\Psi^T(x)
&=\sum_s\int\widetilde{dp}\,
[b_s^\dagger\mathcal C\bar u_s^T e^{-ipx}
+d_s\mathcal C\bar v_s^T e^{ipx}]\\
&=\sum_s\int\widetilde{dp}\,
[b_s^\dagger v_s e^{-ipx}+d_s u_s e^{ipx}].
\end{aligned}
\tag{39.28}
$$

第二行给出电荷共轭的模式展开。利用[（38.32）](/posts/srednicki-38/#eq:c38-charge-pairing)已经固定相位的同标签关系$\mathcal C\bar u_s^T=v_s$、$\mathcal C\bar v_s^T=u_s$，便得到末行。它与原场的展开使用同一组旋量基，因此可以逐个比较$u_s e^{ipx}$与$v_s e^{-ipx}$的系数。实条件要求这些系数相等，于是

<span id="eq:c39-majorana-expansion"></span>

$$
\begin{gathered}
d_s(\mathbf p)=b_s(\mathbf p),\\
\Psi_M(x)=\sum_s\int\widetilde{dp}\,
[b_s(\mathbf p)u_s(\mathbf p)e^{ipx}
+b_s^\dagger(\mathbf p)v_s(\mathbf p)e^{-ipx}].
\end{gathered}
\tag{39.29}
$$

实条件把独立模式减为一套，它的代数由[第37节约束消元](/posts/srednicki-37/#c37-constraints)后的马约拉纳场关系决定。由于上下块已属于同一个场，混合自反对易子也随之改变：

<span id="eq:c39-majorana-field-cars"></span>

$$
\begin{aligned}
\{\Psi_{M\alpha}(t,\mathbf x),\Psi_{M\beta}(t,\mathbf y)\}
&=(\mathcal C\gamma^0)_{\alpha\beta}\delta^3(\mathbf x-\mathbf y),\\
\{\Psi_{M\alpha}(t,\mathbf x),\bar\Psi_{M\beta}(t,\mathbf y)\}
&=(\gamma^0)_{\alpha\beta}\delta^3(\mathbf x-\mathbf y).
\end{aligned}
\tag{39.30}
$$

其中场与伴随场的关系和狄拉克情形相同，故$\{b,b^\dagger\}$仍由[（39.10）](#eq:c39-b-car)的反演积分求得。场的自反对易子却已改变，$\{b,b\}$需要用第一式重新投影。令$\mathsf A=\mathcal C\gamma^0$，将$\mathsf A^T=\mathsf A$、$\mathsf A^2=I_4$及$v_s=\mathsf A u_s^*$用于两个反演式，计算成为

<span id="eq:c39-majorana-mode-cars"></span>

$$
\begin{aligned}
\{b_s(\mathbf p),b_r(\mathbf q)\}
&=(2\pi)^3\delta^3(\mathbf p+\mathbf q)e^{2i\omega_p t}
u_s^\dagger(\mathbf p)\mathsf A u_r^*(-\mathbf p)\\
&=(2\pi)^3\delta^3(\mathbf p+\mathbf q)e^{2i\omega_p t}
u_s^\dagger(\mathbf p)v_r(-\mathbf p)=0,\\
\{b_s(\mathbf p),b_r^\dagger(\mathbf q)\}
&=(2\pi)^3\,2\omega_p\delta^3(\mathbf p-\mathbf q)\delta_{sr}.
\end{aligned}
\tag{39.31}
$$

湮灭模式的自反对易子为零，仍来自两条频率支的旋量正交性：完整马约拉纳场的等时自反对易子虽非零，投影后的湮灭模式却彼此反对易。反过来，从模式展开求场关系时，场与其伴随仍满足[（39.13）](#eq:c39-field-car-check)；再用$\bar\Psi_M=\Psi_M^T\mathcal C$并右乘$\mathcal C^{-1}$，由$\gamma^0\mathcal C^{-1}=\mathcal C\gamma^0$便得到[（39.30）](#eq:c39-majorana-field-cars)第一式。两种场关系和一套模式代数由此相互衔接。

<span id="c39-majorana-energy"></span>

### 半因子、能量与统计

模式数减半以后，每个模式的能量仍应由场的哈密顿量确定。作勒让德变换时，马约拉纳作用量中的整体半因子仍然保留：

<span id="eq:c39-majorana-hamiltonian"></span>

$$
\begin{aligned}
H_M&=\frac12\int d^3x\,\Psi_M^T\mathcal C
(-i\gamma^i\partial_i+m)\Psi_M\\
&=\frac12\int d^3x\,\bar\Psi_M
(-i\gamma^i\partial_i+m)\Psi_M.
\end{aligned}
\tag{39.32}
$$

这里的空间微分核没有改变，可以沿用[（39.14）](#eq:c39-h-operator)、[（39.15）](#eq:c39-h-four-terms)已求出的四项空间积分，把$d,d^\dagger$换成$b,b^\dagger$，再乘整体的$1/2$。反向三动量的交叉内积仍为零，留下

<span id="eq:c39-majorana-h-unordered"></span>

$$
H_M=\frac12\sum_s\int\widetilde{dp}\,\omega_p
[b_s^\dagger b_s-b_s b_s^\dagger].
\tag{39.33}
$$

再用$b b^\dagger=\{b,b^\dagger\}-b^\dagger b$排列算符，两个相同的数算符项相加，恰好消去外面的半因子。每个盒模式同时留下常数$-\omega_p/2$，两个自旋标签共给$-\sum_{\mathbf p}\omega_p=-2\mathcal E_0V$，从而

<span id="eq:c39-majorana-zero-point"></span>

$$
H_M=\sum_s\int\widetilde{dp}\,\omega_p b_s^\dagger b_s
-2\mathcal E_0V.
\tag{39.34}
$$

取$\Omega_0=-2\mathcal E_0$就能同样把真空能选为零。每个$b_s^\dagger$仍增加能量$\omega_p$，但现在只有两种自旋态，反粒子不再构成独立的另一套模式。马约拉纳作用量的$1/2$与这种模式合并相配，使单个粒子的能量保持原来的归一。

反对易关系对这一能量解释不可缺少。若在[（39.33）](#eq:c39-majorana-h-unordered)中改用正定归一的普通对易关系，由$b^\dagger b-bb^\dagger=-[b,b^\dagger]$可知哈密顿量只剩一个常数，进而给出$[\Psi_M,H_M]=0$。它无法产生场展开中非零频率的时间演化，因而与当前自由场构造不相容。下面从类空分离处的场关系再推导一次统计号。

粒子与反粒子模式合并后，狄拉克场的共同相位转动也不再保持实条件：若$\Psi'_M=e^{-i\alpha}\Psi_M$，则$\mathcal C\bar\Psi_M^{\prime T}=e^{i\alpha}\Psi_M$，二者相等要求$e^{2i\alpha}=1$，只保留整体正负号。因此，前面用于区别$b$与$d$的矢量$U(1)$荷在这里不再存在。有质量单马约拉纳场没有这种连续的$U(1)$对称性；当$m=0$时，单外尔场的相位对称性仍在四分量记号中表现为手征转动，见[第36节的马约拉纳实条件](/posts/srednicki-36/#c36-majorana)。这一无质量对称性仍作用在现有的一套模式上，并不产生独立的第二套模式。

<span id="c39-locality"></span>

## 类空局域性怎样选出费米统计

现在从一套正能模式出发，比较对易与反对易两种选择。记$[A,B]_\sigma=AB-\sigma BA$，其中$\sigma=+1$表示对易子，$\sigma=-1$表示反对易子。假定同类产生、同类湮灭的括号为零，并取正的模式归一

<span id="eq:c39-statistics-postulate"></span>

$$
[b_s(\mathbf p),b_r^\dagger(\mathbf q)]_\sigma
=(2\pi)^3\,2\omega_p\delta^3(\mathbf p-\mathbf q)\delta_{sr}.
$$

将两个频率片段分开，定义

<span id="eq:c39-frequency-parts"></span>

$$
\Psi^+(x)=\sum_s\int\widetilde{dp}\,b_su_s e^{ipx},\qquad
\Psi^-(x)=\sum_s\int\widetilde{dp}\,b_s^\dagger v_s e^{-ipx}.
$$

固有正时变换保持未来与过去质量壳，所以这两片段分别服从旋量场的变换律；上面的旋量与模式变换式也可直接给出这一结果。它们的伴随则彼此联系。由$v_s=\mathcal C\bar u_s^T$、$\mathcal C^T=-\mathcal C$及$\mathcal C^2=-I$，有$v_s^T\mathcal C=\bar u_s$，从而

<span id="eq:c39-frequency-adjoint"></span>

$$
[\Psi^-(x)]^T\mathcal C\beta
=\sum_s\int\widetilde{dp}\,b_s^\dagger v_s^T\mathcal C\beta e^{-ipx}
=[\Psi^+(x)]^\dagger.
$$

一个只含湮灭片段的多项式取伴随以后，就含有对应的产生片段。构造厄米相互作用时两者都会出现，还要检查它们组合后的类空局域关系。以下$\overline{\Psi^+}$表示先取$\Psi^+$再作狄拉克伴随，因此它含产生算符及负频率指数；$\overline{\Psi^-}$则含湮灭算符。

令$z=x-y$，采用[第 4 节的正频率核](/posts/srednicki-04/#eq:c04-kernel-final)$W_+(z)=\int\widetilde{dp}\,e^{ipz}$。将模式括号与自旋求和代入，两个需要的矩阵核为

<span id="eq:c39-two-frequency-kernels"></span>

$$
\begin{aligned}
M_{\alpha\beta}(z)
&\equiv[\Psi_\alpha^+(x),\overline{\Psi^+}_\beta(y)]_\sigma\\
&=\int\widetilde{dp}\,(-\slashed p+m)_{\alpha\beta}e^{ipz}
=(i\slashed\partial_z+m)_{\alpha\beta}W_+(z),\\
F_{\alpha\beta}(z)
&\equiv[\Psi_\alpha^+(x),\Psi_\beta^-(y)]_\sigma
=\int\widetilde{dp}\,\sum_s(u_s)_\alpha(v_s)_\beta e^{ipz}
=-[M(z)\mathcal C]_{\alpha\beta}.
\end{aligned}
$$

第一式的导数号来自$i\partial_\mu e^{ipz}=-p_\mu e^{ipz}$，末式则用了$v_s^T=-\bar u_s\mathcal C$。它们都由$[b,b^\dagger]_\sigma$给出，所以到这一步还没有统计号的区别。

在类空区域$z^2=r^2>0$，[第 4 节](/posts/srednicki-04/#eq:c04-kernel-final)已计算出

<span id="eq:c39-spacelike-kernel"></span>

$$
W_+(z)=W_+(-z)=C_m(r),\qquad
C_m(r)=\frac{mK_1(mr)}{4\pi^2r},\qquad
C_0(r)=\frac1{4\pi^2r^2}.
$$

因$\partial_\mu r=z_\mu/r$，核$M$可写成$mC_m(r)I_4+i\slashed z\,C_m'(r)/r$。当$m>0$时，$K_1$的正积分表示使$\operatorname{tr}M=4mC_m(r)>0$，所以这个矩阵非零。当$m=0$时，直接对$C_0$求导得到$M(z)=-i\slashed z/(2\pi^2r^4)$；由$\slashed z^{\,2}=-r^2I_4$，它也非零。$\mathcal C$可逆，因此$F$同样非零。

接着同时交换时空点与旋量指标。类空处$W_+$为偶函数，故一阶导数在$-z$处反号；结合$\mathcal C(\gamma^\mu)^T=-\gamma^\mu\mathcal C$，逐步转置得

<span id="eq:c39-kernel-exchange"></span>

$$
\begin{aligned}
F(-z)^T
&=\bigl[(i\slashed\partial_z-m)W_+(z)\mathcal C\bigr]^T\\
&=-\mathcal C(i(\gamma^\mu)^T\partial_\mu-m)W_+(z)\\
&=(i\slashed\partial_z+m)W_+(z)\mathcal C=-F(z).
\end{aligned}
$$

取一般线性组合$\Psi_\lambda=\Psi^++\lambda\Psi^-$，其中$\lambda$为复数。自括号只含两个交叉项；用$[B,A]_\sigma=-\sigma[A,B]_\sigma$及上式，有

<span id="eq:c39-self-locality"></span>

$$
\begin{aligned}
[\Psi_{\lambda\alpha}(x),\Psi_{\lambda\beta}(y)]_\sigma
&=\lambda F_{\alpha\beta}(z)-\sigma\lambda F_{\beta\alpha}(-z)\\
&=\lambda(1+\sigma)F_{\alpha\beta}(z),\qquad z^2>0.
\end{aligned}
$$

场与伴随场的括号中，正频率贡献为$M(z)$，负频率贡献则带$[b^\dagger,b]_\sigma=-\sigma[b,b^\dagger]_\sigma$和$|\lambda|^2$。因此

<span id="eq:c39-adjoint-locality"></span>

$$
\begin{aligned}
[\Psi_\lambda(x),\bar\Psi_\lambda(y)]_\sigma
&=M(z)-\sigma|\lambda|^2
\int\widetilde{dp}\,(-\slashed p-m)e^{-ipz}\\
&=M(z)-\sigma|\lambda|^2(-i\slashed\partial_z-m)W_+(-z)\\
&=(1+\sigma|\lambda|^2)M(z),\qquad z^2>0.
\end{aligned}
$$

最后一步在整个类空区域使用$W_+(-z)=W_+(z)$，所以也可对它求导。由于$M$非零，取对易子时系数$1+|\lambda|^2$总为正；取反对易子时，自括号自动消失，伴随括号则要求$|\lambda|=1$。于是，在这套正能模式、正定归一与线性自由场构造中，两种类空局域关系同时成立，当且仅当采用费米统计且两频率片段的系数模相同。

若$\lambda=e^{i\vartheta}$，则$\Psi_\lambda^C=e^{-i\vartheta}\Psi_\lambda$，再定义$\Psi_M=e^{-i\vartheta/2}\Psi_\lambda$就恢复$\Psi_M^C=\Psi_M$。这与前面的马约拉纳场相位一致。由偶数个这种奇场构成的局域可观测量，在类空交换时经过偶数次反对易，因而满足普通的对易关系。

---

[← 第 38 节](/posts/srednicki-38/) · [章节地图](/srednicki/) · [第 40 节 →](/posts/srednicki-40/)
