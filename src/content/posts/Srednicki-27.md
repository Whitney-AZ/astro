---
title: 'Srednicki §27 其他重整化方案'
date: 2026-09-14
category: 笔记
tags: [物理, 量子场论, Srednicki]
series: 'Srednicki QFT'
srednickiSections: [27]
hideFromHome: true
draft: false
---

<span id="c27"></span>

第26节把未被分辨的粒子配置加在一起以后，截面中仍留下$\ln(s/m^2)$。当$s\gg m^2$时，这个大对数会使高阶圈修正变得重要。要理解它的来源，需要回到质量和耦合的定义：我们过去把$m$定义为传播子的极点质量，并在零动量处规定三点顶角等于$g$。这些条件将参数与低能物理直接联系起来，但用这组参数描述远高于质量的散射时，圈图中就会出现两个能标之比的对数。下面改变反项的有限部分，再通过同一物理量换算两组参数，看看怎样选择更适合高能计算的耦合定义。所需圈积分已在[第14节](/posts/srednicki-14/#c14)和[第16节](/posts/srednicki-16/#c16)求出，以下从这些积分的有限部分开始。

<span id="c27-schemes"></span>

## 从极点条件到最小减除

仍取$d=6-\epsilon$，并用第14节的尺度$\mu^2=4\pi e^{-\gamma}\widetilde\mu^2$。为使两种方案的差别直接显现在反项中，先不指定它们的有限部分。置$z=k^2$、$a=x(1-x)$、$D=m^2+az-i0$，一圈自能写为

<span id="eq:c27-unsubtracted"></span>

$$
\begin{aligned}
\Pi(z)={}&-\left[A+\frac{\alpha}{6}
 \left(\frac1\epsilon+\frac12\right)\right]z
 -\left[B+\alpha\left(\frac1\epsilon+\frac12\right)\right]m^2\\
&+\frac{\alpha}{2}\int_0^1dx\,D\ln\frac D{\mu^2}+O(\alpha^2).
\end{aligned}
\tag{27.1}
$$

反项系数$A$和$B$分别来自$-\tfrac12A(\partial\varphi)^2$及$-\tfrac12Bm^2\varphi^2$，所以它们在$\Pi$中带负号。极点的归一化还取决于自能的斜率。对$z$求导时，积分中的$D$及$\ln D$都要微分，因此得到

<span id="eq:c27-unsubtracted-derivative"></span>

$$
\Pi'(z)=-A-\frac{\alpha}{6}
\left(\frac1\epsilon+\frac12\right)
+\frac{\alpha}{2}\int_0^1dx\,a
\left(\ln\frac D{\mu^2}+1\right)+O(\alpha^2).
\tag{27.2}
$$

这里$\Pi$的质量维数为2，$\Pi'$、$A$、$B$都是无量纲量。两个反项的有限部分分别调整自能的动量项和质量项，用来实现选定的极点位置与场归一化。式中$1/2$来自维数积分的有限展开，与$1/\epsilon$极点应分别保留；改变减除方案所涉及的，正是有限部分怎样分配给反项。

以前采用的极点方案（on-shell scheme，简称OS）要求$\Pi_{\rm OS}(-m^2)=\Pi'_{\rm OS}(-m^2)=0$，分别将参数质量定在物理极点上，并把留数归一为一。用这两个条件确定有限反项后，第14节的结果为

<span id="eq:c27-os-reminder"></span>

$$
\Pi_{\rm OS}(z)=
\frac{\alpha}{2}\int_0^1dx\,D
\ln\frac{D}{m^2(1-a)}
-\frac{\alpha}{12}(z+m^2)+O(\alpha^2).
\tag{27.3}
$$

取$m\to0$而保持类空$z>0$，积分内出现$az\ln(z/m^2)$，表明这组归一化条件在小质量极限变得奇异。传播子的解析结构也说明了困难所在：单粒子极点在$z=-m^2$，两粒子阈值在$z=-4m^2$，它们在$m=0$时相遇。原来用来隔离单粒子态的间隔消失了，因而有质量时的孤立、单位留数极点条件不能直接延续到这里。

重整化仍允许我们在任意非零尺度$\mu$处定义参数。为摆脱有限部分对物理极点的依赖，可以只要求反项消去维数调节中的发散，取

<span id="eq:c27-msbar-counterterms"></span>

$$
A=-\frac{\alpha}{6\epsilon},\qquad
B=-\frac{\alpha}{\epsilon},\qquad
C=-\frac{\alpha}{\epsilon},
\tag{27.4}
$$

这便定义了修正最小减除方案（modified minimal subtraction，$\overline{\mathrm{MS}}$）。这里的$C$用于三点顶角，稍后将与二点函数采用同一减除规定。结合上述尺度定义，式[（27.4）](#eq:c27-msbar-counterterms)消去了维数积分中的极点，以及原始尺度下与极点相伴的$\ln4\pi-\gamma$。

两种最小减除的区别可以通过尺度换算写明。记$p=\ln4\pi-\gamma$；若普通MS在$g_d=g\nu^{\epsilon/2}$下只减$1/\epsilon$，那么在数值相同的$\nu=\mu$处，两种有限核之间有

<span id="eq:c27-ms-scale-conversion"></span>

$$
\begin{aligned}
\Pi_{\rm MS}(z;\nu)&=\Pi_{\overline{\rm MS}}(z;\mu=\nu)
-\frac{\alpha p}{2}\left(m^2+\frac z6\right),\\
\frac{V_{3,\rm MS}}g&=\frac{V_{3,\overline{\rm MS}}}g+\frac{\alpha p}{2}.
\end{aligned}
\tag{27.5}
$$

第一行的差来自$\int D\,dx=m^2+z/6$，第二行则利用了归一化费曼测度$\int dF_3=1$。改取$\nu=\widetilde\mu=\mu e^{-p/2}$后，尺度对数中的常数恰好补偿这两个差，恢复前面采用的有限核。下面统一使用$\overline{\mathrm{MS}}$和$\mu$，这一常数已经包含在尺度定义中。

将式[（27.4）](#eq:c27-msbar-counterterms)代回自能，极点项相消，余下有限部分：

<span id="eq:c27-msbar-self-energy"></span>

$$
\Pi(z)=-\frac{\alpha}{12}(z+6m^2)
+\frac{\alpha}{2}\int_0^1dx\,D\ln\frac D{\mu^2}
+O(\alpha^2).
\tag{27.6}
$$

现在可以直接检查新核的无质量极限。在$m=0$、$z>0$处，对数的尺度由外动量给定；利用$\int_0^1a\,dx=1/6$及$\int_0^1a\ln a\,dx=-5/18$，把尺度对数和参数对数分别积分，得到

<span id="eq:c27-massless-offshell"></span>

$$
\begin{aligned}
\Pi(z)\big|_{m=0}
 &=\frac{\alpha z}{12}\left(\ln\frac z{\mu^2}-\frac83\right),\\
\Pi'(z)\big|_{m=0}
 &=\frac{\alpha}{12}\left(\ln\frac z{\mu^2}-\frac53\right).
\end{aligned}
\tag{27.7}
$$

虽然$z\ln z\to0$，导数仍在$z=0$发散。新方案因此给出了有限的离壳归一化，但要将它用于物理截面，仍需结合上一节对共线粒子配置的处理。下面先保持$m>0$，利用孤立极点确定LSZ的外腿因子，再作高能展开。

<span id="c27-pole-lsz"></span>

## 物理质量和外腿留数

有限反项改动以后，拉格朗日量中的$m$不再直接等于实测质量；物理质量仍由完整传播子的极点定义。把它记为$M=m_{\rm ph}$，极点方程及其附近的传播子便为

<span id="eq:c27-pole-definition"></span>

$$
M^2=m^2-\Pi(-M^2),\qquad
\boldsymbol\Delta(z)=\frac1{z+m^2-\Pi(z)-i0}
\simeq\frac R{z+M^2-i0},
\tag{27.8}
$$

留数由逆传播子在极点附近的一阶系数确定：

<span id="eq:c27-residue-definition"></span>

$$
R^{-1}=1-\Pi'(-M^2).
\tag{27.9}
$$

具体地说，展开分母时先用极点方程消去常数项，余下$(z+M^2)[1-\Pi'(-M^2)]$，所以逆留数中的减号随之确定。这里取的是关于$k^2$的留数；若把传播子看成$k^0$的函数，变量代换还会带来$2\sqrt{\mathbf k^2+M^2}$的雅可比。

谱表示将这个留数与场产生单粒子的振幅联系起来：对归一化单粒子态，有$\langle0|\varphi(0)|\mathbf k\rangle=\sqrt R$。把场改为$\varphi_{\rm OS}=R^{-1/2}\varphi$，这个矩阵元才等于一。因此，LSZ修正同时涉及物理质量和场归一化：约化算符应在质量$M$处截腿，每个场再附加$R^{-1/2}$。将这两个操作施加在同一条完整外传播线上，得到

<span id="eq:c27-lsz-one-leg"></span>

$$
\frac1{\sqrt R}\,i(z+M^2)\,
\frac1i\,\frac R{z+M^2-i0}
\longrightarrow\sqrt R.
\tag{27.10}
$$

由此，有$n$条外腿的物理振幅等于截腿图之和乘$R^{n/2}$。四点振幅含有$R^2$，取模方时相应出现$R^4$。内部自由线仍为$-i/(k^2+m^2-i0)$，其中的质量是组织微扰展开的拉格朗日量参数；外动量则满足$k_i^2=-M^2$，位置空间的约化算符相应为$-\partial^2+M^2$。三价顶角仍为$ig(1+C)$，二价反项仍为$-i(Ak^2+Bm^2)$。这样，内线和顶角继续按所选方案计算，外腿因子则将所得图核连接到归一化的物理粒子态。

接下来求出极点位置。一圈中$M^2-m^2=O(\alpha m^2)$，而$\Pi'=O(\alpha)$，因此可以在自能中围绕参数质量展开：

<span id="eq:c27-pole-order"></span>

$$
\Pi(-M^2)=\Pi(-m^2)-(M^2-m^2)\Pi'(-m^2)+\cdots
=\Pi(-m^2)+O(\alpha^2m^2).
\tag{27.11}
$$

这一截断按$\alpha|\ln(\mu^2/m^2)|\ll1$使用；对数很大时，需要后面给出的跑动解重新组织展开。令$L_\mu=\ln(\mu^2/m^2)$。在$z=-m^2$处，$D_0=m^2(1-a)>0$，因而这里需要的都是阈值下的实积分。[第14节的有限积分](/posts/srednicki-14/#c14-finite-constants)已经给出

<span id="eq:c27-j0-j1"></span>

$$
\begin{aligned}
J_0&=\int_0^1dx\,\ln(1-a)=-2+\frac{\pi}{\sqrt3},\\
J_1&=\int_0^1dx\,a\ln(1-a)=-\frac{17}{18}+\frac{\pi}{2\sqrt3}.
\end{aligned}
\tag{27.12}
$$

质量方程所需的积分带有$(1-a)$权重，因此把这两个已知积分作差，并将尺度对数单独积分，便有

<span id="eq:c27-pole-integral"></span>

$$
\int_0^1dx\,D_0\ln\frac{D_0}{\mu^2}
=m^2\left[-\frac56L_\mu+J_0-J_1\right]
=m^2\left[-\frac56L_\mu-\frac{19}{18}
+\frac{\pi}{2\sqrt3}\right].
\tag{27.13}
$$

将这一积分乘上自能中的系数，再与式[（27.6）](#eq:c27-msbar-self-energy)中的$-5\alpha m^2/12$相加，极点方程化为

<span id="eq:c27-physical-mass"></span>

$$
\begin{gathered}
\Pi(-m^2)=-\frac{5\alpha m^2}{12}(L_\mu+c'),\qquad
c'=\frac{34-3\sqrt3\pi}{15},\\
M^2=m^2\left[1+\frac{5\alpha}{12}(L_\mu+c')\right]+O(\alpha^2m^2).
\end{gathered}
\tag{27.14}
$$

常数$c'$由这些有限积分完全确定；给定减除方案后，它已经没有另行选择的自由。

留数可按同样的步骤求出。在式[（27.2）](#eq:c27-unsubtracted-derivative)中代入$A$后，积分中$+1$所给的贡献与显式$-\alpha/12$相消，剩下的对数积分直接由前面的加权结果计算：

<span id="eq:c27-residue-evaluated"></span>

$$
\begin{aligned}
\Pi'(-m^2)&=\frac{\alpha}{2}
\int_0^1dx\,a\left[-L_\mu+\ln(1-a)\right]
=-\frac{\alpha}{12}L_\mu+\frac{\alpha}{2}J_1,\\
R^{-1}&=1+\frac{\alpha}{12}(L_\mu+c'')+O(\alpha^2),\qquad
c''=-6J_1=\frac{17-3\sqrt3\pi}{3}.
\end{aligned}
\tag{27.15}
$$

这里用$-m^2$代替$-M^2$，所引入的误差仍在二圈阶。两个有限常数$c'$和$c''$分别来自质量条件与留数条件。

<span id="c27-mass-running"></span>

## 质量为什么随尺度变化

现在有了参数质量与物理质量的明确关系。物理质量$M$应当与任意选择的$\mu$无关，因此参数本身的变化必须补偿圈图中显式的尺度变化。对式[（27.14）](#eq:c27-physical-mass)取平方根再取对数，将这一条件写成便于求导的形式：

<span id="eq:c27-log-mass"></span>

$$
\ln M=\ln m+\frac{5\alpha}{12}
\left(\ln\frac\mu m+\frac{c'}2\right)+O(\alpha^2).
\tag{27.16}
$$

为表示质量参数和耦合随尺度的变化，定义

<span id="eq:c27-rg-definitions"></span>

$$
\gamma_m(\alpha)=\frac{d\ln m}{d\ln\mu},\qquad
\beta(\alpha)=\frac{d\alpha}{d\ln\mu},
\tag{27.17}
$$

这两个导数都沿着同一裸理论取值，即改变减除尺度时保持所描述的物理体系不变。因此物理质量关系右边的$m$也随尺度变化，要与显式对数一起微分。保留所需阶数的完整链式法则，得到

<span id="eq:c27-mass-chain-rule"></span>

$$
0=\gamma_m+\frac5{12}\left[
\beta\left(\ln\frac\mu m+\frac{c'}2\right)
+\alpha(1-\gamma_m)\right]+O(\alpha^2).
\tag{27.18}
$$

稍后将从散射率得到$\beta=O(\alpha^2)$，而上式本身给出$\gamma_m=O(\alpha)$。于是括号中的$\beta$项和$\alpha\gamma_m$项都进入下一阶，领先项便化为

<span id="eq:c27-mass-anomalous-dimension"></span>

$$
\gamma_m=-\frac5{12}\alpha+O(\alpha^2).
\tag{27.19}
$$

增大$\mu$时，$m(\mu)$随之下降，正好补偿圈图中对数的变化，使$M$保持不变。这种由量子修正引起的尺度变化称为“反常量纲”（anomalous dimension）；质量原有的质量维数1仍由单位制确定。

<span id="c27-vertex-matching"></span>

## 三点顶角和方案之间的有限换算

质量和场的归一化确定以后，还须用同一方案定义耦合。第16节三角图的归一化测度为$dF_3=2\,dx\,dy\,dw\,\delta(x+y+w-1)$，积分区域是$x,y,w\ge0$。取$D_3=m^2+xyk_1^2+ywk_2^2+wxk_3^2-i0$，并减去$C=-\alpha/\epsilon$，得到有限顶角及其零动量值

<span id="eq:c27-msbar-vertex"></span>

$$
\frac{V_3(k_1,k_2,k_3)}g
=1-\frac{\alpha}{2}\int dF_3\ln\frac{D_3}{\mu^2}+O(\alpha^2),
\qquad
\frac{V_3(0,0,0)}g=1+\frac{\alpha}{2}L_\mu+O(\alpha^2).
\tag{27.20}
$$

三角图的对称因子和参数积分沿用[第16节](/posts/srednicki-16/#c16)的推导，变化只在有限减除。零动量时$D_3=m^2$，对数不再依赖参数，因而第二个结果由$\int dF_3=1$直接得到。

这时可以比较两种方案对同一理论的描述。先将$\overline{\mathrm{MS}}$场写成$\varphi=\sqrt R\,\varphi_{\rm OS}$，使OS场的单粒子重叠归一为一。有效作用量中的每个场因子都带来$\sqrt R$，所以各阶顶角和零动量耦合相应变为

<span id="eq:c27-finite-coupling-conversion"></span>

$$
\begin{aligned}
V_{n,\rm OS}&=R^{n/2}V_n,\\
g_{\rm OS}=V_{3,\rm OS}(0)
&=R^{3/2}V_3(0)
=g\left[1+\frac{3\alpha}{8}L_\mu-\frac{\alpha}{8}c''\right]
+O(g\alpha^2),\\
\alpha_{\rm OS}
&=\alpha\left[1+\frac{3\alpha}{4}L_\mu
-\frac{\alpha}{4}c''\right]+O(\alpha^3).
\end{aligned}
\tag{27.21}
$$

其中$R^{3/2}=1-\alpha(L_\mu+c'')/8+O(\alpha^2)$；其对数项与顶角的$+\alpha L_\mu/2$相加，留下$3\alpha L_\mu/8$。可见场的有限归一化和顶角的有限修正都参与耦合换算，两种方案中同写作$g$的参数一般并不取相同数值。

二点函数也随同一场变换而改变。由$\boldsymbol\Delta_{\rm OS}=R^{-1}\boldsymbol\Delta$可知，逆核应乘$R$。再用$M^2=m^2-\Pi(-m^2)$消去常数项，并保留到一圈，得到

<span id="eq:c27-finite-self-energy-conversion"></span>

$$
\Pi_{\rm OS}(z)=\Pi(z)-\Pi(-m^2)
-(z+m^2)\Pi'(-m^2)+O(\alpha^2).
\tag{27.22}
$$

右边只需使用共同的领先$m,g$，其差异乘上一圈项后属于更高阶；完整OS参数则是$M,g_{\rm OS}$。式中的第二项将极点放在物理质量处，第三项把留数归一为一。代入对数积分，便恢复式[（27.3）](#eq:c27-os-reminder)，从而看出两种二点核怎样通过有限减除相互转换。

同一转换也可从裸量不变直接求出。两种方案都描述相同的裸场、裸质量和裸耦合，因此应固定

<span id="eq:c27-bare-parameters"></span>

$$
\varphi_B=Z_\varphi^{1/2}\varphi,\qquad
m_B^2=\frac{Z_m}{Z_\varphi}m^2,\qquad
g_B=\frac{Z_g}{Z_\varphi^{3/2}}g\widetilde\mu^{\epsilon/2}.
\tag{27.23}
$$

记$\delta A=A_{\rm OS}-A_{\overline{\rm MS}}$，其余反项的差作类似定义。把极点、导数及零动量顶角条件分别施加到新方案的核上，所需的有限反项差为

<span id="eq:c27-finite-counterterms"></span>

$$
\begin{aligned}
\delta A&=-\frac{\alpha}{12}(L_\mu+c''),\\
\delta B&=-\frac{\alpha}{12}(6L_\mu+c''+5c'),\\
\delta C&=-\frac{\alpha}{2}L_\mu.
\end{aligned}
\tag{27.24}
$$

例如，质量条件$0=\Pi(-m^2)+m^2(\delta A-\delta B)$与已求出的场反项差一起给出第二行。裸耦合不变则要求$g_{\rm OS}/g=1-\delta C+\tfrac32\delta A$，代入后得到与式[（27.21）](#eq:c27-finite-coupling-conversion)相同的换算。场和参数必须一起改变，才能使两种图展开对应同一个散射过程。

<span id="c27-inclusive"></span>

## 重新计算高能散射

现在用新参数重做第26节的高能散射，取$s\gg M^2$，并保持$t/s,u/s$远离零。树振幅仍由三条交换道相加得到：

<span id="eq:c27-hard-tree"></span>

$$
\mathcal T_0=-g^2\left(\frac1s+\frac1t+\frac1u\right).
\tag{27.25}
$$

要找出各通道的共同对数，先看任意一条交换道。令交换动量平方为$z$，自能的大$|z|$部分可直接使用式[（27.7）](#eq:c27-massless-offshell)。对于该道的三点顶角，两个外宗量在领先质量阶为零，因此$D_3\simeq xyz$，其中$x,y$是费曼参数。将尺度对数从参数积分中提出后，余下的对数积分可按单纯形几何计算：固定$x$时，剩余积分区间的长度为$1-x$，于是

<span id="eq:c27-hard-triangle-integral"></span>

$$
\int dF_3\ln x=2\int_0^1dx\,(1-x)\ln x
=2\left(-1+\frac14\right)=-\frac32,
\qquad
\int dF_3\ln(xy)=-3.
\tag{27.26}
$$

沿费曼边界从$z-i0$连续取对数，并记$\ell_z=\ln[(z-i0)/\mu^2]$，上述积分便把自能和顶角分别化为

<span id="eq:c27-hard-subgraphs"></span>

$$
\frac{\Pi(z)}z=\frac{\alpha}{12}
\left(\ell_z-\frac83\right),\qquad
\frac{V_3}g=1-\frac{\alpha}{2}(\ell_z-3)
\tag{27.27}
$$

这两式保留到一圈和领先质量阶。每条交换道含有两个三点顶角，传播子则按$\boldsymbol\Delta=z^{-1}(1+\Pi/z+\cdots)$展开。将三处的一圈贡献相加，该道相对于树图的修正为

<span id="eq:c27-hard-eleven"></span>

$$
2\left(\frac{V_3}g-1\right)+\frac{\Pi(z)}z
=-\frac{11\alpha}{12}\ell_z+\frac{25\alpha}{9}.
\tag{27.28}
$$

共同系数$11/12$的大小由两次顶角的$-1/2$与自能的$+1/12$相加确定，整体符号为负。对于$s$道，$\ell_{-s}=\ln(s/\mu^2)-i\pi$；$t,u$道分别多出$\ln(-t/s)$、$\ln(-u/s)$。固定散射角时，这些差保持有限，可以与共同的硬尺度对数分开。第20节已经求出的三个箱图是紫外有限的，领先部分只依赖角度比值及其对数，因而不再贡献$\ln\mu$。三道相加并乘上外腿因子后，振幅为

<span id="eq:c27-hard-amplitude"></span>

$$
\mathcal T=R^2\mathcal T_0
\left[1-\frac{11\alpha}{12}\ln\frac s{\mu^2}
+\alpha F_{\rm hard}(t/s,u/s)+O(\alpha^2)\right].
\tag{27.29}
$$

这里$F_{\rm hard}$收集了式[（27.28）](#eq:c27-hard-eleven)中的常数、三道不同的有限对数以及[第20节箱积分](/posts/srednicki-20/#c20-box)。它可以有虚部，但不依赖$\mu$，也不含发散的质量对数；需要完整有限角函数时，可直接代入这些已求出的表达式。本节关注的是各道共有的尺度对数。以上各式略去了随$m^2/s$及其对数趋零的质量修正，并在$\alpha|\ln(s/\mu^2)|$和$\alpha|\ln(s/m^2)|$尚小时按固定阶展开。

还有一份质量对数来自外态的归一化。由式[（27.15）](#eq:c27-residue-evaluated)，$R^2=1-\alpha(L_\mu+c'')/6+O(\alpha^2)$，将它乘入振幅并保留同一阶，得到

<span id="eq:c27-expanded-external-legs"></span>

$$
\frac{\mathcal T}{\mathcal T_0}
=1-\alpha\left[\frac{11}{12}\ln\frac s{\mu^2}
+\frac16L_\mu\right]
+\alpha\left(F_{\rm hard}-\frac{c''}6\right)+O(\alpha^2).
\tag{27.30}
$$

取模方时，一圈修正贡献其两倍实部，所以虚圈部分的两个大对数为$-11\alpha\ln(s/\mu^2)/6-\alpha L_\mu/3$。外腿修正由此进入事件概率，接下来还须加入给出同一探测读数的真实分裂。

采用[第26节规定的初末态权重](/posts/srednicki-26/#c26-initial-states)，四条腿的实分裂因子为

<span id="eq:c27-real-splitting"></span>

$$
1+\frac{\alpha}{3}
\left[\ln\frac{\delta^2s}{m^2}+c-\ln4\right]+O(\alpha^2),
\qquad c=\frac43-\sqrt3\pi.
\tag{27.31}
$$

这里使用两体质心系的$K^2=s/4$，角分辨率满足$m^2/s\ll\delta^2\ll1$。为与虚圈项逐项相加，把$\ln(\delta^2s/m^2)$写成$\ln(s/\mu^2)+L_\mu+\ln\delta^2$；这样，真实与虚圈项中相反的$L_\mu$系数就显现出来：

<span id="eq:c27-log-cancellation"></span>

$$
\begin{aligned}
&-\frac{11\alpha}{6}\ln\frac s{\mu^2}
-\frac{\alpha}{3}L_\mu
+\frac{\alpha}{3}
\left(\ln\frac s{\mu^2}+L_\mu+\ln\delta^2\right)\\
&\hspace{15mm}
=-\alpha\left[\frac32\ln\frac s{\mu^2}
+\frac13\ln\frac1{\delta^2}\right].
\end{aligned}
\tag{27.32}
$$

质量对数相消后，包容结果成为

<span id="eq:c27-inclusive-rate"></span>

$$
\frac{|\mathcal T|_{\rm obs}^2}{|\mathcal T_0|^2}
=1-\alpha\left[\frac32\ln\frac s{\mu^2}
+\frac13\ln\frac1{\delta^2}\right]
+\alpha F_{\rm obs}(t/s,u/s)+O(\alpha^2).
\tag{27.33}
$$

其中的有限函数为$F_{\rm obs}=2\operatorname{Re}F_{\rm hard}
-c''/3+(c-\ln4)/3$，在本节近似精度内不依赖$m,\mu$。这一相消使用了四条腿的共同权重；若固定两粒子纯初态，自动求和的只有两条出腿，式[（27.31）](#eq:c27-real-splitting)的系数便应减半，仍留下入射共线质量对数。因此，式[（27.33）](#eq:c27-inclusive-rate)的无质量极限与第26节的初态制备规定相联系。

还可以从旧方案的结果直接看出这一变化。旧方案的树率正比于$\alpha_{\rm OS}^2$，将耦合作有限换算后，它成为

<span id="eq:c27-rate-matching"></span>

$$
\alpha_{\rm OS}^2
=\alpha^2\left[1+\frac{3\alpha}{2}L_\mu
-\frac{\alpha}{2}c''\right]+O(\alpha^4).
\tag{27.34}
$$

将它乘上上一节的$1-\tfrac32\alpha\ln(s/m^2)+\cdots$，两处质量对数合为$-\tfrac32\alpha\ln(s/\mu^2)$，有限项也随$c''$一起换算。这就解释了为何改变耦合定义能够改写上一节留下的质量对数：描述同一过程的两种结果经过参数换算仍然相同。

<span id="c27-beta"></span>

## 从尺度独立性求出耦合的跑动

新的表达式中出现了任意选定的$\mu$，物理截面却应与这个选择无关。既然式[（27.33）](#eq:c27-inclusive-rate)显含$\mu$，耦合$g$就必须随尺度变化，使显式和隐式的依赖相互抵消。为将这一条件写成无量纲的对数关系，先把$|\mathcal T|_{\rm obs}^2$除以固定的运动学因子，使树级结果为$\alpha^2$，记所得量为$\mathcal R$。固定$s,t,u,\delta$后，式[（27.33）](#eq:c27-inclusive-rate)可写成

<span id="eq:c27-log-observable"></span>

$$
\ln\mathcal R
=2\ln\alpha+3\alpha\left[\ln\frac{\mu}{\mu_*}+C_2\right]
+O(\alpha^2).
\tag{27.35}
$$

这里$\mu_*$是固定参照尺度，$C_2$收集有限角函数和探测角$\delta$的依赖，因此它不随$\mu$或$\alpha$改变。若除去的运动学因子另选一个常数倍，右边只会增加一个与尺度无关的常数，不影响随后求出的尺度关系。

沿同一理论对$\ln\mu$求导时，树级的$\alpha^2$也随耦合变化，因此有

<span id="eq:c27-beta-chain-rule"></span>

$$
0=\frac{2\beta}{\alpha}+3\alpha
+3\beta\left[\ln\frac{\mu}{\mu_*}+C_2\right]+O(\alpha^2).
\tag{27.36}
$$

第一项须与$O(\alpha)$的第二项相消，从而确定$\beta=O(\alpha^2)$。第三项对$\beta$的影响则进入下一阶，领先结果为

<span id="eq:c27-beta-one-loop"></span>

$$
\beta(\alpha)=-\frac32\alpha^2+O(\alpha^3).
\tag{27.37}
$$

这同时给出了前面求质量反常量纲时暂用的阶数。所得$\beta$在此阶不依赖探测角，因为$\delta$只进入有限常数，求尺度导数时不参与领先相消。

裸参数提供了同一尺度关系的另一种写法。将式[（27.4）](#eq:c27-msbar-counterterms)代入裸质量和裸耦合，可得

<span id="eq:c27-bare-poles"></span>

$$
m_B^2=m^2\left(1-\frac{5\alpha}{6\epsilon}\right)+\cdots,\qquad
g_B=g\widetilde\mu^{\epsilon/2}
\left(1-\frac{3\alpha}{4\epsilon}\right)+\cdots .
\tag{27.38}
$$

在$d=6-\epsilon$中，耦合的工程维数先给出经典变化$\beta_d=-\epsilon\alpha+O(\alpha^2)$。这一项与反项极点相乘，会在物理维数的极限留下有限贡献。固定$g_B$，对第二式取对数再求导，得到

<span id="eq:c27-bare-beta-check"></span>

$$
0=\frac{\epsilon}{2}+\frac{\beta_d}{2\alpha}
-\frac{3}{4\epsilon}\beta_d+\cdots.
\tag{27.39}
$$

设$\beta_d=-\epsilon\alpha+b\alpha^2+\cdots$，方程中有限的$O(\alpha)$部分为$b\alpha/2+3\alpha/4$，于是$b=-3/2$。同样固定$m_B^2$，便有$0=2\gamma_m-5\beta_d/(6\epsilon)+\cdots$，在此阶得到$\gamma_m=-5\alpha/12$。这两次求导都需要先保留$\epsilon$项，让它与极点相乘后取有限部分，最后才令$\epsilon$趋于零。更高阶时各极点怎样配合，将在第28节继续讨论。

<span id="c27-flow"></span>

## 选择能标与渐近自由

重整化群方程使我们能够在不同能标之间换算耦合。只保留式[（27.37）](#eq:c27-beta-one-loop)的首项，将未知量改为耦合的倒数，方程便化成

<span id="eq:c27-inverse-coupling"></span>

$$
\frac{d}{d\ln\mu}\frac1\alpha=\frac32.
\tag{27.40}
$$

右边是常数，从$\mu_1$积分至$\mu_2$，再解出终点处的耦合，便有

<span id="eq:c27-running-coupling"></span>

$$
\frac1{\alpha(\mu_2)}-\frac1{\alpha(\mu_1)}
=\frac32\ln\frac{\mu_2}{\mu_1},\qquad
\alpha(\mu_2)=
\frac{\alpha(\mu_1)}
{1+\tfrac32\alpha(\mu_1)\ln(\mu_2/\mu_1)}.
\tag{27.41}
$$

这是截断微分方程的完整解，将由同一领先系数产生的一串尺度对数求和起来。对于正耦合，增大$\mu$会减小$\alpha$，这种行为称为渐近自由（asymptotic freedom）。因而在散射能量$\sqrt s$处取$\mu\simeq\sqrt s$，既可减小式[（27.33）](#eq:c27-inclusive-rate)中的硬尺度对数，又能用较小的耦合组织高能展开。若$\delta$极小，角分辨率对数仍会很大，需要另行处理；这里的跑动求和针对共同的硬尺度部分。

沿相反方向降低$\mu$，耦合会逐渐增大。式[（27.41）](#eq:c27-running-coupling)的分母在下面这个形式尺度处降为零：

<span id="eq:c27-formal-strong-scale"></span>

$$
\Lambda_{\rm formal}
=\mu_1\exp\left[-\frac{2}{3\alpha(\mu_1)}\right]
\tag{27.42}
$$

耦合在接近这一尺度前已增至一的量级，高阶 $\beta$ 项随之变得重要。$\Lambda_{\rm formal}$ 因而标记领先跑动解进入强耦合区的尺度。

对于有质量粒子的散射，实际两粒子阈值是$s=4M^2$。领先阶可以用$4m^2$代替，超出这一精度时则须区分$m(\mu)$与$M$。当过程能量接近质量，通常在$\mu$约为物理质量处使用保留质量的圈积分，或作低能匹配。这是一种为低能计算选择尺度的安排；$\overline{\mathrm{MS}}$采用质量无关的$\beta$函数，它本身并不会在$\mu=M$自动变为零。只要该尺度的耦合仍小，有质量过程还可以作微扰计算；令$m=0$后，则没有相同的质量尺度截住向低能的演化，因而需要进一步研究强耦合物理。

本例的低能讨论还须结合第5节提出的真空问题。实$\varphi^3$势及其导数为

<span id="eq:c27-cubic-vacuum"></span>

$$
V(\varphi)=\frac12m^2\varphi^2-\frac g6\varphi^3,\qquad
V'(\varphi)=\varphi\left(m^2-\frac g2\varphi\right).
\tag{27.43}
$$

当$m^2>0$时，$\varphi=0$是局部极小值，另一驻点$\varphi_b=2m^2/g$满足$V''(\varphi_b)=-m^2$及$V(\varphi_b)=2m^6/(3g^2)$，因此形成一个局部势垒。越过势垒，沿$g\varphi>0$方向势能向下无界；当$m=0$时，连这个局部势垒也消失了。本节对有质量情形所作的计算，采用的正是围绕局部真空的微扰展开。这里的真空判断来自势的形状，而负$\beta$描述的是弱耦合下的尺度变化，两种性质分别由各自的计算得到。

量子色动力学在高能处耦合变弱，低能激发用无色强子描述，[第73节](/posts/srednicki-73/)和[第82节](/posts/srednicki-82/)将讨论这种变化。若某理论在小正耦合处$\beta>0$，降低能标就使耦合减小，这称为红外自由（infrared freedom）；沿相反方向提高能量，耦合则逐渐增大。[第66节](/posts/srednicki-66/)将计算量子电动力学的跑动。$\beta$还可能在非零耦合处出现零点，[下一节](/posts/srednicki-28/)将讨论这样的固定点。

<span id="c27-coupled-running"></span>

## 质量与耦合的共同跑动

最后将质量方程与耦合方程一起求解。在正质量、正耦合的区间内，先写出一般的领先形式

<span id="eq:c27-general-leading-flow"></span>

$$
\frac{d\alpha}{d\ln\mu}=b_1\alpha^2,\qquad
\frac{d\ln m}{d\ln\mu}=c_1\alpha,\qquad b_1\ne0.
$$

两式相除便消去任意尺度参数，得到 $d\ln m/d\alpha=c_1/(b_1\alpha)$。从 $\mu_1$ 对应的耦合积分到 $\mu_2$ 对应的耦合，结果为

<span id="eq:c27-coupled-mass-integral"></span>

$$
\ln\frac{m(\mu_2)}{m(\mu_1)}
=\frac{c_1}{b_1}\int_{\alpha(\mu_1)}^{\alpha(\mu_2)}\frac{d\alpha}{\alpha}
=\frac{c_1}{b_1}\ln\frac{\alpha(\mu_2)}{\alpha(\mu_1)}.
$$

于是 $m(\mu)\alpha(\mu)^{-c_1/b_1}$ 在这两个截断方程下保持不变。本节 $b_1=-3/2$、$c_1=-5/12$，其比值为 $5/18$，故

<span id="eq:c27-coupled-running-solution"></span>

$$
\begin{aligned}
m(\mu_2)
&=m(\mu_1)\left[\frac{\alpha(\mu_2)}{\alpha(\mu_1)}\right]^{5/18}\\
&=m(\mu_1)\left[1+\frac32\alpha(\mu_1)
 \ln\frac{\mu_2}{\mu_1}\right]^{-5/18}.
\end{aligned}
$$

在括号为正且耦合仍小时，提高能标同时降低耦合和参数质量。将最后一行展开，首项为 $m(\mu_1)[1-\frac5{12}\alpha(\mu_1)\ln(\mu_2/\mu_1)+\cdots]$，与质量反常量纲的微分方程一致。

---

[← 第 26 节](/posts/srednicki-26/) · [章节地图](/srednicki/) · [第 28 节 →](/posts/srednicki-28/)
