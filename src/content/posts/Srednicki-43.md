---
title: 'Srednicki §43 费米子场的路径积分'
date: 2026-09-14
category: 笔记
tags: [物理, 量子场论, Srednicki]
series: 'Srednicki QFT'
srednickiSections: [43]
hideFromHome: true
draft: false
---

<span id="c43"></span>

自由费米场的时间序矩阵元可以由一个带外源的生成泛函产生。源与场同为反交换变量，源导数便能记录场交换的负号。先在有限个格拉斯曼生成元上把积分定义为最高次系数的提取，再完成作用量中的平方，即可求出生成泛函；二点、四点和一般配对将与[第42节](/posts/srednicki-42/#c42-wick)的模式计算相接。相互作用中的有序场单项式也由同序的源导数生成。

<span id="c43-scalar"></span>

## 实标量与复标量的参照

先回想自由实标量场。令$K_B=-\partial^2+m^2$，要把作用量写成便于积分的二次型，就需将动能项中的一个导数移到另一份场上。乘积法则给出
<span id="eq:c43-real-quadratic"></span>

$$
\begin{aligned}
\partial_\mu(\varphi\partial^\mu\varphi)
&=(\partial_\mu\varphi)(\partial^\mu\varphi)
  +\varphi\partial^2\varphi,\\
\mathcal L_{0,R}
&=-\frac12\partial^\mu\varphi\,\partial_\mu\varphi
  -\frac12m^2\varphi^2\\
&=-\frac12\varphi K_B\varphi
  -\frac12\partial_\mu(\varphi\partial^\mu\varphi).
\end{aligned}
\tag{43.1}
$$

在周期边界条件下，或边界上的场使表面项消失时，总散度不贡献作用量，所余的二次核便决定高斯积分。第8节用$m^2\mapsto m^2-i\epsilon$选定入、出真空的费曼边界条件，相应的逆核为
<span id="eq:c43-scalar-inverse"></span>

$$
\begin{aligned}
\Delta_\epsilon(x-y)
&=\int\frac{d^4k}{(2\pi)^4}
 \frac{e^{ik(x-y)}}{k^2+m^2-i\epsilon},\\
(K_B-i\epsilon)\Delta_\epsilon&=\delta^4,
\qquad K_B\Delta=\delta^4,\quad
\Delta=\lim_{\epsilon\to0^+}\Delta_\epsilon .
\end{aligned}
\tag{43.2}
$$

这两条逆关系适用于不同阶段：保留调节器时，对应的是受调节波算符；撤去调节后，才得到后一条分布恒等式。真空投影所需的谱条件和时间端点处理见[第6节](/posts/srednicki-06/#c06)，场核的具体积分见[第8节](/posts/srednicki-08/#c08-functional)。

有了逆核，就可以移去作用量中的线性源项。为简写二次型，以下重复的连续指标包括时空积分，例如$J\Delta J=\int d^4x\,d^4y\,J(x)\Delta(x-y)J(y)$。实场的平方完成写成
<span id="eq:c43-real-square"></span>

$$
-\frac12\varphi K_B\varphi+J\varphi
=-\frac12(\varphi-\Delta J)K_B(\varphi-\Delta J)
 +\frac12J\Delta J .
\tag{43.3}
$$

展开右端时，由于$\Delta^T=\Delta$，两个交叉项相同；它们各带$1/2$，合起来恰好还原$J\varphi$。实际积分先使用$K_B-i\epsilon$及其逆来作同一平移。平移后的场积分与外源无关，除以零源积分就将它消去，剩下只依赖外源的生成泛函：
<span id="eq:c43-real-generator"></span>

$$
Z_{0,R}[J]
=\frac{\int\mathcal D\varphi\,
 e^{i\int d^4x(\mathcal L_{0,R}+J\varphi)}}
 {\int\mathcal D\varphi\,e^{i\int d^4x\mathcal L_{0,R}}}
=\exp\!\left(\frac i2J\Delta J\right).
\tag{43.4}
$$

也可将这个分母吸收到测度的归一化中，使$Z_{0,R}[0]=1$。现在对指数中的$J\varphi$求导，每次都会带下$i\varphi$；在导数前乘以相应因子，再令源为零，便得到场插入公式：
<span id="eq:c43-real-insertions"></span>

$$
\langle0|T\varphi(x_1)\cdots\varphi(x_n)|0\rangle
=\left.
 \prod_{a=1}^n\frac1i\frac{\delta}{\delta J(x_a)}
 Z_{0,R}[J]\right|_{J=0}.
\tag{43.5}
$$

这里的时间序由先前的路径积分构造确定，源导数则把场插到指定的时空点。这一方法也适用于复标量场，只是场与伴随场各需一份源。先用同一乘积法则整理复场拉氏密度：
<span id="eq:c43-complex-quadratic"></span>

$$
\begin{aligned}
\mathcal L_{0,C}
&=-\partial^\mu\varphi^\dagger\partial_\mu\varphi
  -m^2\varphi^\dagger\varphi\\
&=-\varphi^\dagger K_B\varphi
  -\partial_\mu(\varphi^\dagger\partial^\mu\varphi).
\end{aligned}
\tag{43.6}
$$

加入源项$J^\dagger\varphi+\varphi^\dagger J$后，按照[第8节的复标量源](/posts/srednicki-08/#eq:c08-complex-source)，求导时把$J,J^\dagger$视为独立变量。两份实场的二次型合成复场二次型，平方完成及归一积分随之成为
<span id="eq:c43-complex-generator"></span>

$$
\begin{aligned}
&-\varphi^\dagger K_B\varphi+J^\dagger\varphi+\varphi^\dagger J\\
&\quad=-(\varphi^\dagger-J^\dagger\Delta)K_B(\varphi-\Delta J)
 +J^\dagger\Delta J,\\
Z_{0,C}[J^\dagger,J]&=\exp(iJ^\dagger\Delta J).
\end{aligned}
\tag{43.7}
$$

两类源分别与场和伴随场耦合，因而指数中没有实场的$1/2$。插入时，每个$\varphi$由$J^\dagger$导数产生，每个$\varphi^\dagger$由$J$导数产生：
<span id="eq:c43-complex-insertions"></span>

$$
\begin{aligned}
&\langle0|T\varphi(x_1)\cdots\varphi(x_r)
 \varphi^\dagger(y_1)\cdots\varphi^\dagger(y_s)|0\rangle\\
&\quad=\left.
 \prod_{a=1}^r\frac1i\frac{\delta}{\delta J^\dagger(x_a)}
 \prod_{b=1}^s\frac1i\frac{\delta}{\delta J(y_b)}
 Z_{0,C}[J^\dagger,J]\right|_{J=J^\dagger=0}.
\end{aligned}
\tag{43.8}
$$

这两套源及其插入规则，为构造狄拉克生成泛函提供了参照。接下来要改变的是源的代数性质，使求导本身带出费米统计的符号。

<span id="c43-left-derivatives"></span>

## 奇源的左导数

普通数值源的导数互相对易，而费米场的时间排序还要计入交换号。为使这两种操作相配，我们为狄拉克场引入格拉斯曼奇源$\eta,\bar\eta$，并令它们与费米积分变量及其它奇源反交换。同一个奇生成元的平方因而为零。求导时，$\eta$与$\bar\eta$作为两套独立变量；横线标明相应的对偶旋量，并不把这一源规定成$\eta$的函数。

奇变量的变分放在哪一侧，会影响导数的符号。这里统一采用左导数：暂以离散指标$a$代表旋量和时空标签，令变分写在最左边，由$\delta F=\delta\eta_a\,\partial_a^L F$定义导数。若$A$具有确定的奇偶性$|A|=0,1$，乘积法则就是
<span id="eq:c43-left-leibniz"></span>

$$
\begin{aligned}
\partial_a^L(AB)
&=(\partial_a^L A)B+(-1)^{|A|}A(\partial_a^L B),\\
\partial_a^L\eta_b&=\delta_{ab},
\qquad
\partial_a^L\partial_b^L=-\partial_b^L\partial_a^L .
\end{aligned}
\tag{43.9}
$$

第二项来自对后一个因子作变分，再把$\delta\eta_a$从$A$的右边移到最左边，因此其符号取决于前一因子的奇偶性。例如$\partial_1^L(\eta_1\eta_2)=\eta_2$，而$\partial_2^L(\eta_1\eta_2)=-\eta_1$；对这两式再分别求另一个导数，便得到上面的反交换关系。恢复连续标签时，只需把$\delta_{ab}$换成$\delta_{\alpha\beta}\delta^4(x-y)$。第37节定义正则动量时采用过右速度导数，这里的源导数则统一取左导数。

现在将这个规则用于源耦合。设$\mathscr J_F=\int d^4y\,[\bar\eta_\gamma(y)\Psi_\gamma(y)
+\bar\Psi_\gamma(y)\eta_\gamma(y)]$，两种源所在的位置不同，左微分越过的奇变量也不同，因而两次变分分别给出
<span id="eq:c43-source-variation"></span>

$$
\begin{aligned}
\frac{\delta^L\mathscr J_F}{\delta\eta_\alpha(x)}
&=-\int d^4y\,\bar\Psi_\gamma(y)
 \delta_{\gamma\alpha}\delta^4(y-x)
 =-\bar\Psi_\alpha(x),\\
\frac{\delta^L\mathscr J_F}{\delta\bar\eta_\alpha(x)}
&=+\int d^4y\,\delta_{\alpha\gamma}\delta^4(x-y)
 \Psi_\gamma(y)
 =+\Psi_\alpha(x).
\end{aligned}
\tag{43.10}
$$

对$\eta$求导时要越过奇场$\bar\Psi$，对$\bar\eta$求导则直接作用于最左端的源，所以只有前者变号。另一方面，$\mathscr J_F$是偶量，与自己的奇导数交换，指数仍满足$\delta^L e^{i\mathscr J_F}=i(\delta^L\mathscr J_F)e^{i\mathscr J_F}$。将这个因子与刚才的符号一并计入，产生两种场的插入算符应为
<span id="eq:c43-dirac-insertion-operators"></span>

$$
\begin{aligned}
\mathcal O_{\Psi_\alpha(x)}
&=\frac1i\frac{\delta^L}{\delta\bar\eta_\alpha(x)},&
\mathcal O_{\bar\Psi_\alpha(x)}
&=i\frac{\delta^L}{\delta\eta_\alpha(x)},\\
\mathcal O_{\Psi_\alpha(x)}e^{i\mathscr J_F}
&=\Psi_\alpha(x)e^{i\mathscr J_F},&
\mathcal O_{\bar\Psi_\alpha(x)}e^{i\mathscr J_F}
&=\bar\Psi_\alpha(x)e^{i\mathscr J_F}.
\end{aligned}
\tag{43.11}
$$

伴随场插入前的因子是$i$，因为$i(-i)=1$；若也使用$1/i$，就会多出一个负号。源耦合同时确定源的量纲：四维拉氏密度的维数为四，而$[\Psi]=3/2$，故$[\eta]=[\bar\eta]=5/2$。

单次插入确定以后，还需说明多次求导怎样排列。微分算符总是由右端先作用。若$\Phi_1,\ldots,\Phi_n$是按指定次序排列的奇场，并假定后$n-1$次插入已产生相应的场链，则最左微分须越过这$n-1$份场才能作用于指数。因此
<span id="eq:c43-ordered-insertion-proof"></span>

$$
\begin{aligned}
\mathcal O_{\Phi_1}\cdots\mathcal O_{\Phi_n}e^{i\mathscr J_F}
&=(-1)^{n-1}\Phi_2\cdots\Phi_n\Phi_1e^{i\mathscr J_F}\\
&=\Phi_1\Phi_2\cdots\Phi_ne^{i\mathscr J_F}.
\end{aligned}
\tag{43.12}
$$

第一行的新插入$\Phi_1$位于链尾；把它移回链首又需越过$n-1$个奇场，两个换序符号恰好相消。因此，导数链与场链可以保持同一书写次序，得到
<span id="eq:c43-dirac-correlators"></span>

$$
\begin{aligned}
&\langle0|T\Psi_{\alpha_1}(x_1)\cdots
 \bar\Psi_{\beta_1}(y_1)\cdots|0\rangle\\
&\quad=\left.
 \frac1i\frac{\delta^L}{\delta\bar\eta_{\alpha_1}(x_1)}\cdots
 i\frac{\delta^L}{\delta\eta_{\beta_1}(y_1)}\cdots
 Z_{0,D}[\bar\eta,\eta]\right|_{\eta=\bar\eta=0}.
\end{aligned}
\tag{43.13}
$$

这个等式把右端格拉斯曼变量的微分与左端量子场的时间序矩阵元联系起来。要使这一联系成立，还需找到相应的$Z_{0,D}$，并说明它产生的矩阵元与上一节的自由场结果相同。

<span id="c43-dirac-gaussian"></span>

## 狄拉克自由生成泛函

构造生成泛函仍从自由作用量的二次核开始。将狄拉克拉氏密度写为
<span id="eq:c43-dirac-quadratic"></span>

$$
\mathcal L_{0,D}
=i\bar\Psi\slashed\partial\Psi-m\bar\Psi\Psi
=-\bar\Psi\mathscr D\Psi,
\qquad
\mathscr D=-i\slashed\partial+m .
\tag{43.14}
$$

这个一阶波算符的双侧逆，正是[第42节传播子](/posts/srednicki-42/#eq:c42-fourier-propagator)。核与逆关系分别为
<span id="eq:c43-dirac-kernel"></span>

$$
S(x-y)=\int\frac{d^4p}{(2\pi)^4}
 \frac{(-\slashed p+m)e^{ip(x-y)}}{p^2+m^2-i0},
\qquad
\mathscr D_xS(x-y)=\delta^4(x-y)I_4.
\tag{43.15}
$$

平方完成需要二次核的双侧逆。可以先在有限模式空间取一个可逆矩阵$D$，令$S=D^{-1}$；若以连续记号保留调节器，一种相容的选择是
<span id="eq:c43-compatible-regulator"></span>

$$
m_\epsilon=\sqrt{m^2-i\epsilon},\qquad
D_\epsilon=-i\slashed\partial+m_\epsilon,\qquad
\widetilde S_\epsilon(p)=
 \frac{-\slashed p+m_\epsilon}{p^2+m^2-i\epsilon}.
\tag{43.16}
$$

取$m_\epsilon\to m>0$的一支，就有精确的$D_\epsilon S_\epsilon=1$。这里有限$\epsilon$同时改变分母和分子，撤去调节后才恢复式[（43.15）](#eq:c43-dirac-kernel)。以下平方完成都使用相容的$D,S$，连续核的无调节记号表示最终费曼边界值。

为了在平方完成后平移格拉斯曼变量，先给出有限个生成元的积分定义，并由此说明积分的平移不变性。将场生成元按$\theta_1,\ldots,\theta_N$排列，所有外源写在它们右边，并把积分定义为最高次场单项式的系数：
<span id="eq:c43-finite-integration"></span>

$$
\int d\theta_N\cdots d\theta_1\,
 \sum_{I} \theta_{i_1}\cdots\theta_{i_r}\,c_I(\eta)
 =c_{\{1,\ldots,N\}}(\eta),\qquad i_1<\cdots<i_r .
\tag{43.17}
$$

单变量的特例是$\int d\theta\,1=0$、$\int d\theta\,\theta=1$，这就是贝雷津积分。若作奇平移，将$\theta_a$换成$\chi_a+\xi_a(\eta)$，原来低于最高场次数的项不可能增加场次数，而最高项中$\chi_1\cdots\chi_N$的系数仍为一。因此，积分所提取的最高次系数不变。我们可以据此像处理高斯积分那样平移场变量；格拉斯曼测度的一般规则将在下一节展开。

对狄拉克二次型，取$\chi=\Psi-S\eta$、$\bar\chi=\bar\Psi-\bar\eta S$，保持奇量原有次序展开，得到
<span id="eq:c43-dirac-square"></span>

$$
\begin{aligned}
&-(\bar\Psi-\bar\eta S)D(\Psi-S\eta)\\
&\quad=-\bar\Psi D\Psi+\bar\Psi\eta+\bar\eta\Psi
 -\bar\eta S\eta,\\
&-\bar\Psi D\Psi+\bar\eta\Psi+\bar\Psi\eta\\
&\quad=-\bar\chi D\chi+\bar\eta S\eta .
\end{aligned}
\tag{43.18}
$$

第一行展开后的第二、三项分别使用$DS=1$和$SD=1$。数值核是偶量，消去核与其逆的过程中，奇场和奇源始终保持原次序。平移后，全部源依赖留在最后一个二次项中，余下的积分恰好等于零源分母，因而
<span id="eq:c43-dirac-generator"></span>

$$
\begin{aligned}
Z_{0,D}[\bar\eta,\eta]
&=\frac{\int\mathcal D\Psi\,\mathcal D\bar\Psi\,
 e^{i(-\bar\Psi D\Psi+\bar\eta\Psi+\bar\Psi\eta)}}
 {\int\mathcal D\Psi\,\mathcal D\bar\Psi\,e^{-i\bar\Psi D\Psi}}\\
&=\exp\!\left[
 i\int d^4x\,d^4y\,
 \bar\eta_\alpha(x)S_{\alpha\beta}(x-y)\eta_\beta(y)\right].
\end{aligned}
\tag{43.19}
$$

这里的$\Psi,\bar\Psi$是独立的格拉斯曼积分变量。改变有限积分中变量的排列次序，会改变共同的源无关因子，而这个因子已在归一比值中消去。将这一分母并入测度，也就得到$Z_{0,D}[0,0]=1$的归一约定。

<span id="c43-dirac-tests"></span>

## 直接求出狄拉克二点与四点

生成泛函已求出，接下来用它计算最简单的矩阵元。暂将连续标签缩写成离散指标，记$Q_D=i\bar\eta_aS_{ab}\eta_b$。混合二点函数的导数链从右边的$\eta_b$导数开始：
<span id="eq:c43-dirac-two-point"></span>

$$
\begin{aligned}
\partial_{\eta_b}^LQ_D&=-i\bar\eta_cS_{cb},\\
i\partial_{\eta_b}^L e^{Q_D}&=\bar\eta_cS_{cb}e^{Q_D},\\
\left.\frac1i\partial_{\bar\eta_a}^L
 i\partial_{\eta_b}^L e^{Q_D}\right|_0
&=\frac1iS_{ab}=-iS_{ab}.
\end{aligned}
\tag{43.20}
$$

最后一次微分若作用于指数，就会留下两份源，令源为零后该项消失；只有作用于显式$\bar\eta_c$的部分留下$S_{ab}/i$。这给出$i\langle T\Psi_a\bar\Psi_b\rangle=S_{ab}$，而倒转两次奇导数的次序便得到带相反符号的反序二点核。对于同类场，指数中的每个因子同时含一份$\eta$和一份$\bar\eta$，两次同类源微分总会留下另一类源，因此零源处的同类狄拉克二点函数为零。这与上一节模算符计算中的粒子、反粒子配对相符。

四点函数能进一步说明不同配对之间的相对符号。所需项是$e^{Q_D}$中的$Q_D^2/2$；把第一个$\eta$移过第二个$\bar\eta$时得到的负号，与$i^2=-1$相消，因而
<span id="eq:c43-dirac-quartic-source"></span>

$$
\frac{Q_D^2}{2}
=\frac12\bar\eta_a\bar\eta_c\,S_{ab}S_{cd}\,\eta_b\eta_d .
\tag{43.21}
$$

固定四个不同标签，将源统一排成$\bar\eta_a,\bar\eta_c,\eta_b,\eta_d$的次序。原来的求和中，交换两个$\bar\eta$或两个$\eta$各会变号，将这四种选取合并，规范单项式的系数为
<span id="eq:c43-dirac-quartic-coefficient"></span>

$$
\begin{aligned}
\relax
[\bar\eta_a\bar\eta_c\eta_b\eta_d]\,e^{Q_D}
&=\frac12\bigl(
 S_{ab}S_{cd}-S_{ad}S_{cb}
 -S_{cb}S_{ad}+S_{cd}S_{ab}\bigr)\\
&=S_{ab}S_{cd}-S_{ad}S_{cb}.
\end{aligned}
\tag{43.22}
$$

这里方括号表示提取所写单项式的系数，与对易子无关。为了生成按$\Psi_a\bar\Psi_b\Psi_c\bar\Psi_d$排列的场链，应使用导数链$\partial_{\bar\eta_a}^L\partial_{\eta_b}^L
\partial_{\bar\eta_c}^L\partial_{\eta_d}^L$，四个插入前因子之积为一。
这些导数仍由右端先作用，将单项式依次变成
<span id="eq:c43-dirac-four-derivatives"></span>

$$
\bar\eta_a\bar\eta_c\eta_b\eta_d
 \ \longrightarrow\ -\bar\eta_a\bar\eta_c\eta_b
 \ \longrightarrow\ +\bar\eta_a\eta_b
 \ \longrightarrow\ -\bar\eta_a
 \ \longrightarrow\ -1.
\tag{43.23}
$$

将这个微分符号乘回刚求出的源系数，就得到四点函数：
<span id="eq:c43-dirac-four-point"></span>

$$
i^2\langle T\Psi_a\bar\Psi_b\Psi_c\bar\Psi_d\rangle
 =S_{ab}S_{cd}-S_{ad}S_{cb}.
\tag{43.24}
$$

恢复时空点和旋量指标后，结果便是式[（42.33）](/posts/srednicki-42/#eq:c42-dirac-four-point)。即使同类标签重合，这个表达式仍然相容：相应奇微分的平方为零，右端两项也恰好相消。生成泛函的左导数因此同时给出了二点核与不同配对的相对负号。

<span id="c43-interaction"></span>

## 相互作用仍可换成源导数

自由生成泛函一旦确定，相互作用的处理就可以沿用标量场的方法。先看复标量场：对于给定的$\mathcal L_1(\varphi^\dagger,\varphi)$，将每份场换成相应源导数，并定义
<span id="eq:c43-scalar-interaction"></span>

$$
\begin{aligned}
\mathscr V_C
&=\exp\!\left[
 i\int d^4x\,\mathcal L_1\!\left(
 \frac1i\frac{\delta}{\delta J(x)},
 \frac1i\frac{\delta}{\delta J^\dagger(x)}
 \right)\right],\\
Z_C[J^\dagger,J]
&=\frac{\mathscr V_C Z_{0,C}[J^\dagger,J]}
 {(\mathscr V_C Z_{0,C})[0,0]} .
\end{aligned}
\tag{43.25}
$$

这一写法来自[第9节的源算符展开](/posts/srednicki-09/#c09-source-operator)。把$e^{i\int\mathcal L_1}$逐项展开后，每个场都能由相应的源导数产生；将导数提出自由积分，便留下它们对自由生成泛函的作用。分母消去与外源无关的真空因子，使零源值保持为一。

对于狄拉克场，式[（43.12）](#eq:c43-ordered-insertion-proof)已经说明，同样的替换也能保留奇场的有序单项式。因而，若$\mathcal L_1(\bar\Psi,\Psi)$是格拉斯曼偶的相互作用，只需在原有次序上使用费米插入算符，便得到
<span id="eq:c43-dirac-interaction"></span>

$$
\begin{aligned}
\mathscr V_D
&=\exp\!\left[
 i\int d^4x\,\mathcal L_1\!\left(
 i\frac{\delta^L}{\delta\eta(x)},
 \frac1i\frac{\delta^L}{\delta\bar\eta(x)}
 \right)\right],\\
Z_D[\bar\eta,\eta]
&=\frac{\mathscr V_D Z_{0,D}[\bar\eta,\eta]}
 {(\mathscr V_D Z_{0,D})[0,0]} .
\end{aligned}
\tag{43.26}
$$

在这个替换中，$\mathcal L_1$原有的旋量缩并和场排列都随之保留。作为补充例子，取一个有序四场单项式；先按原次序替换，再将同类导数排在一起，就有
<span id="eq:c43-ordered-vertex-example"></span>

$$
\begin{aligned}
\bar\Psi_a\Psi_b\bar\Psi_c\Psi_d
&\ \longmapsto\
 \partial_{\eta_a}^L\partial_{\bar\eta_b}^L
 \partial_{\eta_c}^L\partial_{\bar\eta_d}^L\\
&=-\partial_{\eta_a}^L\partial_{\eta_c}^L
 \partial_{\bar\eta_b}^L\partial_{\bar\eta_d}^L .
\end{aligned}
\tag{43.27}
$$

四个前因子$i,(1/i),i,(1/i)$相乘为一。第二行将第三个奇导数移过第二个时所出的负号，恰与场单项式的重排

$$
\bar\Psi_a\Psi_b\bar\Psi_c\Psi_d
=-\bar\Psi_a\bar\Psi_c\Psi_b\Psi_d
$$

相对应。相互作用的整体偶性，使它可以置于作用量的指数中；内部的奇因子则仍按各自次序运算。

再看零源归一如何消去真空部分。暂将$\mathcal L_1$乘上无量纲计数参数$\lambda$，并记

$$
\mathscr W=\int d^4x\,\mathcal L_1(\mathcal O_{\bar\Psi},\mathcal O_\Psi).
$$

在固定调节器下，把分子和分母分别展开到一阶，得到
<span id="eq:c43-vacuum-normalization"></span>

$$
\begin{aligned}
\mathscr V_D Z_{0,D}
 &=Z_{0,D}+i\lambda\,\mathscr W Z_{0,D}+O(\lambda^2),\\
(\mathscr V_D Z_{0,D})[0,0]
 &=1+i\lambda(\mathscr W Z_{0,D})[0,0]+O(\lambda^2),\\
Z_D
 &=Z_{0,D}+i\lambda\bigl[
 \mathscr W Z_{0,D}
 -Z_{0,D}(\mathscr W Z_{0,D})[0,0]\bigr]+O(\lambda^2).
\end{aligned}
\tag{43.28}
$$

最后一行用到了分母的倒数$1-i\lambda(\mathscr W Z_{0,D})[0,0]$。它减去相互作用新产生的源无关真空部分，所以令源为零后，一阶修正中的两项相消。完成计数后取$\lambda=1$，更高阶也按同一形式级数相除。

相互作用关联函数仍由式[（43.13）](#eq:c43-dirac-correlators)生成，只需将$Z_{0,D}$换成$Z_D$。由于分母是源无关的偶数值，外部奇微分只作用于分子：自由高斯的微分给出配对，每个相互作用插入则给出一组待配的场，于是逐阶计算自然组织成费曼图。在[第45节](/posts/srednicki-45/#c45)将它写成具体图规则时，还要随着每条收缩保留旋量指标，并随着每次奇因子置换记下符号。

<span id="c43-majorana-square"></span>

## 马约拉纳的一套源与反对称二次核

最后考虑马约拉纳场。它只有一套独立场变量，二次型与实标量场相似，带有$1/2$的系数：
<span id="eq:c43-majorana-quadratic"></span>

$$
\begin{aligned}
\mathcal L_{0,M}
&=\frac i2\Psi^T\mathcal C\slashed\partial\Psi
 -\frac m2\Psi^T\mathcal C\Psi\\
&=-\frac12\Psi^T M\Psi,\qquad M=\mathcal C\mathscr D .
\end{aligned}
\tag{43.29}
$$

这里$\Psi$已表示马约拉纳场。要对这一二次型完成平方，先需了解核的转置性质。转置$M$时，不仅交换旋量指标，也交换连续时空指标；在总散度积分为零的边界条件下，$\partial_\mu^T=-\partial_\mu$，因此
<span id="eq:c43-majorana-antisymmetric-operator"></span>

$$
\begin{aligned}
M^T
&=\bigl(+i(\gamma^\mu)^T\partial_\mu+m\bigr)\mathcal C^T\\
&=-i(\gamma^\mu)^T\mathcal C\,\partial_\mu-m\mathcal C\\
&=+i\mathcal C\gamma^\mu\partial_\mu-m\mathcal C
=-M .
\end{aligned}
\tag{43.30}
$$

第三行使用$(\gamma^\mu)^T\mathcal C=-\mathcal C\gamma^\mu$。上述转置及分部积分均不取复共轭，所以采用式[（43.16）](#eq:c43-compatible-regulator)的复质量调节时，核仍保持反对称。它的逆也随之反对称，而上一节已经给出了这个逆核的具体形式：
<span id="eq:c43-majorana-inverse"></span>

$$
F=M^{-1}=S\mathcal C^{-1},\qquad F^T=-F,\qquad
\mathcal C\mathscr D_x S(x-y)\mathcal C^{-1}
 =\delta^4(x-y)I_4 .
\tag{43.31}
$$

这里$F^T(x,y)=F(y,x)^T$，与上一节的$F(-z)^T=-F(z)$是同一反对称性在两种记号下的表达。

由于只有一套独立场，马约拉纳源耦合取为$\eta^T\Psi$。为使这一项在洛伦兹变换下不变，$\eta$应属于场的对偶空间：若$\Psi\mapsto R\Psi$，则取$\eta\mapsto R^{-T}\eta$，便能保持$\eta^T\Psi$。左微分直接给出$\partial_{\eta_a}^L(\eta_b\Psi_b)=\Psi_a$，所以每次场插入都对应$(1/i)\partial_{\eta_a}^L$，无需另设一套独立的$\bar\eta$。

虽然源的数目与实标量情形相同，平方完成的符号却受奇变量和反对称核共同控制。先取两个奇列$\chi,\xi$，交换它们时有$\xi_aM_{ab}\chi_b=-\chi_bM_{ab}\xi_a=\chi_bM_{ba}\xi_a$，从而$\xi^TM\chi=\chi^TM\xi$。据此选择$\xi=-F\eta$、$\Psi=\chi+\xi$，所需的平移关系为
<span id="eq:c43-majorana-shift-identities"></span>

$$
M\xi=-\eta,\qquad
\xi^T=\eta^TF,\qquad
\xi^TM\xi=-\eta^TF\eta .
\tag{43.32}
$$

第一式用到$MF=1$，第二式则用到$F^T=-F$。将这些关系代入展开后的二次型和线性源项，各项依次成为
<span id="eq:c43-majorana-completion"></span>

$$
\begin{aligned}
-\frac12\Psi^TM\Psi+\eta^T\Psi
&=-\frac12\chi^TM\chi-\chi^TM\xi
  -\frac12\xi^TM\xi+\eta^T\chi+\eta^T\xi\\
&=-\frac12\chi^TM\chi
  +\chi^T\eta+\eta^T\chi
  +\frac12\eta^TF\eta-\eta^TF\eta\\
&=-\frac12\chi^TM\chi-\frac12\eta^TF\eta,
\qquad \chi=\Psi+F\eta .
\end{aligned}
\tag{43.33}
$$

中间的两个线性项由$\chi^T\eta=-\eta^T\chi$相消，纯源项的系数则合成$1/2-1=-1/2$。再利用平移不变性消去共同的零源积分，便得到
<span id="eq:c43-majorana-generator"></span>

$$
\begin{aligned}
Z_{0,M}[\eta]
&=\frac{\int\mathcal D\Psi\,
 e^{i(-\Psi^TM\Psi/2+\eta^T\Psi)}}
 {\int\mathcal D\Psi\,e^{-i\Psi^TM\Psi/2}}\\
&=\exp\!\left[
 -\frac i2\int d^4x\,d^4y\,
 \eta^T(x)S(x-y)\mathcal C^{-1}\eta(y)\right].
\end{aligned}
\tag{43.34}
$$

用各个源导数产生场插入，得到
<span id="eq:c43-majorana-insertions"></span>

$$
\langle0|T\Psi_{\alpha_1}(x_1)\cdots\Psi_{\alpha_n}(x_n)|0\rangle
=\left.
 \frac1i\frac{\delta^L}{\delta\eta_{\alpha_1}(x_1)}\cdots
 \frac1i\frac{\delta^L}{\delta\eta_{\alpha_n}(x_n)}
 Z_{0,M}[\eta]\right|_{\eta=0}.
\tag{43.35}
$$

<span id="c43-majorana-tests"></span>

## 马约拉纳的二点、四点与一般配对

先计算二点函数，以说明指数的负号和二分之一怎样进入收缩。记$Q_M=-i\eta_aF_{ab}\eta_b/2$，左导数作用于两份源时，一项直接给出$F_{ab}\eta_b$，另一项先越过第一份$\eta$，再用$F_{ba}=-F_{ab}$把核的指标换回。因此两项相同，相加后消去$1/2$：
<span id="eq:c43-majorana-two-point"></span>

$$
\begin{aligned}
\partial_{\eta_a}^LQ_M
&=-\frac i2(F_{ab}\eta_b-\eta_bF_{ba})
 =-iF_{ab}\eta_b,\\
\partial_{\eta_a}^L\partial_{\eta_b}^LQ_M
&=-iF_{ba}=+iF_{ab},\\
\left.\frac1i\partial_{\eta_a}^L
 \frac1i\partial_{\eta_b}^L e^{Q_M}\right|_0
&=-iF_{ab}.
\end{aligned}
\tag{43.36}
$$

于是$i\langle T\Psi_a\Psi_b\rangle=F_{ab}= (S\mathcal C^{-1})_{ab}$，与式[（42.27）](/posts/srednicki-42/#eq:c42-majorana-three-kernels)中的收缩一致。狄拉克二点函数的两个插入前因子为$(1/i)\,i=1$，而这里是$(1/i)^2=-1$；两种源指数的相对负号正好与此配合。式[（43.33）](#eq:c43-majorana-completion)从平方完成出发，给出了同一个负号的来源。

四点函数还包含不同配对之间的交换号。取四个不同标签，利用反对称性写成$Q_M=-i\sum_{a<b}F_{ab}\eta_a\eta_b$，则$Q_M^2/2$中$\eta_1\eta_2\eta_3\eta_4$的系数为
<span id="eq:c43-majorana-quartic-coefficient"></span>

$$
[\eta_1\eta_2\eta_3\eta_4]\,e^{Q_M}
=-\bigl(F_{12}F_{34}-F_{13}F_{24}+F_{14}F_{23}\bigr).
\tag{43.37}
$$

对于每个配对，两份偶二次单项式可以按两种次序取出，抵消展开分母中的$2!$。排列$(12)(34)$时源已经有序；$(13)(24)$需要交换$\eta_3,\eta_2$一次，而$(14)(23)$需要将$\eta_4$移过两份源，因而三个配对号依次为加、减、加，共同的负号则来自$(-i)^2$。随后由微分链$\partial_1^L\partial_2^L\partial_3^L\partial_4^L$从右开始删去源，分别越过三、二、一、零份源，总符号为$(-1)^6=+1$。四个$1/i$的乘积也为一，四点函数遂为
<span id="eq:c43-majorana-four-point"></span>

$$
i^2\langle T\Psi_1\Psi_2\Psi_3\Psi_4\rangle
=F_{12}F_{34}-F_{13}F_{24}+F_{14}F_{23}.
\tag{43.38}
$$

这里的三种马约拉纳配对与式[（42.34）](/posts/srednicki-42/#eq:c42-majorana-four-point)相同。将刚才的计数推广，就能得到全部偶数点函数：指数的第$n$次项含有$n$对源，固定一个完全配对后，$n$个偶二次项的$n!$种选取次序恰好抵消指数分母$n!$，每对内部则已按$a<b$排列。把全部源排回$1,\ldots,2n$次序所需的符号，就是配对置换的符号$\operatorname{sgn}\mathcal P$。再对规范排列的$2n$份源由右向左微分，所得符号为$(-1)^{2n(2n-1)/2}=(-1)^n$，它与插入前因子$(1/i)^{2n}=(-1)^n$相消。因此
<span id="eq:c43-general-gaussian-pairing"></span>

$$
\langle T\Psi_1\cdots\Psi_{2n}\rangle
=\frac1{i^n}\sum_{\mathcal P}
 \operatorname{sgn}(\mathcal P)
 \prod_{(a,b)\in\mathcal P}F_{ab}.
\tag{43.39}
$$

奇数次导数无法消去指数项中的全部源，因而在零源处消失。狄拉克情形也可以作同样的计数，只是每个二次项恰含一份$\bar\eta$和一份$\eta$，所以仅允许两类源相配，其余置换符号照旧。这样，两种高斯泛函都产生了第42节的全部自由场配对，并由此确定任意线性场插入的时间序矩阵元。

<span id="c43-finite-check"></span>

## 补充计算：有限模式中的直接积分

作为具体例子，取四个积分生成元和四个源生成元，直接展开有限格拉斯曼积分，看看归一和插入如何作用。狄拉克积分的规范场排列取为$\bar\psi_1\bar\psi_2\psi_1\psi_2$，源排列为$\bar\eta_1\bar\eta_2\eta_1\eta_2$；马约拉纳分别取$\psi_1\psi_2\psi_3\psi_4$和$\eta_1\eta_2\eta_3\eta_4$。各组都按式[（43.17）](#eq:c43-finite-integration)提取最高场系数，并将全部源放在右边。以下有限矩阵和生成元均用无量纲形式，先为狄拉克例子选取
<span id="eq:c43-finite-dirac-input"></span>

$$
\begin{aligned}
D&=\begin{pmatrix}2&1\\3&2\end{pmatrix},
\qquad
S=D^{-1}=\begin{pmatrix}2&-1\\-3&2\end{pmatrix},\\
I_{D,0}&=\frac{(-i)^2}{2}
 (-2D_{11}D_{22}+2D_{12}D_{21})=\det D=1.
\end{aligned}
\tag{43.40}
$$

先在零源处展开$e^{i(-\bar\psi D\psi+\bar\eta\psi+\bar\psi\eta)}$，并提取最高场项；此时只有二次幂留下四份场。将各项中的$\psi$移过后面的$\bar\psi$，两个对角乘积各变号一次，两个交叉乘积还需交换同类指标，便得到式[（43.40）](#eq:c43-finite-dirac-input)的零源系数。然后保留外源，将完整积分除以这个零源值，得到
<span id="eq:c43-finite-dirac-polynomial"></span>

$$
\begin{aligned}
Z_{0,D}
&=1+i\bigl(
 2\bar\eta_1\eta_1-\bar\eta_1\eta_2
 -3\bar\eta_2\eta_1+2\bar\eta_2\eta_2\bigr)\\
&\quad+\bar\eta_1\bar\eta_2\eta_1\eta_2 .
\end{aligned}
\tag{43.41}
$$

四源项的系数也可从式[（43.22）](#eq:c43-dirac-quartic-coefficient)读出，为$S_{11}S_{22}-S_{12}S_{21}=4-3=1$。按交替场链的次序求源导数，便得到四点函数$-1$。若改为直接插入，先将$\psi_1\bar\psi_1\psi_2\bar\psi_2
=-\bar\psi_1\bar\psi_2\psi_1\psi_2$排成规范次序；它已含全部积分变量，因此指数只贡献常数项，直接积分同样给出$-1$。

马约拉纳例子则选取反对称核及其逆为
<span id="eq:c43-finite-majorana-input"></span>

$$
M=\begin{pmatrix}
0&2&1&-1\\
-2&0&3&2\\
-1&-3&0&4\\
1&-2&-4&0
\end{pmatrix},
\qquad
F=M^{-1}=\frac13
\begin{pmatrix}
0&-4&2&-3\\
4&0&1&1\\
-2&-1&0&-2\\
3&-1&2&0
\end{pmatrix}.
\tag{43.42}
$$

先求零源积分。指数的最高项系数为$-(M_{12}M_{34}-M_{13}M_{24}+M_{14}M_{23})
=-(8-2-3)=-3$；这个常数包含既定积分排列的符号以及$(-i)^2$，归一时须将它除去。将带源项一并展开后，完整源多项式为
<span id="eq:c43-finite-majorana-polynomial"></span>

$$
\begin{aligned}
Z_{0,M}
&=1+\frac i3\bigl(
4\eta_1\eta_2-2\eta_1\eta_3+3\eta_1\eta_4
-\eta_2\eta_3-\eta_2\eta_4+2\eta_3\eta_4\bigr)\\
&\quad-\frac13\eta_1\eta_2\eta_3\eta_4 .
\end{aligned}
\tag{43.43}
$$

直接插入$\psi_1\psi_2\psi_3\psi_4$时，分子积分为一，除以零源积分$-3$便得到四点函数$-1/3$。另一方面，式[（43.38）](#eq:c43-majorana-four-point)给出$F_{12}F_{34}-F_{13}F_{24}+F_{14}F_{23}=1/3$，再除以$i^2=-1$就得到同一结果。这个例子显示，零源积分本身虽带有与排列有关的常数，归一后的源微分仍产生相应的场插入。

这些有限模式例子把归一、场插入和配对都落实为多项式的系数提取。[下一节](/posts/srednicki-44/#c44)将进一步说明格拉斯曼积分的换元规则，并由有限高斯积分建立费米路径积分。

---

[← 第 42 节](/posts/srednicki-42/) · [章节地图](/srednicki/) · [第 44 节 →](/posts/srednicki-44/)
