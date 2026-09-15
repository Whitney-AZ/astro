---
title: 'Srednicki §28 重整化群'
date: 2026-09-14
category: 笔记
tags: [物理, 量子场论, Srednicki]
series: 'Srednicki QFT'
srednickiSections: [28]
hideFromHome: true
draft: false
---

<span id="c28"></span>

上一节要求物理质量和散射截面不随$\mu$改变，由此求出了$m$和$\alpha$的跑动。这个方法直接联系可观测量，但若每次都先完成整套散射计算，许多与尺度变化无关的有限部分也要一起求出。本节从同一理论的裸参数保持不变出发，直接利用反项的极点得到跑动方程，并进一步考察关联函数怎样随场的归一化改变。这些描述参数及关联函数尺度变化的方程，统称为重整化群方程（renormalization group equations）。反项和尺度方程都按微扰阶数展开，下面逐阶比较它们的系数。

<span id="c28-bare"></span>

## 同一个拉格朗日量的两种写法

要把改变尺度与保持理论不变这两件事联系起来，先比较拉格朗日量的两种参数化。在$d=6-\epsilon$维，用重整化量和裸量分别写为

<span id="eq:c28-two-lagrangians"></span>

$$
\begin{aligned}
\mathcal L
&=-\frac12Z_\varphi(\partial\varphi)^2
-\frac12Z_m m^2\varphi^2
+\frac16Z_g g\widetilde\mu^{\epsilon/2}\varphi^3+Y\varphi,\\
\mathcal L
&=-\frac12(\partial\varphi_0)^2
-\frac12m_0^2\varphi_0^2+\frac16g_0\varphi_0^3+Y_0\varphi_0.
\end{aligned}
\tag{28.1}
$$

两种写法表示同一个拉格朗日量，因此各个场单项式的系数必须对应。先从动能项确定$\varphi_0=\sqrt{Z_\varphi}\varphi$，再把这一关系代入其余各项，比较$\varphi^2,\varphi^3,\varphi$的系数，得到

<span id="eq:c28-bare-relations"></span>

$$
\begin{gathered}
m_0^2Z_\varphi=Z_m m^2,\qquad
g_0Z_\varphi^{3/2}=Z_g g\widetilde\mu^{\epsilon/2},\qquad
Y_0\sqrt{Z_\varphi}=Y,\\
m_0=Z_\varphi^{-1/2}Z_m^{1/2}m,\qquad
g_0=Z_\varphi^{-3/2}Z_g g\widetilde\mu^{\epsilon/2},\qquad
Y_0=Z_\varphi^{-1/2}Y.
\end{gathered}
\tag{28.2}
$$

这里的质量平方根取正质量分支。$\varphi^3$中的三个$\sqrt{Z_\varphi}$给出$3/2$次幂，线性项则只有一个场因子；各裸参数中相应的场重整化幂次，都由这些单项式直接决定。$Y$继续按前面的无蝌蚪条件选择，因此在线性项的两种写法中也要同时保留。

重整化群导数所比较的是同一个理论：改变减除尺度时，固定裸场、全部裸参数和外部动量，允许重整化场及参数随之变化。于是式[（28.1）](#eq:c28-two-lagrangians)的第二行保持不变，第一行则通过系数与场归一化的共同变化表示同一内容。这也解释了上一节为什么要求物理量的显式尺度依赖与参数跑动相抵消。这里$g$无量纲，而$[g_0]=\epsilon/2$；$\mu$和$\widetilde\mu$只差固定常数，求对数导数时两者给出相同结果。

<span id="c28-beta"></span>

## 反项的极点怎样决定耦合变化

在$\overline{\mathrm{MS}}$中，反项只减去维数调节的极点，场和参数的重整化因子因而具有如下形式：

<span id="eq:c28-pure-poles"></span>

$$
Z_\varphi=1+\sum_{n\ge1}\frac{a_n(\alpha)}{\epsilon^n},\qquad
Z_m=1+\sum_{n\ge1}\frac{b_n(\alpha)}{\epsilon^n},\qquad
Z_g=1+\sum_{n\ge1}\frac{c_n(\alpha)}{\epsilon^n}.
\tag{28.3}
$$

每个极点系数又可以按$\alpha$展开为形式泰勒级数；在固定圈阶，只出现有限多个极点。已有的一圈计算给出了简单极点：

<span id="eq:c28-one-loop-poles"></span>

$$
a_1=-\frac{\alpha}{6}+O(\alpha^2),\qquad
b_1=-\alpha+O(\alpha^2),\qquad
c_1=-\alpha+O(\alpha^2).
\tag{28.4}
$$

由于一圈只有简单极点，$n\ge2$的系数至少从$O(\alpha^2)$开始。这里的$n$数的是极点次数；同一个简单极点系数本身仍可包含多个圈阶的信息。

耦合的裸量关系包含场因子和顶角因子的乘积。先将裸耦合平方，再用对数把这一乘积化为和，定义

<span id="eq:c28-bare-alpha"></span>

$$
\alpha_0=\frac{g_0^2}{(4\pi)^3}
=\widetilde\mu^\epsilon\alpha\,e^{G(\alpha,\epsilon)},\qquad
G=\ln(Z_g^2Z_\varphi^{-3})
=\sum_{n\ge1}\frac{G_n(\alpha)}{\epsilon^n}.
\tag{28.5}
$$

其中$\alpha_0$有质量维数$\epsilon$，而$\alpha$无量纲。取对数后，$G$仍保持纯极点结构：在$\ln(1+u)=u-u^2/2+\cdots$中，每个$u$都至少含有$\epsilon^{-1}$，所以$u^2$从二重极点开始，更高次项也只能产生更高极点。简单极点因此完全由线性项决定。例如，对场因子和耦合因子分别展开，有

<span id="eq:c28-log-simple-pole"></span>

$$
\ln Z_\varphi=\frac{a_1}{\epsilon}
+\frac{a_2-a_1^2/2}{\epsilon^2}+\cdots,\qquad
G_1=2c_1-3a_1=-\frac32\alpha+O(\alpha^2).
\tag{28.6}
$$

二重极点中的$1/2$正来自对数展开的二次项。把乘积化为和之后，裸耦合不变的条件就可以直接转化为尺度导数关系。

记$B_\epsilon=d\alpha/d\ln\mu$，对$\ln\alpha_0=G+\ln\alpha+\epsilon\ln\widetilde\mu$求导，并保持裸量不变，得到

<span id="eq:c28-bare-chain-rule"></span>

$$
0=\left(\partial_\alpha G+\frac1\alpha\right)B_\epsilon+\epsilon,
\qquad
0=\left(1+\alpha\sum_{n\ge1}\frac{G_n'}{\epsilon^n}\right)B_\epsilon
+\epsilon\alpha.
\tag{28.7}
$$

为解出$B_\epsilon$，按耦合逐阶展开$-\epsilon\alpha(1+\alpha\partial_\alpha G)^{-1}$。分母修正只含$\epsilon$的负幂，因此除树项$-\epsilon\alpha$外，其余各项至多到$\epsilon^0$。重整化参数的尺度导数还须在$\epsilon\to0$时逐阶有限，这就要求所有剩余负幂相消，留下

<span id="eq:c28-regulated-beta"></span>

$$
B_\epsilon=-\epsilon\alpha+\beta(\alpha).
\tag{28.8}
$$

这一形式同时利用了纯极点减除和逐阶有限性：前者限制可能出现的调节器幂次，后者使负幂系数为零。

将式[（28.8）](#eq:c28-regulated-beta)代回裸量的导数关系，按有限项和各重极点重新排列，便有

<span id="eq:c28-pole-matching"></span>

$$
0=\beta-\alpha^2G_1'
+\sum_{n\ge1}
\frac{\alpha\beta G_n'-\alpha^2G_{n+1}'}{\epsilon^n}.
\tag{28.9}
$$

例如，$-\epsilon\alpha$乘上$G_{n+1}'/\epsilon^{n+1}$后，恰好成为第$n$重极点；相邻两重极点因而在同一系数中相遇。有限项与各个负幂的系数分别为零，给出

<span id="eq:c28-pole-recursion"></span>

$$
\beta=\alpha^2G_1',\qquad
G_{n+1}'=\frac{\beta}{\alpha}G_n'
=\alpha G_1'G_n',\qquad G_n(0)=0.
\tag{28.10}
$$

最后的边界值来自零耦合时$Z=1$，它固定了每次积分的常数。取第一步递推，便有$G_2'=\alpha(G_1')^2$。继续递推可见，一旦完整的简单极点确定，高重极点就受到一致性关系的约束。

先在一圈精度内代入$G_1=-3\alpha/2$，得到

<span id="eq:c28-beta-evaluated"></span>

$$
\beta(\alpha)=-\frac32\alpha^2+O(\alpha^3),\qquad
\frac{dg}{d\ln\mu}
=-\frac{\epsilon}{2}g-\frac{3g^3}{4(4\pi)^3}+O(g^5).
\tag{28.11}
$$

第二式利用了$\alpha\propto g^2$，所以$\beta_g/g=B_\epsilon/(2\alpha)$。第一式与上一节从物理截面求出的结果一致，说明同一尺度变化已经包含在紫外简单极点中，求它时可以省去散射率的有限部分。

递推还告诉我们，一圈信息能确定高阶结果中的哪些部分。若在$G_1$中只保留一圈项，依次使用递推并取零耦合边界值，便得到

<span id="eq:c28-leading-pole-example"></span>

$$
G_2=\frac98\alpha^2,\qquad
G_n=\frac{(-3/2)^n}{n}\alpha^n,\qquad
G=-\ln\left(1+\frac{3\alpha}{2\epsilon}\right).
\tag{28.12}
$$

把一般$G_n$求导后代入式[（28.10）](#eq:c28-pole-recursion)，两边的耦合幂次与系数相同；$n=1$又给回起始的一圈项。这一列就是由一圈函数生成的最高极点。完整多圈结果的$G_1$还含有新的$\alpha^2,\alpha^3,\ldots$系数，它们来自新的图积分，随后又各自参与高极点递推。

<span id="c28-mass"></span>

## 质量反常量纲

质量可以按同样的思路处理。对$m_0$的乘法关系取对数，并用$\mathcal M$表示质量的对数反项，以区别物理极点质量，定义

<span id="eq:c28-mass-log"></span>

$$
\mathcal M=\frac12\ln\frac{Z_m}{Z_\varphi}
=\sum_{n\ge1}\frac{\mathcal M_n}{\epsilon^n},\qquad
\mathcal M_1=\frac12(b_1-a_1)=-\frac5{12}\alpha+O(\alpha^2).
\tag{28.13}
$$

这里的$b_1$是质量反项的简单极点系数，由质量项的重标度关系确定。

现在$m_0=me^{\mathcal M}$。固定$m_0$后，参数质量的变化须抵消对数反项的变化；将耦合的跑动代入并逐重极点展开，有

<span id="eq:c28-mass-pole-matching"></span>

$$
\begin{aligned}
\frac{d\ln m}{d\ln\mu}
&=-B_\epsilon\partial_\alpha\mathcal M\\
&=\alpha\mathcal M_1'
+\sum_{n\ge1}
\frac{\alpha\mathcal M_{n+1}'-\beta\mathcal M_n'}{\epsilon^n}.
\end{aligned}
\tag{28.14}
$$

参数质量的尺度导数必须逐阶有限，因此负幂系数给出与耦合相同的递推结构，留下的有限项则确定质量反常量纲：

<span id="eq:c28-mass-gamma"></span>

$$
\mathcal M_{n+1}'=\frac{\beta}{\alpha}\mathcal M_n',\qquad
\gamma_m=\frac{d\ln m}{d\ln\mu}
=\alpha\mathcal M_1'
=-\frac5{12}\alpha+O(\alpha^2).
\tag{28.15}
$$

这里$\gamma_m$定义的是$m$的相对变化，所以$dm^2/d\ln\mu=2\gamma_m m^2$。若改用无量纲质量$m/\mu$，对数导数还须减去能标本身的变化，成为$\gamma_m-1$。质量、质量平方和无量纲质量的系数之所以不同，正是这两种运算的结果。

<span id="c28-cs"></span>

## 场的归一化和Callan–Symanzik方程

场归一化的改变还会传入关联函数。即使所描述的物理过程相同，用不同归一化场写出的传播子也会随尺度变化。先在正则化维数定义重整化传播子与裸传播子：

<span id="eq:c28-two-point-renormalization"></span>

$$
\begin{aligned}
\boldsymbol\Delta(k^2)
&=i\int d^dx\,e^{ikx}\langle0|T\varphi(x)\varphi(0)|0\rangle,\\
\boldsymbol\Delta_0(k^2)
&=i\int d^dx\,e^{ikx}\langle0|T\varphi_0(x)\varphi_0(0)|0\rangle
=Z_\varphi\boldsymbol\Delta(k^2).
\end{aligned}
\tag{28.16}
$$

对于实标量的时间序二点函数，平移不变性与两个场的交换使它在$x\mapsto-x$下不变，因此这里的$e^{+ikx}$与前面采用的相反傅里叶号给出同一个$k^2$函数。前置因子$i$则使自由传播子为$\boldsymbol\Delta=1/(k^2+m^2-i0)$。下面还要作维数极点运算，积分测度先保留$d$，取物理维数时再置6。

为了求场归一化的尺度变化，定义$\mathcal A=\ln Z_\varphi=\sum_{n\ge1}\mathcal A_n/\epsilon^n$，其简单极点为$\mathcal A_1=a_1$。对这个对数求导，再按调节器幂次展开，得到

<span id="eq:c28-field-poles"></span>

$$
\frac{d\ln Z_\varphi}{d\ln\mu}
=-\alpha a_1'
+\sum_{n\ge1}
\frac{\beta\mathcal A_n'-\alpha\mathcal A_{n+1}'}{\epsilon^n}.
\tag{28.17}
$$

重整化场及其传播子的尺度变化应当有限，因此负幂部分同样相消。场的反常量纲由剩下的有限部分确定，定义为

<span id="eq:c28-field-gamma"></span>

$$
\gamma_\varphi=\frac12\frac{d\ln Z_\varphi}{d\ln\mu}
=-\frac12\alpha a_1'
=\frac{\alpha}{12}+O(\alpha^2),\qquad
\left.\frac{d\varphi}{d\ln\mu}\right|_{\varphi_0}
=-\gamma_\varphi\varphi.
\tag{28.18}
$$

定义中的$1/2$来自裸场关系里的平方根，固定裸场后，重整化场必须作相反的归一化变化。线性项也随场一起转换：保持$Y_0$不变时，式[（28.2）](#eq:c28-bare-relations)给出$dY/d\ln\mu=\gamma_\varphi Y$，所以由无蝌蚪条件选定的$Y$也随之跑动。

在外部$k$固定时，直接对$\boldsymbol\Delta_0=Z_\varphi\boldsymbol\Delta$求导，既要微分场因子，也要计入传播子中参数的变化，因而有

<span id="eq:c28-two-point-chain-rule"></span>

$$
0=Z_\varphi\left[
\left(\frac{\partial}{\partial\ln\mu}
+B_\epsilon\frac{\partial}{\partial\alpha}
+\gamma_m m\frac{\partial}{\partial m}\right)\boldsymbol\Delta
+2\gamma_\varphi\boldsymbol\Delta\right].
\tag{28.19}
$$

显式$\mu$导数先固定$m,\alpha$，其余两个导数再补上这些参数的跑动，合起来才是沿同一裸理论的全导数。在无蝌蚪的参数曲面上，$Y$已经由归一化条件消去。最后取$\epsilon\to0$，得到传播子的Callan–Symanzik方程：

<span id="eq:c28-callan-symanzik"></span>

$$
\left[
\frac{\partial}{\partial\ln\mu}
+\beta(\alpha)\frac{\partial}{\partial\alpha}
+\gamma_m(\alpha)m\frac{\partial}{\partial m}
+2\gamma_\varphi(\alpha)
\right]\boldsymbol\Delta(k^2;\mu,\alpha,m)=0.
\tag{28.20}
$$

上一节的一圈自能可以具体展示这些尺度变化怎样相互补偿。令$z=k^2$，在固定$m,\alpha$处对式[（27.6）](/posts/srednicki-27/#eq:c27-msbar-self-energy)求显式尺度导数，有

<span id="eq:c28-self-energy-scale-check"></span>

$$
\frac{\partial\Pi}{\partial\ln\mu}
=-\alpha\int_0^1dx\,[m^2+x(1-x)z]
=-\alpha\left(m^2+\frac z6\right).
\tag{28.21}
$$

记$\mathcal D=\partial_{\ln\mu}+\beta\partial_\alpha+\gamma_m m\partial_m$。其中$\beta$作用于一圈自能时只贡献下一阶；本阶的质量隐式导数也只需作用于树级质量项。于是逆传播子的全导数为

<span id="eq:c28-cs-inverse-check"></span>

$$
\begin{aligned}
\mathcal D\boldsymbol\Delta^{-1}
&=\alpha\left(m^2+\frac z6\right)+2\gamma_m m^2+O(\alpha^2)\\
&=\frac{\alpha}{6}(z+m^2)+O(\alpha^2).
\end{aligned}
\tag{28.22}
$$

再对倒数求导，就得到$\mathcal D\boldsymbol\Delta=-(\alpha/6)\boldsymbol\Delta+O(\alpha^2)$，与场归一化项$+2\gamma_\varphi\boldsymbol\Delta$相消。这个例子把自能的显式变化、参数质量的跑动和场因子合在一起，也显示了自能在逆传播子中所带负号的作用。

<span id="c28-scattering-scale"></span>

## 外腿归一化怎样消去尺度变化

对连通的 $n$ 点函数，每个场都贡献一个 $Z_\varphi^{1/2}$。在去掉共同的动量守恒函数后，裸函数与重整化函数满足

<span id="eq:c28-npoint-running"></span>

$$
G_{c,0}^{(n)}=Z_\varphi^{n/2}G_c^{(n)},\qquad
\mathcal D G_c^{(n)}=-n\gamma_\varphi G_c^{(n)}.
$$

这里 $\mathcal D$ 仍在固定外动量处作用，且每个场采用同一归一化。先在离壳处截去全部精确外传播子，定义截腿连通核 $\mathcal A_n=\prod_{j=1}^n\boldsymbol\Delta(k_j)^{-1}G_c^{(n)}$。每个逆传播子满足 $\mathcal D\boldsymbol\Delta^{-1}=2\gamma_\varphi\boldsymbol\Delta^{-1}$，乘积法则于是给出

<span id="eq:c28-amputated-running"></span>

$$
\mathcal D\mathcal A_n
=(2n\gamma_\varphi-n\gamma_\varphi)\mathcal A_n
=n\gamma_\varphi\mathcal A_n.
$$

对于存在孤立稳定单粒子极点的外腿，写 $\boldsymbol\Delta(k^2)\sim R/(k^2+M^2-i0)$。物理极点质量满足 $\mathcal D M^2=0$，因此比较尺度方程在极点处的留数，得到 $\mathcal D R=-2\gamma_\varphi R$。按 [LSZ 约化](/posts/srednicki-05/)在壳化，并把固定的 $i$ 因子计入振幅定义，便有

<span id="eq:c28-lsz-scale-cancellation"></span>

$$
\begin{aligned}
\mathcal T_n&=R^{n/2}\mathcal A_n\big|_{\rm on\ shell},\\
\mathcal D\mathcal T_n
&=(-n\gamma_\varphi+n\gamma_\varphi)
 R^{n/2}\mathcal A_n\big|_{\rm on\ shell}=0.
\end{aligned}
$$

关联函数与截腿核都随场的归一化变化，而每条外腿的 $\sqrt R$ 恰好补偿这一变化。因此，从裸参数不变推出的关联函数方程，与上一节用物理振幅不变得到的参数跑动相容。

<span id="c28-characteristics"></span>

## 沿跑动参数求解

传播子的尺度方程同时包含质量和耦合的导数，可以沿它们的跑动轨迹化为普通微分方程。取$t=\ln(\mu/\mu_r)$，令$d\alpha/dt=\beta$、$dm/dt=\gamma_m m$；沿这条参数曲线，链式法则将式[（28.20）](#eq:c28-callan-symanzik)化为

<span id="eq:c28-characteristic"></span>

$$
\frac{d}{dt}\boldsymbol\Delta(k;\mu_re^t,\alpha(t),m(t))
=-2\gamma_\varphi(\alpha(t))\boldsymbol\Delta,
\tag{28.23}
$$

用积分因子解这一线性方程，从参照尺度积分到所求尺度，得到

<span id="eq:c28-characteristic-solution"></span>

$$
\boldsymbol\Delta(t)
=\exp\left[-2\int_0^tdu\,\gamma_\varphi(\alpha(u))\right]
\boldsymbol\Delta(0).
\tag{28.24}
$$

积分过程中动量$k$保持不变，改变的是计算同一裸理论所用的能标。若连续经过两个尺度区间，指数中的积分相加，参数曲线也首尾相接。在流方程具有唯一解的区间，这便给出了尺度变换的合成性质。

一圈时定义$W=1+\tfrac32\alpha_rt$。[上一节](/posts/srednicki-27/#c27-coupled-running)已经给出联立跑动解$\alpha=\alpha_r/W$、$m=m_rW^{-5/18}$。利用$d\ln W/dt=3\alpha/2$，场反常量纲的积分成为$\int_0^t\gamma_\varphi\,du=\ln W/18$，所以场与二点函数的归一化分别满足

<span id="eq:c28-one-loop-field-running"></span>

$$
\varphi(t)=W^{-1/18}\varphi(0),\qquad
\boldsymbol\Delta(t)=W^{-1/9}\boldsymbol\Delta(0).
\tag{28.25}
$$

这两式表示同一裸场在不同重整化尺度下的归一化关系，其中的演化参数是对数能标。使用这些表达式时，须有$W>0$，并且整个积分区间内的跑动耦合都足够小。

它们也给出了高能计算的一个方便步骤。若原参数在低尺度$\mu_r$指定，而要计算类空大动量$k^2$处的传播子，可以先在$\mu_h=\sqrt{k^2}$处计算，再沿同一轨迹反向换回原来的归一化：

<span id="eq:c28-hard-scale-conversion"></span>

$$
\boldsymbol\Delta(k;\mu_r)
=W_h^{1/9}\boldsymbol\Delta(k;\mu_h),\qquad
W_h=1+\frac34\alpha_r\ln\frac{k^2}{\mu_r^2}.
\tag{28.26}
$$

当$m^2\ll k^2$时，硬尺度处的领先传播子为$1/k^2$；把换回低尺度所需的$W_h^{1/9}$展开，就得到

<span id="eq:c28-leading-log-check"></span>

$$
\boldsymbol\Delta(k;\mu_r)
=\frac1{k^2}\left[1+\frac{\alpha_r}{12}
\ln\frac{k^2}{\mu_r^2}+\text{有限一圈项}+\cdots\right].
\tag{28.27}
$$

共同对数的系数与式[（27.7）](/posts/srednicki-27/#eq:c27-massless-offshell)中直接计算的自能相同，因而跑动方程将这一对数包含进了尺度换算因子。对于上一节的包容率，耦合跑动所给的领先因子同样可以写为

<span id="eq:c28-rate-leading-logs"></span>

$$
\alpha(\sqrt s)^2
=\frac{\alpha_r^2}
{[1+\tfrac34\alpha_r\ln(s/\mu_r^2)]^2}
=\alpha_r^2\left[1-\frac32\alpha_r\ln\frac s{\mu_r^2}+\cdots\right].
\tag{28.28}
$$

这将一圈$\beta$所决定的领先对数组织起来；完整的两圈有限部分仍需由相应图积分给出。包容率的含义也继续沿用第26节相同的初末态定义。

还可以保留有限的$\epsilon$，考察工程维数与量子修正共同引起的跑动。取$\epsilon\ne0$，方程为$d\alpha/dt=-\epsilon\alpha-3\alpha^2/2$，其解为

<span id="eq:c28-finite-epsilon-flow"></span>

$$
D_\epsilon(t)=1+\frac{3\alpha_r}{2\epsilon}(1-e^{-\epsilon t}),
\qquad
\alpha(t)=\frac{\alpha_re^{-\epsilon t}}{D_\epsilon(t)}.
\tag{28.29}
$$

求这个解时，先令$q=1/\alpha$，把方程化为$q'-\epsilon q=3/2$，再乘积分因子$e^{-\epsilon t}$后求得。沿同一条耦合轨迹积分，质量和场的比值分别为$m/m_r=D_\epsilon^{-5/18}$、$\varphi/\varphi_r=D_\epsilon^{-1/18}$。令$\epsilon\to0$，有$(1-e^{-\epsilon t})/\epsilon\to t$，便回到前面的物理维数解。

<span id="c28-fixed-point"></span>

## 固定点上的异常幂律

最后考察一种特殊情形。设某理论的$\beta$在非零$\alpha_*$处为零，并取$m=0$。此时$\alpha$保持不动，$\gamma_*=\gamma_\varphi(\alpha_*)$也成为常数，传播子的CS方程及其尺度解为

<span id="eq:c28-fixed-point-mu"></span>

$$
\left(\frac{\partial}{\partial\ln\mu}+2\gamma_*\right)
\boldsymbol\Delta(k^2)=0,
\qquad
\boldsymbol\Delta(k^2)=\mu^{-2\gamma_*}A(k^2).
\tag{28.30}
$$

这个微分方程先确定了尺度依赖。若所考察的无质量真空还不含另一有量纲尺度，洛伦兹不变性使$A$只能依赖$k^2$；再由$[\boldsymbol\Delta]=-2$，得到$[A]=-2+2\gamma_*$。于是其动量依赖也被量纲关系确定，先在$k^2>0$处写为

<span id="eq:c28-fixed-point-power"></span>

$$
\boldsymbol\Delta(k^2)
=\frac{C(\alpha_*)}{k^2}
\left(\frac{\mu^2}{k^2}\right)^{-\gamma_*}.
\tag{28.31}
$$

对$\ln\mu$取对数导数，这个解给回$-2\gamma_*$；同时$\mu^{-2\gamma_*}(k^2)^{-1+\gamma_*}$的工程质量维数仍为$-2$。因此异常指数改变的是动量的标度行为，并没有改变传播子整体的工程量纲。继续到类时动量时，非整数幂须按$k^2-i0$和原来的对数支定义。

固定$\mu$而缩放动量，传播子便随$k^{-2+2\gamma_*}$变化。要将这一指数与位置空间的场联系起来，设分离点场的标度维数为$\Delta_\varphi$，则二点函数的傅里叶变换带有幂次$k^{2\Delta_\varphi-d}$。具体地说，作$x\mapsto x/b$的代换，测度给出$b^{-d}$，两个场给出$b^{2\Delta_\varphi}$，相乘就得到这一动量幂。与传播子的幂次比较，有

<span id="eq:c28-field-scaling-dimension"></span>

$$
\Delta_\varphi=\frac{d-2}{2}+\gamma_*.
\tag{28.32}
$$

场的反常量纲由此直接进入了标度维数，临界现象中的异常幂律正体现这种变化。对于此处的实$\varphi^3$模型，一圈$\beta=-3\alpha^2/2$尚未给出非零正固定点；应用本段结果时，须先满足$\beta(\alpha_*)=0$，并确认真空没有其它尺度。

---

[← 第 27 节](/posts/srednicki-27/) · [章节地图](/srednicki/) · [第 29 节 →](/posts/srednicki-29/)
