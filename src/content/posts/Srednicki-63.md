---
title: 'Srednicki §63 旋量电动力学中的顶角函数'
date: 2026-09-14
category: 笔记
tags: [物理, 量子场论, Srednicki]
series: 'Srednicki QFT'
srednickiSections: [63]
hideFromHome: true
draft: false
---

<span id="c63"></span>

上一节已经求出了顶角的一圈积分，并用$Z_1$消去了紫外发散；还剩下一个有限常数，需要由电荷的定义来确定。此前的标量理论和汤川理论常在零外动量处定义耦合，这样做便于计算。电动力学则有一个更直接的选择：把电荷定义为长距离库仑作用中的系数。下面先说明这个定义怎样成为顶角的归一条件，再将已经算出的矩阵积分化为两个形状因子。

<span id="c63-charge"></span>

## 从库仑作用规定电荷

仍以$p$表示入射电子动量、$p'$表示出射电子动量，把入射光子的转移动量记为$q=p'-p$。电荷条件施加在外电子都在壳上的旋量夹式中：
<span id="eq:c63-charge-condition"></span>

$$
\left.\bar u_{s'}(p')V^\mu(p',p)u_s(p)\right|_{p^2=p'^2=-m^2,\ q^2=0}
=\left.e\bar u_{s'}(p')\gamma^\mu u_s(p)\right|_{p^2=p'^2=-m^2,\ q^2=0}.
\tag{63.1}
$$

这里的$e<0$是负电子电荷，沿用上一节的符号。质量和外场留数已经固定，因而这个条件恰好决定尚未固定的顶角有限部分。施加条件时仍保留正的光子调节质量$m_\gamma$；零质量光子的物理动量条件与内部积分的红外调节分别使用。

先看这些在壳条件选出了什么运动学。取真实、未来向的两个电子动量，并到$p$的静止系中计算。此时
<span id="eq:c63-zero-transfer-kinematics"></span>

$$
\begin{aligned}
p&=(m,\mathbf0),\qquad p'=(E',\mathbf p'),\qquad
E'=\sqrt{m^2+|\mathbf p'|^2},\\
q^2&=p'^2+p^2-2p\cdot p'=2m(E'-m)\ge0,\\
q^2=0&\quad\Longrightarrow\quad E'=m,
\quad\mathbf p'=0,\quad p'=p.
\end{aligned}
\tag{63.2}
$$

由于等式协变，最后一个结论在原来的参考系中也成立。归一条件选出的因此是零转移动量：电子与一个能量趋于零的光子相耦合。它并不是自由电子发射一束有限能量光子的过程。

在相同动量处，旋量归一和第38节的狄拉克方程给
<span id="eq:c63-diagonal-spin-charge"></span>

$$
\begin{aligned}
\bar u_{s'}(p)u_s(p)&=2m\delta_{s's},\\
\bar u_{s'}(p)\gamma^\mu u_s(p)&=2p^\mu\delta_{s's},\\
\bar u_s(p)V^\mu(p,p)u_s(p)&=2ep^\mu.
\end{aligned}
\tag{63.3}
$$

第二式也可由下面将使用的戈登恒等式在$q=0$时得到。不同自旋的右侧为零，不能由它读取电荷的数值；选择相同自旋，则$p^0>0$保证至少时间分量不为零。因此可用最后一行的对角矩阵元来确定电荷。

这个定义与库仑定律的联系，可由电子—电子散射看出。按第19节的完整核树图装配，振幅由两个单光子交换道和一个完整四费米顶角组成：

![完整顶角和光子传播子组成的两个交换道及四费米不可约核](/images/srednicki/s63-c63_01.svg)

<span id="c63-scattering-figure"></span>

图63a：完整电子—电子散射的三个核树图。空心圆表示完整电子—光子顶角，双波纹线表示完整光子传播子，方框表示四费米1PI核。第一图的向下动量为$Q_t=p_1-p'_1$，第二图为$Q_u=p_1-p'_2$；交换两个出射电子带来中间的负号。

记$J^\mu_{b'a}=\bar u(p'_b)V^\mu(p'_b,p_a)u(p_a)$。对直接道，光子在两个顶角的入射动量分别为$-Q_t$和$Q_t$，而光子核的标量系数只依赖$Q_t^2$。三个图的结构可写成
<span id="eq:c63-exact-kernel-assembly"></span>

$$
\begin{aligned}
\mathcal T
 &=J^\mu_{1'1}\,\widetilde{\boldsymbol\Delta}_{\mu\nu}(Q_t)J^\nu_{2'2}
   -J^\mu_{2'1}\,\widetilde{\boldsymbol\Delta}_{\mu\nu}(Q_u)J^\nu_{1'2}
   +\mathcal T_{4\psi},\\
\widetilde{\boldsymbol\Delta}_{\mu\nu}(Q)
 &\underset{Q^2\to0}{\sim}\frac{g_{\mu\nu}}{Q^2-i0}
 \quad\text{在守恒电流之间},\\
J^\mu(p,p)&=2ep^\mu\quad\text{对相同自旋}.
\end{aligned}
\tag{63.4}
$$

第一行的整体$i$来自两个$iV$和一条$\boldsymbol\Delta/i$，除去振幅定义中的$i$后正好留下所写的乘积。上一节的$\Pi(0)=0$使单光子极点具有单位留数，本节条件则固定它两端的电荷因子。因此，在各自的小转移道中，单光子交换的留数与以电荷$e$计算的树图相同。

再取非相对论、近静态的直接交换，$Q^0$相对于空间动量可略，两个电流的主项均为$J^0=2em$。由$g_{00}=-1$，得
<span id="eq:c63-coulomb-matching"></span>

$$
\begin{aligned}
\mathcal T_{\rm direct}&\simeq-\frac{4e^2m^2}{|\mathbf Q|^2},\\
\widetilde V(\mathbf Q)
 &=-\frac{\mathcal T_{\rm direct}}{4m^2}
   =\frac{e^2}{|\mathbf Q|^2},\\
V(r)&=e^2\int\frac{d^3\mathbf Q}{(2\pi)^3}
       \frac{e^{i\mathbf Q\cdot\mathbf r}}{|\mathbf Q|^2}
     =\frac{e^2}{4\pi r}.
\end{aligned}
\tag{63.5}
$$

第二行的$4m^2$来自四条相对论外态相对于非相对论态的$\sqrt{2E}$归一因子；负号则来自势在时间演化中的$-i\int Vdt$与散射振幅的$+i\mathcal T$。末行正是第55、56节已经评价的三维库仑核，只需乘上两端的电荷。两个同号电子的势为正，因而相互排斥。实验中的远距离小偏转所测量的就是这个系数。若同时给交换线保留辅助质量，先在$m_\gamma\ll|\mathbf Q|\ll m$的范围读取此系数；该质量不会成为物理上的电磁力程。

四费米1PI核不含上述单光子交换极点，所以这个极点的系数可以通过玻恩匹配规定长距离电荷。去掉红外调节后，多光子中间态还会产生割线及库仑迭代，完整散射须按上一节的方法合并软光子贡献。

<span id="c63-subtraction"></span>

## 顶角的有限减除

现在把这个条件用于上一节的积分。以下将式[（62.38）](/posts/srednicki-62/#eq:c62-vertex-numerator)中的有限分子$\widetilde N^\mu$简记为$N^\mu$；它已经不含圈动量。利用$Z_1$中一个有限常数的自由，可以把完整一圈顶角写成
<span id="eq:c63-subtracted-vertex"></span>

$$
V^\mu(p',p)=e\gamma^\mu-\frac{e^3}{16\pi^2}\int dF_3
 \left[\left(\ln\frac D{D_0}+2\kappa_1\right)\gamma^\mu
            -\frac{N^\mu}{2D}\right]+O(e^5).
\tag{63.6}
$$

这里$\int dF_3=1$，$\kappa_1$与参数无关；其归一与上一节电子留数中的$\kappa_2$不同。分母及分子分别为
<span id="eq:c63-denominators-numerator"></span>

$$
\begin{aligned}
D&=x_1(1-x_1)p^2+x_2(1-x_2)p'^2-2x_1x_2p\cdot p'\\
 &\quad+(x_1+x_2)m^2+x_3m_\gamma^2-i0,\\
D_0&=(x_1+x_2)^2m^2+x_3m_\gamma^2
     =(1-x_3)^2m^2+x_3m_\gamma^2,\\
a_1&=x_1p-(1-x_2)p',\qquad a_2=x_2p'-(1-x_1)p,\\
N^\mu&=\gamma_\nu(\slashed a_1+m)\gamma^\mu
                         (\slashed a_2+m)\gamma^\nu\\
 &=2\slashed a_2\gamma^\mu\slashed a_1
       +4m(a_1+a_2)^\mu I+2m^2\gamma^\mu.
\end{aligned}
\tag{63.7}
$$

第一行直接沿用上一节的配方，第二行代入$p'=p$及$p^2=-m^2$；剩余的$x_1+x_2$平方由各动量项相加得到。最后两行的三种伽马夹乘已在式[（62.39）](/posts/srednicki-62/#eq:c62-vertex-finite-numerator)中逐一缩去，此处将两个辅助动量$a,b$分别改记$a_1,a_2$。相应径向积分UV收敛，因而可以使用四维的最后一行。

有限反项怎样产生式[（63.6）](#eq:c63-subtracted-vertex)也应写明。令$c=e^2/(8\pi^2)$，将式[（62.42）](/posts/srednicki-62/#eq:c62-vertex-result)中的$\ln(D/\mu^2)$拆为$\ln(D/D_0)+\ln(D_0/\mu^2)$。同$e\delta Z_1\gamma^\mu$相加以后，所需的反项为
<span id="eq:c63-z1-finite-choice"></span>

$$
\delta Z_1
=c\left[-\frac1\varepsilon+1
       +\frac12\int dF_3\ln\frac{D_0}{\mu^2}-\kappa_1\right]+O(e^4).
\tag{63.8}
$$

$1/\varepsilon$及其有限常数随之消去，对数留下零转移的减除形式。这给出了壳上方案中$Z_1$与$\kappa_1$的具体对应。

在$p'=p$处，式[（63.6）](#eq:c63-subtracted-vertex)中的对数为零。夹在相同自旋的外旋量之间，再用$\bar u\gamma^\mu u=2p^\mu$，归一条件化为
<span id="eq:c63-kappa-condition"></span>

$$
4\kappa_1p^\mu
 =\int dF_3\frac{\bar u(p)N_0^\mu u(p)}{2D_0}.
\tag{63.9}
$$

因此剩下的工作只是求出这个在壳分子。此时$a_1=a_2=-x_3p$，由式[（63.7）](#eq:c63-denominators-numerator)，
<span id="eq:c63-zero-transfer-numerator"></span>

$$
\begin{aligned}
N_0^\mu&=2x_3^2\slashed p\gamma^\mu\slashed p
              -8mx_3p^\mu I+2m^2\gamma^\mu,\\
\bar uN_0^\mu u
 &=2x_3^2m^2(2p^\mu)-8mx_3p^\mu(2m)+2m^2(2p^\mu)\\
 &=4(1-4x_3+x_3^2)m^2p^\mu.
\end{aligned}
\tag{63.10}
$$

第一项的两个$\slashed p$分别作用在左右外旋量上，各给$-m$，所以相乘为正。第二项含标量双线性$\bar uu=2m$，它正是系数中$-4x_3$的来源。

利用参数δ函数消去$x_2$后，在固定$x_3$时$x_1$从0积到$1-x_3$，被积函数已不依赖$x_1$，因此
<span id="eq:c63-kappa-integral"></span>

$$
\begin{aligned}
\kappa_1
 &=\frac12\int dF_3\,
 \frac{1-4x_3+x_3^2}{(1-x_3)^2+x_3m_\gamma^2/m^2}\\
 &=\int_0^1dx_3\,(1-x_3)
 \frac{1-4x_3+x_3^2}{(1-x_3)^2+x_3m_\gamma^2/m^2}\\
 &=\int_0^1du\,
 \frac{u(u^2+2u-2)}{u^2+a^2(1-u)},\qquad
 u=1-x_3,\quad a=\frac{m_\gamma}{m}.
\end{aligned}
\tag{63.11}
$$

这里$dF_3$中的2与第一行的$1/2$相消。最后一行把危险端点移到$u=0$，这与上一节的留数积分具有相同分母。

<span id="c63-infrared-normalization"></span>

## 红外常数与两个反项的关系

上一节已经完整评价了$\kappa_2$的红外对数。将两个分子相减，可以用那个结果求出本节的新常数，而不必再做一遍相同的端点积分。记$h(u)=u^2+a^2(1-u)$，则
<span id="eq:c63-kappa-difference"></span>

$$
\begin{aligned}
\kappa_1-\kappa_2
 &=\int_0^1du\,\frac{u^2(2-u)}{h(u)}\\
 &=\frac32-a^2\int_0^1du\,\frac{(1-u)(2-u)}{h(u)}.
\end{aligned}
\tag{63.12}
$$

第二行用了$u^2=h-a^2(1-u)$，而$\int_0^1(2-u)du=3/2$。还须保证剩余积分乘$a^2$后消失。对$0<a\le1/2$，上一节已证明$h\ge(u^2+a^2)/2$；又有$(1-u)(2-u)\le2$，故余项的绝对值不超过
$4a^2\int_0^1du/(u^2+a^2)\le2\pi a$。于是
<span id="eq:c63-kappa-asymptotic"></span>

$$
\kappa_1=\kappa_2+\frac32+O(a)
        =-2\ln\frac m{m_\gamma}+\frac52+O(m_\gamma/m).
\tag{63.13}
$$

这个展开保留了小光子质量下的对数项与常数$5/2$，余项随$m_\gamma/m$趋于零。顶角的有限减除项与电子留数一样含软光子对数；紫外减除后的在壳积分仍须保留$m_\gamma$。

两个反项还满足一个较强的一圈关系。把$dF_3$积分改写成$u$积分，令$L(u)=\ln[m^2h(u)/\mu^2]$，由式[（63.8）](#eq:c63-z1-finite-choice)和式[（62.29）](/posts/srednicki-62/#eq:c62-counterterm-finite)得
<span id="eq:c63-finite-z1-z2"></span>

$$
\begin{aligned}
\frac{\delta Z_1-\delta Z_2}{c}
 &=\frac12+\int_0^1du\,(2u-1)L(u)-(\kappa_1-\kappa_2),\\
\int_0^1du\,(2u-1)L(u)
 &=\int_0^1du\,\frac{u(1-u)(2u-a^2)}{h(u)},\\
\frac{u(1-u)(2u-a^2)-u^2(2-u)}{h(u)}&=-u,\\
\delta Z_1&=\delta Z_2+O(e^4).
\end{aligned}
\tag{63.14}
$$

第二行对$(u^2-u)L$分部积分；固定$a>0$时$L$在两端有限，边界项为零。第三行将两个有理分子实际相减，最后用$\int_0^1u\,du=1/2$。因此这次相等包括有限部分，而且在去掉红外调节之前就成立。它与式[（62.45）](/posts/srednicki-62/#eq:c62-one-loop-vertex-ward)的一圈沃德关系相容，所得$Z_1$的小$a$展开也与式[（62.34）](/posts/srednicki-62/#eq:c62-onshell-z-finite)中的$Z_2$完全相同。

<span id="c63-onshell-numerator"></span>

## 把一般在壳顶角化为两个结构

为了将顶角用于散射，需要保持两条电子外腿在壳上，同时允许$q^2$非零。由式[（63.2）](#eq:c63-zero-transfer-kinematics)，真实电子散射的这个$q^2$为非负的类空转移。两条外腿始终满足同一个质量壳条件$p^2=p'^2=-m^2$。

长矩阵链的化简依靠两端的狄拉克方程，但$\slashed p$必须先移到右端，$\slashed p'$必须先移到左端。为清楚展示这一步，暂记$P=\slashed p$、$P'=\slashed p'$，并用$\doteq$表示夹在$\bar u(p')$与$u(p)$之间相等。反对易关系给出四个所需的夹式：
<span id="eq:c63-four-slash-sandwiches"></span>

$$
\begin{aligned}
P'\gamma^\mu P&\doteq m^2\gamma^\mu,\\
P\gamma^\mu P&=-m^2\gamma^\mu-2p^\mu P
                \doteq-m^2\gamma^\mu+2mp^\mu I,\\
P'\gamma^\mu P'&\doteq-m^2\gamma^\mu+2mp'^\mu I,\\
P\gamma^\mu P'
 &=\gamma^\mu P'P+2p\cdot p'\gamma^\mu-2p^\mu P'\\
 &=-P'\gamma^\mu P-2p'^\mu P
                   +2p\cdot p'\gamma^\mu-2p^\mu P'\\
 &\doteq(2p\cdot p'-m^2)\gamma^\mu+2m(p+p')^\mu I.
\end{aligned}
\tag{63.15}
$$

例如第二行先将左边的$P$移过$\gamma^\mu$，再用$P^2=-p^2=m^2$。最后一项需要两次移动，因而保留了内积项和两种外动量。

现在展开$\slashed a_2\gamma^\mu\slashed a_1$。四种矩阵的系数依次为$x_1x_2$、$-x_1(1-x_1)$、$-x_2(1-x_2)$和$(1-x_1)(1-x_2)$。把式[（63.15）](#eq:c63-four-slash-sandwiches)代入式[（63.7）](#eq:c63-denominators-numerator)，得到
<span id="eq:c63-expanded-onshell-numerator"></span>

$$
\begin{aligned}
N^\mu\doteq{}&
 \bigl[4(1-x_1-x_2+x_1x_2)p\cdot p'\\
 &\hspace{9mm}+2(2x_1-x_1^2+2x_2-x_2^2)m^2\bigr]\gamma^\mu\\
 &+4m(x_1^2-x_2+x_1x_2)p^\mu I
  +4m(x_2^2-x_1+x_1x_2)p'^\mu I.
\end{aligned}
\tag{63.16}
$$

例如$p^\mu I$的系数在提出$4m$后为
$-x_1(1-x_1)+(1-x_1)(1-x_2)+(2x_1-1)$，
乘开即为$x_1^2-x_2+x_1x_2$。这里最后一项来自$4m(a_1+a_2)^\mu$。另一个动量系数交换$x_1,x_2$便得。

令$K=p'+p$，以$q=p'-p$替换动量差。两个在壳条件给
$p\cdot p'=-m^2-q^2/2$；两个动量系数的和与差则分别给$K$和$q$。用$x_1+x_2=1-x_3$整理后，
<span id="eq:c63-sum-difference-basis"></span>

$$
\begin{aligned}
N^\mu\doteq{}&
 2\bigl[(1-2x_3-x_3^2)m^2-(x_3+x_1x_2)q^2\bigr]\gamma^\mu\\
 &-2m(x_3-x_3^2)K^\mu I\\
 &-2m\bigl[(x_1+x_1^2)-(x_2+x_2^2)\bigr]q^\mu I.
\end{aligned}
\tag{63.17}
$$

在$K$的系数中，两项之和除以2为
$2m[(x_1+x_2)^2-(x_1+x_2)]=-2mx_3(1-x_3)$。
在$q$的系数中，两项之差除以2为
$-2m(x_1-x_2)(1+x_1+x_2)$。
至于$\gamma^\mu$的系数，只需将$1-x_1-x_2$换成$x_3$并代入内积；其中的质量项合成$2(1-2x_3-x_3^2)m^2$。

分母也必须使用同一组在壳代入，得到
<span id="eq:c63-onshell-denominator"></span>

$$
D=x_1x_2q^2+(1-x_3)^2m^2+x_3m_\gamma^2-i0.
\tag{63.18}
$$

它在$x_1\leftrightarrow x_2$下对称，积分域及$dF_3$也不变。式[（63.17）](#eq:c63-sum-difference-basis)最后一行的系数却变号，因此
<span id="eq:c63-antisymmetric-parameter-integral"></span>

$$
\int dF_3\,
 \frac{(x_1+x_1^2)-(x_2+x_2^2)}D=0.
\tag{63.19}
$$

证明只需在整个单纯形上交换两个积分变量：积分值不变，而被积函数变为其负值，所以它必须为零。这一步是积分后的相消，不能逐点删去该分子。

剩下的$K^\mu$可以用第38节的戈登恒等式换成磁矩所需的反对称矩阵结构：
<span id="eq:c63-gordon-identity"></span>

$$
\begin{aligned}
\bar u'K^\mu u
 &=\bar u'\bigl[2m\gamma^\mu+2iS^{\mu\nu}q_\nu\bigr]u,\\
S^{\mu\nu}&=\frac i4[\gamma^\mu,\gamma^\nu].
\end{aligned}
\tag{63.20}
$$

为核对这里的号，可在$-2m\bar u'\gamma^\mu u$中分别用左右狄拉克方程代替两个$m$，再将$\slashed p'\gamma^\mu+\gamma^\mu\slashed p$分为反对易子与对易子；反对易子给$-K^\mu$，对易子给$2iS^{\mu\nu}q_\nu$。整理后便是所写的正号。

将戈登恒等式代入式[（63.17）](#eq:c63-sum-difference-basis)的$K^\mu$项，$\gamma^\mu$的质量系数再减去$4m^2(x_3-x_3^2)$。经过在壳夹式及完整参数积分两步后，分子可按下式使用：
<span id="eq:c63-integrated-numerator"></span>

$$
\begin{aligned}
\int dF_3\frac{\bar u'N^\mu u}D
 =\int dF_3\frac1D\bar u'\Bigl\{
 &2\bigl[(1-4x_3+x_3^2)m^2-(x_3+x_1x_2)q^2\bigr]\gamma^\mu\\
 &-4im(x_3-x_3^2)S^{\mu\nu}q_\nu\Bigr\}u.
\end{aligned}
\tag{63.21}
$$

因而顶角只剩下两个独立结构。我们将这两个结构的系数定义为无量纲形状因子：
<span id="eq:c63-form-factor-definition"></span>

$$
\bar u'V^\mu(p',p)u
=e\bar u'\left[F_1(q^2)\gamma^\mu
               -\frac i m F_2(q^2)S^{\mu\nu}q_\nu\right]u.
\tag{63.22}
$$

$F_1$称狄拉克形状因子，$F_2$称泡利形状因子。树级有$F_1=1$、$F_2=0$；电荷归一要求$F_1(0)=1$。第二项显含$q$，所以它在零转移电荷条件中不产生贡献，却能在转移的第一阶响应中留下新的物理效应。[下文的一般顶角分解](#c63-general-structure)将从规范不变性推出这两个结构。

<span id="c63-form-factors"></span>

## 两个形状因子与红外端点

从式[（63.6）](#eq:c63-subtracted-vertex)按两个矩阵结构分别读取系数即可。为把分式写清，记
$z=q^2/m^2$、$d=D/m^2$、$d_0=D_0/m^2$，
以及$R=1-4x_3+x_3^2$、$B=x_3+x_1x_2$。在固定$a=m_\gamma/m>0$下有
<span id="eq:c63-regulated-form-factors"></span>

$$
\begin{aligned}
F_1(q^2;a)
 &=1-\frac{e^2}{16\pi^2}\int dF_3
       \left[\ln\frac d{d_0}+\frac R{d_0}
                           +\frac{Bz-R}{d}\right]+O(e^4),\\
F_2(q^2;a)
 &=\frac{e^2}{8\pi^2}\int dF_3
          \frac{x_3(1-x_3)}{d}+O(e^4).
\end{aligned}
\tag{63.23}
$$

第一式中的$R/d_0$来自$2\kappa_1=\int dF_3R/d_0$；最后一项来自原分子的$\gamma^\mu$部分。第二式的号可从反对称部分单独核对：
$e^3N^\mu/(32\pi^2D)$给$-ie^3m(x_3-x_3^2)S^{\mu\nu}q_\nu/(8\pi^2D)$，
与定义中的$-ieF_2S^{\mu\nu}q_\nu/m$相比，正好得到所写的正系数。
在$q^2=0$处，$d=d_0$，第一式的两个有理项逐点抵消，因此$F_1(0;a)=1$。

接下来考察哪些积分允许去掉红外调节。为分析端点，把三角积分域改成矩形。先用δ函数消去$x_2$，再令
<span id="eq:c63-rectangular-parameters"></span>

$$
\begin{aligned}
t&=1-x_3,\qquad x_1=ty,\qquad x_2=t(1-y),
       \qquad 0\le t,y\le1,\\
\left|\frac{\partial(x_1,x_3)}{\partial(t,y)}\right|&=t,\qquad
dF_3=2t\,dt\,dy,\\
A(y,z)&=1+z\,y(1-y),\\
d&=t^2A(y,z)+(1-t)a^2,\qquad d_0=t^2+(1-t)a^2.
\end{aligned}
\tag{63.24}
$$

在真实散射域$z\ge0$，$A\ge1$，分母无零点。于是
<span id="eq:c63-infrared-dominating-bounds"></span>

$$
\begin{aligned}
0\le\ln\frac d{d_0}&\le\ln A(y,z),\\
0\le 2t\,\frac{x_3(1-x_3)}d
 &=\frac{2t^2(1-t)}{t^2A+(1-t)a^2}
 \le\frac{2(1-t)}A\le2.
\end{aligned}
\tag{63.25}
$$

第一行乘测度$2t$后可积，第二行已经包含测度。两者都有与$a$无关的可积上界，所以可以在这些积分中令$a\to0$。$F_1$剩下的两个有理项则没有同样的端点改善：其分子在$t=0$处通常非零，乘测度后出现$dt/t$，必须保留调节质量。

把允许取极限的对数改写出来，并在两个有理项中保留调节质量，第一形状因子成为
<span id="eq:c63-dirac-form-factor"></span>

$$
\begin{aligned}
F_1(q^2;a)=1-\frac{e^2}{16\pi^2}\int dF_3
\Bigg[&
 \ln\left(1+\frac{x_1x_2z}{(1-x_3)^2}\right)
 +\frac{1-4x_3+x_3^2}{(1-x_3)^2+x_3a^2}\\
 &+\frac{(x_3+x_1x_2)z-(1-4x_3+x_3^2)}
          {x_1x_2z+(1-x_3)^2+x_3a^2}\Bigg]\\
 &\hspace{14mm}+e^2o_{a\to0}(1)+O(e^4).
\end{aligned}
\tag{63.26}
$$

消失项来自对数中略去的调节质量，故上式按小$a$极限使用。固定$a$的完整一圈结果由式[（63.23）](#eq:c63-regulated-form-factors)给出。

<span id="c63-pauli-integral"></span>

## 完成泡利形状因子的参数积分

$F_2$的整个一圈积分都可去掉调节质量。利用式[（63.24）](#eq:c63-rectangular-parameters)的雅可比，分子的$x_3(1-x_3)=(1-t)t$与分母的$t^2$相约，得到
<span id="eq:c63-pauli-one-parameter"></span>

$$
\begin{aligned}
F_2(q^2)
 &=\frac{e^2}{8\pi^2}
  \int_0^1dy\int_0^1dt\,\frac{2(1-t)}{1+zy(1-y)}+O(e^4)\\
 &=\frac{e^2}{8\pi^2}
       \int_0^1\frac{dy}{1+zy(1-y)}+O(e^4).
\end{aligned}
\tag{63.27}
$$

最后一步用了$\int_0^12(1-t)dt=1$。由于$z=q^2/m^2\ge0$，分母$1+zy(1-y)$在整个积分区间为正；这个符号也决定了非零转移处的斜率和解析延拓的阈值。

最后一个积分可以完全求出。记它为$J(z)$，令$r=2y-1$，再定义$v^2=z/(z+4)$。利用关于$r$的偶性，
<span id="eq:c63-pauli-closed-form"></span>

$$
\begin{aligned}
J(z)&=\int_0^1\frac{dy}{1+zy(1-y)}
     =\frac4{z+4}\int_0^1\frac{dr}{1-v^2r^2},\\
\int_0^1\frac{dr}{1-v^2r^2}
 &=\left.\frac{\operatorname{artanh}(vr)}v\right|_0^1
   =\frac{\operatorname{artanh}v}{v},\\
J(z)&=\frac{4}{\sqrt{z(z+4)}}\,
       \operatorname{artanh}\sqrt{\frac z{z+4}},
       \qquad z>0,\\
F_2(q^2)&=\frac{e^2}{8\pi^2}J(q^2/m^2)+O(e^4).
\end{aligned}
\tag{63.28}
$$

这里$0<v<1$，所有函数均取实值。$z=0$由连续极限得到$J(0)=1$。若要延拓到类时区域，则从参数分母$1+zy(1-y)-i0$沿同一因果边界继续；最近的阈值是$z=-4$，对应电子—正电子对的产生。真实的类空轴$z\ge0$上则没有这个奇点。

两个极限也可以直接核对这个闭式。小$|z|$时，在$|z|<4$的邻域一致展开分母，再用
$\int_0^1y(1-y)dy=1/6$和$\int_0^1y^2(1-y)^2dy=1/30$，得到
<span id="eq:c63-pauli-limits"></span>

$$
\begin{aligned}
F_2(q^2)
 &=\frac{e^2}{8\pi^2}
   \left[1-\frac{q^2}{6m^2}+\frac{q^4}{30m^4}
                  +O(q^6/m^6)\right]+O(e^4),\\
\frac{dJ}{dz}
 &=-\int_0^1dy\,\frac{y(1-y)}{[1+zy(1-y)]^2}<0
       \qquad(z\ge0),\\
J(z)&=\frac{2\ln z}{z}
       +O\left(\frac{\ln z}{z^2}\right)\qquad(z\to+\infty).
\end{aligned}
\tag{63.29}
$$

最后一行来自$v=1-2/z+O(z^{-2})$及
$\operatorname{artanh}v=\frac12\ln z+O(z^{-1})$。
因此泡利部分在类空转移增大时下降；它的零动量有限值与高转移处的行为均由同一个参数积分给出。

这个积分还能帮助我们理解$F_1$与$F_2$的红外差别。作为补充，取固定$z>0$，在$F_1$有理项中只保留$t\to0$时的非零分子。它们分别为$R\to-2$与$Bz-R\to z+2$。含测度的软端点项为
<span id="eq:c63-dirac-infrared-coefficient"></span>

$$
\begin{aligned}
&\int_0^1dt\,2t
 \left[-\frac2{t^2+a^2}
             +\frac{z+2}{A t^2+a^2}\right]\\
&\hspace{12mm}
 =\left[-4+\frac{2(z+2)}A\right]\ln\frac1a+O(1),\\
F_1(q^2;a)-1
 &=-\frac{e^2}{8\pi^2}\bigl[(z+2)J(z)-2\bigr]
                  \ln\frac m{m_\gamma}+O(e^2)+O(e^4).
\end{aligned}
\tag{63.30}
$$

第一行的积分由$\int2t\,dt/(A t^2+a^2)=A^{-1}\ln(A t^2+a^2)$直接得到。分子被略去的部分至少多一阶$t$，其积分保持有界；把$a^2(1-t)$换成$a^2$时，两个分式之差的分子是$a^2t$。对$0<a\le1/2$、$A\ge1$，乘上测度$2t$后的绝对值不超过$4a^2t^2/(t^2+a^2)^2$，其积分又不超过$2\pi a$。乘上固定$z$的端点系数仍趋零，因而不会改变对数系数。最后一行的$O(e^2)$表示$a\to0$时有界的一圈剩余项，$O(e^4)$则表示另一个微扰阶次。在$z=0$时，$J(0)=1$使对数系数消失，与严格归一$F_1(0;a)=1$一致；在非零转移处，一圈顶角自身仍带软光子依赖。

最后取决定磁矩的零转移值。式[（63.27）](#eq:c63-pauli-one-parameter)中被积函数变成1，因此
<span id="eq:c63-pauli-zero"></span>

$$
F_2(0)=\frac{e^2}{8\pi^2}+O(e^4)
      =\frac{\alpha}{2\pi}+O(\alpha^2),\qquad
\alpha=\frac{e^2}{4\pi}.
\tag{63.31}
$$

数值评价可取经验输入$\alpha\simeq1/137.036$。给定电荷以后，圈积分确定了泡利形状因子的第一个量子修正。下一节把这个顶角与缓慢变化的外电磁场相接，求出它对电子能量和磁矩的影响。

<span id="c63-general-structure"></span>

## 一般在壳顶角的三个协变量

仍令电子以$p$入射、以$p'$出射，光子的转移动量为$q=p'-p$，
并用$K=p'+p$缩短公式。两电子在同一个正能质量壳上，因而
<span id="eq:c63-ex-1-kinematics"></span>

$$
\begin{aligned}
p^2=p'^2&=-m^2,\qquad m>0,\\
q\cdot K&=0,\qquad p\cdot p'=-m^2-\frac12q^2,\\
\slashed p\,u&=-mu,\qquad
\bar u'\slashed p'=-m\bar u'.
\end{aligned}
\tag{63.32}
$$

这里$u=u_s(p)$、$\bar u'=\bar u_{s'}(p')$。以下约化发生在
$\bar u'$与$u$之间；离壳的完整顶角矩阵还可以含有更多结构。
基分解使用四维物理外旋量空间；圈积分仍按$d=4-\varepsilon$正规化，
完成紫外减除后再取四维极限。
质量、耦合及调节尺度给定后，由两外动量组成的洛伦兹标量只剩$q^2$，
所以形状因子对运动学的依赖也只需写成$q^2$。

先看克利福德代数怎样减少候选项。记$X=\slashed p$、
$Y=\slashed p'$；本书的负号约定给
<span id="eq:c63-ex-1-clifford-reordering"></span>

$$
\begin{aligned}
X^2=Y^2&=m^2,\qquad
XY+YX=2m^2+q^2,\\
\gamma^\mu X&=-X\gamma^\mu-2p^\mu,\qquad
\gamma^\mu Y=-Y\gamma^\mu-2p'^\mu.
\end{aligned}
\tag{63.33}
$$

在不带独立赝矢量耦合的矩阵串中，自由指标$\mu$或者在一个
$\gamma^\mu$上，或者在$p^\mu,p'^\mu$上；其余动量进入$X,Y$或标量积。
利用前两条关系，把所有$Y$移向左端、所有$X$移向右端，再消去各自的平方。
若移动时遇到$\gamma^\mu$，后两条关系产生的附加项正好带
$p^\mu$或$p'^\mu$。因此只须保留
$Y^aX^b$及$Y^a\gamma^\mu X^b$，其中$a,b=0,1$。
两端在壳方程随即给出
<span id="eq:c63-ex-1-endpoint-reduction"></span>

$$
\begin{aligned}
\bar u'Y^aX^bu&=(-m)^{a+b}\bar u'u,\\
\bar u'Y^a\gamma^\mu X^bu
 &=(-m)^{a+b}\bar u'\gamma^\mu u.
\end{aligned}
\tag{63.34}
$$

例如$S^{\mu\nu}p_\nu$本来就是
$i(\gamma^\mu X-X\gamma^\mu)/4$，也包含在这个约化过程中。
更高阶的动量因子只改变标量系数，不增加新的在壳协变量。

[第47节的矩阵基推导](/posts/srednicki-47/#c47-matrix-basis)所建立的16个矩阵基
包括$\gamma_5$和$\gamma^\mu\gamma_5$；以普通矢量$p,p'$组成的
独立赝矢量项在本节的宇称不变真空与矢量耦合中被排除。
但在改写一个普通伽马矩阵串时，$\gamma_5$仍可能和
$\epsilon^{\mu\nu\rho\sigma}$同时出现。以本书
$\epsilon^{0123}=+1$、$\gamma_5=i\gamma^0\gamma^1\gamma^2\gamma^3$为例，
三伽马的完全反对称部分给
<span id="eq:c63-ex-1-parity-even-dual"></span>

$$
\begin{aligned}
-i\epsilon^{\mu\nu\rho\sigma}p_\nu p'_\rho\gamma_\sigma\gamma_5
 ={}&\gamma^\mu XY+p^\mu Y-p'^\mu X
       +(p\cdot p')\gamma^\mu .
\end{aligned}
\tag{63.35}
$$

右边由$\gamma^\mu\gamma^\nu\gamma^\rho$减去其三种度规缩并得到，
所以它同样按前述移序约化。左边同时含反对称张量与伽马五，
整体仍是普通矢量。宇称守恒限制的是独立的物理结构，并不禁止这样的中间写法。

将三个剩余协变量的系数分别记为$A,B,C$，在壳顶角便可写成
<span id="eq:c63-ex-1-three-form-factors"></span>

$$
\bar u'V^\mu(p',p)u
 =e\,\bar u'\!
 \left[A(q^2)\gamma^\mu+B(q^2)K^\mu+C(q^2)q^\mu\right]u.
\tag{63.36}
$$

其中$e<0$，$A$无量纲，$B,C$的质量维数为$-1$。
这些系数在特殊运动学点上可能需要由一般动量处的定义取极限；
下面先在一般$q^2$处使用这组基。

<span id="c63-gauge-constraint"></span>

## 从局域变换推导顶角约束

对于一般转移动量，所需的纵向约束可以直接从局域场变换得到。
先用$\mathfrak e$记局域相位中的电荷系数，随后用物理归一把它与$e$对应。
第58节的变换写成
<span id="eq:c63-ex-1-gauge-transformation"></span>

$$
\begin{aligned}
A_\mu^\chi&=A_\mu-\partial_\mu\chi,&
\Psi^\chi&=U\Psi,\\
\bar\Psi^\chi&=\bar\Psi U^{-1},&
U(x)&=e^{-i\mathfrak e\chi(x)}.
\end{aligned}
\tag{63.37}
$$

取$\chi$平滑且有紧支撑，使变换不改变真空边界和外态。
动能中对$U$求导产生
$+\mathfrak e\bar\Psi\gamma^\mu\Psi\,\partial_\mu\chi$，
而$+\mathfrak e A_\mu\bar\Psi\gamma^\mu\Psi$的变分恰好是它的负值；
质量项与麦克斯韦项分别不变。共同的费米场归一因子同时乘在动能和
协变耦合上，不影响这个抵消。

在量子计算中还须处理规范固定。将显式依赖规范代表的二次项记为
<span id="eq:c63-ex-1-quadratic-breaking"></span>

$$
S_{\rm br}[A]=-\frac12\int d^4x
 \left[\frac1\xi(\partial_\mu A^\mu)^2+m_\gamma^2A_\mu A^\mu\right].
\tag{63.38}
$$

本节实际计算取$\xi=1$，并保持$m_\gamma>0$调节软光子。
它们的无穷小规范变分对$A$都是线性的：
<span id="eq:c63-ex-1-linear-breaking-variation"></span>

$$
\delta S_{\rm br}
 =\int d^4x\left[
 \frac1\xi(\partial\cdot A)\,\partial^2\chi
 +m_\gamma^2 A^\mu\partial_\mu\chi\right].
\tag{63.39}
$$

由于这一变分只含光子场，它不会在费米两点与顶角之间增加新项。

为看清这一点，在路径积分中保留线性源
$S_{\rm src}=\int(J^\mu A_\mu+\bar\eta\Psi+\bar\Psi\eta)$。
对积分变量作式[（63.37）](#eq:c63-ex-1-gauge-transformation)的变换，
使用相容的矢量对称调节和局部减除。费米场与其独立伴随变量的贝雷津
雅可比分别为$(\det U)^{-1}$和$\det U$，在相同调节基底中相消；
光子场平移的雅可比为1。这里没有手征变换或伽马五插入。
于是无穷小变元公式与源项的实际变分为
<span id="eq:c63-ex-1-change-variable-identity"></span>

$$
\begin{aligned}
0&=\left\langle\delta S_{\rm br}+\delta S_{\rm src}\right\rangle,\\
\delta S_{\rm src}
 &=\int d^4x\left[
 -J^\mu\partial_\mu\chi
 -i\mathfrak e\,\bar\eta\chi\Psi
 +i\mathfrak e\,\bar\Psi\chi\eta\right].
\end{aligned}
\tag{63.40}
$$

源的次序始终保持为$\bar\eta\Psi+\bar\Psi\eta$。
因为右侧对每个场至多一次，取期望值就是把场换成平均场。
再按[第21节](/posts/srednicki-21/)的正源项约定作勒让德变换，
其变分为$-\delta S_{\rm src}$，从而得到
<span id="eq:c63-ex-1-effective-gauge-invariance"></span>

$$
\delta\Gamma=\delta S_{\rm br},\qquad
\delta\widehat\Gamma=0,\qquad
\widehat\Gamma:=\Gamma-S_{\rm br}.
\tag{63.41}
$$

量子作用量的规范约束由此从作用量、测度及源的变元传递下来，
规范固定与光子质量调节的已知变分则保留在$S_{\rm br}$中。
对微扰展开，这一等式逐阶成立；维数正规化中的无伽马五矢量电流及
保持该恒等式的反项正是这里采用的设置。

在$\widehat\Gamma$中抽出恰含一对费米平均场的部分，定义逆传播核
$\mathcal K[A]$。由于$\bar\psi$始终放在左边，有
<span id="eq:c63-ex-1-kernel-covariance"></span>

$$
\begin{aligned}
\widehat\Gamma\big|_{\bar\psi\psi}
 &=-\int d^4x\,d^4y\,
       \bar\psi(x)\mathcal K[A](x,y)\psi(y),\\
\mathcal K[A-\partial\chi](x,y)
 &=U(x)\mathcal K[A](x,y)U^{-1}(y).
\end{aligned}
\tag{63.42}
$$

第二行直接由第一行在任意$\bar\psi,\psi$下不变得到。
这个核属于完整1PI量子作用量，所以对它的$A$系数取导数时得到的
正是电磁顶角。按$e^{ipx}$的傅里叶约定展开，
<span id="eq:c63-ex-1-kernel-vertex-expansion"></span>

$$
\begin{aligned}
\mathcal K[A](p',p)
 &=(2\pi)^4\delta^4(p'-p)\mathcal K(p)
    -V^\mu(p',p)A_\mu(q)+O(A^2),\\
\mathcal K(p)&=\slashed p+m-\Sigma(\slashed p).
\end{aligned}
\tag{63.43}
$$

这里二次核的负号与自由作用量
$\bar\psi(i\slashed\partial-m)\psi$相符；
因此$A$项在$\mathcal K$中带负号，在作用量中却给$+\bar\psi V^\mu A_\mu\psi$。

对式[（63.42）](#eq:c63-ex-1-kernel-covariance)取$\chi$的一次项。
左侧用$\delta A_\mu(q)=-iq_\mu\chi(q)$，右侧分别让相位作用在核的两端，
得到同一矩阵的两种表达式：
<span id="eq:c63-ex-1-ward-kernel"></span>

$$
\begin{aligned}
\delta\mathcal K(p',p)
 &=i q_\mu V^\mu(p',p)\chi(q),\\
\delta\mathcal K(p',p)
 &=i\mathfrak e\,[\mathcal K(p')-\mathcal K(p)]\chi(q),\\
q_\mu V^\mu(p',p)
 &=\mathfrak e\,[\mathcal K(p')-\mathcal K(p)].
\end{aligned}
\tag{63.44}
$$

右侧第一项的$\mathcal K(p')$来自核右端的相位，第二项的
$\mathcal K(p)$来自核左端的相位；按此顺序保留即可固定差分的号。
外电子在物理质量壳上时，
$\mathcal K(p)u=0$且$\bar u'\mathcal K(p')=0$，
故这个等式已经证明$q_\mu\bar u'V^\mu u=0$。

它也说明$\mathfrak e$如何由本节的电荷条件确定。
固定$m_\gamma>0$，在单位留数的质量壳附近可写
$\mathcal K(z)=z+m+(z+m)^2H(z)$，其中$z=\slashed p$、$H$在该处正则。
求一次动量导数后，第二项留下的每一项至少有一个$(z+m)$位于外端，
因此夹在在壳旋量之间为零。把差分恒等式取$p'\to p$，得到
<span id="eq:c63-ex-1-phase-charge-normalization"></span>

$$
\begin{aligned}
\bar u V^\mu(p,p)u
 &=\mathfrak e\,\bar u
       \frac{\partial\mathcal K(p)}{\partial p_\mu}u
 \\&=\mathfrak e\,\bar u\gamma^\mu u
 =e\,\bar u\gamma^\mu u,\qquad \mathfrak e=e .
\end{aligned}
\tag{63.45}
$$

最后一步使用式[（63.1）](#eq:c63-charge-condition)的物理电荷归一，选取非零的对角自旋矩阵元即可。
这里先保留红外调节，因而确有上述孤立质量壳和留数展开。

对实际的一圈结果，可以用已求出的自能再核对一次这个差分。
式[（62.45）](/posts/srednicki-62/#eq:c62-one-loop-vertex-ward)的光子动量在本节改记$q$；
将树顶角、顶角反项和自能反项都写出，便有
<span id="eq:c63-ex-1-one-loop-counterterms"></span>

$$
\begin{aligned}
q_\mu V_{\rm loop}^\mu(p',p)
 &=e[\Sigma_{\rm loop}(\slashed p)-\Sigma_{\rm loop}(\slashed p')],\\
\Sigma(z)&=\Sigma_{\rm loop}(z)-\delta Z_2z-\delta Z_m m+O(e^4),\\
V^\mu&=e(1+\delta Z_1)\gamma^\mu+V_{\rm loop}^\mu+O(e^5),\\
q_\mu V^\mu
 &=e(1+\delta Z_1)\slashed q
   +e[\Sigma_{\rm loop}(\slashed p)-\Sigma_{\rm loop}(\slashed p')]
   +O(e^5)\\
 &=e[\mathcal K(p')-\mathcal K(p)]+O(e^5).
\end{aligned}
\tag{63.46}
$$

最后一行用了本节在相同$m_\gamma$下固定的
$\delta Z_1=\delta Z_2+O(e^4)$，其中包括有限部分；
两自能的质量反项相减为零。于是壳上减除
$\Sigma(-m)=0$使两端分别消去，一圈结果给
$q_\mu\bar u'V^\mu u=0+O(e^5)$。
这里复用的是第62节已建立的开费米链恒等式
$S'\slashed qS=S-S'$，所有核先在可逆的解析域中比较，再取共同的费曼边界。

现在将规范约束代入三系数分解。式[（63.32）](#eq:c63-ex-1-kinematics)分别消去
伽马项和$K^\mu$项：
<span id="eq:c63-ex-1-longitudinal-form-factor"></span>

$$
\begin{aligned}
\bar u'\slashed q\,u
 &=\bar u'(\slashed p'-\slashed p)u
   =(-m+m)\bar u'u=0,\\
q_\mu\bar u'V^\mu u
 &=e\left[A\bar u'\slashed q\,u
     +B(q\cdot K)\bar u'u+Cq^2\bar u'u\right]\\
 &=e\,q^2C(q^2)\bar u'u=0.
\end{aligned}
\tag{63.47}
$$

条件须对全部外自旋成立。为确认可以消去$\bar u'u$，用第38节的自旋和，
并用$(\bar u'u)^*=\bar u u'$，得到
<span id="eq:c63-ex-1-nonzero-scalar-bilinear"></span>

$$
\begin{aligned}
\sum_{s,s'}|\bar u_{s'}(p')u_s(p)|^2
 &=\operatorname{tr}\!\left[
       (-\slashed p'+m)(-\slashed p+m)\right]\\
 &=4(m^2-p\cdot p')=8m^2+2q^2>0
 \qquad(q^2\ge0,\ m>0).
\end{aligned}
\tag{63.48}
$$

因此在每个真实的非零类空转移处，至少有一对自旋给出非零标量双线性，
从而
<span id="eq:c63-ex-1-c-constraint"></span>

$$
q^2C(q^2)=0,\qquad C(q^2)=0\quad(q^2\ne0).
\tag{63.49}
$$

这项沃德约束不给$A$与$B$之间增加另一条关系。
在$q^2=0$处，式[（63.49）](#eq:c63-ex-1-c-constraint)的第一式单独不能约束$C$；
而且真实的同支等质量动量此时已经满足$p'=p$，$q^\mu$结构本身消失。
我们按一般$q^2$处定义形状因子，并在固定$m_\gamma>0$下取其正则的连续极限，
由此确定$C(0)=0$。在复动量域中同样沿既定解析分支及其边界取值。

<span id="c63-form-factor-map"></span>

## 两种形状因子记法的对应

剩下的两个协变量可换成$\gamma^\mu$与$S^{\mu\nu}q_\nu$，以便直接读取狄拉克、泡利形状因子。按
$S^{\mu\nu}=i[\gamma^\mu,\gamma^\nu]/4$，
第38节的戈登恒等式由下面两项相加得到：
<span id="eq:c63-ex-1-gordon"></span>

$$
\begin{aligned}
\gamma^\mu\slashed p&=-p^\mu-2iS^{\mu\nu}p_\nu,\\
\slashed p'\gamma^\mu&=-p'^\mu+2iS^{\mu\nu}p'_\nu,\\
-2m\bar u'\gamma^\mu u
 &=\bar u'[-K^\mu+2iS^{\mu\nu}q_\nu]u,\\
\bar u'K^\mu u
 &=\bar u'[2m\gamma^\mu+2iS^{\mu\nu}q_\nu]u.
\end{aligned}
\tag{63.50}
$$

把最后一行代入$B K^\mu$，并使用$C=0$，得到
<span id="eq:c63-ex-1-two-basis-conversion"></span>

$$
\bar u'V^\mu u
 =e\,\bar u'\left[
 (A+2mB)\gamma^\mu+2iB S^{\mu\nu}q_\nu\right]u.
\tag{63.51}
$$

式[（63.22）](#eq:c63-form-factor-definition)在泡利项前定义的系数是$-iF_2/m$；
逐项比较，便得到两个形状因子及其逆变换：
<span id="eq:c63-ex-1-form-factor-map"></span>

$$
\begin{aligned}
F_1(q^2)&=A(q^2)+2mB(q^2),&
F_2(q^2)&=-2mB(q^2),\\
A(q^2)&=F_1(q^2)+F_2(q^2),&
B(q^2)&=-\frac{F_2(q^2)}{2m},\qquad C(q^2)=0.
\end{aligned}
\tag{63.52}
$$

两个$F$均无量纲，泡利项的负号则由本书的定义固定。
物理电荷条件另外给出
<span id="eq:c63-ex-1-charge-condition"></span>

$$
A(0)+2mB(0)=F_1(0)=1.
\tag{63.53}
$$

规范约束消除了独立的纵向响应，电荷归一固定了零转移时的一个组合；
其余动量依赖以及$F_2$的数值由动力学计算决定。

---

[← 第 62 节](/posts/srednicki-62/) · [章节地图](/srednicki/) · [第 64 节 →](/posts/srednicki-64/)
