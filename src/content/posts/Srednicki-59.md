---
title: 'Srednicki §59 旋量电动力学中的散射'
date: 2026-09-14
category: 笔记
tags: [物理, 量子场论, Srednicki]
series: 'Srednicki QFT'
srednickiSections: [59]
hideFromHome: true
draft: false
---

<span id="c59"></span>

上一节建立的费曼规则，现在可以用来计算电子与正电子湮灭为两个光子的过程。
它只有两幅树图，却同时用到了费米子的自旋求和、光子的偏振求和以及规范不变性。
先把这些步骤接起来，再完成其中的矩阵迹，就能得到适用于任意入射能量的树级结果。
高能时还可进一步忽略电子质量；下一节将利用旋量螺旋度方法简化这一情形。

<span id="c59-amplitude"></span>

## 两幅图怎样给出振幅

用$p=p_1$、$q=p_2$分别表示入射电子和正电子的动量，用$k=k'_1$、$l=k'_2$
表示两个出射光子的动量。撇号只用来区别末态标签。所有这些动量都取正能，
并满足
<span id="eq:c59-external-momenta"></span>

$$
e^-(p)e^+(q)\longrightarrow\gamma(k)\gamma(l),\qquad
p+q=k+l,\qquad
p^2=q^2=-m^2,\quad k^2=l^2=0 .
\tag{59.1}
$$

本节取$m>0$。两条光子可以按两种次序接到同一条费米线上，因而有图59a的
两个贡献。没有三光子顶点，也没有同时连接两光子与一对费米子的原始顶点，
所以在$e^2$阶没有其他树图。

<span id="c59-figure"></span>

![电子正电子湮灭为两光子的t道与u道图，出光子次序相反而两图相加](/images/srednicki/s59-c59_01.svg)

图59a：电子正电子湮灭的两种光子次序。
左图内部箭头带动量$a=p-k$，右图带$b=p-l$。入正电子的物理动量是$q$，
其费米箭头却沿$-q$；因此左图下顶点有$a=l-q$，右图有$b=k-q$。
两条出光子线的箭头表示正能动量流出。图间的加号来自光子的玻色统计。

从左图的正电子端$\bar v(q)$开始，逆着费米箭头读到电子端$u(p)$，依次遇到
出光子$l$的顶角、内部传播子以及出光子$k$的顶角。
先固定全部外自旋和偏振，并省略相应标签：例如
$\varepsilon_k^\mu=\varepsilon_{\lambda'_1}^\mu(\mathbf k)$、
$\bar v(q)=\bar v_{s_2}(q)$、$u(p)=u_{s_1}(p)$。
将上一节的内线$\widetilde S/i$和两个$ie\gamma$相乘，得到
<span id="eq:c59-one-graph"></span>

$$
\begin{aligned}
i\mathcal T_t
&=\varepsilon_k^\mu\varepsilon_l^\nu\,
 \bar v(q)(ie\gamma_\nu)
 \frac{-i(-\slashed a+m)}{a^2+m^2-i0}
 (ie\gamma_\mu)u(p)\\
&=ie^2\varepsilon_k^\mu\varepsilon_l^\nu\,
 \bar v(q)\gamma_\nu
 \frac{-\slashed a+m}{a^2+m^2-i0}\gamma_\mu u(p).
\end{aligned}
\tag{59.2}
$$

这里$(ie)^2(-i)=ie^2$，而图的值是$i\mathcal T_t$，故振幅本身的系数为$e^2$。
以归一化波包表示外端点，沿既定入态$b_1^\dagger d_2^\dagger|0\rangle$，
两个湮灭端点按$d_2b_1$作用，
有$\langle0|d_2b_1b_1^\dagger d_2^\dagger|0\rangle=1$，这也固定了共同相位。
交换两条光子线不交换费米外端，第二幅图因此与第一幅相加。
两个出光子都带$\varepsilon$，只有共轭振幅才带$\varepsilon^*$。

为把分母写成不变量，定义
<span id="eq:c59-mandelstam"></span>

$$
\begin{aligned}
s&=-(p+q)^2=-(k+l)^2,\\
t&=-(p-k)^2=-(q-l)^2,\qquad
u=-(p-l)^2=-(q-k)^2,\\
s+t+u
&=4m^2+2p\cdot(k+l-q)=2m^2 .
\end{aligned}
\tag{59.3}
$$

最后一行先展开三个负平方，再使用$k+l-q=p$与$p^2=-m^2$。
记$r=m^2$、$d_t=r-t$、$d_u=r-u$，则两内线分母分别为$d_t$和$d_u$。
把两个图相加，并将所有gamma矩阵收集到一个矩阵中，便有
<span id="eq:c59-matrix-amplitude"></span>

$$
\begin{aligned}
\mathcal T&=\varepsilon_k^\mu\varepsilon_l^\nu
                 \bar v(q)A_{\mu\nu}u(p),\\
A_{\mu\nu}
&=e^2\left[
 \gamma_\nu\frac{N_a}{d_t}\gamma_\mu+
 \gamma_\mu\frac{N_b}{d_u}\gamma_\nu\right],\\
N_a&=-\slashed a+m,\qquad N_b=-\slashed b+m,\qquad
a=p-k,\quad b=p-l .
\end{aligned}
\tag{59.4}
$$

$A_{\mu\nu}$是作用于旋量指标的矩阵，其两个洛伦兹指标与外偏振连接。
此处省去分母的$i0$有直接的运动学依据。取质心系，将入射电子方向选作第三轴，
令$\mathbf n$是第一个出光子的单位方向、$c=n_3=\cos\theta$，则
<span id="eq:c59-cm-momenta"></span>

$$
\begin{aligned}
E&=\frac{\sqrt s}{2},\qquad
\beta=\sqrt{1-\frac{4r}{s}},\\
p^\mu&=(E,0,0,\beta E),\qquad
q^\mu=(E,0,0,-\beta E),\\
k^\mu&=(E,E\mathbf n),\qquad l^\mu=(E,-E\mathbf n).
\end{aligned}
\tag{59.5}
$$

能量守恒使每个光子的能量也等于$E$。由$p\cdot k=-E^2+\beta E^2c$
及$t=r+2p\cdot k$，立即得到
<span id="eq:c59-physical-denominators"></span>

$$
d_t=\frac{s}{2}(1-\beta c),\qquad
d_u=\frac{s}{2}(1+\beta c),\qquad
d_t+d_u=s .
\tag{59.6}
$$

在有限$s\ge4m^2$处，$0\le\beta<1$且$|c|\le1$，所以两个分母均为正。
本节树幅可以在整个有质量物理区域直接取实分母。以下保留振幅的$e^2$阶、
模方的$e^4$阶；在固定非奇异运动学处，圈幅与树幅的干涉从$e^6$阶开始。

<span id="c59-spin-average"></span>

## 自旋平均为什么成为一个迹

我们要计算未分辨初态自旋的湮灭率，因而需要先求振幅的模方，再对两个独立
初态各平均两个自旋。矩阵$A_{\mu\nu}$使这个计算与第46节的办法完全衔接。
沿狄拉克共轭的定义$\bar M=\gamma^0M^\dagger\gamma^0$，实动量满足
$\overline{\slashed a}=\slashed a$，乘积则反序。因此
<span id="eq:c59-dirac-adjoint"></span>

$$
\begin{aligned}
\overline{\gamma_\nu N_a\gamma_\mu}
 &=\gamma_\mu N_a\gamma_\nu,\\
\bar A_{\rho\sigma}
 &=e^2\left[
  \gamma_\rho\frac{N_a}{d_t}\gamma_\sigma+
  \gamma_\sigma\frac{N_b}{d_u}\gamma_\rho\right]
 =A_{\sigma\rho}.
\end{aligned}
\tag{59.7}
$$

这里交换的是两个矩阵指标，外动量仍固定不动。
若在别的运动学区域保留有限极点处方，取伴随时还须共轭该处方；
当前的实分母由式[（59.6）](#eq:c59-physical-denominators)保证。

利用$(\bar vMu)^*=\bar u\bar Mv$，先取复共轭，再与原来的振幅相乘：
<span id="eq:c59-complex-square"></span>

$$
\begin{aligned}
\mathcal T^*
 &=\varepsilon_k^{\rho*}\varepsilon_l^{\sigma*}
       \bar u(p)A_{\sigma\rho}v(q),\\
|\mathcal T|^2
 &=\varepsilon_k^\mu\varepsilon_l^\nu
   \varepsilon_k^{\rho*}\varepsilon_l^{\sigma*}
   \bigl(\bar vA_{\mu\nu}u\bigr)
   \bigl(\bar uA_{\sigma\rho}v\bigr).
\end{aligned}
\tag{59.8}
$$

外旋量的分量都是普通复数；两括号交换时没有格拉斯曼负号。
自旋求和则用第38节的完备关系，简记
<span id="eq:c59-spin-densities"></span>

$$
P=\sum_{s_1}u_{s_1}(p)\bar u_{s_1}(p)=-\slashed p+m,\qquad
Q=\sum_{s_2}v_{s_2}(q)\bar v_{s_2}(q)=-\slashed q-m .
\tag{59.9}
$$

$Q$的质量项带负号，这是正电子求和与电子求和的关键差别。
为看清矩阵次序，暂把旋量指标全部写出：
<span id="eq:c59-spin-trace-indices"></span>

$$
\begin{aligned}
\sum_{s_1,s_2}
 (\bar v_a A_{\mu\nu,ab}u_b)
 (\bar u_c A_{\sigma\rho,cd}v_d)
 &=A_{\mu\nu,ab}P_{bc}A_{\sigma\rho,cd}Q_{da}\\
 &=\operatorname{Tr}[A_{\mu\nu}P A_{\sigma\rho}Q].
\end{aligned}
\tag{59.10}
$$

第一个自旋和连接$u_b\bar u_c$，第二个连接$v_d\bar v_a$，恰好把矩阵链首尾闭合。
对四种等概率初态取平均，结果为
<span id="eq:c59-initial-average"></span>

$$
\frac14\sum_{s_1,s_2}|\mathcal T|^2
=\frac14\varepsilon_k^\mu\varepsilon_l^\nu
 \varepsilon_k^{\rho*}\varepsilon_l^{\sigma*}
 \operatorname{Tr}[A_{\mu\nu}P A_{\sigma\rho}Q].
\tag{59.11}
$$

接下来还要把未分辨的末态光子偏振相加。它们是不同的末态结果，所以求和，
不再除以偏振数。两个光子的同一性则在积分计数时处理。

<span id="c59-polarizations"></span>

## 偏振求和与两幅图的纵向抵消

库仑规范的两种物理偏振只占垂直于$\mathbf k$的空间平面。第56节已经求得
其完备关系。引入时间方向的单位矢量$\hat t$和传播方向的空间单位矢量$\hat z$，可写成
<span id="eq:c59-physical-polarization"></span>

$$
\begin{aligned}
P_\gamma^{\mu\rho}(k)
&=\sum_{\lambda=\pm}
  \varepsilon_\lambda^\mu(\mathbf k)
  \varepsilon_\lambda^{\rho*}(\mathbf k)
 =g^{\mu\rho}+\hat t^\mu\hat t^\rho-\hat z^\mu\hat z^\rho,\\
\hat t^2&=-1,\qquad \zeta=\hat t\cdot k,\qquad
\hat z^\mu=\frac{k^\mu+\zeta\hat t^\mu}{\sqrt{k^2+\zeta^2}} .
\end{aligned}
\tag{59.12}
$$

在$\hat t=(1,\mathbf0)$的坐标系中，$\zeta=-k^0$，分子正是$(0,\mathbf k)$；
故$\hat z$是光子传播方向的空间单位矢量。这种写法同时消去了时间分量和
空间纵向分量，只留下两个物理方向。

如果把$\hat z$展开，投影中除度规外会出现含$k^\mu$的项。前面处理光子传播子时，
这样的项与守恒流缩并后消失；散射振幅的对应条件则是：给外偏振加上一个
沿$k^\mu$的分量，振幅保持不变。规范变换$\delta A^\mu=-\partial^\mu\Gamma$
恰好产生这种纵向分量。若将实规范波的两种频率系数记为$\Gamma_\pm$，则
<span id="eq:c59-gauge-frequency"></span>

$$
\begin{aligned}
\Gamma(x)&=\Gamma_+(k)e^{ikx}+\Gamma_-(k)e^{-ikx},
 \qquad \Gamma_-=\Gamma_+^*,\\
\delta\varepsilon^{\mu*}&=-ik^\mu\Gamma_+,\qquad
\delta\varepsilon^\mu=+ik^\mu\Gamma_- .
\end{aligned}
\tag{59.13}
$$

这里已把单个平面波的共同归一化吸收入$\Gamma_\pm$。
前一偏振配入光子，后一偏振配出光子，两式彼此共轭。

对一条特定的外光子线，先把其余因子统写成$\mathcal M_\mu$。纵向位移不改变振幅，
就要求这个矩阵元与光子动量正交：
<span id="eq:c59-ward-condition"></span>

$$
\mathcal T_{\rm out}=\varepsilon^\mu\mathcal M_\mu,\qquad
\mathcal T_{\rm in}=\varepsilon^{\mu*}\mathcal M_\mu,\qquad
k^\mu\mathcal M_\mu=0 .
\tag{59.14}
$$

这个条件称为沃德恒等式。对于本节的两幅树图，只需使用
自由狄拉克方程就能证明它。关键在于同时保留光子接到费米线上的两种次序。

令$D(v)=\slashed v+m$，并把去掉$i$的自由传播子记为$S(v)$。克利福德关系及外旋量方程给出
<span id="eq:c59-dirac-inverse"></span>

$$
\begin{aligned}
S(v)&=\frac{-\slashed v+m}{v^2+m^2},\qquad
D(v)S(v)=S(v)D(v)=1,\\
D(p)u(p)&=0,\qquad \bar v(q)D(-q)=0 .
\end{aligned}
\tag{59.15}
$$

这里仅需$v=a,b$，其分母已知非零。把第一条光子的偏振换成动量$k$，
两幅图分别出现$S(a)\slashed k$和$\slashed kS(b)$。由于$k=p-a=b+q$，
它们可各化成两个逆传播子的差：
<span id="eq:c59-first-photon-ward"></span>

$$
\begin{aligned}
S(a)\slashed k\,u
 &=S(a)[D(p)-D(a)]u=-u,\\
\bar v\slashed kS(b)
 &=\bar v[D(b)-D(-q)]S(b)=\bar v,\\
k^\mu\bar v A_{\mu\nu}u
 &=e^2\bigl[-\bar v\gamma_\nu u+\bar v\gamma_\nu u\bigr]=0 .
\end{aligned}
\tag{59.16}
$$

第一项的负号来自内线末端，第二项的正号来自同一条线的另一端。
单幅图通常留下非零的$\bar v\gamma_\nu u$，相加后才抵消。
交换$(k,\mu)$与$(l,\nu)$使$a,b$及两图互换，因而同时得到
<span id="eq:c59-two-photon-ward"></span>

$$
k^\mu\bar v A_{\mu\nu}u=0,\qquad
l^\nu\bar v A_{\mu\nu}u=0 .
\tag{59.17}
$$

两个等式均对外旋量的每一种自旋成立。第67节将从量子理论的规范对称性出发，
把这种抵消推广到含圈图的情形。

现在展开式[（59.12）](#eq:c59-physical-polarization)。同完整振幅及其共轭缩并时，
所有带$k^\mu$或$k^\rho$的项由上面的关系消失，剩下的时间方向分量也因$k^2=0$而消失：
<span id="eq:c59-polarization-replacement"></span>

$$
\begin{aligned}
P_\gamma^{\mu\rho}
&=g^{\mu\rho}+\hat t^\mu\hat t^\rho
 -\frac{k^\mu k^\rho+\zeta(k^\mu\hat t^\rho+\hat t^\mu k^\rho)
                  +\zeta^2\hat t^\mu\hat t^\rho}{k^2+\zeta^2}\\
&\longrightarrow
g^{\mu\rho}+
\left(1-\frac{\zeta^2}{k^2+\zeta^2}\right)\hat t^\mu\hat t^\rho
\ \xrightarrow{k^2=0}\ g^{\mu\rho}.
\end{aligned}
\tag{59.18}
$$

两条外光子都可以这样处理。这里的箭头指缩并中的替换；物理偏振张量本身
仍是秩为2的投影。因而要先对完整两图使用横向性，再将结果展开为各图的平方
和干涉项。偏振求和与自旋平均合在一起，得到
<span id="eq:c59-unpolarized-trace"></span>

$$
\mathcal A(s,t,u):=\langle|\mathcal T|^2\rangle
\equiv\frac14\sum_{s_1,s_2}\sum_{\lambda'_1,\lambda'_2}|\mathcal T|^2
=\frac14\operatorname{Tr}[A_{\mu\nu}P A^{\nu\mu}Q].
\tag{59.19}
$$

接下来的计算完全归结为四维gamma矩阵的代数。

<span id="c59-traces"></span>

## 把四个矩阵迹化为不变量

矩阵$A_{\mu\nu}$含$t$、$u$两项，它与共轭矩阵相乘便给四个贡献。
仍用$P,Q,N_a,N_b$表示前面定义的矩阵，把初态平均的$1/4$计入各核，并按
两条内线的组合分别记为
<span id="eq:c59-four-traces"></span>

$$
\begin{aligned}
\langle\Phi_{tt}\rangle
 &=\frac14\operatorname{Tr}
 [\gamma^\nu N_a\gamma^\mu P\gamma_\mu N_a\gamma_\nu Q],\\
\langle\Phi_{uu}\rangle
 &=\frac14\operatorname{Tr}
 [\gamma^\mu N_b\gamma^\nu P\gamma_\nu N_b\gamma_\mu Q],\\
\langle\Phi_{tu}\rangle
 &=\frac14\operatorname{Tr}
 [\gamma^\nu N_a\gamma^\mu P\gamma_\nu N_b\gamma_\mu Q],\\
\langle\Phi_{ut}\rangle
 &=\frac14\operatorname{Tr}
 [\gamma^\mu N_b\gamma^\nu P\gamma_\mu N_a\gamma_\nu Q].
\end{aligned}
\tag{59.20}
$$

每个重复洛伦兹指标都出现一次上标、一次下标。
将两条内线的分母和耦合补回去，就有
<span id="eq:c59-four-kernel-square"></span>

$$
\mathcal A=e^4\left[
\frac{\langle\Phi_{tt}\rangle}{d_t^2}
+\frac{\langle\Phi_{tu}\rangle+\langle\Phi_{ut}\rangle}{d_td_u}
+\frac{\langle\Phi_{uu}\rangle}{d_u^2}\right].
\tag{59.21}
$$

交换两光子使$a\leftrightarrow b$、$t\leftrightarrow u$，并使矩阵中的
$\mu\leftrightarrow\nu$。第一条迹由此变成第二条，第三条变成第四条。
所以只需独立计算$tt$与$tu$，但两者的缩并次序不同：$tt$在$P$两边有一对
同指标gamma，$tu$的同指标gamma之间还隔着传播分子。

第47节已经从克利福德代数推导了所需的夹乘恒等式。
直接使用式[（47.23）](/posts/srednicki-47/#eq:c47-contractions-four-d)的四维结果，连同这里所需的迹公式，有
<span id="eq:c59-gamma-identities"></span>

$$
\begin{aligned}
\gamma^\mu\gamma_\mu&=-4,&
\gamma^\mu\slashed v\gamma_\mu&=2\slashed v,\\
\gamma^\mu\slashed v\slashed w\gamma_\mu&=4v\cdot w,&
\gamma^\mu\slashed v\slashed w\slashed z\gamma_\mu
 &=2\slashed z\slashed w\slashed v,\\
\operatorname{Tr}1&=4,&
\operatorname{Tr}(\slashed v\slashed w)&=-4v\cdot w .
\end{aligned}
\tag{59.22}
$$

奇数个gamma的迹为零。用这些夹乘式先缩短链，就能免去直接展开八个gamma的
全部配对。剩下的标量积由运动学决定：例如$s=2r-2p\cdot q$，
$t=r+2p\cdot k$，可得四组关系
<span id="eq:c59-external-products"></span>

$$
\begin{aligned}
p\cdot q&=r-\frac s2,\qquad &k\cdot l&=-\frac s2,\\
p\cdot k=q\cdot l&=\frac{t-r}{2},&
p\cdot l=q\cdot k&=\frac{u-r}{2}.
\end{aligned}
\tag{59.23}
$$

第一行来自$s$的两种写法，第二行来自$t,u$各自的两种写法，
只需分别使用$p^2=q^2=-r$与$k^2=l^2=0$。
据此再列出内部动量将要用到的积：
<span id="eq:c59-internal-products"></span>

$$
\begin{aligned}
a^2&=-t,\qquad b^2=-u,\\
p\cdot a&=-r-p\cdot k=-\frac{t+r}{2},&
q\cdot a&=q\cdot p-q\cdot k=\frac{t+r}{2},\\
p\cdot b&=-\frac{u+r}{2},&
q\cdot b&=\frac{u+r}{2},\\
a\cdot b
&=p^2-p\cdot(k+l)+k\cdot l\\
&=-r-\frac{t+u-2r}{2}-\frac s2=-r .
\end{aligned}
\tag{59.24}
$$

$q\cdot a$一式的最后一步及最后一行用了$s+t+u=2r$；
换成$b$时只交换$t,u$。这些关系将所有迹的结果化为$s,t,u,m$。

先计算$tt$。紧邻$P$的夹乘为
$\gamma^\mu P\gamma_\mu=-2(\slashed p+2m)$。
因此剩下的工作是先把$X=N_a(\slashed p+2m)N_a$化为单位矩阵和一个gamma的线性组合。
把两个$N_a$展开，有
<span id="eq:c59-tt-numerator"></span>

$$
\begin{aligned}
X={}&\slashed a\slashed p\slashed a
 +2m\slashed a^2
 -m(\slashed a\slashed p+\slashed p\slashed a)
 -4r\slashed a+r\slashed p+2m^3\\
={}&(a^2+r)\slashed p
 -2(a\cdot p+2r)\slashed a
 +2m(a\cdot p-a^2+r)\\
={}&(r-t)\slashed p+(t-3r)\slashed a+m(t+r).
\end{aligned}
\tag{59.25}
$$

第二行用了$\slashed a^2=-a^2$以及
$\slashed a\slashed p+\slashed p\slashed a=-2a\cdot p$。
三gamma项也可先交换前两个因子，得到
$\slashed a\slashed p\slashed a
=-\slashed p\slashed a^2-2(a\cdot p)\slashed a
=a^2\slashed p-2(a\cdot p)\slashed a$。
再代入式[（59.24）](#eq:c59-internal-products)，便是最后一行。

现在只剩$X$外面的另一对gamma。一个gamma的夹乘给2，单位矩阵的夹乘给$-4$，
于是
<span id="eq:c59-tt-scalar-reduction"></span>

$$
\begin{aligned}
\langle\Phi_{tt}\rangle
 &=-\frac12\operatorname{Tr}[\gamma^\nu X\gamma_\nu Q],\\
\gamma^\nu X\gamma_\nu
 &=2(r-t)\slashed p+2(t-3r)\slashed a-4m(t+r),\\
\operatorname{Tr}(\slashed pQ)&=4p\cdot q,\qquad
\operatorname{Tr}(\slashed aQ)=4a\cdot q,\qquad
\operatorname{Tr}Q=-4m,\\
\langle\Phi_{tt}\rangle
 &=-4\bigl[(r-t)p\cdot q+(t-3r)a\cdot q+2r(t+r)\bigr].
\end{aligned}
\tag{59.26}
$$

将两个标量积代入，再按$s+t+u=2r$消去$s$，便得到
<span id="eq:c59-tt-polynomial"></span>

$$
\begin{aligned}
\langle\Phi_{tt}\rangle
 &=-4\left[(r-t)\left(r-\frac s2\right)
       +\frac{(t-3r)(t+r)}2+2r(t+r)\right]\\
 &=2[(r-t)s-t^2-3r^2]\\
 &=2[tu-r(3t+u)-r^2].
\end{aligned}
\tag{59.27}
$$

中间一行保留$s$，有助于检查最后的变量替换；它与最后一行是同一多项式。

干涉核$tu$的计算从另一处开始。先缩并第一与第三个显式gamma，把所得矩阵记为$L^\mu$：
<span id="eq:c59-interference-sandwich"></span>

$$
\begin{aligned}
L^\mu
&=\gamma^\nu N_a\gamma^\mu P\gamma_\nu\\
&=\gamma^\nu\left[
 \slashed a\gamma^\mu\slashed p
 -m\slashed a\gamma^\mu-m\gamma^\mu\slashed p+r\gamma^\mu
 \right]\gamma_\nu\\
&=2\slashed p\gamma^\mu\slashed a
  -4m(a^\mu+p^\mu)+2r\gamma^\mu,\\
\langle\Phi_{tu}\rangle
&=\frac14\operatorname{Tr}[L^\mu N_b\gamma_\mu Q].
\end{aligned}
\tag{59.28}
$$

三gamma夹乘反转次序，所以第一项变为$2\slashed p\gamma^\mu\slashed a$；
两个二gamma夹乘分别给$4a^\mu$、$4p^\mu$。
由此得到的三项可分别求迹，最后再相加。

第一项中还含一对夹乘。将$N_b=-\slashed b+m$展开，它成为
$\gamma^\mu\slashed aN_b\gamma_\mu=-4a\cdot b+2m\slashed a$，故
<span id="eq:c59-interference-first"></span>

$$
\begin{aligned}
T_1
&=\frac12\operatorname{Tr}
 [\slashed p\gamma^\mu\slashed aN_b\gamma_\mu Q]\\
&=-2(a\cdot b)\operatorname{Tr}(\slashed pQ)
    +m\operatorname{Tr}(\slashed p\slashed aQ)\\
&=-8(a\cdot b)(p\cdot q)+4r(p\cdot a).
\end{aligned}
\tag{59.29}
$$

最后一步中，$\slashed p\slashed aQ$的三gamma部分迹为零，
质量项则为$-m\operatorname{Tr}(\slashed p\slashed a)=4m\,p\cdot a$。

第二项的$a^\mu+p^\mu$直接与$\gamma_\mu$缩并，形成$\slashed h$，
其中$h=a+p$。乘开两个质量项后，只有两个二gamma迹留下：
<span id="eq:c59-interference-second"></span>

$$
\begin{aligned}
T_2
&=-m\operatorname{Tr}[(-\slashed b+m)\slashed h(-\slashed q-m)]\\
&=-m\operatorname{Tr}
 [\slashed b\slashed h\slashed q
    +m\slashed b\slashed h-m\slashed h\slashed q-r\slashed h]\\
&=-m[-4m\,b\cdot h+4m\,h\cdot q]\\
&=4r[b\cdot(a+p)-q\cdot(a+p)].
\end{aligned}
\tag{59.30}
$$

第一项和最后一项分别含三个、一个gamma，故迹为零。
第三部分最短；由$\gamma^\mu N_b\gamma_\mu=-2\slashed b-4m$，得到
<span id="eq:c59-interference-third"></span>

$$
\begin{aligned}
T_3
&=\frac r2\operatorname{Tr}[\gamma^\mu N_b\gamma_\mu Q]\\
&=\frac r2\operatorname{Tr}[(-2\slashed b-4m)(-\slashed q-m)]\\
&=\frac r2[-8b\cdot q+16r]
 =-4r\,b\cdot q+8r^2.
\end{aligned}
\tag{59.31}
$$

这样原来的长迹已经全部变成标量积。将三部分合并，用
$a\cdot b=-r$、$p\cdot q=r-s/2$以及式[（59.24）](#eq:c59-internal-products)，便有
<span id="eq:c59-tu-polynomial"></span>

$$
\begin{aligned}
\langle\Phi_{tu}\rangle
={}&-8(a\cdot b)(p\cdot q)\\
 &+4r[p\cdot a+a\cdot b+p\cdot b-q\cdot a-p\cdot q-q\cdot b]
 +8r^2\\
={}&8r\left(r-\frac s2\right)
 +4r\left(\frac{3s}{2}-6r\right)+8r^2\\
={}&2r(s-4r).
\end{aligned}
\tag{59.32}
$$

第二行方括号内的化简也可直接分组：
$p\cdot a-q\cdot a=-(t+r)$，
$p\cdot b-q\cdot b=-(u+r)$，
$a\cdot b-p\cdot q=s/2-2r$；
总和为$s/2-t-u-4r=3s/2-6r$。

最后交换两光子，即将$t,u$互换，另外两个核便为
<span id="eq:c59-exchanged-kernels"></span>

$$
\begin{aligned}
\langle\Phi_{uu}\rangle
 &=2[tu-r(3u+t)-r^2],\\
\langle\Phi_{ut}\rangle
 &=2r(s-4r)=\langle\Phi_{tu}\rangle .
\end{aligned}
\tag{59.33}
$$

$tt$与$uu$交换了$t,u$的系数，干涉项只依赖$s$，所以在交换下保持不变。
四个核都具有质量维数4，除以相应两个分母后，式[（59.21）](#eq:c59-four-kernel-square)
成为无量纲的振幅平方。

<span id="c59-limits"></span>

## 完整结果及其物理极限

把四个核合起来，便可直接讨论湮灭率的能量和角度依赖。
先用$t=r-d_t$、$u=r-d_u$将各核改写为
<span id="eq:c59-denominator-polynomials"></span>

$$
\begin{aligned}
\langle\Phi_{tt}\rangle&=2d_td_u+4rd_t-8r^2,\\
\langle\Phi_{uu}\rangle&=2d_td_u+4rd_u-8r^2,\\
\langle\Phi_{tu}\rangle+\langle\Phi_{ut}\rangle
 &=4r(d_t+d_u)-16r^2 .
\end{aligned}
\tag{59.34}
$$

例如第一行的$t,u$乘积给
$2(r^2-rd_t-rd_u+d_td_u)$，线性质量项给
$-2r(4r-3d_t-d_u)$，再减$2r^2$，便得到所列结果。
把三行分别除以$d_t^2,d_u^2,d_td_u$后，线性质量项中的两组倒数相加，
平方质量项中的交叉分母则补成一个完全平方：
<span id="eq:c59-combined-square"></span>

$$
\mathcal A
=2e^4\left[
\frac{d_t}{d_u}+\frac{d_u}{d_t}
+4r\left(\frac1{d_t}+\frac1{d_u}\right)
-4r^2\left(\frac1{d_t}+\frac1{d_u}\right)^2
\right].
\tag{59.35}
$$

这个表达式显然在$t,u$交换下不变，但最后一项带负号，非负性尚未直接显出。
将它改写到质心系便能同时看清符号与角分布。式[（59.6）](#eq:c59-physical-denominators)给
<span id="eq:c59-cm-substitution"></span>

$$
\begin{aligned}
\frac{d_t}{d_u}+\frac{d_u}{d_t}
 &=\frac{2(1+\beta^2c^2)}{1-\beta^2c^2},\\
\frac1{d_t}+\frac1{d_u}
 &=\frac{4}{s(1-\beta^2c^2)},\qquad
\frac{4r}{s}=1-\beta^2 .
\end{aligned}
\tag{59.36}
$$

记$D_c=1-\beta^2c^2$，后两个质量项合起来为
$4(1-\beta^2)/D_c-4(1-\beta^2)^2/D_c^2
=4\beta^2(1-\beta^2)(1-c^2)/D_c^2$。
于是完整树级结果也可写成
<span id="eq:c59-positive-cm-square"></span>

$$
\mathcal A
=4e^4\left[
\frac{1+\beta^2c^2}{1-\beta^2c^2}
+\frac{2\beta^2(1-\beta^2)(1-c^2)}
       {(1-\beta^2c^2)^2}\right].
\tag{59.37}
$$

在物理区域内两项均非负，且$c\to-c$对应交换两个相同光子。
阈值附近$\beta\to0$，入粒子失去空间运动方向，未极化的结果应当各向同性；
上式确实给出
<span id="eq:c59-threshold"></span>

$$
\mathcal A\longrightarrow4e^4,\qquad
\langle\Phi_{tu}\rangle=\langle\Phi_{ut}\rangle\longrightarrow0 .
\tag{59.38}
$$

这里取极限的是振幅平方。若用它求湮灭截面，还须除以入射通量。
第11节的两体相空间公式[（11.30）](/posts/srednicki-11/#eq:c11-cm-differential)在本节只需代入
$|\mathbf k|/|\mathbf p|=1/\beta$；若用第一个带标签光子的全立体角计数事件，
再除以两个相同末态的$2!$，得到补充的截面关系
<span id="eq:c59-cross-section-normalization"></span>

$$
\begin{aligned}
\left.\frac{d\sigma_{\rm event}}{d\Omega}\right|_{\rm full\ sphere}
&=\frac1{2!}\frac{\mathcal A}{64\pi^2s}\frac1\beta,\\
\sigma_{\rm event}\xrightarrow{\beta\to0}
&\frac{e^4}{32\pi m^2\beta}
=\frac{\pi\alpha_{\rm em}^2}{2m^2\beta}.
\end{aligned}
\tag{59.39}
$$

最后一式用了角积分$4\pi$、$s\to4m^2$和$e^2=4\pi\alpha_{\rm em}$。
也可以只积分一个不重复的光子半球，此时不写$1/2!$。
阈值处截面的$1/\beta$来自趋零的入射通量，前面的振幅平方本身保持有限。
这里先取树级贡献，再作小$\beta$展开。

另一个有用极限是$s\gg m^2$。在$c$固定且远离$\pm1$时，
$1-\beta^2c^2$保持非零，所有显式质量修正都按$m^2/s$减小，故
<span id="eq:c59-high-energy"></span>

$$
\mathcal A
=2e^4\left(\frac ut+\frac tu\right)+O(e^4m^2/s)
=4e^4\frac{1+c^2}{1-c^2}+O(e^4m^2/s).
\tag{59.40}
$$

误差估计在任意固定的闭角区间$|c|\le1-\delta$、$\delta>0$上成立。
若同时接近前向，$1-\beta c$中的$1-\beta\simeq2m^2/s$
会与$1-c\simeq\theta^2/2$竞争；当$\theta^2$降到$m^2/s$量级时，
分母中的质量便不能先删去。后向区域同理。因此无质量电子近似
适合固定角的高能振幅，全角积分仍需保留两端的质量尺度。

<span id="c59-compton"></span>

## 从湮灭过程到康普顿散射

用$p,k$表示入射电子和光子的动量，用$p',k'$表示相应的末态动量。四个外动量
均取正能，康普顿过程及其不变量为

<span id="eq:c59-ex-compton-kinematics"></span>

$$
\begin{aligned}
e^-(p)+\gamma(k)&\longrightarrow e^-(p')+\gamma(k'),
&p+k&=p'+k',\\
p^2=p'^2&=-m^2,& k^2=k'^2&=0,\\
s&=-(p+k)^2,&t&=-(p-p')^2,\qquad u=-(p-k')^2,\\
s+t+u&=2m^2.
\end{aligned}
\tag{59.41}
$$

为区分两个过程，暂将湮灭的不变量记成$s_{\rm a},t_{\rm a},u_{\rm a}$。
湮灭的矩阵表达式是四动量的有理函数；在保持外线在壳的条件下作代换

<span id="eq:c59-ex-crossing-momenta"></span>

$$
p_1\mapsto p,\qquad p_2\mapsto-p',\qquad
k'_1\mapsto-k,\qquad k'_2\mapsto k'.
\tag{59.42}
$$

原来的守恒式$p_1+p_2=k'_1+k'_2$由此变成$p-p'=-k+k'$，正是康普顿过程
的动量守恒。三个不变量则逐一变为

<span id="eq:c59-ex-crossing-invariants"></span>

$$
\begin{aligned}
s_{\rm a}=-(p_1+p_2)^2&\longmapsto-(p-p')^2=t,\\
t_{\rm a}=-(p_1-k'_1)^2&\longmapsto-(p+k)^2=s,\\
u_{\rm a}=-(p_1-k'_2)^2&\longmapsto-(p-k')^2=u.
\end{aligned}
\tag{59.43}
$$

可见$s,t$的交换来自一条费米外线与一条光子外线同时换到另一边。
在新的物理过程里，两个内部费米动量为$p+k$和$p-k'$。记$r=m^2$，直接沿
第58节的费曼规则读这两幅图，就得到

<span id="eq:c59-ex-compton-matrix"></span>

$$
\begin{aligned}
\mathcal T_{\rm C}
 &=\varepsilon^{\mu *}(k)\varepsilon^\nu(k')
   \bar u(p')B_{\mu\nu}u(p),\\
B_{\mu\nu}
 &=e^2\left[
   \gamma_\nu\frac{-\slashed p-\slashed k+m}{r-s}\gamma_\mu
  +\gamma_\mu\frac{-\slashed p+\slashed k'+m}{r-u}\gamma_\nu
  \right].
\end{aligned}
\tag{59.44}
$$

第一条光子现在入射，依本书的模式展开带$\varepsilon^*(k)$；出光子仍带
$\varepsilon(k')$。矩阵$B$就是前面的$A$经过式[（59.42）](#eq:c59-ex-crossing-momenta)
的动量代换所得的矩阵。将它接到康普顿过程的正能外旋量和偏振上，
便得到所需的物理振幅。

接下来比较两种未极化模方。仍记湮灭结果为$\mathcal A$，康普顿结果记为
$\mathcal C$，并把求和、平均的对象明确写出：

<span id="eq:c59-ex-two-averages"></span>

$$
\begin{aligned}
\mathcal A
 &=\frac14\sum_{s_1,s_2}\sum_{\lambda_1,\lambda_2}
       |\mathcal T_{\rm ann}|^2,\\
\mathcal C
 &=\frac14\sum_{s,\lambda}\sum_{s',\lambda'}
       |\mathcal T_{\rm C}|^2.
\end{aligned}
\tag{59.45}
$$

湮灭初态是两个各有两种自旋的费米子；康普顿初态是一个电子和一个有两种
物理偏振的光子。因此两者的初态平均都为$1/(2\times2)=1/4$，末态则各自
求和。交叉虽然改变了哪些标签属于初态，却没有改变这次平均的总权重。

负号出现在费米子的自旋求和处。原来入射正电子的自旋和是
$Q_2=-\slashed p_2-m$，经过交叉后

<span id="eq:c59-ex-crossed-spin-density"></span>

$$
\begin{aligned}
Q_2\big|_{p_2=-p'}
 &=\slashed p'-m=-P',\\
P'&=\sum_{s'}u_{s'}(p')\bar u_{s'}(p')=-\slashed p'+m,
\qquad P=-\slashed p+m.
\end{aligned}
\tag{59.46}
$$

其余矩阵链仍按原有次序相乘。前面的两图沃德消去只用了动量守恒和外壳
狄拉克方程，经过上述代换后仍成立，故康普顿的入、出物理偏振和也可在完整
幅中用度规替代。用$\bar B=\gamma^0B^\dagger\gamma^0$记狄拉克共轭，有

<span id="eq:c59-ex-crossing-trace-sign"></span>

$$
\begin{aligned}
\mathcal C(s,t,u)
 &=\frac14g^{\mu\rho}g^{\nu\sigma}
   \operatorname{Tr}(B_{\mu\nu}P\bar B_{\rho\sigma}P'),\\
\mathcal A(s_{\rm a},t_{\rm a},u_{\rm a})\big|_{\rm crossing}
 &=\frac14g^{\mu\rho}g^{\nu\sigma}
   \operatorname{Tr}(B_{\mu\nu}P\bar B_{\rho\sigma}[-P'])
 =-\mathcal C(s,t,u).
\end{aligned}
\tag{59.47}
$$

这个负号来自正电子自旋和与交叉后的电子自旋和之差。右边的$\mathcal A(t,s,u)$是原有理函数在
交叉运动学处的值，已离开湮灭的正能物理区域；它不再代表那个区域中的
非负湮灭概率。固定自旋振幅的交叉还涉及外态旋量和相位，而这里的负号
已经由求和后的矩阵$Q_2\mapsto-P'$完全确定。

将[前面合并后的结果](#c59-limits)，即式[（59.35）](#eq:c59-combined-square)，
作$s_{\rm a}\mapsto t$、$t_{\rm a}\mapsto s$、$u_{\rm a}\mapsto u$的代换，
得到完整的康普顿模方

<span id="eq:c59-ex-compton-invariant-square"></span>

$$
\begin{aligned}
\mathcal C(s,t,u)&=-\mathcal A(t,s,u)\\
 &=2e^4\left[
 -\frac{d_s}{d_u}-\frac{d_u}{d_s}
 -4r\left(\frac1{d_s}+\frac1{d_u}\right)
 +4r^2\left(\frac1{d_s}+\frac1{d_u}\right)^2
 \right],\\
d_s&=r-s,\qquad d_u=r-u.
\end{aligned}
\tag{59.48}
$$

对未来向的有质量$p$及非零未来向光子动量，有$p\cdot k<0$、
$p\cdot k'<0$，所以$d_s=2p\cdot k<0$而$d_u=-2p\cdot k'>0$。
两条内部费米子均不在壳，可以按上面的步骤在这些物理点使用实分母。
四项的组合及其非负性，到电子静止系会变得更直观。

### 光子反冲怎样进入模方

取初电子静止系，用$\omega,\omega'>0$表示入、出光子的能量，
$\boldsymbol n,\boldsymbol n'$表示它们的方向：

<span id="eq:c59-ex-rest-frame"></span>

$$
\begin{aligned}
p&=(m,\mathbf0),&k&=(\omega,\omega\boldsymbol n),
&k'&=(\omega',\omega'\boldsymbol n'),\\
c&=\boldsymbol n\cdot\boldsymbol n'=\cos\theta,
&p'&=p+k-k',&E'&=m+\omega-\omega'.
\end{aligned}
\tag{59.49}
$$

末态电子发生反冲。把$p'=p+k-k'$代入
它的外壳条件，利用$p^2=-m^2$及两个光子的零质量，得到

<span id="eq:c59-ex-recoil-shell"></span>

$$
\begin{aligned}
0=p'^2+m^2
 &=2p\cdot(k-k')-2k\cdot k'\\
 &=-2m(\omega-\omega')+2\omega\omega'(1-c).
\end{aligned}
\tag{59.50}
$$

将最后一式除以$2m\omega\omega'$，便有康普顿的能量关系

<span id="eq:c59-ex-compton-energy-shift"></span>

$$
\frac1{\omega'}-\frac1\omega=\frac{1-c}{m},
\qquad
\omega'=\frac{\omega}{1+(\omega/m)(1-c)}.
\tag{59.51}
$$

分母不小于1，故$0<\omega'\le\omega$；只有正前向散射保持原来的光子
能量。这个损失正是电子获得的反冲动能$E'-m$。
在同一参考系，不变量和分母分别成为

<span id="eq:c59-ex-rest-invariants"></span>

$$
\begin{aligned}
s&=r+2m\omega,&u&=r-2m\omega',&
t&=-2\omega\omega'(1-c),\\
d_s&=-2m\omega,&d_u&=2m\omega'.
\end{aligned}
\tag{59.52}
$$

因此式[（59.48）](#eq:c59-ex-compton-invariant-square)中的两个组合可直接化为

<span id="eq:c59-ex-rest-substitution"></span>

$$
\begin{aligned}
\frac{d_s}{d_u}+\frac{d_u}{d_s}
 &=-\frac\omega{\omega'}-\frac{\omega'}\omega,\\
\frac1{d_s}+\frac1{d_u}
 &=\frac1{2m}\left(\frac1{\omega'}-\frac1\omega\right)
 =\frac{1-c}{2r}.
\end{aligned}
\tag{59.53}
$$

前一个组合来自两条内线的能量分母；后一个组合正好由外电子的在壳条件
确定。代入后，两个质量项合成$-2(1-c)+(1-c)^2=c^2-1$，结果为

<span id="eq:c59-ex-klein-nishina-square"></span>

$$
\begin{aligned}
\mathcal C
 &=2e^4\left[\frac\omega{\omega'}+\frac{\omega'}\omega
             -2(1-c)+(1-c)^2\right]\\
 &=2e^4\left[\frac\omega{\omega'}+\frac{\omega'}\omega
             -\sin^2\theta\right].
\end{aligned}
\tag{59.54}
$$

这就是产生克莱因–仁科截面的未极化树级模方。因为正数$\omega'/\omega$
与其倒数之和不小于2，方括号至少为$1+c^2$，结果的非负性现在已经显出。
进一步令$x=\omega/m$，用式[（59.51）](#eq:c59-ex-compton-energy-shift)可把低能
修正也完整留下：

<span id="eq:c59-ex-low-energy-square"></span>

$$
\begin{aligned}
\frac\omega{\omega'}+\frac{\omega'}\omega
 &=2+\frac{x^2(1-c)^2}{1+x(1-c)},\\
\mathcal C
 &=2e^4\left[1+c^2+\frac{x^2(1-c)^2}{1+x(1-c)}\right]\\
 &=2e^4(1+c^2)+O(e^4x^2),\qquad x\to0^+.
\end{aligned}
\tag{59.55}
$$

能量比及其倒数的一阶修正相消，所以模方的第一项反冲修正从$x^2$开始。
这个展开在全角范围$-1\le c\le1$一致成立，因为$0\le x(1-c)\le2x$。
若要得到实际角分布，还须把末态相空间随$\omega'$的变化包括进来。

### 从两体测度得到角分布

沿[第11节的通量归一](/posts/srednicki-11/#c11-flux)，初电子静止时的不变通量因子为
$\mathcal F=|p\cdot k|=m\omega$。末态是一个电子和一个光子，二者可区别，
因此没有相同末态的阶乘。取末光子的立体角为$d\Omega$，有

<span id="eq:c59-ex-compton-phase-space"></span>

$$
\begin{aligned}
d\sigma&=\frac{\mathcal C}{4m\omega}\,d\Phi_2,\\
d\Phi_2&=(2\pi)^4\delta^4(p+k-p'-k')
 \frac{d^3p'}{(2\pi)^3\,2E'}
 \frac{d^3k'}{(2\pi)^3\,2\omega'}.
\end{aligned}
\tag{59.56}
$$

先用三维动量$\delta$积分掉$\mathbf p'$，令剩余光子径向变量为$w>0$。
这时$\mathbf p'=\omega\boldsymbol n-w\boldsymbol n'$，故电子能量以及
能量$\delta$的宗量是

<span id="eq:c59-ex-radial-measure"></span>

$$
\begin{aligned}
E'(w)&=\sqrt{m^2+\omega^2+w^2-2\omega wc},\\
f(w)&=m+\omega-w-E'(w),\\
\frac{d\Phi_2}{d\Omega}
 &=\frac1{16\pi^2}\int_0^\infty dw\,
     \frac{w}{E'(w)}\delta(f(w)).
\end{aligned}
\tag{59.57}
$$

系数来自$(2\pi)^4/(2\pi)^6$与两条测度的$1/4$；$d^3k'=w^2dw\,d\Omega$
再与光子测度中的$1/w$相约，只留下一个$w$。因$m>0$，有
$E'(w)>|w-\omega c|$，所以$f$严格递减，它的正根就是
式[（59.51）](#eq:c59-ex-compton-energy-shift)给出的$w=\omega'$。根处的雅可比为

<span id="eq:c59-ex-energy-delta-jacobian"></span>

$$
\begin{aligned}
f'(w)&=-1-\frac{w-\omega c}{E'(w)}<0,\\
|f'(\omega')|
 &=\frac{E'+\omega'-\omega c}{E'}
  =\frac{m+\omega(1-c)}{E'},\\
\delta(f(w))
 &=\frac{E'}{m+\omega(1-c)}\delta(w-\omega').
\end{aligned}
\tag{59.58}
$$

第二行用了根处的能量守恒$E'+\omega'=m+\omega$。把这个因子代回径向
积分，并再次使用$m+\omega(1-c)=m\omega/\omega'$，得到

<span id="eq:c59-ex-evaluated-phase-space"></span>

$$
\frac{d\Phi_2}{d\Omega}
 =\frac1{16\pi^2}\frac{\omega'}{m+\omega(1-c)}
 =\frac{\omega'^2}{16\pi^2m\omega}.
\tag{59.59}
$$

现在通量与相空间的来源都已明确。用$\alpha_{\rm em}=e^2/(4\pi)>0$，
最终得到克莱因–仁科微分截面

<span id="eq:c59-ex-klein-nishina-cross-section"></span>

$$
\begin{aligned}
\frac{d\sigma}{d\Omega}
 &=\frac{\mathcal C}{64\pi^2m^2}
    \left(\frac{\omega'}\omega\right)^2\\
 &=\frac{\alpha_{\rm em}^2}{2m^2}
    \left(\frac{\omega'}\omega\right)^2
    \left[\frac\omega{\omega'}+\frac{\omega'}\omega-\sin^2\theta\right].
\end{aligned}
\tag{59.60}
$$

截面的质量维数为$-2$；前面的能量比来自末态测度和能量守恒的雅可比。
它使截面在$x=\omega/m$的一阶就感受到反冲，尽管模方本身的一阶项已相消：

<span id="eq:c59-ex-thomson-angular-limit"></span>

$$
\frac{d\sigma}{d\Omega}
 =\frac{\alpha_{\rm em}^2}{2m^2}(1+c^2)
   \left[1-2x(1-c)+O(x^2)\right],\qquad x\to0^+.
\tag{59.61}
$$

零阶项就是汤姆孙角分布。由于这里的低能展开对全角一致，可以将领先项
直接积分；方位角给$2\pi$，余下的多项式积分给出有限总截面

<span id="eq:c59-ex-thomson-total"></span>

$$
\begin{aligned}
\sigma_{\mathrm{Th}}
 &=\frac{\alpha_{\rm em}^2}{2m^2}\,2\pi\int_{-1}^1dc\,(1+c^2)\\
 &=\frac{\alpha_{\rm em}^2}{2m^2}\,2\pi\left(2+\frac23\right)
 =\frac{8\pi\alpha_{\rm em}^2}{3m^2}.
\end{aligned}
\tag{59.62}
$$

低能光子主要改变方向，反冲能量占入射光子能量的比例趋于零，因而恢复这一
只由电荷和电子质量决定的散射尺度。较高能量时，式[（59.51）](#eq:c59-ex-compton-energy-shift)
给出的能量损失同时改变模方和可用末态相空间，两者合在一起才是完整的角分布。

下一节回到高能情形，直接组织各个螺旋度的振幅。

---

[← 第 58 节](/posts/srednicki-58/) · [章节地图](/srednicki/) · [第 60 节 →](/posts/srednicki-60/)
