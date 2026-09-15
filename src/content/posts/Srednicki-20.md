---
title: 'Srednicki §20 单圈二粒子弹性散射'
date: 2026-09-14
category: 笔记
tags: [物理, 量子场论, Srednicki]
series: 'Srednicki QFT'
srednickiSections: [20]
hideFromHome: true
draft: false
---

<span id="c20"></span>

上一节把连通函数分解成完整传播子与顶角组成的树；现在用六维$\varphi^3$理论计算二粒子弹性散射，看看这一组织方法怎样把已经求出的圈图变成散射振幅。仍记$\alpha=g^2/(4\pi)^3$，耦合$g$由零外动量三点顶角定义。所谓弹性，是指入射和出射的粒子种类及数目相同。计算先在一般的在壳运动学下进行，得到包含所有一圈修正的参数积分；随后取高能固定角极限，把这些积分算成对数函数，从中看出散射振幅随能量和角度的变化。

<span id="c20-channels"></span>

## 三个通道与一圈截断

先把外部粒子的运动学确定下来。物理动量记为$p_1,p_2\to p_3,p_4$，各粒子都取正能并满足$p_i^2=-m^2$，动量守恒写成$p_1+p_2=p_3+p_4$。顶角函数采用所有动量流入的约定，因此出射粒子的动量在顶角中要取反号：
<span id="eq:c20-incoming-labels"></span>

$$
(k_1,k_2,k_3,k_4)=(p_1,p_2,-p_3,-p_4).
\tag{20.1}
$$

三个交换通道的内线动量平方，可以用Mandelstam变量统一表示：
<span id="eq:c20-mandelstam"></span>

$$
s=-(p_1+p_2)^2,\qquad
t=-(p_1-p_3)^2,\qquad
u=-(p_1-p_4)^2.
\tag{20.2}
$$

这三个变量受到动量守恒的约束。展开右边三项，便有$s+t+u=6m^2-2p_1\cdot p_2+2p_1\cdot(p_3+p_4)=4m^2$。为了看清它们在物理散射区的取值，再到质心系中，令入射空间动量的长度为$p$、散射角为$\theta$，于是
<span id="eq:c20-center-of-mass"></span>

$$
s=4(m^2+p^2),\qquad
t=-2p^2(1-\cos\theta),\qquad
u=-2p^2(1+\cos\theta).
\tag{20.3}
$$

这里用到的只是空间矢量的长度和夹角，因此在本节的五维空间中仍然成立。一般散射有$s>0,t<0,u<0$；到了阈值或前后向，$t,u$还可以等于零。这些边界在后面选择高能固定角极限时会起作用。

运动学确定后，便可用[第19节的四点树装配](/posts/srednicki-19/#c19-trees)写出振幅。四条外腿或者都连在一个完整四点顶角上，或者分成两组，由一条完整内线连接两端的完整三点顶角。后一种情形共有三个外标签分组，恰好对应$s,t,u$三道，如下图所示。

<span id="c20-channel-figure"></span>

![完整四点顶角与 s、t、u 三道交换，双线和圆圈分别表示完整传播子与三点顶角](/images/srednicki/s20-channels.svg)

图20a：完整四点核和三道交换。
方块为$iV_4$，圆圈为$iV_3$，双线为$\widetilde{\boldsymbol\Delta}/i$；
外部短线取单位在壳留数。箭头标示物理动量$p_1,p_2,p_3,p_4$。
右下两条外线交叉处没有顶点。

在每个交换通道中，两端三点核的三个腿平方分别相同，因而它们给出的乘积为$V_3(z)^2$，其中$z=s,t,u$。按照费曼规则，把两个顶角与中间的传播子相乘，其相位为$(iV_3)(\widetilde{\boldsymbol\Delta}/i)(iV_3)
=iV_3^2\widetilde{\boldsymbol\Delta}$。除去散射矩阵元共有的整体$i$后，精确振幅便写成
<span id="eq:c20-full-amplitude"></span>

$$
\mathcal T
=\sum_{z=s,t,u}V_3(z)^2\,
 \widetilde{\boldsymbol\Delta}(-z)
 +V_4(s,t,u).
\tag{20.4}
$$

这时外腿的极点已经截去，每条腿只留下单位留数，场的归一化因而已经包含在上式中。先取各核的最低阶，即$V_3=g$、$V_4=0$、$\widetilde{\boldsymbol\Delta}=\widetilde\Delta_0$，四点核项消失，三个交换项便给出树振幅：
<span id="eq:c20-tree-amplitude"></span>

$$
\mathcal T^{(0)}
=g^2\left[
 \frac1{m^2-s-i0}
+\frac1{m^2-t-i0}
+\frac1{m^2-u-i0}\right].
\tag{20.5}
$$

这也把完整核的写法与[第10节逐腿约化](/posts/srednicki-10/#c10-amputation)所得的三个交换项联系起来：在树级，两端是立方顶点，中间是自由传播子；圈修正则分别进入这些核，并产生非零的四点顶角。

接下来在式[（20.4）](#eq:c20-full-amplitude)中代入各核的一圈表达式。由于分块式包含平方和逆分母，这一步还会产生更高阶乘积，需要再按同一微扰阶数展开。为此，令$a_z=m^2-z-i0$、$v_z=(V_3(z)-g)/g=O(\alpha)$、$\Pi_z=\Pi(-z)=O(\alpha)$。在运动学固定、远离另需重求和的极点时，顶角的平方和传播子的逆分母分别展开为
<span id="eq:c20-one-loop-expansion"></span>

$$
\begin{aligned}
V_3(z)^2&=g^2[1+2v_z+O(\alpha^2)],\\
\frac1{a_z-\Pi_z}
&=\frac1{a_z}
 \left[1+\frac{\Pi_z}{a_z}+O(\alpha^2)\right].
\end{aligned}
\tag{20.6}
$$

把这两式相乘并加入四点核，就能将各类一圈贡献分开。用$O(\alpha)$表示相对于树级所保留的阶数，所得振幅记为$\mathcal T^{[1]}$：
<span id="eq:c20-consistent-one-loop-amplitude"></span>

$$
\mathcal T^{[1]}
=\sum_{z=s,t,u}\frac{g^2}{a_z}
 \left[1+2v_z^{(1)}+\frac{\Pi_z^{(1)}}{a_z}\right]
+V_4^{(1)}(s,t,u).
\tag{20.7}
$$

括号中的因子2来自两个三点顶角：圈修正可以放在左端，也可以放在右端。相乘时产生的$v_z^2,v_z\Pi_z,\Pi_z^2$都已超出一圈阶，故在展开中舍去。这样定义的“一圈振幅”包含树级部分，新增的修正为$O(g^2\alpha)$；后面组装各个显式结果时，也都沿用这一截阶方式。

<span id="c20-parameters"></span>

## 把前面求出的核放到质量壳上

接下来把前面几节的两点、三点和四点函数代入这个振幅。它们虽然含有不同数目的费曼参数，却可以统一采用归一化的参数测度：
<span id="eq:c20-parameter-measure"></span>

$$
dF_n=(n-1)!\prod_{a=1}^n dx_a\,
 \delta\!\left(1-\sum_a x_a\right),\qquad x_a\ge0.
\tag{20.8}
$$

这个归一化的作用，可以直接从参数区域看出。对$x_n$作delta积分时，雅可比为1；其余参数的积分界限依次为$0\le x_1\le1$、$0\le x_2\le1-x_1$，直到$0\le x_{n-1}\le1-x_1-\cdots-x_{n-2}$。这一区域的单纯形体积是$1/(n-1)!$，所以$\int dF_n=1$。测度中的阶乘来自分母的参数合并，图的对称因子仍按原来的图计算。

先看两点核。在第14节的在壳减除式中，内线动量平方取$k^2=-z$。记$a_x=x(1-x)$，动力学分母和减除点的分母便分别成为
<span id="eq:c20-two-point-masses"></span>

$$
D_2(z)=m^2-a_xz,\qquad
D_0=m^2(1-a_x).
\tag{20.9}
$$

由于$0\le a_x\le1/4$，减除分母满足$D_0\ge3m^2/4>0$，对数的支割只须由动力学分母来确定。原减除式中的$-a_x(k^2+m^2)$积分后给出$-\alpha(m^2-z)/12$，因此在壳重整化后的自能为
<span id="eq:c20-on-shell-self-energy"></span>

$$
\Pi^{(1)}(-z)
=\frac{\alpha}{2}\int_0^1dx\,D_2(z)
 \ln\frac{D_2(z)-i0}{D_0}
-\frac{\alpha}{12}(m^2-z).
\tag{20.10}
$$

其中已经包含有限减除项；把它放回传播子时，逆核仍是$m^2-z-i0-\Pi(-z)$。

对于交换图两端的三点核，两条外腿在壳，中间一条腿的平方为$-z$。第16节的参数质量为$m^2+x_1x_3k_1^2+x_2x_3k_2^2+x_1x_2k_3^2$；依次将前两个腿平方置为$-m^2$、第三个置为$-z$，便得到
<span id="eq:c20-on-shell-three-point"></span>

$$
\begin{aligned}
D_3(z)&=-x_1x_2z+[1-(x_1+x_2)x_3]m^2,\\
\frac{V_3(z)}g
&=1-\frac{\alpha}{2}\int dF_3
 \ln\frac{D_3(z)-i0}{m^2}+O(\alpha^2).
\end{aligned}
\tag{20.11}
$$

对数分母中的$m^2$仍由零外动量的耦合减除点决定。这里求值的$V_3(z)$具有两个在壳腿，而三个外动量全零的顶角则用来定义$g$；它们是同一个函数在不同运动学点上的取值。因此，改变外腿运动学以后，原先固定的减除项仍须保留。

四点函数的四个腿平方都取$-m^2$，而每个箱图还保留两个相邻外动量之和的平方。沿用第17节有序首图$1234$的标签，这两个量是$(k_1+k_2)^2=-s$和$(k_2+k_3)^2=(k_1+k_4)^2=-u$。四个单腿项的参数系数相加为$(x_1+x_2)(x_3+x_4)$，于是它们与原来的质量项合并，给出
<span id="eq:c20-first-box-order"></span>

$$
D_{1234}
=m^2[1-(x_1+x_2)(x_3+x_4)]
-x_1x_2s-x_3x_4u.
\tag{20.12}
$$

把两个不变量暂记为一般的自变量，定义
<span id="eq:c20-box-parameter-mass"></span>

$$
D_4(z,w)
=-x_1x_2z-x_3x_4w
+[1-(x_1+x_2)(x_3+x_4)]m^2.
\tag{20.13}
$$

便可把三个箱图的参数分母列在一起：

| 第17节环序 | 在壳参数分母 |
| ---------- | ------------ |
| $1234$     | $D_4(s,u)$   |
| $1324$     | $D_4(t,u)$   |
| $1243$     | $D_4(s,t)$   |

要将这个结果排成通道的循环和，只需对第一项交换参数对$(x_1,x_2)\leftrightarrow(x_3,x_4)$。这一变换保持测度和质量项不变，雅可比绝对值为1，于是积分中的$D_4(s,u)$可改写为$D_4(u,s)$。三个箱图仍各计一次，它们的和为
<span id="eq:c20-on-shell-four-point"></span>

$$
V_4^{(1)}(s,t,u)
=\frac{g^2\alpha}{6}\int dF_4
 \left[
 \frac1{D_4(s,t)-i0}
+\frac1{D_4(t,u)-i0}
+\frac1{D_4(u,s)-i0}\right].
\tag{20.14}
$$

这里的系数$g^2\alpha/6=g^4/[6(4\pi)^3]$来自第17节已求出的六维圈积分，每个固定外标签箱图的对称因子仍为1。这样，参数测度、环序和通道标签都已与前面的结果接上。

把这些核代入式[（20.7）](#eq:c20-consistent-one-loop-amplitude)，便得到任意非奇异在壳运动学的一圈振幅。不过，这时的答案仍包含几个参数积分。为了看清圈修正的能量和角度依赖，下面选取一个能将它们显式算出的极限。

<span id="c20-high-energy"></span>

## 高能固定角下的自能和三点顶角

令$s,|t|,|u|\gg m^2$，同时固定$t/s,u/s$并使它们离开零。由式[（20.3）](#eq:c20-center-of-mass)可见，这要求散射角离开前向和后向。此时各动力学分母只需保留关于$m^2/s$的领先项，因而可略去$D_2,D_3,D_4$中的质量项。定义在壳减除和耦合时所用的$m$则继续作为对数的参照尺度；以下所求的正是原有质量理论在这一条件下的高能渐近式。

质量项略去以后，对数中将直接出现各个不变量。它们在物理区域内有不同的符号，因此先把费曼规定包含在记号中：
<span id="eq:c20-channel-logarithms"></span>

$$
L_z=\operatorname{Log}\frac{-z-i0}{m^2}.
\tag{20.15}
$$

从$s$的正虚部接近物理轴时，$-s$从下方接近负实轴，因此在物理固定角区域，这三个边界值分别为
<span id="eq:c20-physical-logarithms"></span>

$$
L_s=\ln\frac{s}{m^2}-i\pi,\qquad
L_t=\ln\frac{|t|}{m^2},\qquad
L_u=\ln\frac{|u|}{m^2}.
\tag{20.16}
$$

对于负实数$t$本身，如果从上方取边界值，则有$\operatorname{Log}[(t+i0)/m^2]=\ln(|t|/m^2)+i\pi$。后面即使把两个对数写成比值的对数，也要保留这里分别规定的边界值，因为它们决定了振幅的虚部。

先计算自能。用$D_2(s)\simeq-a_xs$代入式[（20.10）](#eq:c20-on-shell-self-energy)，将能量依赖与参数依赖分开，得到
<span id="eq:c20-hard-self-energy-integral"></span>

$$
\Pi^{(1)}(-s)\simeq
-\frac{\alpha s}{2}
 \left[
 L_s\int_0^1a_x\,dx
 +\int_0^1a_x\ln\frac{a_x}{1-a_x}\,dx
 \right]
+\frac{\alpha s}{12}.
\tag{20.17}
$$

其中参数分母的对数已经在第14节式[（14.44）](/posts/srednicki-14/#eq:c14-j1-evaluated)中积分完毕：
<span id="eq:c20-reused-logarithmic-moment"></span>

$$
\int_0^1a_x\ln(1-a_x)\,dx
=-\frac{17}{18}+\frac{\pi}{2\sqrt3}.
\tag{20.18}
$$

余下的是分子所带的参数对数。利用$x\leftrightarrow1-x$的对称性，将$\ln a_x=\ln x+\ln(1-x)$的两项归并，再用$\int_0^1x^r\ln x\,dx=-1/(r+1)^2$逐项积分，便有
<span id="eq:c20-hard-logarithmic-combination"></span>

$$
\begin{aligned}
\int_0^1a_x\ln a_x\,dx
&=2\int_0^1(x-x^2)\ln x\,dx
=2\left(-\frac14+\frac19\right)=-\frac5{18},\\
\int_0^1a_x\ln\frac{a_x}{1-a_x}\,dx
&=\frac23-\frac{\pi}{2\sqrt3}.
\end{aligned}
\tag{20.19}
$$

再用$\int_0^1a_xdx=1/6$积分能量对数的系数，并把有限减除项合进去，常数部分成为$6(2/3-\pi/(2\sqrt3))-1=3-\pi\sqrt3$。这样就得到了高能自能：
<span id="eq:c20-hard-self-energy"></span>

$$
\Pi^{(1)}(-s)\simeq
-\frac{\alpha s}{12}(L_s+3-\pi\sqrt3).
\tag{20.20}
$$

将它代回传播子时，先写成$-s-\Pi(-s)=-s[1+\Pi(-s)/s]$，再对括号取倒数并保留至一阶，得到
<span id="eq:c20-hard-propagator"></span>

$$
\widetilde{\boldsymbol\Delta}(-s)\simeq
-\frac1s
\left[1+\frac{\alpha}{12}(L_s+3-\pi\sqrt3)\right].
\tag{20.21}
$$

这里及以下用$\simeq$同时表示一圈截阶和质量的领先项近似。自能经逆核展开后已化为对自由传播子的乘性修正，现在只需以同样精度求出两端的三点顶角。

三点函数中取$D_3(s)\simeq-sx_1x_2$，对数就分解为$L_s+\ln x_1+\ln x_2$。由于单纯形的$x_1$边际测度是$2(1-x_1)dx_1$，每个参数对数的积分都可化为一维积分，例如
<span id="eq:c20-triangle-log-moment"></span>

$$
\int dF_3\ln x_1
=2\int_0^1(1-x_1)\ln x_1\,dx_1
=2\left(-1+\frac14\right)=-\frac32.
\tag{20.22}
$$

由参数的交换对称性，$x_2$项给出相同结果；能量对数则乘以$\int dF_3=1$。将这三项合起来，便得
<span id="eq:c20-hard-three-point"></span>

$$
\frac{V_3(s)}g\simeq1-\frac{\alpha}{2}(L_s-3).
\tag{20.23}
$$

式中的常数$-3$来自两个参数对数的积分。参数边界上出现的$\ln x_i$仍然可积，故在欧氏域中可以用这些对数控制领先质量极限，再沿同一个费曼解析继续取到物理值。至此，交换图所需的自能和三点核都已经算成显式函数，还剩四点箱图。

<span id="c20-box"></span>

## 箱积分及其对数分支

箱图的参数分母含有两对参数乘积。按交错的参数对换元，可以先积掉两个变量，再对剩余积分中的比例参数求导，求出闭式。

先在欧氏不变量域取$A=-s>0,B=-t>0$，使参数分母为正。无质量箱积分写成
<span id="eq:c20-euclidean-box-integral"></span>

$$
J(A,B)
=6\int_{x_i\ge0}\prod_{i=1}^4dx_i\,
 \frac{\delta(1-\sum_i x_i)}{Ax_1x_2+Bx_3x_4}.
\tag{20.24}
$$

将参数对 $(x_1,x_3)$ 的总量记为 $r$，另一对的总量就是 $1-r$；用 $z,y$ 分别表示各对内部的比例：

<span id="eq:c20-box-jacobian"></span>

$$
\begin{aligned}
x_1&=rz,&x_3&=r(1-z),\\
x_2&=(1-r)y,&x_4&=(1-r)(1-y),\\
\left|\frac{\partial(x_1,x_2,x_3)}{\partial(r,z,y)}\right|
&=\left|\det\begin{pmatrix}
z&r&0\\-y&0&1-r\\1-z&-r&0
\end{pmatrix}\right|=r(1-r).
\end{aligned}
$$

三个新变量都在 $[0,1]$ 内。分母变成 $r(1-r)[Azy+B(1-z)(1-y)]$，消去雅可比中的同一因子后，$r$ 积分给1。剩余分母对 $y$ 为一次式，故

<span id="eq:c20-box-after-y"></span>

$$
\begin{aligned}
\frac{J(A,B)}6
&=\int_0^1dz\int_0^1dy\,
\frac1{Azy+B(1-z)(1-y)}\\
&=\int_0^1dz\,
\frac{\ln[Az/(B(1-z))]}{(A+B)z-B}.
\end{aligned}
$$

在 $z=B/(A+B)$ 处分子分母同时为零，其比值的极限为 $(A+B)/(AB)$；两端的对数也可积。令 $a=A/B$，把对数中的比值本身换成变量 $w=az/(1-z)$，则

<span id="eq:c20-box-ratio-integral"></span>

$$
\begin{aligned}
z&=\frac{w}{a+w},&dz&=\frac{a\,dw}{(a+w)^2},\\
\frac{J(A,B)}6&=\frac{K(a)}{A+B},&
K(a)&=\int_0^\infty dw\,\ln w
\left(\frac1{w-1}-\frac1{w+a}\right).
\end{aligned}
$$

括号中的差在无穷远按 $w^{-2}$ 衰减，$w=1$ 处由 $\ln w$ 消去极点。对正参数 $a$ 求导后令 $w=av$，有

<span id="eq:c20-box-ratio-derivative"></span>

$$
\begin{aligned}
K'(a)
&=\int_0^\infty\frac{\ln w}{(w+a)^2}\,dw
=\frac1a\int_0^\infty\frac{\ln a+\ln v}{(1+v)^2}\,dv\\
&=\frac{\ln a}{a},\qquad
K(a)=\frac12\ln^2a+K(1).
\end{aligned}
$$

其中 $\int_0^\infty dv/(1+v)^2=1$；另一积分在 $v\mapsto1/v$ 下变号，因而为零。求导的被积函数在 $a$ 的任意正紧区间内受 $|\ln w|/(w+a_{\min})^2$ 控制，允许交换求导和积分。

最后求积分常数。把 $K(1)$ 在 $w=1$ 处分开，令上半段的 $w=1/v$，两段就成为相同积分。展开几何级数并逐项积分，得到

<span id="eq:c20-box-integration-constant"></span>

$$
\begin{aligned}
K(1)
&=-4\int_0^1\frac{\ln w}{1-w^2}\,dw
=4\sum_{n=0}^\infty\int_0^1(-\ln w)w^{2n}\,dw\\
&=4\sum_{n=0}^\infty\frac1{(2n+1)^2}
=\frac{\pi^2}{2}.
\end{aligned}
$$

所用的平方倒数和也可由傅里叶系数核对：$x$ 在 $(-\pi,\pi)$ 上的正弦系数为 $b_n=2(-1)^{n+1}/n$，Parseval 等式给出

$$
\frac1\pi\int_{-\pi}^{\pi}x^2dx
=4\sum_{n=1}^{\infty}\frac1{n^2},\qquad
\sum_{n=0}^{\infty}\frac1{(2n+1)^2}
=\left(1-\frac14\right)\frac{\pi^2}{6}
=\frac{\pi^2}{8}.
$$

代回 $J=6K/(A+B)$，便得到

<span id="eq:c20-evaluated-box"></span>

$$
J(A,B)=\frac3{A+B}
 \left[\pi^2+\ln^2\frac AB\right].
\tag{20.25}
$$

例如两个不变量相等时，$J(A,A)=3\pi^2/(2A)>0$；交换$A,B$，闭式保持不变，而将两者同时放大，它按共同尺度的逆一次幂缩小。这些性质也可直接从参数积分看出，并与四点函数的质量维数$-2$相符。

有了有限的闭式，还可以说明欧氏域中为何能把质量取到零。质量项的系数满足$b(x)=1-(x_1+x_2)(x_3+x_4)\ge3/4$，从而$0<1/[D^{(0)}+m^2b]\le1/D^{(0)}$。式[（20.25）](#eq:c20-evaluated-box)表明右边在参数区域内可积，因此支配收敛允许在积分内取领先质量极限。所得函数再按费曼规定延拓，就给出物理不变量下的箱图。

这一延拓也确定了平方对数的分支。在复域中，将$\ln(A/B)$理解为$\operatorname{Log}A-\operatorname{Log}B$，然后令$A=-s-i0,B=-t-i0$。最后，在领先质量阶利用$s+t+u=0$，便得到物理箱积分的两种形式：
<span id="eq:c20-physical-box"></span>

$$
\begin{aligned}
\int\frac{dF_4}{-s x_1x_2-t x_3x_4-i0}
&=-\frac3{s+t}\left[\pi^2+(L_s-L_t)^2\right]\\
&=\frac3u\left[\pi^2+(L_s-L_t)^2\right].
\end{aligned}
\tag{20.26}
$$

例如$L_s-L_t=\ln(s/|t|)-i\pi$，而$L_t-L_u=\ln(|t|/|u|)$；前者有虚部，后者为实数。各通道的平方对数都由这样的对数差来确定。如此便可将欧氏域得到的闭式用于物理散射，同时保留正确的虚部。

<span id="c20-assembly"></span>

## 把三个核合起来

现在所有参数积分都已完成，可以按最初的分块式组装振幅。先处理一个交换通道：由式[（20.23）](#eq:c20-hard-three-point)，两个三点顶角相乘给出$V_3(s)^2/g^2\simeq1-\alpha(L_s-3)$；再乘式[（20.21）](#eq:c20-hard-propagator)，保留至$O(\alpha)$，得到
<span id="eq:c20-exchange-combination"></span>

$$
\frac{V_3(s)^2
 \widetilde{\boldsymbol\Delta}(-s)}{g^2}
\simeq-\frac1s
\left[
1-\frac{11\alpha}{12}L_s
+\frac{\alpha}{12}(39-\pi\sqrt3)
\right].
\tag{20.27}
$$

对数系数中的$-1+1/12=-11/12$，分别来自两个顶角和内线自能；常数项也按同样方式相加，成为$3+(3-\pi\sqrt3)/12$。于是交换图的全部一圈修正已经合在一个括号内。

为了把箱图接到这个结果上，可按最终出现的$1/s$、$1/t$、$1/u$分母将四点核分为三组。其中，与$1/s$交换项同组的是$D_4(t,u)$，因为式[（20.26）](#eq:c20-physical-box)将它的积分写成
<span id="eq:c20-box-in-s-group"></span>

$$
\frac{\alpha}{6}\int
 \frac{dF_4}{D_4(t,u)-i0}
\simeq\frac{\alpha}{2s}
 \left[\pi^2+(L_t-L_u)^2\right].
\tag{20.28}
$$

把这一项加到式[（20.27）](#eq:c20-exchange-combination)上，平方对数与常数分别归并，括号中的常数变为$\alpha(39-\pi\sqrt3-6\pi^2)/12$。为简化最后的表达式，定义
<span id="eq:c20-finite-constant"></span>

$$
c=\frac{6\pi^2+\pi\sqrt3-39}{11}
=2.3326385908\ldots,
\tag{20.29}
$$

再加上另外两个通道的循环项，所得振幅为
<span id="eq:c20-final-hard-amplitude"></span>

$$
\begin{aligned}
\mathcal T^{[1]}_{\rm hard}
&=g^2[F(s,t,u)+F(t,u,s)+F(u,s,t)],\\
F(s,t,u)
&=-\frac1s\left\{
1-\frac{11\alpha}{12}(L_s+c)
-\frac{\alpha}{2}(L_t-L_u)^2
\right\}.
\end{aligned}
\tag{20.30}
$$

每个$F$在最后两个变量互换时保持不变，所以三个循环项的和对全部三道置换对称，正好满足相同实标量的交换对称性。每一项又都带有一个逆不变量，因而$[\mathcal T]=-2$。圈修正保留了树振幅的对称性和量纲，同时在其能量与角度依赖中引入了对数及平方对数。

这个闭式给出固定角下的质量领先项及一圈修正。取 $\alpha\ll1$、$\alpha|\ln(s/m^2)|\ll1$，高阶耦合项受到抑制；质量修正按 $m^2/s$ 的幂及其对数趋零。

<span id="c20-right-angle"></span>

## 一个直角散射的例子

作为补充，考察$\theta=\pi/2$的高能散射，看看这些对数怎样进入可测的散射率。这时$t=u=-s/2$。记$L=\ln(s/m^2)$，三个边界对数便是$L_s=L-i\pi$、$L_t=L_u=L-\ln2$。由于后两者相等，$s$组中的平方对数为零；另外两组相同，其中的平方对数可展开为
<span id="eq:c20-right-angle-log-square"></span>

$$
(L-\ln2-L+i\pi)^2
=\ln^22-\pi^2-2i\pi\ln2.
\tag{20.31}
$$

把各项代入三个$F$，树级部分的系数相加为$-1+2+2=3$，能量对数的系数相加为$11/12-44/12=-11/4$。再将实部和虚部分开，便可写成
<span id="eq:c20-right-angle-amplitude"></span>

$$
\begin{aligned}
\mathcal T^{[1]}_{\rm hard}\big|_{\pi/2}
&=\frac{g^2}{s}
 \left[3+\alpha R_{90}(L)
 +i\pi\alpha\left(4\ln2-\frac{11}{12}\right)\right],\\
R_{90}(L)
&=-\frac{11}{4}(L+c)
 +\frac{11}{3}\ln2-2\ln^22+2\pi^2.
\end{aligned}
\tag{20.32}
$$

这里的虚部从一圈开始出现，来自物理$s$道的费曼边界及箱图中的对数差。它在振幅中与实部一同存在，但进入这一阶截面的方式，还要由振幅与共轭的乘积来确定。

在同一能量和角度比较圈修正前后的微分截面，相空间和通量因子会相消。树振幅为实数$3g^2/s$，因此只需将$\mathcal T^{(0)}+\delta\mathcal T$与其共轭相乘，并保留至一阶，得到
<span id="eq:c20-right-angle-cross-section-ratio"></span>

$$
\left.
\frac{d\sigma^{[1]}}{d\sigma^{(0)}}\right|_{\pi/2}
=1+\frac{2\alpha}{3}R_{90}(L)+O(\alpha^2)
\tag{20.33}
$$

这里仍取相同的领先质量近似。一圈虚部的平方属于相对$O(\alpha^2)$，所以当前阶数的截面修正由实部与树振幅的干涉给出。振幅中的对数依赖由此转化为散射率随能量和角度的变化。

---

[← 第 19 节](/posts/srednicki-19/) · [章节地图](/srednicki/) · [第 21 节 →](/posts/srednicki-21/)
