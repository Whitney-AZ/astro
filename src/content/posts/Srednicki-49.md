---
title: 'Srednicki §49 马约拉纳场的费曼规则'
date: 2026-09-14
category: 笔记
tags: [物理, 量子场论, Srednicki]
series: 'Srednicki QFT'
srednickiSections: [49]
hideFromHome: true
draft: false
---

<span id="c49"></span>

在第45节的汤川理论中，把狄拉克场换成马约拉纳场，费米粒子便成为自身的反粒子。我们将它的质量记为$m$，用$\nu$表示这个模型中的粒子；它与质量为$M$的实标量的相互作用为
<span id="eq:c49-interaction"></span>

$$
\mathcal L_1=\frac g2\varphi\bar\Psi\Psi
=\frac g2\varphi\Psi^T\mathcal C\Psi .
\tag{49.1}
$$

$g$为实数，在四维无量纲。相互作用中的$1/2$与自由马约拉纳作用量的半因子有相同的起因：原来分别属于场和共轭场的两个费米位置，现在属于同一个场。计算顶角时，两种连接怎样处理，便直接关系到这个因子是否留下。本节只求最低阶树图，把场和参数的$Z$因子取为一；四点振幅从$g^2$开始，所求模平方为$g^4$阶。

粒子和反粒子不再独立，也使外腿的写法多了一种选择。同一个入射马约拉纳粒子既可写成$u$列旋量，也可写成$\bar v$行旋量。两者都来自同一个LSZ外腿，选用哪一种要和整条费米链的指标次序配合。先建立这两种写法的关系，便能把马约拉纳传播子中的电荷共轭矩阵与顶角、外腿中的因子一并消去。

<span id="c49-lsz"></span>

## 两种等价的外腿写法

为同时书写右作用和左作用的狄拉克算符，记
<span id="eq:c49-dirac-operators"></span>

$$
\mathscr D=-i\slashed\partial+m,\qquad
\overleftarrow{\mathscr D}=+i\overleftarrow{\slashed\partial}+m,\qquad
\mathcal C^T=\mathcal C^{-1}=-\mathcal C .
\tag{49.2}
$$

[第41节](/posts/srednicki-41/#c41)已从入出算符之差导出了LSZ外腿公式。在散射矩阵元中选定需要截除的入出腿，并将旁观项另行分离，得到以下外腿替换：
<span id="eq:c49-direct-lsz"></span>

$$
\begin{aligned}
b_\sigma^\dagger(\mathbf p)_{\rm in}
&\longrightarrow-i\int d^4x\,
 e^{ipx}\bar v_\sigma(\mathbf p)\mathscr D\Psi(x),\\
b_{\sigma'}(\mathbf p')_{\rm out}
&\longrightarrow+i\int d^4x\,
 e^{-ip'x}\bar u_{\sigma'}(\mathbf p')\mathscr D\Psi(x).
\end{aligned}
\tag{49.3}
$$

这两个替换截除的是矩阵元中已经选定的外腿，波包极限仍按第41节取。为免与稍后散射运动学的变量混淆，这里把自旋标签写成$\sigma$，将$s$留给曼德尔斯塔姆不变量。要把行外旋量移到场的另一侧，只需转置旋量指标；用到的电荷共轭恒等式为
<span id="eq:c49-transpose-identities"></span>

$$
\bar v^T=-\mathcal C u,\qquad
\bar u^T=-\mathcal C v,\qquad
\mathscr D^T=\mathcal C(+i\slashed\partial+m)\mathcal C^{-1}.
\tag{49.4}
$$

前两式可由$v=\mathcal C\bar u^T$、$u=\mathcal C\bar v^T$直接转写，末式则把$\mathcal C(\gamma^\mu)^T\mathcal C^{-1}=-\gamma^\mu$用于狄拉克算符。转置时，外旋量的分量作为普通复数移过$\Psi$，不产生费米换序号；原来作用于$\Psi$的导数改记为作用于$\Psi^T$的左导数。于是两个被积式分别成为
<span id="eq:c49-transposed-integrands"></span>

$$
\begin{aligned}
\bar v\mathscr D\Psi
&=\Psi^T\mathcal C\overleftarrow{\mathscr D}
   \mathcal C^{-1}\bar v^T
=-\Psi^T\mathcal C\overleftarrow{\mathscr D}u,\\
\bar u\mathscr D\Psi
&=\Psi^T\mathcal C\overleftarrow{\mathscr D}
   \mathcal C^{-1}\bar u^T
=-\Psi^T\mathcal C\overleftarrow{\mathscr D}v.
\end{aligned}
\tag{49.5}
$$

两个被积式都多出一个负号。将它们代回式[（49.3）](#eq:c49-direct-lsz)，便得到同一入出腿的另一种写法：
<span id="eq:c49-transposed-lsz"></span>

$$
\begin{aligned}
b_\sigma^\dagger(\mathbf p)_{\rm in}
&\longrightarrow+i\int d^4x\,
 \Psi^T(x)\mathcal C\overleftarrow{\mathscr D}
 u_\sigma(\mathbf p)e^{ipx},\\
b_{\sigma'}(\mathbf p')_{\rm out}
&\longrightarrow-i\int d^4x\,
 \Psi^T(x)\mathcal C\overleftarrow{\mathscr D}
 v_{\sigma'}(\mathbf p')e^{-ip'x}.
\end{aligned}
\tag{49.6}
$$

这里的左导数始终只作用于左侧的场，转置也只改变旋量指标的排列，因而每式仍只有一个平面波。平面波既可放在$\Psi^T$前，也可放在$v$后；这两个位置对应同一个标量因子。

<span id="c49-vertex"></span>

## 顶角的半因子与开链中的电荷共轭矩阵

两种外腿写法的用途，要放回关联函数中才能看清。马约拉纳条件把$\bar\Psi$表示为$\Psi^T\mathcal C$，因而关联函数可全部用$\Psi$来写。[第42节](/posts/srednicki-42/#c42)给出的两场收缩是
<span id="eq:c49-majorana-contraction"></span>

$$
G_{ab}(x-y):=\langle T\Psi_a(x)\Psi_b(y)\rangle
=\frac1i\bigl[S(x-y)\mathcal C^{-1}\bigr]_{ab}.
\tag{49.7}
$$

传播子末端的电荷共轭逆矩阵将与顶角中的$ig\mathcal C$相配。先确定这个顶角的系数：对局部的两个奇变量位置依次求左导数，有
<span id="eq:c49-two-attachments"></span>

$$
\begin{aligned}
\frac{\partial^L}{\partial\Psi_c}
 \left(\frac12\Psi_a\mathcal C_{ab}\Psi_b\right)
&=\frac12\bigl(\mathcal C_{cb}\Psi_b
              -\Psi_a\mathcal C_{ac}\bigr)
=\mathcal C_{cb}\Psi_b,\\
\frac{\partial^L}{\partial\Psi_d}
\frac{\partial^L}{\partial\Psi_c}
 \left(\frac12\Psi_a\mathcal C_{ab}\Psi_b\right)
&=\mathcal C_{cd}.
\end{aligned}
\tag{49.8}
$$

把两个外端点接到这两个同类场时，交换所接的位置会引入奇变量的换序负号，而$\mathcal C_{dc}=-\mathcal C_{cd}$又给出一个负号。因此两种连接的贡献相加，消去作用量中的$1/2$。再乘上$e^{i\int\mathcal L_1}$产生的$i$并对标量求导，就得到带明确指标次序的顶角$ig\mathcal C_{cd}$。

接着沿一条连续费米链收缩内部指标。传播子和顶角交替排列，两个相邻传播子之间的一次连接已经显示出抵消的方式：
<span id="eq:c49-c-cancellation"></span>

$$
\left(\frac{S_1\mathcal C^{-1}}i\right)
 (ig\mathcal C)
\left(\frac{S_2\mathcal C^{-1}}i\right)
=\frac{ig}{i^2}S_1S_2\mathcal C^{-1}.
\tag{49.9}
$$

同样的乘法可沿链重复。若有$r$个顶角，未截腿的矩阵积便含$(ig)^r i^{-(r+1)}S_1\cdots S_{r+1}\mathcal C^{-1}$：每个内部$\mathcal C^{-1}$都与相邻顶角的$\mathcal C$抵消，最后只剩一个端点$\mathcal C^{-1}$。在这一端选用式[（49.6）](#eq:c49-transposed-lsz)，其中的$\mathcal C$恰好将它消去；另一端则选式[（49.3）](#eq:c49-direct-lsz)。随后利用$\mathscr D S=S\overleftarrow{\mathscr D}=\delta$截去两端传播子，链内留下的顶角与传播子因子就与第45节相同。

能够逐点作这样的配对，是因为这里每个顶角的两条费米腿都属于同一马约拉纳场。若相互作用同时含狄拉克场和马约拉纳场，顶角的两个旋量指标可能属于不同种场，上面的$\mathcal C^{-1}\mathcal C$便未必能逐对配齐。计算混合链时，应按各场的通常规则保留尚未消去的电荷共轭矩阵，继续完成明确的指标收缩。

<span id="c49-rules"></span>

## 给一条费米链选择方向

从上述消去过程可以系统地整理树图规则。每个汤川顶角连着两条费米半线；暂时略去标量线，费米子图中的内部顶点就都是二度，连通部分只能形成路径或闭合圈。树图没有闭合圈，每条路径因而有两个外端点。若外马约拉纳粒子总数为$2n$，它们便分成$n$条连续费米链，奇数条外腿无法由这些顶角构成。画图时先画出这些连续费米链，再按顶角结构补上标量外线和内线，列出所有不等价的连通树。

为把旋量指标按矩阵乘法排列，在每条开链上任选一个连续方向。狄拉克线的方向可由电荷流固定；马约拉纳粒子没有独立的反粒子与之区分，同一条链的两个方向都可以使用。标量线仍按物理动量的入出方向画箭头。费米线箭头若与正能物理动量同向，标记为$+p$；反向则标记为$-p$。具体说，入射腿的箭头若离开顶角，就标$-p$；出射腿的箭头若指入顶角，就标$-p'$。同时反转整条费米链的箭头和动量标签，只改变同一张图的定向，这张图仍只计一次。

把外粒子标签按所有不等价方式分配到树上之后，内线动量由各顶角的四动量守恒确定。剪开任意一条树内线，原图分成两块；该内线携带的就是其中一块全部外动量的有符号总和，因而树图没有独立的圈动量积分。按照选定的箭头，两种LSZ写法给出下列外线因子：

| 物理外腿              | 沿链标出的动量 | 旋量因子                       |
| --------------------- | -------------- | ------------------------------ |
| 入射$\nu(p,\sigma)$   | $+p$           | $u_\sigma(\mathbf p)$          |
| 入射$\nu(p,\sigma)$   | $-p$           | $\bar v_\sigma(\mathbf p)$     |
| 出射$\nu(p',\sigma')$ | $+p'$          | $\bar u_{\sigma'}(\mathbf p')$ |
| 出射$\nu(p',\sigma')$ | $-p'$          | $v_{\sigma'}(\mathbf p')$      |

标量外线给出因子一，顶角和内线则分别给出
<span id="eq:c49-local-rules"></span>

$$
\begin{aligned}
\text{汤川顶角}:&\quad ig,\\
\text{标量内线}:&\quad\frac{-i}{k^2+M^2-i0},\\
\text{费米内线}:&\quad
\frac{-i(-\slashed q+m)}{q^2+m^2-i0}.
\end{aligned}
\tag{49.10}
$$

$k,q$都沿图上选定的箭头取有符号动量。书写链值时，从行旋量一端开始，逆着箭头依次排列传播子与顶角，最后抵达列旋量端。例如一端是出射的$+p'$，另一端是入射的$+p$，中间有两个顶角和动量为$q$的费米内线，矩阵链就是$\bar u'(ig)[-i(-\slashed q+m)/(q^2+m^2-i0)](ig)u$。这个读图次序使每一对相邻旋量指标直接按照矩阵乘法收缩。

还须把各图的费米相对号合在一起。选定一张图的整体号，将其它图一侧的端点排成同样的固定次序，再看另一侧端点的排列：奇排列给一个负号。如果为作比较而反转了一整条费米链，还要再乘一个负号。把所有不等价图按这些相对号相加，所得便是$i\mathcal T$。[第51节](/posts/srednicki-51/#c51)将把圈修正和反项纳入计算。先说明链反转为何引入这个附加号，便能将树图规则用于具体过程。

<span id="c49-reversal"></span>

## 整条链反向为什么带负号

为了用同一个推导处理$u$和$v$两种端点，记普通外旋量$w$的电荷共轭为$w^c=\mathcal C\bar w^T$，于是$\overline{w^c}=w^T\mathcal C$。若$A$为链内的矩阵积，将整个数值双线性转置，得到
<span id="eq:c49-chain-reversal"></span>

$$
\begin{aligned}
\bar w_1 A w_2
&=w_2^T A^T\bar w_1^T\\
&=\overline{w_2^c}\,
 \mathcal C^{-1}A^T\mathcal C^{-1}w_1^c\\
&=-\overline{w_2^c}\,
 \bigl(\mathcal C A^T\mathcal C^{-1}\bigr)w_1^c .
\end{aligned}
\tag{49.11}
$$

最后一步的负号来自$\mathcal C^{-1}=-\mathcal C$。要辨认右边剩下的矩阵，先看转置对传播子分子的作用，再将同样的变换用于整条乘积：
<span id="eq:c49-reversed-propagator"></span>

$$
\begin{aligned}
N(q)&=-\slashed q+m,\\
\mathcal C N(q)^T\mathcal C^{-1}
&=+\slashed q+m=N(-q),\\
\mathcal C(A_1\cdots A_r)^T\mathcal C^{-1}
&=(\mathcal C A_r^T\mathcal C^{-1})
 \cdots(\mathcal C A_1^T\mathcal C^{-1}).
\end{aligned}
\tag{49.12}
$$

传播子分母在$q\mapsto-q$下不变，标量顶角的$ig$也不变；这里作的是转置，所以$i$和$i0$都保持原号。式[（49.11）](#eq:c49-chain-reversal)右边括号内的乘积，因而正是反转整条链并将线上动量标签全部换号后的矩阵链。

两种定向得到的原始链值相差负号，而它们代表同一张图。只要在反转时将图前的费米号也改变一次，两种画法就给出同一振幅。这说明了[定向规则](#c49-rules)中的附加负号，也说明为什么两个定向只应计一次。取$A=1$，上述关系简化为
<span id="eq:c49-antisymmetric-bilinears"></span>

$$
\bar v_1u_2=-\bar v_2u_1,\qquad
\bar u_1v_2=-\bar u_2v_1.
\tag{49.13}
$$

这个最简单的情形也能直接由$\bar v_1u_2=u_1^T\mathcal C u_2$看出：两个普通列旋量交换后，$\mathcal C^T=-\mathcal C$给出负号。它来自电荷共轭矩阵的反对称性，外旋量的复数分量本身仍相互对易。

<span id="c49-decay"></span>

## 一个标量衰变成两个马约拉纳粒子

先把定向规则用于标量衰变。下图显示同一衰变过程的两种费米链定向：

<span id="c49-decay-figure"></span>

![标量衰变的两种等价费米链定向；反向后两个出射动量标签同时换号](/images/srednicki/s49_decay.svg)

无论怎样选费米箭头，两条实线的物理动量都是出射的$p_1',p_2'$。左图从上端$\bar u_1'$逆箭头读到下端$v_2'$，链值为$ig\bar u_1'v_2'$；右图的链值为$ig\bar u_2'v_1'$。由式[（49.13）](#eq:c49-antisymmetric-bilinears)，两者相差负号，再计入整条链反转的负号，右图便恢复左图的结果。

第一图的整体号可以从所选福克态直接确定，同时看清作用量中半因子的消去。取有序末态$|1',2'\rangle=b_1'{}^\dagger b_2'{}^\dagger|0\rangle$，相应的左矢为$\langle0|b_2'b_1'$。在马约拉纳模式展开中，$\bar\Psi$的产生部分是$b_a^\dagger\bar u_a$，$\Psi$的产生部分是$b_b^\dagger v_b$，故相互作用中能产生这两个粒子的部分含有
<span id="eq:c49-pair-creation"></span>

$$
\frac g2\,b_a^\dagger b_b^\dagger
  (\bar u_a v_b)\,
  e^{-i(p_a+p_b)x}\varphi(x).
\tag{49.14}
$$

这里沿用第37节的动量测度与自旋求和，只将需要同末态收缩的算符、旋量和平面波写出。两个产生算符与末态的两种匹配由CAR给出：
<span id="eq:c49-decay-fock-sign"></span>

$$
\begin{aligned}
\langle0|b_2'b_1'b_a^\dagger b_b^\dagger|0\rangle
&=\delta_{1'a}\delta_{2'b}-\delta_{1'b}\delta_{2'a},\\
\frac g2\bigl(\bar u_1'v_2'-\bar u_2'v_1'\bigr)
&=g\bar u_1'v_2'.
\end{aligned}
\tag{49.15}
$$

第二行把这两种匹配的反对称组合化成了同一个双线性。第一行的$\delta$还包括既定的自旋与动量归一因子；它们与模式积分配对后，再提出四动量守恒的$\delta$函数，就得到衰变振幅
<span id="eq:c49-decay-amplitude"></span>

$$
i\mathcal T_{\varphi\to\nu\nu}
=ig\bar u_1'v_2'.
\tag{49.16}
$$

交换两个末粒子时，振幅随有序费米末态一起变号。这个推导也确定了出射端应使用的旋量种类。逆过程的链为$ig\bar v_2'u_1'$，其中$\bar v_2'u_1'$是$\bar u_1'v_2'$的复共轭。两种双线性在自旋基重定相下的变化不同：保持马约拉纳关系而作$u_j'\mapsto e^{i\alpha_j}u_j'$、$v_j'\mapsto e^{-i\alpha_j}v_j'$，式[（49.16）](#eq:c49-decay-amplitude)的双线性获得因子$e^{-i(\alpha_1+\alpha_2)}$，逆过程的双线性则获得$e^{+i(\alpha_1+\alpha_2)}$。因此，外旋量的选用必须与实际入出过程一致，不能用一个固定整体相位代替复共轭。

有了振幅，还可以求这个过程的最低阶宽度。取$M>2m$，衰变在运动学上开放；初态标量无需自旋平均，对两个末态自旋使用完整性关系，得到
<span id="eq:c49-decay-square"></span>

$$
\begin{aligned}
\sum_{\sigma_1',\sigma_2'}|\mathcal T|^2
&=g^2\operatorname{tr}
 \bigl[(-\slashed p_1'+m)(-\slashed p_2'-m)\bigr]\\
&=-4g^2(p_1'p_2')-4g^2m^2\\
&=2g^2(M^2-4m^2).
\end{aligned}
\tag{49.17}
$$

最后一行将总动量条件$(p_1'+p_2')^2=-M^2$写成$(p_1'p_2')=m^2-M^2/2$后代入。接下来按[第11节的衰变公式](/posts/srednicki-11/#c11-decay)积分两体相空间：在母粒子静止系记$\beta_\nu=\sqrt{1-4m^2/M^2}$，两末粒子的动量模为$|\mathbf p'|=M\beta_\nu/2$，相空间积分因此为$|\mathbf p'|/(4\pi M)=\beta_\nu/(8\pi)$。两个末粒子相同，还须除去完整标号相空间的重复计数，于是
<span id="eq:c49-decay-width"></span>

$$
\begin{aligned}
\Gamma_{\varphi\to\nu\nu}
&=\frac1{2M}\frac1{2!}\,
 2g^2(M^2-4m^2)\frac{\beta_\nu}{8\pi}\\
&=\frac{g^2M}{16\pi}\,\beta_\nu^3 .
\end{aligned}
\tag{49.18}
$$

宽度中一个$\beta_\nu$来自相空间，另外两个来自标量双线性在阈值处的零点。若以相同顶角强度产生狄拉克粒子反粒子对，自旋总和相同，但可区分的末态不再带这个相空间半因子，宽度便加倍。这里所得$\Gamma$即[第25节](/posts/srednicki-25/#c25)微扰共振宽度的最低阶值。

<span id="c49-two-fermions"></span>

## 只有一条开费米链的散射

衰变例说明，只要过程只有两个外马约拉纳粒子，两种箭头选择就始终围绕同一条开链。因此可以把$\nu\varphi\to\nu\varphi$和$\nu\nu\to\varphi\varphi$同第45节的相应狄拉克树幅联系起来：每个顶角的$1/2$已被局部的两种连接消去，整条链反向又不构成新图；在两种理论中以$ig$表示有效顶角，留下的矩阵链便相同。

具体考察$\nu(p)\varphi(k)\to\nu(p')\varphi(k')$，沿用$s=-(p+k)^2$、$u=-(p-k')^2$。将[第45节的两个内动量](/posts/srednicki-45/#c45-electron-scalar)写成$q_s=p+k$、$q_u=p-k'$，两张图相加给出
<span id="eq:c49-neutrino-scalar"></span>

$$
\begin{aligned}
\mathcal T_{\nu\varphi}
=g^2\bar u'\bigg[
 \frac{N(p+k)}{m^2-s-i0}
+\frac{N(p-k')}{m^2-u-i0}
\bigg]u .
\end{aligned}
\tag{49.19}
$$

用右端外旋量的在壳方程$(\slashed p+m)u=0$，两个分子依次约化为$-\slashed k+2m$、$\slashed k'+2m$，从而得到式[（48.24）](/posts/srednicki-48/#eq:c48-scalar-matrix)中相同的$A$。初态也只有一个费米粒子，自旋平均同为$1/2$，所以第48节算出的四个多项式及截面可直接用于此处。含外标量的弹性过程，仍取此前说明的稳定质量区间。

再看$\nu(p_1)\nu(p_2)\to\varphi(k_1)\varphi(k_2)$。定义$t=-(p_1-k_1)^2$、$u=-(p_1-k_2)^2$，并固定有序入态$b_1^\dagger b_2^\dagger|0\rangle$；把第二个入射端写成$\bar v_2$，即可沿链读取两个标量的两种连接次序：
<span id="eq:c49-neutrino-annihilation"></span>

$$
\mathcal T_{\nu\nu\to\varphi\varphi}
=g^2\bar v_2\bigg[
 \frac{N(p_1-k_1)}{m^2-t-i0}
+\frac{N(p_1-k_2)}{m^2-u-i0}
\bigg]u_1 .
\tag{49.20}
$$

交换两个标量只会交换方括号中的两项，因而振幅具有所需的末态对称性。要比较交换两个入射费米粒子后的结果，则先用式[（49.11）](#eq:c49-chain-reversal)把链转回原来的方向，再将动量守恒写成$-(p_2-k_1)=p_1-k_2$、$-(p_2-k_2)=p_1-k_1$。这样，两项的分子、分母交换位置，链反转的总负号留下，正好给出入态的反对称性。

对于两束独立未极化 $\nu$，初态平均为 $1/4$，相同末标量的相空间带 $1/2!$。可以从[第48节的电子标量结果](/posts/srednicki-48/#c48-scalar-checks)作交叉变换得到这里的平均模平方。记原结果为 $F(s,t,u)$，作代换

$$
p\mapsto p_1,\quad p'\mapsto-p_2,\quad
k\mapsto-k_1,\quad k'\mapsto k_2,
\qquad(s,t,u)\mapsto(t,s,u).
$$

出射电子的完整性核随之变成 $-\slashed p'+m\mapsto\slashed p_2+m=-(-\slashed p_2-m)$，比入射反粒子的核多一个负号。初态自旋平均又从 $1/2$ 变为 $1/4$，因此

$$
\langle|\mathcal T_{\nu\nu\to\varphi\varphi}|^2\rangle
=-\frac12 F(t,s,u).
$$

末态的 $1/2!$ 在对两个标量的有序相空间作全域积分时另行计入。

<span id="c49-four-fermions"></span>

## 四个马约拉纳外腿的三种配对

外费米粒子增加到四个以后，就有了相应狄拉克过程没有的配对。考虑$\nu\nu\to\nu\nu$，固定入态$b_1^\dagger b_2^\dagger|0\rangle$与末态$b_1'{}^\dagger b_2'{}^\dagger|0\rangle$，并定义
<span id="eq:c49-four-kinematics"></span>

$$
\begin{aligned}
s&=-(p_1+p_2)^2,&
t&=-(p_1-p_1')^2,&
u&=-(p_1-p_2')^2,\\
s+t+u&=4m^2.&
\end{aligned}
\tag{49.21}
$$

将四个外端点配成两条费米链，只有三种方式：每个入射粒子与编号相同的末粒子相连，两个末粒子的连接互换，或把两个入射端接成一条链、两个出射端接成另一条链。这三种方式的两顶角间分别交换$t,u,s$动量的标量，如下图所示：

<span id="c49-scattering-figure"></span>

![马约拉纳四粒子散射的t、u、s三道图，相对号依次为正、负、正](/images/srednicki/s49_scattering.svg)

三条虚线的动量都按向下方向标出。右图尤能说明费米箭头与物理入出方向的区别：上方两个端点都是入射，下方两个端点都是出射；标签$-p_2$和$-p_2'$的负号，使上下两条费米链可以同时从左向右定向。沿各条链读取外旋量，记三个乘积为
<span id="eq:c49-three-chains"></span>

$$
\begin{aligned}
D_t&=(\bar u_1'u_1)(\bar u_2'u_2),\\
D_u&=(\bar u_2'u_1)(\bar u_1'u_2),\\
D_s&=(\bar v_2u_1)(\bar u_1'v_2'),\qquad
d_x=M^2-x .
\end{aligned}
\tag{49.22}
$$

把第一图的号固定为正，第二图只交换两个末端，故带相对负号。第三图连接了两入射端和两出射端，比较时需先把第一图的下链反向：
<span id="eq:c49-s-channel-sign"></span>

$$
D_t=-(\bar u_1'u_1)(\bar v_2v_2').
\tag{49.23}
$$

反向后，两链的行端依次为$\bar u_1',\bar v_2$，列端依次为$u_1,v_2'$。固定行端的次序，再交换两个列端，所得乘积就是$(\bar u_1'v_2')(\bar v_2u_1)=D_s$。这一次端点奇排列又带来一个负号，与链反转的负号相乘，便使第三图相对于原第一图取正号。

每图都有两个顶角和一个标量内线，公共因子为$(ig)^2/i=ig^2$。计入刚确定的三个相对号，树级振幅为
<span id="eq:c49-four-amplitude"></span>

$$
i\mathcal T
=ig^2\left[
 \frac{D_t}{d_t-i0}
-\frac{D_u}{d_u-i0}
+\frac{D_s}{d_s-i0}
\right].
\tag{49.24}
$$

其中$t,u$图也出现在两个狄拉克电子的散射中；马约拉纳粒子还可与同类粒子湮灭，因而多出$s$图。这个新配对与外态的费米反对称性相容：交换任一对相同外粒子时，$D_t,D_u$互换，$D_s$按式[（49.13）](#eq:c49-antisymmetric-bilinears)变号，$t,u$两个分母也同时互换，完整振幅便整体变号。

<span id="c49-spin-square"></span>

## 三个平方项与三个干涉项

求平均模平方时，大部分迹仍可借用第48节的结果，新增的工作是把同一自旋标签下出现的两类旋量先化成通常的完整性核。特别是这种混合收缩带来的负号，要与振幅本身的三道相对号分别保留。以下取实$g$，并在远离内部标量极点的树级运动学中计算，使$d_s,d_t,d_u$可取为实数。为整理各道的乘积，记
<span id="eq:c49-spin-kernels"></span>

$$
U_i=-\slashed p_i+m,\qquad
W_i=-\slashed p_i-m,\qquad
K_{xy}:=\frac14\sum_{\rm spins}D_xD_y^* .
\tag{49.25}
$$

带撇号的量按同样方式定义，$1/4$来自两束未极化入射粒子的平均。对角项中的两条费米链可以分别求和，各自闭合成一个二因子迹，故三个对角核为
<span id="eq:c49-diagonal-kernels"></span>

$$
\begin{aligned}
K_{tt}
&=\frac14\operatorname{tr}(U_1U_1')
             \operatorname{tr}(U_2U_2')=(t-4m^2)^2,\\
K_{uu}
&=\frac14\operatorname{tr}(U_1U_2')
             \operatorname{tr}(U_2U_1')=(u-4m^2)^2,\\
K_{ss}
&=\frac14\operatorname{tr}(U_1W_2)
             \operatorname{tr}(U_1'W_2')=(s-4m^2)^2 .
\end{aligned}
\tag{49.26}
$$

例如$\operatorname{tr}(U_1U_1')=-4(p_1p_1')+4m^2
=2(4m^2-t)$，另一个迹相同，两者相乘再乘初态平均因子，便得到第一行；湮灭道中相应的迹为$\operatorname{tr}(U_1W_2)=-4(p_1p_2)-4m^2=2(s-4m^2)$。所用的内积替换与[第48节两个平方项](/posts/srednicki-48/#c48-pair-squares)相同，只是外腿标签作了相应改变。

干涉项把不同的配对接在一起。其中$t$与$s$的乘积同时出现$u_2$和$v_2$，不能立即合成通常的同类完整性核。先把$v_2=\mathcal C\bar u_2^T$代入并对这个自旋求和，就有
<span id="eq:c49-mixed-spin-sum"></span>

$$
\begin{aligned}
\sum_{\sigma_2}v_2(\bar u_2'u_2)
&=\mathcal C U_2^T\bar u_2'{}^T\\
&=(\mathcal C U_2^T\mathcal C^{-1})v_2'
=-W_2v_2' .
\end{aligned}
\tag{49.27}
$$

最后一步用的是$\mathcal C U_2^T\mathcal C^{-1}=+\slashed p_2+m=-W_2$，所以比纯$u\bar u$收缩多出一个负号。将它用于两道尚未求和的乘积，可以保留这个号的来源：
<span id="eq:c49-ts-trace"></span>

$$
\begin{aligned}
D_tD_s^*
&=(\bar u_1'u_1)(\bar u_2'u_2)
  (\bar u_1v_2)(\bar v_2'u_1'),\\
\sum_{\sigma_1,\sigma_2}D_tD_s^*
&=-(\bar u_1'U_1W_2v_2')(\bar v_2'u_1'),\\
K_{ts}
&=-\frac14\operatorname{tr}(U_1W_2W_2'U_1').
\end{aligned}
\tag{49.28}
$$

先用$u_1\bar u_1$的求和生成$U_1$，再用式[（49.27）](#eq:c49-mixed-spin-sum)处理混合端点；剩下两次求和依次生成$W_2'$和$U_1'$，于是全部指标闭合成最后一行的迹。这个矩阵顺序正好与式[（48.7）](/posts/srednicki-48/#eq:c48-pair-average-traces)中的一个干涉迹一致。第48节已将该迹逐项展开，除以四后为$-st/2+2m^2u$；连同这里混合求和留下的负号，便得
<span id="eq:c49-ts-kernel"></span>

$$
K_{ts}=K_{st}=\frac{st}{2}-2m^2u .
\tag{49.29}
$$

因此，借用电子正电子的干涉迹时，须同时带入刚才混合自旋求和的负号。再看$t$与$u$的干涉，两道都只含$u$旋量，收缩次序与[第48节的两电子散射](/posts/srednicki-48/#c48-crossed-electrons)相同。令$r=m^2$，将第48节的内积表代入四因子迹，展开为
<span id="eq:c49-tu-kernel"></span>

$$
\begin{aligned}
K_{tu}
&=\frac14\operatorname{tr}(U_1U_2'U_2U_1')\\
&=\left(\frac u2-r\right)^2
 -\left(r-\frac s2\right)^2
 +\left(\frac t2-r\right)^2\\
&\quad-r(-s+t+u-2r)+r^2\\
&=-\frac{tu}{2}+2rs=K_{ut}.
\end{aligned}
\tag{49.30}
$$

六个二gamma项留下的质量因子都是$+m^2$，其迹合成第三行的线性组合；再用$t+u=4r-s$收集各项，三个平方项合为$r^2-tu/2$，其余部分合为$2rs-r^2$，就得到最后一行。

至此只剩$u,s$干涉。它可以用已经建立的末态反对称性求出，无须另展开一个四因子迹。交换$1'\leftrightarrow2'$，原来的$D_t\mapsto D_u$，同时$D_s\mapsto-D_s$且$t\leftrightarrow u$；自旋求和的四个标签只作重命名，平均因子保持不变。因此
<span id="eq:c49-us-kernel"></span>

$$
K_{us}=-K_{ts}\big|_{t\leftrightarrow u}
=-\frac{us}{2}+2m^2t=K_{su}.
\tag{49.31}
$$

这些核都是实数，而反向干涉核是其复共轭，三个对角项和三对干涉因而已经包含平方展开的九项。最后把振幅中的$+,-,+$系数同各核相乘，得到
<span id="eq:c49-square-structure"></span>

$$
\begin{aligned}
\langle|\mathcal T|^2\rangle=g^4\bigg[
&\frac{K_{tt}}{d_t^2}+\frac{K_{uu}}{d_u^2}
 +\frac{K_{ss}}{d_s^2}\\
&-\frac{2K_{tu}}{d_td_u}
 +\frac{2K_{ts}}{d_td_s}
 -\frac{2K_{us}}{d_ud_s}\bigg].
\end{aligned}
\tag{49.32}
$$

将六个核逐一代入，三个干涉项中由配对收缩产生的号与振幅前的号合在一起，便得到完全由不变量表示的结果：
<span id="eq:c49-invariant-square"></span>

$$
\begin{aligned}
\langle|\mathcal T|^2\rangle=g^4\bigg[
&\frac{(s-4m^2)^2}{(M^2-s)^2}
 +\frac{st-4m^2u}{(M^2-s)(M^2-t)}\\
&+\frac{(t-4m^2)^2}{(M^2-t)^2}
 +\frac{tu-4m^2s}{(M^2-t)(M^2-u)}\\
&+\frac{(u-4m^2)^2}{(M^2-u)^2}
 +\frac{us-4m^2t}{(M^2-u)(M^2-s)}
\bigg].
\end{aligned}
\tag{49.33}
$$

三个平方项与三个成对干涉项合在一起，对$s,t,u$的任意置换都对称。相同粒子的$t,u$交换只体现其中一部分：马约拉纳粒子交叉以后仍属同类外腿，三个道因此进入同一个表达式。在具体的弹性质心系中，$s\geq4m^2$而$t,u\leq0$，这些运动学范围仍须分别满足；式中的代数置换对称性不改变各道对应的物理区域。

<span id="c49-cross-section"></span>

## 截面、阈值与无质量极限

得到平均模平方后，按第48节的弹性相空间即可求截面。先以有标签的$p_1'$方向定义角分布，再在积分完整末态时除去两个相同粒子的重复计数：
<span id="eq:c49-cross-section"></span>

$$
\begin{aligned}
\frac{d\sigma_{\rm ord}}{d\Omega_{\rm CM}}
&=\frac{\langle|\mathcal T|^2\rangle}{64\pi^2s},\\
t&=-2q^2(1-\cos\theta),\qquad
u=-2q^2(1+\cos\theta),\qquad q^2=\frac s4-m^2,\\
\sigma&=\frac1{2!}\int d\Omega_{\rm CM}\,
 \frac{d\sigma_{\rm ord}}{d\Omega_{\rm CM}} .
\end{aligned}
\tag{49.34}
$$

由于$t\leftrightarrow u$对应$\theta\leftrightarrow\pi-\theta$，前后两个方向描述的是同一对无序末粒子。最后一行也可改成只在一半末态方向域内积分，并去掉除二的因子。

先看阈值附近。固定$M>0$且$M^2\ne4m^2$，令$s\to4m^2$、$t,u\to0$，各分母在此极限保持非零。$s$道平方以及两个含$s$的干涉项都消失，余下三项为
<span id="eq:c49-threshold"></span>

$$
\langle|\mathcal T|^2\rangle_{\rm threshold}
=\frac{g^4}{M^4}
 \bigl(16m^4+16m^4-16m^4\bigr)
=\frac{16g^4m^4}{M^4}.
\tag{49.35}
$$

静止旋量使这一抵消的意义更直接：$\bar vu=0$令$s$链消失，$t,u$链分别成为$4m^2\delta_{\sigma_1'\sigma_1}
\delta_{\sigma_2'\sigma_2}$及交换末标签后的式子。
它们相减，只留下初末自旋空间的反对称部分，取模平方并作四自旋平均后便得到上述阈值结果。

另一个有用的极限是固定非前向、非后向散射角，使$s,|t|,|u|$都远大于$m^2,M^2$。此时式[（49.33）](#eq:c49-invariant-square)的三个平方项各趋于一，三个干涉项也各趋于一，故
<span id="eq:c49-high-energy"></span>

$$
\begin{aligned}
\langle|\mathcal T|^2\rangle
&=6g^4+g^4\,O\!\left(\frac{m^2+M^2}{s}\right),\\
\frac{d\sigma_{\rm ord}}{d\Omega_{\rm CM}}
&=\frac{3g^4}{32\pi^2s}
 +\frac{g^4}{s}\,O\!\left(\frac{m^2+M^2}{s}\right).
\end{aligned}
\tag{49.36}
$$

固定角度使两个交换道分母与$s$保持同阶，质量修正因而可以按上式展开。在这一极限，不仅振幅的迹表达式简化，外旋量本身也能换用更方便的形式；[下一节](/posts/srednicki-50/#c50)将据此引入无质量粒子的旋量螺旋度方法。

若改在$M>2m$且$s$接近$M^2$的区域，内部标量已进入可衰变共振，须按第25节把自能吸收部纳入传播子。共振附近的三道干涉需使用修正后的复分母。

---

[← 第 48 节](/posts/srednicki-48/) · [章节地图](/srednicki/) · [第 50 节 →](/posts/srednicki-50/)
