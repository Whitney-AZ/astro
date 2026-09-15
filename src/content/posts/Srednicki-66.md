---
title: 'Srednicki §66 量子电动力学中的贝塔函数'
date: 2026-09-14
category: 笔记
tags: [物理, 量子场论, Srednicki]
series: 'Srednicki QFT'
srednickiSections: [66]
hideFromHome: true
draft: false
---

<span id="c66"></span>

前面的圈图已经给出电磁顶角和传播子的紫外极点。固定裸作用量，对裸电荷与重整化电荷的关系作尺度微分，就能由这些极点求出电荷的运行。计算沿用第28、52节的方法。旋量电动力学只有一个电磁耦合；在标量电动力学中，电荷和四次耦合还会共同进入同一个反项，因此后半节要同时对两个变量求导。

以下使用$\overline{\mathrm{MS}}$方案，$d=4-\varepsilon$，$\mu^2=4\pi e^{-\gamma_E}\widetilde\mu^2$；令$t=\ln\mu$，所有尺度微分均在固定裸参数和$\varepsilon$时进行。电荷继续取第58、61节的负支$e<0$。求运行时较方便的正变量是精细结构常数$\alpha=e^2/(4\pi)$。

<span id="c66-dirac"></span>

## 旋量电动力学：从裸电荷到简单极点

先把三个场的归一因子从相互作用中取出。裸场与重整化场的关系是
<span id="eq:c66-dirac-bare-fields"></span>

$$
\begin{gathered}
\Psi_0=Z_2^{1/2}\Psi,\qquad
\bar\Psi_0=Z_2^{1/2}\bar\Psi,\qquad
A_{0\mu}=Z_3^{1/2}A_\mu,\\
e_0\bar\Psi_0\gamma^\mu\Psi_0A_{0\mu}
 =e_0Z_2Z_3^{1/2}\bar\Psi\gamma^\mu\Psi A_\mu .
\end{gathered}
\tag{66.1}
$$

另一方面，第62节拉格朗日量中这一项的系数为$Z_1e\widetilde\mu^{\varepsilon/2}$。比较两个系数，得到裸电荷关系：
<span id="eq:c66-dirac-bare-charge"></span>

$$
e_0Z_2Z_3^{1/2}=Z_1e\widetilde\mu^{\varepsilon/2},
\qquad
e_0=\widetilde\mu^{\varepsilon/2}
            e\frac{Z_1}{Z_2\sqrt{Z_3}}.
\tag{66.2}
$$

两条旋量腿各给一个平方根，所以最后是$Z_2^{-1}$；光子只有一条，给$Z_3^{-1/2}$。电荷的工程质量维数为$\varepsilon/2$，正是尺度因子的幂。将此式平方并除以$4\pi$，便可改用正的裸参数：
<span id="eq:c66-alpha-bare"></span>

$$
\alpha=\frac{e^2}{4\pi},\qquad
\alpha_0=\frac{e_0^2}{4\pi}
 =\widetilde\mu^\varepsilon\alpha\,
                  Z_3^{-1}Z_2^{-2}Z_1^2 .
\tag{66.3}
$$

现在代入第62节费曼规范的极部。该节先给出一般圈函数，再讨论OS有限减除；本节只保留$\overline{\mathrm{MS}}$所需的极点，得到
<span id="eq:c66-dirac-z"></span>

$$
\begin{aligned}
Z_1&=1-\frac{\alpha}{2\pi\varepsilon}+O(\alpha^2),\\
Z_2&=1-\frac{\alpha}{2\pi\varepsilon}+O(\alpha^2),\\
Z_3&=1-\frac{2\alpha}{3\pi\varepsilon}+O(\alpha^2).
\end{aligned}
\tag{66.4}
$$

$O(\alpha^2)$表示更高圈反项，还可以包含更高次极点。把它们的乘积取对数后，极点级数写得最为直接。为与本节后面的裸$e$对数区别，给这里的系数加上上标$(\alpha)$：
<span id="eq:c66-alpha-log"></span>

$$
\begin{aligned}
\ln\!\left(Z_3^{-1}Z_2^{-2}Z_1^2\right)
 &=\sum_{n\ge1}\frac{E_n^{(\alpha)}(\alpha)}{\varepsilon^n},\\
\ln\alpha_0
 &=\ln\alpha+\varepsilon\ln\widetilde\mu
      +\sum_{n\ge1}\frac{E_n^{(\alpha)}(\alpha)}{\varepsilon^n},\\
E_1^{(\alpha)}(\alpha)
 &=\frac{2\alpha}{3\pi}
     +\frac{\alpha}{\pi}-\frac{\alpha}{\pi}
     +O(\alpha^2)
 =\frac{2\alpha}{3\pi}+O(\alpha^2).
\end{aligned}
\tag{66.5}
$$

最后一行依次来自$-\ln Z_3$、$-2\ln Z_2$和$2\ln Z_1$。顶角与旋量场的贡献已经相消，剩下光子场的归一。对有量纲的裸量取对数时，可先除以固定的单位；这个单位对下面的微分没有影响。

为了说明简单极点怎样决定有限的贝塔函数，记
<span id="eq:c66-regulated-alpha"></span>

$$
B_\alpha:=\frac{d\alpha}{dt}
       =-\varepsilon\alpha+\beta_\alpha(\alpha).
\tag{66.6}
$$

第一项是$d$维工程量纲，第二项是四维量子运行。这个分离已在[第52节](/posts/srednicki-52/#eq:c52-regulated-beta)从纯极点关系的逆矩阵和有限性要求推出；这里只有一个变量。对式[（66.5）](#eq:c66-alpha-log)求导，先保留完整的$B_\alpha$，有
<span id="eq:c66-alpha-laurent"></span>

$$
\begin{aligned}
0&=\varepsilon+\frac{B_\alpha}{\alpha}
       +B_\alpha\sum_{n\ge1}
             \frac{E_n^{(\alpha)\prime}}{\varepsilon^n}\\
 &=\frac{\beta_\alpha}{\alpha}
        -\alpha E_1^{(\alpha)\prime}
   +\sum_{n\ge1}\frac{
      \beta_\alpha E_n^{(\alpha)\prime}
          -\alpha E_{n+1}^{(\alpha)\prime}}{\varepsilon^n}.
\end{aligned}
\tag{66.7}
$$

撇号表示对$\alpha$求导。第一行的$\varepsilon$与$B_\alpha/\alpha$中的工程项消去；工程项乘简单极点留下第二行的$-\alpha E_1'$。其余工程项把极点次数降低一阶，于是下标变为$n+1$。逐阶有限要求负幂的系数相消，而有限部分给
<span id="eq:c66-dirac-beta"></span>

$$
\beta_\alpha=\alpha^2E_1^{(\alpha)\prime}
       =\frac{2\alpha^2}{3\pi}+O(\alpha^3).
\tag{66.8}
$$

若在求导前就将$\varepsilon$设为零，恰好会丢掉产生这个有限结果的工程项。

改回电荷变量只须使用链式法则：
<span id="eq:c66-charge-chain"></span>

$$
\beta_\alpha=\frac{e}{2\pi}\beta_e,
\qquad
\beta_e=\frac{2\pi}{e}\frac{2}{3\pi}
                  \left(\frac{e^2}{4\pi}\right)^2
        =\frac{e^3}{12\pi^2}+O(e^5).
\tag{66.9}
$$

在$e<0$支上，$\beta_e$为负，电荷向更负的方向变化；同时$\alpha$与$|e|$增大。因此用$\alpha$或电荷大小表述物理结论最为直接：电磁相互作用随能标升高而增强。

<span id="c66-species"></span>

## 多种电荷与同一个运行耦合

若有$N$个狄拉克场，第$i$种场的电荷为$Q_i e$，其场和顶角归一分别记为$Z_{2i}$、$Z_{1i}$。一圈电子自能和顶角修正都含两个额外电磁顶角，故只需在式[（66.4）](#eq:c66-dirac-z)中作$\alpha\mapsto Q_i^2\alpha$。光子自能的圈则可以由任一种带电场构成，不同物种的中间态相互独立，因而圈贡献直接相加：
<span id="eq:c66-dirac-species"></span>

$$
\begin{aligned}
Z_{1i}&=Z_{2i}
 =1-\frac{Q_i^2\alpha}{2\pi\varepsilon}+O(\alpha^2),\qquad
\frac{Z_{1i}}{Z_{2i}}=1+O(\alpha^2),\\
Z_3&=1-\frac{2\alpha}{3\pi\varepsilon}
                     \sum_{i=1}^NQ_i^2+O(\alpha^2),\\
\beta_e&=\frac{e^3}{12\pi^2}\sum_{i=1}^NQ_i^2+O(e^5).
\end{aligned}
\tag{66.10}
$$

相反电荷在这里同号相加，因为光子二点图含两个电磁顶角。一个狄拉克场的粒子和反粒子已包含在同一个圈中，不另计为两个狄拉克物种；颜色等独立内部标签则各给一份。

动能与顶角反项之间的关系可以从已经证明的局域核恒等式推出。在保持这一沃德关系的减除中，把重整化场的局域相位系数取为$Q_i e$，并像第65节一样从三点顶角提出公共$\widetilde\mu^{\varepsilon/2}$，则
<span id="eq:c66-ward-counterterms"></span>

$$
\begin{aligned}
q_\mu V_i^\mu(p+q,p)
 &=Q_i e\,[\mathcal K_i(p+q)-\mathcal K_i(p)],\\
V_{i,\mathrm{ct}}^\mu&=Q_i e\,\delta Z_{1i}\gamma^\mu,\qquad
\mathcal K_{i,\mathrm{ct}}(p)
   =\delta Z_{2i}\slashed p+\delta Z_{mi}m_i,\\
Q_i e\,\delta Z_{1i}\slashed q
 &=Q_i e\,\delta Z_{2i}\slashed q .
\end{aligned}
\tag{66.11}
$$

最后一行取每阶局部极点部分，质量反项在差分中消去。对非零电荷，它强制相应动能和顶角的反项系数相等。逐阶保持相同的沃德电荷定义，便可把该等式用于纯极点方案的所有阶。中性场的电磁顶角本来消失，也不贡献式[（66.10）](#eq:c66-dirac-species)的和。这段说明使用第63节已给出的变元证明；当前一圈结果本身只需要前一式列出的三个极部。

运行的物理意义还可由积分式看出。设一段能区内所保留的带电物种不变，记$C_D=\sum_iQ_i^2$。一圈近似给
<span id="eq:c66-one-loop-flow"></span>

$$
\begin{aligned}
\frac{d}{dt}\frac1\alpha
 &=-\frac{2C_D}{3\pi},\\
\frac1{\alpha(\mu)}
 &=\frac1{\alpha(\mu_0)}
       -\frac{2C_D}{3\pi}\ln\frac\mu{\mu_0},\\
\alpha(\mu)
 &=\frac{\alpha(\mu_0)}{
 1-\dfrac{2C_D\alpha(\mu_0)}{3\pi}\ln(\mu/\mu_0)}.
\end{aligned}
\tag{66.12}
$$

它把反复出现的领先对数合并起来。升高能标使分母减小，与真空极化的屏蔽解释相符。用它计算时仍须处于运行耦合较小的区域；将分母外推到零，表示一圈近似已不能继续控制结果。质量无关的MS方案不会在$\mu$低于某个质量时自动删掉该场。跨越阈值时，应将完整理论匹配到相应有效理论，再在每段能区使用自己的物种和。[下文的逐段退耦计算](#c66-thresholds)将用具体质量参数求出这一领先对数近似。

<span id="c66-scalar-bare"></span>

## 标量电动力学：两种顶角怎样给出同一裸电荷

现在转向上一节的复标量。为区别旋量场与标量场，将标量动能因子记为$Z_\varphi$；它就是上一节的$Z_2$。裸场为
<span id="eq:c66-scalar-fields"></span>

$$
\varphi_0=Z_\varphi^{1/2}\varphi,\qquad
\varphi_0^\dagger=Z_\varphi^{1/2}\varphi^\dagger,
\qquad A_{0\mu}=Z_3^{1/2}A_\mu,
\qquad Z_\varphi=Z_2.
\tag{66.13}
$$

三价电磁项含两条标量和一条光子，其归一幂与旋量情形相同。接触项却含两条光子，四标量项则含四条标量。逐项比较裸作用量与第65节的作用量，得到
<span id="eq:c66-scalar-bare-couplings"></span>

$$
\begin{aligned}
e_0 Z_\varphi Z_3^{1/2}
 &=e\widetilde\mu^{\varepsilon/2}Z_1,
& e_0&=\widetilde\mu^{\varepsilon/2}e
          \frac{Z_1}{Z_\varphi\sqrt{Z_3}},\\
e_0^2 Z_\varphi Z_3
 &=e^2\widetilde\mu^\varepsilon Z_4,
& e_0^2&=\widetilde\mu^\varepsilon e^2
          \frac{Z_4}{Z_\varphi Z_3},\\
\lambda_0 Z_\varphi^2
 &=\lambda\widetilde\mu^\varepsilon Z_\lambda,
&\lambda_0&=\widetilde\mu^\varepsilon\lambda
          \frac{Z_\lambda}{Z_\varphi^2}.
\end{aligned}
\tag{66.14}
$$

在第二行中，两个光子场合起来给$Z_3$，一对标量给$Z_\varphi$，两者移到右边都是负一次。把第一行平方，再与第二行相等，正好得到
<span id="eq:c66-seagull-consistency"></span>

$$
\frac{Z_1^2}{Z_\varphi^2Z_3}
 =\frac{Z_4}{Z_\varphi Z_3}
\quad\Longleftrightarrow\quad
Z_4=\frac{Z_1^2}{Z_\varphi}.
\tag{66.15}
$$

这条关系已经由[第65节的有限规范变换](/posts/srednicki-65/#c65-finite-gauge)直接证明。两种电磁顶角由同一个电荷确定。进一步以同一个局域相位系数定义重整化电荷，标量的三点核恒等式使动能与电流反项同属一个协变平方，给$Z_1=Z_\varphi$，于是$Z_4=Z_\varphi$。在本节的一圈计算中，这些关系还可直接由上一节的实际结果读出：
<span id="eq:c66-scalar-z"></span>

$$
\begin{aligned}
Z_1=Z_\varphi=Z_4
 &=1+\frac{3e^2}{8\pi^2\varepsilon}+\text{更高圈项},\\
Z_3&=1-\frac{e^2}{24\pi^2\varepsilon}+\text{更高圈项},\\
Z_\lambda
 &=1+\frac1{16\pi^2\varepsilon}
           \left(\frac{24e^4}{\lambda}+5\lambda\right)
        +\text{更高圈项}.
\end{aligned}
\tag{66.16}
$$

这里使用第65节的朗道规范和MS极部。最后一行的乘法写法暂取$\lambda\ne0$；其真正进入作用量的乘积$\lambda Z_\lambda$在零点仍有加性意义。

<span id="c66-two-couplings"></span>

## 两个工程权重与四次耦合的贝塔函数

电荷的两个顶角归一相消后，仍须保留工程尺度：$e_0=\widetilde\mu^{\varepsilon/2}eZ_3^{-1/2}$。仿照前半节，对两个裸耦合所含的重整化因子分别取对数：
<span id="eq:c66-scalar-log-poles"></span>

$$
\begin{aligned}
\ln Z_3^{-1/2}
 &=\sum_{n\ge1}\frac{E_n^{(e)}(e,\lambda)}{\varepsilon^n},\\
\ln(Z_\varphi^{-2}Z_\lambda)
 &=\sum_{n\ge1}\frac{L_n(e,\lambda)}{\varepsilon^n}.
\end{aligned}
\tag{66.17}
$$

$E_n^{(e)}$属于裸电荷的对数，其定义中含光子归一的$1/2$，与前面的$E_n^{(\alpha)}$不同。在耦合保持非零定号的区间，裸关系成为
<span id="eq:c66-scalar-bare-logs"></span>

$$
\begin{aligned}
\ln|e_0|
 &=\ln|e|+\frac{\varepsilon}{2}\ln\widetilde\mu
       +\sum_{n\ge1}\frac{E_n^{(e)}}{\varepsilon^n},\\
\ln|\lambda_0|
 &=\ln|\lambda|+\varepsilon\ln\widetilde\mu
       +\sum_{n\ge1}\frac{L_n}{\varepsilon^n}.
\end{aligned}
\tag{66.18}
$$

绝对值使第一行在负电荷支上为实；两个尺度项中的系数分别为工程维数$\varepsilon/2$与$\varepsilon$。

由式[（66.16）](#eq:c66-scalar-z)逐项取对数，一圈简单极点为
<span id="eq:c66-scalar-residues"></span>

$$
\begin{aligned}
E_1^{(e)}
 &=-\frac12\left(-\frac{e^2}{24\pi^2}\right)
       +\text{更高圈项}
   =\frac{e^2}{48\pi^2}+\text{更高圈项},\\
L_1
 &=-2\frac{3e^2}{8\pi^2}
       +\frac1{16\pi^2}
           \left(\frac{24e^4}{\lambda}+5\lambda\right)
       +\text{更高圈项}\\
 &=\frac1{16\pi^2}
        \left(5\lambda+\frac{24e^4}{\lambda}-12e^2\right)
       +\text{更高圈项}.
\end{aligned}
\tag{66.19}
$$

$L_1$中的$-12e^2$来自四条外标量的场归一$Z_\varphi^{-2}$。上一节零动量四标量顶角中的混合圈已经相消，但重新归一场以后，裸四次耦合仍会含这个混合项。

下一步对两个裸量求导。电荷和四次耦合的工程维数不同，所以先定义
<span id="eq:c66-engineering-operator"></span>

$$
\begin{gathered}
B_e=-\frac{\varepsilon e}{2}+\beta_e,
\qquad B_\lambda=-\varepsilon\lambda+\beta_\lambda,\\
\mathcal D:=\frac e2\frac{\partial}{\partial e}
                  +\lambda\frac{\partial}{\partial\lambda},\qquad
\mathcal B:=\beta_e\frac{\partial}{\partial e}
                  +\beta_\lambda\frac{\partial}{\partial\lambda}.
\end{gathered}
\tag{66.20}
$$

沿第52节已经建立的双耦合链式法则，裸量的两个导数是
<span id="eq:c66-double-chain"></span>

$$
\begin{aligned}
0&=\frac{B_e}{e}+\frac\varepsilon2
   +\sum_{n\ge1}\frac{
       B_e\partial_eE_n^{(e)}+B_\lambda\partial_\lambda E_n^{(e)}}
                        {\varepsilon^n},\\
0&=\frac{B_\lambda}{\lambda}+\varepsilon
   +\sum_{n\ge1}\frac{
       B_e\partial_eL_n+B_\lambda\partial_\lambda L_n}
                        {\varepsilon^n}.
\end{aligned}
\tag{66.21}
$$

把$B_e\partial_e+B_\lambda\partial_\lambda$写成$-\varepsilon\mathcal D+\mathcal B$，先取简单极点与工程项相乘的有限部分，再把其余项下标移一格，得到
<span id="eq:c66-double-laurent"></span>

$$
\begin{aligned}
0&=\frac{\beta_e}{e}-\mathcal D E_1^{(e)}
  +\sum_{n\ge1}\frac{\mathcal B E_n^{(e)}-\mathcal D E_{n+1}^{(e)}}
                         {\varepsilon^n},\\
0&=\frac{\beta_\lambda}{\lambda}-\mathcal D L_1
  +\sum_{n\ge1}\frac{\mathcal B L_n-\mathcal D L_{n+1}}
                         {\varepsilon^n}.
\end{aligned}
\tag{66.22}
$$

和式[（66.7）](#eq:c66-alpha-laurent)一样，负幂的相消是高次极点之间的一致性条件；有限部分才确定四维运行：
<span id="eq:c66-beta-from-residues"></span>

$$
\beta_e=e\mathcal D E_1^{(e)},\qquad
\beta_\lambda=\lambda\mathcal D L_1.
\tag{66.23}
$$

一圈$E_1^{(e)}$不含$\lambda$，因而
<span id="eq:c66-scalar-charge-beta"></span>

$$
\beta_e=e\frac e2\frac{\partial}{\partial e}
                        \frac{e^2}{48\pi^2}
       =\frac{e^3}{48\pi^2}+\text{更高圈项}.
\tag{66.24}
$$

四次耦合中的$e^4/\lambda$同时依赖两个变量。分别作用两个偏导，有
<span id="eq:c66-lambda-residue-derivatives"></span>

$$
\begin{aligned}
\frac e2\partial_e L_1
 &=\frac1{16\pi^2}
          \left(\frac{48e^4}{\lambda}-12e^2\right),\\
\lambda\partial_\lambda L_1
 &=\frac1{16\pi^2}
          \left(5\lambda-\frac{24e^4}{\lambda}\right),\\
\mathcal D L_1
 &=\frac1{16\pi^2}
          \left(5\lambda+\frac{24e^4}{\lambda}-12e^2\right)
       \qquad\text{至一圈阶}.
\end{aligned}
\tag{66.25}
$$

因此得到
<span id="eq:c66-scalar-lambda-beta"></span>

$$
\beta_\lambda
 =\frac{5\lambda^2-12e^2\lambda+24e^4}{16\pi^2}
      +\text{更高圈项}.
\tag{66.26}
$$

混合项的系数来自场归一$-2\ln Z_\varphi$，其中因子二对应两对外标量。

在$\lambda=0$附近，可以用不含耦合对数的办法重新求同一个结果。将上一节的加性反项乘以$Z_\varphi^{-2}$，到一圈阶得到
<span id="eq:c66-additive-bare-quartic"></span>

$$
\begin{aligned}
\lambda_0
 &=\widetilde\mu^\varepsilon
     \left[\lambda+\frac{P(e,\lambda)}{\varepsilon}
                       +\text{更高圈项}\right],\\
P(e,\lambda)
 &=\frac{5\lambda^2-12e^2\lambda+24e^4}{16\pi^2}.
\end{aligned}
\tag{66.27}
$$

这里的三个单项式都有工程权重2：$\mathcal D\lambda^2=2\lambda^2$，$\mathcal D(e^2\lambda)=2e^2\lambda$，$\mathcal D e^4=2e^4$。因此$\mathcal D P=2P$。固定裸量求导并只保留一圈，得到
<span id="eq:c66-additive-derivative"></span>

$$
\begin{aligned}
0&=\varepsilon\lambda+P+B_\lambda
        +\frac{B_e\partial_eP+B_\lambda\partial_\lambda P}{\varepsilon}
        +\text{更高圈项}\\
 &=\beta_\lambda+P-\mathcal DP+\text{更高圈项}
  =\beta_\lambda-P+\text{更高圈项}.
\end{aligned}
\tag{66.28}
$$

$P$已经是一圈量，所以它的导数中只需代入$B_e,B_\lambda$的工程项；量子贝塔函数乘$\partial P$属于更高圈。这个推导在$\lambda=0$也成立，直接给$\beta_\lambda=24e^4/(16\pi^2)$。电磁相互作用会生成标量自耦合，和上一节四标量图产生局部反项的结论一致。

标量四次耦合在单圈近似下随能标增大，因为
<span id="eq:c66-scalar-beta-positivity"></span>

$$
5\lambda^2-12e^2\lambda+24e^4
 =5\left(\lambda-\frac65e^2\right)^2
       +\frac{84}{5}e^4 .
\tag{66.29}
$$

它除自由点$e=\lambda=0$外严格为正。取$e=0$则恢复$-\lambda|\varphi|^4/4$归一下纯复标量的$5\lambda^2/(16\pi^2)$。对电磁耦合仍应说$|e|$增大；在对称真空和微扰展开有效的能区内，$\lambda$也随能标增大。若耦合已大到更高圈与一圈可比，或有效势不再支持所取真空，这个单圈趋势就不足以继续决定理论的行为。

<span id="c66-mixed-matter"></span>

## 旋量与标量贡献的合并

最后考虑两类场同时存在的理论。第62节的狄拉克圈与第65节的复标量圈，都能写成同一光子横向张量乘参数积分。以公共极点$e^2/(8\pi^2\varepsilon)$为单位，它们的正权重分别为
<span id="eq:c66-spin-weights"></span>

$$
\begin{aligned}
w_\Psi&=\int_0^1 8x(1-x)\,dx
        =8\left(\frac12-\frac13\right)=\frac43,\\
w_\varphi&=\int_0^1(1-2x)^2dx
        =1-2+\frac43=\frac13,\qquad
\frac{w_\varphi}{w_\Psi}=\frac14 .
\end{aligned}
\tag{66.30}
$$

标量权重已经包含接触项恢复横向性的贡献，狄拉克权重已经包含旋量迹；这正是两种结果相差四倍的来源。给每个场乘上它的$Q^2$，再把独立圈相加，就得到总的电荷贝塔函数：
<span id="eq:c66-mixed-beta"></span>

$$
\begin{aligned}
C&:=\sum_{\Psi}Q_\Psi^2+\frac14\sum_{\varphi}Q_\varphi^2,\\
Z_3&=1-\frac{e^2 C}{6\pi^2\varepsilon}+\text{更高圈项},\\
\beta_e&=\frac{C e^3}{12\pi^2}+\text{更高圈项},\qquad
\beta_\alpha=\frac{2C\alpha^2}{3\pi}+\text{更高圈项}.
\end{aligned}
\tag{66.31}
$$

第一项的求和单位是狄拉克场，第二项的单位是复标量场。若有多种标量，它们之间还可能需要不同的四次耦合；此处的电荷贝塔函数仍由这些单圈光子自能相加，而式[（66.26）](#eq:c66-scalar-lambda-beta)只对应本节那个单复标量的自耦合。

同样的裸量微分还可以求出质量和场的反常维数。先完成这些导数，再用质量阈值把各段能区的电荷运行连接起来。

<span id="c66-anomalous"></span>

## 质量与场的反常维数

采用[第52节](/posts/srednicki-52/#c52-mass-and-fields)的定义，固定裸参数、裸场及$\varepsilon$，并令$t=\ln\mu$。与裸场$F_0=\sqrt{Z_F}F$对应的定义为
<span id="eq:c66-ex-1-gamma-definitions"></span>

$$
\gamma_F=\frac12\frac{d\ln Z_F}{dt},
\qquad
\frac{dF}{dt}\bigg|_{F_0}=-\gamma_FF,
\qquad
\gamma_m=\frac{d\ln m}{dt}.
\tag{66.32}
$$

场的运行式有负号，因为增大的$Z_F$须由减小的$F$补偿。
质量定义中的$m$是有质量量纲的参数；
若改求$m/\mu$的对数导数，才会再出现工程项$-1$。

一圈计算只需知道简单极点。设
$\ln Z_j=a_j(e,\lambda)/\varepsilon+\cdots$，则其有限的一圈导数为
<span id="eq:c66-ex-1-simple-pole-derivative"></span>

$$
\begin{aligned}
\left.\frac{d\ln Z_j}{dt}\right|_{\text{一圈有限}}
&=\frac1\varepsilon
 \left(-\frac{\varepsilon e}{2}\partial_e
       -\varepsilon\lambda\partial_\lambda\right)a_j\\
&=-\mathcal D a_j,
\qquad
\mathcal D\equiv\frac e2\partial_e+\lambda\partial_\lambda .
\end{aligned}
\tag{66.33}
$$

这里的$\varepsilon$与极点相消，留下有限结果。
量子部分$\beta_e,\beta_\lambda$再作用于一圈极点会提高圈数；
这些项在高阶计算中要与相应高阶极点一同处理。
所以这一步提取的是所需的一圈系数。

费曼规范的旋量电动力学采用第62节求得的紫外因子：
<span id="eq:c66-ex-1-dirac-poles"></span>

$$
\begin{aligned}
Z_2&=1-\frac{e^2}{8\pi^2\varepsilon}+\cdots,\\
Z_m&=1-\frac{e^2}{2\pi^2\varepsilon}+\cdots,\\
Z_3&=1-\frac{e^2}{6\pi^2\varepsilon}+\cdots.
\end{aligned}
\tag{66.34}
$$

省略号表示更高圈。动能、质量项写成
$iZ_2\bar\Psi\slashed\partial\Psi-Z_m m\bar\Psi\Psi$，
而麦克斯韦项的系数为$Z_3$，因此裸量关系是
<span id="eq:c66-ex-1-bare-fields-mass"></span>

$$
\Psi_0=\sqrt{Z_2}\Psi,\qquad
A_0^\mu=\sqrt{Z_3}A^\mu,\qquad
m_0=\frac{Z_m}{Z_2}m .
\tag{66.35}
$$

对两个场，直接让$\mathcal D$作用于各自的极点系数。
因为$\mathcal D e^2=e^2$，得到
<span id="eq:c66-ex-1-dirac-field-gammas"></span>

$$
\begin{aligned}
\gamma_\Psi
&=-\frac12\mathcal D\left(-\frac{e^2}{8\pi^2}\right)
 =\frac{e^2}{16\pi^2}
 =\frac{\alpha}{4\pi},\\
\gamma_A
&=-\frac12\mathcal D\left(-\frac{e^2}{6\pi^2}\right)
 =\frac{e^2}{12\pi^2}
 =\frac{\alpha}{3\pi},
\qquad \alpha=\frac{e^2}{4\pi}.
\end{aligned}
\tag{66.36}
$$

质量则取决于$Z_m/Z_2$。先相减两个对数，再固定$m_0$求导：
<span id="eq:c66-ex-1-dirac-mass-gamma"></span>

$$
\begin{aligned}
\ln\frac{Z_m}{Z_2}
&=-\frac{3e^2}{8\pi^2\varepsilon}+\cdots,\\
0=\frac{d\ln m_0}{dt}
&=\gamma_m+\frac{3e^2}{8\pi^2}+\cdots,\\
\gamma_m&=-\frac{3e^2}{8\pi^2}
 =-\frac{3\alpha}{2\pi}
\qquad\text{（一圈）}.
\end{aligned}
\tag{66.37}
$$

狄拉克质量在拉格朗日量中是一次的$m$，这里没有再除以2。
在弱耦合范围内，这一负号说明$\overline{\mathrm{MS}}$质量随能标升高而减小。
物理极点质量由传播子的极点位置定义，其尺度不变性还包含自能的显式标度依赖。

### 横向规范下的标量质量与场

取$\xi=0$的朗道规范，使用横向光子核。
仍将标量动能因子记作$Z_\varphi$；它就是第65节的$Z_2$。
由该节各图的紫外极部，有
<span id="eq:c66-ex-2-scalar-poles"></span>

$$
\begin{aligned}
Z_\varphi&=1+\frac{3e^2}{8\pi^2\varepsilon}+\cdots,\\
Z_m&=1+\frac{\lambda}{8\pi^2\varepsilon}+\cdots,\\
Z_3&=1-\frac{e^2}{24\pi^2\varepsilon}+\cdots .
\end{aligned}
\tag{66.38}
$$

标量质量项为$-Z_m m^2\varphi^\dagger\varphi$，因而
<span id="eq:c66-ex-2-bare-fields-mass"></span>

$$
\varphi_0=\sqrt{Z_\varphi}\varphi,\qquad
A_0^\mu=\sqrt{Z_3}A^\mu,\qquad
m_0^2=\frac{Z_m}{Z_\varphi}m^2 .
\tag{66.39}
$$

式[（66.33）](#eq:c66-ex-1-simple-pole-derivative)仍可使用，
但这次标量的动能极点为正，所以场反常维数为负：
<span id="eq:c66-ex-2-scalar-field-gammas"></span>

$$
\begin{aligned}
\gamma_\varphi
&=-\frac12\mathcal D\left(\frac{3e^2}{8\pi^2}\right)
 =-\frac{3e^2}{16\pi^2},\\
\gamma_A
&=-\frac12\mathcal D\left(-\frac{e^2}{24\pi^2}\right)
 =\frac{e^2}{48\pi^2}.
\end{aligned}
\tag{66.40}
$$

场的这些系数是在指定规范中的结果。
质量要同时考虑$\lambda$和$e$的工程权重：
$\mathcal D\lambda=\lambda$，$\mathcal D e^2=e^2$。
因此
<span id="eq:c66-ex-2-scalar-mass-gamma"></span>

$$
\begin{aligned}
\ln\frac{Z_m}{Z_\varphi}
&=\frac{\lambda-3e^2}{8\pi^2\varepsilon}+\cdots,\\
0=\frac{d\ln m_0^2}{dt}
&=2\gamma_m-\frac{\lambda-3e^2}{8\pi^2}+\cdots,\\
\gamma_m&=\frac{\lambda-3e^2}{16\pi^2},\\
\frac{dm^2}{dt}&=\frac{\lambda-3e^2}{8\pi^2}m^2
\qquad\text{（一圈）}.
\end{aligned}
\tag{66.41}
$$

这里出现$1/2$是因为裸量关系涉及$m^2$。
当$m^2=0$时，用最后一行的$m^2$运行式即可，无须对零质量取对数。

积分质量方程时，$e$与$\lambda$也按式[（66.24）](#eq:c66-scalar-charge-beta)、[（66.26）](#eq:c66-scalar-lambda-beta)同时运行。

<span id="c66-gauge-parameter"></span>

## 一般规范中的质量与电荷

[第62节的一般规范计算](/posts/srednicki-62/#c62-general-gauge-uv)已经从光子纵向核求出了任意$R_\xi$规范的紫外系数。
这里使用那些积分的结果，考察裸质量和裸电荷所需要的组合：
<span id="eq:c66-ex-3-general-gauge-poles"></span>

$$
\begin{aligned}
Z_1=Z_2&=1-\frac{\xi e^2}{8\pi^2\varepsilon}+\cdots,\\
Z_m&=1-\frac{(3+\xi)e^2}{8\pi^2\varepsilon}+\cdots,\\
Z_3&=1-\frac{e^2}{6\pi^2\varepsilon}+\cdots.
\end{aligned}
\tag{66.42}
$$

先看质量。$Z_m$和$Z_2$中含$\xi$的极点相同，作比之后已相消：
<span id="eq:c66-ex-3-gauge-independent-mass"></span>

$$
\begin{aligned}
\ln\frac{Z_m}{Z_2}
&=-\frac{[(3+\xi)-\xi]e^2}{8\pi^2\varepsilon}+\cdots
 =-\frac{3e^2}{8\pi^2\varepsilon}+\cdots,\\
\gamma_m&=-\frac{3e^2}{8\pi^2}+\cdots .
\end{aligned}
\tag{66.43}
$$

固定$m_0$作尺度微分，就得到与费曼规范相同的质量反常维数。

电荷的裸量关系包含两个费米场和一个光子场的归一化。
在固定的$e<0$支上用实对数$\ln|e|$，有
<span id="eq:c66-ex-3-bare-charge-pole"></span>

$$
\begin{aligned}
e_0&=\widetilde\mu^{\varepsilon/2}
       e\,Z_3^{-1/2}Z_2^{-1}Z_1,\\
\ln|e_0|&=\frac{\varepsilon}{2}\ln\widetilde\mu
          +\ln|e|+\frac{F_1(e,\xi)}{\varepsilon}+\cdots,\\
F_1(e,\xi)
&=\frac{e^2}{12\pi^2}
  +\frac{\xi e^2}{8\pi^2}
  -\frac{\xi e^2}{8\pi^2}
 =\frac{e^2}{12\pi^2}.
\end{aligned}
\tag{66.44}
$$

$F_1$表示裸$e$对数的极点，与式[（66.5）](#eq:c66-alpha-log)中裸$\alpha$对数的系数分别定义。
对第二行求导，将$B_e=-\varepsilon e/2+\beta_e$代入，
工程项首先相消，有限的一圈项随即给出
<span id="eq:c66-ex-3-gauge-independent-beta"></span>

$$
\begin{aligned}
0&=\frac{\varepsilon}{2}+\frac{B_e}{e}
  +\frac{B_e}{\varepsilon}\,\partial_eF_1+\cdots,\\
0&=\frac{\beta_e}{e}-\frac e2\,\partial_eF_1
  \qquad\text{（一圈有限部分）},\\
\beta_e&=\frac{e^3}{12\pi^2}.
\end{aligned}
\tag{66.45}
$$

规范参数没有进入最终结果，原因在微分之前就已显现：
质量取$Z_m/Z_2$，电荷取$Z_1/Z_2$，相应的$\xi$项分别相消。

固定裸规范参数与暂时固定重整化$\xi$也须区分。
从规范固定项的场重标度得到$\xi_0=Z_3\xi$，因此
<span id="eq:c66-ex-3-gauge-parameter-running"></span>

$$
\frac{d\xi}{dt}=-\xi\frac{d\ln Z_3}{dt}=-2\xi\gamma_A,
\qquad
\gamma_\Psi=\frac{\xi e^2}{16\pi^2}+\cdots .
\tag{66.46}
$$

$d\xi/dt$从$e^2$阶开始，它再作用于$Z_2$的$e^2/\varepsilon$系数属于更高圈。
质量比和电荷比本来就没有一圈$\xi$依赖。
单个带电场的$\gamma_\Psi$仍依赖规范，这与上述两个组合的相消相容。

<span id="c66-thresholds"></span>

## 跨过质量阈值的精细结构常数

对多种带电狄拉克场，把颜色数并入权重$w_i=N_{c,i}Q_i^2$。活跃物种固定时，式[（66.12）](#eq:c66-one-loop-flow)中的$C_D$就是$\sum_iw_i$。跨越质量阈值时，改用修正退耦减除（modified decoupling subtraction，DS）方案：
当尺度低于$m_i$时，把该场积掉，以下区间的贝塔函数便不再包含它。
在各阈值作连续的领先对数匹配，并将$m_i$作为固定阈值。

对$0<\mu<M_W$及$m_i<M_W$，第$i$味真正参与运行的区间为
$\max(m_i,\mu)<\kappa<M_W$，故
<span id="eq:c66-ex-4-threshold-integral"></span>

$$
\int_\mu^{M_W}\frac{d\kappa}{\kappa}\,
       \Theta(\kappa-m_i)
=\ln\frac{M_W}{\max(m_i,\mu)} .
\tag{66.47}
$$

各味相加后得到
<span id="eq:c66-ex-4-corrected-decoupling"></span>

$$
\frac1{\alpha_{\rm DS}(M_W)}
=\frac1{\alpha_{\rm DS}(\mu)}
-\frac2{3\pi}\sum_{m_i<M_W}w_i
       \ln\frac{M_W}{\max(m_i,\mu)} .
\tag{66.48}
$$

式[（66.47）](#eq:c66-ex-4-threshold-integral)中的下限必须取$\max(m_i,\mu)$：
若$\mu<m_i$，继续降低$\mu$不能重新加回已积掉的场。
在完整理论的$\overline{\mathrm{MS}}$贝塔函数中，重场贡献不会自行消失；
这里的停止运行来自阈值处更换有效理论及相应匹配。

低于电子质量时，这里所含的带电场全部退耦。
用低能在壳电荷固定余下的麦克斯韦系数，
即取$\alpha_{\rm DS}(\mu<m_e)=\alpha_{\rm OS}$。
这一低能匹配条件连同上式给出
<span id="eq:c66-ex-4-os-matched-solution"></span>

$$
\frac1{\alpha_{\rm DS}(M_W)}
=137.036-\frac2{3\pi}\sum_{m_i<M_W}
            w_i\ln\frac{M_W}{m_i}.
\tag{66.49}
$$

低能常数由OS条件提供，
而阈值积分决定它与高能参数之间的对数差。
在领先对数精度下略去有限阈值修正和更高圈贡献。

采用[第83节](/posts/srednicki-83/)、[第88节](/posts/srednicki-88/)表内的质量，以及[第87节](/posts/srednicki-87/)的$M_W$，作为这次估算的历史教学参数：
$m_c=1.3\,{\rm GeV}$、$m_b=4.3\,{\rm GeV}$、$m_t=178\,{\rm GeV}$，
作为相应标度下的近似$\overline{\mathrm{MS}}$质量；
带电轻子的质量取$m_e=0.511\,{\rm MeV}$、$m_\mu=105.7\,{\rm MeV}$、
$m_\tau=1777\,{\rm MeV}$，目标标度取$M_W=80.4\,{\rm GeV}$。
轻夸克统一取$m_u=m_d=m_s=0.300\,{\rm GeV}$，
表示强子效应开始重要时的有效退耦尺度，而非轻夸克的流质量。
这些参数用于说明阈值积分的做法。

电子电荷取$e<0$，因此这里的$Q_i$与以正的质子电荷为单位的电荷数相差总负号，
平方后给相同的$w_i$。换成统一的GeV单位后，对数贡献如下。

| 味     | $m_i\ ({\rm GeV})$ | $w_i=N_{c,i}Q_i^2$ | $w_i\ln(M_W/m_i)$ |
| ------ | -----------------: | -----------------: | ----------------: |
| $e$    |         $0.000511$ |                $1$ |       $11.966155$ |
| $\mu$  |           $0.1057$ |                $1$ |        $6.634165$ |
| $u$    |            $0.300$ |              $4/3$ |        $7.454649$ |
| $d$    |            $0.300$ |              $1/3$ |        $1.863662$ |
| $s$    |            $0.300$ |              $1/3$ |        $1.863662$ |
| $c$    |              $1.3$ |              $4/3$ |        $5.499533$ |
| $\tau$ |            $1.777$ |                $1$ |        $3.812088$ |
| $b$    |              $4.3$ |              $1/3$ |        $0.976133$ |

顶夸克质量高于$M_W$，不属于此和；中微子的电荷为零，也没有贡献。
总共是八种带电味，计入颜色后为十八份带电狄拉克场。
三种轻夸克的权重合为$2$，所以整个对数和可合写为
<span id="eq:c66-ex-4-numerical-log-sum"></span>

$$
\begin{aligned}
L\equiv\sum_iw_i\ln\frac{M_W}{m_i}
={}&\ln\frac{80.4}{0.000511}
   +\ln\frac{80.4}{0.1057}
   +\ln\frac{80.4}{1.777}\\
 &+2\ln\frac{80.4}{0.300}
   +\frac43\ln\frac{80.4}{1.3}
   +\frac13\ln\frac{80.4}{4.3}\\
={}&40.0700475611 .
\end{aligned}
\tag{66.50}
$$

各比值的分子、分母均以GeV计，因而对数的宗量无量纲。
代入式[（66.49）](#eq:c66-ex-4-os-matched-solution)便得
<span id="eq:c66-ex-4-alpha-value"></span>

$$
\begin{aligned}
\alpha_{\rm DS}^{-1}(M_W)
&=137.036-\frac2{3\pi}(40.0700475611)\\
&=137.036-8.5031281857
 =128.5328718143,\\
\alpha_{\rm DS}(M_W)&=0.0077801109233
 \simeq\frac1{128.5}.
\end{aligned}
\tag{66.51}
$$

还可以不按粒子求和，而从最低阈值逐段向上积分。
若区间$[\mu_j,\mu_{j+1}]$的活跃权重为$W_j$，连续匹配给
<span id="eq:c66-ex-4-piecewise-recurrence"></span>

$$
\alpha_{\rm DS}^{-1}(\mu_{j+1})
=\alpha_{\rm DS}^{-1}(\mu_j)
-\frac2{3\pi}W_j\ln\frac{\mu_{j+1}}{\mu_j}.
\tag{66.52}
$$

从$\alpha_{\rm DS}^{-1}(m_e)=137.036$开始，得到下表。
这一积分方式按阈值区间组织贡献，独立检查了每种颜色加入运行的时刻。

| 区间下端至上端（GeV） |  $W_j$ | 上端的$\alpha_{\rm DS}^{-1}$ |
| --------------------- | -----: | ---------------------------: |
| $0.000511\to0.1057$   |    $1$ |               $135.90451646$ |
| $0.1057\to0.300$      |    $2$ |               $135.46177814$ |
| $0.300\to1.3$         |    $4$ |               $134.21711258$ |
| $1.3\to1.777$         | $16/3$ |               $133.86336444$ |
| $1.777\to4.3$         | $19/3$ |               $132.67570915$ |
| $4.3\to80.4$          | $20/3$ |               $128.53287181$ |

两个计算给出相同的末值。
若分别在$\mu=m_e/2$和$m_e/4$应用
式[（66.48）](#eq:c66-ex-4-corrected-decoupling)，所得末值也相同。
表中的多位小数用于复算；轻夸克的$300\,{\rm MeV}$阈值本身是粗略模型，
因此与模型精度相称的结果是$\alpha(M_W)\simeq1/128.5$。
它显示了真空极化的屏蔽效应：由低能向高能推进时，所测得的电磁耦合逐渐增强。

---

[← 第 65 节](/posts/srednicki-65/) · [章节地图](/srednicki/) · [第 67 节 →](/posts/srednicki-67/)
