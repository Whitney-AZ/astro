---
title: 'Srednicki §53 泛函行列式'
date: 2026-09-14
category: 笔记
tags: [物理, 量子场论, Srednicki]
series: 'Srednicki QFT'
srednickiSections: [53]
hideFromHome: true
draft: false
---

<span id="c53"></span>

我们已经多次利用高斯积分计算自由场的生成泛函。
若二次型不依赖其它场，积分给出的行列式只改变整体归一化，
往往可以在零源比值中消去。现在设二次型里还含有一个指定的背景场：
对量子场的积分仍然是高斯型，所得行列式却随背景而变，必须保留下来。
这个泛函行列式（functional determinant）究竟包含哪些物理过程，
可以通过把它展开成费曼图看清楚。

我们先讨论复标量，再讨论狄拉克场；两个计算的差别将给出闭费米圈的统计负号。[第71节](/posts/srednicki-71/#c71)计算非阿贝尔规范场的路径积分时还会用到这项技术，先在熟悉的高斯理论中把它建立起来。

<span id="c53-scalar-gaussian"></span>

## 在指定背景中积掉复标量

先取一个复标量$\chi$，使它与实的背景函数$\varphi(x)$耦合：

<span id="eq:c53-scalar-model"></span>

$$
\mathcal L_\chi
=-\partial^\mu\chi^\dagger\partial_\mu\chi
 -m^2\chi^\dagger\chi+g\varphi\chi^\dagger\chi .
\tag{53.1}
$$

这里$\varphi(x)$已经指定，路径积分只对$\chi,\chi^\dagger$进行。
因此每个相互作用项对被积变量仍是二次型。
若按通常的标量场赋予$[\varphi]=1$，则这一例子的$g$有质量维数一，
$g\varphi$与$m^2$具有相同的量纲。
稍后狄拉克例子也记耦合为$g$，但那时它是无量纲的另一个耦合。

为了消去与背景无关的归一因子，把泛函定义成比值

<span id="eq:c53-scalar-normalization"></span>

$$
Z_\chi[\varphi]
=\frac{\displaystyle\int\mathcal D\chi^\dagger\mathcal D\chi\,
                e^{iS_\chi[\varphi]}}
       {\displaystyle\int\mathcal D\chi^\dagger\mathcal D\chi\,
                e^{iS_\chi[0]}},
\qquad Z_\chi[0]=1 .
\tag{53.2}
$$

分子和分母使用同一个测度、边界条件及调节。先在有限区域和有限基底中进行矩阵运算，再取连续极限，并用费曼处方选定真空边界条件。

对动能作一次分部积分，
$-\partial^\mu\chi^\dagger\partial_\mu\chi
=-\partial_\mu(\chi^\dagger\partial^\mu\chi)
+\chi^\dagger\partial^2\chi$，于是

<span id="eq:c53-integration-by-parts"></span>

$$
S_\chi[\varphi]
=-\int d^4x\,\chi^\dagger
       (-\partial^2+m^2-g\varphi)\chi
 -\int_{\partial\Omega}d\Sigma_\mu\,
       \chi^\dagger\partial^\mu\chi .
\tag{53.3}
$$

取周期边界或使场在边界充分衰减，最后一项为零，二次型的核便是

<span id="eq:c53-scalar-kernel"></span>

$$
Q_\chi(x,y)
=\bigl[-\partial_x^2+m^2-g\varphi(x)\bigr]\delta^4(x-y),
\qquad
S_\chi=-\int d^4x\,d^4y\,\chi^\dagger(x)Q_\chi(x,y)\chi(y).
\tag{53.4}
$$

自由核提出后的余因子记为$\widetilde Q$。

在有限基底中设$\chi$有$N$个复坐标$z_j$。
沿第44节的测度，$z_j=(x_j+iy_j)/\sqrt2$，
$d^Nz\,d^N\bar z=d^Nx\,d^Ny$。
[普通复高斯积分](/posts/srednicki-44/#c44-complex-gaussian)已给出
$\int e^{-z^\dagger A z}=(2\pi)^N/\det A$，
只要$A$的厄米部分正定。
取$A=iQ_\chi$，便得到本节所需的振荡积分：

<span id="eq:c53-finite-scalar-gaussian"></span>

$$
\int d^Nz\,d^N\bar z\,e^{-i\bar z Q_\chi z}
 =\frac{(2\pi)^N}{\det(iQ_\chi)}
 =\frac{(2\pi)^N i^{-N}}{\det Q_\chi}.
\tag{53.5}
$$

例如对有限厄米核先作$Q_\chi\mapsto Q_\chi-i\delta I$，
$\delta>0$，则指数的实部为$-\delta z^\dagger z$，
积分绝对收敛。最后的真空极限从这类有阻尼的积分接出。
自由核$Q_{\chi,0}$取同一处方，所有与背景无关的因子在比值中相消，留下

<span id="eq:c53-scalar-determinant-ratio"></span>

$$
Z_\chi[\varphi]=\frac{\det Q_{\chi,0}}{\det Q_\chi[\varphi]}.
\tag{53.6}
$$

所以负一次行列式幂直接来自普通复变量的积分。
它的$2\pi$及$i$因子虽然不出现在归一化后的答案里，
相消以前仍由测度和指数中的负号确定。

<span id="c53-factor"></span>

## 用自由传播子分解二次核

把$\Phi$定义为乘法算符，$(\Phi f)(x)=\varphi(x)f(x)$。
自由部分与背景部分的分离为

<span id="eq:c53-operator-factor"></span>

$$
\begin{gathered}
Q_\chi=Q_{\chi,0}-g\Phi,\qquad
Q_{\chi,0}(x,y)=(-\partial_x^2+m^2)\delta^4(x-y),\\
Q_\chi=Q_{\chi,0}(I-G_\chi),\qquad
G_\chi=gQ_{\chi,0}^{-1}\Phi .
\end{gathered}
\tag{53.7}
$$

这一写法先要求自由核可逆。其逆取费曼传播子$\Delta$，
沿本书定义满足
$(-\partial_x^2+m^2)\Delta(x-y)=\delta^4(x-y)$；
若保留有限的真空调节，核与逆也相应同时调节。
因此单位算符和剩余核分别为

<span id="eq:c53-remainder-kernel"></span>

$$
\begin{aligned}
I(x,y)&=\delta^4(x-y),\\
G_\chi(x,y)&=g\Delta(x-y)\varphi(y),\\
\widetilde Q_\chi(x,y)&=\delta^4(x-y)-g\Delta(x-y)\varphi(y).
\end{aligned}
\tag{53.8}
$$

背景必须在第二坐标处，因为先由$\Phi$乘上背景，
再由$Q_{\chi,0}^{-1}$传播。对一般非恒定的$\varphi$，
$\Phi$与微分算符并不对易。把核的乘法展开，可以直接检验这个顺序：

<span id="eq:c53-factor-in-kernels"></span>

$$
\begin{aligned}
&\int d^4y\,Q_{\chi,0}(x,y)\widetilde Q_\chi(y,z)\\
&\quad=Q_{\chi,0}(x,z)
 -g(-\partial_x^2+m^2)\Delta(x-z)\varphi(z)\\
&\quad=Q_{\chi,0}(x,z)-g\delta^4(x-z)\varphi(z)\\
&\quad=\bigl[-\partial_x^2+m^2-g\varphi(x)\bigr]\delta^4(x-z).
\end{aligned}
\tag{53.9}
$$

第二行的导数只作用于$\Delta(x-z)$，最后一步才用
$\varphi(z)\delta^4(x-z)=\varphi(x)\delta^4(x-z)$。
这样就得回式[（53.4）](#eq:c53-scalar-kernel)，背景也保持为局部乘法算符。

在同一个有限基底中，行列式的乘法关系给

<span id="eq:c53-normalized-scalar-det"></span>

$$
\det Q_\chi=\det Q_{\chi,0}\det(I-G_\chi),
\qquad
Z_\chi[\varphi]=\det(I-G_\chi)^{-1}.
\tag{53.10}
$$

所用的$\det(AB)=\det A\det B$是普通矩阵的恒等式：
把$AB$的各列看成$A$作用在$B$的列上，行列式仍是这些列的交替多线性函数，
故等于$\det B$乘上它在单位基底上的值$\det A$。
因此这一步可在撤去调节以前完成。背景为零时$G_\chi=0$，
剩余行列式等于一，归一条件也随之满足。

<span id="c53-trace-log"></span>

## 从矩阵对数到闭合传播链

要看清行列式里包含什么，最方便的是先取对数。
所需关系是$\det A=\exp(\operatorname{Tr}\ln A)$，
可在若尔当基底中证明。对于一个可逆的有限矩阵，
一个若尔当块可写成$J=aI+N$，其中$a\ne0$且$N^r=0$。
选定$a$的对数分支后，

<span id="eq:c53-jordan-log"></span>

$$
\ln J=(\ln a)I+
 \sum_{k=1}^{r-1}\frac{(-1)^{k+1}}{k\,a^k}N^k,
\qquad
\operatorname{Tr}\ln J=r\ln a,\qquad
\det J=a^r .
\tag{53.11}
$$

$N$及其正整数次幂都严格上三角，迹为零，
所以只有对角部分进入$\operatorname{Tr}\ln J$。
对全部若尔当块相加，再用相似变换不改变迹与行列式，便得到
$\exp(\operatorname{Tr}\ln A)=\prod a^r=\det A$。
这个证明也适用于不可对角化的矩阵。

这里实际需要的是$A=I-G_\chi$。在有限维下，
若某个次乘法矩阵范数满足$\|G_\chi\|<1$，
对数可在单位阵附近按收敛级数定义：

<span id="eq:c53-scalar-log-series"></span>

$$
\ln(I-G_\chi)=-\sum_{n=1}^{\infty}\frac{G_\chi^n}{n},
\qquad
\ln Z_\chi[\varphi]
=\sum_{n=1}^{\infty}\frac{\operatorname{Tr}G_\chi^n}{n}.
\tag{53.12}
$$

分支从零背景的$\ln Z_\chi[0]=0$连续选定。
若只求背景的微扰展开，这些等式也可以逐阶作为形式级数使用；
撤去有限基底以前，每个系数仍须按同一规则调节。
任意强背景不必处于上述收敛域，核出现零模时更不能直接沿用这个级数。

系数$1/n$还可以从一个积分清楚地看出。
令背景强度乘上参数$t$，并从$t=0$增加到一。
由$\det(I+hB)=1+h\operatorname{Tr}B+O(h^2)$得到

<span id="eq:c53-resolvent-log"></span>

$$
\begin{aligned}
\frac{d}{dt}\ln\det(I-tG_\chi)
 &=-\operatorname{Tr}\bigl[(I-tG_\chi)^{-1}G_\chi\bigr],\\
\ln\det(I-G_\chi)
 &=-\int_0^1dt\sum_{r=0}^{\infty}
       t^r\operatorname{Tr}G_\chi^{r+1}
 =-\sum_{n=1}^{\infty}\frac{\operatorname{Tr}G_\chi^n}{n}.
\end{aligned}
\tag{53.13}
$$

第一个等式可在相邻两点间分解
$I-(t+h)G_\chi=(I-tG_\chi)
[I-h(I-tG_\chi)^{-1}G_\chi]$后取行列式得到。
在$\|G_\chi\|<1$时，诺伊曼级数在$0\leq t\leq1$上一致收敛，
所以第二行可以逐项积分。由此，矩阵对数的展开及其积分因子都已确定。

接下来恢复连续坐标。算符乘法先对中间坐标积分，
取迹再把首尾坐标相等。例如

<span id="eq:c53-scalar-trace-chain"></span>

$$
\begin{aligned}
\operatorname{Tr}G_\chi
 &=g\int d^4x\,\Delta(0)\varphi(x),\\
\operatorname{Tr}G_\chi^2
 &=g^2\int d^4x\,d^4y\,
       \Delta(x-y)\varphi(y)\Delta(y-x)\varphi(x),\\
\operatorname{Tr}G_\chi^n
 &=g^n\int\prod_{j=1}^n d^4x_j\,
       \prod_{j=1}^n
       \bigl[\Delta(x_j-x_{j+1})\varphi(x_{j+1})\bigr],
\qquad x_{n+1}=x_1 .
\end{aligned}
\tag{53.14}
$$

一般式由$n$次核乘法得到。
每个$\varphi$前后各有一条传播核，最后一条把链闭合。
$G_\chi$作为算符无量纲；它的核有质量维数
$[g]+[\Delta]+[\varphi]=1+2+1=4$，
恰由每次坐标积分的维数抵消。因此迹的每一项都可以进入$\ln Z$。

<span id="c53-cycles"></span>

## 把闭合传播链读成圈图

现在直接从相互作用展开计算同一个泛函。
每个顶点含有一个$\chi$和一个$\chi^\dagger$，而$\varphi$只是指定的函数；
把量子场两两收缩以后，每个顶点恰有一条线进入、一条线离开。
所以连通的真空图只能是有向圈，圈上可以有任意正整数个背景插入。
这类图可以统一画成

<span id="fig:c53-background-ring"></span>

![固定背景中的有向圈，四个显式插入点与右侧省略点表示任意插入数](/images/srednicki/s53_background_ring.svg)

背景中的有向圈。黑点给出$ig\varphi(x_j)$，
箭头从传播核的第二坐标指向第一坐标；
右侧省略了其余插入点。四个显式点代表一般圈的一部分，
不把插入数限定为四。两种量子场的内线分别为$\Delta/i$和$S/i$。

先讨论复标量。沿本书的传播子定义，
$\langle T\chi(x)\chi^\dagger(y)\rangle_0=\Delta(x-y)/i$。
相互作用指数展开至$n$阶给出

<span id="eq:c53-scalar-wick-permutations"></span>

$$
\left.Z_\chi[\varphi]\right|_{g^n}
=\frac{(ig)^n}{n!}\int\prod_{j=1}^n d^4x_j\,\varphi(x_j)
 \sum_{\pi\in\mathfrak S_n}
 \prod_{j=1}^n\frac{\Delta(x_j-x_{\pi(j)})}{i}.
\tag{53.15}
$$

这里排列$\pi$说明第$j$个$\chi$与第$\pi(j)$个$\chi^\dagger$配对。
每个排列都能唯一分解成若干互不相交的循环；一个循环恰好就是一个连通圈。
要得到含全部$n$个顶点的连通图，$\pi$必须是一个$n$循环。
固定从标签1开始读这个循环，剩下$n-1$个标签可以任意排列，
所以这样的收缩共有$(n-1)!$个。
各顶点的坐标都要积分，重新命名这些哑变量便使所有单圈积分相同。
它们与指数展开中的$n!$相除，留下

<span id="eq:c53-scalar-connected-weight"></span>

$$
\begin{aligned}
C_{\chi,n}[\varphi]
&=\frac{(n-1)!}{n!}(ig)^n
  \int\prod_{j=1}^n d^4x_j\,\varphi(x_j)
       \prod_{j=1}^n\frac{\Delta(x_j-x_{j+1})}{i}\\
&=\frac{g^n}{n}\int\prod_{j=1}^n d^4x_j\,
       \prod_{j=1}^n
       [\Delta(x_j-x_{j+1})\varphi(x_{j+1})]
 =\frac1n\operatorname{Tr}G_\chi^n .
\end{aligned}
\tag{53.16}
$$

第一行的$n$个顶角各带一个$i$，$n$条传播线各带一个$1/i$，
二者完全相消。积掉所有坐标时，
$\prod_j\varphi(x_j)=\prod_j\varphi(x_{j+1})$，
于是第二行正好成为式[（53.14）](#eq:c53-scalar-trace-chain)的迹。
从无标签图看，同样的$1/n$来自沿有向圈选择起点的$n$种重复；
即对称因子$S=n$。
有向线已经区分两个方向，反射不再给一个额外的二分之一。
当$n=1$时这是单个插入上的蝌蚪；当$n=2$时两条反向传播线接在两个顶点之间，
权重分别为一和二分之一，均包含在上述计数中。

剩下的图只是若干这种圈的乘积。
设其中含有$r_n$个各具$n$个插入的圈，总顶点数为
$N=\sum_n nr_n$。把$N$个标签分成这些圈，给出
$N!/\prod_n[(n!)^{r_n}r_n!]$种分组；
再对每组计入$(n-1)!$种单循环收缩，最后除以展开中的$N!$，
便得到每个圈的$1/n$及相同圈之间的$1/r_n!$。
因此[第9节的连通图指数关系](/posts/srednicki-09/#c09-connected)在这里具体成为

<span id="eq:c53-disconnected-exponentiation"></span>

$$
Z_\chi[\varphi]
=\prod_{n=1}^{\infty}
  \left(\sum_{r_n=0}^{\infty}
  \frac{C_{\chi,n}[\varphi]^{r_n}}{r_n!}\right)
=\exp\!\left(\sum_{n=1}^{\infty}C_{\chi,n}[\varphi]\right).
\tag{53.17}
$$

定义$Z_\chi=e^{i\Gamma_\chi}$，并使$\Gamma_\chi[0]=0$，于是

<span id="eq:c53-scalar-induced-action"></span>

$$
i\Gamma_\chi[\varphi]
=\sum_{n=1}^{\infty}\frac1n\operatorname{Tr}G_\chi^n
=-\operatorname{Tr}\ln(I-G_\chi).
\tag{53.18}
$$

行列式把所有背景插入数一次包含在内；取它的对数，则恰好留下连通的圈。

<span id="c53-dirac-gaussian"></span>

## 积掉狄拉克场

接着把被积变量换成狄拉克场，仍保持$\varphi(x)$为指定背景。
这里采用普通标量耦合：

<span id="eq:c53-dirac-model"></span>

$$
\begin{aligned}
\mathcal L_\Psi
 &=i\bar\Psi\slashed\partial\Psi-m\bar\Psi\Psi
   +g\varphi\bar\Psi\Psi,\\
S_\Psi
 &=-\int d^4x\,\bar\Psi
       (-i\slashed\partial+m-g\varphi)\Psi .
\end{aligned}
\tag{53.19}
$$

这次$[\Psi]=3/2$，故在$[\varphi]=1$时$g$无量纲。
顶角是$ig\varphi$乘旋量单位阵；前两章赝标量耦合中的$\gamma_5$不出现在这里。
动能已经写成导数作用于$\Psi$的形式，第二行只是从整个二次型提取负号，
无需再把导数移过$\bar\Psi$。

在有限基底中，将时空与旋量标签合成一个指标。
若共有$N$个时空基函数，就有$4N$对独立的格拉斯曼变量。
第44节的[复格拉斯曼高斯积分](/posts/srednicki-44/#c44-determinant)
给出$\int e^{\bar\psi A\psi}=\det A$。
把$A=-iQ_\Psi$代入，并与零背景积分相比，有

<span id="eq:c53-dirac-determinant-ratio"></span>

$$
\begin{aligned}
Z_\Psi[\varphi]
&=\frac{\displaystyle\int\mathcal D\bar\Psi\mathcal D\Psi\,
                       e^{iS_\Psi[\varphi]}}
       {\displaystyle\int\mathcal D\bar\Psi\mathcal D\Psi\,
                       e^{iS_\Psi[0]}}\\
&=\frac{\det(-iQ_\Psi)}{\det(-iQ_{\Psi,0})}
 =\frac{(-i)^{4N}\det Q_\Psi}
        {(-i)^{4N}\det Q_{\Psi,0}}
 =\frac{\det Q_\Psi}{\det Q_{\Psi,0}},
\qquad Z_\Psi[0]=1 .
\end{aligned}
\tag{53.20}
$$

格拉斯曼积分只取有限多项式的最高次系数，因而这里不需要普通高斯积分的收敛条件。
归一比仍要求自由核可逆，并须对两项采用一致的真空边界处方。
与复标量相比，行列式幂的正负已经翻转；后面的统计差别都从这里产生。

为了看清旋量指标，把核与自由逆写为

<span id="eq:c53-dirac-kernels"></span>

$$
\begin{aligned}
(Q_\Psi)_{\alpha\beta}(x,y)
 &=\bigl[(-i\slashed\partial_x+m)_{\alpha\beta}
           -g\varphi(x)\delta_{\alpha\beta}\bigr]\delta^4(x-y),\\
(Q_{\Psi,0})_{\alpha\beta}(x,y)
 &=(-i\slashed\partial_x+m)_{\alpha\beta}\delta^4(x-y),\\
(-i\slashed\partial_x+m)_{\alpha\beta}
 S_{\beta\gamma}(x-y)
 &=\delta_{\alpha\gamma}\delta^4(x-y),\\
(I-G_\Psi)_{\alpha\beta}(x,y)
 &=\delta_{\alpha\beta}\delta^4(x-y)
   -gS_{\alpha\beta}(x-y)\varphi(y).
\end{aligned}
\tag{53.21}
$$

重复旋量指标求和。最后一行中的背景仍在右侧，
所以$G_\Psi=gQ_{\Psi,0}^{-1}\Phi$。
进行一次核乘法时，时空积分与中间旋量求和同时出现：

<span id="eq:c53-dirac-factor-check"></span>

$$
\begin{aligned}
&(Q_{\Psi,0}G_\Psi)_{\alpha\gamma}(x,z)\\
&\quad=\int d^4y\,
 (Q_{\Psi,0})_{\alpha\beta}(x,y)
 gS_{\beta\gamma}(y-z)\varphi(z)\\
&\quad=g(-i\slashed\partial_x+m)_{\alpha\beta}
             S_{\beta\gamma}(x-z)\varphi(z)\\
&\quad=g\delta_{\alpha\gamma}\delta^4(x-z)\varphi(z).
\end{aligned}
\tag{53.22}
$$

这便证明$Q_\Psi=Q_{\Psi,0}(I-G_\Psi)$，并确定了核乘法中的指标次序。消去自由行列式后，

<span id="eq:c53-dirac-trace-log"></span>

$$
\begin{aligned}
Z_\Psi[\varphi]&=\det(I-G_\Psi),\\
i\Gamma_\Psi[\varphi]
 =\ln Z_\Psi[\varphi]
 &=\operatorname{Tr}\ln(I-G_\Psi)
 =-\sum_{n=1}^{\infty}\frac1n\operatorname{Tr}G_\Psi^n .
\end{aligned}
\tag{53.23}
$$

这里沿用复标量部分已经说明的对数分支与微扰解释。
大写的$\operatorname{Tr}$现在还包括旋量指标；将时空迹展开以后，
小写的$\operatorname{tr}$只留给旋量矩阵：

<span id="eq:c53-dirac-trace-chain"></span>

$$
\begin{aligned}
\operatorname{Tr}G_\Psi^n
&=g^n\int\prod_{j=1}^n d^4x_j\,\prod_{j=1}^n\varphi(x_j)\,
 \operatorname{tr}\!\left[
 S(x_1-x_2)S(x_2-x_3)\cdots S(x_n-x_1)\right]\\
&=g^n\int\prod_{j=1}^n d^4x_j\,\prod_{j=1}^n\varphi(x_j)\,
 S_{\alpha_1\alpha_2}(x_1-x_2)
 S_{\alpha_2\alpha_3}(x_2-x_3)\cdots
 S_{\alpha_n\alpha_1}(x_n-x_1).
\end{aligned}
\tag{53.24}
$$

首尾旋量指标相接便产生迹。这些$S$一般不彼此对易，
只能整体循环移动，不能任意交换相邻因子。
因而选取圈的另一个起点不改变答案，逆序读圈却须重新按相应的有向收缩组织矩阵。
$[S(x-y)]=3$，所以这次核的维数为$0+3+1=4$，
再次与坐标积分相抵。

<span id="c53-fermion-sign"></span>

## 费米子闭圈的负号

狄拉克图也只有双线性插入，所以循环起点的计数仍给$1/n$。
如果先只把顶角、传播子和这个循环因子相乘，就会得到

<span id="eq:c53-dirac-before-statistics"></span>

$$
\frac{(ig)^n}{n\,i^n}
\int\prod_{j=1}^n d^4x_j\,\prod_{j=1}^n\varphi(x_j)\,
\operatorname{tr}\!\left[
S(x_1-x_2)\cdots S(x_n-x_1)\right]
=+\frac1n\operatorname{Tr}G_\Psi^n .
\tag{53.25}
$$

它与式[（53.23）](#eq:c53-dirac-trace-log)比较，还差一个整体负号。
行列式已经计入了格拉斯曼积分的统计效应，而刚才的图因子尚未计入。
下面用场的反交换次序把这个负号直接算出来。

记第$j$个顶点中的两个奇变量为
$B_j=\bar\Psi_{a_j}(x_j)$、$A_j=\Psi_{b_j}(x_j)$，并记
$K_{jk}=\langle T A_jB_k\rangle_0
=S_{b_j a_k}(x_j-x_k)/i$。
作用量里的次序为$B_jA_j$。为了应用已经建立的
[费米Wick配对](/posts/srednicki-42/#c42-wick)，先把所有$A$移到所有$B$的前面。
$A_1$须跨过一个$B$，$A_2$须跨过两个，依此类推，故

<span id="eq:c53-bilinear-reordering"></span>

$$
B_1A_1B_2A_2\cdots B_nA_n
=(-1)^{n(n+1)/2}A_1A_2\cdots A_nB_1B_2\cdots B_n .
\tag{53.26}
$$

对右侧先考虑$A_j$与$B_j$配对的一项。
将$B_1$移到$A_1$旁边，须跨过$n-1$个$A$；去掉这一对后，
$B_2$须跨过$n-2$个，直至最后一对无需移动。
因此这项收缩带$(-1)^{n(n-1)/2}$。
若改成$A_j$与$B_{\pi(j)}$配对，重排$B$序列还要乘上
$\operatorname{sgn}\pi$。将所有配对相加，再合并前一步的符号，得到

<span id="eq:c53-fermion-wick-permutations"></span>

$$
\begin{aligned}
\langle T A_1\cdots A_nB_1\cdots B_n\rangle_0
 &=(-1)^{n(n-1)/2}
   \sum_{\pi\in\mathfrak S_n}\operatorname{sgn}\pi
       \prod_{j=1}^n K_{j,\pi(j)},\\
\langle T\prod_{j=1}^n B_jA_j\rangle_0
 &=(-1)^n
   \sum_{\pi\in\mathfrak S_n}\operatorname{sgn}\pi
       \prod_{j=1}^n K_{j,\pi(j)} .
\end{aligned}
\tag{53.27}
$$

两次移动的指数之和为$n^2$，与$n$具有相同奇偶性，
这说明第二行前面的$(-1)^n$从何而来。
现在把排列拆成$c(\pi)$个循环，长度分别为$n_1,\ldots,n_{c(\pi)}$。
长度$n_a$的循环由$n_a-1$次对换组成，故

<span id="eq:c53-one-minus-per-cycle"></span>

$$
\operatorname{sgn}\pi
=\prod_{a=1}^{c(\pi)}(-1)^{n_a-1}
=(-1)^{n-c(\pi)},\qquad
(-1)^n\operatorname{sgn}\pi=(-1)^{c(\pi)} .
\tag{53.28}
$$

每个循环就是一个闭圈，所以每个闭费米圈贡献一个负号，
而与圈上有多少个顶点无关。
对于一个连通圈，将这个号与式[（53.25）](#eq:c53-dirac-before-statistics)相乘，
便有

<span id="eq:c53-dirac-connected-weight"></span>

$$
\begin{aligned}
C_{\Psi,n}[\varphi]&=-\frac1n\operatorname{Tr}G_\Psi^n,\\
i\Gamma_\Psi[\varphi]
&=-g\operatorname{Tr}(S\Phi)
  -\frac{g^2}{2}\operatorname{Tr}(S\Phi S\Phi)+O(g^3).
\end{aligned}
\tag{53.29}
$$

最低两阶也可直接读出这个结果。
一个顶点给$\langle T B_1A_1\rangle_0=-K_{11}$。
两个顶点给$K_{11}K_{22}-K_{12}K_{21}$：
第一项是两个独立蝌蚪，属于指数展开中的乘积；
第二项才是连通圈，负号和二阶展开的$1/2!$共同给出上式的二次项。
这样，格拉斯曼配对、行列式正幂与图的闭圈规则得到了同一个答案。
本节未对相互作用作正规序；普通标量耦合允许蝌蚪及其它奇数插入项，
因此不能在圈和中自行删去奇数$n$。

<span id="c53-action"></span>

## 背景的量子作用量与紫外项

最后说明$\Gamma[\varphi]$为什么可以称为背景的量子作用量。
假设$\varphi$也有自己的作用量$S_\varphi$，以后还要对它积分。
先完成对$\chi$的积分，或先完成对$\Psi$的积分，会把原来的被积式改写为

<span id="eq:c53-induced-action-in-path-integral"></span>

$$
\int\mathcal D\varphi\,e^{iS_\varphi[\varphi]}Z[\varphi]
=\int\mathcal D\varphi\,
 e^{i\{S_\varphi[\varphi]+\Gamma[\varphi]\}} .
\tag{53.30}
$$

所以$\Gamma$直接增加到$\varphi$的作用量中。
只要被积场在固定背景下仍是二次型，这次高斯积分便精确完成了对该场的积分。
它含有任意多个背景插入，但每个连通图都只有一个被积场的圈；
$\varphi$自身的量子涨落则由余下的路径积分产生。
这与第21节通过勒让德变换定义完整有效作用量的步骤有所区别：
此处只完成了对其中一种场的积分。

还须处理圈的紫外发散。归一条件$Z[0]=1$消去了无背景的自由真空因子，
但有背景插入的圈一般仍然发散。
以固定外动量考察大的欧几里得圈动量$\ell$，
标量传播子按$\ell^{-2}$衰减，狄拉克传播子的上界按$\ell^{-1}$衰减，
所以$n$个插入的表面发散度为

<span id="eq:c53-background-power-counting"></span>

$$
\omega_{\chi,n}=4-2n,\qquad
\omega_{\Psi,n}=4-n .
\tag{53.31}
$$

复标量的一次插入可产生线性背景项，二次插入可产生背景平方项。
狄拉克圈还可产生三次、四次背景项，二点圈对外动量的二次展开则产生动能项。
旋量迹会降低某些项的实际发散度：例如单插入中的
$\operatorname{tr}\slashed\ell=0$，留下的是
$4m/(\ell^2+m^2)$；三插入中最高的三次动量分子也因奇数gamma迹为零而消失。
因此质量非零时，允许的局部背景反项仍包括
$\varphi,\varphi^2,(\partial\varphi)^2,\varphi^3,\varphi^4$，
各自的系数须按所选调节和减除条件确定。
这些背景相关的紫外项由相应的局部反项减除，余下部分进入重整化后的背景作用量。

<span id="c53-half-weights"></span>

## 补充：实场与马约拉纳场的二分之一

两个例子都使用复变量。与第44节的实变量积分比较，还能看清
实标量和马约拉纳场的圈权重为什么各带一个二分之一。
这项比较不需要重新枚举所有图，只须保持二次作用量的归一化。

将复标量写成$\chi=(\chi_1+i\chi_2)/\sqrt2$，
实背景与实耦合使作用量分成两个相同的实二次型。
每个实场的背景相互作用为$g\varphi\chi_a^2/2$，
故两个相同实场泛函的乘积等于原来的复场泛函。
结合[实高斯积分](/posts/srednicki-44/#c44-real-gaussian)，在零背景附近选择相同的连续分支，

<span id="eq:c53-real-half-weight"></span>

$$
Z_{\rm real}[\varphi]
=\det(I-G_\chi)^{-1/2},\qquad
i\Gamma_{\rm real}
=\frac12\sum_{n=1}^{\infty}\frac1n\operatorname{Tr}G_\chi^n .
\tag{53.32}
$$

拉氏量中的二分之一会被顶角上两个相同场的收缩数抵消，
所以单个顶角仍为$ig\varphi$。
圈的总半因子反映的正是独立实自由度减半。

对于马约拉纳场，沿前文约定$\bar\Psi=\Psi^T\mathcal C$，
作用量写成$-\frac12\Psi^T\mathcal C Q_\Psi\Psi$。
这里的转置同时作用于旋量与时空基底；
在共同边界条件下$(\partial_\mu)^T=-\partial_\mu$。
利用$\gamma^{\mu T}\mathcal C=-\mathcal C\gamma^\mu$，
而标量背景的转置不变，便得到

<span id="eq:c53-majorana-antisymmetric-kernel"></span>

$$
\begin{aligned}
Q_\Psi^T\mathcal C
&=\bigl(i\gamma^{\mu T}\partial_\mu+m-g\varphi\bigr)\mathcal C
 =\mathcal C(-i\gamma^\mu\partial_\mu+m-g\varphi)
 =\mathcal C Q_\Psi,\\
(\mathcal C Q_\Psi)^T&=-\mathcal C Q_\Psi .
\end{aligned}
\tag{53.33}
$$

因此指数中的矩阵$-i\mathcal C Q_\Psi$反对称，
其格拉斯曼积分由[Pfaffian](/posts/srednicki-44/#c44-pfaffian)给出。
对同一测度取零背景比值，再利用$\operatorname{Pf}(A)^2=\det A$，
可得

<span id="eq:c53-majorana-half-weight"></span>

$$
\begin{aligned}
Z_{\mathrm{Maj}}[\varphi]
 &=\frac{\operatorname{Pf}(-i\mathcal C Q_\Psi)}
         {\operatorname{Pf}(-i\mathcal C Q_{\Psi,0})},\\
Z_{\mathrm{Maj}}[\varphi]^2
 &=\frac{\det Q_\Psi}{\det Q_{\Psi,0}}
   =\det(I-G_\Psi),\\
i\Gamma_{\mathrm{Maj}}
 &=\frac12\operatorname{Tr}\ln(I-G_\Psi)
   =-\frac12\sum_{n=1}^{\infty}\frac1n\operatorname{Tr}G_\Psi^n .
\end{aligned}
\tag{53.34}
$$

最后一行的分支从$Z[0]=1$连续固定，前提是过程中没有核的零模。
它保留每圈的费米统计负号，同时把狄拉克的自由度减半。
因而在相同核与顶角归一化下，四种圈在$i\Gamma$中的权重为

| 被积场     | $n$次背景插入的系数               |
| ---------- | --------------------------------- |
| 复标量     | $+\operatorname{Tr}G_\chi^n/n$    |
| 实标量     | $+\operatorname{Tr}G_\chi^n/(2n)$ |
| 狄拉克场   | $-\operatorname{Tr}G_\Psi^n/n$    |
| 马约拉纳场 | $-\operatorname{Tr}G_\Psi^n/(2n)$ |

普通积分与格拉斯曼积分决定统计号，实自由度与复自由度的数目决定半因子。
这两个区别在高斯积分中已经出现，展开成圈图以后仍须同时保留。

---

[← 第 52 节](/posts/srednicki-52/) · [章节地图](/srednicki/) · [第 54 节 →](/posts/srednicki-54/)
