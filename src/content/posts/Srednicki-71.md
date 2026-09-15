---
title: 'Srednicki §71 非阿贝尔规范理论的路径积分'
date: 2026-09-14
category: 笔记
tags: [物理, 量子场论, Srednicki]
series: 'Srednicki QFT'
srednickiSections: [71]
hideFromHome: true
draft: false
---

<span id="c71"></span>

在第57节计算光子的路径积分时，我们先去掉了规范变换造成的重复积分。
这一步之所以容易，是因为每个动量下的规范方向都沿着同一个四矢量$k_\mu$。
杨—米尔斯场的规范变换还含有场本身，重复积分的方向也随场而变。
我们需要一种能随这些方向选取积分面的办法。由此产生的雅可比因子将留在积分中，
并可用第53节的格拉斯曼高斯积分写成一个新的局域作用量。
这个作用量中的辅助场就是费德耶夫—波波夫鬼场。

以下沿用[第69节的规范变换](/posts/srednicki-69/#c69)，并用[第53节的泛函行列式](/posts/srednicki-53/#c53)将换元因子写入作用量。

<span id="c71-orbit"></span>

## 规范轨道的方向

从纯规范场的作用量开始，记

<span id="eq:c71-start"></span>

$$
\begin{aligned}
S_0[A]&=-\frac14\int d^4x\,F^{a\mu\nu}F_{\mu\nu}^a,\\
S_{\rm YM}[A,J]&=S_0[A]+\int d^4x\,J^{a\mu}A_\mu^a,\\
Z[J]&\propto\int\mathcal DA\,e^{iS_{\rm YM}[A,J]} .
\end{aligned}
\tag{71.1}
$$

相互规范等价的场给出同一个物理配置，
所以最后一行尚须规定怎样处理这份重复。我们先取$J=0$完成这一步，
再在选定的规范中引入一般源。$S_0$沿规范轨道不变，
而固定的线性源通常不具有这个性质，稍后会直接算出它的变化。

沿第69节的负相位约定，$A_\mu=A_\mu^aT^a$的有限变换为

<span id="eq:c71-finite"></span>

$$
\begin{gathered}
A_\mu^U=UA_\mu U^\dagger+\frac{i}{g}U\partial_\mu U^\dagger,\\
U=I-ig\theta+O(\theta^2),\qquad
U^\dagger=I+ig\theta+O(\theta^2),\qquad \theta=\theta^aT^a .
\end{gathered}
\tag{71.2}
$$

这里$\theta$恢复第69节的规范参数；上一节把$g$吸收进了群参数。
把两个一阶展开分别代入第一行，有
$UA_\mu U^\dagger=A_\mu+ig(A_\mu\theta-\theta A_\mu)+O(\theta^2)$，
而$(i/g)U\partial_\mu U^\dagger=-\partial_\mu\theta+O(\theta^2)$。
第二项的负号来自两个$i$相乘。因此

<span id="eq:c71-infinitesimal"></span>

$$
\begin{aligned}
\delta_\theta A_\mu
&=ig[A_\mu,\theta]-\partial_\mu\theta,\\
\delta_\theta A_\mu^a
&=-\partial_\mu\theta^a-gf^{abc}A_\mu^b\theta^c
=-D_\mu^{ac}\theta^c,\\
D_\mu^{ac}
&=\delta^{ac}\partial_\mu-igA_\mu^b(T_A^b)^{ac}
=\delta^{ac}\partial_\mu+gf^{abc}A_\mu^b .
\end{aligned}
\tag{71.3}
$$

第二行先用了$[T^b,T^c]=if^{bca}T^a$，再作循环置换
$f^{bca}=f^{abc}$。最后一行则用$(T_A^b)^{ac}=-if^{bac}$：
$(-i)(-i)=-1$，再把$f^{bac}$交换前两个指标，便得到正的连接系数。
规范轨道的切向变化因而由伴随协变导数确定。

为看清它与光子情形的区别，对所有场采用$e^{ikx}$的傅里叶展开。
导数项给$ik_\mu$，乘积项给卷积，于是

<span id="eq:c71-orbit-fourier"></span>

$$
\delta_\theta A_\mu^a(k)
=-ik_\mu\theta^a(k)
-gf^{abc}\int\frac{d^4q}{(2\pi)^4}
 A_\mu^b(q)\theta^c(k-q).
\tag{71.4}
$$

若$f=0$，每个动量的规范变化都沿$k_\mu$，正是第57节去掉的方向。
第二项出现以后，不同动量的规范参数由背景场联系起来，变化一般不再平行于$k_\mu$。
因此需要沿每个场配置自己的规范轨道选代表。下面的普通积分先说明选取代表时
为何必须补上一个雅可比因子。

<span id="c71-finite-integral"></span>

## 在普通积分中选取代表

设作用量只依赖$x$，另一个变量$y$任意变化都不改变它。
比较下列三种写法：

<span id="eq:c71-redundant-integral"></span>

$$
\begin{aligned}
\int dx\,dy\,e^{iS(x)}
&=\left(\int dy\right)\int dx\,e^{iS(x)},\\
Z&:=\int dx\,e^{iS(x)}
=\int dx\,dy\,\delta(y)e^{iS(x)}\\
&=\int dx\,dy\,\delta\bigl(y-f(x)\bigr)e^{iS(x)} .
\end{aligned}
\tag{71.5}
$$

第一行的$y$积分是重复计数的体积。第二行定义除去这份体积后的积分，
最后一行说明每条平行于$y$轴的直线上可以任取一点$y=f(x)$。
取有限的$y$方向体积，并给$x$积分加上共同的振荡积分调节，就能逐项完成这些换元。

选取这些点时，未必能显式解出$f(x)$。设我们只知道一个条件$G(x,y)=0$，
并且对每个$x$，它在考虑的范围内有唯一简单根$y=f(x)$。
固定$x$，在根附近令$z=G(x,y)$，便有
$|dy/dz|=|\partial_yG|^{-1}$。将δ函数作用于一个测试函数$h(y)$，
换元给出

<span id="eq:c71-delta-jacobian"></span>

$$
\begin{aligned}
\int dy\,h(y)\delta(G(x,y))
&=\int dz\,
\frac{h(y(x,z))}{|\partial_yG(x,y(x,z))|}\,\delta(z)\\
&=\frac{h(f(x))}{|\partial_yG(x,f(x))|},\\
\delta(G(x,y))
&=\frac{\delta(y-f(x))}{|\partial_yG(x,f(x))|}.
\end{aligned}
\tag{71.6}
$$

分母取在根处；若把它写成$y$的函数乘在δ函数旁边，
δ函数的支撑仍使它只取这个值。因而

<span id="eq:c71-positive-jacobian"></span>

$$
Z=\int dx\,dy\,|\partial_yG|\,
\delta(G(x,y))\,e^{iS(x)}.
\tag{71.7}
$$

若进一步选定根处$\partial_yG>0$的定向，就可以去掉绝对值。
这个条件与唯一根条件都将在规范场的推广中起作用。

若有$n$个冗余变量$y^j$，就需要$n$个独立条件$G_i(x,y)=0$。
记$J_i{}^j=\partial G_i/\partial y^j$，在唯一根$f(x)$处要求$\det J\ne0$。
普通多变量换元$d^ny=d^nz/|\det J|$同样给出

<span id="eq:c71-multivariate"></span>

$$
\begin{aligned}
\delta^{(n)}(G(x,y))
&=\frac{\delta^{(n)}(y-f(x))}{|\det J(x,f(x))|},\\
Z&=\int d^mx\,d^ny\,
|\det J|\,\delta^{(n)}(G(x,y))\,e^{iS(x)} .
\end{aligned}
\tag{71.8}
$$

固定冗余所需的独立条件数等于冗余方向数$n$，而物理变量仍可有$m$个。如果同一条轨道有几个简单交点，
δ函数换元的结果应当对各根求和，每个交点都会被计入一次。
如果行列式为零，局部逆变换则不存在。因此上述公式自然要求我们先在
交点唯一、雅可比因子非奇异的一片范围内工作。

<span id="c71-faddeev-popov"></span>

## 规范条件与轨道体积

现在以所有$A_\mu^a(x)$代替全部$x,y$，以局部规范参数$\theta^a(x)$
代替冗余变量$y$。选择条件

<span id="eq:c71-gauge-condition"></span>

$$
\mathcal F^a[A](x)=\partial^\mu A_\mu^a(x),\qquad
G^a[A;\omega](x)=\mathcal F^a[A](x)-\omega^a(x)=0.
\tag{71.9}
$$

$\omega^a(x)$暂时是任意指定的实函数。每个颜色和每个时空点各有一个条件，
正好对应一个规范参数。它们在场配置空间中选出一个截面，
也就是从所考虑的每条规范轨道上选出一个代表。
条件对轨道方向的变化率定义为

<span id="eq:c71-fp-definition"></span>

$$
M^{ab}[A](x,y)
:=\left.
\frac{\delta G^a[A^\theta;\omega](x)}
     {\delta\theta^b(y)}\right|_{\theta=0}.
\tag{71.10}
$$

这个核的行指标为$(a,x)$，列指标为$(b,y)$。
它的行列式称为费德耶夫—波波夫行列式。我们将在下一小节求出它，
先用它把去掉轨道体积的步骤写全。

选择与规范变换相容的边界及测度，除去未被条件固定的残余变换。
例如边界上可要求规范参数为零；若仍有零模，还要单独固定相应自由度。
在零场附近采用$M$可逆、轨道与截面相交一次的局部构造，
并在共同调节下假定$\mathcal DA$和$S_0$规范不变。
有限维换元于是成为

<span id="eq:c71-fp-unity"></span>

$$
1=\int\mathcal Dh\,
\delta\bigl(\mathcal F[A^h]-\omega\bigr)\,
|\det M[A^h]| .
\tag{71.11}
$$

这里$\delta(\mathcal F-\omega)$简写$\prod_{x,a}\delta(\mathcal F^a(x)-\omega^a(x))$。
在群元$h$附近以左乘$u_\theta h$作坐标，因为
$A^{u_\theta h}=(A^h)^{u_\theta}$，式中变化率恰是
式[（71.10）](#eq:c71-fp-definition)在$A^h$处的值。
群测度采用与这一坐标相容的哈尔密度。这使式[（71.11）](#eq:c71-fp-unity)
成为前面雅可比因子公式的直接推广。

设$O[A]$是规范不变的插入。将这个单位因子放入积分，再对每个$h$作
$B=A^h$的变元，得到

<span id="eq:c71-orbit-volume"></span>

$$
\begin{aligned}
I[O]&:=\int\mathcal DA\,O[A]e^{iS_0[A]}\\
&=\int\mathcal Dh\int\mathcal DB\,
 \delta(\mathcal F[B]-\omega)\,|\det M[B]|\,
 O[B]e^{iS_0[B]}\\
&=\mathcal V_{\rm gauge}\int\mathcal DA\,
 \delta(\mathcal F[A]-\omega)\,|\det M[A]|\,
 O[A]e^{iS_0[A]} .
\end{aligned}
\tag{71.12}
$$

第二行不再含$h$，它的积分便给出规范体积$\mathcal V_{\rm gauge}$。
积分域也随$B=A^h$一起变换。
除去这个体积，再用$O=1$的积分归一化，物理平均值就写成

<span id="eq:c71-fixed-slice"></span>

$$
\langle O\rangle
=\frac{\int\mathcal DA\,\det M[A]\,
 \delta(\mathcal F[A]-\omega)\,O[A]e^{iS_0[A]}}
 {\int\mathcal DA\,\det M[A]\,
 \delta(\mathcal F[A]-\omega)e^{iS_0[A]}} .
\tag{71.13}
$$

在这同一连通规范片内，$\sigma_0=\operatorname{sgn}\det M$保持不变，
所以$|\det M|=\sigma_0\det M$中的固定号在分子分母中相消。
先对受调节的实核固定定向，再沿共同的解析路径取真空边界值。微扰展开在上述行列式非零、交点唯一的规范片内进行。

固定的一般线性源不能直接放进$O$的位置。由式[（71.3）](#eq:c71-infinitesimal)
并作一次分部积分，

<span id="eq:c71-source-variation"></span>

$$
\begin{aligned}
\delta_\theta\int d^4x\,J^{a\mu}A_\mu^a
&=-\int d^4x\,J^{a\mu}
 \left(\partial_\mu\theta^a+gf^{acb}A_\mu^c\theta^b\right)\\
&=\int d^4x\,\theta^b
 \left(\partial_\mu J^{b\mu}
       +gf^{bca}A_\mu^cJ^{a\mu}\right).
\end{aligned}
\tag{71.14}
$$

边界项按同一边界条件消去，连接项用了$f^{acb}=-f^{bca}$。
即使$\partial_\mu J^{b\mu}=0$，非阿贝尔连接项一般仍存在。
因此在已选规范中定义含源泛函

<span id="eq:c71-fixed-source"></span>

$$
Z_\omega[J]
:=\frac{\int\mathcal DA\,\det M[A]\,\delta(\mathcal F[A]-\omega)\,
 e^{iS_0[A]+i\int d^4x\,J^{a\mu}A_\mu^a}}
{\int\mathcal DA\,\det M[A]\,\delta(\mathcal F[A]-\omega)\,e^{iS_0[A]}} .
\tag{71.14a}
$$

这个泛函产生的规范场关联函数可以依赖所选截面。

<span id="c71-kernel"></span>

## 求出费德耶夫—波波夫核

现在将式[（71.3）](#eq:c71-infinitesimal)代入规范条件。
$\omega$固定不变，所以

<span id="eq:c71-fp-kernel"></span>

$$
\delta_\theta G^a[A;\omega](x)
=-\partial^\mu\!\left(D_\mu^{ab}\theta^b\right)(x),
\qquad
M^{ab}(x,y)
=-\partial_x^\mu D_\mu^{ab}(x)\delta^4(x-y).
\tag{71.15}
$$

其中所有微分都作用于$x$，包括外面的$\partial_x$。
把它完全展开，可以看见两个不同的导数项：

<span id="eq:c71-expanded-kernel"></span>

$$
\begin{aligned}
M^{ab}(x,y)
={}&-\delta^{ab}\partial_x^2\delta^4(x-y)\\
&-gf^{acb}\left[
(\partial^\mu A_\mu^c(x))\delta^4(x-y)
+A_\mu^c(x)\partial_x^\mu\delta^4(x-y)\right].
\end{aligned}
\tag{71.16}
$$

为检验核的方向，将它作用于普通的光滑参数$v^b(y)$，先完成$y$积分：

<span id="eq:c71-kernel-test"></span>

$$
\begin{aligned}
\int d^4y\,M^{ab}(x,y)v^b(y)
&=-\partial^2v^a
-gf^{acb}\left[(\partial^\mu A_\mu^c)v^b
              +A_\mu^c\partial^\mu v^b\right]\\
&=-\partial^\mu\left(\partial_\mu v^a
                  +gf^{acb}A_\mu^cv^b\right).
\end{aligned}
\tag{71.17}
$$

这确实是$-\partial^\mu D_\mu v$。若把$\partial^\mu D_\mu$换成
$D_\mu\partial^\mu$，便会漏掉$(\partial\cdot A)v$，在一般$\omega$下不能这样做。
从量纲也能核对这一式：$[G]=2$、$[\theta]=0$，
$M$作为微分算符的维数为2；式中另含一个维数4的δ函数，故双点核的维数为6。

<span id="c71-ghost"></span>

## 把行列式写成鬼场积分

在式[（71.13）](#eq:c71-fixed-slice)中，行列式还在指数以外。
第53节已经说明，普通复变量的高斯积分产生逆行列式，
复格拉斯曼变量的积分则产生行列式本身。因此对每个伴随指标引入
两个独立的奇积分变量$c^a(x),\bar c^a(x)$。用横线区分反鬼$\bar c$与鬼$c$；积分时它们是第44节所定义的两组独立生成元。

先在有限基底中把时空和颜色合成$I=1,\ldots,n$。
固定配对测度，使单对积分
$\int dc\,d\bar c\,\bar c c=1$，则
[复格拉斯曼高斯公式](/posts/srednicki-44/#c44-determinant)在本节的代入为

<span id="eq:c71-ghost-determinant"></span>

$$
\begin{aligned}
\int\prod_{I=n}^{1}(dc_I\,d\bar c_I)\,
e^{-i\bar c_I M_{IJ}c_J}
&=\det(-iM)=(-i)^n\det M,\\
S_{\rm gh}
&=-\int d^4x\,d^4y\,
\bar c^a(x)M^{ab}(x,y)c^b(y).
\end{aligned}
\tag{71.18}
$$

这里选$-iM$，是为了在指数中写$iS_{\rm gh}$并得到熟悉的标量动能号。
例如一对变量时，指数只有$1-i\bar cMc$两项，积分直接等于$-iM$。
一般$n$对的相位$(-i)^n$在共同的模式调节下与$A$无关，
因此在零源归一比中消去。实际运算始终使用上式的配对测度次序，保证奇变量积分的符号固定。

将式[（71.15）](#eq:c71-fp-kernel)代入第二行，先积掉$y$，得到
$S_{\rm gh}=\int d^4x\,\bar c^a\partial^\mu(D_\mu^{ab}c^b)$。
对外层导数作一次分部积分，

<span id="eq:c71-ghost-boundary"></span>

$$
\begin{aligned}
S_{\rm gh}
={}&\int_{\partial\Omega}d\Sigma^\mu\,
 \bar c^aD_\mu^{ab}c^b\\
&-\int d^4x\,(\partial^\mu\bar c^a)D_\mu^{ab}c^b .
\end{aligned}
\tag{71.19}
$$

$\partial_\mu$是偶微分，上式没有交换$c$与$\bar c$。
在所选边界条件下第一行消失，便得到鬼场拉格朗日量：

<span id="eq:c71-ghost-lagrangian"></span>

$$
\begin{aligned}
\mathcal L_{\rm gh}
&=-(\partial^\mu\bar c^a)D_\mu^{ab}c^b\\
&=-\partial^\mu\bar c^a\partial_\mu c^a
 +ig(\partial^\mu\bar c^a)A_\mu^c(T_A^c)^{ab}c^b\\
&=-\partial^\mu\bar c^a\partial_\mu c^a
 +gf^{abc}A_\mu^c(\partial^\mu\bar c^a)c^b .
\end{aligned}
\tag{71.20}
$$

最后一步用$(T_A^c)^{ab}=-if^{cab}$，
所以$i(-i)=1$，再用$f^{cab}=f^{abc}$。
$A$是偶变量，移到前面不生负号。第一项与复标量的动能具有相同形式，
第二项则使鬼场与规范场相互作用。给$c,\bar c$各取质量维数1，
两项的维数都为4，耦合$g$仍无量纲。

鬼场的自由收缩也可直接由行列式求得。对有限矩阵元$M_{IJ}$求导，
行列式一侧给逆矩阵元，指数一侧给$-i\bar c_Ic_J$的平均值。
两者相等，便有

<span id="eq:c71-ghost-propagator"></span>

$$
\begin{aligned}
\frac{\partial\log\det(-iM)}{\partial M_{IJ}}
&=(M^{-1})_{JI}=-i\langle\bar c_Ic_J\rangle,\\
\langle\bar c_Ic_J\rangle&=i(M^{-1})_{JI},\\
\langle c_J\bar c_I\rangle&=-i(M^{-1})_{JI},\\
\langle c^a(x)\bar c^b(y)\rangle_0
&=\frac{\delta^{ab}}{i}\int\frac{d^4k}{(2\pi)^4}
 \frac{e^{ik(x-y)}}{k^2-i0}.
\end{aligned}
\tag{71.21}
$$

第二个收缩的负号来自交换两个奇变量。
自由核是$M_0=-\partial^2$，其逆采用与先前传播子相同的费曼边界值。
残余零模在求逆前已另行处理。有限贝雷津积分本身是多项式运算，
这里的极点处方来自真空传播的选择。

为便于下面说明鬼外线的含义，还可从相互作用直接读出一个顶角。
把三个傅里叶因子按$A_\mu^c(k)\bar c^a(r)c^b(p)$的次序排列，
全部动量入顶，则

<span id="eq:c71-ghost-vertex"></span>

$$
\begin{aligned}
iS_{\rm gh,int}
={}&-g f^{abc}\int
\frac{d^4k\,d^4r\,d^4p}{(2\pi)^{12}}\,
(2\pi)^4\delta^4(k+r+p)\\
&\hspace{18mm}\times
r^\mu A_\mu^c(k)\bar c^a(r)c^b(p),\\
\mathcal V^{abc,\mu}_{A\bar c c}(k,r,p)
&=-gf^{abc}r^\mu .
\end{aligned}
\tag{71.22}
$$

导数只作用于$\bar c$，给$ir^\mu$；指数展开再给一个$i$，相乘便是负号。
若用$\bar c$端的出顶动量$q=-r$表示，这个系数成为$+gf^{abc}q^\mu$。
动量方向和奇变量次序都固定后，符号便随之确定。

<span id="c71-loops"></span>

## 为什么每个鬼闭圈多一个负号

鬼场是格拉斯曼变量，因此虽然没有旋量指标，闭圈的统计符号仍与费米场相同。
用刚得到的行列式可以直接看到这一点。写
$M[A]=M_0+V[A]$，并用零背景鬼积分归一，则

<span id="eq:c71-ghost-trace-log"></span>

$$
\begin{aligned}
\frac{Z_{\rm gh}[A]}{Z_{\rm gh}[0]}
&=\frac{\det M[A]}{\det M_0}
=\det(1+X),\qquad X=M_0^{-1}V[A],\\
\log\frac{Z_{\rm gh}[A]}{Z_{\rm gh}[0]}
&=\operatorname{Tr}\log(1+X)
=\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}n
 \operatorname{Tr}X^n .
\end{aligned}
\tag{71.23}
$$

这里应用的是[第53节的矩阵对数推导](/posts/srednicki-53/#c53-trace-log)，
将那里的$G_\chi$换成$-X$即可。
在有限矩阵范数$\|X\|<1$时级数收敛；微扰论中则按受调节的逐阶展开使用。
迹包括颜色和时空指标。具体地，

<span id="eq:c71-closed-chain"></span>

$$
\begin{aligned}
\operatorname{Tr}X^n
=\int\prod_{j=1}^n d^4x_j\,
X^{a_1a_2}(x_1,x_2)\cdots
X^{a_na_1}(x_n,x_1).
\end{aligned}
\tag{71.24}
$$

每个$X$含一个自由传播核和一个背景规范场插入，指标首尾相接形成有向圈。
选择圈上的起点有$n$种重复，正是系数$1/n$；
这一计数已在[第53节的闭合传播链](/posts/srednicki-53/#c53-cycles)中由$(n-1)!/n!$求出。
若将$c,\bar c$换成同一二次核的普通复标量，高斯积分给
$\det(1+X)^{-1}$，故其对数中每个连通圈恰与上式相差一个负号。
这就是闭鬼圈额外的$-1$。复鬼是两组独立奇变量，
这里没有实马约拉纳积分的二分之一权重，也没有旋量迹。

在本节的线性规范中取阿贝尔极限$f^{abc}=0$，便有
$D_\mu=\partial_\mu$、$M=-\partial^2=M_0$，所以$X=0$，
鬼积分的归一比等于一。鬼与规范场的顶角也同时消失。
因此第57节的光子路径积分可以把这份自由鬼积分吸收到归一化常数中。
非阿贝尔理论的$M$依赖$A$，上述闭圈则必须随规范场的其它图一起计算。

<span id="c71-physical"></span>

## 辅助鬼场与物理外态

鬼场在这里的任务是表示规范轨道的雅可比因子。它是洛伦兹标量而服从奇统计，
因而不能把它当作满足通常自旋—统计条件的正范数物理粒子。
物理态的选择还须结合规范场的非物理极化，具体构造见[第74节](/posts/srednicki-74/#c74)。
辅助鬼场的关联函数及其截肢核本身可以非零；下面由已得到的作用量算一个例子。

取$SU(2)$，$f^{abc}=\epsilon^{abc}$。
两个入射规范场的颜色都为3，末端$\bar c$和$c$的颜色都为1。
令$E>0$，入射动量和极化、出射鬼端动量分别为

<span id="eq:c71-ghost-example-kinematics"></span>

$$
\begin{gathered}
k_1=(E,0,0,E),\qquad k_2=(E,0,0,-E),\\
\varepsilon_1=\varepsilon_2=(0,1,0,0),\\
p=(E,E,0,0),\qquad q=(E,-E,0,0).
\end{gathered}
\tag{71.25}
$$

四个动量都在零质量壳上，$k_1+k_2=p+q$，两入射极化都与其动量正交。
把$\bar c$端的全入动量记作$r=-q$。
两个规范场在三规范场顶点先汇合的图含有$f^{33b}=0$，所以为零；
式[（71.20）](#eq:c71-ghost-lagrangian)也没有$AA\bar c c$接触项。
在$g^2$阶，剩下的是沿鬼线先后接入$k_1,k_2$的两个排列，内部颜色都是2。

先让$k_1$接在外部$\bar c$的一端。该顶角的颜色为$(a,b,c)=(1,2,3)$；
另一顶角为$(2,1,3)$，其$\bar c$动量是$k_1-q$。逐项代入
式[（71.22）](#eq:c71-ghost-vertex)，有

<span id="eq:c71-ghost-example-factors"></span>

$$
\begin{aligned}
-g\epsilon^{123}\,r\cdot\varepsilon_1&=-gE,\\
-g\epsilon^{213}\,(k_1-q)\cdot\varepsilon_2&=+gE,\\
(q-k_1)^2&=(0,-E,0,-E)^2=2E^2 .
\end{aligned}
\tag{71.26}
$$

交换$k_1,k_2$后，内线的$z$分量反号，但平方、顶角及极化缩并都相同。
两个规范场是偶变量，两种排列相加。沿固定的$A\bar c c$及有向收缩次序，
截肢树核于是为

<span id="eq:c71-nonzero-ghost-kernel"></span>

$$
\begin{aligned}
\mathscr K_{\bar c c;AA}
&=(-gE)\frac{-i}{2E^2-i0}(+gE)
+(-gE)\frac{-i}{2E^2-i0}(+gE)\\
&\longrightarrow ig^2 .
\end{aligned}
\tag{71.27}
$$

相互作用展开的$1/2!$与两个顶点标签的交换相消，留下的正是这两个规范场排列。
图中没有闭鬼圈，因而没有额外的圈负号。统一调换外部奇变量的次序只改变共同号，
不会使结果消失。这个非零截肢核参与规范场非物理极化与鬼场的抵消；物理外态的定义将在[第74节](/posts/srednicki-74/#c74)给出。

<span id="c71-average"></span>

## 对规范条件作高斯平均

回到式[（71.13）](#eq:c71-fixed-slice)。在上述零源或规范不变插入的范围内，
改变$\omega$只是改变每条轨道上所选的代表，因而不改变物理平均值。
于是可给$\omega$一个权重并对它积分。取权重

<span id="eq:c71-omega-weight"></span>

$$
W_\xi[\omega]
=\exp\!\left[-\frac{i}{2\xi}
\int d^4x\,\omega^a(x)\omega^a(x)\right],
\qquad \xi\ne0 .
\tag{71.28}
$$

$\xi$是无量纲的规范参数。对实$\omega$，这是振荡高斯权重，
可先加上$-\eta\int\omega^2/2$的阻尼，$\eta>0$，再取菲涅耳边界值；
等价地，指数中的$\xi^{-1}$先取$\xi^{-1}-i\eta$。
这个共同的权重积分只改归一化常数。

由于$\omega$在δ函数中以系数$-1$出现，换元的绝对雅可比因子为一，
每个时空和颜色分量的积分直接将$\omega$换成$\mathcal F[A]$：

<span id="eq:c71-gauge-fixing-action"></span>

$$
\begin{aligned}
&\int\mathcal D\omega\,W_\xi[\omega]\,
\delta(\mathcal F[A]-\omega)\\
&\qquad=\exp\!\left[-\frac{i}{2\xi}
\int d^4x\,(\partial^\mu A_\mu^a)(\partial^\nu A_\nu^a)\right]
 =e^{iS_{\rm gf}[A]},\\
S_{\rm gf}&=\int d^4x\,\mathcal L_{\rm gf},\\
\mathcal L_{\rm gf}
&=-\frac1{2\xi}(\partial^\mu A_\mu^a)(\partial^\nu A_\nu^a).
\end{aligned}
\tag{71.29}
$$

高斯权重的负号和$1/2$保留在指数中，选定截面的δ泛函由此变成局域规范固定项。
$\xi=0$须以原来的严格δ条件或相应极限理解。
自由场二次项现在与第57节的协变规范相同，只是多了一个颜色单位阵；
因此同一求逆步骤可以给出规范场的自由传播子。

在这个固定规范的积分中加入一般外源，并令$Z_\xi[0]=1$，最终得到

<span id="eq:c71-final-functional"></span>

$$
\begin{aligned}
\mathcal S_\xi[J]
&:=S_0+S_{\rm gh}+S_{\rm gf}
  +\int d^4x\,J^{a\mu}A_\mu^a,\\
Z_\xi[J]
&=\frac{\displaystyle
\int\mathcal DA\,\mathcal D_{\rm pair}(c,\bar c)\,e^{i\mathcal S_\xi[J]}}
{\displaystyle
\int\mathcal DA\,\mathcal D_{\rm pair}(c,\bar c)\,e^{i\mathcal S_\xi[0]}} .
\end{aligned}
\tag{71.30}
$$

对$J$求导可以产生规范场关联函数。
规范不变插入的平均值保持不变，一般固定源则可以依赖规范。普通积分提供了一个直接例子：
$\int dy\,\delta(y-\omega)e^{ijy}=e^{ij\omega}$。
同样，$Z_\xi[J]$生成的非规范不变关联函数可以依赖$\xi$。

现在三个作用量都已是局域的：$S_0$给出规范场的动能和三、四次相互作用，
$S_{\rm gh}$给出鬼传播及鬼—规范场顶角，$S_{\rm gf}$使自由规范场二次核可以求逆。
下一节将把这些项逐一展开为费曼规则。

---

[← 第 70 节](/posts/srednicki-70/) · [章节地图](/srednicki/) · [第 72 节 →](/posts/srednicki-72/)
