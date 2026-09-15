---
title: 'Srednicki §36 旋量场的拉格朗日量'
date: 2026-09-14
category: 笔记
tags: [物理, 量子场论, Srednicki]
series: 'Srednicki QFT'
srednickiSections: [36]
hideFromHome: true
draft: false
---

<span id="c36"></span>

上一节给出了把旋量组合成洛伦兹标量的方法，现在可以用这些组合建立场的动力学。先从一个左手外尔场出发，寻找作用量为实数、关于场为二次式的拉格朗日量。二次作用量产生线性运动方程，其平面波解描述自由粒子，也为建立相互作用理论提供出发点。随后引入第二个左手场，比较两种场组合的自由度与内部对称性，就能看清马约拉纳场和狄拉克场之间的关系。

计算使用第35节的奇场代数和旋量指标约定，以及[第22节](/posts/srednicki-22/#c22)的变分与诺特方法。在四维时空中，$\psi,\chi,\xi$及其共轭均取为格拉斯曼奇量；普通时空导数$\partial_\mu$是偶导数，仍服从通常的乘积法则。

<span id="c36-one-weyl"></span>

## 一个左手场的作用量

先看不含导数的项。单个左手场能给出的二次标量是$\psi\psi$及其厄米共轭。上一节已求得$\psi\psi=-2\psi_1\psi_2$，所以这个奇场缩并一般不为零，可以用作质量项。直接相乘的$\psi^\dagger\psi$则还留有一对点、无点指标，两者不能直接缩并成洛伦兹标量。质量项的形式由此确定。

选择动能时，还要考虑量子化后的态空间。二阶候选$\partial^\mu\psi\partial_\mu\psi+\mathrm{h.c.}$是非退化的：场及其共轭是独立配置坐标，按正则规则，它们的等时反对易子为零。在正定态空间中，这会使任意空间涂抹$A=\int d^3x\,f^a(\mathbf x)\psi_a(t,\mathbf x)$满足

$$
0=\langle v|\{A,A^\dagger\}|v\rangle
=\|Av\|^2+\|A^\dagger v\|^2.
$$

于是$A$和$A^\dagger$在共同定义域上都只能为零，与非平凡的正则场代数矛盾。[本节末的模式计算](#c36-second-order)会把这个矛盾具体写成两支振子反对易关系的相反号。

因此转向一阶导数项。$\psi^\dagger\bar\sigma^\mu\partial_\mu\psi$的旋量和时空指标都恰好缩并，已经具有洛伦兹标量的形式。再给它乘$i$，考察厄米共轭，得到

<span id="eq:c36-kinetic-adjoint"></span>

$$
\begin{aligned}
\bigl(i\psi^\dagger_{\dot a}\bar\sigma^{\mu\dot a c}
       \partial_\mu\psi_c\bigr)^\dagger
&=-i(\partial_\mu\psi^\dagger_{\dot c})
       (\bar\sigma^{\mu\dot a c})^*\psi_a\\
&=-i(\partial_\mu\psi^\dagger_{\dot c})
       \bar\sigma^{\mu\dot c a}\psi_a\\
&=i\psi^\dagger\bar\sigma^\mu\partial_\mu\psi
 -i\partial_\mu(\psi^\dagger\bar\sigma^\mu\psi).
\end{aligned}
\tag{36.1}
$$

第一步倒转因子次序并共轭$i$，第二步利用$\bar\sigma^\mu$的厄米性，最后一步展开乘积的微分。全过程没有额外交换两个奇场。结果与原来的动能只相差一个全散度；只要场在边界充分衰减，或采用使该边界积分消失的相容条件，这一差别在作用量中就为零。若希望拉格朗日密度本身也逐点厄米，可以取原项与其共轭的平均：

<span id="eq:c36-hermitian-density"></span>

$$
\mathcal L_{\rm kin,H}
=\frac i2\bigl[\psi^\dagger\bar\sigma^\mu\partial_\mu\psi
-(\partial_\mu\psi^\dagger)\bar\sigma^\mu\psi\bigr]
=i\psi^\dagger\bar\sigma^\mu\partial_\mu\psi
-\frac i2\partial_\mu(\psi^\dagger\bar\sigma^\mu\psi).
\tag{36.2}
$$

这两种密度给出相同的体内运动方程，下面采用较简洁的前一种写法。将动能系数归一为1，再加上互为共轭的两个质量项，便得到自由拉格朗日量：

<span id="eq:c36-weyl-lagrangian"></span>

$$
\mathcal L_W=i\psi^\dagger\bar\sigma^\mu\partial_\mu\psi
-\frac12m\psi\psi-\frac12m^*\psi^\dagger\psi^\dagger.
\tag{36.3}
$$

动能的正号与后续的正定量子化相配，两个质量系数互为共轭，保证质量部分厄米。质量项前的$1/2$则是为变分作准备：两个相同场各变分一次，会产生两份相同贡献。场和参数的量纲也由动能确定，$[\mathcal L]=4$与$[\partial_\mu]=1$给出$[\psi]=3/2$，进而有$[m]=1$。

这个单场自由理论中的质量相位可以消去。写成$m=|m|e^{i\alpha}$后，作恒定场重定义$\psi=e^{-i\alpha/2}\widetilde\psi$，动能中的两个相位彼此相消，质量项则成为$m\psi\psi=|m|\widetilde\psi\widetilde\psi$，其共轭也获得同样的实系数。因此可选$m\geq0$；以下先讨论$m>0$，再以$m=0$得到无质量情形。

<span id="c36-variation"></span>

## 奇场的变分及两条共轭方程

接下来求运动方程。奇场的变分在移过另一个奇场时会变号，因此求导之前必须固定变分因子的位置。这里把它统一移到各项最左端，定义左泛函导数：

<span id="eq:c36-left-variation"></span>

$$
\delta S=\int d^4x\left[
\delta\psi_a\frac{\delta_L S}{\delta\psi_a}
+\delta\psi^\dagger_{\dot a}
 \frac{\delta_L S}{\delta\psi^\dagger_{\dot a}}\right].
\tag{36.4}
$$

场的变分本身也是奇量，每经过一个奇场就产生一个负号。计算时先把$\psi_a$和$\psi^\dagger_{\dot a}$当作独立变量，所得两条方程最后互为共轭。先处理质量项：无点与点指标的缩并次序相反，所以把变分都移到左侧以后，两种质量乘积的结果带有不同的号：

<span id="eq:c36-mass-variation"></span>

$$
\begin{aligned}
\delta(\psi\psi)
&=\epsilon^{ab}\delta\psi_b\psi_a
 +\epsilon^{ab}\psi_b\delta\psi_a
=-2\delta\psi_a\psi^a,\\
\delta(\psi^\dagger\psi^\dagger)
&=\delta\psi^\dagger_{\dot a}\psi^{\dagger\dot a}
 +\psi^\dagger_{\dot a}\epsilon^{\dot a\dot b}
                  \delta\psi^\dagger_{\dot b}
=2\delta\psi^\dagger_{\dot a}\psi^{\dagger\dot a}.
\end{aligned}
\tag{36.5}
$$

也可以从分量看清这一差别：$\psi\psi=-2\psi_1\psi_2$，而$\psi^\dagger\psi^\dagger=2\psi^\dagger_{\dot1}\psi^\dagger_{\dot2}$，分别对两个因子变分并移到左端，就得到上面的结果。再看动能，对$\psi^\dagger$变分时，变分因子已经在所需位置；对$\psi$变分时，则要先用分部积分移去变分上的导数，再把变分移到左端：

<span id="eq:c36-kinetic-variation"></span>

$$
\begin{aligned}
\int d^4x\,i\psi^\dagger_{\dot a}\bar\sigma^{\mu\dot a c}
       \partial_\mu\delta\psi_c
&=-\int d^4x\,i(\partial_\mu\psi^\dagger_{\dot a})
       \bar\sigma^{\mu\dot a c}\delta\psi_c\\
&=\int d^4x\,i\delta\psi_c\bar\sigma^{\mu\dot a c}
       \partial_\mu\psi^\dagger_{\dot a}.
\end{aligned}
\tag{36.6}
$$

这里采用紧支撑变分，使边界项消失。两步各产生一个负号，分别来自分部积分与奇量交换。将[（36.5）](#eq:c36-mass-variation)和[（36.6）](#eq:c36-kinetic-variation)中相应变分的系数合在一起，令它们为零，便得到

<span id="eq:c36-weyl-euler"></span>

$$
\begin{aligned}
0&=i\bar\sigma^{\mu\dot a c}\partial_\mu\psi_c
    -m\psi^{\dagger\dot a},\\
0&=i\bar\sigma^{\mu\dot c a}\partial_\mu\psi^\dagger_{\dot c}
    +m\psi^a.
\end{aligned}
\tag{36.7}
$$

两条方程互为厄米共轭。为了把它们放在同一种块矩阵记号中，将第一式整体乘$-1$，再降低第二式的自由无点指标。其导数项所需的两次缩并为

<span id="eq:c36-conjugate-lowering"></span>

$$
\epsilon_{ba}\bar\sigma^{\mu\dot c a}
=\epsilon^{\dot c\dot d}\sigma^\mu_{b\dot d},
\qquad
\epsilon^{\dot c\dot d}\psi^\dagger_{\dot c}
=-\psi^{\dagger\dot d}.
\tag{36.8}
$$

第二次缩并使用了$\epsilon$的第一个指标，因而多出负号。将它代回共轭方程，得到

<span id="eq:c36-conjugate-equation"></span>

$$
-i\sigma^\mu_{a\dot c}\partial_\mu\psi^{\dagger\dot c}
+m\psi_a=0.
\tag{36.9}
$$

现在两条方程的导数项都带$-i$，质量项保持原来的场分量。它们共同描述一个外尔场，适合合并为一个四分量方程。

<span id="c36-four-components"></span>

## 四分量记号与马约拉纳场

把场和它的共轭分别放在一个列的上下两块，再把两种$\sigma$矩阵放在相应的非对角块中，就能同时表示这两条方程。定义

<span id="eq:c36-gamma-majorana"></span>

$$
\Psi_M=\begin{pmatrix}\psi_a\\ \psi^{\dagger\dot a}\end{pmatrix},
\qquad
\gamma^\mu=\begin{pmatrix}0&\sigma^\mu_{a\dot c}\\
                       \bar\sigma^{\mu\dot a c}&0\end{pmatrix}.
\tag{36.10}
$$

块矩阵第一行给出降低无点指标后的共轭方程，第二行给出原来的点指标方程，因而有

<span id="eq:c36-majorana-dirac-equation"></span>

$$
\begin{gathered}
\begin{pmatrix}
m\delta_a{}^c&-i\sigma^\mu_{a\dot c}\partial_\mu\\
-i\bar\sigma^{\mu\dot a c}\partial_\mu&m\delta^{\dot a}{}_{\dot c}
\end{pmatrix}
\begin{pmatrix}\psi_c\\\psi^{\dagger\dot c}\end{pmatrix}=0,\\
(-i\gamma^\mu\partial_\mu+m)\Psi_M=0.
\end{gathered}
\tag{36.11}
$$

这个四分量对象称为马约拉纳场（Majorana field），它满足的方程称为狄拉克方程。这里上下两块来自同一个外尔场，独立变量的数目仍与两分量描述相同。

新引入的矩阵继承了$\sigma$的代数。按块相乘，$\gamma^\mu\gamma^\nu$的两个对角块分别是$\sigma^\mu\bar\sigma^\nu$和$\bar\sigma^\mu\sigma^\nu$。第35节[（35.22）](/posts/srednicki-35/#eq:c35-sigma-clifford-pairs)已通过两个时间指标、一时一空和两个空间指标的计算求出它们的对称部分；放入这两个块，得到

<span id="eq:c36-clifford"></span>

$$
\{\gamma^\mu,\gamma^\nu\}=-2g^{\mu\nu}I_4,
\qquad
(\gamma^0)^2=I_4,\quad(\gamma^i)^2=-I_4.
\tag{36.12}
$$

这是所用的克利福德代数。它使一阶场方程导出相对论性的二阶方程：在左侧再作用一个导数项反号、质量项同号的算符，得到

<span id="eq:c36-mass-shell"></span>

$$
(i\gamma^\mu\partial_\mu+m)
(-i\gamma^\nu\partial_\nu+m)\Psi_M
=(-\partial^2+m^2)\Psi_M=0.
\tag{36.13}
$$

展开后，两个一阶交叉项相消；二阶导数对称，恰好只保留$\gamma$矩阵乘积的对称部分。因此平面波$e^{ikx}$必须满足$k^2=-m^2$，即$E_{\mathbf k}^2=\mathbf k^2+m^2$，质量参数也就有了熟悉的运动学含义。

若改为左乘$\gamma^0$，方程还可写成$i\partial_t\Psi_M=(-i\boldsymbol\alpha\cdot\nabla+m\beta)\Psi_M$，其中$\alpha^k=\gamma^0\gamma^k$、$\beta=\gamma^0$作为数值矩阵。这与第1节对相对论性能量关系所作的线性化相同；此处的$\Psi_M$是场，随后将对它的平面波系数按费米统计进行量子化。

<span id="c36-two-weyl"></span>

## 两个外尔场怎样组成狄拉克场

一个外尔场与其共轭构成了马约拉纳场。若从两个等质量左手场$\psi_i$、$i=1,2$出发，拉格朗日量就是两份[（36.3）](#eq:c36-weyl-lagrangian)之和。实正交矩阵$O$满足$O^TO=I$，所以动能中的$\delta_{ij}$和质量中的$\delta_{ij}$都在这种场混合下保持不变。取内部转动，并同时定义下面两个复线性组合：

<span id="eq:c36-internal-change"></span>

$$
\begin{pmatrix}\psi_1\\\psi_2\end{pmatrix}
\longmapsto
\begin{pmatrix}\cos\alpha&\sin\alpha\\-\sin\alpha&\cos\alpha\end{pmatrix}
\begin{pmatrix}\psi_1\\\psi_2\end{pmatrix},
\qquad
\chi=\frac{\psi_1+i\psi_2}{\sqrt2},\quad
\xi=\frac{\psi_1-i\psi_2}{\sqrt2}.
\tag{36.14}
$$

这一换基把内部转动化成相位变换。其中$\chi,\xi$仍是两个独立的左手场；原来的$\psi_1,\psi_2$本来就是旋量场，未加实标量那样的实条件，因此$\xi$并不等于$\chi^\dagger$。利用逆变换$\psi_1=(\chi+\xi)/\sqrt2$、$\psi_2=-i(\chi-\xi)/\sqrt2$，可以逐项看清新拉格朗日量的系数。先代入动能，两份展开的交叉项带相反号，因而相消：

<span id="eq:c36-kinetic-basis"></span>

$$
\begin{aligned}
\sum_i\psi_i^\dagger\bar\sigma^\mu\partial_\mu\psi_i
={}&\frac12(\chi^\dagger+\xi^\dagger)
              \bar\sigma^\mu\partial_\mu(\chi+\xi)\\
&+\frac12(\chi^\dagger-\xi^\dagger)
              \bar\sigma^\mu\partial_\mu(\chi-\xi)\\
={}&\chi^\dagger\bar\sigma^\mu\partial_\mu\chi
 +\xi^\dagger\bar\sigma^\mu\partial_\mu\xi .
\end{aligned}
\tag{36.15}
$$

质量项的展开需要用到奇旋量缩并的对称性$\chi\xi=\xi\chi$。原来两个场的自缩并在新基底中合成一个交叉质量项：

<span id="eq:c36-mass-basis"></span>

$$
\begin{aligned}
\psi_1\psi_1+\psi_2\psi_2
&=\frac12\bigl[(\chi+\xi)(\chi+\xi)-(\chi-\xi)(\chi-\xi)\bigr]\\
&=\chi\xi+\xi\chi=2\chi\xi.
\end{aligned}
\tag{36.16}
$$

取厄米共轭后得到$2\xi^\dagger\chi^\dagger$，与动能的结果合起来，得到

<span id="eq:c36-dirac-two-weyl"></span>

$$
\mathcal L_D=i\chi^\dagger\bar\sigma^\mu\partial_\mu\chi
+i\xi^\dagger\bar\sigma^\mu\partial_\mu\xi
-m\chi\xi-m\xi^\dagger\chi^\dagger.
\tag{36.17}
$$

原质量项的两个$1/2$都已抵消，两个动能则继续保持单位系数。再将内部转动作用于[（36.14）](#eq:c36-internal-change)中的组合，$\chi$所含两个原场的系数分别变为$\cos\alpha-i\sin\alpha$和$\sin\alpha+i\cos\alpha=i e^{-i\alpha}$。这说明新基底中的两个场分别按相反相位变换：

<span id="eq:c36-opposite-phases"></span>

$$
\chi\longmapsto e^{-i\alpha}\chi,\qquad
\xi\longmapsto e^{+i\alpha}\xi.
\tag{36.18}
$$

两个相位在交叉质量项中相消，所以这仍是同一个对称性，只是原来的$SO(2)$如今写成了$U(1)$的形式。运动方程也可沿单场的左变分步骤求出。例如对$\chi^\dagger_{\dot a}$变分，质量项中出现的$-m\xi^\dagger_{\dot b}\epsilon^{\dot b\dot c}
\delta\chi^\dagger_{\dot c}$移到左侧后为
$-m\delta\chi^\dagger_{\dot a}\xi^{\dagger\dot a}$，与动能变分合并后给出$-i\bar\sigma^\mu\partial_\mu\chi+m\xi^\dagger=0$。再对$\xi$变分，并按[（36.8）](#eq:c36-conjugate-lowering)降低自由指标，便得到与它配成一组的方程：

<span id="eq:c36-dirac-block-equations"></span>

$$
\begin{aligned}
-i\bar\sigma^{\mu\dot a c}\partial_\mu\chi_c
 +m\xi^{\dagger\dot a}&=0,\\
-i\sigma^\mu_{a\dot c}\partial_\mu\xi^{\dagger\dot c}
 +m\chi_a&=0.
\end{aligned}
\tag{36.19}
$$

另外两条变分方程与它们互为共轭。这一组方程的块结构与前面完全相同，因此可以定义狄拉克场（Dirac field），并将方程合写为

<span id="eq:c36-dirac-definition"></span>

$$
\Psi_D=\begin{pmatrix}\chi_a\\\xi^{\dagger\dot a}\end{pmatrix},
\qquad
(-i\gamma^\mu\partial_\mu+m)\Psi_D=0.
\tag{36.20}
$$

这里的块核与[（36.11）](#eq:c36-majorana-dirac-equation)相同，区别在于上下两块现在来自两个独立外尔场。为便于比较这两种场，在需要区分时使用下标$D,M$；两者共同满足的关系则用$\Psi$表示。

<span id="c36-dirac-adjoint"></span>

## 狄拉克伴随与四分量拉格朗日量

既然运动方程已经合成四分量形式，拉格朗日量也应能用同一个场写出。先考虑质量项。取厄米共轭得到$\Psi_D^\dagger=(\chi^\dagger_{\dot a},\xi^a)$后，还需把共轭行的两块交换，才能与原场列的指标相配。为此引入

<span id="eq:c36-dirac-adjoint"></span>

$$
\beta=\begin{pmatrix}
0&\delta^{\dot a}{}_{\dot c}\\ \delta_a{}^c&0
\end{pmatrix},
\qquad
\bar\Psi_D\equiv\Psi_D^\dagger\beta
=(\xi^a,\chi^\dagger_{\dot a}).
\tag{36.21}
$$

矩阵$\beta$与$\gamma^0$数值相同，但在这里用于把共轭行的两块变成与$\Psi_D$相配的对偶指标，所以用不同的记号加以区分。所得的$\bar\Psi$称为狄拉克伴随（Dirac adjoint）。将这个行与场列相乘，得到

<span id="eq:c36-dirac-mass"></span>

$$
\bar\Psi_D\Psi_D=\xi^a\chi_a
 +\chi^\dagger_{\dot a}\xi^{\dagger\dot a}
=\chi\xi+\xi^\dagger\chi^\dagger.
\tag{36.22}
$$

最后一步利用第35节标量缩并的对称性，恰好恢复了两分量拉格朗日量中的质量组合。动能的块乘法则先产生两种导数位置：第二项已有所需的外尔形式，第一项的导数还作用在共轭场上，

<span id="eq:c36-dirac-kinetic-blocks"></span>

$$
\bar\Psi_D\gamma^\mu\partial_\mu\Psi_D
=\xi^a\sigma^\mu_{a\dot c}\partial_\mu\xi^{\dagger\dot c}
 +\chi^\dagger_{\dot a}\bar\sigma^{\mu\dot a c}\partial_\mu\chi_c.
\tag{36.23}
$$

因此先对第一项使用乘积法则，把导数移到另一个因子上，再交换两个奇量，使共轭场回到左侧。两步依次给出

<span id="eq:c36-dirac-integration-by-parts"></span>

$$
\begin{aligned}
\xi^a\sigma^\mu_{a\dot c}\partial_\mu\xi^{\dagger\dot c}
&=-(\partial_\mu\xi^a)\sigma^\mu_{a\dot c}\xi^{\dagger\dot c}
  +\partial_\mu(\xi^a\sigma^\mu_{a\dot c}\xi^{\dagger\dot c})\\
&=\xi^{\dagger\dot c}\sigma^\mu_{a\dot c}\partial_\mu\xi^a
  +\partial_\mu(\xi\sigma^\mu\xi^\dagger).
\end{aligned}
\tag{36.24}
$$

乘积法则和奇量交换各产生一个负号，两者相消。剩下的工作是将第一项的指标改成$\bar\sigma$所用的缩并次序；把升降显式写出，便有

<span id="eq:c36-two-index-signs"></span>

$$
\begin{aligned}
\xi^{\dagger\dot c}\sigma^\mu_{a\dot c}\partial_\mu\xi^a
&=\xi^\dagger_{\dot b}
 \epsilon^{\dot c\dot b}\sigma^\mu_{a\dot c}
 \epsilon^{ad}\partial_\mu\xi_d\\
&=\xi^\dagger_{\dot b}\bar\sigma^{\mu\dot b d}\partial_\mu\xi_d.
\end{aligned}
\tag{36.25}
$$

两个$\epsilon$的指标都需倒转次序，各产生一个负号，因此总号仍为正。将这一项和原来的另一个动能相加，就得到两个外尔动能与四分量动能的关系：

<span id="eq:c36-dirac-boundary"></span>

$$
\bar\Psi_D\gamma^\mu\partial_\mu\Psi_D
=\chi^\dagger\bar\sigma^\mu\partial_\mu\chi
+\xi^\dagger\bar\sigma^\mu\partial_\mu\xi
+\partial_\mu(\xi\sigma^\mu\xi^\dagger).
\tag{36.26}
$$

沿用前面使边界积分消失的条件，略去这个全散度后，两分量的动能与质量就合成紧凑形式：

<span id="eq:c36-dirac-lagrangian"></span>

$$
\mathcal L_D=i\bar\Psi_D\gamma^\mu\partial_\mu\Psi_D
-m\bar\Psi_D\Psi_D.
\tag{36.27}
$$

它的厄米性也可从矩阵看出。显式块结构给出$\gamma^0$厄米、$\gamma^i$反厄米，并满足$(\beta\gamma^\mu)^\dagger=\beta\gamma^\mu$。所以质量项逐点厄米，动能取共轭后则仍只改变一个全散度，与两分量作用量的结果相同。

<span id="c36-current"></span>

## 相位对称性与守恒流

在四分量记号中，内部对称性更为直接。由于$\xi^\dagger$和$\chi$具有同一相位，场及其伴随的变换可以写成$\Psi_D\mapsto e^{-i\alpha}\Psi_D$、$\bar\Psi_D\mapsto e^{+i\alpha}\bar\Psi_D$。为求对应的诺特流，沿第22节的方法暂令$\alpha=\alpha(x)$：不含相位导数的变化仍彼此相消，只有动能中的导数作用到$\alpha$时留下

<span id="eq:c36-local-phase"></span>

$$
\delta\mathcal L_D
=i\bar\Psi_D\gamma^\mu(-i\partial_\mu\alpha)\Psi_D
=(\partial_\mu\alpha)\bar\Psi_D\gamma^\mu\Psi_D.
\tag{36.28}
$$

局部参数导数的系数就是诺特流。将它按块展开，便得到四分量与两分量表达：

<span id="eq:c36-dirac-current"></span>

$$
j^\mu=\bar\Psi_D\gamma^\mu\Psi_D
=\chi^\dagger\bar\sigma^\mu\chi
-\xi^\dagger\bar\sigma^\mu\xi.
\tag{36.29}
$$

两个外尔流的相对负号来自场的次序。块乘法先给出$\xi\sigma^\mu\xi^\dagger+\chi^\dagger\bar\sigma^\mu\chi$，其中第一项交换两个奇场后成为$-\xi^{\dagger\dot c}\sigma^\mu_{a\dot c}\xi^a$；再作[（36.25）](#eq:c36-two-index-signs)中的两次升降，就得到上式。若分别对两个动能使用[（36.18）](#eq:c36-opposite-phases)，也会得到$\chi$贡献正号、$\xi$贡献负号，和它们相反的相位一致。

守恒性可以直接从运动方程得到。狄拉克方程及其伴随分别给出

<span id="eq:c36-adjoint-equation"></span>

$$
\gamma^\mu\partial_\mu\Psi_D=-im\Psi_D,\qquad
(\partial_\mu\bar\Psi_D)\gamma^\mu=+im\bar\Psi_D.
\tag{36.30}
$$

第二式也可从[（36.27）](#eq:c36-dirac-lagrangian)对$\Psi_D$变分并分部积分求出。对流求散度，两项分别用这两条方程化简，便有$\partial_\mu j^\mu=im\bar\Psi_D\Psi_D-im\bar\Psi_D\Psi_D=0$。在量子电动力学中，还须乘上粒子的电荷$e$，得到电磁流$e j^\mu$。此处诺特流的归一由所选相位$e^{-i\alpha}$确定，随后进行正则量子化时，它的空间积分将获得电荷算符的粒子解释。

<span id="c36-charge-conjugation"></span>

## 电荷共轭

除连续相位转动外，两分量拉格朗日量[（36.17）](#eq:c36-dirac-two-weyl)还在交换$\chi$与$\xi$时保持不变：两个动能彼此交换，质量项则因标量缩并对称而不变。用原来的$\psi_1,\psi_2$表示，这一交换就是反射$\psi_1\mapsto\psi_1$、$\psi_2\mapsto-\psi_2$，它把$SO(2)$扩充为$O(2)$。由于流[（36.29）](#eq:c36-dirac-current)在该交换下变号，这个变换称为电荷共轭（charge conjugation）。在态空间上，用幺正算符$C$实现这一交换：

<span id="eq:c36-charge-exchange"></span>

$$
C^{-1}\chi_a(x)C=\xi_a(x),\qquad
C^{-1}\xi_a(x)C=\chi_a(x).
\tag{36.31}
$$

这是内部对称性，场的时空宗量保持不变。要在四分量记号中实现同一交换，需要先调整共轭场的旋量指标；为此引入数值矩阵

<span id="eq:c36-charge-matrix"></span>

$$
\mathcal C=
\begin{pmatrix}\epsilon_{ac}&0\\0&\epsilon^{\dot a\dot c}\end{pmatrix}
=\begin{pmatrix}E&0\\0&E^{-1}\end{pmatrix},
\qquad E=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
\tag{36.32}
$$

先把狄拉克伴随的行转成列，再用这个矩阵分别升降两块的指标，便有

<span id="eq:c36-charge-field"></span>

$$
\bar\Psi_D^T=\begin{pmatrix}\xi^a\\\chi^\dagger_{\dot a}\end{pmatrix},
\qquad
\Psi_D^C\equiv\mathcal C\bar\Psi_D^T
=\begin{pmatrix}\xi_a\\\chi^{\dagger\dot a}\end{pmatrix}.
\tag{36.33}
$$

与[（36.20）](#eq:c36-dirac-definition)比较可见，$\chi,\xi$恰好交换了位置，因而四分量变换为$C^{-1}\Psi_D(x)C=\Psi_D^C(x)$。这里数值矩阵$\mathcal C$承担旋量指标的转换，幺正算符$C$则作用在态与场算符上。交换两次会回到原场，所以$(\Psi_D^C)^C=\Psi_D$。

电荷共轭矩阵的若干性质直接来自$\epsilon$。因为$E$实且反对称，并满足$E^2=-I$，它的两个对角块给出

<span id="eq:c36-charge-matrix-properties"></span>

$$
\mathcal C^T=\mathcal C^\dagger=\mathcal C^{-1}=-\mathcal C,
\qquad \mathcal C^2=-I_4.
\tag{36.34}
$$

同一个数值矩阵也可写为$\operatorname{diag}(-\epsilon^{ac},-\epsilon_{\dot a\dot c})$，因为上下$\epsilon$的数值相反。矩阵的平方$\mathcal C^2=-I$与场的两次电荷共轭为$+1$涉及不同的运算：[（36.33）](#eq:c36-charge-field)中除了矩阵乘法，还有伴随与转置。

下面求它与$\gamma$矩阵的关系。先将三个矩阵按块相乘，

<span id="eq:c36-charge-gamma-blocks"></span>

$$
\begin{aligned}
\mathcal C^{-1}\gamma^\mu\mathcal C
&=
\begin{pmatrix}-E&0\\0&E\end{pmatrix}
\begin{pmatrix}0&\sigma^\mu\\\bar\sigma^\mu&0\end{pmatrix}
\begin{pmatrix}E&0\\0&-E\end{pmatrix}\\
&=\begin{pmatrix}0&E\sigma^\mu E\\E\bar\sigma^\mu E&0\end{pmatrix}.
\end{aligned}
\tag{36.35}
$$

两个非对角块都可用第35节的双升指标式$\bar\sigma^\mu=-E(\sigma^\mu)^TE$化简。对这条恒等式转置并使用$E^T=-E$，得到$E\sigma^\mu E=-(\bar\sigma^\mu)^T$；反向操作则给出$E\bar\sigma^\mu E=-(\sigma^\mu)^T$。代回两个块，结果是

<span id="eq:c36-charge-gamma"></span>

$$
\mathcal C^{-1}\gamma^\mu\mathcal C
=-\begin{pmatrix}0&(\bar\sigma^\mu)^T\\
                       (\sigma^\mu)^T&0\end{pmatrix}
=-(\gamma^\mu)^T.
\tag{36.36}
$$

四阶矩阵的转置同时交换两个非对角块，并对每个块内部作转置。两个非对角块前都带负号。按分量看，$\mu=0$时$EIE=-I$；空间分量则满足$E\sigma_iE=\sigma_i^T$，与上述转置形式一致。

<span id="c36-majorana"></span>

## 马约拉纳约束怎样进入变分

有了电荷共轭的明确表达，就可以回到由单个外尔场构成的$\Psi_M$。在[（36.33）](#eq:c36-charge-field)中令$\chi=\xi=\psi$，交换两块中的场不再产生新对象，因而有

<span id="eq:c36-majorana-condition"></span>

$$
\Psi_M^C=\Psi_M,\qquad
\bar\Psi_M^T=\mathcal C^{-1}\Psi_M,\qquad
\bar\Psi_M=\Psi_M^T\mathcal C.
\tag{36.37}
$$

最后一步用到了$(\mathcal C^{-1})^T=\mathcal C$。马约拉纳条件使电荷共轭场由原场本身确定，类似于实标量的$\varphi^\dagger=\varphi$；狄拉克场则类似复标量，具有相应的独立粒子电荷。这个对称性类比用于此处的非零质量理论。单个无质量外尔场仍允许相位转动，在马约拉纳四分量中表现为左右手征分量的相反相位。

接着把作用量也写回单场形式。将$\chi=\xi=\psi$代入[（36.22）](#eq:c36-dirac-mass)和
[（36.26）](#eq:c36-dirac-boundary)，四分量动能给两份
$i\psi^\dagger\bar\sigma^\mu\partial_\mu\psi$，质量部分则给出$\psi\psi+\psi^\dagger\psi^\dagger$。与最初单场拉格朗日量的系数比较，得到

<span id="eq:c36-majorana-lagrangian"></span>

$$
\mathcal L_M=\frac i2\bar\Psi_M\gamma^\mu\partial_\mu\Psi_M
-\frac m2\bar\Psi_M\Psi_M.
\tag{36.38}
$$

它是带有马约拉纳条件的作用量，求变分时须同时实施该条件；若将$\Psi_M$和$\bar\Psi_M$都当作独立狄拉克变量，场的自由度就会改变。利用[（36.37）](#eq:c36-majorana-condition)消去伴随，作用量便成为单个场的二次型：

<span id="eq:c36-majorana-quadratic"></span>

$$
\mathcal L_M=\frac i2\Psi_M^T\mathcal C\gamma^\mu\partial_\mu\Psi_M
-\frac m2\Psi_M^T\mathcal C\Psi_M.
\tag{36.39}
$$

求这个二次型的变分，关键是弄清矩阵的转置性质，这决定了两个场各变分一次所得的项怎样合并。由[（36.36）](#eq:c36-charge-gamma)和$\mathcal C^T=-\mathcal C$，首先得到

<span id="eq:c36-symmetric-cgamma"></span>

$$
(\mathcal C\gamma^\mu)^T
=-(\gamma^\mu)^T\mathcal C
=\mathcal C^{-1}\gamma^\mu\mathcal C^2
=\mathcal C\gamma^\mu.
\tag{36.40}
$$

因此，记$A^\mu=\mathcal C\gamma^\mu$时，动能中的矩阵对称，质量项中的$\mathcal C$反对称。让每一项中的两个场分别变分，作用量一共产生四项：

<span id="eq:c36-majorana-four-terms"></span>

$$
\begin{aligned}
\delta S_M=\frac12\int d^4x\bigl[
&i\delta\Psi_M^T A^\mu\partial_\mu\Psi_M
 +i\Psi_M^T A^\mu\partial_\mu\delta\Psi_M\\
&-m\delta\Psi_M^T\mathcal C\Psi_M
 -m\Psi_M^T\mathcal C\delta\Psi_M\bigr].
\end{aligned}
\tag{36.41}
$$

第一项和第三项的变分已经在左端。第二项先分部积分，再将奇变分移到左边；沿用前面的紧支撑变分，边界项消失，得到

<span id="eq:c36-majorana-kinetic-variation"></span>

$$
\begin{aligned}
\int d^4x\,i\Psi_M^T A^\mu\partial_\mu\delta\Psi_M
&=-\int d^4x\,i(\partial_\mu\Psi_M)^TA^\mu\delta\Psi_M\\
&=\int d^4x\,i\delta\Psi_M^T(A^\mu)^T\partial_\mu\Psi_M.
\end{aligned}
\tag{36.42}
$$

交换两个奇量后，再交换求和指标的名称，就出现了矩阵转置。由于$A^\mu$对称，这一项与第一项相同。第四项也将奇变分移到左侧，但这次使用的是质量矩阵的反对称性：

<span id="eq:c36-majorana-mass-variation"></span>

$$
-m\Psi_M^T\mathcal C\delta\Psi_M
=+m\delta\Psi_M^T\mathcal C^T\Psi_M
=-m\delta\Psi_M^T\mathcal C\Psi_M,
\tag{36.43}
$$

它恰好等于第三项。这样，动能和质量各产生两份相同贡献，分别抵消作用量中的$1/2$，最终有

<span id="eq:c36-majorana-euler"></span>

$$
\delta S_M=\int d^4x\,
\delta\Psi_M^T\mathcal C(i\gamma^\mu\partial_\mu-m)\Psi_M,
\qquad
(-i\gamma^\mu\partial_\mu+m)\Psi_M=0.
\tag{36.44}
$$

利用$\mathcal C$可逆，就从变分系数为零得到最后的狄拉克方程。计算可先对复化分量进行，随后限制到马约拉纳实条件；其独立内容仍是原来$\psi,\psi^\dagger$的两条共轭方程。

同一组矩阵性质还说明马约拉纳场的矢量双线性为何消失。具体地，$\bar\Psi_M\gamma^\mu\Psi_M=\Psi_M^TA^\mu\Psi_M=0$，因为交换两个奇场会把它变成$-\Psi_M^T(A^\mu)^T\Psi_M$，而矩阵对称使它等于自身的负值。这也可从[（36.29）](#eq:c36-dirac-current)中令$\chi=\xi$后两项相消看出。质量项则可以非零，因为其中的$\mathcal C$是反对称矩阵。

<span id="c36-chirality"></span>

## 手征投影

四分量形式便于把方程和作用量写得紧凑；需要单独使用左右手场时，再把上下两块投影出来即可。定义

<span id="eq:c36-chiral-projectors"></span>

$$
\begin{gathered}
\gamma_5=\begin{pmatrix}-I_2&0\\0&I_2\end{pmatrix},\\
P_L=\frac12(I_4-\gamma_5)=\begin{pmatrix}I_2&0\\0&0\end{pmatrix},
\qquad
P_R=\frac12(I_4+\gamma_5)=\begin{pmatrix}0&0\\0&I_2\end{pmatrix}.
\end{gathered}
\tag{36.45}
$$

下标5是这个矩阵名称的一部分，并不是新增的时空指标。由$\gamma_5^2=I_4$可得$P_L^2=P_L$、$P_R^2=P_R$、$P_LP_R=0$、$P_L+P_R=I_4$，所以它们确实把整个四分量空间分成互补的两部分。按块相乘，两种投影分别为

<span id="eq:c36-project-weyl"></span>

$$
P_L\Psi_D=\begin{pmatrix}\chi_a\\0\end{pmatrix},
\qquad
P_R\Psi_D=\begin{pmatrix}0\\\xi^{\dagger\dot a}\end{pmatrix}.
\tag{36.46}
$$

马约拉纳场只需相应取$\chi=\xi=\psi$。除了显式块定义，还可以把$\gamma_5$表示成四个$\gamma$矩阵的乘积。要得到这个表达式，先将矩阵两两相乘：

<span id="eq:c36-gamma-five-pairs"></span>

$$
\gamma^0\gamma^1=
\begin{pmatrix}-\sigma_1&0\\0&\sigma_1\end{pmatrix},\qquad
\gamma^2\gamma^3=
\begin{pmatrix}-\sigma_2\sigma_3&0\\0&-\sigma_2\sigma_3\end{pmatrix}.
\tag{36.47}
$$

再利用$\sigma_1\sigma_2\sigma_3=iI_2$，就有$\gamma^0\gamma^1\gamma^2\gamma^3=\operatorname{diag}(iI_2,-iI_2)$，乘$i$便还原$\gamma_5$的块定义。也可将四个互异时空指标反对称化：$\epsilon$求和中的24个非零项，每次交换两个互异指标，都使$\epsilon$与$\gamma$矩阵乘积各变号，因而每项都等于$\epsilon_{0123}\gamma^0\gamma^1\gamma^2\gamma^3$。代入约定$\epsilon_{0123}=-1$，得到

<span id="eq:c36-gamma-five-epsilon"></span>

$$
\gamma_5=i\gamma^0\gamma^1\gamma^2\gamma^3
=-\frac{i}{24}\epsilon_{\mu\nu\rho\sigma}
                    \gamma^\mu\gamma^\nu\gamma^\rho\gamma^\sigma.
\tag{36.48}
$$

块结构还给出$\{\gamma_5,\gamma^\mu\}=0$，所以$\gamma^\mu P_L=P_R\gamma^\mu$。这说明投影狄拉克方程时，一阶导数连接相反的矩阵块；当$m=0$时，两种外尔方程各自封闭。此时的变换$\Psi_M\mapsto e^{i\alpha\gamma_5}\Psi_M$对应于$\psi\mapsto e^{-i\alpha}\psi$，保持马约拉纳条件。非零质量项含两个同手场，正是它破坏了这个连续相位对称性。

<span id="c36-lorentz"></span>

## 四分量的洛伦兹变换

最后将左右手场的洛伦兹变换也合并起来。两种外尔场分别按$\psi_a(x)\mapsto L_a{}^c\psi_c(\Lambda^{-1}x)$和$\psi^\dagger_{\dot a}(x)\mapsto
R_{\dot a}{}^{\dot c}\psi^\dagger_{\dot c}(\Lambda^{-1}x)$变换，其中$R=L^*$。由于$\Psi$下块使用上点分量，还要对右手矩阵作一次与升指标相应的换基，实际的有限变换矩阵为

<span id="eq:c36-finite-dirac-lorentz"></span>

$$
D(\Lambda)=
\begin{pmatrix}L(\Lambda)&0\\0&E^{-1}R(\Lambda)E\end{pmatrix}
=\begin{pmatrix}L&0\\0&(L^\dagger)^{-1}\end{pmatrix}.
\tag{36.49}
$$

这一换基正是第34节从下点列到上点列所求得的变换。上下块无论由两个独立外尔场组成，还是受马约拉纳条件联系，都因此满足统一形式：

<span id="eq:c36-dirac-transformation"></span>

$$
U(\Lambda)^{-1}\Psi(x)U(\Lambda)
=D(\Lambda)\Psi(\Lambda^{-1}x).
\tag{36.50}
$$

再求它的生成元。将作用于下指标场列的两个矩阵展开为$L=I+i\omega_{\mu\nu}S_L^{\mu\nu}/2+O(\omega^2)$和$R=I+i\omega_{\mu\nu}S_{R,\rm down}^{\mu\nu}/2+O(\omega^2)$。根据第35节[（35.20）](/posts/srednicki-35/#eq:c35-raised-lowered-generator)，将两个自由指标升降所得的生成元张量是$T_R=(S_R)^{\dot a}{}_{\dot c}=-E^{-1}S_{R,\rm down}E$，而作用在上点场列上的生成矩阵为$-T_R$。因此，两块合并后给出

<span id="eq:c36-spin-generators"></span>

$$
\begin{aligned}
S^{\mu\nu}
&=\begin{pmatrix}S_L^{\mu\nu}&0\\0&-T_R^{\mu\nu}\end{pmatrix}\\
&=\frac i4
\begin{pmatrix}
\sigma^\mu\bar\sigma^\nu-\sigma^\nu\bar\sigma^\mu&0\\
0&\bar\sigma^\mu\sigma^\nu-\bar\sigma^\nu\sigma^\mu
\end{pmatrix}
=\frac i4[\gamma^\mu,\gamma^\nu].
\end{aligned}
\tag{36.51}
$$

下块前的负号正好补偿了右手自由指标的升降次序，使整个矩阵作用于所选的四分量场列。相应的无穷小变换为

<span id="eq:c36-infinitesimal-dirac"></span>

$$
D(I+\omega)=I_4+\frac i2\omega_{\mu\nu}S^{\mu\nu}+O(\omega^2).
\tag{36.52}
$$

若要分别看旋转和推动如何作用，只需在[（36.51）](#eq:c36-spin-generators)中代入泡利矩阵乘法，求出两类时空指标的分量：

<span id="eq:c36-rotations-boosts"></span>

$$
S^{ij}=\frac12\epsilon_{ijk}
       \begin{pmatrix}\sigma_k&0\\0&\sigma_k\end{pmatrix},
\qquad
S^{i0}=\frac i2\begin{pmatrix}\sigma_i&0\\0&-\sigma_i\end{pmatrix}.
\tag{36.53}
$$

两块在转动下受到相同作用，在推动下则有相反的号。以$z$轴为例，转动和推动参数分别为$\omega_{12}=-\theta$、$\omega_{30}=\eta$。一参数群的复合律使有限矩阵满足$dD_R/d\theta=-iS^{12}D_R$、$dD_B/d\eta=iS^{30}D_B$，初值均为$I_4$，故解为相应矩阵的指数。代入$\sigma_3=\operatorname{diag}(1,-1)$即可逐个指数化：

<span id="eq:c36-finite-axis-matrices"></span>

$$
\begin{aligned}
D_R(\theta)=e^{-i\theta S^{12}}
&=\operatorname{diag}\bigl(e^{-i\theta/2},e^{+i\theta/2},
 e^{-i\theta/2},e^{+i\theta/2}\bigr),\\
D_B(\eta)=e^{+i\eta S^{30}}
&=\operatorname{diag}\bigl(e^{-\eta/2},e^{+\eta/2},
 e^{+\eta/2},e^{-\eta/2}\bigr).
\end{aligned}
$$

转动$2\pi$给出$-I_4$，体现旋量的双值性。推动矩阵一般不幺正，但左右两块的指数相反，满足$D_B^\dagger\beta D_B=\beta$。

还可以直接用这些四分量矩阵看出作用量的协变性。先对[（36.49）](#eq:c36-finite-dirac-lorentz)按块相乘，得到$D^\dagger\beta D=\beta$，因此狄拉克伴随按$\bar\Psi\mapsto\bar\Psi D^{-1}$变换。再将同一个变换作用于$\gamma$矩阵，利用第 34、35 节的$\sigma$变换关系，便有

<span id="eq:c36-gamma-covariance"></span>

$$
\begin{aligned}
D^{-1}\gamma^\mu D
&=\begin{pmatrix}
0&L^{-1}\sigma^\mu(L^\dagger)^{-1}\\
L^\dagger\bar\sigma^\mu L&0
\end{pmatrix}
=\Lambda^\mu{}_\nu\gamma^\nu.
\end{aligned}
\tag{36.54}
$$

上块由$\sigma^\mu=\Lambda^\mu{}_\nu L\sigma^\nu L^\dagger$移项求得，下块则是[（35.29）](/posts/srednicki-35/#eq:c35-barsigma-covariance)。所以$\bar\Psi\Psi$在变换中保持不变，是洛伦兹标量；$\bar\Psi\gamma^\mu\Psi$按矢量变换，再与导数的逆变换缩并，动能也成为标量。四分量作用量因此保留了最初从两分量不变符号出发建立的洛伦兹不变性。

<span id="c36-second-order"></span>

## 二阶动能的模式与范数

将开头的二阶候选具体写成一个自由模型，可以同时算出它的模式代数和能量。取

<span id="eq:c36-second-order-model"></span>

$$
\mathcal L_2=\frac12\left(
\partial^\mu\psi^a\partial_\mu\psi_a+M^2\psi^a\psi_a\right)
+\mathrm{h.c.},\qquad M>0.
$$

这里场的量纲为1。正的$M^2$使模式频率为实数。令$q=\psi_1$、$r=\psi_2$，则$\psi^a\psi_a=-2qr$。在周期盒中选实的正交归一基$u_n$，满足$-\nabla^2u_n=\kappa_n^2u_n$，将场展开为$\psi_a=\sum_nu_n\psi_{an}$。空间积分后各模式分离，其中一项为

<span id="eq:c36-second-order-mode"></span>

$$
L_n=\dot q\dot r-\omega_n^2qr
-\dot q^\dagger\dot r^\dagger+\omega_n^2q^\dagger r^\dagger,
\qquad \omega_n^2=\kappa_n^2+M^2.
$$

时间项的符号来自$g^{00}=-1$及旋量缩并中的$-2$。在这个模式中，将速度变分放在右端来定义动量，例如$\delta L_n=p_q\delta\dot q+\cdots$，便得到$p_q=-\dot r$、$p_r=\dot q$、$p_{q^\dagger}=\dot r^\dagger$、$p_{r^\dagger}=-\dot q^\dagger$。速度可全部由动量解出，因而没有一阶外尔动能的初级约束。

为对角化这个模式，作保持共轭关系的换元$c=(q+r^\dagger)/\sqrt2$、$d=(q-r^\dagger)/\sqrt2$。例如$qr+r^\dagger q^\dagger=cc^\dagger-dd^\dagger=-c^\dagger c+d^\dagger d$，导数部分也有同样的展开。略去模式标签后，拉格朗日量成为

<span id="eq:c36-second-order-oscillators"></span>

$$
L_n=L_+[d]+L_-[c],\qquad
L_s[\zeta]=s(\dot\zeta^\dagger\dot\zeta-\omega^2\zeta^\dagger\zeta),
\qquad s=\pm1.
$$

对其中一个振子，右动量为$P=s\dot\zeta^\dagger$、$\bar P=-s\dot\zeta=-P^\dagger$。保持动量在速度左侧作勒让德变换，有

<span id="eq:c36-second-order-hamiltonian"></span>

$$
\begin{aligned}
H_s&=P\dot\zeta+\bar P\dot\zeta^\dagger-L_s\\
&=s(\dot\zeta^\dagger\dot\zeta+\omega^2\zeta^\dagger\zeta)
=-sP\bar P+s\omega^2\zeta^\dagger\zeta.
\end{aligned}
$$

采用正则反对易关系$\{\zeta,P\}=i$、$\{\zeta^\dagger,\bar P\}=i$，其余基本反对易子为零。第一式的共轭因$P^\dagger=-\bar P$而恢复第二式，所以这套代数与共轭相容。改用坐标和速度表示，就是

<span id="eq:c36-second-order-car"></span>

$$
\{\zeta,\zeta^\dagger\}=0,\qquad
\{\dot\zeta,\dot\zeta^\dagger\}=0,\qquad
\{\zeta,\dot\zeta^\dagger\}=is,\qquad
\{\dot\zeta,\zeta^\dagger\}=-is.
$$

它也给出所需的海森堡方程。利用$[A,BC]=\{A,B\}C-B\{A,C\}$，有$[\zeta,H_s]=-is\bar P=i\dot\zeta$及$[P,H_s]=-is\omega^2\zeta^\dagger=i\dot P$，合起来就是$\ddot\zeta+\omega^2\zeta=0$。写出一般解及其共轭，

<span id="eq:c36-second-order-frequencies"></span>

$$
\zeta(t)=\frac{ae^{-i\omega t}+b^\dagger e^{i\omega t}}{\sqrt{2\omega}},
\qquad
\zeta^\dagger(t)=\frac{a^\dagger e^{i\omega t}+be^{-i\omega t}}{\sqrt{2\omega}}.
$$

这个展开保留了全部初始数据，因为$t=0$时可反解为$a=\sqrt{\omega/2}\,\zeta+i\dot\zeta/\sqrt{2\omega}$和$b^\dagger=\sqrt{\omega/2}\,\zeta-i\dot\zeta/\sqrt{2\omega}$。代回正则关系，混合反对易子全部为零。记$A=\{a,a^\dagger\}$、$B=\{b,b^\dagger\}$，其余两条独立关系给出

<span id="eq:c36-second-order-opposite-norms"></span>

$$
\frac{A+B}{2\omega}=0,\qquad
\frac{i(A-B)}2=is
\quad\Longrightarrow\quad
\{a,a^\dagger\}=s,\qquad\{b,b^\dagger\}=-s.
$$

无论$s$取何号，总有一支的反对易子为负。例如$s=+1$时，在正定态空间中应有$\langle v|\{b,b^\dagger\}|v\rangle=\|bv\|^2+\|b^\dagger v\|^2\geq0$，上式却使它等于$-\|v\|^2$。这在单个模式上已构成矛盾。

能量也须用这套反对易关系计算。将模式展开代回$H_s$，动能和势能中的交叉项抵消，对角项相加，得到

<span id="eq:c36-second-order-energy"></span>

$$
H_s=s\omega(a^\dagger a+bb^\dagger)
=s\omega(a^\dagger a-b^\dagger b)-\omega.
$$

减去真空常数后，$H_{s,N}=s\omega(a^\dagger a-b^\dagger b)$。由于两支模式的反对易号也相反，$[H_{s,N},a^\dagger]=\omega a^\dagger$、$[H_{s,N},b^\dagger]=\omega b^\dagger$：两种产生算符都将能量升高$\omega$。若允许不定内积，并取$a|0\rangle=b|0\rangle=0$及$\langle0|0\rangle=1$，四个模式态为

| 态                                  | 减去真空常数后的能量 | 范数平方 |
| ----------------------------------- | -------------------: | -------: |
| $\lvert0\rangle$                    |                  $0$ |      $1$ |
| $a^\dagger\lvert0\rangle$           |             $\omega$ |      $s$ |
| $b^\dagger\lvert0\rangle$           |             $\omega$ |     $-s$ |
| $a^\dagger b^\dagger\lvert0\rangle$ |            $2\omega$ |     $-1$ |

最后一行的范数由$\langle0|baa^\dagger b^\dagger|0\rangle=s(-s)=-1$给出。这个二阶模型在保持正则代数时可以有非负激发能，代价是不定内积；其障碍是正定范数与正则量子化不相容。一阶外尔动能改变了约束结构，场及其共轭的等时反对易子成为非零，具体量子化见[下一节](/posts/srednicki-37/)。

---

[← 第 35 节](/posts/srednicki-35/) · [章节地图](/srednicki/) · [第 37 节 →](/posts/srednicki-37/)
