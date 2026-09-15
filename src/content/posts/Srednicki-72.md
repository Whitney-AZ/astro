---
title: 'Srednicki §72 非阿贝尔规范理论的费曼规则'
date: 2026-09-14
category: 笔记
tags: [物理, 量子场论, Srednicki]
series: 'Srednicki QFT'
srednickiSections: [72]
hideFromHome: true
draft: false
---

<span id="c72"></span>

上一节已经把规范固定后的路径积分写成局域作用量的形式。
现在只需把各场的二次项求逆，再将相互作用中的场与外腿逐一对应，
就能得到费曼规则。与电动力学相比，新内容首先出现在规范场本身：
场强中的$AA$项使三个、四个规范场可以直接相互作用。
密度中的同类场都能同任一相应外腿收缩，求顶角时必须把这些分配全部计入。
这也是本节许多动量差、度规配对和结构系数的来源。

先讨论纯规范场，再依次加入鬼场、夸克和复标量。三胶子顶角的动量全部取为流出；将三个动量同时反号，就得到上一节的全入顶记法。

<span id="c72-propagator"></span>

## 从场强平方到自由传播子

先将场强的两部分分开，记

<span id="eq:c72-field-strength-parts"></span>

$$
\begin{aligned}
F_{0\,\mu\nu}^e&=\partial_\mu A_\nu^e-\partial_\nu A_\mu^e,
&G_{\mu\nu}^e&=gf^{abe}A_\mu^aA_\nu^b,\\
F^e_{\mu\nu}&=F_{0\,\mu\nu}^e+G_{\mu\nu}^e .
\end{aligned}
\tag{72.1}
$$

$G_{\nu\mu}^e=-G_{\mu\nu}^e$，因为交换两个普通场以后，
$f^{abe}$交换$a,b$就变号。因此场强平方的交叉项有两个相等的贡献：

<span id="eq:c72-action-expansion"></span>

$$
\begin{aligned}
\mathcal L_{\rm YM}
&=-\frac14F_0^{e\mu\nu}F_{0\,\mu\nu}^e
  -\frac12F_0^{e\mu\nu}G_{\mu\nu}^e
  -\frac14G^{e\mu\nu}G_{\mu\nu}^e\\
&=-\frac12\partial^\mu A^{e\nu}\partial_\mu A_\nu^e
  +\frac12\partial^\mu A^{e\nu}\partial_\nu A_\mu^e\\
&\quad-gf^{abc}A_\mu^aA_\nu^b\partial^\mu A^{c\nu}
  -\frac{g^2}{4}f^{abe}f^{cde}
    A_\mu^aA_\nu^bA^{c\mu}A^{d\nu}.
\end{aligned}
\tag{72.2}
$$

具体地，$F_0G$中的第二个导数项在交换$\mu,\nu$后，
由$G$的反对称性变成第一个，所以抵消了前面的$1/2$。
$F_0^2$的两个平方项和两个交叉项也分别相等。
三次和四次相互作用的号因而与第69节的场强定义一致。

再加上上一节导出的
$\mathcal L_{\rm gf}=-(\partial\cdot A^e)^2/(2\xi)$。
为求自由核，将所有二次项中的一个导数移到右方的场上。
若把总散度也保留，结果是

<span id="eq:c72-quadratic-boundary"></span>

$$
\begin{aligned}
\mathcal L_2
&=\frac12 A_\mu^e
\left[g^{\mu\nu}\partial^2
 -(1-\xi^{-1})\partial^\mu\partial^\nu\right]A_\nu^e
+\partial_\mu B^\mu,\\
B^\mu
&=-\frac12 A_\nu^e\partial^\mu A^{e\nu}
  +\frac12 A_\nu^e\partial^\nu A^{e\mu}
  -\frac1{2\xi}A^{e\mu}\partial^\nu A_\nu^e .
\end{aligned}
\tag{72.3}
$$

对$B^\mu$求导即可将每个乘积还原为原来的两导数形式。
取使其边界积分消失的共同条件，便可将二次项写成一个场乘微分核再乘一个场；
三、四次项保持式[（72.2）](#eq:c72-action-expansion)的形式。

对场作$e^{ikx}$展开，二次作用量为

<span id="eq:c72-momentum-kernel"></span>

$$
\begin{aligned}
S_2&=\frac12\int\frac{d^4k}{(2\pi)^4}\,
A_\mu^a(-k)K^{\mu\nu}(k)A_\nu^a(k),\\
K^{\mu\nu}(k)
&=-k^2g^{\mu\nu}+(1-\xi^{-1})k^\mu k^\nu .
\end{aligned}
\tag{72.4}
$$

在$k^2\ne0$时，用[第57节的投影](/posts/srednicki-57/#c57-projector)
$P_L{}^\mu{}_\nu=k^\mu k_\nu/k^2$和$P_T=I-P_L$。
它们平方等于自身、乘积为零，因此

<span id="eq:c72-projector-inverse"></span>

$$
K=-k^2P_T-\frac{k^2}{\xi}P_L,
\qquad
K^{-1}=-\frac{P_T+\xi P_L}{k^2}.
\tag{72.5}
$$

高斯积分的相关函数为$iK^{-1}$，将其$i$倍定义为传播子$\Delta$，
所以$\widetilde\Delta=-K^{-1}$。颜色空间的核是单位矩阵，
求逆只留下$\delta^{ab}$，不会多出一个伴随表示的维数。

要将逆核用于动量积分，还须定义其光锥奇性，尤其要把纵向双极点定义为同侧费曼边界。
例如先取$\xi>0$、$\eta>0$，在混合指标核中令$K_\eta=K+i\eta I$，
则

<span id="eq:c72-regulated-inverse"></span>

$$
\begin{aligned}
-K_\eta^{-1}
&=\frac{P_T}{k^2-i\eta}
  +\frac{\xi P_L}{k^2-i\xi\eta},\\
(-K_\eta^{-1})_{\mu\nu}
&=\frac{g_{\mu\nu}}{k^2-i\eta}
 +\frac{(\xi-1)k_\mu k_\nu}
 {(k^2-i\eta)(k^2-i\xi\eta)} .
\end{aligned}
\tag{72.6}
$$

从第一行到第二行，$k_\mu k_\nu/k^2$的系数通分后，
分子为$\xi(k^2-i\eta)-(k^2-i\xi\eta)=(\xi-1)k^2$；
正好约去投影里的$k^2$。两个分母取同侧极限可以写成

<span id="eq:c72-common-boundary"></span>

$$
\begin{aligned}
\int_0^1\frac{du}{[s-i\eta(1-u+u\xi)]^2}
&=\frac1{i\eta(\xi-1)}
  \left[\frac1{s-i\xi\eta}-\frac1{s-i\eta}\right]\\
&=\frac1{(s-i\eta)(s-i\xi\eta)}
\ \longrightarrow\ \frac1{(s-i0)^2}.
\end{aligned}
\tag{72.7}
$$

第一行在$\xi\ne1$时按端点求值；$\xi=1$时被积函数与$u$无关，直接得到同一结果。
固定$\xi>0$时$1-u+u\xi$始终为正，极限采用第57节已经说明的
[标量边界值及其导数](/posts/srednicki-57/#c57-boundary)。
因此包含完整边界处方的传播子为

<span id="eq:c72-gluon-propagator"></span>

$$
\begin{aligned}
\widetilde\Delta^{ab}_{\mu\nu}(k)
&=\delta^{ab}\left[
\frac{g_{\mu\nu}}{k^2-i0}
+(\xi-1)\frac{k_\mu k_\nu}{(k^2-i0)^2}\right],\\
\langle T A_\mu^a A_\nu^b\rangle_0(k)
&=\frac1i\,\widetilde\Delta^{ab}_{\mu\nu}(k).
\end{aligned}
\tag{72.8}
$$

$\xi=1$是费曼规范，只剩度规项；在已确定的边界值后取$\xi\to0$
得到朗道规范。这里的$\eta$具有质量平方量纲，表示真空极点处方，
并非维数正规化中的参数。三次和四次项不含$\xi$，下面直接求它们的顶角。

<span id="c72-three"></span>

## 三胶子顶角的六种分配

[下图](#fig:c72-gluon-vertices)左边画出三胶子顶角。
每条腿带颜色、洛伦兹指标和动量，分别为$(a,\mu,p)$、$(b,\nu,q)$、
$(c,\rho,r)$。全部动量流出，局部波因子因而是$e^{-ipx}$等，
时空积分给出$(2\pi)^4\delta^4(p+q+r)$。
以下顶角因子省去这个共同的动量δ函数。

三次密度是$-gf^{ABC}A_\alpha^AA_\beta^B\partial^\alpha A^{C\beta}$。
先把三条有标签外腿按$a,b,c$依次放到三个场的位置。
第三个场被微分，给$-ir$；乘上展开$e^{iS_{\rm int}}$的$i$，这一项为

<span id="eq:c72-three-seed"></span>

$$
i(-gf^{abc})(-ir_\mu g_{\nu\rho})
=-gf^{abc}r_\mu g_{\nu\rho}.
\tag{72.9}
$$

还有五种分配。将共同的$gf^{abc}$提出，六项分别为

| 第一、第二、第三个场所接的外腿 | 剩余因子             |
| ------------------------------ | -------------------- |
| $a,b,c$                        | $-r_\mu g_{\nu\rho}$ |
| $a,c,b$                        | $+q_\mu g_{\nu\rho}$ |
| $b,a,c$                        | $+r_\nu g_{\rho\mu}$ |
| $b,c,a$                        | $-p_\nu g_{\rho\mu}$ |
| $c,a,b$                        | $-q_\rho g_{\mu\nu}$ |
| $c,b,a$                        | $+p_\rho g_{\mu\nu}$ |

每次置换同时带动颜色、洛伦兹指标和动量；奇置换使结构系数反号。
将含相同度规的两项合并，得到

<span id="eq:c72-three-vertex"></span>

$$
\begin{aligned}
iV_{\mu\nu\rho}^{abc}(p,q,r)
&=gf^{abc}\mathcal K_{\mu\nu\rho}(p,q,r),\\
\mathcal K_{\mu\nu\rho}(p,q,r)
&=(q-r)_\mu g_{\nu\rho}
 +(r-p)_\nu g_{\rho\mu}
 +(p-q)_\rho g_{\mu\nu}.
\end{aligned}
\tag{72.10}
$$

密度中没有$1/3!$，六种收缩已经全数计入，不能再除以6。
同时交换任意两条完整外腿时，$f$和$\mathcal K$各反号，
乘积保持不变，正是同类玻色场所需的置换对称性。
若改用上一节的全入顶动量$p_1,p_2,p_3$，
取$p=-p_1,q=-p_2,r=-p_3$，便有
$iV_{\rm in}=-gf^{abc}\mathcal K(p_1,p_2,p_3)$。
这个共同号来自动量方向的改变。

还可作一个有用的解析检验。用$p+q+r=0$缩并第一条腿，
并把新出现的$p$换成$-q-r$，则

<span id="eq:c72-three-contraction"></span>

$$
\begin{aligned}
p^\mu\mathcal K_{\mu\nu\rho}
&=p\cdot(q-r)\,g_{\nu\rho}
 +(r-p)_\nu p_\rho+(p-q)_\rho p_\nu\\
&=(r^2-q^2)g_{\nu\rho}+q_\nu q_\rho-r_\nu r_\rho\\
&=H_{\nu\rho}(r)-H_{\nu\rho}(q),\\
H_{\nu\rho}(k)&:=k^2g_{\nu\rho}-k_\nu k_\rho.
\end{aligned}
\tag{72.11}
$$

第二行的交叉张量$q_\nu r_\rho,r_\nu q_\rho$各自相消。
$H$正是未加规范固定项时的自由逆核的负值。
这样，一个外动量的缩并把三点结构化为两条邻接线的逆核之差，
可用来检查动量差的符号和位置。

<span id="c72-four"></span>

## 四胶子顶角的二十四个收缩

四次密度中的每个场都可以接到四条有标签外腿中的任何一条。
先不合并相同项，完全微分得到

<span id="eq:c72-four-full-permutations"></span>

$$
\begin{aligned}
iV_4
&=-\frac{ig^2}{4}\sum_{\pi\in S_4}
Q\bigl(\pi(1),\pi(2),\pi(3),\pi(4)\bigr),\\
Q(1,2,3,4)
&:=f^{a_1a_2e}f^{a_3a_4e}
  g_{\mu_1\mu_3}g_{\mu_2\mu_4}.
\end{aligned}
\tag{72.12}
$$

每一项表示外腿到四个场位置的一种分配，共有$4!=24$项。
四次密度中的$1/4$尚未被消去。现在观察$Q$在下列四种位置置换下的变化：

<span id="eq:c72-four-stabilizer"></span>

$$
H=\{1,\ (12)(34),\ (13)(24),\ (14)(23)\}.
\tag{72.13}
$$

$(12)(34)$使两个结构系数分别变号，两个度规只交换位置；
$(13)(24)$交换两份结构系数，同时反转对称度规的两个指标。
这两种操作都使$Q$不变，第四种又是它们的复合。
四个操作恰把指定的外腿$a$送到四个不同位置，所以24种分配可分成六组，
每组四项相等，并且恰有一项把$a$放在第一位置。
这四项消去$1/4$，余下的是$b,c,d$的六种排列。
即使外腿的颜色数值偶然相同，这个按外腿身份进行的计数仍然成立。

将外腿依次标为$(a,\mu),(b,\nu),(c,\rho),(d,\sigma)$，
提出共同的$-ig^2$后，六项为

<span id="eq:c72-four-six-terms"></span>

$$
\begin{aligned}
\frac{iV_4}{-ig^2}
={}&f^{abe}f^{cde}g_{\mu\rho}g_{\nu\sigma}
-f^{abe}f^{cde}g_{\mu\sigma}g_{\nu\rho}\\
&+f^{ace}f^{bde}g_{\mu\nu}g_{\rho\sigma}
+f^{ace}f^{dbe}g_{\mu\sigma}g_{\rho\nu}\\
&+f^{ade}f^{bce}g_{\mu\nu}g_{\sigma\rho}
-f^{ade}f^{bce}g_{\mu\rho}g_{\sigma\nu}.
\end{aligned}
\tag{72.14}
$$

第二行用$f^{bde}=-f^{dbe}$，各行就能按共同颜色因子合并，得到

<span id="eq:c72-four-vertex"></span>

$$
\begin{aligned}
iV_{\mu\nu\rho\sigma}^{abcd}
=-ig^2\Big[&
f^{abe}f^{cde}(g_{\mu\rho}g_{\nu\sigma}-g_{\mu\sigma}g_{\nu\rho})\\
&+f^{ace}f^{dbe}(g_{\mu\sigma}g_{\rho\nu}-g_{\mu\nu}g_{\rho\sigma})\\
&+f^{ade}f^{bce}(g_{\mu\nu}g_{\sigma\rho}-g_{\mu\rho}g_{\sigma\nu})
\Big].
\end{aligned}
\tag{72.15}
$$

这里没有导数，因而无需指定动量字母。全置换求和的出发式还表明，
同时交换任意两条完整外腿都不改变结果。
上式已包含该顶点的全部场收缩，不再附加$1/4!$。
整幅图的对称因子仍按[第9节的计数](/posts/srednicki-09/#c09)处理；
顶角中两个张量项的数值相等不会另添一个图对称因子。

![三胶子与四胶子顶角的颜色、洛伦兹指标及流出动量](/images/srednicki/s72_gluon_vertices.svg)

三、四胶子顶角。
波线旁的箭头仅表示流出顶点的动量。左图三个外端的颜色、洛伦兹指标和动量
须同时置换；右图的因子不依赖动量，所以只标颜色和洛伦兹指标。

<span id="fig:c72-gluon-vertices"></span>

这些规则已经能用来计算$gg\to gg$的树幅。固定四条外腿，有三个交换道和一个
四点接触图。直接展开其模方会产生大量中间项。
在费曼规范下，每条内部胶子传播子只含一个度规张量，
如果三点顶角保留表中的六项、四点顶角保留六项，那么

<span id="eq:c72-raw-term-count"></span>

$$
N_{\rm amplitude}=3\times6^2+6=114,
\qquad
N_{\rm square}=114^2=12996.
\tag{72.16}
$$

模方中的每一项都还要作极化和颜色缩并。许多项可以合并，
而且如果先把三点顶角写成三个动量差，幅的外观上就只剩$3\times3^2+6=33$项。
所以这个大数反映的是展开的组织方式。[第81节](/posts/srednicki-81/#c81)将计算完整树散射，
届时将结合色排序、Gervais–Neveu规范和旋量—螺旋度方法减少中间项。
本节继续准备圈计算还需要的规则。

<span id="c72-ghost"></span>

## 鬼线的箭头与导数顶角

对规范场作圈展开时，上一节产生的鬼行列式也必须展开。
将第71节的颜色指标循环改名为下面的次序，并保持$\bar c$在$c$之前，得到

<span id="eq:c72-ghost-density"></span>

$$
\begin{aligned}
\mathcal L_{\rm gh}
&=-(\partial^\mu\bar c^b)
\left(\delta^{bc}\partial_\mu-igA_\mu^a(T_A^a)^{bc}\right)c^c\\
&=-\partial^\mu\bar c^b\partial_\mu c^b
+gf^{abc}A_\mu^a(\partial^\mu\bar c^b)c^c .
\end{aligned}
\tag{72.17}
$$

第二行用$(T_A^a)^{bc}=-if^{abc}$；原密度中的$+ig$乘上$-i$给$+g$。
这只是上一节作用量的指标改名，没有交换两个奇场。
自由核及实际内线分别为

<span id="eq:c72-ghost-line"></span>

$$
\widetilde\Delta_{\rm gh}^{bc}(k)
=\frac{\delta^{bc}}{k^2-i0},
\qquad
\langle c^b\bar c^c\rangle_0(k)
=\frac1i\,\widetilde\Delta_{\rm gh}^{bc}(k).
\tag{72.18}
$$

传播核$\widetilde\Delta$与实际内线相差$1/i$。
在坐标核$\langle c(x)\bar c(y)\rangle$中，箭头从$y$端指向$x$端；
因此接到顶点上的$c$腿箭头流入，$\bar c$腿箭头流出。
这条箭头区分两个独立奇变量的配对方向。

[下图](#fig:c72-matter-vertices)左边标出鬼顶角：
左侧$c$端的动量$r$流入，右侧$\bar c$端的$q$流出，
胶子若取入射动量$k$，则$k+r-q=0$。
局部$\bar c$波因子是$e^{-iqx}$，其导数给$-iq_\mu$。
因此顶角为

<span id="eq:c72-ghost-vertex"></span>

$$
iV_\mu^{abc}(q,r)
=i(gf^{abc})(-iq_\mu)
=gf^{abc}q_\mu .
\tag{72.19}
$$

从上一节全入顶的$-gf^{abc}\ell_\mu$出发，
代入$\ell=-q$也得到同一结果。顶角只含$q$，
因为被微分的是$\bar c$，不是$c$。
每个封闭鬼圈还须乘上上一节已由行列式证明的$-1$。
反转整条鬼线会同时交换$c,\bar c$并改变被微分的端点，
所以不能把它当作无向线再除以2。

<span id="c72-quark"></span>

## 加入夸克和其它物质表示

若加入一个狄拉克夸克，规范场在它的色空间中作用。
沿$D_\mu=\partial_\mu-igA_\mu^aT^a$，有

<span id="eq:c72-quark-density"></span>

$$
\begin{aligned}
\mathcal L_q
&=i\bar\Psi_i\gamma^\mu D_{\mu\,ij}\Psi_j-m\bar\Psi_i\Psi_i\\
&=i\bar\Psi_i\gamma^\mu\partial_\mu\Psi_i-m\bar\Psi_i\Psi_i
+gA_\mu^a\bar\Psi_i\gamma^\mu T^a_{ij}\Psi_j .
\end{aligned}
\tag{72.20}
$$

相互作用的正号仍来自$i(-i)=1$。自由部分在色空间正比于单位阵。
对$\Psi$作$e^{ipx}$展开，二次作用量写成
$-\bar\Psi(\not p+m)\Psi$。所采用的克利福德关系为
$\{\gamma^\mu,\gamma^\nu\}=-2g^{\mu\nu}$，所以

<span id="eq:c72-quark-propagator"></span>

$$
\begin{aligned}
(\not p)^2
&=\frac12p_\mu p_\nu\{\gamma^\mu,\gamma^\nu\}
=-p^2I,\\
(\not p+m)(-\not p+m)
&=(p^2+m^2)I,\\
\widetilde S_{ij}(p)
&=\frac{(-\not p+m)\delta_{ij}}{p^2+m^2-i0}.
\end{aligned}
\tag{72.21}
$$

这与[自由狄拉克传播子](/posts/srednicki-42/#c42-inverse)相同，
实际有向内线为$\widetilde S/i$。颜色单位阵只把线两端的颜色相接；
闭夸克圈时才对经过的整串色矩阵取迹。

相互作用中只有一个$\bar\Psi$、一个$\Psi$和一个$A$，
三者各有固定作用，直接乘上指数展开的$i$即可得到顶角：

<span id="eq:c72-quark-vertex"></span>

$$
iV_{ij}^{\mu a}=ig\gamma^\mu T^a_{ij}.
\tag{72.22}
$$

[下图](#fig:c72-matter-vertices)右边的箭头从左侧$j$流向右侧$i$，
所以生成元是行$i$、列$j$。沿一条线先经过颜色$a_1$的顶点，
再经过$a_2$，颜色乘积为
$(T^{a_2})_{i\ell}(T^{a_1})_{\ell j}=(T^{a_2}T^{a_1})_{ij}$。
这两个色矩阵一般不能交换。$\gamma^\mu$则作用于旋量空间，
与色矩阵作用于不同的因子，可以彼此交换。

![鬼线和夸克线的有向顶角：反鬼动量q流出、色矩阵行i列j](/images/srednicki/s72_matter_vertices.svg)

有向鬼线和夸克线的顶角。
左图点线区分$c,\bar c$的配对，$r$入顶、$q$出顶；
右图实线的方向规定生成元的行$i$与列$j$。下方波线均为颜色$a$、
洛伦兹指标$\mu$的规范场。

<span id="fig:c72-matter-vertices"></span>

如果物质属于其它表示$R$，保持同一规范群的结构系数和耦合，
把每个$T^a$换成$T_R^a$即可。自由传播核的单位阵也换成该表示空间的单位阵。
各表示的迹指标保留其自身取值。
在四维中，三胶子和鬼顶角各含一个动量，四胶子顶角没有动量，
夸克—胶子顶角也没有额外导数；它们分别与各密度的质量维数4相符。
再加入复标量，就得到另一组在后面的圈计算中会用到的物质顶角。

<span id="c72-scalar"></span>

## 复标量的规范顶角

取表示$R$中的复标量场，其规范化的最小动能和共同质量项为
<span id="eq:c72-ex-minimal-lagrangian"></span>

$$
\begin{aligned}
\mathcal L_\varphi
&=-(D_\mu\varphi)^\dagger D^\mu\varphi
  -m^2\varphi^\dagger\varphi,\\
D_\mu&=\partial_\mu-igA_\mu^aT_R^a,\qquad
(T_R^a)^\dagger=T_R^a,\qquad
[T_R^a,T_R^b]=if^{abc}T_R^c .
\end{aligned}
\tag{72.23}
$$

在$m^2\ge0$的零场真空附近展开。若再指定一个规范不变势，其纯标量顶角应由那个势另行展开。这里$\varphi$的各分量是复玻色场，即使$R$碰巧是实表示，也不对$\varphi$施加实条件。四维下$[\varphi]=[A_\mu]=1$、$[g]=0$，度规仍为$(-,+,+,+)$。

先展开协变导数。由于生成元厄米，取共轭时既要改变$i$的符号，也要倒转矩阵作用的方向：
<span id="eq:c72-ex-conjugate-derivative"></span>

$$
(D_\mu\varphi)^\dagger
=\partial_\mu\varphi^\dagger
 +igA_\mu^a\varphi^\dagger T_R^a .
\tag{72.24}
$$

两因子相乘，再乘上动能前的负号，就得到
<span id="eq:c72-ex-expanded-interactions"></span>

$$
\begin{aligned}
\mathcal L_\varphi&=\mathcal L_0+\mathcal L_3+\mathcal L_4,\\
\mathcal L_0&=-\partial_\mu\varphi^\dagger
                 \partial^\mu\varphi-m^2\varphi^\dagger\varphi,\\
\mathcal L_3&=igA^{a\mu}
 \left[(\partial_\mu\varphi^\dagger)T_R^a\varphi
       -\varphi^\dagger T_R^a\partial_\mu\varphi\right],\\
\mathcal L_4&=-g^2 A^{a\mu}A_\mu^b
                    \varphi^\dagger T_R^aT_R^b\varphi .
\end{aligned}
\tag{72.25}
$$

一次$A$的两项互为厄米共轭；二次$A$的项取共轭后把$a,b$重新命名，也回到同一相互作用项。四次项中的$T_R^aT_R^b$按这一顺序作用于标量的内部指标。

### 一个胶子的顶角

从全入动量约定出发最容易确定导数的符号。对每个场都使用
<span id="eq:c72-ex-fourier"></span>

$$
\chi(x)=\int\frac{d^4k}{(2\pi)^4}\,
                  e^{ikx}\widetilde\chi(k),\qquad
\partial_\mu\chi(x)\longleftrightarrow
                  ik_\mu\widetilde\chi(k).
\tag{72.26}
$$

在三价顶角上，$\varphi_j$、$\varphi_i^\dagger$和$A^{a\mu}$的入动量分别记为$p,r,k$。其中$\widetilde{\varphi^\dagger}(r)=\widetilde\varphi(-r)^\dagger$；给共轭场也取$e^{irx}$，并不改变共轭关系。时空积分给出动量守恒，而两处导数分别给出$ir_\mu$和$ip_\mu$：
<span id="eq:c72-ex-three-fourier-coefficient"></span>

$$
\begin{aligned}
\int d^4x\,e^{i(p+r+k)x}
   &=(2\pi)^4\delta^4(p+r+k),\\
ig\left(ir_\mu-ip_\mu\right)(T_R^a)_{ij}
   &=g(p-r)_\mu(T_R^a)_{ij}.
\end{aligned}
\tag{72.27}
$$

第二行是作用量中的系数。微扰展开来自$e^{iS_{\rm int}}$，所以顶角还要乘一个$i$。去掉每个顶角共同的动量守恒$\delta$函数后，规则为
<span id="eq:c72-ex-three-all-in"></span>

$$
iV_{\mu,ij}^{\,a}(p,r)
 =ig(p-r)_\mu(T_R^a)_{ij},
\qquad p+r+k=0 .
\tag{72.28}
$$

此处洛伦兹指标取下标，所连接的规范场为$A^{a\mu}$。这样与第61节标量电动力学的顶角指标一致。

也可以沿标量线的箭头标动量。把进入顶角的箭头动量记作$p$、色指标记作$j$，离开顶角的箭头动量记作$q$、色指标记作$i$。于是共轭场的全入动量为$r=-q$，胶子带入动量$k=q-p$，顶角变成
<span id="eq:c72-ex-three-arrow"></span>

$$
iV_{\mu,ij}^{\,a}(p\to q)
=ig(p+q)_\mu(T_R^a)_{ij},
\qquad p+k=q .
\tag{72.29}
$$

矩阵的列$j$对应入箭头，行$i$对应出箭头，与[夸克顶角](#eq:c72-quark-vertex)的有向色线次序相同。箭头延续自由收缩$\langle{\rm T}\varphi_i(x)\varphi_j^\dagger(y)\rangle$从$y$到$x$的方向，其内线因子为$-i\delta_{ij}/(p^2+m^2-i0)$。粒子和反粒子的图都可用这条连续箭头规则；对于反粒子，箭头方向与正能物理动量方向相反。

用胶子动量缩并还能检查导数顶角。收缩胶子动量$k=q-p$，得到
<span id="eq:c72-ex-three-difference"></span>

$$
k^\mu iV_{\mu,ij}^{\,a}
=ig\left[(q^2+m^2)-(p^2+m^2)\right](T_R^a)_{ij}.
\tag{72.30}
$$

质量项相消，留下两端自由逆核之差。它同时检查了$p+q$的相对号和全入动量到箭头动量的转换。

### 两个胶子的接触顶角

现在给两条胶子腿分别标上$(a,\mu,k)$与$(b,\nu,l)$。在$\mathcal L_4$中暂用$c,d$作求和指标，先看两次对规范场求导的结果：
<span id="eq:c72-ex-two-gluon-assignments"></span>

$$
\frac{\partial^2\bigl(A^{c\rho}A_\rho^d\bigr)}
     {\partial A^{a\mu}\,\partial A^{b\nu}}
=g_{\mu\nu}
  \left(\delta^{ca}\delta^{db}
       +\delta^{cb}\delta^{da}\right).
\tag{72.31}
$$

两项分别把外腿$a,b$接到拉格朗日量的第一、第二个规范场，以及接到第二、第一个规范场。因此它们给出的色矩阵分别为$T_R^aT_R^b$和$T_R^bT_R^a$。再取出$\varphi_j$与$\varphi_i^\dagger$的系数，并乘上展开作用量的$i$，得到
<span id="eq:c72-ex-four-vertex"></span>

$$
\begin{aligned}
iV_{\mu\nu,ij}^{\,ab}
&=-ig^2g_{\mu\nu}
       \left(T_R^aT_R^b+T_R^bT_R^a\right)_{ij}\\
&=-ig^2g_{\mu\nu}\{T_R^a,T_R^b\}_{ij}.
\end{aligned}
\tag{72.32}
$$

这个顶角不含外动量。若仍用标量箭头入$p$、出$q$，动量守恒为$p+k+l=q$；若把共轭标量也改记为全入$r$，则为$p+r+k+l=0$。

两胶子的$2!$已经体现在这两种接法中，不能再乘一次。反过来，也可先用规范场分量的可交换性，把作用量写为
<span id="eq:c72-ex-four-symmetrized-action"></span>

$$
\mathcal L_4
=-\frac{g^2}{2}A^{a\mu}A_\mu^b
                     \varphi^\dagger\{T_R^a,T_R^b\}\varphi .
\tag{72.33}
$$

此时两次求导的$2!$消掉显式的$1/2$，仍得到同一规则。$\varphi$与$\varphi^\dagger$是两种不同的场插槽，并没有另一个标量$2!$。交换两条带标签的胶子腿$(a,\mu,k)\leftrightarrow(b,\nu,l)$时，顶角保持不变，正是所需的玻色对称性。

### 荷号与有序色矩阵

在阿贝尔极限中，把表示限制到一个电荷本征空间，令生成元为数$t$，并作转换$gt=e$。于是这里的协变导数和规范相位变成
<span id="eq:c72-ex-abelian-convention"></span>

$$
D_\mu=\partial_\mu-ieA_\mu,\qquad
\varphi\longmapsto e^{-ie\Gamma}\varphi,\qquad
A_\mu\longmapsto A_\mu-\partial_\mu\Gamma .
\tag{72.34}
$$

这正是[第61节的约定](/posts/srednicki-61/#c61-gauge)，其中$e<0$。若选择$g>0$，相应的$t=e/g$就为负；不能把$gt$换成$|e|$而保留同一粒子荷号。三价和四价规则分别成为
<span id="eq:c72-ex-abelian-vertices"></span>

$$
iV_\mu=ie(p+q)_\mu,\qquad
iV_{\mu\nu}=-2ie^2g_{\mu\nu}.
\tag{72.35}
$$

二式中的$2$来自$\{t,t\}=2t^2$，而不是非阿贝尔色指标求和。若把反粒子也改画成沿其正能物理动量的线，它属于共轭表示，生成元为$T_{\overline R}^a=-(T_R^a)^T$；这等价于原箭头规则中的反向有号动量及转置的色指标，不应同时再加一个独立的电荷负号。

为检验非交换情形，取$SU(2)$基本表示，
<span id="eq:c72-ex-su2-generators"></span>

$$
T^1=\frac12\begin{pmatrix}0&1\\1&0\end{pmatrix},
\qquad
T^2=\frac12\begin{pmatrix}0&-i\\i&0\end{pmatrix},
\qquad
T^3=\frac12\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
\tag{72.36}
$$

直接相乘给出
<span id="eq:c72-ex-su2-products"></span>

$$
\begin{aligned}
T^1T^2&=\frac14\begin{pmatrix}i&0\\0&-i\end{pmatrix}
       =\frac{i}{2}T^3,\\
T^2T^1&=-\frac{i}{2}T^3,\qquad
\{T^1,T^2\}=0,\qquad
\{T^1,T^1\}=\frac12\mathbf1_2 .
\end{aligned}
\tag{72.37}
$$

因此颜色为$1,2$的两胶子在同一个标量接触顶角上的贡献为零，尽管每个有序乘积都不为零；两条颜色均为$1$时则有$iV_{\mu\nu}^{11}=-ig^2g_{\mu\nu}\mathbf1_2/2$。这两种情形分别检查了两个有序项的相消以及同色腿的重数。

若两胶子接在标量线上两个不同的三价顶角，情形就不同了。沿箭头先遇到颜色$a$、再遇到颜色$b$，中间色指标求和给出
<span id="eq:c72-ex-ordered-color-chain"></span>

$$
\sum_h(T_R^b)_{ih}(T_R^a)_{hj}
       =(T_R^bT_R^a)_{ij}.
\tag{72.38}
$$

颠倒两个顶角后色因子为$T_R^aT_R^b$，两者之差是$-if^{abc}T_R^c$。它们还分别带有各自的中间传播子和动量因子。接触顶角中的反对易子来自同一个局部相互作用上两条玻色腿的接法；沿一条有向色线连接不同顶角时，仍须按箭头次序相乘。由最小动能产生的标量相互作用至此只有一胶子的导数顶角和两胶子的接触顶角，因为每个协变导数至多含一次规范场。

下一节将用这些规范场与物质顶角计算非阿贝尔耦合的尺度变化。

---

[← 第 71 节](/posts/srednicki-71/) · [章节地图](/srednicki/) · [第 73 节 →](/posts/srednicki-73/)
