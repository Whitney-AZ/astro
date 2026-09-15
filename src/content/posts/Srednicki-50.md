---
title: 'Srednicki §50 无质量粒子与旋量螺旋度'
date: 2026-09-14
category: 笔记
tags: [物理, 量子场论, Srednicki]
series: 'Srednicki QFT'
srednickiSections: [50]
hideFromHome: true
draft: false
---

<span id="c50"></span>

在第48节计算截面时，我们先对外旋量求和，把振幅平方化为gamma矩阵的迹，
最后再取高能极限。所得结果比计算过程简单得多。
如果一开始就把质量设为零，就有希望同时简化计算过程。
第38节的螺旋度投影已经提供了线索：在外尔表示中，无质量外旋量只有两个非零分量。
我们将利用这个性质，直接化简尚未平方的固定螺旋度振幅。
由此得到的方法称为旋量螺旋度方法（spinor-helicity method）。
本节先考虑费米子与标量的散射；[第60节](/posts/srednicki-60/#c60)将把它用于自旋一粒子。

以下取$p^\mu=(\omega,\mathbf p)$，其中$\omega=|\mathbf p|>0$。
将无质量结果用于有质量理论的高能近似时，
须使各个相关曼德尔斯塔姆变量的绝对值远大于质量平方。
固定角散射满足这一要求；若某个方向使内线分母变小，原来略去的质量项
便可能重新起作用。我们将在最后的角分布中看到这个区别。

<span id="c50-helicity"></span>

## 螺旋度投影与二分量旋量

仍用$\sigma=\pm1$表示螺旋度$h=\sigma/2$。
为了保留每种螺旋度的信息，我们从单个外旋量的投影矩阵出发。
[第38节的无质量极限](/posts/srednicki-38/#c38-helicity)给出
<span id="eq:c50-helicity-projectors"></span>

$$
\begin{aligned}
u_\sigma(p)\bar u_\sigma(p)
&=\frac12(1+\sigma\gamma_5)(-\slashed p),\\
v_\sigma(p)\bar v_\sigma(p)
&=\frac12(1-\sigma\gamma_5)(-\slashed p).
\end{aligned}
\tag{50.1}
$$

粒子旋量$u_\sigma$的手征为$\sigma$，反粒子旋量$v_\sigma$则处在相反的手征块。
比较两式可知，$v_\sigma$与$u_{-\sigma}$只差一个相位；
沿第38节的选择可令这个相位为一，因此只需构造两种$u$旋量。
先选负螺旋度，$\gamma_5u_-=-u_-$。
为把投影式写成二分量形式，引入动量矩阵
<span id="eq:c50-momentum-indices"></span>

$$
\begin{aligned}
p_{a\dot a}&=p_\mu\sigma^\mu_{a\dot a},\\
p^{\dot a a}
&=\varepsilon^{ac}\varepsilon^{\dot a\dot c}p_{c\dot c}
=p_\mu\bar\sigma^{\mu\dot a a}.
\end{aligned}
\tag{50.2}
$$

沿既有约定，$\sigma^\mu=(I,\boldsymbol\sigma)$、
$\bar\sigma^\mu=(I,-\boldsymbol\sigma)$，且
$\gamma^\mu=\left(\begin{smallmatrix}0&\sigma^\mu\\
\bar\sigma^\mu&0\end{smallmatrix}\right)$、
$P_L=(1-\gamma_5)/2=\operatorname{diag}(I_2,0)$。
投影矩阵只留下上面两行，因而
<span id="eq:c50-negative-projector-block"></span>

$$
u_-\bar u_-=P_L(-\slashed p)
=\begin{pmatrix}0&-p_{a\dot a}\\0&0\end{pmatrix}.
\tag{50.3}
$$

$u_-$的下半列为零，便可用一列二分量旋量$\phi_a$表示它。
取狄拉克共轭时还要乘$\beta=\gamma^0$，非零的块随之移到右边：
<span id="eq:c50-negative-spinor"></span>

$$
u_-(p)=\begin{pmatrix}\phi_a\\0\end{pmatrix},\qquad
\bar u_-(p)=\begin{pmatrix}0&\phi^*_{\dot a}\end{pmatrix},
\qquad \phi^*_{\dot a}=(\phi_a)^*.
\tag{50.4}
$$

$\phi_a$的分量是彼此对易的普通复数，本节把这样的动量旋量称为扭量（twistor）。
其归一直接继承自外态：$u_-^\dagger u_-=2\omega$给出
$\phi^\dagger\phi=2\omega$，所以$[\phi]=1/2$。
现在将上式的列与行相乘，唯一的非零块为$\phi_a\phi^*_{\dot a}$。
再与式[（50.3）](#eq:c50-negative-projector-block)比较，便得到本节最基本的关系
<span id="eq:c50-momentum-factorization"></span>

$$
p_{a\dot a}=-\phi_a\phi^*_{\dot a}.
\tag{50.5}
$$

这个外积把四动量分解成一列旋量与其共轭行的乘积。
因此，$\phi$不仅给出外腿的自旋波函数，也包含了它的动量。
先求出$\phi$，就可以同时用它表示外旋量和振幅中出现的动量矩阵。

<span id="c50-explicit"></span>

## 显式角度公式及另一种螺旋度

先把这列旋量具体求出来。将三动量方向写成
$\hat{\mathbf p}=(\sin\theta\cos\phi_{\rm az},
\sin\theta\sin\phi_{\rm az},\cos\theta)$；
$\phi_{\rm az}$是方位角，用下标与旋量$\phi_a$区分。
无质量狄拉克方程$\slashed p\,u_-=0$的下半块给出
$(I+\hat{\mathbf p}\cdot\boldsymbol\sigma)\phi=0$。
它的第一行是
<span id="eq:c50-helicity-eigenvector"></span>

$$
(1+\cos\theta)\phi_1
+\sin\theta\,e^{-i\phi_{\rm az}}\phi_2=0.
\tag{50.6}
$$

当$\theta\ne\pi$时，
$\phi_1=-e^{-i\phi_{\rm az}}\tan(\theta/2)\phi_2$。
取$\phi_2$为非负实数，再使用$\phi^\dagger\phi=2\omega$，
便得到显式表达式
<span id="eq:c50-explicit-phi"></span>

$$
\phi(p)=\sqrt{2\omega}
\begin{pmatrix}
-\sin(\theta/2)e^{-i\phi_{\rm az}}\\
 \cos(\theta/2)
\end{pmatrix}.
\tag{50.7}
$$

代入第二行方程，再用$\sin\theta=2\sin(\theta/2)\cos(\theta/2)$，
也得到零，因此两个分量方程相容。
[下文](#c50-ex-2)将直接计算外积，并从有质量旋量的推动公式求出$\theta=0$的极限。
接着求另一种螺旋度。这里要用到升指标矩阵
<span id="eq:c50-index-raising"></span>

$$
U=(\varepsilon^{ab})
=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\qquad
\binom{\phi^1}{\phi^2}=U\binom{\phi_1}{\phi_2},\qquad
\binom{\phi^{*\dot1}}{\phi^{*\dot2}}
=U\binom{\phi^*_{\dot1}}{\phi^*_{\dot2}}.
\tag{50.8}
$$

由电荷共轭关系取$u_+=\mathcal C\bar u_-^T$，其非零块为$U\phi^*$。
于是两种螺旋度可以由同一列$\phi$表示：
<span id="eq:c50-positive-spinor"></span>

$$
\begin{aligned}
u_+(p)
&=\begin{pmatrix}0\\\phi^{*\dot a}\end{pmatrix}
=\sqrt{2\omega}
\begin{pmatrix}
0\\0\\
\cos(\theta/2)\\
\sin(\theta/2)e^{i\phi_{\rm az}}
\end{pmatrix},\\
\bar u_+(p)&=\begin{pmatrix}\phi^a&0\end{pmatrix}.
\end{aligned}
\tag{50.9}
$$

最后一行中的$\phi^a$按行排列，即$(U\phi)^T=\phi^TU^T$；
直接将$u_+$取厄米共轭再乘$\beta$，也会得到这行旋量。
再作一次电荷共轭，有$\mathcal C\bar u_+^T=u_-$，
因而两种选择确实同时满足$v_-=u_+$、$v_+=u_-$，且归一均为$2\omega$。
它们应当描述同一个动量。为此计算正螺旋度的外积：
<span id="eq:c50-raised-factorization"></span>

$$
\begin{aligned}
u_+\bar u_+
&=\begin{pmatrix}0&0\\
 \phi^{*\dot a}\phi^a&0\end{pmatrix},\\
p^{\dot a a}&=-\phi^{*\dot a}\phi^a .
\end{aligned}
\tag{50.10}
$$

非零块移到了左下，正好是$\frac12(1+\gamma_5)(-\slashed p)$。
要看清这个比较中的指标次序，可把$p_{a\dot a}$记成矩阵$P$。
升指标后的$p^{\dot a a}$以点指标为行，故其矩阵为$UP^TU^T$：
两个$U$分别升起两个指标，而转置把点指标移到前面。
上下两个块由此给出同一个四动量的两种表示。

<span id="c50-rank-one"></span>

## 动量因子分解的唯一性

上面是从已知的外旋量得到动量分解。反过来，给定无质量四动量，
也应该能从动量矩阵找回$\phi$。为说明这一点，将式[（50.2）](#eq:c50-momentum-indices)中的矩阵写开：
<span id="eq:c50-momentum-matrix"></span>

$$
P=p_\mu\sigma^\mu
=\begin{pmatrix}
-p^0+p^3&p^1-ip^2\\
p^1+ip^2&-p^0-p^3
\end{pmatrix}.
\tag{50.11}
$$

实四动量使它为厄米矩阵，其行列式为
<span id="eq:c50-determinant"></span>

$$
\begin{aligned}
\det P
&=(-p^0+p^3)(-p^0-p^3)
 -(p^1-ip^2)(p^1+ip^2)\\
&=(p^0)^2-(p^1)^2-(p^2)^2-(p^3)^2=-p^2 .
\end{aligned}
\tag{50.12}
$$

由于$\hat{\mathbf p}\cdot\boldsymbol\sigma$的本征值为$\pm1$，
对于$p^0=|\mathbf p|=\omega>0$，
$P=-\omega I+\mathbf p\cdot\boldsymbol\sigma$的两个本征值因此是$0,-2\omega$。
若$\chi_-$是非零本征值所属的单位列向量，谱分解给
<span id="eq:c50-spectral-factorization"></span>

$$
P=-2\omega\,\chi_-\chi_-^\dagger
=-\phi\phi^\dagger,\qquad
\phi=\sqrt{2\omega}\,\chi_- .
\tag{50.13}
$$

这样，分解的负号来自负的非零本征值，归一来自它的绝对值。
若另有一列$\psi$满足$P=-\psi\psi^\dagger$，
两个外积的像都是$P$的同一条非零本征直线，故$\psi=c\phi$。
比较迹便得$|c|^2=1$，所以唯一自由度是整体相位。

反过来，给定任意非零复列$\phi$，$-\phi\phi^\dagger$必为秩一负半定矩阵。
用$P=-p^0I+\mathbf p\cdot\boldsymbol\sigma$展开，得到
<span id="eq:c50-recover-momentum"></span>

$$
p^0=\frac12\phi^\dagger\phi>0,\qquad
p^j=-\frac12\phi^\dagger\sigma_j\phi,\qquad p^2=0 .
\tag{50.14}
$$

后一个等式由$\det P=0$保证。
两个复分量包含四个实参数，除去不改变动量的一个相位后，
恰好留下正能无质量壳的三个参数。

能量支在这个结论中起作用。过去指向的$p$使$P$的非零本征值为正，
应写成正的外积，不能仍令$P=-\phi\phi^\dagger$。
$p=0$则对应$\phi=0$，没有可定义的螺旋度方向。
这说明正能条件是分解本身的一部分。[下文](#c50-ex-1)将分别写出两条能量支的完整性关系。

在式[（50.7）](#eq:c50-explicit-phi)的角度公式中，$\theta=0$时相位与方位角无关，
$\theta=\pi$时第一分量却仍含$e^{-i\phi_{\rm az}}$。
若要在南极附近连续选取相位，可改用
$\phi_S=e^{i\phi_{\rm az}}\phi$，
其两分量为$\sqrt{2\omega}(-\sin(\theta/2),
e^{i\phi_{\rm az}}\cos(\theta/2))$。
两个表达在重叠区域相差一个相位，外积仍给出完全相同的$P$。
下面引入的括号会记住这种相位选择，而由它们求出的截面则与选择无关。

<span id="c50-brackets"></span>

## 方括号与尖括号

振幅中的旋量指标最终都要缩并。既然每条外腿已用$\phi$表示，
下一步便是为这些二分量缩并引入简短的记号。
取动量$p,k$所对应的扭量为$\phi,\kappa$，
先定义方括号
<span id="eq:c50-square-bracket"></span>

$$
[p\,k]:=\phi^a\kappa_a
=\phi_2\kappa_1-\phi_1\kappa_2.
\tag{50.15}
$$

交换$\phi,\kappa$时，普通复数分量可以直接换序，
反对称的$\varepsilon$矩阵却给出一个负号。因此
<span id="eq:c50-square-antisymmetry"></span>

$$
[k\,p]=-[p\,k],\qquad [p\,p]=0.
\tag{50.16}
$$

由$\bar u_+=(\phi^a,0)$与$u_-=(\kappa_a,0)^T$可见，
方括号正是四分量乘积$\bar u_+(p)u_-(k)$。
交换两种螺旋度后，乘积将涉及带点的共轭分量；
为此再定义尖括号
<span id="eq:c50-angle-bracket"></span>

$$
\langle p\,k\rangle
:=\phi^*_{\dot a}\kappa^{*\dot a}
=\phi_1^*\kappa_2^*-\phi_2^*\kappa_1^*.
\tag{50.17}
$$

把它与方括号的分量式逐项比较，便有
<span id="eq:c50-conjugate-brackets"></span>

$$
\langle p\,k\rangle=[k\,p]^*=-[p\,k]^*,\qquad
\langle k\,p\rangle=-\langle p\,k\rangle .
\tag{50.18}
$$

共轭关系中反转了方括号的次序，这个约定决定了后面内积公式的符号。
两种括号都是洛伦兹不变的旋量缩并，质量维数均为一。
现在可以把四种标量乘积一起写出：
<span id="eq:c50-four-bilinears"></span>

$$
\begin{aligned}
\bar u_+(p)u_-(k)&=[p\,k],&
\bar u_-(p)u_+(k)&=\langle p\,k\rangle,\\
\bar u_+(p)u_+(k)&=0,&
\bar u_-(p)u_-(k)&=0 .
\end{aligned}
\tag{50.19}
$$

最后两式的行、列各自只占据相反的外尔块，所以相乘为零。
至此，四分量外旋量的标量乘积都已化为括号或零。
不过动量只决定$\phi$到一个相位，因而括号也随这个选择而变。
若重新选取$\phi(p)\mapsto e^{i\alpha_p}\phi(p)$，则
<span id="eq:c50-bracket-phases"></span>

$$
[p\,k]\mapsto e^{i(\alpha_p+\alpha_k)}[p\,k],\qquad
\langle p\,k\rangle\mapsto
e^{-i(\alpha_p+\alpha_k)}\langle p\,k\rangle.
\tag{50.20}
$$

当它们出现在振幅中时，这些因子应当恰好组成外腿的相位。
在求截面之前检查这一点，也可以帮助我们发现括号次序或共轭上的错误。

<span id="c50-dot-product"></span>

## 括号乘积与四动量内积

括号的模应该只由动量决定。将一个尖括号与一个反序方括号相乘，
正好可以重新组合出两个动量矩阵：
<span id="eq:c50-bracket-contraction"></span>

$$
\begin{aligned}
\langle p\,k\rangle[k\,p]
&=(\phi^*_{\dot a}\kappa^{*\dot a})
  (\kappa^a\phi_a)\\
&=(\phi_a\phi^*_{\dot a})
  (\kappa^{*\dot a}\kappa^a)\\
&=p_{a\dot a}k^{\dot a a}
=\operatorname{tr}\!\left[
(p_\mu\sigma^\mu)(k_\nu\bar\sigma^\nu)\right].
\end{aligned}
\tag{50.21}
$$

其中交换的都是普通复数分量。
两个动量分解各带一个负号，相乘后抵消；
第二个矩阵以点指标为行，因而矩阵迹正好完成所需的缩并。
再用$\operatorname{tr}I=2$、
$\operatorname{tr}\sigma_i=0$、
$\operatorname{tr}(\sigma_i\sigma_j)=2\delta_{ij}$展开，便得
<span id="eq:c50-dot-product"></span>

$$
\begin{aligned}
\langle p\,k\rangle[k\,p]
&=\operatorname{tr}
 [(-p^0I+\mathbf p\cdot\boldsymbol\sigma)
  (-k^0I-\mathbf k\cdot\boldsymbol\sigma)]\\
&=2p^0k^0-2\mathbf p\cdot\mathbf k=-2p\cdot k,\\
|[p\,k]|^2=|\langle p\,k\rangle|^2
&=-2p\cdot k
=2\omega_p\omega_k(1-\cos\theta_{pk}).
\end{aligned}
\tag{50.22}
$$

最后一行还用了$\langle p\,k\rangle=[k\,p]^*$。
正能类光四动量的内积非正，因此右边确为非负。
两括号在动量平行时为零；在其他方向，它们的模由能量和夹角决定。
例如让$p$沿正$z$轴，让$k$的极角为$\theta$、方位角为$\phi_{\rm az}$，
将式[（50.7）](#eq:c50-explicit-phi)的两列直接相乘，得到
<span id="eq:c50-simple-brackets"></span>

$$
\begin{aligned}
{}[p\,k]&=-2\sqrt{\omega_p\omega_k}
       \sin\frac\theta2\,e^{-i\phi_{\rm az}},\\
\langle p\,k\rangle&=2\sqrt{\omega_p\omega_k}
       \sin\frac\theta2\,e^{i\phi_{\rm az}} .
\end{aligned}
\tag{50.23}
$$

因子$2$来自两条外腿各自的$\sqrt{2\omega}$归一。
取模平方后，方位角相位消去，再用
$4\sin^2(\theta/2)=2(1-\cos\theta)$就回到式[（50.22）](#eq:c50-dot-product)。
这同时说明括号中哪些信息会留在截面中，哪些只反映外旋量的相位选择。

<span id="c50-amplitude"></span>

## 电子与标量的固定螺旋度振幅

现在把这些关系用于散射过程
$e^-(p)\varphi(k)\to e^-(p')\varphi(k')$。
相互作用仍为第45节的$g\varphi\bar\Psi\Psi$，但同时令$m=M=0$。
两幅树图分别交换动量为$p+k$和$p-k'$的费米子。
把顶角和内线因子相乘，得到树级振幅
<span id="eq:c50-massless-tree"></span>

$$
\mathcal T_{\sigma'\sigma}
=g^2\bar u_{\sigma'}(p')
\left[
\frac{-\slashed p-\slashed k}{(p+k)^2-i0}
+\frac{-\slashed p+\slashed k'}{(p-k')^2-i0}
\right]u_\sigma(p).
\tag{50.24}
$$

我们只保留振幅的$g^2$阶，并先取分母不为零的实运动学。
两张图的内动量和相对号已在[第45节](/posts/srednicki-45/#c45-electron-scalar)导出。
要把分子化为括号，先利用右外腿的在壳关系$\slashed p\,u_\sigma(p)=0$。
而$p^2=k^2=k'^2=0$给$(p+k)^2=2p\cdot k$、
$(p-k')^2=-2p\cdot k'$。
第二项的分子与分母同时提出负号，振幅化为
<span id="eq:c50-on-shell-tree"></span>

$$
\mathcal T_{\sigma'\sigma}
=g^2\left[
 \frac{\bar u_{\sigma'}(p')(-\slashed k)u_\sigma(p)}
 {2p\cdot k}
+\frac{\bar u_{\sigma'}(p')(-\slashed k')u_\sigma(p)}
 {2p\cdot k'}
\right].
\tag{50.25}
$$

这样，分子只剩下两个标量的动量。
虽然$k$和$k'$都属于标量外腿，我们仍可为这两个类光动量各选一列二分量旋量。
由前面的动量分解，$-\slashed k$成为
<span id="eq:c50-slash-factorization"></span>

$$
-\slashed k=
\begin{pmatrix}
0&\kappa_a\kappa^*_{\dot a}\\
\kappa^{*\dot a}\kappa^a&0
\end{pmatrix}.
\tag{50.26}
$$

对于入、出均为正螺旋度的情形，右列$u_+(p)$在下块，
左行$\bar u_+(p')$在上块，因而选出右上块：
<span id="eq:c50-slash-bilinears"></span>

$$
\begin{aligned}
\bar u_+(p')(-\slashed k)u_+(p)
&=\phi'{}^a\kappa_a\,
  \kappa^*_{\dot a}\phi^{*\dot a}
=[p'\,k]\langle k\,p\rangle,\\
\bar u_-(p')(-\slashed k)u_-(p)
&=\phi'^*_{\dot a}\kappa^{*\dot a}\,
  \kappa^a\phi_a
=\langle p'\,k\rangle[k\,p].
\end{aligned}
\tag{50.27}
$$

第二行选出左下块，按同样的矩阵次序完成缩并。
若初末螺旋度相反，非零的行、列就会选到$-\slashed k$的对角块，
因而
<span id="eq:c50-flip-zero"></span>

$$
\bar u_+(p')(-\slashed k)u_-(p)
=\bar u_-(p')(-\slashed k)u_+(p)=0.
\tag{50.28}
$$

将$k$换为$k'$，上述四个矩阵元仍按相同方式计算。
现在分子已经是括号乘积，分母的动量内积也可用
式[（50.22）](#eq:c50-dot-product)改写。保留反对称括号的次序，有
<span id="eq:c50-denominator-brackets"></span>

$$
2p\cdot k
=-[p\,k]\langle k\,p\rangle
=-\langle p\,k\rangle[k\,p].
\tag{50.29}
$$

将它分别代入式[（50.27）](#eq:c50-slash-bilinears)，
第一个分式变成$-[p'\,k]/[p\,k]$，
第二个分式变成$-\langle p'\,k\rangle/\langle p\,k\rangle$。
对$k'$重复这一步，便得到固定螺旋度振幅
<span id="eq:c50-helicity-amplitudes"></span>

$$
\begin{aligned}
\mathcal T_{++}
&=-g^2\left(\frac{[p'\,k]}{[p\,k]}
            +\frac{[p'\,k']}{[p\,k']}\right),\\
\mathcal T_{--}
&=-g^2\left(\frac{\langle p'\,k\rangle}{\langle p\,k\rangle}
            +\frac{\langle p'\,k'\rangle}{\langle p\,k'\rangle}\right),\\
\mathcal T_{+-}&=\mathcal T_{-+}=0 .
\end{aligned}
\tag{50.30}
$$

原来的两条gamma链由此变成了两个括号比值，
每项的质量维数为零，符合四维树幅的要求。
对当前相互作用，这两幅图在无质量极限保持电子的螺旋度；
翻转幅消失的原因正是式[（50.26）](#eq:c50-slash-factorization)的块结构。
此外，两种非零幅并不独立。在实正能动量及实$g$下，
尖括号等于反序方括号的共轭，
而一个比值中的两个反序负号抵消，故
$\mathcal T_{--}=\mathcal T_{++}^*$。
各动量旋量重定相时，$k$、$k'$的相位在每个比值中约去，剩下
<span id="eq:c50-amplitude-phases"></span>

$$
\mathcal T_{++}\mapsto
 e^{i(\alpha_{p'}-\alpha_p)}\mathcal T_{++},\qquad
\mathcal T_{--}\mapsto
 e^{-i(\alpha_{p'}-\alpha_p)}\mathcal T_{--}.
\tag{50.31}
$$

它们恰好等于$\bar u_{\sigma'}(p')$与$u_\sigma(p)$带来的相位。
因此用于表示标量动量的辅助旋量相位已经消去，
电子外腿的剩余相位也将在振幅平方中消去。

<span id="c50-cm-example"></span>

## 从螺旋度幅得到高能截面

括号形式已经简化了固定螺旋度幅，但还没有把散射角显式写出来。
下面补算质心系中的角分布，并与第48节的结果比较。
取能量$E>0$，散射平面为$xz$平面：
<span id="eq:c50-cm-momenta"></span>

$$
\begin{aligned}
p&=(E,0,0,E),\qquad k=(E,0,0,-E),\\
p'&=(E,E\sin\theta,0,E\cos\theta),\\
k'&=(E,-E\sin\theta,0,-E\cos\theta),
\end{aligned}
\tag{50.32}
$$

其中$0<\theta<\pi$。令$c=\cos(\theta/2)$、$d=\sin(\theta/2)$，
采用式[（50.7）](#eq:c50-explicit-phi)的相位选择，有
<span id="eq:c50-cm-spinors"></span>

$$
\begin{aligned}
\phi_p&=\sqrt{2E}\binom01,&
\kappa_k&=\sqrt{2E}\binom{-1}0,\\
\phi_{p'}&=\sqrt{2E}\binom{-d}c,&
\kappa_{k'}&=\sqrt{2E}\binom c d .
\end{aligned}
\tag{50.33}
$$

最后一列对应极角$\pi-\theta$、方位角$\pi$；
在负$z$轴的$k$处选方位角为零。
利用$[p\,k]=\phi_{p,2}\kappa_{k,1}-\phi_{p,1}\kappa_{k,2}$，
四个所需括号为
<span id="eq:c50-cm-brackets"></span>

$$
[p\,k]=-2E,\qquad [p'\,k]=-2Ec,\qquad
[p\,k']=2Ec,\qquad [p'\,k']=2E.
\tag{50.34}
$$

于是这个实相位基中的两个非零振幅相同：
<span id="eq:c50-cm-amplitude"></span>

$$
\mathcal T_{++}=\mathcal T_{--}
=-g^2\left(c+\frac1c\right).
\tag{50.35}
$$

初态只有电子的两个螺旋度需要平均，标量没有自旋简并。
对出射电子求和后，
<span id="eq:c50-spin-average"></span>

$$
\begin{aligned}
\left\langle|\mathcal T|^2\right\rangle
&=\frac12\sum_{\sigma,\sigma'}|\mathcal T_{\sigma'\sigma}|^2
=g^4\left(c^2+2+\frac1{c^2}\right)\\
&=g^4\left(2-\frac us-\frac su\right),\\
s&=4E^2,\qquad
t=-4E^2\sin^2\frac\theta2,\qquad
u=-4E^2\cos^2\frac\theta2 .
\end{aligned}
\tag{50.36}
$$

这正是[第48节四阶迹计算的高能结果](/posts/srednicki-48/#c48-scalar-checks)。
两种算法所处理的中间对象很不同，最后却给出同一角度依赖。
再代入第11节的二体通量和相空间，便得到截面。
这里电子与标量可以区分，末态相空间无需再除以相同粒子的阶乘：
<span id="eq:c50-massless-cross-section"></span>

$$
\frac{d\sigma}{d\Omega}
=\frac{g^4}{64\pi^2s}
 \left(2-\frac us-\frac su\right).
\tag{50.37}
$$

$\theta\to\pi$时$u\to0$，交换费米子趋近质量壳，
$1/c$项随之增大。即使总能量很高，小的$|u|$仍会放大质量项的影响。
因而在接近反向的散射中，应从有质量的分母出发再取极限。

下面推导习题50.1–50.5中的括号恒等式。它们把标量乘积、动量分解和矢量流统一写成外旋量的缩并，可直接用于更长的矩阵链。

<span id="c50-ex-1"></span>

## 左矢、右矢与无质量完整性

为四分量旋量的右矢和左矢引入简写：
<span id="eq:c50-ex-bra-ket-definitions"></span>

$$
\begin{aligned}
|p]&=u_-(p)=v_+(p),&
|p\rangle&=u_+(p)=v_-(p),\\
[p|&=\bar u_+(p)=\bar v_-(p),&
\langle p|&=\bar u_-(p)=\bar v_+(p).
\end{aligned}
\tag{50.38}
$$

将$|p]$取狄拉克共轭得到$\langle p|$，
将$|p\rangle$取狄拉克共轭得到$[p|$。
因而记号左右的方括号或尖括号，是按不变缩并来配对的。
由式[（50.19）](#eq:c50-four-bilinears)的四种标量双线性，逐项得到
<span id="eq:c50-ex-overlaps"></span>

$$
\langle k|p\rangle=\langle k\,p\rangle,\qquad
[k|p]=[k\,p],\qquad
\langle k|p]=[k|p\rangle=0.
\tag{50.39}
$$

(a) 两个螺旋度投影之和为单位矩阵，
故式[（50.1）](#eq:c50-helicity-projectors)给
<span id="eq:c50-ex-completeness"></span>

$$
\begin{aligned}
-\slashed p
&=u_+(p)\bar u_+(p)+u_-(p)\bar u_-(p)\\
&=|p\rangle[p|+|p]\langle p|.
\end{aligned}
\tag{50.40}
$$

按外尔块展开，这就是式[（50.26）](#eq:c50-slash-factorization)。
保持上述狄拉克共轭关系时，这个完整性式适用于正能支。
若$p=-q$且$q$正能，则相应恒等式是
<span id="eq:c50-ex-past-momentum"></span>

$$
-\slashed p=\slashed q
=-|q\rangle[q|-|q]\langle q|.
\tag{50.41}
$$

负能量支的外积系数由此变号。

(b) 在两端夹上左矢和右矢，将完整性式的两项分别相乘：
<span id="eq:c50-ex-amplitude-overlaps"></span>

$$
\begin{aligned}
{}[p'|(-\slashed k)|p\rangle
&=[p'|k\rangle[k|p\rangle+[p'|k]\langle k|p\rangle\\
&=[p'\,k]\langle k\,p\rangle,\\
\langle p'|(-\slashed k)|p]
&=\langle p'|k\rangle[k|p]
 +\langle p'|k]\langle k|p]\\
&=\langle p'\,k\rangle[k\,p].
\end{aligned}
\tag{50.42}
$$

第一行的第一项与第二组的第二项由
式[（50.39）](#eq:c50-ex-overlaps)为零。
对$[p'|(-\slashed k)|p]$，
第一项含$[p'|k\rangle=0$、第二项含$\langle k|p]=0$；
对$\langle p'|(-\slashed k)|p\rangle$亦各有一个为零的因子。
因此两个螺旋度翻转元都为零，重得式[（50.27）](#eq:c50-slash-bilinears)与[（50.28）](#eq:c50-flip-zero)。

<span id="c50-ex-2"></span>

## 角度公式的外积与推动极限

(a) 令$d=\sin(\theta/2)$、$c=\cos(\theta/2)$。
式[（50.7）](#eq:c50-explicit-phi)的列给出
<span id="eq:c50-ex-outer-product"></span>

$$
\begin{aligned}
\phi\phi^\dagger
&=2\omega
\begin{pmatrix}
d^2&-dc\,e^{-i\phi_{\rm az}}\\
-dc\,e^{i\phi_{\rm az}}&c^2
\end{pmatrix}\\
&=\omega
\begin{pmatrix}
1-\cos\theta&-\sin\theta\,e^{-i\phi_{\rm az}}\\
-\sin\theta\,e^{i\phi_{\rm az}}&1+\cos\theta
\end{pmatrix}.
\end{aligned}
\tag{50.43}
$$

把$p^0=\omega$、
$p^3=\omega\cos\theta$、
$p^1\mp ip^2=\omega\sin\theta e^{\mp i\phi_{\rm az}}$
代入式[（50.11）](#eq:c50-momentum-matrix)的矩阵，逐元可见它等于$-\phi\phi^\dagger$。
动量的秩一分解由此得到显式验证，其中右上、左下元的相位互为共轭。

(b) 取$\mathbf p=p\,\hat{\mathbf z}$、$p>0$。
沿[第38节的推动](/posts/srednicki-38/#c38-boost)，静止旋量及相应矩阵为
<span id="eq:c50-ex-z-boost"></span>

$$
\begin{aligned}
u_+(0)&=\sqrt m\,(1,0,1,0)^T,&
u_-(0)&=\sqrt m\,(0,1,0,1)^T,\\
D(\eta)&=
\begin{pmatrix}
e^{-\eta\sigma_3/2}&0\\0&e^{+\eta\sigma_3/2}
\end{pmatrix},&
\omega&=m\cosh\eta,\quad p=m\sinh\eta .
\end{aligned}
\tag{50.44}
$$

$\sigma_3$已为对角矩阵，直接相乘得到
<span id="eq:c50-ex-boosted-columns"></span>

$$
\begin{aligned}
u_+(p)&=
\begin{pmatrix}
\sqrt m\,e^{-\eta/2}\\0\\
\sqrt m\,e^{+\eta/2}\\0
\end{pmatrix}
=\begin{pmatrix}
\sqrt{\omega-p}\\0\\\sqrt{\omega+p}\\0
\end{pmatrix},\\
u_-(p)&=
\begin{pmatrix}
0\\\sqrt m\,e^{+\eta/2}\\
0\\\sqrt m\,e^{-\eta/2}
\end{pmatrix}
=\begin{pmatrix}
0\\\sqrt{\omega+p}\\0\\\sqrt{\omega-p}
\end{pmatrix}.
\end{aligned}
\tag{50.45}
$$

等号用$m e^{\pm\eta}=\omega\pm p$。
在固定$p>0$下令$m\to0$，有$\omega\to p$、
$\omega-p=m^2/(\omega+p)\to0$，故
<span id="eq:c50-ex-boost-limit"></span>

$$
u_+(p)\longrightarrow\sqrt{2p}\,(0,0,1,0)^T,\qquad
u_-(p)\longrightarrow\sqrt{2p}\,(0,1,0,0)^T.
\tag{50.46}
$$

式[（50.7）](#eq:c50-explicit-phi)在$\theta=0$时给$\phi=\sqrt{2p}(0,1)^T$，
而$U\phi^*=\sqrt{2p}(1,0)^T$。
分别放入$u_-$的上块与$u_+$的下块，正好得到这两列。
归一也连续地变为$u_\sigma^\dagger u_\sigma=2p$。

<span id="c50-ex-3"></span>

## 斯考滕恒等式

设$\kappa,\rho,\tau$分别属于$q,r,s$，记其共轭列为
$a=\kappa^*$、$b=\rho^*$、$c=\tau^*$。
二分量反对称乘积为
$\langle q\,r\rangle=a_1b_2-a_2b_1$。
考虑列向量
<span id="eq:c50-ex-schouten-vector"></span>

$$
a(b_1c_2-b_2c_1)
+b(c_1a_2-c_2a_1)
+c(a_1b_2-a_2b_1).
\tag{50.47}
$$

它的第一分量展开为
$a_1b_1c_2-a_1b_2c_1+b_1c_1a_2-b_1c_2a_1
+c_1a_1b_2-c_1a_2b_1$，六项两两相消；
第二分量把外面的$1$换为$2$，同样两两相消。
因此式[（50.47）](#eq:c50-ex-schouten-vector)为零列。
对它作用线性映射$x\mapsto\phi_1^*x_2-\phi_2^*x_1$，就得到
<span id="eq:c50-ex-schouten"></span>

$$
\langle p\,q\rangle\langle r\,s\rangle
+\langle p\,r\rangle\langle s\,q\rangle
+\langle p\,s\rangle\langle q\,r\rangle=0 .
\tag{50.48}
$$

三个向量位于二维空间，使其完全反对称组合为零；收缩后便得到这个斯考滕恒等式。这个多项式恒等式在动量共线时也成立。

<span id="c50-ex-4"></span>

## 四括号与手征迹

令$P_L=(1-\gamma_5)/2$。它选出$|p]$，杀掉$|p\rangle$。
连续使用式[（50.40）](#eq:c50-ex-completeness)和零重叠，得到
<span id="eq:c50-ex-rank-one-trace"></span>

$$
\begin{aligned}
P_L(-\slashed p)&=|p]\langle p|,\\
P_L(-\slashed p)(-\slashed q)
 &=|p]\langle p\,q\rangle[q|,\\
P_L(-\slashed p)(-\slashed q)(-\slashed r)
 &=|p]\langle p\,q\rangle[q\,r]\langle r|,\\
P_L(-\slashed p)(-\slashed q)(-\slashed r)(-\slashed s)
 &=|p]\langle p\,q\rangle[q\,r]\langle r\,s\rangle[s|.
\end{aligned}
\tag{50.49}
$$

列行外积满足$\operatorname{tr}(|p][s|)=[s|p]=[s\,p]$，
而四个负号相乘为正。因此四括号乘积可写成
<span id="eq:c50-ex-four-bracket-trace"></span>

$$
\langle p\,q\rangle[q\,r]\langle r\,s\rangle[s\,p]
=\operatorname{tr}(P_L\slashed p\slashed q\slashed r\slashed s).
\tag{50.50}
$$

按第47节已经推导的普通四阶迹和$\gamma_5$四阶迹，展开右边：
<span id="eq:c50-ex-four-bracket-evaluation"></span>

$$
\begin{aligned}
\operatorname{tr}(P_L\slashed p\slashed q\slashed r\slashed s)
={}&2\bigl[
(p\cdot q)(r\cdot s)
-(p\cdot r)(q\cdot s)
+(p\cdot s)(q\cdot r)\bigr]\\
&+2i\epsilon^{\mu\nu\rho\sigma}p_\mu q_\nu r_\rho s_\sigma .
\end{aligned}
\tag{50.51}
$$

这里沿本书$\epsilon^{0123}=+1$。
普通迹乘$1/2$给第一行；
$\operatorname{tr}(\gamma_5\slashed p\slashed q\slashed r\slashed s)
=-4i\epsilon^{\mu\nu\rho\sigma}p_\mu q_\nu r_\rho s_\sigma$
乘$-1/2$给第二行。
缩并中四个动量指标都是下标；改写成上标动量时应同时使用
$\epsilon_{0123}=-1$。

右边一般为复数。取一个具体的非共面正能例子，
<span id="eq:c50-ex-noncoplanar-example"></span>

$$
\begin{aligned}
p&=(5,3,0,4),&q&=(4,0,4,0),\\
r&=(3,-1,2,-2),&s&=(7,6,3,2),
\end{aligned}
\tag{50.52}
$$

这些数以同一能量单位给出，每个四动量都满足无质量条件。
按式[（50.7）](#eq:c50-explicit-phi)选取的旋量为
$\phi_p=(-1,3)^T$、$\phi_q=(2i,2)^T$、
$\phi_r=(1+2i,1)^T$、$\phi_s=(-2+i,3)^T$。
所需六个内积为
$pq=-20$、$pr=-26$、$ps=-9$、
$qr=-4$、$qs=-16$、$rs=-25$。
三个实项的组合为$500-416+36=120$。
四个下标动量按行排列的行列式为
<span id="eq:c50-ex-epsilon-example"></span>

$$
\det\begin{pmatrix}
-5&3&0&4\\-4&0&4&0\\-3&-1&2&-2\\-7&6&3&2
\end{pmatrix}=240 .
\tag{50.53}
$$

旋量一侧给
$\langle p\,q\rangle=-2+6i$、$[q\,r]=2+2i$、
$\langle r\,s\rangle=5-5i$、$[s\,p]=3-3i$，
四个数相乘为$240+480i$；
右边同样为$2(120)+2i(240)$。
这个例子同时保留了普通迹和$\epsilon$迹的贡献。

<span id="c50-ex-5"></span>

## 矢量双线性与费尔兹恒等式

(a) 先求矢量双线性在整链反向及复共轭下的变换。
沿第49节的[整链转置关系](/posts/srednicki-49/#c49-reversal)，
普通外旋量满足

$$
\bar w_1Aw_2=-\overline{w_2^c}
(\mathcal C A^T\mathcal C^{-1})w_1^c .
$$

取$w_1=u_-(p)$、$w_2=u_-(k)$、$A=\gamma^\mu$，
再用$u_-^c=u_+$及
$\mathcal C(\gamma^\mu)^T\mathcal C^{-1}=-\gamma^\mu$，得
<span id="eq:c50-ex-current-reversal"></span>

$$
\langle p|\gamma^\mu|k]
=-\bar u_+(k)(-\gamma^\mu)u_+(p)
=[k|\gamma^\mu|p\rangle .
\tag{50.54}
$$

链反转的负号与gamma变换的负号抵消。
取复共轭时，沿
$\beta(\gamma^\mu)^\dagger\beta=\gamma^\mu$，
<span id="eq:c50-ex-current-conjugate"></span>

$$
\begin{aligned}
(\bar u_-(p)\gamma^\mu u_-(k))^*
&=\bar u_-(k)\,
  \beta(\gamma^\mu)^\dagger\beta\,u_-(p)\\
&=\bar u_-(k)\gamma^\mu u_-(p).
\end{aligned}
\tag{50.55}
$$

在两端动量相同时，按外尔块相乘得
$\langle p|\gamma^\mu|p]=\phi^\dagger\bar\sigma^\mu\phi$。
式[（50.14）](#eq:c50-recover-momentum)分别给它的时间、空间分量：
<span id="eq:c50-ex-current-normalization"></span>

$$
\langle p|\gamma^0|p]=\phi^\dagger\phi=2p^0,\qquad
\langle p|\gamma^j|p]=-\phi^\dagger\sigma_j\phi=2p^j .
\tag{50.56}
$$

因此，矢量流的归一系数为$2$。
若把另一种左矢、右矢配在一起，$\gamma^\mu$把上块列送到下块，
或把下块列送到上块；相应行却仍留在另一块，故
<span id="eq:c50-ex-gamma-zeroes"></span>

$$
\langle p|\gamma^\mu|k\rangle=0,\qquad
[p|\gamma^\mu|k]=0.
\tag{50.57}
$$

(b) 一次gamma乘法交换上下块，偶数次恢复原块、奇数次交换。
具体说，$\langle p|$只占下行、$[p|$只占上行，
$|k\rangle$只占下列、$|k]$只占上列。
令$G_n=\gamma^{\mu_1}\cdots\gamma^{\mu_n}$，便有
<span id="eq:c50-ex-gamma-parity"></span>

$$
\begin{array}{c|cc}
 &\text{必为零的第一种链}&\text{必为零的第二种链}\\ \hline
n\ \text{为奇数}&
 \langle p|G_n|k\rangle &[p|G_n|k]\\
n\ \text{为偶数}&
 \langle p|G_n|k] &[p|G_n|k\rangle
\end{array}
\tag{50.58}
$$

其中$n=0$恰好包括式[（50.39）](#eq:c50-ex-overlaps)的两个零式。
这项判断只用矩阵块结构，任意洛伦兹指标以及它们的线性缩并都适用。

(c) 接下来把矢量流与gamma矩阵的缩并写成外旋量的秩一外积。从二阶矩阵展开可以同时确定系数和次序。
记$p,q$的旋量分别为$\phi,\kappa$，令
$B=\kappa\phi^\dagger$。
$I,\sigma_1,\sigma_2,\sigma_3$构成二阶复矩阵空间的一组基，
它们的迹内积为$\operatorname{tr}(\sigma_i\sigma_j)=2\delta_{ij}$、
$\operatorname{tr}\sigma_i=0$，故
<span id="eq:c50-ex-pauli-completeness"></span>

$$
B=\frac12\left[
 \operatorname{tr}B\,I+\sum_{j=1}^3
 \operatorname{tr}(\sigma_jB)\sigma_j\right].
\tag{50.59}
$$

四个系数可分别通过取迹或乘$\sigma_j$后取迹求出，
这就给出了任意复矩阵$B$的展开。

令$J^\mu=\langle p|\gamma^\mu|q]
=\phi^\dagger\bar\sigma^\mu\kappa$，
则$J^0=\operatorname{tr}B$、
$J^j=-\operatorname{tr}(\sigma_jB)$。
又$\gamma_0=-\gamma^0$、$\gamma_j=\gamma^j$，
所以$-\frac12J^\mu\gamma_\mu$的右上块为
<span id="eq:c50-ex-fierz-upper-block"></span>

$$
\frac12\left[\operatorname{tr}B\,I+
 \sum_j\operatorname{tr}(\sigma_jB)\sigma_j\right]=B,
\tag{50.60}
$$

左下块为
<span id="eq:c50-ex-fierz-lower-block"></span>

$$
\begin{aligned}
\frac12\left[\operatorname{tr}B\,I-
 \sum_j\operatorname{tr}(\sigma_jB)\sigma_j\right]
&=(\operatorname{tr}B)I-B\\
&=UB^TU^T
=(U\phi^*)(U\kappa)^T .
\end{aligned}
\tag{50.61}
$$

中间的二阶矩阵恒等式可逐元检查：
若$B=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)$，
两边都是$\left(\begin{smallmatrix}d&-b\\-c&a\end{smallmatrix}\right)$。
右上块$B$为$|q]\langle p|$的非零块，
左下块为$|p\rangle[q|$的非零块。因此
<span id="eq:c50-ex-fierz-left"></span>

$$
-\frac12\langle p|\gamma^\mu|q]\,\gamma_\mu
=|q]\langle p|+|p\rangle[q| .
\tag{50.62}
$$

负号和$1/2$已由度规与泡利迹归一固定。

式[（50.54）](#eq:c50-ex-current-reversal)给$[p|\gamma^\mu|q\rangle=\langle q|\gamma^\mu|p]$。
在刚得到的恒等式中交换$p,q$，便有
<span id="eq:c50-ex-fierz-right"></span>

$$
-\frac12[p|\gamma^\mu|q\rangle\,\gamma_\mu
=|q\rangle[p|+|p]\langle q|.
\tag{50.63}
$$

最后在左边乘$\langle r|$、右边乘$|s]$，则右边第二项为零，
第一项为$\langle r\,q\rangle[p\,s]$。于是
<span id="eq:c50-ex-fierz-two-currents"></span>

$$
\begin{aligned}
-\frac12[p|\gamma^\mu|q\rangle
 \langle r|\gamma_\mu|s]
&=\langle r\,q\rangle[p\,s],\\
[p|\gamma^\mu|q\rangle
 \langle r|\gamma_\mu|s]
&=2[p\,s]\langle q\,r\rangle .
\end{aligned}
\tag{50.64}
$$

最后一步用了尖括号反对称性。
这样，两条矢量流的缩并可直接换成两个标量括号的乘积。

<span id="c50-source-reference"></span>

---

[← 第 49 节](/posts/srednicki-49/) · [章节地图](/srednicki/) · [第 51 节 →](/posts/srednicki-51/)
