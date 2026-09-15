---
title: 'Srednicki §67 量子电动力学中的沃德恒等式 I'
date: 2026-09-14
category: 笔记
tags: [物理, 量子场论, Srednicki]
series: 'Srednicki QFT'
srednickiSections: [67]
hideFromHome: true
draft: false
---

<span id="c67"></span>

第59节计算电子与正电子湮灭时，曾利用一个重要性质：把外光子的极化矢量加上它的四动量，振幅不变。第61节的标量计算也具有这一性质，不过那里必须把两个交换图和双光子接触图相加，才能看见抵消。现在从流的守恒出发说明它们的共同原因。这样得到的关系作用于图的总和，也适用于包含圈修正的振幅。

沿第22节的路径积分约定、第59节的外线规则及本节的流归一约定，将一个外光子的偏振因子提出，写成
<span id="eq:c67-longitudinal-target"></span>

$$
\mathcal T=\epsilon^\mu\mathcal M_\mu,\qquad
\mathcal T[\epsilon+ck]-\mathcal T[\epsilon]
 =c\,k^\mu\mathcal M_\mu.
\tag{67.1}
$$

这里$k^2=0$，其他外态保持不变。所求的规范不变性于是等价于$k^\mu\mathcal M_\mu=0$。以下把所有外动量看作出射；实际入粒子的动量在这个记号中取负，因而$k_i^0<0$。$\epsilon^\mu$统指该外腿实际使用的偏振因子：出射与入射的共轭关系仍按第58、59节处理。

<span id="c67-external-poles"></span>

## 散射振幅是哪些极点的留数

证明中最有用的LSZ性质，是它只提取每条外腿都带有传播子极点的部分。先用标量场说明，并把$m$改记为$M$，强调这里取的是物理极点质量。讨论连通散射时，
<span id="eq:c67-connected-s"></span>

$$
\langle f|S|i\rangle_c
 =i(2\pi)^4\delta^4\!\left(\sum_{a=1}^n k_a\right)\mathcal T.
\tag{67.2}
$$

完整$S$矩阵中还有恒等项和可能的旁观粒子因子，它们在第5节已经分开处理。这里的单个总动量δ函数与全外腿留数对应连通散射部分。

暂取单位极点留数的外场，并定义含一个额外$i$的傅里叶插入，以便吸收每条外腿的LSZ因子：
<span id="eq:c67-coordinate-lsz"></span>

$$
\begin{aligned}
\widetilde\phi(k)&:=i\int d^4x\,e^{-ikx}\phi(x),\\
\langle f|S|i\rangle_c
 &=\left[\prod_{a=1}^n
       i\int d^4x_a\,e^{-ik_ax_a}(-\partial_a^2+M_a^2)\right]\\
 &\qquad{}\times
       \langle0|T\phi_1(x_1)\cdots\phi_n(x_n)|0\rangle_c .
\end{aligned}
\tag{67.3}
$$

这个$i$把每条外线原来携带的LSZ因子吸收到场的定义中。它只用于本节的$\widetilde\phi$，通常的傅里叶变换约定不随之改变。对波包形式的外态分部积分，两个导数都转到指数上；由于$\partial^2e^{-ikx}=-k^2e^{-ikx}$，有
<span id="eq:c67-full-residue"></span>

$$
\begin{aligned}
\langle0|T\widetilde\phi_1(k_1)\cdots
                   \widetilde\phi_n(k_n)|0\rangle_c
 &=(2\pi)^4\delta^4\!\left(\sum_a k_a\right)\mathcal F(k_1,\ldots,k_n),\\
i\mathcal T
 &=\lim_{k_a^2\to-M_a^2}
       \prod_{a=1}^n(k_a^2+M_a^2)\,\mathcal F.
\end{aligned}
\tag{67.4}
$$

总δ函数来自共同平移所有插入点；提出它之后，标量函数只依赖$k_a^2$及$k_a\cdot k_b$等洛伦兹不变量。在取极限之前，外动量先保持离壳，因而每一个外腿的极点都可以单独辨认。

若所用场是第66节的减除方案场，它的极点留数一般不等于一。令对应的真空—单粒子重叠为$\sqrt{r_a}$，每条LSZ外腿还须除以这个重叠，所以上式推广为
<span id="eq:c67-overlaps-remainder"></span>

$$
\begin{aligned}
i\mathcal T
 &=\left(\prod_a r_a^{-1/2}\right)
   \lim_{k_a^2\to-M_a^2}\prod_a(k_a^2+M_a^2)\,\mathcal F,\\
\mathcal F
 &=\frac{i\mathcal T\prod_a\sqrt{r_a}}
          {\prod_a(k_a^2+M_a^2)}+\mathcal F_{\rm rem},\\
0&=\lim_{k_a^2\to-M_a^2}
       \prod_a(k_a^2+M_a^2)\mathcal F_{\rm rem}.
\end{aligned}
\tag{67.5}
$$

这些重叠是两点函数的实际留数，不是拉氏量中的反项$Z_a$。对余项只要求最后一行的极限为零，不要求它在所有通道都正则。例如，$H/(k_1^2+M_1^2)$仍有第一条腿的极点，但若$H$在第二条腿的壳附近正则，就会被第二个LSZ因子消去。以下均在其他道的奇点没有与所取外腿极点重合的动量邻域中作这种留数提取。

费米场的传播子极点还带有旋量矩阵。例如，对物理出射电子，相应的自由逆核为$K_0(p)=\slashed p+M$；利用$\slashed p^{\,2}=-p^2$，有

$$
K_0(p)(-\slashed p+M)=(p^2+M^2)\mathbf1,\qquad
\bar u(p)K_0(p)=0.
$$

第一式消去传播子的极点分母，而不带该极点的正则矩阵在外端乘$\bar uK_0$后为零。反粒子使用相应的$v$外端，理由相同。光子的约化则先作物理偏振投影，再以$k^2$提取横向极点。因而不同自旋改变留数的张量结构，却不改变这种外腿选择作用。

<span id="c67-contact-terms"></span>

## 场方程在关联函数中产生什么

场方程作用于时间排序关联函数时，会在重合点产生接触项。第22节的施温格–戴森方程给出它们的系数。含导数的复合插入沿第22节的路径积分处方定义；波算符作用于完整时间序函数，包含时间排序阶跃函数的导数。令$O=\phi_{a_1}(x_1)\cdots\phi_{a_n}(x_n)$。先对一个偶场作积分变量的无穷小位移；路径积分的总泛函导数为零，因而
<span id="eq:c67-schwinger-dyson"></span>

$$
\begin{aligned}
0&=\int D\phi\,
 \frac{\delta}{\delta\phi_a(x)}\left(Oe^{iS}\right),\\
\left\langle T\frac{\delta S}{\delta\phi_a(x)}O\right\rangle
 &=i\left\langle T\frac{\delta O}{\delta\phi_a(x)}\right\rangle\\
 &=i\sum_{j=1}^n\delta_{aa_j}\delta^4(x-x_j)
   \left\langle T\phi_{a_1}(x_1)\cdots
        \widehat{\phi_{a_j}(x_j)}\cdots\phi_{a_n}(x_n)\right\rangle .
\end{aligned}
\tag{67.6}
$$

帽号表示删去该因子。第二行的正$i$来自将第一行中的作用量导数移到另一边：$-1/i=i$。当$x$与其他插入点分离时，右端没有支撑，关联函数中的欧拉导数才等于零；在重合点，δ函数就是场方程的量子接触项。

场$\phi_a$可以具有任意自旋。若它是格拉斯曼奇场，乘积求导须使用有序的左导数。记$\eta_a=0,1$为场的奇偶性，把欧拉插入放在乘积左端，则
<span id="eq:c67-graded-derivative"></span>

$$
\begin{aligned}
\frac{\delta_L O}{\delta\phi_a(x)}
 &=\sum_j(-1)^{\eta_a(\eta_{a_1}+\cdots+\eta_{a_{j-1}})}
   \delta_{aa_j}\delta^4(x-x_j)\,O_{\widehat j},\\
\left\langle T\frac{\delta_L S}{\delta\phi_a(x)}O\right\rangle
 &=i\left\langle T\frac{\delta_L O}{\delta\phi_a(x)}\right\rangle .
\end{aligned}
\tag{67.7}
$$

每越过一个此前的奇场，左导数产生一个负号。对$Oe^{iS}$用分级乘法法则时，作用量导数一项先有$(-1)^{\eta_a|O|}$；再将这个奇欧拉导数从$O$右侧移到左侧，会产生相同的号，两者相消，得到第二行。本节随后只对光子$A_\mu$求场导数，它是偶场，因此式[（67.6）](#eq:c67-schwinger-dyson)本身已经适用。

接触项为何与外腿极点不同，可以直接作一次傅里叶变换。考虑
$\delta^4(x_1-x_2)H(x_2,x_3,\ldots)$，置$y=x_1-x_2$、$X=x_2$。这个线性变换的雅可比行列式为1，于是
<span id="eq:c67-contact-fourier"></span>

$$
\begin{aligned}
&\int d^4x_1d^4x_2\,
 e^{-ik_1x_1-ik_2x_2}\delta^4(x_1-x_2)H(x_2,\ldots)\\
&\qquad=\int d^4X\,d^4y\,
 e^{-i(k_1+k_2)X-ik_1y}\delta^4(y)H(X,\ldots)\\
&\qquad=\int d^4X\,e^{-i(k_1+k_2)X}H(X,\ldots).
\end{aligned}
\tag{67.8}
$$

两个独立的外动量已合成$k_1+k_2$。因此低点函数即使含有
$[(k_1+k_2)^2+M^2]^{-1}$这样的通道极点，也不会在一般动量处分别含有
$(k_1^2+M_1^2)^{-1}$和$(k_2^2+M_2^2)^{-1}$。乘上完整外腿逆核，再取独立的外腿留数，就得到零。

重整化的局域接触分布还可能含δ函数的有限阶导数。一次分部积分给
<span id="eq:c67-contact-derivative"></span>

$$
\int d^4y\,e^{-ik_1y}\,
       \partial_{y^\nu}\delta^4(y)=ik_{1\nu};
\tag{67.9}
$$

更多导数只增加动量多项式。这样的多项式也不能补出缺少的外腿传播子。接触项缺少完整的独立外腿极点，但仍可有合并动量通道的奇性。软光子或共线等例外极限须在这一步之后另作分析。

<span id="c67-photon-current"></span>

## 把外光子改写为流的插入

现在回到量子电动力学。先确定场方程右侧的流，才能把光子的LSZ波算符换成它。对狄拉克场，含反项的物质拉氏量为
<span id="eq:c67-dirac-action"></span>

$$
\mathcal L_{\rm D}
 =iZ_2\bar\Psi\gamma^\mu\partial_\mu\Psi
  -Z_m m\bar\Psi\Psi+eZ_1A_\mu\bar\Psi\gamma^\mu\Psi .
\tag{67.10}
$$

将整体相位暂时改为位置函数，但在这次变元中保持$A_\mu$不变：
$\delta\Psi=-ie\alpha(x)\Psi$、$\delta\bar\Psi=ie\alpha(x)\bar\Psi$。
质量项和电磁相互作用项的两个相位相消，动能中只留下导数作用于$\alpha$的一项，故
<span id="eq:c67-dirac-current-normalization"></span>

$$
\begin{aligned}
\delta\mathcal L_{\rm D}
 &=eZ_2\bar\Psi\gamma^\mu\Psi\,\partial_\mu\alpha
   =J^\mu_{\rm D}\partial_\mu\alpha,\\
J^\mu_{\rm D}&=eZ_2\bar\Psi\gamma^\mu\Psi,\\
K^\mu_{\rm D}:=\frac{\partial\mathcal L_{\rm D}}{\partial A_\mu}
 &=eZ_1\bar\Psi\gamma^\mu\Psi
 =\frac{Z_1}{Z_2}J^\mu_{\rm D}.
\end{aligned}
\tag{67.11}
$$

因此诺特流$J^\mu$与麦克斯韦方程的源$K^\mu$相差常数$Z_1/Z_2$。定义$j^\mu=J^\mu/Z_2$，便可将$K^\mu$写成$Z_1j^\mu$。这个归一差别并不影响守恒，但会进入沃德接触项的系数。

标量理论要保留含$A_\mu$的那一部分流。为直接沿用第65节的记号，本段记$Z_\varphi=Z_2$，并定义
$B^\mu=\varphi^\dagger\partial^\mu\varphi-(\partial^\mu\varphi^\dagger)\varphi$、
$\rho=\varphi^\dagger\varphi$。依照第61节确定的电荷支，
<span id="eq:c67-scalar-action"></span>

$$
\mathcal L_{\rm s}
 =-Z_2\partial_\mu\varphi^\dagger\partial^\mu\varphi
  -Z_m m^2\rho-\frac14Z_\lambda\lambda\rho^2
  -ieZ_1 B^\mu A_\mu-e^2Z_4\rho A^2 .
\tag{67.12}
$$

取$\delta\varphi=-ie\alpha\varphi$及其共轭。由于$\delta\rho=0$，
势能和$A^2$项不变，而
$\delta B^\mu=-2ie\rho\,\partial^\mu\alpha$。动能与线性电磁项的变分分别给
$-ieZ_2B^\mu\partial_\mu\alpha$和$-2e^2Z_1\rho A^\mu\partial_\mu\alpha$，
所以
<span id="eq:c67-scalar-current-normalization"></span>

$$
\begin{aligned}
J^\mu_{\rm s}&=-ieZ_2B^\mu-2e^2Z_1\rho A^\mu,\\
K^\mu_{\rm s}&=-ieZ_1B^\mu-2e^2Z_4\rho A^\mu,\\
Z_4=\frac{Z_1^2}{Z_2}
&\quad\Longrightarrow\quad
K^\mu_{\rm s}=\frac{Z_1}{Z_2}J^\mu_{\rm s}=Z_1j^\mu_{\rm s}.
\end{aligned}
\tag{67.13}
$$

最后一行使用[第65节由有限规范变换证明的条件](/posts/srednicki-65/#c65-finite-gauge)。流中的$A^\mu$项正与作用量中的双光子项相配，使两种理论都满足$K_\mu=Z_1j_\mu$；这里允许$Z_1/Z_2$为一般常数。

还需处理光子方程中的纵向部分。写一般协变规范的光子拉氏量为
<span id="eq:c67-gauge-fixing"></span>

$$
\mathcal L_A=-\frac{Z_3}{4}F_{\mu\nu}F^{\mu\nu}
             -\frac{\kappa}{2}(\partial_\mu A^\mu)^2,\qquad
\kappa=\frac1\xi .
\tag{67.14}
$$

这里$\kappa$只表示规范固定项的系数，先取有限非零$\xi$；严格横向规范可在完成横向投影后取$\xi\to0$极限。麦克斯韦项的一次变分为
$-Z_3F^{\mu\nu}\partial_\mu\delta A_\nu$，分部积分后变成
$Z_3(\partial_\mu F^{\mu\nu})\delta A_\nu$；规范固定项同样分部积分一次。
将整个欧拉导数的指标统一写在下方，得到
<span id="eq:c67-photon-euler"></span>

$$
\begin{aligned}
E_{A\mu}:=\frac{\delta S}{\delta A^\mu}
 &=Z_3\partial^\nu F_{\nu\mu}
      +\kappa\,\partial_\mu(\partial A)+K_\mu\\
 &=Z_3\partial^2A_\mu
      +(\kappa-Z_3)\partial_\mu(\partial A)+Z_1j_\mu .
\end{aligned}
\tag{67.15}
$$

若选择$\kappa=Z_3$，
即对归一后的光子场用费曼规范，这个梯度确实不出现。保留一般$\kappa$也可以继续证明，不过要在外光子的约化中消去它。

将式[（67.6）](#eq:c67-schwinger-dyson)用于$A^\mu$。记$O$为其余所有外场的有序乘积，$G_{A\mu}=\langle TA_\mu(x)O\rangle$、
$G_{j\mu}=\langle Tj_\mu(x)O\rangle$，并用$C_\mu$表示对$O$作光子场导数所得的δ函数接触项之和，则
<span id="eq:c67-photon-schwinger-dyson"></span>

$$
(-\partial^2)G_{A\mu}
 =\frac{Z_1}{Z_3}G_{j\mu}
  +\frac{\kappa-Z_3}{Z_3}\partial_\mu
       \langle T(\partial A)(x)O\rangle
  -\frac{i}{Z_3}C_\mu .
\tag{67.16}
$$

最后一项的负号来自把欧拉插入移到等号右边。若$O$中含另一光子，
场导数在其位置产生δ函数并删去该光子场；若$O$只含独立的物质场，
这类光子场导数接触项本来就是零。

令$f^\mu(x)$为外光子的自由波包。它满足$\partial_\mu f^\mu=0$，
空间无穷远的表面项由波包衰减消去，时间边界按LSZ的绝热散射极限处理。
于是对于中间梯度项，
<span id="eq:c67-transverse-wave-test"></span>

$$
\int d^4x\,f^\mu\partial_\mu H
 =-\int d^4x\,(\partial_\mu f^\mu)H=0.
\tag{67.17}
$$

对一个傅里叶分量，$f^\mu=\epsilon^\mu e^{-ikx}$时这一条件就是$k\epsilon=0$。
稍后将$\epsilon^\mu$换成$k^\mu$，因为$k^2=0$，新的自由测试波仍满足同一散度条件。因此省去梯度在证明的两步中都成立。

用$\mathscr L_{\rm rest}$代表其余各条外腿的完整约化操作：每条腿的傅里叶积分及其$i$因子、相应自由逆核、在壳极限、外旋量或外偏振，以及逆重叠因子都包括在内；该记号中不含当前光子这条腿。式[（67.3）](#eq:c67-coordinate-lsz)于是给
<span id="eq:c67-current-lsz"></span>

$$
\begin{aligned}
\langle f|S|i\rangle_c
 &=\frac{i\epsilon^\mu}{\sqrt{r_A}}\int d^4x\,e^{-ikx}
      \mathscr L_{\rm rest}\,(-\partial^2)G_{A\mu}\\
 &=\frac{iZ_1}{Z_3\sqrt{r_A}}\epsilon^\mu
      \int d^4x\,e^{-ikx}
      \mathscr L_{\rm rest}\,G_{j\mu}.
\end{aligned}
\tag{67.18}
$$

第一行的每条其他外腿仍须取留数。式[（67.16）](#eq:c67-photon-schwinger-dyson)中的$C_\mu$缺少与它重合的那条其他外腿传播子，按式[（67.8）](#eq:c67-contact-fourier)的分析被约化消去；纵向梯度则由前一式消去。光子动能和电流耦合分别给出$Z_3$与$Z_1$；非单位光子留数还带来$1/\sqrt{r_A}$。

<span id="c67-ward-identity"></span>

## 流的沃德恒等式完成证明

现在对式[（67.18）](#eq:c67-current-lsz)收缩$k^\mu$。在作这一步之前，先从刚才的局域相位变元写出流散度的接触项。这样可以看清楚经典守恒在量子乘积里如何使用。

选择保持矢量相位对称性的调节与反项。对复标量，相位矩阵$U=e^{-ie\alpha}$及其共轭的雅可比行列式相乘为1。对狄拉克的格拉斯曼变量，两个测度分别给逆行列式，因而
<span id="eq:c67-vector-jacobian"></span>

$$
D\Psi'\,D\bar\Psi'
 =(\det U)^{-1}(\det U^{-1})^{-1}D\Psi\,D\bar\Psi
 =D\Psi\,D\bar\Psi .
\tag{67.19}
$$

在有限调节的变量集合中，这个相消可以逐项进行。去调节时，复合流插入和反项须按同一恒等式定义；这就是第22节量子沃德关系在这里所用的条件。此处变元是矢量相位，且$A_\mu$保持不变，规范固定项本身不参与变分。

令第$a$个外场的变分为$\delta\Phi_a=\alpha R_a$，
其中$R_a=-ieq_a\Phi_a$，共轭场取相反$q_a$，光子取$q_a=0$。
由于$\delta S=\int J^\mu\partial_\mu\alpha$，对紧支撑的$\alpha$分部积分，
再利用路径积分的换元不变性，得到
<span id="eq:c67-noether-ward"></span>

$$
\begin{aligned}
\delta S&=-\int d^4x\,\alpha(x)\,\partial_\mu J^\mu(x),\\
0&=\langle\delta O\rangle+i\langle O\,\delta S\rangle,\\
\partial_\mu\langle TJ^\mu(x)O\rangle
 &=-i\sum_a\delta^4(x-x_a)
      \langle T\Phi_1\cdots R_a(x_a)\cdots\Phi_N\rangle\\
 &=-e\sum_a q_a\delta^4(x-x_a)\langle TO\rangle .
\end{aligned}
\tag{67.20}
$$

相位参数是格拉斯曼偶数，作用于整个有序乘积时不引入奇置换。
最后一行的负号来自$(-i)(-i)=-1$。用$j^\mu=J^\mu/Z_2$改写，得到
<span id="eq:c67-normalized-current-ward"></span>

$$
\partial^\mu G_{j\mu}(x)
 =-\frac e{Z_2}\sum_a q_a\delta^4(x-x_a)\langle TO\rangle.
\tag{67.21}
$$

在非重合点它还原为流守恒；在外场所在的位置，流的散度记录该场所带的电荷。

回到光子的傅里叶积分，利用
$ik^\mu e^{-ikx}=-\partial^\mu e^{-ikx}$。
用同样的波包和边界条件分部积分，有
<span id="eq:c67-longitudinal-current"></span>

$$
\begin{aligned}
\left.\langle f|S|i\rangle_c\right|_{\epsilon\to k}
 &=\frac{Z_1}{Z_3\sqrt{r_A}}
   \int d^4x\,e^{-ikx}\,
      \mathscr L_{\rm rest}\,\partial^\mu G_{j\mu}(x)\\
 &=-\frac{eZ_1}{Z_3Z_2\sqrt{r_A}}
   \sum_a q_a\,
   \mathscr L_{\rm rest}
   \int d^4x\,e^{-ikx}\delta^4(x-x_a)\langle TO\rangle .
\end{aligned}
\tag{67.22}
$$

这里又出现接触项，但它们来自流的沃德关系，与前面欧拉方程产生的接触项不同。要判断它们的贡献，仍须保留$\mathscr L_{\rm rest}$中的每一个外腿逆核。

对第$a$项，把$\mathscr L_{\rm rest}$中的其他傅里叶积分先展开。除去其中显式的LSZ因子后，普通傅里叶积分给
<span id="eq:c67-ward-merged-leg"></span>

$$
\begin{aligned}
&\int d^4x\prod_b d^4x_b\,
  e^{-ikx-i\sum_b k_bx_b}\,
  \delta^4(x-x_a)\langle T\Phi_1(x_1)\cdots\Phi_N(x_N)\rangle\\
&\qquad=\widehat G_N(k_1,\ldots,k_a+k,\ldots,k_N).
\end{aligned}
\tag{67.23}
$$

因此第$a$条物质传播子的动量是$k_a+k$，而它的LSZ因子仍按外态动量$k_a$取壳。对一般非零外光子动量，
<span id="eq:c67-missing-matter-pole"></span>

$$
\begin{gathered}
(k_a+k)^2+M_a^2=(k_a^2+M_a^2)+2k_ak,\\
\lim_{k_a^2\to-M_a^2}
 (k_a^2+M_a^2)\widehat G_N(\ldots,k_a+k,\ldots)=0 .
\end{gathered}
\tag{67.24}
$$

其中极限在$2k_ak\ne0$及其余通道非例外的邻域取。费米场对应的自由逆核与外旋量给同样的外腿留数选择。每一项都缺少自己所需的一条物质外腿极点，于是式[（67.22）](#eq:c67-longitudinal-current)为零。提出总动量δ函数后，最终得到
<span id="eq:c67-ward-result"></span>

$$
k^\mu\mathcal M_\mu=0,\qquad
\mathcal T[\epsilon+ck]=\mathcal T[\epsilon].
\tag{67.25}
$$

这个结论说明，改变外光子势的纯规范部分不会改变散射振幅。第59节用它消去了物理偏振和中的参考矢量项；现在可以把同一操作用于满足上述量子沃德关系的圈图总和。证明先在一般动量处进行，随后才取特殊运动学极限。它按微扰约化来理解，红外调节必须与所用场方程、外腿波算符相容；若另外保留光子质量，质量项也须一同保留。排他带电散射率在去掉红外调节后的存在性，还需结合第26节所讨论的未分辨辐射来处理。

标量理论的双光子接触图在LSZ约化中仍有贡献。这类图的内部顶角是局域的，四条外传播子照常从该顶角延伸到各自的外场位置，所以图仍有完整外腿极点。沃德或欧拉关系中的δ函数却直接合并两个外插入点，才会缺少一条独立外腿极点。下面用两个树级例子展开这种相消：标量双光子顶角补齐两个交换图的余项，费米图则在内线逆核相消后留下外端的狄拉克方程。

<span id="c67-tree-examples"></span>

## 树图中的纵向光子相消

把第一个出光子的极化矢量换成它的动量，
直接验证湮灭幅为零。以下保留第59、61节的物理入、出射记号：
两个物质粒子的正能入射动量记为$p,q$，两个出光子动量记为
$k=k'_1,l=k'_2$，其极化矢量记为$\epsilon=\varepsilon'_1,\eta=\varepsilon'_2$。
出光子外因子取$\varepsilon$，
不在振幅中另加复共轭。

前面的LSZ叙述把全部外腿看作出射，因而其四个动量为$-p,-q,k,l$。
若按顶角规则把全部外动量取为入射，则是$p,q,-k,-l$。
下面每幅图都按后一规则检查顶角守恒，同时保留$k,l$作为实际出光子动量。
仍取$g=(-,+,+,+)$、$e<0$及$m>0$，只计算$e^2$阶树幅。

<span id="c67-scalar-tree"></span>

### 标量交换图与双光子顶角

两条外标量腿在壳，两个光子无质量，故
<span id="eq:c67-ex-1-kinematics"></span>

$$
\begin{aligned}
p+q&=k+l,\qquad p^2=q^2=-m^2,\qquad k^2=l^2=0,\\
t&=-(p-k)^2,\qquad u=-(p-l)^2,\\
d_t\equiv m^2-t&=(p-k)^2+m^2=-2p\cdot k,\\
d_u\equiv m^2-u&=(p-l)^2+m^2=-2p\cdot l=-2q\cdot k .
\end{aligned}
\tag{67.26}
$$

第三行使用$p^2=-m^2$与$k^2=0$。
第四行最后一个等式由$p-l=k-q$及$q^2=-m^2$得到，
所以两条物质腿的在壳条件都已进入分母的化简。
有质量的湮灭物理区中$d_t,d_u>0$，如[第59节](/posts/srednicki-59/#eq:c59-physical-denominators)已经求出的
$d_t=s(1-\beta\cos\theta)/2$、$d_u=s(1+\beta\cos\theta)/2$；
这里$s=-(p+q)^2\ge4m^2$，$\beta=\sqrt{1-4m^2/s}<1$。
以下消去分母不会遇到内部极点。

用$k\cdot\epsilon=l\cdot\eta=0$简化两幅交换图和接触图之和，得到
<span id="eq:c67-ex-1-source-amplitude"></span>

$$
\mathcal T=-e^2\left[
 \frac{4(p\cdot\epsilon)(q\cdot\eta)}{d_t}
 +\frac{4(p\cdot\eta)(q\cdot\epsilon)}{d_u}
 +2\epsilon\cdot\eta\right].
\tag{67.27}
$$

令$\epsilon=k$后，$k\cdot\epsilon=k^2=0$仍然成立，
因此这次代入可以继续使用该简化式。
第一幅交换图由$2p\cdot k=-d_t$消去分母，
第二幅由$2q\cdot k=-d_u$消去分母，
第三幅则留下双光子顶角的局部项：
<span id="eq:c67-ex-1-direct-contraction"></span>

$$
\begin{aligned}
\mathcal T\big|_{\epsilon=k}
&=-e^2\left[-2q\cdot\eta-2p\cdot\eta+2k\cdot\eta\right]\\
&=2e^2(p+q-k)\cdot\eta
 =2e^2l\cdot\eta=0 .
\end{aligned}
\tag{67.28}
$$

最后一步用了另一条出光子的物理横向性$l\cdot\eta=0$。
因此纵向替换后的振幅为零。

双光子项的系数2是这次相消所必需的。
从[第61节的树规则](/posts/srednicki-61/#c61-vertices)可以看得更清楚：
标量内线为$-i/(r^2+m^2-i0)$，沿同一标量箭头的三价顶角为
$ie(r+r')_\mu$，双光子顶角为$-2ie^2g_{\mu\nu}$。
让第一幅图的内部箭头带$a=p-k=l-q$，
两顶角沿标量箭头的动量分别是$(p,a)$与$(a,-q)$。
入射标量反粒子的物理动量$q$在这条连续箭头上因此写成$-q$。
逐因子相乘给
<span id="eq:c67-ex-1-vertex-factors"></span>

$$
\begin{aligned}
i\mathcal T_t
&=ie(2p-k)\cdot\epsilon\,
  \frac{-i}{d_t}\,
  ie(l-2q)\cdot\eta\\
&=-ie^2\,
  \frac{[(2p-k)\cdot\epsilon][(2q-l)\cdot\eta]}{d_t},\\
i\mathcal T_{\rm contact}
&=-2ie^2\,\epsilon\cdot\eta .
\end{aligned}
\tag{67.29}
$$

第一行的两个$ie$与内线$-i$合为$ie^2$，
第二行的负号来自$l-2q=-(2q-l)$。
交换两个出光子得到另一幅交换图，光子的玻色统计使两幅图相加。
除去图值的共同$i$，在使用偏振横向性之前的完整张量是
<span id="eq:c67-ex-1-complete-tensor"></span>

$$
\begin{aligned}
\mathcal T&=\epsilon^\mu\eta^\nu M_{\mu\nu},\\
M_{\mu\nu}
&=-e^2\left[
 \frac{(2p-k)_\mu(2q-l)_\nu}{d_t}
 +\frac{(2q-k)_\mu(2p-l)_\nu}{d_u}
 +2g_{\mu\nu}\right].
\end{aligned}
\tag{67.30}
$$

它与式[（67.27）](#eq:c67-ex-1-source-amplitude)在物理偏振上给相同的幅。
要识别外物质在壳条件的作用，可以把标量逆核记为$D(r)=r^2+m^2$，
暂只使用动量守恒：
<span id="eq:c67-ex-1-inverse-differences"></span>

$$
\begin{aligned}
k\cdot(2p-k)&=p^2-(p-k)^2=D(p)-d_t,\\
k\cdot(2q-k)&=q^2-(q-k)^2=D(q)-d_u.
\end{aligned}
\tag{67.31}
$$

这些等式自身不要求标量在壳。
代入完整张量之后，不含$D(p),D(q)$的两项之和为
$-(2q-l)_\nu-(2p-l)_\nu=-2k_\nu$，
恰好被局部双光子项的$2k_\nu$消去。因此
<span id="eq:c67-ex-1-external-inverses"></span>

$$
\begin{aligned}
k^\mu M_{\mu\nu}
&=-e^2\left[
 \frac{D(p)}{d_t}(2q-l)_\nu+
 \frac{D(q)}{d_u}(2p-l)_\nu\right]\\
&=0\qquad\text{在 }D(p)=D(q)=0\text{ 时}.
\end{aligned}
\tag{67.32}
$$

剩下的恰是两条外物质腿的逆核。
在壳后，完整张量的收缩已经为零，可再乘任意$\eta^\nu$；
用简化幅计算时，则在式[（67.28）](#eq:c67-ex-1-direct-contraction)最后使用了$\eta$的横向性。
交换$(k,\mu)$与$(l,\nu)$使两幅交换图互换，局部顶角不变，
所以同样有$l^\nu M_{\mu\nu}=0$。

这里的双光子接触图来自拉格朗日量中的
$-e^2A^2\varphi^\dagger\varphi$，在约化前连接着四条外传播子，
能够贡献完整的外腿极点。前面场方程中合并两个外插入点的接触项
在一般非退化散射运动学下缺少相应的独立外腿极点；
两种接触结构在LSZ约化中的作用由此区分。

<span id="c67-fermion-tree"></span>

### 费米线两端的逆核差

运动学仍取式[（67.26）](#eq:c67-ex-1-kinematics)，
把$p,q$分别认作电子与正电子的动量。
与标量情形相比，费米子动能只含一阶导数，
最小耦合只产生$ie\gamma_\mu$顶角；
本过程在$e^2$阶由两种光子次序的树图组成。
以下保持它们从右侧入电子$u(p)$到左侧入正电子$\bar v(q)$的矩阵次序。

令$a=p-k=l-q$、$b=p-l=k-q$，
并取$\slashed r=r_\mu\gamma^\mu=-r^0\gamma^0+r^i\gamma^i$。
克利福德关系及自由传播核给出
<span id="eq:c67-ex-2-dirac-inverse"></span>

$$
\begin{aligned}
\{\gamma^\mu,\gamma^\nu\}&=-2g^{\mu\nu},
\qquad\slashed r^{\,2}=-r^2,\\
K(r)&=\slashed r+m,
\qquad N(r)=-\slashed r+m,\\
K(r)N(r)&=N(r)K(r)=(r^2+m^2)\mathbf1,
\\
S(r)&=\frac{N(r)}{r^2+m^2}.
\end{aligned}
\tag{67.33}
$$

这里$S$是传播核，实际内部费米线带$S/i=-iS$。
乘积恒等式来自$-\slashed r^{\,2}+m^2=r^2+m^2$；
$K(r),N(r)$都只含同一个$\slashed r$，因而这两个因子的次序可交换。
外旋量则满足
<span id="eq:c67-ex-2-external-dirac-equations"></span>

$$
K(p)u(p)=(\slashed p+m)u(p)=0,\qquad
\bar v(q)K(-q)=\bar v(q)(-\slashed q+m)=0 .
\tag{67.34}
$$

第一式等价于$\slashed p\,u=-mu$，第二式等价于
$\bar v\,\slashed q=m\bar v$；这两个质量号正好不同。

两个顶角与内线给$(ie)^2(-i)=ie^2$，
因此图之和$i\mathcal T$除去共同$i$后，振幅为
<span id="eq:c67-ex-2-source-amplitude"></span>

$$
\mathcal T=e^2\bar v(q)\left[
 \slashed\eta\,\frac{N(a)}{d_t}\slashed\epsilon
 +\slashed\epsilon\,\frac{N(b)}{d_u}\slashed\eta
 \right]u(p).
\tag{67.35}
$$

$N(a)=-\slashed p+\slashed k+m$与
$N(b)=-\slashed p+\slashed l+m$，
分别给出两种光子次序下的内部费米分子。
两个光子次序的交换没有交换费米外端，因此相对号为加号。

现在令$\epsilon=k$。在第一幅图中，$\slashed k$紧邻$u(p)$，
应使用$k=p-a$，把它写成$K(p)-K(a)$：
<span id="eq:c67-ex-2-right-end-contraction"></span>

$$
\begin{aligned}
N(a)\slashed k\,u
&=N(a)\,[K(p)-K(a)]u\\
&=-N(a)K(a)u=-d_t\,u .
\end{aligned}
\tag{67.36}
$$

从第一行到第二行使用了入电子的在壳狄拉克方程。
而在第二幅图中，$\slashed k$邻接左端$\bar v(q)$，
此时用$k=b+q$，即$\slashed k=K(b)-K(-q)$：
<span id="eq:c67-ex-2-left-end-contraction"></span>

$$
\begin{aligned}
\bar v\slashed k\,N(b)
&=\bar v\,[K(b)-K(-q)]N(b)\\
&=\bar v K(b)N(b)=d_u\,\bar v .
\end{aligned}
\tag{67.37}
$$

这里消去的是正电子外端的$K(-q)$。
两个内线分母于是分别被消掉，一端留下负号，另一端留下正号：
<span id="eq:c67-ex-2-amplitude-cancellation"></span>

$$
\mathcal T\big|_{\epsilon=k}
=e^2\left[-\bar v(q)\slashed\eta\,u(p)
           +\bar v(q)\slashed\eta\,u(p)\right]=0 .
\tag{67.38}
$$

整个计算保持了$\slashed\eta$与内部传播子分子的矩阵次序。
相消对每一组外费米自旋分别成立。

还可在夹上外旋量以前保留两端的逆核，看清零结果出现的条件。
定义$\mathcal T=\epsilon^\mu\eta^\nu\bar v A_{\mu\nu}u$，则
<span id="eq:c67-ex-2-open-matrix-identity"></span>

$$
\begin{aligned}
A_{\mu\nu}
&=e^2\left[\gamma_\nu S(a)\gamma_\mu
          +\gamma_\mu S(b)\gamma_\nu\right],\\
k^\mu A_{\mu\nu}
&=e^2\left[
 \gamma_\nu S(a)K(p)-K(-q)S(b)\gamma_\nu\right].
\end{aligned}
\tag{67.39}
$$

第二行由$S(a)[K(p)-K(a)]$与$[K(b)-K(-q)]S(b)$展开，
其中$-\gamma_\nu$与$+\gamma_\nu$先相消，余下的正是所示两端逆核。
只有再用式[（67.34）](#eq:c67-ex-2-external-dirac-equations)夹上在壳外旋量，
这两个矩阵项才消失。
由于式[（67.35）](#eq:c67-ex-2-source-amplitude)在
$(k,\epsilon)\leftrightarrow(l,\eta)$下交换两项，
第二条光子也满足同一关系：
<span id="eq:c67-ex-2-both-photons"></span>

$$
k^\mu\bar v(q)A_{\mu\nu}u(p)=0,\qquad
l^\nu\bar v(q)A_{\mu\nu}u(p)=0 .
\tag{67.40}
$$

这与标量完整张量的结果相同：纵向光子在带电线上产生相邻逆传播子的差，
内部部分经过图的求和相消，外端部分由物质粒子的在壳方程消去。

---

[← 第 66 节](/posts/srednicki-66/) · [章节地图](/srednicki/) · [第 68 节 →](/posts/srednicki-68/)
