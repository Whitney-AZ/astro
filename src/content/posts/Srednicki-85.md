---
title: 'Srednicki §85 自发破缺的阿贝尔规范理论'
date: 2026-09-14
category: 笔记
tags: [物理, 量子场论, Srednicki]
series: 'Srednicki QFT'
srednickiSections: [85]
hideFromHome: true
draft: false
---

<span id="c85"></span>

上一节说明，标量场的真空值可以使规范粒子获得质量，同时仍留下一个实标量粒子。现在要把这个描述用于量子计算。首先沿幺正规范量子化有质量矢量场，找出它的三个偏振态和传播子；随后考察圈图，便会看到为什么还需要保留角向标量，并采用另一种规范固定。这样得到的$R_\xi$规范既保持良好的大动量行为，又容许我们在计算中检查规范参数是否消去。

沿用[标量电动力学](/posts/srednicki-61/#c61)的协变导数，以及[上一节](/posts/srednicki-84/#c84)的真空和质量归一。

<span id="c85-proca"></span>

## 从标量真空到三个矢量偏振

取标量电动力学
<span id="eq:c85-model"></span>

$$
\begin{aligned}
\mathcal L&=-(D_\mu\varphi)^\dagger D^\mu\varphi
 -V(\varphi)-\frac14F_{\mu\nu}F^{\mu\nu},\\
D_\mu&=\partial_\mu-igA_\mu,\qquad
V(\varphi)=\frac{\lambda}{4}
 \left(\varphi^\dagger\varphi-\frac{v^2}{2}\right)^2,
\qquad g,v,\lambda>0 .
\end{aligned}
\tag{85.1}
$$

势的最低值在$|\varphi|=v/\sqrt2$处。这与上一节的势有相同的形状，只是加上常数使最低值为零。为了把径向振动和真空圆周上的转动分开，仍写
<span id="eq:c85-polar-potential"></span>

$$
\begin{aligned}
\varphi&=\frac{v+\rho}{\sqrt2}e^{-i\chi/v},\\
V&=\frac{\lambda}{4}
 \left(v\rho+\frac{\rho^2}{2}\right)^2
 =\frac{\lambda v^2}{4}\rho^2
  +\frac{\lambda v}{4}\rho^3+\frac{\lambda}{16}\rho^4 .
\end{aligned}
\tag{85.2}
$$

因此势不含$\chi$。在$v+\rho>0$的局部坐标片内，用上一节的规范变换令$\chi=0$，就得到幺正规范（unitary gauge）。此时协变导数的实部是$\partial_\mu\rho/\sqrt2$，虚部是$-g(v+\rho)A_\mu/\sqrt2$；复共轭相乘时两个交叉项相消，故
<span id="eq:c85-unitary-masses"></span>

$$
\begin{aligned}
-(D_\mu\varphi)^\dagger D^\mu\varphi
 &=-\frac12(\partial\rho)^2
   -\frac12g^2(v+\rho)^2 A_\mu A^\mu,\\
M&=gv,\qquad m_\rho^2=\frac{\lambda v^2}{2},\\
\mathcal L_{\rho A,\mathrm{int}}
 &=-g^2v\rho A_\mu A^\mu
   -\frac12g^2\rho^2 A_\mu A^\mu .
\end{aligned}
\tag{85.3}
$$

这一局部展开确定了后面所有质量和顶角的归一。质量在此均指树级二次项的系数。

先暂时略去相互作用。矢量场的自由拉格朗日量为
<span id="eq:c85-proca-eom"></span>

$$
\begin{aligned}
\mathcal L_{A,0}
 &=-\frac14F_{\mu\nu}F^{\mu\nu}-\frac12M^2A_\mu A^\mu,\\
0&=\partial_\mu F^{\mu\nu}-M^2A^\nu
 =(\partial^2-M^2)A^\nu-\partial^\nu(\partial\cdot A).
\end{aligned}
\tag{85.4}
$$

对第二式取散度，反对称张量$F^{\mu\nu}$的双散度为零，于是$M^2\partial\cdot A=0$。由于$M>0$，将所得约束代回运动方程便有
<span id="eq:c85-proca-constraint"></span>

$$
\partial_\mu A^\mu=0,\qquad
(-\partial^2+M^2)A^\mu=0.
\tag{85.5}
$$

四个分量都满足克莱因—戈登方程，但它们不是四个独立的振子：散度条件除去了一个自由度。

这个约束在正则量子化中也必须保留。用下标$A_0$作为时间分量，动量和哈密顿密度为
<span id="eq:c85-proca-hamiltonian"></span>

$$
\begin{aligned}
\pi^i&=\dot A_i-\partial_iA_0,\qquad \pi^0=0,\\
\mathcal H
 &=\frac12\boldsymbol\pi^2+\frac14F_{ij}F_{ij}
   +\frac12M^2\boldsymbol A^2
   +\pi^i\partial_iA_0-\frac12M^2A_0^2 .
\end{aligned}
\tag{85.6}
$$

时间分量没有独立共轭动量。对空间积分中的$\pi^i\partial_iA_0$分部积分，边界项在所取边界条件下消失；再变分$A_0$，得到$A_0=-\partial_i\pi^i/M^2$。代回之后，
<span id="eq:c85-proca-positive-hamiltonian"></span>

$$
H_{\mathrm{red}}=\int d^3x\left[
\frac12\boldsymbol\pi^2+\frac14F_{ij}F_{ij}
+\frac12M^2\boldsymbol A^2
+\frac{(\partial_i\pi^i)^2}{2M^2}\right].
\tag{85.7}
$$

剩下的三对正则变量具有正定的自由能量。特别地，对一个空间动量为$\boldsymbol k$的实傅里叶模，沿$\boldsymbol k$的部分是
<span id="eq:c85-longitudinal-oscillator"></span>

$$
\begin{aligned}
H_L&=\frac12\frac{E_{\boldsymbol k}^2}{M^2}\pi_L^2
 +\frac12M^2 A_L^2,\qquad
E_{\boldsymbol k}=\sqrt{\boldsymbol k^2+M^2},\\
Q_L&=\frac{M}{E_{\boldsymbol k}}A_L,\qquad
P_L=\frac{E_{\boldsymbol k}}{M}\pi_L,\qquad
H_L=\frac12P_L^2+\frac12E_{\boldsymbol k}^2Q_L^2 .
\end{aligned}
\tag{85.8}
$$

变换中两个比例互为倒数，故保持正则对易关系。这个振子和两个空间横向振子有相同的频率$E_{\boldsymbol k}$；它就是有质量矢量粒子的第三种物理偏振。

固定产生、湮灭分支的相位，将自由场展开为
<span id="eq:c85-vector-modes"></span>

$$
\begin{aligned}
A^\mu(x)&=\sum_{\lambda=-,0,+}\int
 \frac{d^3k}{(2\pi)^3\,2E_{\boldsymbol k}}
 \Bigl[
 \varepsilon_\lambda^{\mu *}(k)a_\lambda(\boldsymbol k)e^{ikx}
 \\
 &\hspace{37mm}
 +\varepsilon_\lambda^\mu(k)a_\lambda^\dagger(\boldsymbol k)e^{-ikx}
 \Bigr],\\
[a_\lambda(\boldsymbol k),a_{\lambda'}^\dagger(\boldsymbol q)]
 &=(2\pi)^3\,2E_{\boldsymbol k}\,
 \delta_{\lambda\lambda'}\delta^3(\boldsymbol k-\boldsymbol q).
\end{aligned}
\tag{85.9}
$$

这里$k^0=E_{\boldsymbol k}$，$kx=-E_{\boldsymbol k}t+\boldsymbol k\cdot\boldsymbol x$。静止系中$k^\mu=(M,0,0,0)$，偏振选择为
<span id="eq:c85-rest-polarizations"></span>

$$
\begin{aligned}
\varepsilon_+(0)&=\frac{(0,1,-i,0)}{\sqrt2},\\
\varepsilon_-(0)&=\frac{(0,1,+i,0)}{\sqrt2},\\
\varepsilon_0(0)&=(0,0,0,1).
\end{aligned}
\tag{85.10}
$$

这组偏振使用固定自旋轴。一般动量下可对这组三矢量作洛伦兹推动；若要用螺旋度基底，再把自旋轴转到$\boldsymbol k$方向。例如沿正$z$方向运动时，
<span id="eq:c85-physical-longitudinal"></span>

$$
k^\mu=(E,0,0,p),\qquad
\varepsilon_0^\mu(k)=\frac{(p,0,0,E)}{M},
\qquad
k\cdot\varepsilon_0=0,\quad
\varepsilon_0^2=1 .
\tag{85.11}
$$

所以“空间纵向”不妨碍四维正交条件。本节的$\varepsilon_-=\varepsilon_+^*$与第60节的相位不同。若$\varepsilon_\lambda\to e^{i\alpha_\lambda}\varepsilon_\lambda$，在本节场展开中须同时取$a_\lambda\to e^{i\alpha_\lambda}a_\lambda$、$a_\lambda^\dagger\to e^{-i\alpha_\lambda}a_\lambda^\dagger$，于是场及散射概率均不变。

在静止系直接相乘，三偏振之和的矩阵是$\operatorname{diag}(0,1,1,1)$，亦即$g^{\mu\nu}+k^\mu k^\nu/M^2$。两边都是洛伦兹张量，对它们作同一个推动便得
<span id="eq:c85-polarization-completeness"></span>

$$
\varepsilon_{\lambda'}\cdot\varepsilon_\lambda^*
=\delta_{\lambda'\lambda},\qquad
\sum_\lambda\varepsilon_\lambda^{\mu *}(k)
\varepsilon_\lambda^\nu(k)
=g^{\mu\nu}+\frac{k^\mu k^\nu}{M^2}.
\tag{85.12}
$$

也可以把$k^\mu/M$加入三个偏振中，组成闵可夫斯基空间的一组完备正交基；类时基矢的负范数正好给出右边的正号。这给出了偏振的归一与完备关系。

场展开的归一还能与正则条件直接核对。由式[（85.12）](#eq:c85-polarization-completeness)的空间和混合分量，
<span id="eq:c85-mode-canonical-check"></span>

$$
\sum_\lambda\varepsilon_\lambda^{i *}
 \left(E_{\boldsymbol k}\varepsilon_\lambda^j
       -k^j\varepsilon_\lambda^0\right)
=E_{\boldsymbol k}\left(\delta^{ij}+\frac{k^ik^j}{M^2}\right)
 -k^j\frac{E_{\boldsymbol k}k^i}{M^2}
=E_{\boldsymbol k}\delta^{ij}.
\tag{85.13}
$$

括号中的组合来自$\pi^j=\dot A^j+\partial_jA^0$。正、负频率两项各给出一半等时delta函数，因此式[（85.9）](#eq:c85-vector-modes)确实产生$[A_i(t,\boldsymbol x),\pi^j(t,\boldsymbol y)]=i\delta_i{}^j\delta^3(\boldsymbol x-\boldsymbol y)$。正则约束由此与产生、湮灭算符方法衔接起来。

<span id="c85-propagator"></span>

## 传播子中的极点与接触项

从自由作用量求传播子，最方便的是直接求二次核的逆。在动量空间，Proca核及其候选逆为
<span id="eq:c85-unitary-propagator"></span>

$$
\begin{aligned}
K^{\mu\nu}(k)&=(k^2+M^2)g^{\mu\nu}-k^\mu k^\nu,\\
\widetilde\Delta_U^{\mu\nu}(k)
&=\frac{g^{\mu\nu}+k^\mu k^\nu/M^2}{k^2+M^2-i0}.
\end{aligned}
\tag{85.14}
$$

先在极点以外验算有理式。由于$K^\mu{}_\alpha k^\alpha=M^2k^\mu$，
<span id="eq:c85-proca-inverse"></span>

$$
K^\mu{}_\alpha
 \left(g^{\alpha\nu}+\frac{k^\alpha k^\nu}{M^2}\right)
=(k^2+M^2)g^{\mu\nu}-k^\mu k^\nu+k^\mu k^\nu
=(k^2+M^2)g^{\mu\nu}.
\tag{85.15}
$$

再按费曼处方取边界值。极点在$k^2=-M^2$，其留数正是三个物理偏振之和。沿既定约定，$\Delta=iG$，图中的内部矢量线实际带$\widetilde\Delta_U/i$。

协变逆核与普通时间排序的$i\langle TA^\mu A^\nu\rangle$并不完全相同：对于受约束的时间分量，两者相差一个局部接触项。可以从已经量子化的模式明确看出差别。记自由标量的传播子为
<span id="eq:c85-scalar-time-kernel"></span>

$$
\Delta_M(t,\boldsymbol x)
=i\int\frac{d^3k}{(2\pi)^3\,2E_{\boldsymbol k}}\,
e^{i\boldsymbol k\cdot\boldsymbol x-iE_{\boldsymbol k}|t|}.
\tag{85.16}
$$

它在$t=0$连续，而时间导数的跃变为
$\partial_t\Delta_M(0^+,\boldsymbol x)
-\partial_t\Delta_M(0^-,\boldsymbol x)=\delta^3(\boldsymbol x)$。
因此再次微分会产生$\delta(t)\delta^3(\boldsymbol x)$。在$t\ne0$处，偏振和可以写成作用于标量核的$g^{\mu\nu}-\partial^\mu\partial^\nu/M^2$；把时间排序完整保留下来则得到
<span id="eq:c85-proca-time-contact"></span>

$$
\begin{aligned}
i\langle0|T A^\mu(x)A^\nu(y)|0\rangle
 &=
 \left(g^{\mu\nu}-\frac{\partial^\mu\partial^\nu}{M^2}\right)
 \Delta_M(x-y)
 +\frac{n^\mu n^\nu}{M^2}\delta^4(x-y),\\
n^\mu&=(1,0,0,0).
\end{aligned}
\tag{85.17}
$$

右边第一项的傅里叶变换就是式[（85.14）](#eq:c85-unitary-propagator)。例如取$\boldsymbol k=0$，场展开中所有$\varepsilon^0$为零，普通时间排序的$00$分量也为零；协变逆核的该分量却是$-1/M^2$，恰由上式的接触项抵消。时间微分产生的局部项由此将普通时间排序与协变逆核联系起来。

正则路径积分与协变逆核的关系也可由高斯积分直接建立。从$H_{\rm red}$出发，将其中最后一项写成

$$
\exp\left[-i\int d^4x\,\frac{(\partial_i\pi^i)^2}{2M^2}\right]
\ \propto\
\int\mathcal DA_0\,
\exp\left[i\int d^4x
\left(\frac12M^2 A_0^2+A_0\partial_i\pi^i\right)\right].
$$

右边完成平方后，平方中心为$A_0=-\partial_i\pi^i/M^2$，余项就是左边的指数。再对$A_0\partial_i\pi^i$分部积分，$\pi^i$的指数成为

$$
-\frac12\boldsymbol\pi^2+\pi^i(\dot A_i-\partial_iA_0)
=-\frac12\{\pi^i-(\dot A_i-\partial_iA_0)\}^2
 +\frac12(\dot A_i-\partial_iA_0)^2 .
$$

积掉平方项就恢复式[（85.4）](#eq:c85-proca-eom)的Proca拉格朗日量。引入的$A_0$除了正则约束值，还有无导数的高斯涨落；其$i$乘二点为$-\delta^4/M^2$，恰是从普通时间序到协变核所减去的接触项。路径积分的费曼规则因而使用协变时间排序$T^*$及式[（85.14）](#eq:c85-unitary-propagator)。$\rho^3,\rho^4,\rho A^2,\rho^2A^2$的系数已由式[（85.2）](#eq:c85-polar-potential)和[（85.3）](#eq:c85-unitary-masses)确定，足以进行树级计算。

<span id="c85-unitary-measure"></span>

## 极坐标测度为何留下鬼场

圈图还涉及场积分的测度。幺正规范把$\chi$设为零以前，原来积分的变量是$\operatorname{Re}\varphi$和$\operatorname{Im}\varphi$。在每个时空点写$r=v+\rho$，局部变量代换为
<span id="eq:c85-polar-jacobian"></span>

$$
\begin{aligned}
\operatorname{Re}\varphi&=\frac{r}{\sqrt2}\cos\frac{\chi}{v},
&\operatorname{Im}\varphi&=-\frac{r}{\sqrt2}\sin\frac{\chi}{v},\\
\det\frac{\partial(\operatorname{Re}\varphi,\operatorname{Im}\varphi)}
 {\partial(\rho,\chi)}
 &=
\det\begin{pmatrix}
 \cos(\chi/v)/\sqrt2&-r\sin(\chi/v)/(\sqrt2v)\\
 -\sin(\chi/v)/\sqrt2&-r\cos(\chi/v)/(\sqrt2v)
\end{pmatrix}
=-\frac{r}{2v}.
\end{aligned}
\tag{85.18}
$$

在$r>0$的坐标片取绝对值，并把与场无关的常数收入整体归一，便有
<span id="eq:c85-unitary-functional-measure"></span>

$$
\mathcal D\operatorname{Re}\varphi\,\mathcal D\operatorname{Im}\varphi
\ \propto\
\mathcal D\rho\,\mathcal D\chi\,
\prod_x(v+\rho(x)).
\tag{85.19}
$$

规范变换使$\delta_\theta\chi=gv\theta$，所以$\chi=0$的FP行列式只是常数；插入$\prod_x\delta(\chi(x))$并对$\chi$积分之后，径向雅可比仍留在测度中。也可以始终用笛卡儿坐标，直接固定$\operatorname{Im}\varphi=0$；该规范条件的FP因子正比于$v+\rho$，给出同一个结果。两种做法各产生一次这个因子。

将常数$v$提出，径向测度的行列式可写成
<span id="eq:c85-ultralocal-ghost"></span>

$$
\begin{aligned}
J[\rho]&=\det(1+\rho/v),\\
J[\rho]&\ \propto\
\int\mathcal D\bar c\,\mathcal Dc\,
\exp\left[-i m_{\rm gh}^2
 \int d^4x\,\bar c(1+\rho/v)c\right].
\end{aligned}
\tag{85.20}
$$

这里使用[第44节已求出的复Grassmann 高斯积分](/posts/srednicki-44/#c44-determinant)，核代为$m_{\rm gh}^2(1+\rho/v)$；因子$-i m_{\rm gh}^2$的行列式与场无关，由整体归一消去。$m_{\rm gh}$只是为了方便选取的归一参数。由于没有导数项，鬼场在不同的时空点不传播，动量空间规则为
<span id="eq:c85-unitary-ghost-rules"></span>

$$
\widetilde\Delta_{\rm gh}(k)=\frac{1}{m_{\rm gh}^2},
\qquad
\text{内部鬼线}=\frac{1}{i m_{\rm gh}^2},
\qquad
\rho\bar c c\text{顶角}=-\frac{i m_{\rm gh}^2}{v}.
\tag{85.21}
$$

鬼场只与$\rho$相连，没有鬼场–矢量场顶角。闭鬼圈还须带Grassmann负号。它们不作为外部物理粒子出现，因而不改变前面的纯物理树图。

行列式的展开把这些圈图的内容表达得更直接：
<span id="eq:c85-measure-loop-expansion"></span>

$$
\begin{aligned}
\log J[\rho]
 &=\delta_{\rm reg}^4(0)\int d^4x\,
 \log(1+\rho/v)\\
 &=\delta_{\rm reg}^4(0)\int d^4x
 \sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n}
 \left(\frac{\rho}{v}\right)^n,\qquad |\rho|<v,\\
\delta_{\rm reg}^4(0)&=\int_{\rm reg}\frac{d^4\ell}{(2\pi)^4}\,1 .
\end{aligned}
\tag{85.22}
$$

写成作用量时，这一贡献为$S_J=-i\log J$，因为$J e^{iS}=e^{i(S-i\log J)}$。每一项对应一个带$n$条外部$\rho$线的鬼圈；顶角和内部线中的$m_{\rm gh}^2$逐一抵消，留下$v^{-n}$和同一个无衰减的圈积分。硬截止给出幂发散，而在维数正规化中，此处无任何尺度的积分按该方案取零。

矢量线也有类似的大动量问题。在远离类光方向、所有分量一同放大的动量区域，式[（85.14）](#eq:c85-unitary-propagator)的$kk/M^2$项使传播子保持$M^{-2}$量级，不像通常的玻色线那样按$k^{-2}$下降。因此增加内部线并不必然改善幺正规范图的表面收敛性，带许多外线的图也可能发散。这个现象使逐图的重整化分析很不方便。要恢复适合圈计算的幂次计数，我们转回线性标量变量，并在规范固定中消去矢量与角向振动之间的混合。

<span id="c85-rxi-fixing"></span>

## 用规范固定消去混合项

现在采用笛卡儿变量：
<span id="eq:c85-cartesian-fields"></span>

$$
\begin{aligned}
\varphi&=\frac{v+h+ib}{\sqrt2},\\
h&=(v+\rho)\cos(\chi/v)-v,\qquad
b=-(v+\rho)\sin(\chi/v).
\end{aligned}
\tag{85.23}
$$

真空附近$h=\rho+\cdots$、$b=-\chi+\cdots$；负号来自原来极坐标指数的选择。由于
$\varphi^\dagger\varphi-v^2/2=vh+(h^2+b^2)/2$，势成为
<span id="eq:c85-cartesian-potential"></span>

$$
V=\frac{\lambda v^2}{4}h^2
 +\frac{\lambda v}{4}h(h^2+b^2)
 +\frac{\lambda}{16}(h^2+b^2)^2 .
\tag{85.24}
$$

此时$b$在势的二次部分仍无质量。将$\partial_\mu-igA_\mu$作用于复场，并分别收集实、虚部，得到
<span id="eq:c85-cartesian-covariant-derivative"></span>

$$
\begin{aligned}
D_\mu\varphi
 &=\frac1{\sqrt2}
 \left[\partial_\mu h+gbA_\mu
       +i\{\partial_\mu b-g(v+h)A_\mu\}\right],\\
-(D_\mu\varphi)^\dagger D^\mu\varphi
 &=-\frac12(\partial h+gbA)^2
   -\frac12\{\partial b-g(v+h)A\}^2 .
\end{aligned}
\tag{85.25}
$$

第一平方的交叉项为$-gbA^\mu\partial_\mu h$，第二平方的交叉项为$g(v+h)A^\mu\partial_\mu b$。把含$v$的部分与真正的相互作用分开，便有
<span id="eq:c85-cartesian-kinetic-expanded"></span>

$$
\begin{aligned}
\mathcal L_{\varphi,\mathrm{kin}}
 &=-\frac12(\partial h)^2-\frac12(\partial b)^2
   -\frac12M^2 A^2+gvA^\mu\partial_\mu b\\
 &\quad+gA^\mu(h\partial_\mu b-b\partial_\mu h)
   -g^2vhA^2-\frac12g^2(h^2+b^2)A^2 .
\end{aligned}
\tag{85.26}
$$

其中$gvA\cdot\partial b$仍是二次项，若直接求传播子就必须同时逆转$A,b$的混合矩阵。第二平方中的$-g^2(v+h)^2A^2/2$给出$hA^2$项的系数$-g^2v$，与幺正规范的$\rho A^2$项一致。

对未破缺的阿贝尔理论，通常取$G=\partial\cdot A$，加入$-G^2/(2\xi)$。现在希望规范固定再产生一个与$gvA\cdot\partial b$相反的交叉项，因此选
<span id="eq:c85-rxi-gauge-function"></span>

$$
G_\xi=\partial_\mu A^\mu-\xi gvb,\qquad
\mathcal L_{\rm gf}=-\frac{G_\xi^2}{2\xi},
\qquad 0<\xi<\infty .
\tag{85.27}
$$

这里$\xi$无量纲；两个相减的量都具有质量维2。将平方展开，
<span id="eq:c85-gauge-fixing-expanded"></span>

$$
\mathcal L_{\rm gf}
=-\frac{(\partial\cdot A)^2}{2\xi}
 +gvb\,\partial\cdot A-\frac12\xi M^2 b^2 .
\tag{85.28}
$$

对中间项的时空积分分部积分，$\int b\,\partial\cdot A=-\int A\cdot\partial b$，于是混合项恰好消去。同时$b$获得质量平方$\xi M^2$。这正是规范函数中选择$-\xi gvb$的目的。当$v=0$时，它又回到普通洛伦茨规范。

第一项还可改写为$-\partial_\mu A_\nu\partial^\nu A^\mu/(2\xi)$。这个等式是在作用量的积分内成立的。去掉共同系数$-1/(2\xi)$后，两种导数乘积满足

$$
\int d^4x\,(\partial\cdot A)^2
=-\int d^4x\,A^\mu\partial_\mu\partial_\nu A^\nu
=\int d^4x\,\partial_\mu A_\nu\partial^\nu A^\mu .
$$

以下推导均取场在边界衰减，或取容许这些分部积分的相容边界条件。

规范固定还需要FP行列式。普通无穷小变换为
<span id="eq:c85-cartesian-gauge-variation"></span>

$$
\begin{aligned}
\delta_\theta A_\mu&=-\partial_\mu\theta,\qquad
\delta_\theta\varphi=-ig\theta\varphi,\\
\delta_\theta h&=g\theta b,\qquad
\delta_\theta b=-g\theta(v+h).
\end{aligned}
\tag{85.29}
$$

后两式由$\delta h+i\delta b=-ig\theta(v+h+ib)$的实、虚部直接得到。代入$G_\xi$，有
<span id="eq:c85-fp-operator"></span>

$$
\begin{aligned}
\delta_\theta G_\xi(x)
 &=\{-\partial^2+\xi g^2v(v+h(x))\}\theta(x),\\
\mathcal M_{\rm FP}(x,y)
 &\equiv\frac{\delta G_\xi(x)}{\delta\theta(y)}
 =\{-\partial_x^2+\xi g^2v(v+h(x))\}\delta^4(x-y).
\end{aligned}
\tag{85.30}
$$

因此鬼场拉格朗日量为
<span id="eq:c85-rxi-ghost-lagrangian"></span>

$$
\begin{aligned}
\mathcal L_{\rm gh}
 &=-\bar c\,\{-\partial^2+\xi g^2v(v+h)\}c\\
 &=-\partial_\mu\bar c\,\partial^\mu c
   -\xi M^2\bar c c-\xi g^2vh\,\bar c c .
\end{aligned}
\tag{85.31}
$$

从第一行到第二行只作普通时空分部积分，始终保持$\bar c$在$c$前面，没有交换两个Grassmann变量。这里鬼场与$b$有相同的质量平方$\xi M^2$，并且与$h$相互作用。阿贝尔群并不保证鬼场总是自由的：在未破缺理论中，$G=\partial\cdot A$的变分给出$\delta G/\delta\theta=-\partial^2$，不含场；现在$G_\xi$含$b$，而$b$的变换又含$h$，于是产生了最后一个顶角。

FP构造用于所选真空附近的局部微扰积分。自由算符为$-\partial^2+\xi M^2$，按指定边界值求逆；含$h$的项再作为相互作用展开。这样便完成了规范固定，同时使$A,h,b,c,\bar c$的自由二次部分互不混合。

<span id="c85-rxi-propagator"></span>

## 把矢量二次核分成两个投影

将矢量动能及规范固定项分部积分，得到坐标空间二次核：
<span id="eq:c85-rxi-coordinate-kernel"></span>

$$
\mathcal L_{A,0}
=-\frac12 A_\mu
\left[g^{\mu\nu}(-\partial^2+M^2)
 +(1-\xi^{-1})\partial^\mu\partial^\nu\right]A_\nu .
\tag{85.32}
$$

傅里叶变换使每个$\partial^\mu$变为$ik^\mu$，两个微分的乘积因而给出$-k^\mu k^\nu$。相应的动量核是
<span id="eq:c85-rxi-momentum-kernel"></span>

$$
\begin{aligned}
S_{A,0}&=-\frac12\int\frac{d^4k}{(2\pi)^4}
 \widetilde A_\mu(-k)K_\xi^{\mu\nu}(k)\widetilde A_\nu(k),\\
K_\xi^{\mu\nu}(k)&=(k^2+M^2)g^{\mu\nu}
 -(1-\xi^{-1})k^\mu k^\nu .
\end{aligned}
\tag{85.33}
$$

两个$i$的乘积固定了$k^\mu k^\nu$项前的负号；接下来直接验算逆矩阵。

先取$k^2\ne0$，定义混合指标的两个投影
<span id="eq:c85-lorentz-projectors"></span>

$$
(P_L)^\mu{}_\nu=\frac{k^\mu k_\nu}{k^2},\qquad
(P_T)^\mu{}_\nu=\delta^\mu{}_\nu-(P_L)^\mu{}_\nu .
\tag{85.34}
$$

由于$k_\alpha k^\alpha=k^2$，有$(P_L^2)^\mu{}_\nu=k^\mu k_\nu/k^2=P_L^\mu{}_\nu$。再用$P_T=I-P_L$，便得$P_T^2=P_T$、$P_TP_L=P_LP_T=0$和$P_T+P_L=I$。因此核可写为
<span id="eq:c85-rxi-projector-decomposition"></span>

$$
\begin{aligned}
K_\xi
 &=(k^2+M^2)P_T+
 \{k^2+M^2-(1-\xi^{-1})k^2\}P_L\\
 &=(k^2+M^2)P_T+
 \xi^{-1}(k^2+\xi M^2)P_L .
\end{aligned}
\tag{85.35}
$$

两个子空间不混合，故只须分别把各自的本征值取倒数。乘回核时，两个交叉项都为零，同一投影的系数均为一；这就给出
<span id="eq:c85-rxi-propagator-projectors"></span>

$$
\widetilde\Delta_\xi^{\mu\nu}(k)
=\frac{P_T^{\mu\nu}(k)}{k^2+M^2-i0}
 +\frac{\xi P_L^{\mu\nu}(k)}{k^2+\xi M^2-i0}.
\tag{85.36}
$$

两个分母中的$i0$表示相应的因果边界值。若在移去调节之前逐项验算，可对原核统一作$K_\xi\mapsto K_\xi-i\epsilon I$，此时第二个分母是$k^2+\xi M^2-i\xi\epsilon$；固定正$\xi$后，它给出同一费曼边界值。

投影式中出现了$1/k^2$，但完整传播子并没有额外的无质量极点。令$a=k^2+M^2-i\epsilon$、$b=k^2+\xi M^2-i\xi\epsilon$，有$\xi a-b=(\xi-1)k^2$，于是
<span id="eq:c85-rxi-propagator-combined"></span>

$$
\begin{aligned}
\frac{P_T^{\mu\nu}}a+\frac{\xi P_L^{\mu\nu}}b
 &=\frac{g^{\mu\nu}}a+
 \frac{k^\mu k^\nu}{k^2}\left(\frac{\xi}{b}-\frac1a\right)\\
 &=\frac{g^{\mu\nu}+(\xi-1)k^\mu k^\nu/b}{a}.
\end{aligned}
\tag{85.37}
$$

先合并再取$k^2\to0$，结果有限；前面的投影只是在该点不能单独定义。这个形式也显示，固定有限$\xi$时，传播子的所有分量在一般欧几里得大动量方向上都按$k^{-2}$下降。鬼场和两个标量也具有通常的二阶动能，幺正规范中无衰减内部线造成的困难由此消除。

当$\xi=1$时，两个投影重新合成度规，得到费曼规范的传播子：
<span id="eq:c85-feynman-gauge-propagator"></span>

$$
\widetilde\Delta_{\xi=1}^{\mu\nu}(k)
=\frac{g^{\mu\nu}}{k^2+M^2-i0}.
\tag{85.38}
$$

这使圈图的张量代数最简便。若保留一般$\xi$，则可以在最终物理幅中检查所有$\xi$项是否相消。

对于$\xi\ne1$，物理质量极点的留数为
$P_T^{\mu\nu}|_{k^2=-M^2}=g^{\mu\nu}+k^\mu k^\nu/M^2$，
秩为三，正是式[（85.12）](#eq:c85-polarization-completeness)。另一极点属于沿四动量$k^\mu$的$P_L$分量，其质量平方为$\xi M^2$。这里所说的“纵向分量”是指沿四动量的投影。式[（85.11）](#eq:c85-physical-longitudinal)的物理螺旋度零态满足$k\cdot\varepsilon_0=0$，属于$P_T$，仍然可以作为外态。当$\xi=1$时两个极点重合，必须依靠物理态条件来区分它们，不能只凭分母判断。

其余自由线由各自二次项给出：
<span id="eq:c85-rxi-scalar-ghost-lines"></span>

$$
\begin{aligned}
m_h^2&=\frac{\lambda v^2}{2},&
\widetilde\Delta_h(k)&=\frac1{k^2+m_h^2-i0},\\
m_b^2&=m_c^2=\xi M^2,&
\widetilde\Delta_b(k)&=\widetilde\Delta_c(k)
=\frac1{k^2+\xi M^2-i0}.
\end{aligned}
\tag{85.39}
$$

这些仍是$\Delta$，内部线都须再除以$i$。外部矢量取三个物理偏振，$b,c,\bar c$及沿$k^\mu$的矢量分量不取作物理入射、出射粒子。物理态的这一限制与规范参数独立性由BRST条件联系起来，下面在给出顶角之后说明。

<span id="c85-vertices-brst"></span>

## 相互作用与物理态

把式[（85.24）](#eq:c85-cartesian-potential)、[（85.26）](#eq:c85-cartesian-kinetic-expanded)和[（85.31）](#eq:c85-rxi-ghost-lagrangian)中三次以上的项合在一起，相互作用密度为
<span id="eq:c85-all-interactions"></span>

$$
\begin{aligned}
\mathcal L_1
 &=-\frac{\lambda v}{4}h(h^2+b^2)
   -\frac{\lambda}{16}(h^2+b^2)^2\\
 &\quad+gA^\mu(h\partial_\mu b-b\partial_\mu h)
   -g^2vhA_\mu A^\mu\\
 &\quad-\frac12g^2(h^2+b^2)A_\mu A^\mu
   -\xi g^2vh\,\bar c c .
\end{aligned}
\tag{85.40}
$$

$hA^2$中的$g^2$来自前面的协变动能平方。其余系数的阶乘可以逐项从相同场的排列得到：$-\lambda vh^3/4$有$3!$种收缩，$-\lambda vhb^2/4$只有两个$b$可以交换，分别给出$-3i\lambda v/2$和$-i\lambda v/2$。四次混合项的系数为$-\lambda h^2b^2/8$，再乘$2!2!$；两个同类四次项则各乘$4!$。

对矢量项，两个$A$给出因子$2!$及$g_{\mu\nu}$，若还含两个相同标量，再乘一个$2!$。微分顶角取全部动量流入，$e^{ikx}$使$\partial_\mu$给出$ik_\mu$；连同作用量展开的$i$，有$i\,g\,i(k_b-k_h)_\mu=g(k_h-k_b)_\mu$。鬼与反鬼彼此不同，固定$\bar c c$次序后没有相同粒子的阶乘。所有顶角于是为：

| 入射场                                 | 顶角因子              |
| -------------------------------------- | --------------------- |
| $h,h,h$                                | $-3i\lambda v/2$      |
| $h,b,b$                                | $-i\lambda v/2$       |
| $h,h,h,h$ 或 $b,b,b,b$                 | $-3i\lambda/2$        |
| $h,h,b,b$                              | $-i\lambda/2$         |
| $h,A^\mu,A^\nu$                        | $-2ig^2v\,g_{\mu\nu}$ |
| $h,h,A^\mu,A^\nu$ 或 $b,b,A^\mu,A^\nu$ | $-2ig^2g_{\mu\nu}$    |
| $A^\mu,h(k_h),b(k_b)$                  | $g(k_h-k_b)_\mu$      |
| $h,\bar c,c$                           | $-i\xi g^2v$          |

三次顶角具有质量维1，四次顶角无量纲，微分顶角的质量维由一个外动量提供。交换两个同类外场不改变相应顶角；$Ahb$中的动量差按表中$h,b$的标签定义。

在幺正规范中，将表中的$h$换为$\rho$，保留$\rho^3,\rho^4,\rho A^2,\rho^2A^2$四种物理顶角，系数完全相同；鬼场顶角则用式[（85.21）](#eq:c85-unitary-ghost-rules)。因此前面得到的幺正规范树规则也已在表中逐项求出。

不同$\xi$给出同一物理散射，可以用[第74节的BRST物理态条件](/posts/srednicki-74/#c74)证明。以奇微分$s$表示BRST变换：
<span id="eq:c85-brst-transformations"></span>

$$
\begin{aligned}
sA_\mu&=\partial_\mu c,& sc&=0,&s\bar c&=B,&sB&=0,\\
sh&=-gcb,&sb&=gc(v+h).
\end{aligned}
\tag{85.41}
$$

这里$B$是辅助场。相对于式[（85.29）](#eq:c85-cartesian-gauge-variation)，规范参数替换为$\theta=-c$。反对易的$c$保证$s^2=0$：例如$s^2h=g c\,sb=g^2c^2(v+h)=0$，$s^2b=-g c\,sh=g^2c^2b=0$。规范函数的变分则是$sG_\xi=-\mathcal M_{\rm FP}c$。

选择奇泛函
<span id="eq:c85-gauge-fermion"></span>

$$
\Psi_\xi=\int d^4x\,\bar c
\left(-G_\xi+\frac{\xi}{2}B\right).
\tag{85.42}
$$

$s$越过奇变量$\bar c$时给出负号，故
<span id="eq:c85-brst-exact-fixing"></span>

$$
\begin{aligned}
s\Psi_\xi
 &=\int d^4x\left[
 -BG_\xi+\frac{\xi}{2}B^2+\bar c\,sG_\xi\right]\\
 &=\int d^4x\left[
 -BG_\xi+\frac{\xi}{2}B^2-\bar c\mathcal M_{\rm FP}c\right].
\end{aligned}
\tag{85.43}
$$

辅助场的方程为$B=G_\xi/\xi$，代回前两项得到$-G_\xi^2/(2\xi)$，恰好还原本节的规范固定与鬼场作用量。这样，改变$\xi$只改变一个BRST恰当项（BRST-exact term）。

在保持BRST的调节及重整化下，且没有规范反常时，路径积分作BRST变量代换给出$\langle sX\rangle=0$。取不显含$\xi$的偶观测量$\mathcal O$，满足$s\mathcal O=0$；对归一化期望求导，分母的导数扣掉真空断开部分，于是
<span id="eq:c85-physical-xi-independence"></span>

$$
\begin{aligned}
\partial_\xi\langle\mathcal O\rangle
 &=i\left\langle
 \mathcal O\,s(\partial_\xi\Psi_\xi)\right\rangle_{\rm conn}\\
 &=i\left\langle
 s\{\mathcal O\,\partial_\xi\Psi_\xi\}\right\rangle_{\rm conn}
 =0 .
\end{aligned}
\tag{85.44}
$$

第二行用到了$s\mathcal O=0$和$\mathcal O$的偶性。散射情形按第74节将入出态取为BRST上同调类，插入的恰当项在物理矩阵元中消失；相应的外腿极点留数及LSZ因子也须一并处理。这就是保持一般$\xi$可以检查物理幅的理由。

物理极点还可以直接用规范不变的局域算符提取。标量密度和带一个矢量指标的流分别给出
<span id="eq:c85-gauge-invariant-interpolators"></span>

$$
\begin{aligned}
\mathcal O_h
&=\frac{\varphi^\dagger\varphi-v^2/2}{v}
 =h+\frac{h^2+b^2}{2v},\\
\mathcal O_\mu
&=\frac{i}{gv^2}
 \left[\varphi^\dagger D_\mu\varphi
       -(D_\mu\varphi)^\dagger\varphi\right]\\
&=\frac{gA_\mu[(v+h)^2+b^2]-(v+h)\partial_\mu b
                  +b\partial_\mu h}{gv^2}\\
&=A_\mu-\frac{\partial_\mu b}{M}+O(\text{二次场}).
\end{aligned}
\tag{85.50}
$$

协变导数与$\varphi$同相变换，故两个双线性中的相位各自消去。在自由BRST变换中，$sA_\mu=\partial_\mu c$、$sb=Mc$也使最后一行的两个变分相消。将矢量插入与满足$k\cdot\varepsilon=0$的偏振收缩，导数$b$项给零，留下的三个偏振包括物理的螺旋度零态。

在树级二点函数中，只需保留插入算符的线性部分。$A,b$的自由混合传播子为零；两个$b$导数分别作用于两个端点，傅里叶变换给$(ik^\mu)(-ik^\nu)=k^\mu k^\nu$。使用协变时间排序，得到
<span id="eq:c85-invariant-vector-pole"></span>

$$
\begin{aligned}
\widetilde\Delta_{\mathcal O}^{(0)\mu\nu}(k)
&\equiv i\langle T^*\mathcal O^\mu\mathcal O^\nu\rangle_k^{(0)}\\
&=\widetilde\Delta_\xi^{\mu\nu}(k)
 +\frac{k^\mu k^\nu}{M^2(k^2+\xi M^2-i0)}\\
&=\frac{g^{\mu\nu}+k^\mu k^\nu/M^2}
        {k^2+M^2-i0}.
\end{aligned}
\tag{85.51}
$$

最后一步将式[（85.36）](#eq:c85-rxi-propagator-projectors)中的纵向系数与$b$项合并；$k^2=-\xi M^2$的极点相消，只剩三个物理偏振的极点。对稳定的径向标量一粒子态，$\mathcal O_h$在线性阶与$h$有相同的极点耦合。$b$、鬼场及沿四动量的规范分量则属于BRST非物理部分。这里使用BRST不变真空及相容边界条件。

<span id="c85-xi-infinity"></span>

## 幺正规范怎样从大规范参数极限恢复

现在令规范参数增大，考察$R_\xi$规则与幺正规范的关系。将式[（85.37）](#eq:c85-rxi-propagator-combined)与Proca传播子相减，先在极点以外计算有理式：
<span id="eq:c85-unitary-limit-propagator"></span>

$$
\begin{aligned}
\widetilde\Delta_\xi^{\mu\nu}
-\widetilde\Delta_U^{\mu\nu}
 &=\frac{k^\mu k^\nu}{k^2+M^2}
 \left[\frac{\xi-1}{k^2+\xi M^2}-\frac1{M^2}\right]\\
 &=-\frac{k^\mu k^\nu}{M^2(k^2+\xi M^2)}
 \ \longrightarrow\ 0\qquad(\xi\to\infty).
\end{aligned}
\tag{85.45}
$$

所以固定动量下的矢量线回到幺正规范；相应的因果边界值按同一处方取得。$b$的传播子$1/(k^2+\xi M^2)$趋于零，而它的相互作用系数没有$\xi$的正幂，看起来可以将它消去。

鬼场需要另作计算。它的质量平方也是$\xi M^2$，但$h\bar c c$顶角为$-i\xi M^2/v$。沿一个闭鬼圈，将每个顶角和一条内部线配起来，有
<span id="eq:c85-heavy-ghost-cancellation"></span>

$$
\frac{-i\xi M^2/v}{i(k^2+\xi M^2)}
=-\frac1v\frac{\xi M^2}{k^2+\xi M^2}
\ \longrightarrow\ -\frac1v .
\tag{85.46}
$$

因此$n$个顶角与$n$条线中的质量因子逐一抵消，鬼圈并不趋于零。取$m_{\rm gh}^2=\xi M^2$，它恰好回到式[（85.21）](#eq:c85-unitary-ghost-rules)的无导数鬼场规则。

为了更清楚地看出留下来的是什么，可以先保持有限的紫外调节，将场积分看成有限维积分。在固定的有界标量背景上，
<span id="eq:c85-ghost-determinant-limit"></span>

$$
\begin{aligned}
\mathcal M_{\rm FP}
 &=\xi M^2\left(1+\frac h v
                   -\frac{\partial^2}{\xi M^2}\right),\\
\frac{\det\mathcal M_{\rm FP}}{\det(\xi M^2)}
 &\ \longrightarrow\ \det(1+h/v).
\end{aligned}
\tag{85.47}
$$

有限调节使微分矩阵的本征值保持有界，故先取大$\xi$时，最后一项逐矩阵元趋于零，行列式的连续性给出第二行。分母与场无关，已经由归一化积分消去。这个结果正是幺正规范的径向测度。

同一极限也可以在鬼场作用量中逐项实现。引入任意固定质量$m_{\rm aux}>0$，作常数变量代换
<span id="eq:c85-ghost-rescaling-limit"></span>

$$
\begin{aligned}
c&=\frac{m_{\rm aux}}{\sqrt{\xi}M}\,\widehat c,\qquad
\bar c=\frac{m_{\rm aux}}{\sqrt{\xi}M}\,\widehat{\bar c},\\
\mathcal L_{\rm gh}
 &=-\frac{m_{\rm aux}^2}{\xi M^2}
    \partial_\mu\widehat{\bar c}\,\partial^\mu\widehat c
   -m_{\rm aux}^2\widehat{\bar c}(1+h/v)\widehat c\\
 &\ \longrightarrow\
   -m_{\rm aux}^2\widehat{\bar c}(1+h/v)\widehat c .
\end{aligned}
\tag{85.48}
$$

Grassmann测度的雅可比是比例因子的倒数，但仍与场无关，归一化后不影响结果。最后一行就是幺正规范的鬼场作用量，任意的归一质量仍然保留。

对$b$则作$b=\beta/\sqrt\xi$。其质量项与其他项分别变成
<span id="eq:c85-goldstone-decoupling"></span>

$$
-\frac12\xi M^2b^2=-\frac12M^2\beta^2,\qquad
(\partial b)^2=O(\xi^{-1}),\qquad
h b^2,\ h^2b^2,\ A^2b^2=O(\xi^{-1}).
\tag{85.49}
$$

$Ah\partial b-Ab\partial h$中的每项为$O(\xi^{-1/2})$，$b^4$为$O(\xi^{-2})$。因此在有限调节下、对固定背景取此局部微扰极限，$\beta$只留下与其他场无关的高斯积分，测度中的常数比例也由归一化消去。剩余标量满足$b=0$，在$v+h>0$的片内就是$h=\rho$。矢量线、标量作用量和鬼行列式由此同时恢复为幺正规范，完成了传播子层面之外的测度比较。

固定有限$\xi$后让圈动量增大，式[（85.37）](#eq:c85-rxi-propagator-combined)仍按$k^{-2}$下降；先令$\xi\to\infty$则得到不衰减的Proca分子。两种近似在$|k^2|\sim\xi M^2$的区域相遇，大$\xi$极限对全部圈动量不一致。所以上述比较先保留有限紫外调节；去掉调节时，测度与局部项也参与匹配。实际圈图通常在有限$\xi$完成，$\xi=1$尤其方便。

下一节将把这一构造推广到非阿贝尔群，处理多个破缺方向及其在质量本征基中的混合。

---

[← 第 84 节](/posts/srednicki-84/) · [章节地图](/srednicki/) · [第 86 节 →](/posts/srednicki-86/)
