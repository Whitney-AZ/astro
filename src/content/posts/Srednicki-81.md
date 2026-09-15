---
title: 'Srednicki §81 量子色动力学中的散射'
date: 2026-09-14
category: 笔记
tags: [物理, 量子场论, Srednicki]
series: 'Srednicki QFT'
srednickiSections: [81]
hideFromHome: true
draft: false
---

<span id="c81"></span>

现在可以把前两节的方法用于胶子的实际散射。矩阵场的双线规则先处理颜色，Gervais–Neveu规范再减少每个顶角的洛伦兹结构；最后用第60节的旋量螺旋度方法选择外偏振，就能在相乘之前消去许多项。我们将先算四胶子散射，再加入一对无质量夸克。这两个例子也说明，颜色次序、螺旋度和运动学各自简单的表达式，怎样合成为可以用于截面的结果。

本节用到[第60节](/posts/srednicki-60/#c60)、[第79节](/posts/srednicki-79/#c79)和[第80节](/posts/srednicki-80/#c80)。计算在四维进行，保留树级振幅的$g^2$阶及平方的$g^4$阶；夸克质量取零。对实际轻夸克，这要求$m_q^2\ll s,|t|,|u|$，即在硬散射区域取$m_q/Q$的零阶。颜色群暂取$SU(N)$、$N\ge2$，量子色动力学最后令$N=3$。

<span id="c81-rules"></span>

## 固定颜色次序后的规则

沿第79节，我们把生成元归一为$\operatorname{Tr}T^aT^b=\delta^{ab}$，协变导数写作$D_\mu=\partial_\mu-igA_\mu/\sqrt2$。这里$g$又是规范耦合，在四维无量纲。计算所用的紧凑密度为

<span id="eq:c81-gn-density"></span>

$$
\mathcal L_{\rm GN}
=\operatorname{Tr}\left[
-\frac12\partial^\mu A^\nu\partial_\mu A_\nu
-i\sqrt2g\,\partial^\mu A^\nu A_\nu A_\mu
+\frac{g^2}{4}A^\mu A^\nu A_\mu A_\nu\right].
\tag{81.1}
$$

它的适用场空间已在[第79节](/posts/srednicki-79/#c79-un-completion)确定：为使用这里的单迹规则，内部采用完整$U(N)$矩阵场，并保留中央方向的规范固定；物理外胶子最终取无迹方向。若只对无迹场积分，应另加$-g^2[\operatorname{Tr}(A_\mu A^\mu)]^2/(4N)$。下面采用完整矩阵实现，其物理外$SU(N)$振幅按[已建立的BRST规范变形](/posts/srednicki-79/#c79-complex-brst)与通常规范相同。无外鬼的树图没有鬼线，因为每个鬼顶角都延续鬼数流，内部鬼链若没有端点便形成圈。

一张平面树的外腿沿逆时针方向排为$1,\ldots,n$时，第80节的逐边迹拼接给颜色因子$\operatorname{Tr}(T^{a_1}\cdots T^{a_n})$。先确定它携带的耦合次幂。设三、四顶角数为$V_3,V_4$，内部线数为$I$；树的连通性和端点计数分别给

<span id="eq:c81-tree-count"></span>

$$
I=V_3+V_4-1,\qquad
3V_3+4V_4=2I+n,
\qquad V_3+2V_4=n-2.
\tag{81.2}
$$

每个三顶角含$g$，每个四顶角含$g^2$，故所有$n$点树都含$g^{n-2}$。将它和颜色迹取出，定义部分振幅（partial amplitude）$A$：

<span id="eq:c81-color-decomposition"></span>

$$
\begin{aligned}
\mathcal T(1,\ldots,n)
 &=g^{n-2}\sum_{\text{非循环排列}}
 \operatorname{Tr}(T^{a_1}\cdots T^{a_n})A(1,\ldots,n),\\
A(2,\ldots,n,1)&=A(1,2,\ldots,n).
\end{aligned}
\tag{81.3}
$$

求和可固定第一条腿，只排列其余$n-1$条。第二行来自同一张有序图沿边界改变起点，动量和偏振仍随各腿一起移动。$A$包含该边界次序允许的全部平面树；它的质量量纲为$4-n$，四点时为零。图值为$i\mathcal T$，因此提取$A$时还要除去共同的$i$。

自由二次项与第80节相同，只多一个洛伦兹度规。去掉颜色连接后，传播函数及实际图线分别为

<span id="eq:c81-propagator"></span>

$$
\begin{gathered}
\widetilde\Delta^{\mu\nu}(k)=\frac{g^{\mu\nu}}{k^2-i0},
\qquad s_{ij}=-(k_i+k_j)^2,\\
\frac{\widetilde\Delta^{\mu\nu}(k)}i
 =-\frac{ig^{\mu\nu}}{k^2-i0}
 =\frac{ig^{\mu\nu}}{s_{ij}+i0}.
\end{gathered}
\tag{81.4}
$$

最后一式用于内部动量$k=k_i+k_j$。以下先在通道不为零处计算树幅的有理式，省写$0^+$；需要极点边界值时再恢复这一处方。它与维数调节参数无关。

三次项有一个导数。取三个外动量$p,q,r$全部向外，洛伦兹指标相应为$\mu,\nu,\rho$。第一条腿落在有导数的场上时，导数给$-ip_\rho$，另外两场的相同指标给$g_{\mu\nu}$；乘上作用量展开的$i$及密度系数$-i\sqrt2g$，得到$-i\sqrt2g\,p_\rho g_{\mu\nu}$。同一循环字中还可让第二、第三条腿落在导数上，于是

<span id="eq:c81-ordered-vertices"></span>

$$
\begin{aligned}
iV^{\rm GN}_{\mu\nu\rho}(p,q,r)
 &=-i\sqrt2g\left(
 p_\rho g_{\mu\nu}+q_\mu g_{\nu\rho}
 +r_\nu g_{\rho\mu}\right),\\
iV^{\rm GN}_{\mu\nu\rho\sigma}
 &=ig^2g_{\mu\rho}g_{\nu\sigma}.
\end{aligned}
\tag{81.5}
$$

四次项的四个循环起点都给相对两腿的配对，恰好消去密度中的$1/4$。不同的非循环分配已经归入[（81.3）](#eq:c81-color-decomposition)的不同颜色字。这与第80节区分固定分量顶角和循环顶角的做法相同。

给每条外腿乘上指定螺旋度的偏振$\varepsilon_i$，三、四顶角便成为

<span id="eq:c81-polarized-vertices"></span>

$$
\begin{aligned}
iV_{123}=-i\sqrt2g\bigl[&
 (\varepsilon_1\cdot\varepsilon_2)(k_1\cdot\varepsilon_3)
 +(\varepsilon_2\cdot\varepsilon_3)(k_2\cdot\varepsilon_1)\\
 &+(\varepsilon_3\cdot\varepsilon_1)(k_3\cdot\varepsilon_2)\bigr],\\
iV_{1234}=ig^2&
 (\varepsilon_1\cdot\varepsilon_3)(\varepsilon_2\cdot\varepsilon_4).
\end{aligned}
\tag{81.6}
$$

内部线也可以暂用一个$\varepsilon_5$标出尚未收缩的指标，但另一端要另写$\varepsilon_{5'}$，最后将$\varepsilon_5^\mu\varepsilon_{5'}^\nu$替成传播子。这两个字母表示待收缩的洛伦兹指标，内部离壳动量通过完整传播子连接。

<span id="c81-reflection"></span>

## 颜色次序的反射

除了循环对称，部分幅还满足反射关系$A(n,\ldots,1)=(-1)^nA(1,\ldots,n)$。先把这一关系的顶角依据说清楚。若将[（81.6）](#eq:c81-polarized-vertices)三顶角方括号内的量记为$X_{123}$，动量守恒直接给

<span id="eq:c81-longitudinal-remainder"></span>

$$
\begin{aligned}
X_{123}+X_{321}
={}&-(\varepsilon_1\cdot\varepsilon_2)(k_3\cdot\varepsilon_3)
 -(\varepsilon_2\cdot\varepsilon_3)(k_1\cdot\varepsilon_1)\\
 &-(\varepsilon_3\cdot\varepsilon_1)(k_2\cdot\varepsilon_2).
\end{aligned}
\tag{81.7}
$$

例如$\varepsilon_1\cdot\varepsilon_2$的系数由$k_1+k_2=-k_3$得到，其余两项由循环排列给出。三条横向外腿使右边为零；有内线时这一步不能直接用于每个GN顶角。为证明完整部分幅的反射关系，可以先使用线性费曼规范，再利用物理振幅的规范不变性。

令$\kappa=g/\sqrt2$。展开$-\operatorname{Tr}F^2/4$，其三、四次项是

<span id="eq:c81-linear-gauge-density"></span>

$$
\begin{aligned}
\mathcal L_{{\rm F},3}
 &=i\kappa\operatorname{Tr}\bigl(
 \partial^\mu A^\nu A_\mu A_\nu
 -\partial^\mu A^\nu A_\nu A_\mu\bigr),\\
\mathcal L_{{\rm F},4}
 &=\frac{\kappa^2}{2}\operatorname{Tr}\bigl(
 A^\mu A^\nu A_\mu A_\nu-A_\mu A^\mu A_\nu A^\nu\bigr).
\end{aligned}
\tag{81.8}
$$

三次项的两个相反次序给动量的差；四次项的第一种配对有四个循环起点，第二种分别有两个$12/34$和两个$14/23$配对。因此对应的有序规则为

<span id="eq:c81-linear-gauge-vertices"></span>

$$
\begin{aligned}
iV^{\rm F}_{\mu\nu\rho}
 &=-i\kappa\bigl[(p-q)_\rho g_{\mu\nu}
 +(q-r)_\mu g_{\nu\rho}+(r-p)_\nu g_{\rho\mu}\bigr],\\
iV^{\rm F}_{1234}
 &=ig^2\bigl[(\varepsilon_1\cdot\varepsilon_3)
                 (\varepsilon_2\cdot\varepsilon_4)\\
 &\hspace{12mm}-\tfrac12(\varepsilon_1\cdot\varepsilon_2)
                 (\varepsilon_3\cdot\varepsilon_4)
 -\tfrac12(\varepsilon_1\cdot\varepsilon_4)
                 (\varepsilon_2\cdot\varepsilon_3)\bigr].
\end{aligned}
\tag{81.9}
$$

反转三条腿时，每个动量差反号，配对指标相应互换；四顶角则不变。传播子的两端互换也不改变其值。于是每张反射树给$(-1)^{V_3}$，再用[（81.2）](#eq:c81-tree-count)中的$V_3=n-2-2V_4$，得到$(-1)^n$。

从完整颜色幅的规范不变性传到每个部分幅，可以把某个颜色迹单独挑出来。对$N\ge n$，令外颜色矩阵依次取$X_1=E_{12},X_2=E_{23},\ldots,X_n=E_{n1}$，其中$E_{ij}$只有第$i$行第$j$列为1。它们属于厄米基的复线性张成；振幅对每个外颜色线性，所以允许这样检验系数。由$E_{ij}E_{kl}=\delta_{jk}E_{il}$，只有沿这条闭合路径走完的乘积才有非零迹，故

<span id="eq:c81-reflection"></span>

$$
\begin{gathered}
\operatorname{Tr}(X_{\pi(1)}\cdots X_{\pi(n)})
 =\begin{cases}1,&\pi\text{属于循环字 }12\cdots n,\\
 0,&\text{其它非循环次序},\end{cases}\\
A_{\mathrm{GN}}(1,\ldots,n)=A_{\mathrm F}(1,\ldots,n),\qquad
A(n,\ldots,1)=(-1)^nA(1,\ldots,n).
\end{gathered}
\tag{81.10}
$$

这里用了第79节相同物理外态下的规范等价。完整矩阵树的内部颜色收缩只拼成外迹，没有剩余的颜色环，所以有序系数本身不含$N$；在足够大的$N$证明的等式因而也适用于较小的$N$。对以下四点过程，反射号为正，六个循环次序于是分为三对。

<span id="c81-zero-helicities"></span>

## 选择偏振先消去零幅

所有外动量仍向外指定。若第1、2腿实际入射，它们的指定能量为负，螺旋度标签也与真实入射值相反；旋量按[第60节](/posts/srednicki-60/#c60-brackets)延拓。偏振的代数形式不变。把[第60节的偏振收缩](/posts/srednicki-60/#c60-polarizations)用于胶子，得到

<span id="eq:c81-polarization-products"></span>

$$
\begin{aligned}
\varepsilon_+(k;q)\cdot\varepsilon_+(k';q')
 &=\frac{\langle qq'\rangle[kk']}
         {\langle qk\rangle\langle q'k'\rangle},\\
\varepsilon_-(k;q)\cdot\varepsilon_-(k';q')
 &=\frac{[qq']\langle kk'\rangle}{[qk][q'k']},\\
\varepsilon_+(k;q)\cdot\varepsilon_-(k';q')
 &=\frac{\langle qk'\rangle[kq']}
         {\langle qk\rangle[q'k']}.
\end{aligned}
\tag{81.11}
$$

先看为什么使所有双偏振内积为零，就足以使树幅消失。每个外偏振只出现一次，共有$n$个。GN顶角和传播子只用度规连接指标，三顶角各提供一个动量，故每项最多有$V_3\le n-2$个动量可与偏振收缩。至少余下两个偏振必须彼此相乘。因此每项都含某个$\varepsilon_i\cdot\varepsilon_j$。

若所有螺旋度为正，为它们选同一个有效参考$q$，[（81.11）](#eq:c81-polarization-products)第一行的$\langle qq\rangle$使任意一对的内积为零。若只有第$r$腿为负，则令所有正偏振的参考为$k_r$，负偏振另取有效参考。正正内积仍为零，正负内积的分子含$\langle k_rk_r\rangle$，也为零。交换角、方括号得到另一组号，因而

<span id="eq:c81-zero-amplitudes"></span>

$$
\begin{aligned}
A(1^+,\ldots,n^+)&=0,&
A(1^+,\ldots,r^-,\ldots,n^+)&=0,\\
A(1^-,\ldots,n^-)&=0,&
A(1^-,\ldots,r^+,\ldots,n^-)&=0
\qquad(n\ge4).
\end{aligned}
\tag{81.12}
$$

证明在参考分母均非零的一般运动学区域进行，所得树级有理函数恒等式可在其它有效参考片继续使用。复三点运动学有全部角括号或全部方括号为零的特殊分支；这时上述参考选择可能无定义，不能将单异号零幅断言用于该分支。后面的四点计算则取$s,t,u$均非零，满足所需条件。

<span id="c81-adjacent-mhv"></span>

## 相邻两个负螺旋度的四胶子幅

四点只有两正两负的组合还未排除。先求$A(1^-,2^-,3^+,4^+)$，选择参考动量

<span id="eq:c81-four-gluon-references"></span>

$$
\begin{gathered}
q_1=q_2=k_3,\qquad q_3=q_4=k_2,\\
\varepsilon_1\cdot\varepsilon_4
 =\frac{\langle21\rangle[43]}{\langle24\rangle[31]},
\qquad
\varepsilon_i\cdot\varepsilon_j=0
\quad(i<j,\ (i,j)\ne(1,4)).
\end{gathered}
\tag{81.13}
$$

例如$12$、$34$的内积各因同参考为零；$13$、$23$的异号收缩含$[33]$，$24$的收缩含$\langle22\rangle$。只有$14$不含这些零因子。这样的选择正好消去固定边界$1234$的三张图中的两张。

![四胶子的两条交换道与接触图](/images/srednicki/s81_gluon_trees.svg)

固定循环次序1234的三张四胶子树，分别为12通道、23通道和接触图。箭头规定内部动量，两端取相反号。

接触图含$(\varepsilon_1\cdot\varepsilon_3)(\varepsilon_2\cdot\varepsilon_4)$，直接为零。23通道的一个顶角按$235$排列，三个项分别含

<span id="eq:c81-vanishing-gluon-diagrams"></span>

$$
\begin{aligned}
&(\varepsilon_2\cdot\varepsilon_3)(k_2\cdot\varepsilon_5)=0,\\
&(\varepsilon_3\cdot\varepsilon_5)(k_3\cdot\varepsilon_2)=0,
 &&k_3=q_2,\\
&(\varepsilon_5\cdot\varepsilon_2)(k_5\cdot\varepsilon_3)=0,
 &&k_5=-k_2-k_3=-q_3-k_3.
\end{aligned}
\tag{81.14}
$$

第二行用参考横向性$q_2\cdot\varepsilon_2=0$，第三行同时用$q_3\cdot\varepsilon_3=0$和$k_3\cdot\varepsilon_3=0$。这三项在收缩内槽以前已经为零，故整张图消失。

只需计算12通道。左端内部动量取$k_5=-k_1-k_2$，右端取$k_{5'}=-k_5$，两个顶角按$125$及$345'$排列。各自第一项含$\varepsilon_1\cdot\varepsilon_2$或$\varepsilon_3\cdot\varepsilon_4$，故剩

<span id="eq:c81-two-surviving-vertices"></span>

$$
\begin{aligned}
iV_{125}=-i\sqrt2g\bigl[&
 (\varepsilon_2\cdot\varepsilon_5)(k_2\cdot\varepsilon_1)
 +(\varepsilon_5\cdot\varepsilon_1)(k_5\cdot\varepsilon_2)\bigr],\\
iV_{345'}=-i\sqrt2g\bigl[&
 (\varepsilon_4\cdot\varepsilon_{5'})(k_4\cdot\varepsilon_3)
 +(\varepsilon_{5'}\cdot\varepsilon_3)(-k_5\cdot\varepsilon_4)\bigr].
\end{aligned}
\tag{81.15}
$$

将$\varepsilon_5^\mu\varepsilon_{5'}^\nu$替为$ig^{\mu\nu}/s_{12}$。两个二项式相乘产生四项，其中三项依次含$\varepsilon_2\cdot\varepsilon_4$、$\varepsilon_2\cdot\varepsilon_3$和$\varepsilon_1\cdot\varepsilon_3$，全部为零。左端第二项与右端第一项相乘留下

<span id="eq:c81-gluon-one-term"></span>

$$
\begin{aligned}
ig^2A_{--++}
 &=(-i\sqrt2g)^2\frac{i}{s_{12}}
 (\varepsilon_1\cdot\varepsilon_4)
 (k_5\cdot\varepsilon_2)(k_4\cdot\varepsilon_3),\\
A_{--++}
 &=\frac{2}{s_{12}}
 (\varepsilon_1\cdot\varepsilon_4)
 (k_1\cdot\varepsilon_2)(k_4\cdot\varepsilon_3).
\end{aligned}
\tag{81.16}
$$

第二行的正号来自两处：$(-i)^2=-1$，而$k_5\cdot\varepsilon_2=-k_1\cdot\varepsilon_2$。再除去整个图共有的$ig^2$，便得到上式的因子2。

接着把动量收缩也变成括号。[（60.12）](/posts/srednicki-60/#eq:c60-polarization-transversality)已经从$-\slashed p$的两外积分解给出，对类光$p$有

<span id="eq:c81-momentum-polarizations"></span>

$$
\begin{aligned}
p\cdot\varepsilon_+(k;q)
 &=\frac{\langle qp\rangle[pk]}{\sqrt2\langle qk\rangle},&
 p\cdot\varepsilon_-(k;q)
 &=\frac{[qp]\langle pk\rangle}{\sqrt2[qk]},\\
k_1\cdot\varepsilon_2
 &=\frac{[31]\langle12\rangle}{\sqrt2[32]},&
 k_4\cdot\varepsilon_3
 &=\frac{\langle24\rangle[43]}{\sqrt2\langle23\rangle}.
\end{aligned}
\tag{81.17}
$$

这里的两次代入都是类光外动量。将它们和[（81.13）](#eq:c81-four-gluon-references)代入[（81.16）](#eq:c81-gluon-one-term)，两份$\sqrt2$抵消因子2，$[31]$、$\langle24\rangle$分别约去，再用$s_{12}=\langle12\rangle[21]$，得到只含旋量括号的幅。从这一中间式到最终对称形式的每一步可写为

<span id="eq:c81-adjacent-result"></span>

$$
\begin{aligned}
A_{--++}
 &=\frac{\langle21\rangle[43]^2}{[21][32]\langle23\rangle}\\
 &=\frac{\langle21\rangle\langle12\rangle[43]}
 {[32]\langle23\rangle\langle34\rangle}\\
 &=-\frac{\langle21\rangle^2\langle12\rangle[23]}
 {[32]\langle23\rangle\langle34\rangle\langle41\rangle}\\
 &=\frac{\langle12\rangle^4}
 {\langle12\rangle\langle23\rangle\langle34\rangle\langle41\rangle}.
\end{aligned}
\tag{81.18}
$$

第二行先乘$\langle34\rangle/\langle34\rangle$，利用$\langle34\rangle[43]=s_{34}=s_{12}=\langle12\rangle[21]$。第三行再乘$\langle41\rangle/\langle41\rangle$，用动量守恒的旋量夹乘

<span id="eq:c81-gluon-bracket-identity"></span>

$$
\langle21\rangle[23]+\langle41\rangle[43]=0.
\tag{81.19}
$$

这是[（60.34）](/posts/srednicki-60/#eq:c60-momentum-sandwich)取左端为1、右端为3后，再利用角括号反对称性所得。最后$[23]=-[32]$消去负号，$\langle21\rangle^2=\langle12\rangle^2$；为使分母成为完整循环乘积，再补一份$\langle12\rangle/\langle12\rangle$。这样便得到了循环对称的分母。

这个表达式的分母只记循环相邻的腿，分子挑出两个负螺旋度。循环移动标签立即给出$A(1^+,2^-,3^-,4^+)=\langle23\rangle^4/(\langle12\rangle\langle23\rangle\langle34\rangle\langle41\rangle)$及其它相邻情形。四个括号在分子、分母各有四次，总质量量纲为零，与四点树幅相符。还缺少负螺旋度不相邻的一类；下面用颜色关系把它归到已经算出的结果。

<span id="c81-decoupling"></span>

## 用光子退耦求非相邻情形

对于无迹$SU(N)$基，完备关系包含单位矩阵的减项：

<span id="eq:c81-su-projector"></span>

$$
\sum_{a=1}^{N^2-1}(T^a)_i{}^j(T^a)_k{}^l
 =\delta_i{}^l\delta_k{}^j-\frac1N\delta_i{}^j\delta_k{}^l.
\tag{81.20}
$$

为什么纯胶子散射又能使用第80节的完整基颜色和，可以从规范不变场强看出。把完整矩阵分成$A_\mu=\widehat A_\mu+a_\mu^0\mathbf1_N/\sqrt N$，中央分量与所有矩阵对易，故

<span id="eq:c81-central-decoupling"></span>

$$
\begin{aligned}
F_{\mu\nu}
 &=\widehat F_{\mu\nu}
  +\frac{\mathbf1_N}{\sqrt N}
    (\partial_\mu a_\nu^0-\partial_\nu a_\mu^0),\\
-\frac14\operatorname{Tr}F^2
 &=-\frac14\operatorname{Tr}\widehat F^2
   -\frac14(f_{\mu\nu}^0)^2 .
\end{aligned}
\tag{81.21}
$$

交叉项因$\operatorname{Tr}\widehat F=0$消失。这样引入的中央粒子就是一个自由的“光子”，任何含它的非平凡纯规范场散射都为零。线性规范下这一点逐图可见；GN规范固定项虽产生中央耦合，完整物理幅仍由规范等价退耦。因此在对完整幅的外颜色求和时，补进中央方向只是在原和式中加入零。完整基的完备关系可在这个意义下使用。

让四点幅的第4条外颜色取单位矩阵，六种循环字只剩两种三矩阵迹。将相同的迹收集在一起，[（81.3）](#eq:c81-color-decomposition)成为

<span id="eq:c81-photon-insertion"></span>

$$
\begin{aligned}
0={}&\operatorname{Tr}(T^{a_1}T^{a_2}T^{a_3})
 \bigl[A(1234)+A(1243)+A(1423)\bigr]\\
 &+\operatorname{Tr}(T^{a_1}T^{a_3}T^{a_2})
 \bigl[A(1324)+A(1342)+A(1432)\bigr].
\end{aligned}
\tag{81.22}
$$

这里把单位矩阵的共同归一因子约去。在$N\ge3$时，取前三个颜色为$E_{12},E_{23},E_{31}$，第一个迹等于1，第二个等于0；交换其中两矩阵则反过来。于是两个方括号分别为零。$SU(2)$的三生成元迹相互有线性关系；有序树系数本身不依赖$N$，所以在$N\ge3$得到的系数恒等式也适用于$SU(2)$。第一组给

<span id="eq:c81-photon-decoupling-identity"></span>

$$
A(1234)=-A(1243)-A(1423).
\tag{81.23}
$$

这就是光子退耦恒等式（photon decoupling identity）。把原来的$1^-,3^-$负螺旋度保持在各自标签上，右边的两个次序都使它们循环相邻，可以代入[（81.18）](#eq:c81-adjacent-result)：

<span id="eq:c81-nonadjacent-reduction"></span>

$$
\begin{aligned}
A(1^-,2^+,3^-,4^+)
={}&-\frac{\langle31\rangle^4}
 {\langle31\rangle\langle12\rangle\langle24\rangle\langle43\rangle}
 -\frac{\langle31\rangle^4}
 {\langle31\rangle\langle14\rangle\langle42\rangle\langle23\rangle}\\
={}&-\frac{\langle13\rangle^3}{\langle24\rangle}
 \frac{\langle14\rangle\langle23\rangle
       +\langle12\rangle\langle34\rangle}
 {\langle12\rangle\langle34\rangle\langle14\rangle\langle23\rangle}.
\end{aligned}
\tag{81.24}
$$

第二行将$\langle31\rangle$、$\langle43\rangle$和$\langle42\rangle$分别反向，再通分。分子正好是第50节斯豪滕恒等式的一种排列：

<span id="eq:c81-schouten"></span>

$$
\langle14\rangle\langle23\rangle
 +\langle12\rangle\langle34\rangle
 =\langle13\rangle\langle24\rangle.
\tag{81.25}
$$

它消掉$\langle24\rangle$并补出第四份$\langle13\rangle$；剩下的负号用$\langle14\rangle=-\langle41\rangle$吸收。至此两类结果合为

<span id="eq:c81-four-gluon-mhv"></span>

$$
A(1,2,3,4)\big|_{r^-,s^-}
 =\frac{\langle rs\rangle^4}{D_{1234}},\qquad
D_{1234}\equiv\langle12\rangle\langle23\rangle
                 \langle34\rangle\langle41\rangle.
\tag{81.26}
$$

其它两条腿为正螺旋度。这种恰有两个负螺旋度的幅通常称为最大螺旋度违背幅（maximally helicity violating amplitude，MHV）。上式给出全部四点两负螺旋度部分幅。

<span id="c81-direct-nonadjacent"></span>

### 直接由23通道得到非相邻幅

同一个$A(1^-,2^+,3^-,4^+)$也可直接从三张树图求出。取
$q_1=q_3=k_2$、$q_2=q_4=k_1$。
两个同号偏振共用参考，异号收缩中只有$\varepsilon_3\cdot\varepsilon_4$可能非零。接触图立即为零；12顶角的三项分别含
$\varepsilon_1\cdot\varepsilon_2$、$k_2\cdot\varepsilon_1$及
$(-k_1-k_2)\cdot\varepsilon_2$，也全部消失。

在23通道取$k_5=-k_2-k_3$，另一端为$k_{5'}=-k_5$，两个循环顶角按$235$、$415'$排列。前者仅留$(\varepsilon_3\cdot\varepsilon_5)(k_3\cdot\varepsilon_2)$，后者仅留$(\varepsilon_{5'}\cdot\varepsilon_4)(k_{5'}\cdot\varepsilon_1)$。这里
$k_{5'}\cdot\varepsilon_1=k_3\cdot\varepsilon_1$，
所以

<span id="eq:c81-direct-nonadjacent-graph"></span>

$$
A(1^-,2^+,3^-,4^+)
=-\frac2{s_{23}}
 (\varepsilon_3\cdot\varepsilon_4)
 (k_3\cdot\varepsilon_2)(k_3\cdot\varepsilon_1).
\tag{81.48}
$$

负号来自$(-i\sqrt2g)^2(i/s_{23})/(ig^2)=-2/s_{23}$。
按所选参考，

<span id="eq:c81-direct-nonadjacent-products"></span>

$$
\begin{aligned}
\varepsilon_3\cdot\varepsilon_4
 &=\frac{\langle13\rangle[42]}{\langle14\rangle[23]},\\
k_3\cdot\varepsilon_2
 &=\frac{\langle13\rangle[32]}{\sqrt2\langle12\rangle},\qquad
k_3\cdot\varepsilon_1
 =\frac{[23]\langle31\rangle}{\sqrt2[21]}.
\end{aligned}
\tag{81.49}
$$

约去$[23]$和两份$\sqrt2$，再用
$s_{23}=\langle23\rangle[32]$及
$\langle31\rangle[12]+\langle34\rangle[42]=0$，得到

<span id="eq:c81-direct-nonadjacent-result"></span>

$$
\begin{aligned}
A
 &=\frac{\langle13\rangle^3[42]}
        {\langle23\rangle\langle14\rangle\langle12\rangle[21]}\\
 &=-\frac{\langle13\rangle^4}
         {\langle12\rangle\langle23\rangle\langle34\rangle\langle14\rangle}
 =\frac{\langle13\rangle^4}{D_{1234}}.
\end{aligned}
\tag{81.50}
$$

这与光子退耦得到的[（81.26）](#eq:c81-four-gluon-mhv)一致。

<span id="c81-gluon-color-sum"></span>

## 四胶子的颜色、螺旋度和与平均

仍用第80节的三个颜色次序代表，而$g^2$已从四点部分幅中提出：

<span id="eq:c81-gluon-partials"></span>

$$
A_3=A(1234),\qquad A_4=A(1342),\qquad A_2=A(1423),
\qquad A_2+A_3+A_4=0.
\tag{81.27}
$$

最后一式由[（81.23）](#eq:c81-photon-decoupling-identity)和循环、反射给出，因为$A(1243)=A(1342)$。每个$A_j$对应两种相反的颜色字；第80节已逐个收缩得到六色序格拉姆矩阵$(N^4-N^2)\mathbf1_6+N^2J_6$。把六个系数依次替成三对相同的$A_j$，直接得到

<span id="eq:c81-gluon-color-squared"></span>

$$
\begin{aligned}
\sum_{\rm color}|\mathcal T|^2
 &=g^4\left[2(N^4-N^2)\sum_{j=2}^4|A_j|^2
            +4N^2\left|\sum_{j=2}^4A_j\right|^2\right]\\
 &=2N^2(N^2-1)g^4\bigl(|A_2|^2+|A_3|^2+|A_4|^2\bigr).
\end{aligned}
\tag{81.28}
$$

第一项中的2数的是每一对反向字，第二项中的4来自两份系数和各带一个2。光子退耦使第二项消失，于是复杂的颜色干涉只留下三个部分幅的模方。这里的颜色和仍包括入射颜色。

令实际过程为$gg\to gg$，则全出记号中的$k_1,k_2$为负能，$k_3,k_4$为正能。定义

<span id="eq:c81-physical-invariants"></span>

$$
\begin{gathered}
s=s_{12}=s_{34}>0,\qquad
 t=s_{13}=s_{24}<0,\qquad
 u=s_{14}=s_{23}<0,\qquad s+t+u=0,\\
|\langle ij\rangle|^2=|[ij]|^2=|s_{ij}|.
\end{gathered}
\tag{81.29}
$$

最后一式已在第60节连同负能旋量的$i$因子证明。对固定$--++$，三个部分幅都有分子$\langle12\rangle^4$，模方为$s^4$。三个循环分母的模方分别为$s^2u^2$、$s^2t^2$和$t^2u^2$，故

<span id="eq:c81-gluon-fixed-helicity"></span>

$$
\sum_{\rm color}|\mathcal T_{--++}|^2
 =2N^2(N^2-1)g^4s^4
 \left(\frac1{s^2t^2}+\frac1{t^2u^2}+\frac1{u^2s^2}\right).
\tag{81.30}
$$

剩余螺旋度求和只需数负螺旋度落在哪两条腿上。$12$和$34$两种位置各给$s^4$，$13$和$24$各给$t^4$，$14$和$23$各给$u^4$；其它十种组合已经为零。把这些结果相加，再除以两个初态各自的$2(N^2-1)$种等权状态：

<span id="eq:c81-gluon-unpolarized"></span>

$$
\begin{aligned}
\sum_{\rm color,hel}|\mathcal T|^2
 &=4N^2(N^2-1)g^4(s^4+t^4+u^4)
 \left(\frac1{s^2t^2}+\frac1{t^2u^2}+\frac1{u^2s^2}\right),\\
\overline{|\mathcal T_{gg\to gg}|^2}
 &=\frac{N^2g^4}{N^2-1}(s^4+t^4+u^4)
 \left(\frac1{s^2t^2}+\frac1{t^2u^2}+\frac1{u^2s^2}\right).
\end{aligned}
\tag{81.31}
$$

作为这个结果的解析核验，还可以把它化为较熟悉的通道形式。记$S=s^2+t^2+u^2$，由$s+t+u=0$有$st+su+tu=-S/2$及$s^2t^2+s^2u^2+t^2u^2=S^2/4$，所以$s^4+t^4+u^4=S^2/2$。再令$x=st,y=su,z=tu$，则$xy+yz+zx=stu(s+t+u)=0$，从三次恒等式得到$x^3+y^3+z^3=-S^3/8+3s^2t^2u^2$。两边通分后便有

<span id="eq:c81-gluon-channel-form"></span>

$$
\begin{aligned}
&(s^4+t^4+u^4)
 \left(\frac1{s^2t^2}+\frac1{t^2u^2}+\frac1{u^2s^2}\right)
 =\frac{S^3}{2s^2t^2u^2}\\
&\hspace{15mm}=4\left(3-\frac{tu}{s^2}
                       -\frac{su}{t^2}-\frac{st}{u^2}\right),\\
&\overline{|\mathcal T_{gg\to gg}|^2}_{N=3}
 =\frac92g^4\left(3-\frac{tu}{s^2}
                       -\frac{su}{t^2}-\frac{st}{u^2}\right).
\end{aligned}
\tag{81.32}
$$

在质心$90^\circ$处，$t=u=-s/2$，结果为$243g^4/8$；未化简表达式中的四次和为$9s^4/8$，倒数和为$24/s^4$，直接相乘给出相同值。若$t\to0$而$u\to-s$，一般$N$的首项为$4N^2g^4s^2/[(N^2-1)t^2]$。这一小角增强来自无质量胶子交换；计算角度积分时需给出相应的角截取或红外安全观测量。

<span id="c81-quark-rules"></span>

## 加入一条夸克线

接下来加入一个无质量基本表示狄拉克场。其拉氏密度及有序顶角为

<span id="eq:c81-quark-vertex"></span>

$$
\begin{aligned}
\mathcal L_q
 &=i\bar\Psi\slashed D\Psi
 =i\bar\Psi\slashed\partial\Psi
  +\frac g{\sqrt2}\bar\Psi\gamma^\mu A_\mu\Psi,\\
iV_q^\mu&=\frac{ig}{\sqrt2}\gamma^\mu.
\end{aligned}
\tag{81.33}
$$

这里的$1/\sqrt2$正好补偿$T^a=\sqrt2t^a$，分量顶角仍是熟悉的$igt^a\gamma^\mu$。夸克线只携带一个基本颜色指标，因此把上一节的双线接到它上面，闭合颜色迹就变成一条开放矩阵链。

把全出费米端标为$1_{\bar q},2_q$，胶子标为3、4。固定这个循环次序时，有内部夸克交换和内部胶子交换两张图。沿颜色箭头的反方向从2读到1，先遇胶子3，再遇胶子4，所得链为$(T^{a_3}T^{a_4})_{i_2}{}^{i_1}$。交换两个胶子的外标号补出另一种次序，故

<span id="eq:c81-open-color-chain"></span>

$$
\begin{aligned}
\mathcal T_{i_2}{}^{i_1}
 =g^2\bigl[& (T^{a_3}T^{a_4})_{i_2}{}^{i_1}A(1_{\bar q},2_q,3,4)\\
 &+(T^{a_4}T^{a_3})_{i_2}{}^{i_1}A(1_{\bar q},2_q,4,3)\bigr].
\end{aligned}
\tag{81.34}
$$

![两夸克两胶子的费米和胶子交换图](/images/srednicki/s81_quark_trees.svg)

两夸克两胶子的两个有序树图。费米箭头沿1到2；左图内部夸克动量为$p_5=-p_1-k_4=p_2+k_3$，右图三胶子端流出的内部动量为$k_5=-k_3-k_4=p_1+p_2$。

![夸克线上的有序颜色链](/images/srednicki/s81_quark_colors.svg)

前两图的颜色连接。胶子换成两条有向颜色线，夸克仍为单线；两图均从2端读出$T^{a_3}T^{a_4}$。线的相接说明指标乘法，运动学因子由前图规则给出。

夸克也与中央单位矩阵方向耦合，因此以后对外胶子求颜色和时必须保留无迹投影。这里仍能借完整矩阵GN规则计算两夸克、两外$SU(N)$胶子的树幅：在线性规范中，额外中央内线若接到两个外胶子上，其三顶角因对易子为零而消失，故此过程与$SU(N)$相同；规范变形保持这个物理结果。更多费米线之间还可能通过中央场交换，这时完整矩阵理论的物理过程会有所增加。

无质量费米传播分子及向量顶角均在两个外尔块之间切换。含$v$个夸克顶角和$v-1$个内部费米分子的开放链共有$2v-1$个非对角因子，仍为非对角矩阵。因而非零外端点必须一方一角，即$1_{\bar q}^-,2_q^+$或其相反组合。先算前一种，链为$[2|\cdots|1\rangle$。

令$A=A_q+A_g$，$J^\mu=[2|\gamma^\mu|1\rangle$。左图的动量方向给$-\slashed p_5=\slashed p_1+\slashed k_4$、$p_5^2=-s_{14}$；两个顶角和传播函数外的$1/i$给$(ig/\sqrt2)^2/i=ig^2/2$。右图则有共同系数$(ig/\sqrt2)i(-i\sqrt2g)=ig^2$。除去整个幅的$ig^2$，两个部分幅便明确写为

<span id="eq:c81-quark-two-diagrams"></span>

$$
\begin{aligned}
A_q={}&-\frac1{2s_{14}}[2|\slashed\varepsilon_3
 (\slashed p_1+\slashed k_4)\slashed\varepsilon_4|1\rangle,\\
A_g={}&\frac1{s_{12}}\bigl[
 (\varepsilon_3\cdot\varepsilon_4)(J\cdot k_3)
 +(J\cdot\varepsilon_4)(k_4\cdot\varepsilon_3)\\
 &\hspace{27mm}+(J\cdot\varepsilon_3)(k_5\cdot\varepsilon_4)\bigr],
 \qquad k_5=p_1+p_2.
\end{aligned}
\tag{81.35}
$$

胶子两端的独立洛伦兹槽已在第二行缩并。无质量端点还使$J\cdot k_5=[2|(\slashed p_1+\slashed p_2)|1\rangle=0$；后面选择参考时，既可消掉偏振内积，也可消掉这种端点矩阵元。

<span id="c81-quark-mhv"></span>

## 两种非零夸克螺旋度幅

先把偏振写成[第60节已经推导的外积](/posts/srednicki-60/#c60-polarizations)：

<span id="eq:c81-polarization-slashes"></span>

$$
\begin{aligned}
\slashed\varepsilon_+(k;q)
 &=\frac{\sqrt2}{\langle qk\rangle}
   \bigl(|k]\langle q|+|q\rangle[k|\bigr),\\
\slashed\varepsilon_-(k;q)
 &=\frac{\sqrt2}{[qk]}
   \bigl(|k\rangle[q|+|q]\langle k|\bigr),\\
\slashed p&=-|p\rangle[p|-|p]\langle p|.
\end{aligned}
\tag{81.36}
$$

斜线矩阵连接两个外尔空间，它的外积因而分别取一角一方两类端点。负偏振的第二项为$|q]\langle k|$；代入$q=k_3,k=k_4$就得到下面的$|3]\langle4|$。

若两个胶子都为正，令$q_3=q_4=p_1$，则$\slashed\varepsilon_3|1\rangle=\slashed\varepsilon_4|1\rangle=0$，且$\varepsilon_3\cdot\varepsilon_4=0$。$A_q$的右端消失，$A_g$三项分别由偏振内积或$J\cdot\varepsilon_{3,4}$消失。若两个胶子都为负，改取$q_3=q_4=p_2$，便有$[2|\slashed\varepsilon_3=[2|\slashed\varepsilon_4=0$，同样逐项为零。因此只剩胶子螺旋度相反的两种情形。

取$3^+,4^-$，令$q_3=k_4,q_4=k_3$。此时$\varepsilon_3\cdot\varepsilon_4=0$，$k_4\cdot\varepsilon_3=0$，而$k_5\cdot\varepsilon_4=-(k_3+k_4)\cdot\varepsilon_4=0$，所以整个胶子图消失。两个偏振斜线矩阵恰好含同一个外积和：

<span id="eq:c81-quark-mutual-references"></span>

$$
\slashed\varepsilon_3^+
 =\frac{\sqrt2}{\langle43\rangle}
   (|4\rangle[3|+|3]\langle4|),\qquad
\slashed\varepsilon_4^-
 =\frac{\sqrt2}{[34]}
   (|4\rangle[3|+|3]\langle4|).
\tag{81.37}
$$

把它们接到外旋量上，方角的零重叠使每端只留一个因子；再展开中间的斜线矩阵，夸克链的运算就分解为

<span id="eq:c81-quark-positive-three-chain"></span>

$$
\begin{aligned}
\relax[2|\slashed\varepsilon_3^+
 &=\frac{\sqrt2[23]}{\langle43\rangle}\langle4|,\qquad
\slashed\varepsilon_4^-|1\rangle
 =\frac{\sqrt2\langle41\rangle}{[34]}|3],\\
\langle4|(\slashed p_1+\slashed k_4)|3]
 &=-\langle41\rangle[13]-\langle44\rangle[43]
 =-\langle41\rangle[13],\\
A(1_{\bar q}^-,2_q^+,3^+,4^-)
 &=\frac{[23]\langle41\rangle^2[13]}
        {\langle43\rangle[34]s_{14}}.
\end{aligned}
\tag{81.38}
$$

两份$\sqrt2$约去[（81.35）](#eq:c81-quark-two-diagrams)的$1/2$，中间斜线矩阵的负号与$-1/s_{14}$相消。这同时确定了整体相位。为继续约分，在总动量守恒的斜线矩阵式左右分别夹$[3|,|4\rangle$及$[3|,|1\rangle$，删除同腿括号，得到

<span id="eq:c81-quark-bracket-identities"></span>

$$
\begin{aligned}
\relax[31]\langle14\rangle+[32]\langle24\rangle&=0
 &\Longrightarrow\quad
 [13]\langle41\rangle&=-[23]\langle42\rangle,\\
[32]\langle21\rangle+[34]\langle41\rangle&=0
 &\Longrightarrow\quad
 [23]\langle12\rangle&=[34]\langle14\rangle.
\end{aligned}
\tag{81.39}
$$

同时$s_{14}=s_{23}=-\langle23\rangle[23]$。先用第一条关系替换分子的一份$[13]\langle41\rangle$，再用第二条消$[23]/[34]$，有

<span id="eq:c81-quark-four-negative-result"></span>

$$
\begin{aligned}
A(1_{\bar q}^-,2_q^+,3^+,4^-)
 &=\frac{[23]\langle41\rangle\langle42\rangle}
        {\langle43\rangle[34]\langle23\rangle}\\
 &=\frac{\langle14\rangle\langle41\rangle\langle42\rangle}
        {\langle12\rangle\langle43\rangle\langle23\rangle}\\
 &=-\frac{\langle14\rangle^2\langle24\rangle}
        {\langle12\rangle\langle23\rangle\langle34\rangle}
 =\frac{\langle14\rangle^3\langle24\rangle}{D_{1234}}.
\end{aligned}
\tag{81.40}
$$

最后两步分别反转$41,42,43$的括号，再补$\langle41\rangle$进入循环分母。这就得到所求的第一种非零夸克幅。

另一种非零螺旋度也可逐段收缩。仍取$q_3=k_4,q_4=k_3$，现在$3^-,4^+$的共同外积为$|3\rangle[4|+|4]\langle3|$，胶子图的三个零因子不变。夸克图依次给

<span id="eq:c81-quark-three-negative-result"></span>

$$
\begin{aligned}
\relax[2|\slashed\varepsilon_3^-
 &=\frac{\sqrt2[24]}{[43]}\langle3|,\qquad
\slashed\varepsilon_4^+|1\rangle
 =\frac{\sqrt2\langle31\rangle}{\langle34\rangle}|4],\\
\langle3|(\slashed p_1+\slashed k_4)|4]
 &=-\langle31\rangle[14]-\langle34\rangle[44]
 =-\langle31\rangle[14],\\
A(1_{\bar q}^-,2_q^+,3^-,4^+)
 &=\frac{[24]\langle31\rangle^2[14]}
        {[43]\langle34\rangle s_{14}}\\
 &=-\frac{[24]\langle13\rangle^2}
        {[43]\langle34\rangle\langle14\rangle}
 =-\frac{\langle13\rangle^3}
        {\langle12\rangle\langle34\rangle\langle14\rangle}\\
 &=\frac{\langle13\rangle^3\langle23\rangle}{D_{1234}}.
\end{aligned}
\tag{81.41}
$$

倒数第二次约分用了$\langle12\rangle[24]+\langle13\rangle[34]=0$，即$\langle1|\sum_j\slashed p_j|4]=0$。其余只用$s_{14}=-\langle14\rangle[14]$和括号反对称性。这给出了负螺旋度胶子在第3腿的幅。两式又有相同的循环分母，但负螺旋度胶子在分子中分别出现三次于反夸克括号、一次于夸克括号。

<span id="c81-quark-alternate-reference"></span>

### 改换参考后由胶子图给出同一振幅

改取$q_4=p_1,q_3=k_4$。对刚才两种非零螺旋度，这个选择都使夸克图消失。逐项计算可以看出振幅如何在两图之间重新分配。

沿[（81.35）](#eq:c81-quark-two-diagrams)，先取$3^-,4^+$。由于$q_4=p_1$，$\slashed\varepsilon_4^+|1\rangle=0$，整张夸克图已经消失。胶子图中有

<span id="eq:c81-ex-literal-reference-zeroes"></span>

$$
\begin{aligned}
\varepsilon_3^-\cdot\varepsilon_4^+
 &=\frac{\langle13\rangle[44]}{\langle14\rangle[43]}=0,
 & k_4\cdot\varepsilon_3^-&=0,\\
k_5\cdot\varepsilon_4^+
 &=(p_1+p_2)\cdot\varepsilon_4^+
 =p_2\cdot\varepsilon_4^+.
\end{aligned}
\tag{81.51}
$$

第一行分别用同腿括号为零及参考横向性，第二行用$p_1=q_4$。所以只有$(J\cdot\varepsilon_3)(k_5\cdot\varepsilon_4)/s_{12}$留下。由已建立的偏振外积和动量收缩，两个因子是

<span id="eq:c81-ex-literal-gluon-factors"></span>

$$
J\cdot\varepsilon_3^-
 =\frac{\sqrt2[24]\langle31\rangle}{[43]},\qquad
p_2\cdot\varepsilon_4^+
 =\frac{\langle12\rangle[24]}{\sqrt2\langle14\rangle}.
\tag{81.52}
$$

相乘后用$s_{12}=\langle12\rangle[21]$约分，得

<span id="eq:c81-ex-literal-gluon-result"></span>

$$
\begin{aligned}
A_g
 &=\frac{[24]^2\langle31\rangle\langle12\rangle}
        {[43]\langle14\rangle s_{12}}\\
 &=-\frac{[24]^2\langle13\rangle}
        {[43][21]\langle14\rangle}
 =-\frac{\langle13\rangle^3}
        {\langle12\rangle\langle34\rangle\langle14\rangle}\\
 &=\frac{\langle13\rangle^3\langle23\rangle}{D_{1234}}.
\end{aligned}
\tag{81.53}
$$

最后一次约分依次用$[24]/[43]=\langle13\rangle/\langle12\rangle$及$[24]/[21]=\langle13\rangle/\langle34\rangle$。前式来自$\langle1|\sum\slashed p|4]=0$；后式来自$\langle3|\sum\slashed p|2]=0$，展开其非零项为$\langle31\rangle[12]+\langle34\rangle[42]=0$。于是得到与前面[（81.41）](#eq:c81-quark-three-negative-result)完全相同的幅，只是此前由夸克图给出，现在由胶子图给出。

再取$3^+,4^-$及同一组参考。夸克图两端成为

<span id="eq:c81-ex-target-reference-chain"></span>

$$
[2|\slashed\varepsilon_3^+
 =\frac{\sqrt2[23]}{\langle43\rangle}\langle4|,
\qquad
\slashed\varepsilon_4^-|1\rangle
 =\frac{\sqrt2\langle41\rangle}{[14]}|1].
\tag{81.54}
$$

中间矩阵元为$\langle4|(\slashed p_1+\slashed k_4)|1]=-\langle41\rangle[11]-\langle44\rangle[41]=0$，故夸克图仍然消失。这次胶子图的第一项含$\langle44\rangle$，第二项仍含$k_4\cdot\varepsilon_3=0$，又只剩第三项。代入

<span id="eq:c81-ex-target-gluon-factors"></span>

$$
J\cdot\varepsilon_3^+
 =\frac{\sqrt2[23]\langle41\rangle}{\langle43\rangle},\qquad
p_2\cdot\varepsilon_4^-
 =\frac{[12]\langle24\rangle}{\sqrt2[14]},
\tag{81.55}
$$

并用$[12]=-[21]$，得到

<span id="eq:c81-ex-target-gluon-result"></span>

$$
\begin{aligned}
A_g
 &=\frac{[23]\langle41\rangle[12]\langle24\rangle}
        {\langle43\rangle[14]s_{12}}\\
 &=-\frac{[23]\langle14\rangle\langle24\rangle}
        {[14]\langle12\rangle\langle34\rangle}
 =-\frac{\langle14\rangle^2\langle24\rangle}
        {\langle12\rangle\langle23\rangle\langle34\rangle}\\
 &=\frac{\langle14\rangle^3\langle24\rangle}{D_{1234}}.
\end{aligned}
\tag{81.56}
$$

其中$[23]/[14]=\langle14\rangle/\langle23\rangle$直接来自$s_{23}=s_{14}$。结果与[（81.40）](#eq:c81-quark-four-negative-result)一致。两条路线对图的分配不同，却给相同部分幅，因而同时检查了参考自由度、内部传播子的$i$和顶角的$\sqrt2$。

<span id="c81-quark-color-sum"></span>

## 夸克幅的颜色干涉与螺旋度和

现在令$A_3=A(1_{\bar q},2_q,3,4)$、$A_4=A(1_{\bar q},2_q,4,3)$，这两个下标只区分胶子次序。取[（81.34）](#eq:c81-open-color-chain)的绝对值平方，对两个费米颜色$i_1,i_2$求和，就是取矩阵与其厄米共轭之积的迹。由于$(T^aT^b)^\dagger=T^bT^a$，直接项和干涉项分别为

<span id="eq:c81-quark-color-decomposition"></span>

$$
\begin{aligned}
\sum_{\rm color}|\mathcal T|^2
 &=g^4\bigl[D_{\rm dir}(|A_3|^2+|A_4|^2)
       +D_{\rm int}(A_3^*A_4+A_4^*A_3)\bigr],\\
D_{\rm dir}&=\sum_{a,b}\operatorname{Tr}(T^aT^bT^bT^a),\qquad
D_{\rm int}=\sum_{a,b}\operatorname{Tr}(T^aT^bT^aT^b).
\end{aligned}
\tag{81.42}
$$

这里$a,b$只遍历$N^2-1$个胶子颜色。把[（81.20）](#eq:c81-su-projector)两边接到同一个矩阵$X$上，得$\sum_aT^aXT^a=\operatorname{Tr}X\,\mathbf1_N-X/N$；取$X=\mathbf1_N$，则$\sum_aT^aT^a=C_F\mathbf1_N$，$C_F=(N^2-1)/N$。直接迹先对相邻的两个$T^b$求和，交叉迹则先对隔着$T^b$的两个$T^a$求和，得到

<span id="eq:c81-quark-color-traces"></span>

$$
\begin{aligned}
D_{\rm dir}
 &=C_F\sum_a\operatorname{Tr}(T^aT^a)
 =\frac{(N^2-1)^2}{N},\\
D_{\rm int}
 &=\sum_b\operatorname{Tr}\left[
    \left(\operatorname{Tr}T^b\,\mathbf1_N-\frac{T^b}{N}\right)T^b\right]
 =-\frac{N^2-1}{N}.
\end{aligned}
\tag{81.43}
$$

第二式的第一项因无迹而消失，负号正是完备关系减项的作用。这同时确定了直接项与干涉项的颜色权重。

每次外胶子颜色求和都包含完整连接$\delta_i{}^l\delta_k{}^j$及减项$-\delta_i{}^j\delta_k{}^l/N$。两个颜色指标$a,b$各作一次选择，共有四项。完整写出直接迹的指标，便能逐个数闭环：

<span id="eq:c81-ex-direct-trace-indices"></span>

$$
D_{\rm dir}
 =\sum_{a,b}(T^a)_i{}^j(T^b)_j{}^k
                  (T^b)_k{}^l(T^a)_l{}^i.
\tag{81.57}
$$

对$b$取完整连接，先给$\delta_j{}^l\delta_k{}^k=N\delta_j{}^l$；再对$a$取完整连接，余下两环给$N^2$，故两者全取完整连接时为$N^3$。若$b$改取减项，它给$-\delta_j{}^k\delta_k{}^l/N=-\delta_j{}^l/N$，再收缩完整$a$连接便为$-N$。在$a$上取一次减项给相同结果，两次都取减项则为$1/N$。

交叉迹的字为$abab$。两个完整连接施加$i=l,j=k,j=i,k=l$，使四个指标全部相同，只剩一圈，故为$N$。若只在一个颜色上取减项，另外两个独立指标各自求和，因子为$-N^2/N=-N$；两次减项又只剩一圈，连同$1/N^2$成为$1/N$。结果列为

| 两次投影的选择 | 直接迹$abba$ | 交叉迹$abab$ |
| -------------- | -----------: | -----------: |
| 两个完整连接   |        $N^3$ |          $N$ |
| 仅第一个减项   |         $-N$ |         $-N$ |
| 仅第二个减项   |         $-N$ |         $-N$ |
| 两个减项       |        $1/N$ |        $1/N$ |

四项相加分别为$(N^2-1)^2/N$及$-(N^2-1)/N$，与前面[（81.43）](#eq:c81-quark-color-traces)的逐次矩阵收缩一致。交叉迹的负号来自无迹投影的减项。

对简单代数的不可约表示$R$，还可以用二次卡西米尔得到一般式。定义

<span id="eq:c81-ex-representation-data"></span>

$$
\begin{aligned}
\operatorname{Tr}_R(T_R^aT_R^b)&=T(R)\delta^{ab},\qquad
\sum_aT_R^aT_R^a=C_R\mathbf1_{D(R)},\\
C_RD(R)&=T(R)D(A),\qquad C_A=T(A).
\end{aligned}
\tag{81.58}
$$

卡西米尔与所有生成元对易，由不可约性成为标量；取迹就给第二行第一个关系。二重对易子在伴随表示上作用，故$\sum_a[T_R^a,[T_R^a,T_R^b]]=C_AT_R^b$。把左边的四项展开，得到

<span id="eq:c81-ex-double-commutator"></span>

$$
2C_RT_R^b-2\sum_aT_R^aT_R^bT_R^a=C_AT_R^b,
\qquad
\sum_aT_R^aT_R^bT_R^a
 =\left(C_R-\frac{C_A}{2}\right)T_R^b.
\tag{81.59}
$$

直接迹先收缩相邻的两个$b$生成元，给$C_R^2D(R)$；交叉迹用上式，再对$b$取迹。因此

<span id="eq:c81-ex-general-color-traces"></span>

$$
\begin{aligned}
D_{\rm dir}(R)
 &=C_R^2D(R)=\frac{T(R)^2D(A)^2}{D(R)},\\
D_{\rm int}(R)
 &=\left(C_R-\frac{C_A}{2}\right)C_RD(R)\\
 &=\frac{T(R)^2D(A)^2}{D(R)}-\frac12T(A)T(R)D(A).
\end{aligned}
\tag{81.60}
$$

回到本节基本表示，取$T(R)=1,D(R)=N,D(A)=N^2-1,T(A)=2N$。最后一个数因生成元乘$\sqrt2$而增为旧归一的两倍；代入即恢复[（81.43）](#eq:c81-quark-color-traces)的两个答案。也可将$\kappa=g/\sqrt2$与这些新卡西米尔一同使用，使物理分量耦合不变。

若$R$可约，卡西米尔通常不是全空间的同一个数。令$R=\bigoplus_r n_rR_r$，正确式为

<span id="eq:c81-ex-reducible-color-traces"></span>

$$
D_{\rm dir}(R)=\sum_r n_rC_r^2D(R_r),\qquad
D_{\rm int}(R)=D_{\rm dir}(R)-\frac12T(A)T(R)D(A).
\tag{81.61}
$$

例如基本表示直和一个单态时，总维数为$N+1$、总迹指标仍为1，但单态生成元为零，所以实际直接迹仍为$(N^2-1)^2/N$；把总$D,T$代入不可约式却给$(N^2-1)^2/(N+1)$。各不可约块的二次卡西米尔决定了直接迹；交叉迹的伴随减项只需总迹指标。

还需确定两个颜色次序的相对相位，才能求干涉。交换3、4在边界上的位置时，负螺旋度仍随其原标签走，因此[（81.40）](#eq:c81-quark-four-negative-result)、[（81.41）](#eq:c81-quark-three-negative-result)的分子都不变。只比较循环分母，利用$\langle2|\sum_j\slashed p_j|1]=0$给出的$\langle23\rangle/\langle24\rangle=-[14]/[13]$，有

<span id="eq:c81-quark-relative-phase"></span>

$$
\begin{aligned}
\frac{A_4}{A_3}
 &=\frac{\langle23\rangle\langle34\rangle\langle41\rangle}
        {\langle24\rangle\langle43\rangle\langle31\rangle}
 =-\frac{\langle23\rangle\langle14\rangle}
         {\langle24\rangle\langle13\rangle}\\
 &=\frac{\langle14\rangle[14]}{\langle13\rangle[13]}
 =\frac ut.
\end{aligned}
\tag{81.44}
$$

在$q\bar q\to gg$物理区中，$t,u$均负，比值为正实数。由括号模长，例如$|A_3(3^+,4^-)|^2=|u|^3|t|/(s^2|u|^2)=tu/s^2$；另一种给$t^3/(s^2u)$。两个颜色次序的结果列为

| 指定螺旋度 |            $ |          A_3 |       ^2$ | $   | A_4 | ^2$ | $\operatorname{Re}(A_3^*A_4)$ |
| ---------- | -----------: | -----------: | --------: | --- | --- | --- | ----------------------------- |
| $-++-$     |     $tu/s^2$ | $u^3/(s^2t)$ | $u^2/s^2$ |
| $-+-+$     | $t^3/(s^2u)$ |     $tu/s^2$ | $t^2/s^2$ |

例如第一行的$A_3$模方由$|\langle14\rangle|^6|\langle24\rangle|^2/|D_{1234}|^2=|u|^3|t|/(s^2|u|^2)$给出；$t,u$同负才化成$tu/s^2$。$A_4$模方乘$u^2/t^2$，实干涉则乘$u/t$。另一行将分子换成$|t|^3|u|$，其余运算不变。

对相反费米端点，外链为$\langle2|\cdots|1]$，仍取相互参考$q_3=k_4,q_4=k_3$。为核清共轭时的相位，直接写出三段收缩。先取$+--+$：

<span id="eq:c81-ex-conjugate-first-chain"></span>

$$
\begin{aligned}
\langle2|\slashed\varepsilon_3^-
 &=\frac{\sqrt2\langle23\rangle}{[43]}[4|,
 &\slashed\varepsilon_4^+|1]
 &=\frac{\sqrt2[41]}{\langle34\rangle}|3\rangle,\\
[4|(\slashed p_1+\slashed k_4)|3\rangle
 &=-[41]\langle13\rangle,\\
A(1_{\bar q}^+,2_q^-,3^-,4^+)
 &=\frac{\langle23\rangle[41]^2\langle13\rangle}
        {[43]\langle34\rangle s_{14}}.
\end{aligned}
\tag{81.62}
$$

另一种$+-+-$的相应因子为

<span id="eq:c81-ex-conjugate-second-chain"></span>

$$
\begin{aligned}
\langle2|\slashed\varepsilon_3^+
 &=\frac{\sqrt2\langle24\rangle}{\langle43\rangle}[3|,
 &\slashed\varepsilon_4^-|1]
 &=\frac{\sqrt2[31]}{[34]}|4\rangle,\\
[3|(\slashed p_1+\slashed k_4)|4\rangle
 &=-[31]\langle14\rangle,\\
A(1_{\bar q}^+,2_q^-,3^+,4^-)
 &=\frac{\langle24\rangle[31]^2\langle14\rangle}
        {\langle43\rangle[34]s_{14}}.
\end{aligned}
\tag{81.63}
$$

两个中间式都用了$[44]=0$或$\langle44\rangle=0$，内部动量始终为$p_1+k_4$，没有因改变螺旋度而改换传播通道。每次两份$\sqrt2$与夸克图$1/2$约去，斜线分解的负号与分母的负号相消。

在本物理区，令$\eta_1=\eta_2=-1,\eta_3=\eta_4=1$，第60节的共轭规则是

<span id="eq:c81-ex-negative-energy-conjugation"></span>

$$
\langle ij\rangle^*=\eta_i\eta_j[ji],\qquad
[ij]^*=\eta_i\eta_j\langle ji\rangle.
\tag{81.64}
$$

例如[（81.38）](#eq:c81-quark-positive-three-chain)最后一行分子$[23]\langle41\rangle^2[13]$的共轭为$\langle23\rangle[41]^2\langle13\rangle$：每个混合能量对的$\eta_i\eta_j=-1$与括号反向号相消。分母变成$[43]\langle34\rangle s_{14}$，所以正好是[（81.62）](#eq:c81-ex-conjugate-first-chain)；[（81.41）](#eq:c81-quark-three-negative-result)的未约分式同样变成[（81.63）](#eq:c81-ex-conjugate-second-chain)。两种颜色次序获得同样的共轭规则，表中的模方及实干涉分别重复一次。

将四种非零螺旋度相加，得到

<span id="eq:c81-quark-helicity-sums"></span>

$$
\begin{aligned}
\sum_{\rm hel}(|A_3|^2+|A_4|^2)
 &=\frac{2(t^2+u^2)}{s^2}\left(\frac tu+\frac ut\right)
 =\frac{2(t^2+u^2)^2}{s^2tu},\\
\sum_{\rm hel}(A_3^*A_4+A_4^*A_3)
 &=\frac{4(t^2+u^2)}{s^2}.
\end{aligned}
\tag{81.45}
$$

第一行的2来自相反端点螺旋度，第二行再多一个由$A_3^*A_4+A_4^*A_3=2\operatorname{Re}(A_3^*A_4)$产生的2。将它们代入[（81.42）](#eq:c81-quark-color-decomposition)，先提出共同因子，再用$t^2+u^2=s^2-2tu$，得到

<span id="eq:c81-quark-unpolarized"></span>

$$
\begin{aligned}
\sum_{\rm color,hel}|\mathcal T|^2
 &=\frac{2g^4(N^2-1)(t^2+u^2)}{Ns^2}
   \left[\frac{(N^2-1)(t^2+u^2)}{tu}-2\right]\\
 &=\frac{2g^4(N^2-1)(t^2+u^2)}N
   \left[\frac{N^2-1}{tu}-\frac{2N^2}{s^2}\right],\\
\overline{|\mathcal T_{q\bar q\to gg}|^2}
 &=g^4\left[
 \frac{(N^2-1)^2}{2N^3}\left(\frac tu+\frac ut\right)
 -\frac{N^2-1}{N}\frac{t^2+u^2}{s^2}\right].
\end{aligned}
\tag{81.46}
$$

最后一行除去两个入射费米子各自的$2N$种等权状态。在$N=3$时两系数为$32/27$与$-8/3$，而$t=u=-s/2$处为$28g^4/27$。干涉项虽为负，总结果在物理区为正：$tu/s^2\le1/4$使第二行方括号不小于$2(N^2-2)/s^2$。结果对$t,u$交换不变，正对应两个末态胶子的互换。

从模方到微分截面仍用[第11节的通量和二体相空间](/posts/srednicki-11/#c11)。两个胶子若在全带标号相空间积分，要另除$2!$；[（81.31）](#eq:c81-gluon-unpolarized)和[（81.46）](#eq:c81-quark-unpolarized)已包含初态平均。

<span id="c81-partons"></span>

## 从部分子幅到强子过程

夸克和胶子的有色树幅描述强子碰撞中的短距离部分。当动量转移$Q$远大于强相互作用的长距离尺度时，第73、78节的渐近自由允许在$\mu_R$取$Q$附近，用较小的$g(\mu_R)$计算碰撞的短距离部分。

强子的动量并非由其中某个固定部分子携带。要将硬散射用于强子截面，还要知道部分子带走的纵向动量分数。以$f_{a/H}(x,\mu_F)$记强子$H$中种类$a$的部分子分布函数（parton distribution function），硬碰撞核须对来自两个强子的$x_1,x_2$积分。在可用共线因子化的包容硬过程及所选喷注观测量下，这个结构为

<span id="eq:c81-factorization"></span>

$$
\begin{aligned}
d\sigma_{H_1H_2\to{\rm jets}+X}
 ={}&\sum_{a,b}\int_0^1dx_1\int_0^1dx_2\,
 f_{a/H_1}(x_1,\mu_F)f_{b/H_2}(x_2,\mu_F)\\
 &\times d\widehat\sigma_{ab}(x_1P_1,x_2P_2;\mu_R,\mu_F)
 +\text{随硬标增大受幂压低的贡献}.
\end{aligned}
\tag{81.47}
$$

积分限以硬核中的运动学条件实现实际阈值。最低阶的$d\widehat\sigma_{gg}$、$d\widehat\sigma_{q\bar q}$正由本节振幅、通量与相空间给出。这种因子化适用于硬不变量足够大、对未观测末态作相应包容求和的过程。喷注定义在添加软辐射或将一粒子作共线分裂时保持不变，便满足所需的红外安全性；幂修正的具体阶数取决于观测量。[Collins、Soper 与 Sterman，第1节](https://arxiv.org/pdf/hep-ph/0409313#page=1)介绍了这些条件及分布函数的普适性，第1.3节式(11)、(13)给出双分布卷积与部分子硬截面的关系。

$\mu_R$控制重整化耦合，$\mu_F$规定长距离部分收进分布函数的分界，二者可以同取$Q$。分布函数在一个尺度上的形状需要非微扰输入；微扰理论则可计算它随尺度的演化。因而从一类过程获得分布以后，另一类硬过程的能量、角度与尺度依赖仍可检验同一套量子色动力学。这些分布把部分子计算与强子实验联系起来。下一节将转向长距离问题本身，用威尔逊圈和格点语言讨论禁闭。

---

[← 第 80 节](/posts/srednicki-80/) · [章节地图](/srednicki/) · [第 82 节 →](/posts/srednicki-82/)
