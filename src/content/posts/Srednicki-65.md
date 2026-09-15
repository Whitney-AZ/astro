---
title: 'Srednicki §65 标量电动力学中的圈修正'
date: 2026-09-14
category: 笔记
tags: [物理, 量子场论, Srednicki]
series: 'Srednicki QFT'
srednickiSections: [65]
hideFromHome: true
draft: false
---

<span id="c65"></span>

第61节已经建立标量电动力学的树级规则。现在让虚粒子在图中形成闭圈，求它们对传播子和顶角的修正。与第62节不同，这一次主要关心紫外发散的系数：在$\overline{\mathrm{MS}}$方案中，它们确定重整化因子，并为判断耦合随能标怎样变化提供依据。有限的散射振幅需要保留完整外动量；提取局部发散时，却可以选择使计算显著简化的动量和规范。

<span id="c65-model"></span>

## 拉氏量、顶角和减除约定

考虑保持洛伦兹与局域$U(1)$对称性的复标量理论，取质量项、四次势和协变动能，并加上麦克斯韦动能。这些项给出本节的可重整化模型。先将每种结构的系数分开记下，便于从不同的格林函数中确定它们。沿第61节的电荷及场约定，写成
<span id="eq:c65-lagrangian"></span>

$$
\begin{aligned}
\mathcal L&=\mathcal L_0+\mathcal L_1,\\
\mathcal L_0
 &=-\partial^\mu\varphi^\dagger\partial_\mu\varphi
   -m^2\varphi^\dagger\varphi-\frac14F^{\mu\nu}F_{\mu\nu},\\
\mathcal L_1
 &=-iZ_1e\,[\varphi^\dagger\partial^\mu\varphi
                  -(\partial^\mu\varphi^\dagger)\varphi]A_\mu
   -Z_4e^2\varphi^\dagger\varphi A^\mu A_\mu\\
 &\quad-\frac{Z_\lambda\lambda}{4}(\varphi^\dagger\varphi)^2
   +\mathcal L_{\rm ct},\\
\mathcal L_{\rm ct}
 &=-(Z_2-1)\partial^\mu\varphi^\dagger\partial_\mu\varphi
   -(Z_m-1)m^2\varphi^\dagger\varphi
   -\frac{Z_3-1}{4}F^{\mu\nu}F_{\mu\nu}.
\end{aligned}
\tag{65.1}
$$

这里$m^2>0$，在$\varphi=A=0$的对称真空附近作微扰，$e<0$、$\lambda$为实数。正的$\lambda$给出有下界的树级四次势。线性交叉项的负号由协变导数$D_\mu=\partial_\mu-ieA_\mu$确定。展开协变动能$-(D^\mu\varphi)^\dagger D_\mu\varphi$，有
<span id="eq:c65-action-sign"></span>

$$
\begin{aligned}
-(D^\mu\varphi)^\dagger D_\mu\varphi
 &=-\partial^\mu\varphi^\dagger\partial_\mu\varphi\\
 &\quad+ieA_\mu\big[(\partial^\mu\varphi^\dagger)\varphi
                          -\varphi^\dagger\partial^\mu\varphi\big]
       -e^2A^2\varphi^\dagger\varphi .
\end{aligned}
\tag{65.2}
$$

因此，导数作用于入射的$e^{ipx}$和出射的$e^{-ip'x}$时，线性交叉项给出三点顶角$ie(p+p')^\mu$。若交换$\varphi$与$\varphi^\dagger$，线性交叉项和粒子荷支同时反号；[有限规范变换](#c65-finite-gauge)将给出两种写法对应的相位及同一个规范约束。

记$\delta Z_i=Z_i-1$。本节用到的树顶角与二点反项为
<span id="eq:c65-rules-counterterms"></span>

$$
\begin{aligned}
iV_{3,\rm tree}^{\mu}(p',p)&=ieZ_1(p'+p)^\mu,\\
iV_{4,\rm tree}^{\mu\nu}&=-2ie^2Z_4g^{\mu\nu},\qquad
iV_{4\varphi,\rm tree}=-iZ_\lambda\lambda,\\
i\Pi_{\varphi,\rm ct}(k^2)
 &=-i\delta Z_2k^2-i\delta Z_m m^2,\\
i\Pi_{\rm ct}^{\mu\nu}(k)
 &=-i\delta Z_3(k^2g^{\mu\nu}-k^\mu k^\nu).
\end{aligned}
\tag{65.3}
$$

前两个电磁顶角的阶乘和动量号已在第61节逐一求出。四标量顶角中的$2!\,2!$抵消拉氏量的$1/4$。内线仍为相应传播核除以$i$，闭合的标量圈没有费米统计负号。光子反项保留$\mu,\nu$两个自由指标，其纵向张量为$k^\mu k^\nu$。

维数调节采用
<span id="eq:c65-dimensions"></span>

$$
\begin{gathered}
d=4-\varepsilon,\qquad
e_d=e\widetilde\mu^{\varepsilon/2},\qquad
\lambda_d=\lambda\widetilde\mu^\varepsilon,\qquad
\mu^2=4\pi e^{-\gamma_E}\widetilde\mu^2,\\
[\varphi]=[A]=\frac{d-2}{2},\qquad
[e_d]=\frac{\varepsilon}{2},\qquad
[\lambda_d]=\varepsilon .
\end{gathered}
\tag{65.4}
$$

以下$\int_\ell$表示$d^d\ell/(2\pi)^d$。三点函数提出一个公共$\widetilde\mu^{\varepsilon/2}$，两个四点函数提出$\widetilde\mu^\varepsilon$，所余圈积分统一带$\widetilde\mu^\varepsilon$。这种写法使显示的$e,\lambda$无量纲，又不会丢失外顶角的工程量纲。各$Z_i$在圈内只需取1；在那里再插入$\delta Z_i$，便增加一阶圈修正。我们将保留一圈产生的$e^2,\lambda,e^4,e^2\lambda,\lambda^2$各项，并由它们所在的格林函数判断阶次。

<span id="c65-photon"></span>

## 标量圈与接触项怎样给出横向光子自能

光子二点函数有一个有向标量泡、一个接触顶角上的标量闭线，以及光子动能反项。图65a依次画出这三个贡献。

![光子自能的标量泡、标量接触闭线和反项](/images/srednicki/s65-c65_01.svg)

图65a：虚线箭头记录复标量的电荷方向，上、下内线的带符号动量为$\ell+k$、$\ell$；波线外动量均为$k$。中图的闭线是复标量，右图叉号为$\delta Z_3$。<span id="c65-photon-figure"></span>

两条标量内线给$(1/i)^2$，与两个$ie$相乘后为$+e^2$。接触图只有一条标量内线，故$(-2ie^2)(1/i)=-2e^2$。于是
<span id="eq:c65-photon-three-terms"></span>

$$
\begin{aligned}
i\Pi^{\mu\nu}(k)
 &=e^2\widetilde\mu^\varepsilon\int_\ell
 \frac{(2\ell+k)^\mu(2\ell+k)^\nu}
      {[(\ell+k)^2+m^2](\ell^2+m^2)}\\
 &\quad-2e^2g^{\mu\nu}\widetilde\mu^\varepsilon
                           \int_\ell\frac1{\ell^2+m^2}
       -i\delta Z_3(k^2g^{\mu\nu}-k^\mu k^\nu).
\end{aligned}
\tag{65.5}
$$

分母都继承$-i0$；在下面的欧氏参数计算中暂不重复写出。两个圈图单独都含表面的二次发散，因此先把它们合并，更容易看见质量型项如何消去。给第二项乘上缺少的分母，得到
<span id="eq:c65-combined-numerator"></span>

$$
\begin{aligned}
i\Pi^{\mu\nu}(k)
 &=e^2\widetilde\mu^\varepsilon\int_\ell
 \frac{N^{\mu\nu}}
      {[(\ell+k)^2+m^2](\ell^2+m^2)}
 -i\delta Z_3(k^2g^{\mu\nu}-k^\mu k^\nu),\\
N^{\mu\nu}
 &=(2\ell+k)^\mu(2\ell+k)^\nu
                  -2[(\ell+k)^2+m^2]g^{\mu\nu}.
\end{aligned}
\tag{65.6}
$$

用一个费曼参数合并分母，并作允许的圈动量平移：
<span id="eq:c65-photon-parameters"></span>

$$
\begin{gathered}
\frac1{AB}=\int_0^1\frac{dx}{[xA+(1-x)B]^2},\\
A=(\ell+k)^2+m^2,\quad B=\ell^2+m^2,\quad
q=\ell+xk,\quad D=m^2+x(1-x)k^2,\\
xA+(1-x)B=q^2+D,\qquad
\int_\ell\frac{N^{\mu\nu}}{AB}
 =\int_0^1dx\int_q\frac{N^{\mu\nu}}{(q^2+D)^2}.
\end{gathered}
\tag{65.7}
$$

平移的雅可比行列式为1。先在威克转动后积分收敛的维数域中使用这些操作，再作解析延拓，正是第14、62节所用的维数调节方式。

将$\ell=q-xk$代入分子。关于$q$的一次项在对称积分中为零，而$q^\mu q^\nu$在只依赖$q^2$的分母下平均为$g^{\mu\nu}q^2/d$，所以
<span id="eq:c65-photon-angular"></span>

$$
\begin{aligned}
N^{\mu\nu}
 &=[2q+(1-2x)k]^\mu[2q+(1-2x)k]^\nu\\
 &\quad-2[(q+(1-x)k)^2+m^2]g^{\mu\nu}\\
 &\ \longrightarrow\
 4q^\mu q^\nu+(1-2x)^2k^\mu k^\nu
              -2[q^2+(1-x)^2k^2+m^2]g^{\mu\nu}\\
 &\ \longrightarrow\
 2\left(\frac2d-1\right)q^2g^{\mu\nu}
 +(1-2x)^2k^\mu k^\nu
              -2[(1-x)^2k^2+m^2]g^{\mu\nu}.
\end{aligned}
\tag{65.8}
$$

箭头表示放入当前积分后的等价替换。特别是$\varepsilon$尚未取零，$d$不能在二次发散项前随意换成4。

接着复用[第62节的径向分部积分](/posts/srednicki-62/#eq:c62-radial-identity)。令$J_n(D)=\widetilde\mu^\varepsilon\int_q(q^2+D)^{-n}$。总导数积分及$q^2=(q^2+D)-D$给
<span id="eq:c65-radial-replacement"></span>

$$
\begin{aligned}
0&=dJ_1(D)
 -2\widetilde\mu^\varepsilon\int_q\frac{q^2}{(q^2+D)^2},\\
\widetilde\mu^\varepsilon\int_q\frac{q^2}{(q^2+D)^2}
 &=J_1(D)-DJ_2(D),\\
\left(\frac2d-1\right)
 \widetilde\mu^\varepsilon\int_q\frac{q^2}{(q^2+D)^2}
 &=DJ_2(D).
\end{aligned}
\tag{65.9}
$$

因此，在式[（65.8）](#eq:c65-photon-angular)的积分里，可将$(2/d-1)q^2$换成$D$。代入$D$以后，显式的$m^2$相消：
<span id="eq:c65-photon-after-radial"></span>

$$
\begin{aligned}
N^{\mu\nu}
 &\ \longrightarrow\
 2Dg^{\mu\nu}+(1-2x)^2k^\mu k^\nu
                    -2[(1-x)^2k^2+m^2]g^{\mu\nu}\\
 &=(1-2x)^2k^\mu k^\nu
                    -2(1-2x)(1-x)k^2g^{\mu\nu}.
\end{aligned}
\tag{65.10}
$$

还剩一个参数上的不对称写法。取$x=y+1/2$，有
<span id="eq:c65-centered-parameter"></span>

$$
\begin{aligned}
-\frac12&\le y\le\frac12,\qquad
D=m^2+\left(\frac14-y^2\right)k^2,\\
N^{\mu\nu}
 &=4y^2k^\mu k^\nu-2(2y^2-y)k^2g^{\mu\nu}\\
 &\ \longrightarrow\
 -4y^2(k^2g^{\mu\nu}-k^\mu k^\nu).
\end{aligned}
\tag{65.11}
$$

$D$是$y$的偶函数，故最后一行删去的是$2yk^2g^{\mu\nu}$这一奇项。

经过这两次积分化简，光子自能成为
<span id="eq:c65-photon-transverse"></span>

$$
\begin{aligned}
\Pi^{\mu\nu}(k)
 &=\Pi(k^2)(k^2g^{\mu\nu}-k^\mu k^\nu),\\
\Pi(k^2)
 &=-\frac{e^2}{i}\int_0^1dx\,(1-2x)^2
                       J_2\big(m^2+x(1-x)k^2\big)-\delta Z_3 .
\end{aligned}
\tag{65.12}
$$

收缩$k_\mu$立即给零。标量接触顶角因而不仅改变图的数目，它还使二点函数具有规范对称性所要求的结构；没有留下可解释为光子质量的常数张量。

圈积分已在第62节求出。这里取$n=2$，并保留提取极部所需的两项：
<span id="eq:c65-j2-pole"></span>

$$
\begin{aligned}
J_2(D)
 &=\frac{i\widetilde\mu^\varepsilon}
         {(4\pi)^{d/2}}\Gamma(2-d/2)D^{d/2-2}\\
 &=\frac{i}{16\pi^2}
   \left[\frac2\varepsilon-\ln\frac D{\mu^2}
                              +O(\varepsilon)\right].
\end{aligned}
\tag{65.13}
$$

这里$\Gamma(\varepsilon/2)=2/\varepsilon-\gamma_E+O(\varepsilon)$，其常数项已经合入$\mu$的定义。极点系数与$D$无关，剩余参数积分于是只是
<span id="eq:c65-photon-parameter-weight"></span>

$$
\int_0^1(1-2x)^2dx
 =\left[x-2x^2+\frac43x^3\right]_0^1
 =\frac13
 =4\int_{-1/2}^{1/2}y^2dy .
\tag{65.14}
$$

所以
<span id="eq:c65-z3"></span>

$$
\Pi(k^2)\big|_{\rm pole}
 =-\frac{e^2}{24\pi^2\varepsilon}-\delta Z_3,
\qquad
Z_3=1-\frac{e^2}{24\pi^2\varepsilon}
           +\text{更高圈项}.
\tag{65.15}
$$

对一个复标量，极点系数是第62节一个狄拉克场结果的四分之一。两者的电荷相同，差别来自各自的传播子分子和自由度；此处的$1/3$已由实际参数积分得到。

<span id="c65-scalar-self"></span>

## 横向光子中的标量自能

接下来求标量二点函数。内部出现光子以后，规范的选择就能帮助我们化简分子。选取朗道规范的横向光子核：
<span id="eq:c65-transverse-projector"></span>

$$
\begin{gathered}
\widetilde\Delta_{\mu\nu}(\ell)
 =\frac{P_{\mu\nu}(\ell)}{\ell^2-i0},\qquad
P_{\mu\nu}(\ell)=g_{\mu\nu}-\frac{\ell_\mu\ell_\nu}{\ell^2},\\
\ell^\mu P_{\mu\nu}=P_{\mu\nu}\ell^\nu=0,\qquad
P_\mu{}^\rho P_{\rho\nu}=P_{\mu\nu},\qquad
g^{\mu\nu}P_{\mu\nu}=d-1 .
\end{gathered}
\tag{65.16}
$$

这是第57节的横向核，也就是协变规范族中的$\xi=0$。收缩一只$\ell$时，投影中的两项给$\ell_\nu-\ell^2\ell_\nu/\ell^2=0$；取迹则从$d$减去1。光锥上的表达式仍按该节的共同边界处方理解，下面在维数积分的欧氏表示中使用投影恒等式。

![标量自能的混合泡、两种蝌蚪图和反项](/images/srednicki/s65-c65_02.svg)

图65b：依次为标量—光子泡、光子蝌蚪、标量蝌蚪和二点反项。虚线沿外电荷方向，泡内标量带$\ell+k$，光子带$\ell$。光子蝌蚪的两条相同半线可以互换，权重为$1/2$。<span id="c65-scalar-figure"></span>

先确定两个蝌蚪的计数。一次插入$-e^2\varphi^\dagger\varphi A_\mu A^\mu$，两个标量各接一条外线，余下两个$A$只组成一个收缩。因此从完整接触顶角读取时，应有$1/2$。四标量插入的两个外端却各有两个可选的同类场，得到
<span id="eq:c65-tadpole-contractions"></span>

$$
\begin{aligned}
\text{光子蝌蚪顶角权重}:&
 \qquad \frac12(-2ie^2)=-ie^2,\\
\text{标量蝌蚪顶角权重}:&
 \qquad \left(-\frac{i\lambda}{4}\right)(2)(2)=-i\lambda .
\end{aligned}
\tag{65.17}
$$

第一行的$1/2$来自两个相同光子端点的交换。光子蝌蚪在去掉调节质量后趋于零；在取这个极限以前，应保留该收缩权重。

泡图分子中的$(\ell+2k)^\mu(\ell+2k)^\nu$与$P_{\mu\nu}$缩并，只留下$4P_{\mu\nu}k^\mu k^\nu$。两个顶角和两条内线的相位仍给$+e^2$。结合式[（65.17）](#eq:c65-tadpole-contractions)，有
<span id="eq:c65-scalar-self-integrals"></span>

$$
\begin{aligned}
i\Pi_\varphi(k^2)
 &=4e^2\widetilde\mu^\varepsilon
    \int_\ell\frac{P_{\mu\nu}(\ell)k^\mu k^\nu}
                   {\ell^2[(\ell+k)^2+m^2]}\\
 &\quad-(d-1)e^2J_1(m_\gamma^2)-\lambda J_1(m^2)\\
 &\quad-i\delta Z_2 k^2-i\delta Z_m m^2 .
\end{aligned}
\tag{65.18}
$$

光子蝌蚪中临时加入正的$m_\gamma^2$。所有圈积分均使用$d$维测度，并带相应的$\widetilde\mu^\varepsilon$。

同一个维数积分公式取$n=1$便给
<span id="eq:c65-j1-pole"></span>

$$
\begin{aligned}
J_1(M^2)
 &=\frac{i\widetilde\mu^\varepsilon}{(4\pi)^{d/2}}
       \Gamma(1-d/2)(M^2)^{d/2-1}\\
 &=\frac{iM^2}{16\pi^2}
     \left[-\frac2\varepsilon+\ln\frac{M^2}{\mu^2}-1
                                  +O(\varepsilon)\right].
\end{aligned}
\tag{65.19}
$$

负号来自$\Gamma(-1+\varepsilon/2)=\Gamma(\varepsilon/2)/(-1+\varepsilon/2)$，与分母平方积分的正极点不同。对光子蝌蚪应先用第一行的完整表达式：
<span id="eq:c65-tadpole-massless-limit"></span>

$$
J_1(m_\gamma^2)
 =\frac{i\widetilde\mu^\varepsilon
                 \Gamma(-1+\varepsilon/2)}
        {(4\pi)^{2-\varepsilon/2}}
       (m_\gamma^2)^{1-\varepsilon/2}
 \ \longrightarrow\ 0
 \quad
 (m_\gamma\to0,\ 0<\operatorname{Re}\varepsilon<2).
\tag{65.20}
$$

在这个固定维数域中，质量的幂为正，再将零结果作维数延拓。标量蝌蚪则保留$m>0$，给$i\lambda m^2/(8\pi^2\varepsilon)$这一质量型极点。

现在评价泡图。把$P$中的$\ell^2$乘到分母中，便得到三个因子，其中两个相同：
<span id="eq:c65-scalar-parameters"></span>

$$
\begin{aligned}
\frac{P_{\mu\nu}(\ell)k^\mu k^\nu}
     {\ell^2[(\ell+k)^2+m^2]}
 &=\frac{\ell^2k^2-(\ell\cdot k)^2}
         {(\ell^2)^2[(\ell+k)^2+m^2]},\\
dF_3&=2\,dx_1dx_2dx_3\,
       \delta(x_1+x_2+x_3-1),\qquad x_i\ge0,\\
q&=\ell+x_3k,\qquad
D=x_3m^2+x_3(1-x_3)k^2,\\
\int dF_3\,h(x_3)
 &=2\int_0^1dx_3\,(1-x_3)h(x_3),\qquad
\int dF_3=1 .
\end{aligned}
\tag{65.21}
$$

因子2是三分母参数公式中的$\Gamma(3)$；消去$x_2$后，$x_1$从0积到$1-x_3$，才产生最后一行的权重。虽然两个分母相同，它们仍占据两个参数位置，不能少计这个权重。

分子在平移后有一个有用的精确相消：
<span id="eq:c65-scalar-numerator"></span>

$$
\begin{aligned}
N&=(q-x_3k)^2k^2-(q\cdot k-x_3k^2)^2\\
 &=q^2k^2-2x_3(q\cdot k)k^2+x_3^2(k^2)^2\\
 &\quad-(q\cdot k)^2+2x_3(q\cdot k)k^2-x_3^2(k^2)^2\\
 &=q^2k^2-(q\cdot k)^2
 \ \longrightarrow\ \left(1-\frac1d\right)q^2k^2 .
\end{aligned}
\tag{65.22}
$$

关于$q$的一次项在求角平均以前就已精确相消。剩下的积分可用$q^2=(q^2+D)-D$拆开：
<span id="eq:c65-q2-cubic-pole"></span>

$$
\begin{aligned}
\widetilde\mu^\varepsilon
   \int_q\frac{q^2}{(q^2+D)^3}
 &=J_2(D)-DJ_3(D),\\
J_3(D)
 &=\frac{i}{32\pi^2D}+O(\varepsilon),\\
J_2(D)-DJ_3(D)
 &=\frac{i}{16\pi^2}
       \left[\frac2\varepsilon-\ln\frac D{\mu^2}
                         -\frac12+O(\varepsilon)\right].
\end{aligned}
\tag{65.23}
$$

第一项有极点，$DJ_3$没有，因此本式与$J_2$具有相同的极点系数。对空间样外动量，$D$在$x_3=0$的一次零点只给可积的$\ln x_3$；提取这里的紫外系数不引入新的红外极点。

将三参数归一与$d\to4$时的$1-1/d=3/4$相乘，泡图的极部为$4e^2(3/4)i k^2/(8\pi^2\varepsilon)$。于是
<span id="eq:c65-scalar-self-poles"></span>

$$
i\Pi_\varphi(k^2)\big|_{\rm pole}
 =i\left[
 \left(\frac{3e^2}{8\pi^2\varepsilon}-\delta Z_2\right)k^2
 +\left(\frac{\lambda}{8\pi^2\varepsilon}-\delta Z_m\right)m^2
 \right].
\tag{65.24}
$$

两个独立的局部结构分别给
<span id="eq:c65-z2-zm"></span>

$$
Z_2=1+\frac{3e^2}{8\pi^2\varepsilon}
                  +\text{更高圈项},\qquad
Z_m=1+\frac{\lambda}{8\pi^2\varepsilon}
                  +\text{更高圈项}.
\tag{65.25}
$$

$Z_2$中的电磁项依赖这里的横向规范。$Z_m$是拉氏量质量项的因子；把场重新归一以后，裸质量平方含的是$Z_m/Z_2$，所以本式并不意味着电磁相互作用不影响质量参数的运行。

<span id="c65-three-vertex"></span>

## 用特殊外动量求三点顶角的极部

三点顶角的表面发散度为1。在一个圈图中，每条内线给两个分母幂，每个三价导数顶角至多给一个圈动量，故$\delta=4L-2I+V_3$。若把各类四价顶角的总数记为$V_4$，则连通图满足$L=I-V_3-V_4+1$，线端计数给$3V_3+4V_4=2I+E$。先消去$L$，得到$\delta=4+2I-3V_3-4V_4$，再用后一关系就得$\delta=4-E$。对于两个标量和一个光子的局部反项，洛伦兹协变性只允许一次外动量。电荷共轭使$A_\mu$反号而保持$\varphi^\dagger\varphi$，所以排除$A_\mu\partial^\mu(\varphi^\dagger\varphi)$，留下的正是式[（65.1）](#eq:c65-lagrangian)中的电流耦合。因此只要求出一个能测到其系数的动量配置，就能确定紫外反项。

取入射标量动量为零，入射光子和出射标量动量均为$k$。这是一组用于格林函数的离壳动量。内部光子的动量记$\ell$。

![零入射标量动量下的四幅三点顶角圈图](/images/srednicki/s65-c65_03.svg)

图65c：四幅图依次是左接触顶角的混合泡、三个导数顶角的三角图、右接触顶角的混合泡，以及含四标量顶角的标量圈。第二、第三幅图的左端给$\ell^\mu P_{\mu\nu}(\ell)=0$；第四幅的积分由参数交换为零。<span id="c65-three-figure"></span>

第二、第三幅图的左端，外标量动量为零，三点顶角只给$ie\ell^\mu$。它立即被内部光子的横向投影消去。余下第一幅的相位为
$(ie)(-2ie^2)(1/i)^2=-2e^3$，第四幅为
$(-i\lambda)(ie)(1/i)^2=-e\lambda$。因此
<span id="eq:c65-three-integrals"></span>

$$
\begin{aligned}
iV_3^\mu(k,0)
 &=ieZ_1k^\mu
   -2e^3\widetilde\mu^\varepsilon\int_\ell
      \frac{P^\mu{}_\rho(\ell)(\ell+2k)^\rho}
           {\ell^2[(\ell+k)^2+m^2]}\\
 &\quad-e\lambda\widetilde\mu^\varepsilon\int_\ell
      \frac{(2\ell+k)^\mu}
           {(\ell^2+m^2)[(\ell+k)^2+m^2]} .
\end{aligned}
\tag{65.26}
$$

先看$\lambda$项。用与光子自能相同的参数和移位，积分化为
<span id="eq:c65-three-lambda-zero"></span>

$$
\begin{aligned}
B^\mu(k)
 &=\widetilde\mu^\varepsilon
   \int_0^1dx\int_q
       \frac{2q^\mu+(1-2x)k^\mu}
            {[q^2+m^2+x(1-x)k^2]^2}\\
 &=k^\mu\int_0^1dx\,(1-2x)
                  J_2\big(m^2+x(1-x)k^2\big)=0 .
\end{aligned}
\tag{65.27}
$$

第一项对$q$为奇；剩下一项在$x\mapsto1-x$时，分母不变，分子反号，故也为零。这是该图整个积分的相消，不仅是其极点的相消。

在第一幅图中，$P\ell=0$已经提出一个$2k^\rho$。为确定一次动量反项，只需分母的零阶展开：
<span id="eq:c65-three-uv-expansion"></span>

$$
\begin{aligned}
\frac1{(\ell+k)^2+m^2}
 &=\frac1{\ell^2+m^2}
   -\frac{2\ell\cdot k+k^2}
     {(\ell^2+m^2)[(\ell+k)^2+m^2]},\\
P^\mu{}_\rho(\ell)k^\rho
 &\ \longrightarrow\
 \left(1-\frac1d\right)k^\mu
 \quad\text{在径向分母的圈积分中}.
\end{aligned}
\tag{65.28}
$$

第一行余项在大$\ell$处至少多衰减一个幂，所以在已经提出外动量的图中不再产生原来的对数发散。零阶分母包含$m>0$，其小$\ell$行为为$1/\ell^2$，在四维附近局部可积。这里的外动量选择因而保留了所需紫外极点。

记这个混合质量积分为
<span id="eq:c65-mixed-mass-integral"></span>

$$
\begin{aligned}
J_{11}(m^2)
 &:=\widetilde\mu^\varepsilon
       \int_\ell\frac1{\ell^2(\ell^2+m^2)}
   =\int_0^1dx\,J_2(xm^2),\\
J_{11}(m^2)\big|_{\rm pole}
 &=\frac{i}{8\pi^2\varepsilon}.
\end{aligned}
\tag{65.29}
$$

有限部分中的$\int_0^1\ln x\,dx=-1$也是收敛的。于是式[（65.26）](#eq:c65-three-integrals)的极部为
<span id="eq:c65-z1"></span>

$$
\begin{aligned}
\frac{V_3^\mu(k,0)}e\bigg|_{\rm tree+pole}
 &=\left[Z_1-\frac{4e^2}{8\pi^2\varepsilon}
                          \left(1-\frac14\right)\right]k^\mu\\
 &=\left[Z_1-\frac{3e^2}{8\pi^2\varepsilon}\right]k^\mu,\\
Z_1&=1+\frac{3e^2}{8\pi^2\varepsilon}
                         +\text{更高圈项}.
\end{aligned}
\tag{65.30}
$$

这与$Z_2$相同。此前我们分别从标量动能和电磁三点函数确定两者，现在由具体图的计算看到了规范对称性对它们的联系。

<span id="c65-mixed-four"></span>

## 两标量两光子顶角中的相消

这个四点函数的表面发散度为零，树顶角也与外动量无关。把全部外动量置零以后，只要外标量通过三点顶角接到内部光子上，就又出现$\ell^\mu P_{\mu\nu}=0$。留下图65d中的三类图。

![二标量二光子顶角的三个非零圈图类别](/images/srednicki/s65-c65_04.svg)

图65d：全部外动量为零。三类分别含两个接触顶角、一个四标量及两个三点顶角、一个四标量及一个接触顶角。前两类还各有一次$\mu\leftrightarrow\nu$的外光子排列，故各取两份；第三类的两个光子已经接在同一个顶角。<span id="c65-mixed-four-figure"></span>

外动量相同并不使两条带标签的外光子变成同一条线。第一类的两个光子可以分别接到左右接触顶角；第二类的两个三点顶角也可交换外光子身份。因此前两类各乘2。把相位、导数和这一排列数合起来，有
<span id="eq:c65-mixed-four-weights"></span>

$$
\begin{aligned}
c_a&=2(-2ie^2)^2(1/i)^2=8e^4,\\
c_b&=2(ie)^2(-i\lambda)(1/i)^3\frac4d
                  =-\frac8d e^2\lambda,\\
c_c&=(-i\lambda)(-2ie^2)(1/i)^2=2e^2\lambda .
\end{aligned}
\tag{65.31}
$$

第二行的$4/d$来自$(2\ell)^\mu(2\ell)^\nu$的角平均。第一行仍保留内部光子的投影。因此三个圈贡献为
<span id="eq:c65-mixed-four-integrals"></span>

$$
\begin{aligned}
\Delta(iV_4^{\mu\nu})
 &=8e^4\widetilde\mu^\varepsilon
       \int_\ell\frac{P^{\mu\nu}(\ell)}
                    {\ell^2(\ell^2+m^2)}\\
 &\quad-\frac8d e^2\lambda g^{\mu\nu}
       \widetilde\mu^\varepsilon
            \int_\ell\frac{\ell^2}{(\ell^2+m^2)^3}
       +2e^2\lambda g^{\mu\nu}J_2(m^2).
\end{aligned}
\tag{65.32}
$$

后两项在整个积分层面相消。对同一个$d$维积分作一次分部积分：
<span id="eq:c65-mixed-lambda-cancellation"></span>

$$
\begin{aligned}
0&=\widetilde\mu^\varepsilon
 \int_\ell\frac{\partial}{\partial\ell^\rho}
        \frac{\ell^\rho}{(\ell^2+m^2)^2}\\
 &=dJ_2(m^2)
      -4\widetilde\mu^\varepsilon
          \int_\ell\frac{\ell^2}{(\ell^2+m^2)^3},\\
-\frac8d e^2\lambda\left(\frac d4J_2\right)
       +2e^2\lambda J_2&=0 .
\end{aligned}
\tag{65.33}
$$

所以在全零外动量、相同维数调节下，$\lambda$相关的这两个贡献连有限部分也恰好相消。若先在张量平均中把$d$取为4，再保留其余积分的有限部分，便会破坏这里的精确联系。

第一项平均$P^{\mu\nu}$后给$(1-1/d)g^{\mu\nu}J_{11}$。加上树项，得到
<span id="eq:c65-z4"></span>

$$
\begin{aligned}
\frac{V_4^{\mu\nu}(0,0,0)}{e^2}
    \bigg|_{\rm tree+pole}
 &=\left[-2Z_4+\frac{8e^2}{8\pi^2\varepsilon}
                       \left(1-\frac14\right)\right]g^{\mu\nu}\\
 &=\left[-2Z_4+\frac{3e^2}{4\pi^2\varepsilon}\right]g^{\mu\nu},\\
Z_4&=1+\frac{3e^2}{8\pi^2\varepsilon}
                       +\text{更高圈项}.
\end{aligned}
\tag{65.34}
$$

树顶角为$-2e^2g^{\mu\nu}$，所以消去圈极点所需的反项是$\delta Z_4=3e^2/(8\pi^2\varepsilon)$。

<span id="c65-four-scalar"></span>

## 四标量顶角与不可省去的四次耦合

最后一个局部四点函数有四条标量外线。仍取全零外动量，横向性消去所有外标量经三点顶角接到内部光子的图。余下的五幅图必须继续保留外线身份：1、2入射，3、4出射。

![保留四条外线标签的五幅四标量顶角圈图](/images/srednicki/s65-c65_05.svg)

图65e：前两幅为光子泡，外线配对分别是$(13|24)$与$(14|23)$；第三幅是$(12|34)$的同向标量泡，后两幅为$(13|24)$与$(14|23)$的异向标量泡。五幅权重依次为$1/2,1/2,1/2,1,1$。<span id="c65-four-scalar-figure"></span>

每个双光子接触顶角含一条入、一条出标量，因而光子泡只能有前两种外线分配。固定外标签以后，两条内部光子仍可以交换，两个图的对称因子都为2。第三幅的两条内部标量沿同一方向流动，也可以交换，故同样取$1/2$。后两幅的内部标量箭头相反，交换内线会改变有向图，因而各取1。对称因子中的图自同构固定每一条外线；交换整组外线得到的是另一种外线分配。

也可以直接数带标签的威克收缩。将两个插入点分别记为$x,y$，保留展开系数$1/2!$。两个海鸥顶角的单项式系数为1；两个四标量顶角则另带$(1/4)^2$。对每一种无序外线分配，把$x,y$两种标记都计入，有：

| 内部线与外线分配         | 收缩数 | 单项式及展开系数 | 除以完整顶角乘积后的权重 |
| ------------------------ | -----: | ---------------: | -----------------------: |
| 光子泡，$(13\mid24)$     |      4 |            $1/2$ |     $4/(2\times2^2)=1/2$ |
| 光子泡，$(14\mid23)$     |      4 |            $1/2$ |                    $1/2$ |
| 同向标量泡，$(12\mid34)$ |     16 |           $1/32$ |                    $1/2$ |
| 异向标量泡，$(13\mid24)$ |     32 |           $1/32$ |                      $1$ |
| 异向标量泡，$(14\mid23)$ |     32 |           $1/32$ |                      $1$ |

表中海鸥顶角的完整树系数含因子2，四标量顶角的完整树系数为1；电荷、四次耦合和共同相位已提出。光子泡每一种分配有两种顶角标记和两种光子配对，共4次收缩。同向标量泡在固定顶角标记下有$2!\,2!$种外端连接、$2!$种内线连接，共8次；异向标量泡的四个外端各有两个同类场可选，共16次。再乘两种顶角标记，就得到表中计数。

光子泡的洛伦兹缩并是两个投影的迹：
<span id="eq:c65-projector-trace"></span>

$$
\begin{aligned}
g^{\mu\nu}P_{\nu\rho}(\ell)
       g^{\rho\sigma}P_{\sigma\mu}(\ell)
 &=P^\mu{}_\rho P^\rho{}_\mu
   =\operatorname{tr}P^2
   =\operatorname{tr}P=d-1 .
\end{aligned}
\tag{65.35}
$$

闭链中每个内部洛伦兹指标都出现两次，缩并结果为投影的迹$d-1$。两个接触顶角与两条光子内线给$(-2ie^2)^2(1/i)^2=4e^4$。两四标量顶角及两条标量内线则给$(-i\lambda)^2(1/i)^2=\lambda^2$。于是
<span id="eq:c65-four-scalar-integrals"></span>

$$
\begin{aligned}
iV_{4\varphi}(0,0,0)
 &=-iZ_\lambda\lambda
   +\left(\frac12+\frac12\right)4e^4(d-1)J_2(m_\gamma^2)\\
 &\quad+\left(\frac12+1+1\right)\lambda^2J_2(m^2)\\
 &=-iZ_\lambda\lambda
       +4e^4(d-1)J_2(m_\gamma^2)
       +\frac52\lambda^2J_2(m^2).
\end{aligned}
\tag{65.36}
$$

这里的光子泡与前面的光子蝌蚪有不同的红外行为。它的积分是$J_2(m_\gamma^2)\propto(m_\gamma^2)^{-\varepsilon/2}$，在固定正$\varepsilon$时随$m_\gamma\to0$发散。若从一开始把$m_\gamma$也置零，维数调节会把这个没有尺度的积分记成零，同时隐去原本需要提取的紫外极点。因此先在$m_\gamma>0$时确定极部；红外质量不参与最终的紫外反项。

将式[（65.13）](#eq:c65-j2-pole)用于两个质量，圈项中的$d-1$只在极点系数中取3，得到
<span id="eq:c65-four-scalar-poles"></span>

$$
V_{4\varphi}(0,0,0)\big|_{\rm tree+pole}
 =-Z_\lambda\lambda
   +\frac{3e^4}{2\pi^2\varepsilon}
   +\frac{5\lambda^2}{16\pi^2\varepsilon}.
\tag{65.37}
$$

本式是$V$，前式计算的是$iV$；整体除以$i$以后，树项和圈项都按同一规则变换。

消去极点便给
<span id="eq:c65-zlambda"></span>

$$
Z_\lambda
 =1+\frac1\varepsilon
      \left(\frac{3e^4}{2\pi^2\lambda}
                    +\frac{5\lambda}{16\pi^2}\right)
      +\text{更高圈项}.
\tag{65.38}
$$

以上用乘法因子$Z_\lambda$表示四次项的重整化。当$\lambda$趋零时，更合适的是保留作用量里真正出现的乘积：
<span id="eq:c65-additive-quartic"></span>

$$
Z_\lambda\lambda=\lambda+\delta\lambda,\qquad
\delta\lambda
 =\frac1\varepsilon
       \left(\frac{3e^4}{2\pi^2}
                    +\frac{5\lambda^2}{16\pi^2}\right)
       +\text{更高圈项}.
\tag{65.39}
$$

即使先把树级$\lambda$设为零，两个光子泡仍产生四标量发散。因此局部四次项必须保留，正好实现了第61节引入它时所指出的可重整性要求。取$e=0$则只剩三个有向标量泡，它们的权重和$5/2$给出纯复标量理论的结果。

这次计算还得到$Z_1,Z_2,Z_4$的相同一圈极部。记$a=3e^2/(8\pi^2\varepsilon)$，在同一微扰阶上
<span id="eq:c65-gauge-z-check"></span>

$$
\frac{Z_1^2}{Z_2}
 =\frac{1+2a+O(\text{二圈})}
        {1+a+O(\text{二圈})}
 =1+a+O(\text{二圈})=Z_4 .
\tag{65.40}
$$

下面先从量子作用量求出低能顶角的归一条件，再由有限规范变换推导这些重整化因子的关系。

<span id="c65-os-charge"></span>

## 在壳物理电荷与软顶角

以下取$m>0$，在保留红外调节的微扰理论中定义标量极点及其导数；
先作紫外减除，再讨论软光子的边界。
标量内线为$-i/K(p^2)$，其在壳归一是
<span id="eq:c65-ex-1-os-propagator"></span>

$$
\begin{aligned}
K(z)&=z+m^2-\Pi_\varphi(z),\qquad z=p^2,\\
K(-m^2)&=0,\qquad K'(-m^2)=1,\\
\Pi_\varphi(-m^2)&=0,\qquad \Pi_\varphi'(-m^2)=0.
\end{aligned}
\tag{65.41}
$$

物理横向光子的单位留数另由$\Pi_\gamma(0)=0$固定，
如[第62节](/posts/srednicki-62/)的在壳方案。
这里的$m$因这些条件而成为物理质量；
它与前面$\overline{\mathrm{MS}}$计算中尚未施加这些条件的质量参数含义不同。
下面未写出的虚光子红外调节始终保留在$\Pi_\varphi$及顶角函数中。

<span id="c65-ward-identities"></span>

### 从局域相位到三点、四点关系

先以$\mathfrak e$表示局域相位中的常数，暂不预先把它等同于物理电荷。
对平滑紧支撑函数$\chi(x)$，采用
<span id="eq:c65-ex-1-local-phase"></span>

$$
A_\mu^\chi=A_\mu-\partial_\mu\chi,\qquad
\varphi^\chi=U\varphi,\qquad
\varphi^{\dagger\chi}=\varphi^\dagger U^{-1},
\qquad U=e^{-i\mathfrak e\chi}.
\tag{65.42}
$$

相应反项与这一变换的相容条件将在[下文](#c65-finite-gauge)求出。
量子恒等式所需的变元论证可沿用
[第63节的量子规范恒等式](/posts/srednicki-63/#c63-gauge-constraint)：标量的两组积分变量$\varphi,\varphi^\dagger$
分别产生$\det U$与$\det U^{-1}$，在共同调节下相消；
光子场平移的雅可比行列式为1。
标量线性源$\eta^\dagger\varphi+\varphi^\dagger\eta$的变分分别为
$-i\mathfrak e\eta^\dagger\chi\varphi$与
$+i\mathfrak e\varphi^\dagger\chi\eta$。
这些项对场都是线性的，取期望后可直接用平均场替换。
因此相同的勒让德变换给
$\delta\Gamma=\delta S_{\rm br}$：
二次规范固定项以及作为红外调节的二次光子质量项，其已知变分留在
$S_{\rm br}[A]$中；减去它们后，$\widehat\Gamma=\Gamma-S_{\rm br}$
满足局域相位不变性。调节及反项取成与矢量规范对称相容。

抽出$\widehat\Gamma$中恰含一对标量平均场的部分，定义完整逆核：
<span id="eq:c65-ex-1-kernel-covariance"></span>

$$
\begin{aligned}
\widehat\Gamma\big|_{\varphi^\dagger\varphi}
 &=-\int d^4x\,d^4y\,
       \varphi^\dagger(x)\mathcal K[A](x,y)\varphi(y),\\
\mathcal K[A-\partial\chi](x,y)
 &=U(x)\mathcal K[A](x,y)U^{-1}(y).
\end{aligned}
\tag{65.43}
$$

第二行由第一行对任意$\varphi,\varphi^\dagger$不变得到。
所有顶角均取自完整1PI量子作用量。
令$q=p'-p$，第二个光子的入动量为$q-k$，
并沿$e^{ipx}$的傅里叶约定展开：
<span id="eq:c65-ex-1-kernel-expansion"></span>

$$
\begin{aligned}
\mathcal K[A](p',p)
 ={}&(2\pi)^4\delta^4(q)K(p^2)-V_3^\mu(p',p)A_\mu(q)\\
 &-\frac12\int\frac{d^4k}{(2\pi)^4}\,
 V_4^{\mu\nu}(k,p',p)A_\mu(k)A_\nu(q-k)+O(A^3).
\end{aligned}
\tag{65.44}
$$

两个光子是相同玻色场，故二次项有$1/2!$。
作用量前面的负号使核内的两个顶角系数都带负号；
例如树级常背景给
$\mathcal K[A]=(p-eA)^2+m^2$，
恰好对应$V_3^\mu=e(p'+p)^\mu$和$V_4^{\mu\nu}=-2e^2g^{\mu\nu}$。

对式[（65.43）](#eq:c65-ex-1-kernel-covariance)取$\chi$的一次项和$A$的零次项。
左边由$\delta A_\mu(q)=-iq_\mu\chi(q)$得到，
右边由相位作用在核的两端得到：
<span id="eq:c65-ex-1-three-ward"></span>

$$
\begin{aligned}
\delta\mathcal K(p',p)
 &=iq_\mu V_3^\mu(p',p)\chi(q)\\
 &=i\mathfrak e\,[K(p'^2)-K(p^2)]\chi(q),\\
q_\mu V_3^\mu(p',p)
 &=\mathfrak e\,[K(p'^2)-K(p^2)].
\end{aligned}
\tag{65.45}
$$

在固定红外调节下取任意方向的$q\to0$，逐项比较$q$的一次系数，
即得零转移关系
<span id="eq:c65-ex-1-three-soft"></span>

$$
V_3^\mu(p,p)=\mathfrak e\,\frac{\partial K(p^2)}{\partial p_\mu}
            =2\mathfrak e\,p^\mu K'(p^2).
\tag{65.46}
$$

这里$\partial p^2/\partial p_\mu=2p^\mu$，度规仍为$(-,+,+,+)$。
由于式[（65.41）](#eq:c65-ex-1-os-propagator)已把外标量留数定为1，
物理电荷的定义就是
<span id="eq:c65-ex-1-charge-condition"></span>

$$
\left.V_3^\mu(p,p)\right|_{p^2=-m^2}=2e\,p^\mu,
\qquad\mathfrak e=e.
\tag{65.47}
$$

若将两条标量腿均放在壳上，可写
$V_3^\mu=e[(p'+p)^\mu F(q^2)+q^\mu G(q^2)]$。
它们是此时可用的两个洛伦兹向量；
式[（65.45）](#eq:c65-ex-1-three-ward)给$q^2G(q^2)=0$。
在$q^2\ne0$先得$G=0$，再以固定调节下的连续边界到达$q^2=0$，
所以电荷条件也可写成$F(0)=1$。非零$q^2$处的$F$描述电荷分布的动量依赖。

再取式[（65.43）](#eq:c65-ex-1-kernel-covariance)中恰含一份$\chi(k)$
和一份$A_\nu(q-k)$的系数。核内二次项的两个光子位置各产生一次变分，
正好抵消$1/2$；核两端的相位则分别平移出、入标量动量：
<span id="eq:c65-ex-1-four-ward"></span>

$$
\begin{aligned}
\delta\mathcal K\big|_{\chi A}
 &=i k_\mu V_4^{\mu\nu}(k,p',p)\chi(k)A_\nu(q-k),\\
\delta\mathcal K\big|_{\chi A}
 &=ie\,[V_3^\nu(p'-k,p)-V_3^\nu(p',p+k)]
       \chi(k)A_\nu(q-k),\\
k_\mu V_4^{\mu\nu}(k,p',p)
 &=e\,[V_3^\nu(p'-k,p)-V_3^\nu(p',p+k)].
\end{aligned}
\tag{65.48}
$$

代入树级三点核，右边为$-2e^2k^\nu$，
与左边的$V_4^{\mu\nu}=-2e^2g^{\mu\nu}$一致，因而这里的差分次序已固定。
在顶角关于软动量可微的调节设置下，对$k$的一次系数比较给
<span id="eq:c65-ex-1-four-soft-one"></span>

$$
V_4^{\mu\nu}(0,p',p)
 =-e\left(\frac{\partial}{\partial p'_\mu}
          +\frac{\partial}{\partial p_\mu}\right)V_3^\nu(p',p).
\tag{65.49}
$$

然后令$p'=p$。括号内的两个导数正是沿对角线$p'=p$的全导数，
因此第二个光子也变软时，
<span id="eq:c65-ex-1-four-hessian"></span>

$$
\begin{aligned}
V_4^{\mu\nu}(0,p,p)
 &=-e^2\frac{\partial^2K(p^2)}{\partial p_\mu\partial p_\nu}\\
 &=-2e^2g^{\mu\nu}K'(p^2)
   -4e^2p^\mu p^\nu K''(p^2).
\end{aligned}
\tag{65.50}
$$

这一步显式给出了完整1PI四点核中可能存在的第二个张量结构。
在标量质量壳上，它成为
<span id="eq:c65-ex-1-four-os-tensor"></span>

$$
\left.V_4^{\mu\nu}(0,p,p)\right|_{p^2=-m^2}
 =-2e^2g^{\mu\nu}
   +4e^2p^\mu p^\nu\Pi_\varphi''(-m^2).
\tag{65.51}
$$

二阶导数$\Pi_\varphi''(-m^2)$由在壳附近的曲率决定。
例如局部展开$K(z)=z+m^2+\zeta(z+m^2)^2$满足同样的极点与单位留数，
但给四点核增添$-8e^2\zeta p^\mu p^\nu$，
其中$\zeta$的质量维数为$-2$。
这里的$\zeta$代表完整动量函数在壳附近的泰勒系数，由圈修正确定。

<span id="c65-thomson"></span>

### 四点条件与汤姆孙散射

对在壳时间样动量$p^2=-m^2$，定义投到其静止空间的投影张量
<span id="eq:c65-ex-1-rest-projector"></span>

$$
\mathcal P^{\mu\nu}(p)=g^{\mu\nu}+\frac{p^\mu p^\nu}{m^2},
\qquad
\mathcal P^{\mu\nu}p_\nu=0,\qquad
\mathcal P^\mu{}_\alpha\mathcal P^{\alpha\nu}=\mathcal P^{\mu\nu}.
\tag{65.52}
$$

式[（65.51）](#eq:c65-ex-1-four-os-tensor)在这个空间内的归一条件为
<span id="eq:c65-ex-1-four-os-projection"></span>

$$
\left.
\mathcal P^\mu{}_\alpha\mathcal P^\nu{}_\beta
V_4^{\alpha\beta}(0,p,p)\right|_{p^2=-m^2}
 =-2e^2\mathcal P^{\mu\nu}.
\tag{65.53}
$$

等价地，若$v\cdot p=w\cdot p=0$，
则$v_\mu w_\nu V_4^{\mu\nu}(0,p,p)=-2e^2v\cdot w$。
这保留了质量壳上的物理横向响应，同时容许
式[（65.51）](#eq:c65-ex-1-four-os-tensor)所要求的$p^\mu p^\nu$项。

在入射标量静止系，这一条件直接给出汤姆孙极限。
取$p=(m,\mathbf0)$，入、出光子动量分别为$k,k'$，
满足$k^2=k'^2=0$且$p'=p+k-k'$在壳。
入光子偏振取$\epsilon_{\rm in}^{\mu *}$，
出光子取$\epsilon_{\rm out}^{\nu}$。
选取两者的时间分量均为零的横向规范代表，则
<span id="eq:c65-ex-1-thomson-polarizations"></span>

$$
\begin{aligned}
p\cdot\epsilon_{\rm in}^*
 &=p\cdot\epsilon_{\rm out}=0,\\
k\cdot\epsilon_{\rm in}^*
 &=k'\cdot\epsilon_{\rm out}=0.
\end{aligned}
\tag{65.54}
$$

两个单标量交换项各含一个消失的端点收缩。
在吸收入光子的那个初态端点，
$V_3^\mu(p+k,p)$只能是$p^\mu$与$k^\mu$的线性组合，
因而它与$\epsilon_{\rm in}^{\mu *}$的收缩为零；
另一个交换项的初态端点为$V_3^\nu(p-k',p)$，
同理被$\epsilon_{\rm out}^{\nu}$消去。
在非零频率上完成这一收缩后，便可安全地取交换项的软极限。
在电荷共轭不破缺的零背景真空中，
$A\mapsto-A$、$\varphi\leftrightarrow\varphi^\dagger$
使零标量背景的量子作用量为$A$的偶函数，
故其三光子1PI系数为零，不存在额外的三光子交换项。
剩下的完整二标量二光子1PI核在双软边界由
式[（65.53）](#eq:c65-ex-1-four-os-projection)确定：
<span id="eq:c65-ex-1-thomson-amplitude"></span>

$$
\lim_{\omega\to0}\mathcal T_{\lambda'\lambda}
 =-2e^2\,
 \epsilon_{\rm out}(k')\cdot\epsilon_{\rm in}^*(k).
\tag{65.55}
$$

这里$\omega=k^0$；令$\omega'=k'^0$及$\theta$为两光子夹角，
$p'^2=p^2$给$m(\omega-\omega')=\omega\omega'(1-\cos\theta)$，
从而$\omega'/\omega=[1+(\omega/m)(1-\cos\theta)]^{-1}\to1$。
这就是标量汤姆孙归一。上述微分和软极限均先在固定红外调节下进行，
物理无质量光子的结果取其横向边界。对于有限频率的散射，
可测截面还须合并实、虚软光子造成的红外贡献。

因此三点条件可取式[（65.47）](#eq:c65-ex-1-charge-condition)，
四点条件可取式[（65.53）](#eq:c65-ex-1-four-os-projection)，
并同时保留完整核的式[（65.51）](#eq:c65-ex-1-four-os-tensor)。
若将顶角写为
<span id="eq:c65-ex-1-counterterm-conditions"></span>

$$
\begin{aligned}
V_3^\mu(p',p)&=eZ_1(p'+p)^\mu+V_{3,\mathrm{loop}}^\mu(p',p),\\
V_4^{\mu\nu}(k,p',p)
 &=-2e^2Z_4g^{\mu\nu}
   +V_{4,\mathrm{loop}}^{\mu\nu}(k,p',p),
\end{aligned}
\tag{65.56}
$$

它们固定的是相应物理投影的有限减除部分；
规范恒等式使这两个条件与标量留数相联系。
要得到OS方案的有限$Z$因子，应在这些物理投影上评价圈顶角。
前面的[三点](#c65-three-vertex)与[四点](#c65-mixed-four)计算选择特殊离壳动量，只确定紫外极部，
其有限部分还须按上述在壳条件重新求出。

<span id="c65-finite-gauge"></span>

## 有限规范变换与重整化常数

现在直接考察含独立$Z_1,Z_2,Z_4$的局部拉格朗日量。
为同时讨论互为共轭的两种电荷约定，定义$\sigma=\pm1$，并记
<span id="eq:c65-ex-2-action-sign"></span>

$$
\begin{aligned}
\rho&=\varphi^\dagger\varphi,\qquad
J^\mu=\varphi^\dagger\partial^\mu\varphi
      -(\partial^\mu\varphi^\dagger)\varphi,\\
\mathcal L_\sigma
 &=-Z_2\,\partial_\mu\varphi^\dagger\partial^\mu\varphi
   -i\sigma Z_1eJ^\mu A_\mu-Z_4e^2\rho A_\mu A^\mu\\
 &\hspace{1em}-Z_m m^2\rho-\frac14Z_\lambda\lambda\rho^2
             -\frac14Z_3F_{\mu\nu}F^{\mu\nu}.
\end{aligned}
\tag{65.57}
$$

$\sigma=+1$表示与第61节相容的负交叉项，
$\sigma=-1$表示交换共轭荷支后的正交叉项。
$J^\mu$本身是纯虚的，实$Z_i,e,\lambda$使拉格朗日量厄米。
在$d=4-\varepsilon$的调节中，可把下面每个$e$理解为
$e_d=e\widetilde\mu^{\varepsilon/2}$、每个$\lambda$理解为
$\lambda_d=\lambda\widetilde\mu^\varepsilon$；
两条电磁耦合仍含同一个$e_d$，所以所要证明的无量纲$Z$关系不变。

取标准的局域$U(1)$作用：
在每一点把一个复标量乘以单位模相位，保持$\rho$，
变换连续地连到恒等元，并遵守相位的群合成律。
该相位只依赖该点的规范参数，不依赖场、$A$或规范参数的导数。
若$U(\Gamma_1+\Gamma_2)=U(\Gamma_1)U(\Gamma_2)$且在原点可微，
对$\Gamma_2$求导并令其为零即得
$dU/d\Gamma=U\,U'(0)$；单位模性令$U'(0)=-ic$，$c$为实常数。
故所需的一般形式是
<span id="eq:c65-ex-2-general-phase"></span>

$$
A_\mu'=A_\mu-r_\mu,\qquad
r_\mu=\partial_\mu\Gamma,\qquad
\varphi'=e^{-ic\Gamma}\varphi,\qquad
\varphi^{\dagger\prime}=\varphi^\dagger e^{ic\Gamma}.
\tag{65.58}
$$

规范参数的整体周期在此未作规定；我们只考察上述连通局域变换，
并取通常微扰理论中的非退化动能$Z_2\ne0$及非零$e$。

展开导数可得
<span id="eq:c65-ex-2-transformed-terms"></span>

$$
\begin{aligned}
\partial_\mu\varphi'
 &=e^{-ic\Gamma}(\partial_\mu\varphi-icr_\mu\varphi),\\
\partial_\mu\varphi^{\dagger\prime}
 &=(\partial_\mu\varphi^\dagger+icr_\mu\varphi^\dagger)e^{ic\Gamma},\\
J'^\mu&=J^\mu-2ic\rho r^\mu,\\
\partial_\mu\varphi^{\dagger\prime}\partial^\mu\varphi'
 &=\partial_\mu\varphi^\dagger\partial^\mu\varphi
   +icJ^\mu r_\mu+c^2\rho r_\mu r^\mu.
\end{aligned}
\tag{65.59}
$$

其中$J'$的两个导数项各给$-ic\rho r^\mu$，所以有因子2。
代入线性相互作用时还须同时使用$A'=A-r$；
两者共同决定电流项的系数。
质量项和标量四次项仅依赖$\rho$，而$F'_{\mu\nu}=F_{\mu\nu}$，
它们均不变。剩下的精确差为
<span id="eq:c65-ex-2-full-variation"></span>

$$
\begin{aligned}
\mathcal L_\sigma'-\mathcal L_\sigma
={}&i(\sigma Z_1e-Z_2c)\,J^\mu r_\mu\\
 &+2(Z_4e^2-\sigma Z_1ec)\,\rho A^\mu r_\mu\\
 &+(-Z_2c^2+2\sigma Z_1ec-Z_4e^2)\,\rho r_\mu r^\mu .
\end{aligned}
\tag{65.60}
$$

这是有限$\Gamma$的结果，保留了$(\partial\Gamma)^2$项。
例如交叉作用的变化来自
$-i\sigma Z_1e[(J-2ic\rho r)\cdot(A-r)-J\cdot A]$；
因此$\rho A\cdot r$的贡献为$-2\sigma Z_1ec$，
而$\rho r^2$的贡献为$+2\sigma Z_1ec$，两者的号不同。

规范参数及场的局部取值可任意变化。
先让$\varphi$的相位梯度改变$J^\mu$，而固定$\rho,A,r$，
电流项便要求$c=\sigma eZ_1/Z_2$。
把它代回其余两项，得到
<span id="eq:c65-ex-2-necessity"></span>

$$
\begin{aligned}
c&=\sigma e\frac{Z_1}{Z_2},\\
\mathcal L_\sigma'-\mathcal L_\sigma
 &=e^2\left(Z_4-\frac{Z_1^2}{Z_2}\right)
       \rho\left(2A\cdot r-r^2\right).
\end{aligned}
\tag{65.61}
$$

对非零$\rho$再独立改变$A$与$r$，
就得到必要条件$Z_4=Z_1^2/Z_2$。
这一条件保证拉格朗日量在每一点保持不变，对任意离壳场都成立。

充分性可直接写成一个完整的平方。
在这一关系成立时，定义
<span id="eq:c65-ex-2-covariant-square"></span>

$$
\begin{aligned}
D_{\sigma\mu}&=\partial_\mu-i\sigma e\frac{Z_1}{Z_2}A_\mu,\\
\mathcal L_{\sigma,\mathrm{matter}}
 &=-Z_2(D_{\sigma\mu}\varphi)^\dagger D_\sigma^\mu\varphi
   -Z_m m^2\rho-\frac14Z_\lambda\lambda\rho^2,\\
D_{\sigma\mu}'\varphi'
 &=e^{-ic\Gamma}D_{\sigma\mu}\varphi,\qquad
 c=\sigma eZ_1/Z_2.
\end{aligned}
\tag{65.62}
$$

最后一行中的$-ic\,\partial_\mu\Gamma$来自场相位，
$+ic\,\partial_\mu\Gamma$来自$A_\mu'=A_\mu-\partial_\mu\Gamma$，
所以精确抵消。结合$\rho'= \rho$与$F'=F$，整部拉格朗日量不变，
充要性因而完成。

将两种符号约定分别还原，结论为
<span id="eq:c65-ex-2-two-source-signs"></span>

$$
\begin{aligned}
\text{正交叉项}:\quad&
 \varphi'= \exp\!\left(+ie\frac{Z_1}{Z_2}\Gamma\right)\varphi,\\
\text{负交叉项}:\quad&
 \varphi'= \exp\!\left(-ie\frac{Z_1}{Z_2}\Gamma\right)\varphi,\\
&Z_4=\frac{Z_1^2}{Z_2}.
\end{aligned}
\tag{65.63}
$$

负交叉项在$Z_1=Z_2=1$时恢复相位$e^{-ie\Gamma}$。
正交叉项可通过$\varphi\leftrightarrow\varphi^\dagger$与之对应，
这同时交换粒子与反粒子的电荷。
若$e=0$，所有这些电磁物质耦合已消失，
任意$Z_4$都不影响规范不变性，上述关系便不再是必要条件。
$Z_2=0$则失去这里所用的非退化传播动能，不能套用含$1/Z_2$的推论。

现在把这个局部作用量与物理电荷的归一条件相接。
在第61节相容的荷支上，式[（65.62）](#eq:c65-ex-2-covariant-square)
中的相位系数为$\mathfrak e=eZ_1/Z_2$。
[在壳电荷条件](#c65-os-charge)用标量和光子的物理留数以及零转移顶角将它校准为$e$，
故在同一归一与保持沃德关系的减除方案中
<span id="eq:c65-ex-2-os-ward-z"></span>

$$
Z_1=Z_2,\qquad Z_4=Z_2.
\tag{65.64}
$$

三点荷与两光子接触耦合因而不提供两个彼此独立的物理电荷。
若只取一圈，记$Z_i=1+\delta Z_i$，
充要关系在保留的一圈阶成为
<span id="eq:c65-ex-2-one-loop-z"></span>

$$
\delta Z_4=2\delta Z_1-\delta Z_2.
\tag{65.65}
$$

前面由式[（65.25）](#eq:c65-z2-zm)、[（65.30）](#eq:c65-z1)及[（65.34）](#eq:c65-z4)在横向规范下得到三个相同的
$3e^2/(8\pi^2\varepsilon)$紫外极部，正满足此式。
这里比较的是一圈紫外系数；
在壳有限项由上述物理投影确定。

---

[← 第 64 节](/posts/srednicki-64/) · [章节地图](/srednicki/) · [第 66 节 →](/posts/srednicki-66/)
