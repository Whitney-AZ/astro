---
title: 'Srednicki §64 电子的磁矩'
date: 2026-09-14
category: 笔记
tags: [物理, 量子场论, Srednicki]
series: 'Srednicki QFT'
srednickiSections: [64]
hideFromHome: true
draft: false
---

<span id="c64"></span>

上一节求出的$F_2(0)=\alpha/(2\pi)+O(\alpha^2)$会改变电子在弱磁场中的能量。求出能量对磁场的一次响应，就能把这个顶角系数转化为磁矩。计算中既要保留顶角的新泡利项，也要保留原来最小耦合的贡献。后者虽然没有显式写出自旋矩阵，却会通过动量旋量的变化产生磁矩。

<span id="c64-matching"></span>

## 从形状因子写出磁场耦合

沿用$q=p'-p$及本书的$(-+++)$度规，上一节的在壳顶角为
<span id="eq:c64-vertex"></span>

$$
\begin{gathered}
\bar u'V^\mu(p',p)u
=e\bar u'\left[F_1(q^2)\gamma^\mu
       -\frac{i}{m}F_2(q^2)S^{\mu\nu}q_\nu\right]u,\\
S^{\mu\nu}=\frac i4[\gamma^\mu,\gamma^\nu].
\end{gathered}
\tag{64.1}
$$

我们关心的是匀强磁场的响应，所需转移动量趋于零。因此这里只用到
<span id="eq:c64-zero-form-factors"></span>

$$
F_1(0)=1,\qquad
F_2(0)=\frac{\alpha}{2\pi}+O(\alpha^2),\qquad
\alpha=\frac{e^2}{4\pi}.
\tag{64.2}
$$

第一式是物理电荷的归一条件，第二式才是圈计算给出的结果。为把这两个系数用于经典外场，可像第21节那样，用量子作用量的相应项来表示完整顶角。在含一对电子场和一个外光子的部分，选择
<span id="eq:c64-effective-interaction"></span>

$$
\Gamma_{\rm int}^{(1A)}
=\int d^4x\left[
 eF_1(0)\bar\Psi\gamma^\mu A_\mu\Psi
 +\frac{eF_2(0)}{2m}
        F_{\mu\nu}\bar\Psi S^{\mu\nu}\Psi
 \right]+\text{高阶转移项}.
\tag{64.3}
$$

这是在壳矩阵元的低转移匹配，乘外电子运动方程后消失的项不影响它。第63节先保持正的红外调节质量，使转移展开可以在零点进行。磁矩所需的系数由$F_1(0)$和有限的$F_2(0)$给出，求出后再去掉调节质量。

第二项的系数可直接核对。对入射光子的一个平面波分量，取
$A_\mu=\varepsilon_\mu^*e^{iqx}$，于是
<span id="eq:c64-pauli-vertex"></span>

$$
\begin{aligned}
F_{\mu\nu}
 &=i(q_\mu\varepsilon_\nu^*-q_\nu\varepsilon_\mu^*)e^{iqx},\\
\frac{eF_2(0)}{2m}F_{\mu\nu}S^{\mu\nu}
 &=\frac{ieF_2(0)}m q_\mu S^{\mu\nu}\varepsilon_\nu^*e^{iqx}\\
 &=-\frac{ieF_2(0)}m S^{\mu\nu}q_\nu\varepsilon_\mu^*e^{iqx}.
\end{aligned}
\tag{64.4}
$$

第一步用$S^{\mu\nu}=-S^{\nu\mu}$把两项合并，消去$1/2$；第二步交换哑指标，再使用反对称性，得到顶角中的负号。作用量在振幅中还要乘$i$，所以从这里读取的是$V^\mu$，相应顶角因子仍为$iV^\mu$。

现在取沿第三轴的匀强磁场，选择规范势
<span id="eq:c64-uniform-field"></span>

$$
\begin{gathered}
A_0=0,\qquad \mathbf A=(0,Bx,0),\qquad
F_{12}=-F_{21}=B,\\
\widetilde A_2(q)=iB(2\pi)^4\delta(q^0)\,
                         \partial_{q_1}\delta^3(\mathbf q),\\
\widetilde F_{12}(q)=B(2\pi)^4\delta(q^0)\delta^3(\mathbf q),
\qquad q^2\widetilde A_2(q)=0.
\end{gathered}
\tag{64.5}
$$

这里$x=x^1$，傅里叶变换采用$A_\mu(x)=\int d^4q\,e^{iqx}\widetilde A_\mu(q)/(2\pi)^4$。把$x$变成对$q_1$的导数便得到第二行，再用$q_1\partial_{q_1}\delta^3=-\delta^3$得到场强的第三行。$q^2$乘这个δ函数导数时，其零点值和一次导数都为零，故乘积为零；固定调节下含额外$q^2$的形状因子项因此不贡献匀强磁场响应。同时$F_{\mu\nu}S^{\mu\nu}=2BS^{12}$，其它场强分量均不参与。

<span id="c64-packet"></span>

## 归一化波包与磁矩的定义

为了得到有限范数的静止电子态，先按第38节不附加转动的推动约定选定$s=+$的旋量，再把动量集中在$\mathbf p=0$附近。记
<span id="eq:c64-normalized-packet"></span>

$$
\begin{aligned}
|e\rangle
 &=\int d\widetilde p\,f(\mathbf p)b_+^\dagger(\mathbf p)|0\rangle,\\
d\widetilde p&=\frac{d^3p}{(2\pi)^3\,2\omega_{\mathbf p}},
\qquad\omega_{\mathbf p}=\sqrt{m^2+\mathbf p^2},\\
\{b_+(\mathbf p'),b_+^\dagger(\mathbf p)\}
 &=(2\pi)^3\,2\omega_{\mathbf p}
                       \delta^3(\mathbf p'-\mathbf p),\\
\langle e|e\rangle
 &=\int d\widetilde p'\,d\widetilde p\,
 f^*(\mathbf p')f(\mathbf p)(2\pi)^3\,2\omega_{\mathbf p}
                       \delta^3(\mathbf p'-\mathbf p)\\
 &=\int d\widetilde p\,|f(\mathbf p)|^2=1.
\end{aligned}
\tag{64.6}
$$

δ函数消去一个动量积分时，其$2\omega$恰好与该积分的测度相消。选择径向函数$f(\mathbf p)=f(|\mathbf p|)$，轨道生成元$-i\mathbf p\times\nabla_{\mathbf p}$作用于包函数便为零；沿第三轴的角动量由所选自旋给出。

具体选择高斯波包。把归一常数记为$\mathcal N_a$，有
<span id="eq:c64-gaussian-width"></span>

$$
\begin{aligned}
f_a(\mathbf p)&=\mathcal N_a e^{-a^2\mathbf p^2/2},\\
\mathcal N_a^{-2}
 &=\int\frac{d^3p}{(2\pi)^3\,2\omega_{\mathbf p}}e^{-a^2\mathbf p^2}\\
 &=\frac{\pi^{3/2}}{(2\pi)^3\,2ma^3}
    \left[1-\frac{3}{4a^2m^2}+O((am)^{-4})\right],\\
\frac{\Delta p}{m}&\sim\frac1{am}\ll1,\qquad am\gg1.
\end{aligned}
\tag{64.7}
$$

这个展开用$1/\omega=m^{-1}[1-\mathbf p^2/(2m^2)+\cdots]$，再用
$\int d^3p\,e^{-a^2p^2}=\pi^{3/2}/a^3$及其对$a^2$的导数。对$x\ge0$，泰勒余项满足$0\le(1+x)^{-1/2}-1+x/2\le3x^2/8$；取$x=\mathbf p^2/m^2$后由下一高斯矩控制误差，因而大动量尾部不妨碍所写渐近阶次。
动量分布的宽度与$a$成反比，因此窄动量包要求$a\gg1/m$。

静磁场的两项耦合都不含新的费米场时间导数，所以线性相互作用哈密顿量由$-\mathcal L_{\rm int}$得到：
<span id="eq:c64-field-hamiltonian"></span>

$$
H_1=-eB\int d^3x\,
 \bar\Psi\left[x\gamma^2+\frac{F_2(0)}mS^{12}\right]\Psi.
\tag{64.8}
$$

令$\delta E$表示相对于真空的单电子能移。磁矩就是这个能移对磁场的一次响应：
<span id="eq:c64-moment-definition"></span>

$$
\delta E=\langle e|H_1|e\rangle=-\mu_z B,\qquad
\mu_z=-\left.\frac{\partial\,\delta E}{\partial B}\right|_{B=0}.
\tag{64.9}
$$

我们先对固定有限$a$的波包取这个导数，再取$am\to\infty$的静止极限。若把$B$看作小而有限的数，$|eB|a^2\ll1$是一组足够的弱场条件：在波包尺度上，磁场改变的动量$|eB|a$小于原来的动量宽度$1/a$。计算只保留关于$B$的一次项、非相对论展开的首项，以及形状因子的一圈修正。

<span id="c64-momentum-energy"></span>

## 空间坐标怎样变为旋量的动量导数

下面在$t=0$计算这个期望值。将自由场的平面波展开用于有效哈密顿量的树级矩阵元；圈修正已经包含在$F_2$中。取相对于真空正规序的局部双线性，电子的两个外算符分别与其中的$b^\dagger,b$相配，得到
<span id="eq:c64-connected-bilinear"></span>

$$
\begin{aligned}
&\langle0|b_+(\mathbf p'):\bar\Psi_\alpha(x)\Psi_\beta(x):
                         b_+^\dagger(\mathbf p)|0\rangle\\
&\qquad=\bar u_+(\mathbf p')_\alpha u_+(\mathbf p)_\beta
                      e^{i(p-p')x}.
\end{aligned}
\tag{64.10}
$$

每次收缩都给$(2\pi)^3\,2\omega\,\delta^3$，与相应场展开的测度相消，所以右边没有额外的$2\omega$。电子部分的算符次序是$b(\mathbf p')b^\dagger(\mathbf k')b(\mathbf k)b^\dagger(\mathbf p)$，两次收缩均取正号。正规序去掉真空收缩，留下这个连通单粒子矩阵元。

用两个包函数组合平面波态，就有
<span id="eq:c64-packet-energy"></span>

$$
\begin{aligned}
\delta E=-eB\int d\widetilde p\,d\widetilde p'\,d^3x\,
 &e^{i(\mathbf p-\mathbf p')\cdot\mathbf x}
 f^*(\mathbf p')\bar u_+(\mathbf p')\\
 &\times\left[x\gamma^2+\frac{F_2(0)}mS^{12}\right]
                 u_+(\mathbf p)f(\mathbf p).
\end{aligned}
\tag{64.11}
$$

泡利项不显含坐标，空间积分直接给δ函数。最小耦合项多一个$x$，可先写成动量导数：
<span id="eq:c64-fourier-derivative"></span>

$$
x\,e^{i(\mathbf p-\mathbf p')\cdot\mathbf x}
=-i\partial_{p_1}e^{i(\mathbf p-\mathbf p')\cdot\mathbf x}.
\tag{64.12}
$$

这个形式使用$t=0$；在一般时间，四维相位中的$\omega_{\mathbf p}t$也参与求导。选定零时刻的波包使所需的静磁响应计算最为直接。

分部积分时，导数不仅作用于$u_+f$，还要作用于$d\widetilde p$中的$1/(2\omega)$。将$\mathbf p$积分暂时写为普通勒贝格测度，便有
<span id="eq:c64-measure-derivative"></span>

$$
\begin{aligned}
&-i\int\frac{d^3p}{(2\pi)^3}\,
 \frac{u_+f}{2\omega}\,\partial_{p_1}
                         e^{i(\mathbf p-\mathbf p')\cdot\mathbf x}\\
&\qquad=i\int\frac{d^3p}{(2\pi)^3}\,
 e^{i(\mathbf p-\mathbf p')\cdot\mathbf x}
                    \partial_{p_1}\left(\frac{u_+f}{2\omega}\right),\\
\partial_{p_1}\left(\frac{u_+f}{2\omega}\right)
 &=\frac1{2\omega}
       \left(\partial_{p_1}-\frac{p_1}{\omega^2}\right)(u_+f).
\end{aligned}
\tag{64.13}
$$

高斯衰减使无穷远表面项为零。最后一行用了$\partial_{p_1}\omega=p_1/\omega$，因而$\partial_{p_1}\ln(1/2\omega)=-p_1/\omega^2$。

接着做空间积分，再用$(2\pi)^3\delta^3(\mathbf p-\mathbf p')$消去$p'$。这一次δ函数来自傅里叶积分，前面没有收缩产生的$2\omega'$，所以$p'$测度中的$1/(2\omega')$会留下来。完整的一动量式为
<span id="eq:c64-full-momentum-energy"></span>

$$
\delta E=-eB\int\frac{d\widetilde p}{2\omega}\,
 f^*\bar u_+
 \left[i\gamma^2\left(\partial_{p_1}-\frac{p_1}{\omega^2}\right)
                      +\frac{F_2(0)}mS^{12}\right](u_+f).
\tag{64.14}
$$

其中的测度导数项来自协变归一。对本节的径向波包，该项的积分恰好为零。利用$\bar u_+\gamma^2u_+=2p_2$，两个不对旋量求导的贡献分别正比于
<span id="eq:c64-radial-zero-terms"></span>

$$
\begin{aligned}
\int\frac{d\widetilde p}{2\omega}\,
       2ip_2 f^*\partial_{p_1}f&=0,\\
\int\frac{d\widetilde p}{2\omega}\,
       \left(-\frac{2ip_1p_2}{\omega^2}\right)|f|^2&=0.
\end{aligned}
\tag{64.15}
$$

径向$f$的导数带$p_1$，其余系数只依赖$p^2$；两行在反射$p_1\to-p_1$或$p_2\to-p_2$时都变号。因此余下的最小耦合贡献来自$\partial_{p_1}u_+$，这正是自旋磁矩从狄拉克耦合中出现的位置。

<span id="c64-rest-spin"></span>

## 静止旋量的变化给出狄拉克磁矩

第38节已用不附加转动的推动构造了动量旋量。现在只需这个推动在原点的一阶展开：
<span id="eq:c64-boost-expansion"></span>

$$
\begin{aligned}
u_s(\mathbf p)&=\exp(i\eta\hat{\mathbf p}\cdot\mathbf K)\,u_s(0),\\
K^j&=S^{j0}=\frac i2\gamma^j\gamma^0,\qquad
\eta=\operatorname{arsinh}(|\mathbf p|/m),\\
\eta\hat p_j&=\frac{p_j}{m}+O(|\mathbf p|^3/m^3),\\
u_s(\mathbf p)
 &=\left[1+\frac{i}{m}p_jK^j+O(\mathbf p^2/m^2)\right]u_s(0).
\end{aligned}
\tag{64.16}
$$

虽然$\hat{\mathbf p}$在原点没有确定方向，乘积$\eta\hat{\mathbf p}$在原点却有平滑的一阶展开，因而动量导数存在。对$p_1$求导，并用静止正能旋量的$\gamma^0u_s(0)=u_s(0)$，得到
<span id="eq:c64-rest-spinor-derivative"></span>

$$
\left.\partial_{p_1}u_+(\mathbf p)\right|_{\mathbf p=0}
=\frac{i}{m}K^1u_+(0)
=-\frac1{2m}\gamma^1\gamma^0u_+(0)
=-\frac1{2m}\gamma^1u_+(0).
\tag{64.17}
$$

代入最小耦合项，两个空间伽马的反对易关系给
<span id="eq:c64-minimal-spin-term"></span>

$$
\begin{aligned}
\left.\bar u_+i\gamma^2\partial_{p_1}u_+\right|_{\mathbf p=0}
 &=-\frac{i}{2m}\bar u_+(0)\gamma^2\gamma^1u_+(0)\\
 &=\frac{i}{2m}\bar u_+(0)\gamma^1\gamma^2u_+(0)\\
 &=\frac1m\bar u_+(0)S^{12}u_+(0).
\end{aligned}
\tag{64.18}
$$

所以狄拉克项与泡利项现在具有相同的自旋矩阵结构。前者的系数为1，后者的系数为$F_2(0)$；它们会相加。

对径向窄包，线性于$\mathbf p$的修正角积分为零，首个相对修正为$\langle\mathbf p^2\rangle/m^2=O((am)^{-2})$。同时，
<span id="eq:c64-packet-rest-limit"></span>

$$
\begin{aligned}
\int\frac{d\widetilde p}{2\omega}|f_a|^2
 &=\frac1{2m}\left[1+O((am)^{-2})\right],\\
\delta E
 &=-\frac{eB}{2m^2}[1+F_2(0)]
                     \bar u_+(0)S^{12}u_+(0)
       +O\left(\frac{|eB|}{m(am)^2}\right).
\end{aligned}
\tag{64.19}
$$

第一行保留原有的相对论归一$\int d\widetilde p\,|f_a|^2=1$，只对额外留下的$1/(2\omega)$作展开。这个额外因子使第二行的分母成为$2m^2$；该行按静止近似理解。

最后使用自旋本征值和旋量范数，
<span id="eq:c64-spin-energy"></span>

$$
\begin{aligned}
S^{12}u_\pm(0)&=\pm\frac12u_\pm(0),\qquad
\bar u_\pm(0)u_\pm(0)=2m,\\
\bar u_+(0)S^{12}u_+(0)&=m,\\
\delta E
 &=-\frac{eB}{2m}\left[1+\frac{\alpha}{2\pi}
                   +O(\alpha^2)+O((am)^{-2})\right].
\end{aligned}
\tag{64.20}
$$

依磁矩定义，并取静止极限，便得
<span id="eq:c64-magnetic-moment-g"></span>

$$
\begin{aligned}
\boldsymbol\mu&=g\,\frac e{2m}\,\mathbf S,\qquad
\mu_z=g\,\frac e{2m}\,\frac12,\\
g&=2[1+F_2(0)]
   =2\left[1+\frac{\alpha}{2\pi}+O(\alpha^2)\right],\\
a_e:=\frac{g-2}{2}&=F_2(0).
\end{aligned}
\tag{64.21}
$$

这里$a_e$称反常磁矩的无量纲系数，区别于波包的长度$a$。最小狄拉克耦合给$g=2$，一圈泡利项给第一个偏离2的修正。由于$e<0$，自旋向上态的$\mu_z$为负，磁矩与自旋反向；沿正第三轴加磁场时，该态的能量升高。这里的$e/(2m)$带电荷符号；用作正单位的玻尔磁子大小为$\mu_B=|e|/(2m)$。

还可用经典带电旋转小球来比较这个结果。若电荷密度和质量密度处处成同一比例$\rho_e=(e/m)\rho_m$，并且两者具有同一个速度场$\mathbf v$，则
<span id="eq:c64-classical-orbital"></span>

$$
\boldsymbol\mu_{\rm cl}
 =\frac12\int d^3x\,\mathbf r\times(\rho_e\mathbf v)
 =\frac e{2m}\int d^3x\,\mathbf r\times(\rho_m\mathbf v)
 =\frac e{2m}\mathbf L.
\tag{64.22}
$$

经典轨道运动的系数因而对应$g_L=1$。电子自旋的狄拉克值是它的两倍，这个差别由式[（64.18）](#eq:c64-minimal-spin-term)的旋量计算得出。[下文](#c64-orbital-packet)给波包加上球谐角向依赖，直接从同一个哈密顿量求出轨道磁矩与自旋磁矩的和。

<span id="c64-finite-width"></span>

## 有限宽度波包的静止极限

还可以在式[（64.8）](#eq:c64-field-hamiltonian)所取的两项中保留全部波包动量，检查前面的非相对论近似怎样成立。为方便写分量，暂把第38节的外尔矩阵作一个常数酉变换：
<span id="eq:c64-dirac-basis"></span>

$$
T=\frac1{\sqrt2}\begin{pmatrix}I_2&I_2\\-I_2&I_2\end{pmatrix},
\qquad u_D=Tu_W,\qquad
\gamma_D^\mu=T\gamma_W^\mu T^\dagger.
\tag{64.23}
$$

于是$\gamma_D^0=\operatorname{diag}(I_2,-I_2)$，
$\gamma_D^i=\left(\begin{smallmatrix}0&\sigma_i\\-\sigma_i&0\end{smallmatrix}\right)$。
这是同一克利福德代数的另一组矩阵；所有双线性都保持原值，以下略去下标$D$。
对$\chi=(1,0)^T$，式[（64.16）](#eq:c64-boost-expansion)的完整推动可写为
<span id="eq:c64-explicit-spinor"></span>

$$
u_+(\mathbf p)=\sqrt{\omega+m}
 \begin{pmatrix}\chi\\ \dfrac{\boldsymbol\sigma\cdot\mathbf p}{\omega+m}\chi\end{pmatrix},
\qquad
S^{12}=\frac12\begin{pmatrix}\sigma_3&0\\0&\sigma_3\end{pmatrix}.
\tag{64.24}
$$

这由$\cosh(\eta/2)=\sqrt{(\omega+m)/(2m)}$和
$\sinh(\eta/2)=|\mathbf p|/\sqrt{2m(\omega+m)}$代入推动矩阵得到。泡利项的双线性为
<span id="eq:c64-pauli-bilinear"></span>

$$
\begin{aligned}
\bar u_+S^{12}u_+
 &=\frac{\omega+m}{2}
 \left[1-\frac{\chi^\dagger(\boldsymbol\sigma\cdot\mathbf p)
                    \sigma_3(\boldsymbol\sigma\cdot\mathbf p)\chi}
                   {(\omega+m)^2}\right]\\
 &=\frac{\omega+m}{2}
       -\frac{2p_3^2-\mathbf p^2}{2(\omega+m)}
 =\omega-\frac{p_3^2}{\omega+m}.
\end{aligned}
\tag{64.25}
$$

第二行用$(\boldsymbol\sigma\cdot\mathbf p)\sigma_3
(\boldsymbol\sigma\cdot\mathbf p)
=2p_3(\boldsymbol\sigma\cdot\mathbf p)-\mathbf p^2\sigma_3$，
并代入$\chi^\dagger\boldsymbol\sigma\chi=(0,0,1)$。

最小耦合项中的导数也可直接求出。记$n=\sqrt{\omega+m}$、
$R=\boldsymbol\sigma\cdot\mathbf p/(\omega+m)$，则
$\partial_1n=p_1/(2\omega n)$，
$\partial_1R=\sigma_1/(\omega+m)
 -p_1\boldsymbol\sigma\cdot\mathbf p/[\omega(\omega+m)^2]$。
按上下两个块相乘，有
<span id="eq:c64-derivative-bilinear"></span>

$$
\begin{aligned}
\bar u_+i\gamma^2\partial_{p_1}u_+
 &=n(\partial_1n)\chi^\dagger(i\sigma_2R+Ri\sigma_2)\chi\\
 &\quad+n^2\chi^\dagger i\sigma_2(\partial_1R)\chi\\
 &=\frac{ip_1p_2}{\omega(\omega+m)}
      +1-\frac{p_1(p_1+ip_2)}{\omega(\omega+m)}\\
 &=1-\frac{p_1^2}{\omega(\omega+m)}.
\end{aligned}
\tag{64.26}
$$

这里$\{\sigma_2,\boldsymbol\sigma\cdot\mathbf p\}=2p_2I$、
$\chi^\dagger i\sigma_2\sigma_1\chi=1$，
而$\chi^\dagger i\sigma_2(\boldsymbol\sigma\cdot\mathbf p)\chi=p_1+ip_2$。
虚部在两种导数之间消去，静止点的值正好为1。

定义径向包的平均$\langle h(\omega)\rangle_f=\int d\widetilde p\,|f|^2h(\omega)$。
对球面作角平均时$p_1^2$、$p_3^2$均变成$\mathbf p^2/3$，
再用$\mathbf p^2/(\omega+m)=\omega-m$。式[（64.14）](#eq:c64-full-momentum-energy)于是给
<span id="eq:c64-finite-packet"></span>

$$
\mu_z(f)=\frac e{2m}\left[
 \left\langle\frac{m(2\omega+m)}{3\omega^2}\right\rangle_f
 +F_2(0)\left\langle\frac{2\omega+m}{3\omega}\right\rangle_f
 \right].
\tag{64.27}
$$

两个平均在静止极限都趋于1。展开$\omega/m=\sqrt{1+\mathbf p^2/m^2}$，得到
<span id="eq:c64-finite-width-expansion"></span>

$$
\begin{aligned}
\frac{\mu_z(f)}{e/(2m)}
 &=1+F_2(0)
   -\left[\frac23+\frac{F_2(0)}6\right]
                    \frac{\langle\mathbf p^2\rangle_f}{m^2}
   +O(\langle\mathbf p^4\rangle_f/m^4),\\
\frac{\langle\mathbf p^2\rangle_{f_a}}{m^2}
 &=\frac{3}{2(am)^2}+O((am)^{-4}),\\
\frac{\mu_z(f_a)}{e/(2m)}
 &=1+F_2(0)-\frac{1+F_2(0)/4}{(am)^2}+O((am)^{-4}).
\end{aligned}
\tag{64.28}
$$

最后两行在同一个相对论归一中取高斯平均，故归一常数的修正也已经包含。这个例子把式[（64.19）](#eq:c64-packet-rest-limit)的误差阶具体算出；先前抽取的静止磁矩与波包长度无关。

<span id="c64-experimental-context"></span>

顶角计算给出了自旋能级劈裂的量子修正。实验从磁场中的能级差测定同一个$g$因子，便可检验$F_2(0)$的圈展开。

<span id="c64-orbital-packet"></span>

## 球谐波包的轨道磁矩

前面选择没有轨道角动量的径向波包，
用来分离电子自旋的磁矩；现在给同一波包乘上球谐函数，
考察由角向相位产生的额外响应。质量仍记为$m$，
球谐函数的磁量子数改记为$m_\ell$，避免两个$m$混用。

### 球谐波包的归一

取静止自旋标签$s=+$的单电子态，并以任意动量的无转动推动旋量构造波包。记
$E_{\mathbf p}=\sqrt{m^2+\mathbf p^2}$，则
<span id="eq:c64-ex-1-state-normalization"></span>

$$
\begin{aligned}
|\Phi\rangle
 &=\int d\widetilde p\,f(\mathbf p)b_+^\dagger(\mathbf p)|0\rangle,\\
d\widetilde p&=\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}},\\
\langle\mathbf p',s'|\mathbf p,s\rangle
 &=(2\pi)^3\,2E_{\mathbf p}\,
       \delta^3(\mathbf p'-\mathbf p)\delta_{s's},\\
1&=\int d\widetilde p\,|f(\mathbf p)|^2.
\end{aligned}
\tag{64.29}
$$

态内积中的δ函数消去一重动量积分，正好给出最后的归一条件。
这个波包和球谐函数的归一取为
<span id="eq:c64-ex-1-spherical-packet"></span>

$$
f(\mathbf p)=\mathcal N e^{-a^2r^2/2}Y_{\ell m_\ell}(\theta,\phi),
\qquad r=|\mathbf p|,\qquad
\int d\Omega\,|Y_{\ell m_\ell}|^2=1.
\tag{64.30}
$$

这里$\ell$为非负整数，$-\ell\le m_\ell\le\ell$。
径向分布的动量宽度为$1/a$，所以前面要求的窄动量包应满足
$am\gg1$，并以$\delta=(am)^{-1}$作为非相对论展开参数。

角积分已经归一，故$\mathcal N$由一个径向积分固定：
<span id="eq:c64-ex-1-exact-radial-normalization"></span>

$$
|\mathcal N|^{-2}
 =\frac1{(2\pi)^3}\int_0^\infty
   \frac{r^2e^{-a^2r^2}}{2\sqrt{m^2+r^2}}\,dr.
\tag{64.31}
$$

这个式子保留完整的协变测度。为把它评价到这次计算所需的精度，
对$\int_0^\infty e^{-a^2r^2}dr=\sqrt\pi/(2a)$按$a^2$求导，
得到下面两个高斯矩；再展开$1/E_{\mathbf p}$：
<span id="eq:c64-ex-1-nr-normalization"></span>

$$
\begin{aligned}
\int_0^\infty r^2e^{-a^2r^2}dr&=\frac{\sqrt\pi}{4a^3},&
\int_0^\infty r^4e^{-a^2r^2}dr&=\frac{3\sqrt\pi}{8a^5},\\
\int_0^\infty\frac{r^2e^{-a^2r^2}}{2E_{\mathbf p}}dr
 &=\frac{\sqrt\pi}{8ma^3}
       \left[1-\frac34\delta^2+O(\delta^4)\right],\\
|\mathcal N|^2
 &=\frac{8ma^3(2\pi)^3}{\sqrt\pi}
       \left[1+\frac34\delta^2+O(\delta^4)\right].
\end{aligned}
\tag{64.32}
$$

于是$f$的质量维数为$-1$，与$d\widetilde p$的维数2相配。
下面先保持式[（64.31）](#eq:c64-ex-1-exact-radial-normalization)的精确归一，
最后才对磁矩作非相对论展开。

绕$z$轴旋转时，动量测度中的$E_{\mathbf p}$不变。
将$f(R_z^{-1}\mathbf p)$对旋转角展开，便得到作用在标量包络上的
轨道角动量算符
<span id="eq:c64-ex-1-momentum-angular-momentum"></span>

$$
L_z=-i\left(p_1\partial_{p_2}-p_2\partial_{p_1}\right)
    =-i\partial_\phi,\qquad
L_zf=m_\ell f,\qquad
\langle L_z\rangle=m_\ell.
\tag{64.33}
$$

径向测度不随$\phi$变化，所以这里的$L_z$与通常的平直动量测度有同一形式。
最后一个等式使用了波包归一。

### 包络角向导数的贡献

选择$A_2=Bx$、其余分量为零。只取能量对$B$的一次响应，
并以相同真空的能量为基准，含泡利形状因子的相互作用哈密顿量为
<span id="eq:c64-ex-1-magnetic-response"></span>

$$
\begin{aligned}
H_1&=-eB\int d^3x\,
 \bar\Psi\left[x\gamma^2+\frac{F_2(0)}mS^{12}\right]\Psi,
\\
\Delta E&=\langle H_1\rangle,\qquad
\mu_z=-\frac{\Delta E}{B}.
\end{aligned}
\tag{64.34}
$$

这里$F_1(0)=1$已经固定电荷归一，$e<0$。
按前面使用单电子连通矩阵元，选$t=0$作为波包的参考时刻，
$x\gamma^2$项给出
<span id="eq:c64-ex-1-before-integration-by-parts"></span>

$$
\begin{aligned}
\Delta E_{\rm min}
 ={}&-eB\int d\widetilde p\,d\widetilde p'\,d^3x\,
 e^{i(\mathbf p-\mathbf p')\cdot\mathbf x}\\
 &\hspace{1em}\times
 f^*(\mathbf p')\bar u_+(\mathbf p')\,
 x\gamma^2u_+(\mathbf p)f(\mathbf p).
\end{aligned}
\tag{64.35}
$$

在这个积分中，包络的角向依赖将产生新的贡献。
用$x e^{i(\mathbf p-\mathbf p')\cdot\mathbf x}
=-i\partial_{p_1}e^{i(\mathbf p-\mathbf p')\cdot\mathbf x}$分部积分时，
导数也必须作用在$d\widetilde p$的$1/(2E_{\mathbf p})$上。
若将这个权重记为$w(\mathbf p)=1/[(2\pi)^3\,2E_{\mathbf p}]$，
则完整的导数为
<span id="eq:c64-ex-1-weighted-derivative"></span>

$$
\begin{aligned}
\partial_{p_1}\log w&=-\frac{p_1}{E_{\mathbf p}^2},\\
D_1(uf)
 &:=w^{-1}\partial_{p_1}(wuf)
   =\partial_{p_1}(uf)-\frac{p_1}{E_{\mathbf p}^2}uf.
\end{aligned}
\tag{64.36}
$$

分部积分给出的系数是$+iD_1$。随后空间积分产生
$(2\pi)^3\delta^3(\mathbf p'-\mathbf p)$，而对$d\widetilde p'$积分还留下
$1/(2E_{\mathbf p})$，所以含泡利项的完整结果为
<span id="eq:c64-ex-1-after-integration-by-parts"></span>

$$
\Delta E=-eB\int\frac{d\widetilde p}{2E_{\mathbf p}}\,
 f^*\bar u_+
 \left[i\gamma^2D_1(u_+f)
       +\frac{F_2(0)}mS^{12}u_+f\right].
\tag{64.37}
$$

这里的$D_1$只作用在括号内的$u_+f$上。
下面将分别计算旋量导数、包络导数和测度导数，说明最后一项在这个波包中的积分为何恰好为零。

高斯因子使无穷远的表面项消失。对于$\ell>0$，
$Y_{\ell m_\ell}(\widehat{\mathbf p})$在$\mathbf p=0$可能没有方向无关的极限，
但这不妨碍上述一次分部积分：先挖去半径$\eta$的小球，
其表面项因$f,u_+,w$有界而为$O(\eta^2)$；角向导数至多为$O(1/r)$，
在三维中局部可积，且
$\int_{r<\eta}d^3p\,|\nabla f|^2=O(\eta)$。
令$\eta\to0$，便得到同一弱导数公式。单点处给$f$选择什么值不影响积分。

将$D_1(u_+f)$拆成旋量导数和包络导数。后者连同测度导数定义这次计算的轨道贡献。
使用同动量旋量恒等式$\bar u_+\gamma^2u_+=2p_2$，得到
<span id="eq:c64-ex-1-orbital-two-terms"></span>

$$
\begin{aligned}
\Delta E_{\rm orb}
 ={}&-eB\int d\widetilde p\,
       \frac{ip_2}{E_{\mathbf p}}f^*\partial_{p_1}f\\
 &+ieB\int d\widetilde p\,
       \frac{p_1p_2}{E_{\mathbf p}^3}|f|^2.
\end{aligned}
\tag{64.38}
$$

对这个球谐函数，$|Y_{\ell m_\ell}|^2$与方位角$\phi$无关。
第二行的$p_1p_2=r^2\sin^2\theta\cos\phi\sin\phi$在$\phi$上积分为零；
测度导数项在方位角积分后消失。

### 朗道规范中的轨道磁矩

剩下的第一行表面上只含$p_2\partial_{p_1}$，并非完整的$L_z$。
这个差别来自$A_2=Bx$所选的朗道规范。写
$Y_{\ell m_\ell}=\Theta_{\ell m_\ell}(\theta)e^{im_\ell\phi}$，
其中$\Theta_{\ell m_\ell}$可取实函数，动量导数为
<span id="eq:c64-ex-1-cartesian-angular-derivative"></span>

$$
\partial_{p_1}
 =\sin\theta\cos\phi\,\partial_r
  +\frac{\cos\theta\cos\phi}{r}\partial_\theta
  -\frac{\sin\phi}{r\sin\theta}\partial_\phi.
\tag{64.39}
$$

前两项乘上$ip_2 f^*$后均带$\sin\phi\cos\phi$，方位角积分为零。
最后一项作用在$e^{im_\ell\phi}$上，给
$ip_2[-im_\ell\sin\phi/(r\sin\theta)]|f|^2
=m_\ell\sin^2\phi\,|f|^2$。
因$\sin^2\phi$的方位角平均为$1/2$，便有
<span id="eq:c64-ex-1-landau-half"></span>

$$
\begin{aligned}
\int d\widetilde p\,\frac{ip_2}{E_{\mathbf p}}
            f^*\partial_{p_1}f
 &=\frac{m_\ell}{2}\int d\widetilde p\,
              \frac{|f|^2}{E_{\mathbf p}}
 \\&=\frac12\left\langle\frac{L_z}{E_{\mathbf p}}\right\rangle .
\end{aligned}
\tag{64.40}
$$

这就是所需的二分之一。若改用对称规范
$\mathbf A=(-By/2,Bx/2,0)$，两项分别给
$ip_2\partial_{p_1}$与$-ip_1\partial_{p_2}$，在哈密顿量中直接合成$L_z/2$；
这次计算的轴对称波包使两种写法的能量期望一致。

于是轨道磁矩在尚未作窄包展开时为
<span id="eq:c64-ex-1-exact-orbital-moment"></span>

$$
\begin{aligned}
\Delta E_{\rm orb}
 &=-\frac{eB\,m_\ell}{2}\left\langle E_{\mathbf p}^{-1}\right\rangle,\\
\mu_{{\rm orb},z}
 &=\frac{e\,m_\ell}{2}\left\langle E_{\mathbf p}^{-1}\right\rangle.
\end{aligned}
\tag{64.41}
$$

这里的轨道部分是相对于本书固定静止自旋基的包络角动量而言；
旋量随动量变化所给的部分仍保留在式
[（64.37）](#eq:c64-ex-1-after-integration-by-parts)中。
归一常数在这个径向期望中抵消，因而可直接评价为
<span id="eq:c64-ex-1-inverse-energy-average"></span>

$$
\begin{aligned}
\left\langle E_{\mathbf p}^{-1}\right\rangle
 &=\frac{\displaystyle\int_0^\infty
       \frac{r^2e^{-a^2r^2}}{2(m^2+r^2)}\,dr}
        {\displaystyle\int_0^\infty
       \frac{r^2e^{-a^2r^2}}{2\sqrt{m^2+r^2}}\,dr}\\
 &=\frac1m
   \frac{1-\frac32\delta^2+O(\delta^4)}
        {1-\frac34\delta^2+O(\delta^4)}
  =\frac1m\left[1-\frac34\delta^2+O(\delta^4)\right].
\end{aligned}
\tag{64.42}
$$

分子使用$1/E^2=m^{-2}(1-r^2/m^2+\cdots)$，
分母已在式[（64.32）](#eq:c64-ex-1-nr-normalization)中评价。
泰勒余项在$x\ge0$时满足
$0\le(1+x)^{-1/2}-1+x/2\le3x^2/8$及
$0\le(1+x)^{-1}-1+x\le x^2$。
令$x=r^2/m^2$，下一阶高斯矩便控制了上式的$O(\delta^4)$误差。
这里保持$\ell,m_\ell$固定，归一角积分不随$a$改变。
最终得到
<span id="eq:c64-ex-1-orbital-answer"></span>

$$
\begin{aligned}
\mu_{{\rm orb},z}
 &=\frac{e\,m_\ell}{2m}
       \left[1-\frac{3}{4(am)^2}+O((am)^{-4})\right],\\
\boldsymbol\mu_{\rm orb}
 &=\frac{e}{2m}\langle\mathbf L\rangle
 \qquad\text{在非相对论主阶}.
\end{aligned}
\tag{64.43}
$$

球谐态有$\langle L_x\rangle=\langle L_y\rangle=0$，
所以第二行在这次计算中只含$z$分量。
当$m_\ell=0$时，轨道项已由式[（64.41）](#eq:c64-ex-1-exact-orbital-moment)精确为零。
由于$e<0$，正的轨道角动量投影对应负的磁矩投影，
其能量在$B>0$时增加。

最后把轨道结果与前面的自旋部分放在一起。
在$\mathbf p=0$处，本书固定相位的旋量满足
<span id="eq:c64-ex-1-spin-leading-bilinears"></span>

$$
\begin{aligned}
\left.\partial_{p_1}u_+(\mathbf p)\right|_0
 &=-\frac1{2m}\gamma^1u_+(0),\\
\left.\bar u_+i\gamma^2\partial_{p_1}u_+\right|_0
 &=\frac1m\bar u_+(0)S^{12}u_+(0)=1,\\
\bar u_+(0)S^{12}u_+(0)&=m.
\end{aligned}
\tag{64.44}
$$

第二行由$S^{12}u_+(0)=u_+(0)/2$和$\bar u_+(0)u_+(0)=2m$得到。
因此式[（64.37）](#eq:c64-ex-1-after-integration-by-parts)中的旋量导数与泡利项，
在非相对论主阶分别给$e/(2m)$与$eF_2(0)/(2m)$。
归一角密度不改变这两个静止值，故
<span id="eq:c64-ex-1-orbital-plus-spin"></span>

$$
\begin{aligned}
\mu_z
 &=\frac{e}{2m}\left[m_\ell+1+F_2(0)\right]
       +O\!\left(\frac{|e|}{m}(am)^{-2}\right)\\
 &=\frac{e}{2m}
      \left[m_\ell+1+\frac{\alpha}{2\pi}+O(\alpha^2)\right]
       +O\!\left(\frac{|e|}{m}(am)^{-2}\right).
\end{aligned}
\tag{64.45}
$$

此处宽度误差按固定$\ell,m_\ell$计，自旋部分尚未展开到该阶；
式[（64.43）](#eq:c64-ex-1-orbital-answer)中额外给出的宽度修正只属于轨道项。
用角动量系数表示，轨道因子为$g_L=1$，而自旋因子为
$g_s=2[1+F_2(0)]$、$\langle S_z\rangle=1/2$。
轨道响应的主阶系数由物理电荷归一$F_1(0)=1$固定，
反常磁矩则出现在自旋的系数中。

---

[← 第 63 节](/posts/srednicki-63/) · [章节地图](/srednicki/) · [第 65 节 →](/posts/srednicki-65/)
