---
title: 'Srednicki §47 Gamma 矩阵技术'
date: 2026-09-14
category: 笔记
tags: [物理, 量子场论, Srednicki]
series: 'Srednicki QFT'
srednickiSections: [47]
hideFromHome: true
draft: false
---

<span id="c47"></span>

上一节将自旋求和写成了gamma矩阵的迹。要进一步得到便于代入运动学的答案，还须把这些矩阵消去，化成动量的内积，或化成完全反对称张量与动量的收缩。完成这一步可以直接使用反对易关系和迹的循环性，无须每次都代入四乘四矩阵的分量。下面先计算不同阶数的迹，再处理两端指标缩并的矩阵乘积。

<span id="c47-start"></span>

## 从四维克利福德代数出发

所需的出发点是四条代数关系：
<span id="eq:c47-starting-algebra"></span>

$$
\begin{aligned}
\{\gamma^\mu,\gamma^\nu\}&=-2g^{\mu\nu}I_4,&
\gamma_5^2&=I_4,\\
\{\gamma_5,\gamma^\mu\}&=0,&
\operatorname{tr}I_4&=4 .
\end{aligned}
\tag{47.1}
$$

前三条来自[第36节](/posts/srednicki-36/#c36)的四维表示，最后一条给出旋量空间的维数。本书克利福德关系右端带有负号，因而$(\gamma^0)^2=I_4$，$(\gamma^j)^2=-I_4$，$j=1,2,3$；时间与空间矩阵的平方由此区别开来。我们先在四维中使用这些关系，到了两端指标缩并时，再说明形式维度$d$如何进入计算。

迹的循环性直接来自有限矩阵乘法：$\operatorname{tr}(XY)=\sum_{a,b}X_{ab}Y_{ba}
=\operatorname{tr}(YX)$。把长乘积中的其余因子整体看成$Y$，就可以将一个因子从迹的最前端移到最后端。现在令$\Gamma_n=\gamma^{\mu_1}\cdots\gamma^{\mu_n}$，在每个gamma两侧配上$\gamma_5$，得到
<span id="eq:c47-odd-trace-proof"></span>

$$
\begin{aligned}
\gamma_5\Gamma_n\gamma_5
&=(\gamma_5\gamma^{\mu_1}\gamma_5)
  \cdots(\gamma_5\gamma^{\mu_n}\gamma_5)\\
&=(-1)^n\Gamma_n,\\
\operatorname{tr}\Gamma_n
&=\operatorname{tr}(\gamma_5^2\Gamma_n)
 =\operatorname{tr}(\gamma_5\Gamma_n\gamma_5)
 =(-1)^n\operatorname{tr}\Gamma_n .
\end{aligned}
\tag{47.2}
$$

第一行中，相邻两组之间的$\gamma_5^2$均消为单位矩阵；随后在每组内用一次反对易关系，便从每个gamma得到一个负号。最后利用迹的循环性，把首尾的两个附加因子重新合在一起。当$n$为奇数时，迹等于自身的负值，只能为零，因而
<span id="eq:c47-odd-trace"></span>

$$
\operatorname{tr}(\gamma^{\mu_1}\cdots\gamma^{\mu_{2r+1}})=0.
\tag{47.3}
$$

若迹中还多一个$\gamma_5$，可以先将它从最前端循环移到最后端，再逐次反交换回原位。反交换的次数由普通gamma的个数决定，于是有
<span id="eq:c47-gamma5-odd"></span>

$$
\begin{aligned}
\operatorname{tr}(\gamma_5\Gamma_n)
&=\operatorname{tr}(\Gamma_n\gamma_5)
=(-1)^n\operatorname{tr}(\gamma_5\Gamma_n),\\
\operatorname{tr}(\gamma_5\Gamma_{2r+1})&=0 .
\end{aligned}
\tag{47.4}
$$

实际展开旋量外积中的质量项时，先数清每项含有几个普通gamma，就能用这两条奇数迹恒等式消去许多项；余下的偶数迹再逐阶计算。

<span id="c47-even-traces"></span>

## 两个与四个gamma的迹

先看最简单的两个gamma。循环移动说明交换它们的位置不改变迹，因此可以将交换前后的两个式子相加，再除以二，使迹内出现已知的反对易子：
<span id="eq:c47-two-gamma"></span>

$$
\begin{aligned}
\operatorname{tr}(\gamma^\mu\gamma^\nu)
&=\frac12\operatorname{tr}
  (\gamma^\mu\gamma^\nu+\gamma^\nu\gamma^\mu)\\
&=-g^{\mu\nu}\operatorname{tr}I_4
=-4g^{\mu\nu}.
\end{aligned}
\tag{47.5}
$$

取$\mu=\nu=0$时结果为$4$，空间对角分量则为$-4$，正好对应前面各矩阵的平方。为了直接用于含外动量的旋量链，取任意四矢量$a,b$，记$\slashed a=a_\mu\gamma^\mu$、$(ab)=a^\mu b_\mu$。将矢量分量与矩阵指标缩并，便有
<span id="eq:c47-slash-rules"></span>

$$
\begin{aligned}
\operatorname{tr}(\slashed a\slashed b)
&=a_\mu b_\nu(-4g^{\mu\nu})=-4(ab),\\
\slashed a\slashed b&=-\slashed b\slashed a-2(ab)I_4 .
\end{aligned}
\tag{47.6}
$$

前一式计算二阶迹，后一式负责重排相邻的两个斜线矩阵。内积中两个指标一上一下，时间分量的负号已经包含在$(ab)$中。

有了这个重排关系，四阶迹也能化回二阶迹。记$T_4=\operatorname{tr}(\slashed a\slashed b\slashed c\slashed d)$，将最左端的$\slashed a$逐步移向右端：
<span id="eq:c47-four-gamma-reordering"></span>

$$
\begin{aligned}
T_4
&=-\operatorname{tr}(\slashed b\slashed a\slashed c\slashed d)
  -2(ab)\operatorname{tr}(\slashed c\slashed d)\\
&=\operatorname{tr}(\slashed b\slashed c\slashed a\slashed d)
  +2(ac)\operatorname{tr}(\slashed b\slashed d)
  -2(ab)\operatorname{tr}(\slashed c\slashed d)\\
&=-\operatorname{tr}(\slashed b\slashed c\slashed d\slashed a)
  -2(ad)\operatorname{tr}(\slashed b\slashed c)\\
&\hspace{8mm}
  +2(ac)\operatorname{tr}(\slashed b\slashed d)
  -2(ab)\operatorname{tr}(\slashed c\slashed d).
\end{aligned}
\tag{47.7}
$$

每次越过一个gamma，仍未缩并的矩阵链改变符号，同时产生一项内积乘较短的迹。移到最后以后，首项可以按循环性回到$-T_4$。把它移到左边，就将原四阶迹与三个二阶迹联系起来，得到
<span id="eq:c47-four-gamma-recursion"></span>

$$
\begin{aligned}
2T_4={}&-2(ad)\operatorname{tr}(\slashed b\slashed c)
     +2(ac)\operatorname{tr}(\slashed b\slashed d)\\
     &-2(ab)\operatorname{tr}(\slashed c\slashed d).
\end{aligned}
\tag{47.8}
$$

再对每个二阶迹使用式[（47.6）](#eq:c47-slash-rules)，右边三项依次成为$8(ad)(bc)$、$-8(ac)(bd)$和$8(ab)(cd)$。除以左边的二，便得
<span id="eq:c47-four-gamma-trace"></span>

$$
\operatorname{tr}(\slashed a\slashed b\slashed c\slashed d)
=4\big[(ab)(cd)-(ac)(bd)+(ad)(bc)\big].
\tag{47.9}
$$

四阶迹由此化为三个内积配对，其中交叉配对$(ac)(bd)$带负号。几个特殊选择可以说明这三个配对怎样共同起作用：令$a=b=c=d$，结果为$4(a^2)^2$，与先用$(\slashed a)^2=-a^2I_4$再平方一致；若$a^2=b^2=0$，则$\operatorname{tr}(\slashed a\slashed b\slashed a\slashed b)=8(ab)^2$。后一结果也可先由$(\slashed a\slashed b)^2=-2(ab)\slashed a\slashed b$缩短矩阵链，再取二阶迹求出。

<span id="c47-recursion"></span>

## 任意偶数阶的递推

同一技巧可以计算任意偶数个gamma的迹。其原因在于：无论矩阵链有多长，把第一个因子移到末端时，所产生的补项总比原来的迹少两个因子。为了同时确定这些项的符号，令$T_{2r}(a_1,\ldots,a_{2r})
=\operatorname{tr}(\slashed a_1\cdots\slashed a_{2r})$，并取$T_0=4$。当$\slashed a_1$与第$j$项缩并时，它此前已经越过$j-2$项，所以这一缩并项的系数为$-2(-1)^{j-2}(a_1a_j)$。完全移到末端的那一项则越过$2r-1$项，循环回原位后成为$-T_{2r}$。将它移到左边，有
<span id="eq:c47-general-even-recursion"></span>

$$
\begin{aligned}
2T_{2r}
&=-2\sum_{j=2}^{2r}(-1)^{j-2}(a_1a_j)\,
 T_{2r-2}(a_2,\ldots,\widehat a_j,\ldots,a_{2r}),\\
T_{2r}
&=\sum_{j=2}^{2r}(-1)^{j-1}(a_1a_j)\,
 T_{2r-2}(a_2,\ldots,\widehat a_j,\ldots,a_{2r}).
\end{aligned}
\tag{47.10}
$$

帽号表示删去这一项，其余矢量保留原次序。每递推一次，迹中就减少两个gamma，直至以$T_0=4$结束。例如六阶迹先选$a_1$的五个配对伙伴；选定以后，余下四项有三种配对，合起来就是十五个内积乘积。

还可以把递推的终点直接写成所有完全配对的和。将每对记为$(i_k,j_k)$，取$i_k<j_k$，并按$i_1<\cdots<i_r$排列各对；记$\operatorname{sgn}P$为序列$(i_1,j_1,\ldots,i_r,j_r)$相对于$(1,\ldots,2r)$的排列号，则
<span id="eq:c47-pairing-formula"></span>

$$
T_{2r}
=4(-1)^r\sum_P\operatorname{sgn}P
 \prod_{k=1}^r(a_{i_k}a_{j_k}).
\tag{47.11}
$$

从式[（47.10）](#eq:c47-general-even-recursion)看，每次克利福德收缩贡献一个$-1$，共出现$r$次；将第$j$项移到第一项之后所产生的$(-1)^{j-2}$，则逐步组成剩余的排列号。递推先选第一项的伙伴，再处理余下各项，每个完整配对恰好被选出一次，因此没有额外的阶乘。相应的配对数满足$N_r=(2r-1)N_{r-1}$、$N_0=1$，即$(2r-1)!!$。给定矩阵链以后，这个有限求和便将迹全部化为内积。

<span id="c47-gamma5"></span>

## 含有$\gamma_5$的迹

若乘积中含有多个$\gamma_5$，先用反对易关系将它们移到一起，并记录途中越过普通gamma的次数。每一对$\gamma_5$相乘为单位矩阵，所以最后只剩零个或一个。例如，$\gamma_5\slashed a\slashed b\gamma_5=\slashed a\slashed b$，而$\gamma_5\slashed a\gamma_5=-\slashed a$。对于只剩一个$\gamma_5$的情形，式[（47.4）](#eq:c47-gamma5-odd)已经消去了含奇数个普通gamma的迹，接下来只须考虑偶数个。

计算仍从四维定义出发：
<span id="eq:c47-gamma5-definition"></span>

$$
\gamma_5=i\gamma^0\gamma^1\gamma^2\gamma^3.
\tag{47.12}
$$

先求这个矩阵本身的迹。将四阶迹公式用于$\gamma^0\gamma^1\gamma^2\gamma^3$，三个配对都含有非对角度规分量，因而全部为零：
<span id="eq:c47-gamma5-trace"></span>

$$
\operatorname{tr}\gamma_5
=i\operatorname{tr}(\gamma^0\gamma^1\gamma^2\gamma^3)=0 .
\tag{47.13}
$$

再多两个普通gamma时，可利用迹在相似变换下不变来求其结果。对于任意固定的$\mu,\nu$，选四维中一个与两者都不同的指标$\lambda$，以下$\lambda$不求和。由于$\gamma^\lambda$与$\gamma_5$反交换，而移过$\gamma^\mu\gamma^\nu$时有两次反交换，所以它与这两个普通gamma的乘积对易。令$B=\gamma_5\gamma^\mu\gamma^\nu$，就有
<span id="eq:c47-gamma5-two"></span>

$$
\begin{aligned}
\gamma^\lambda B(\gamma^\lambda)^{-1}&=-B,\\
\operatorname{tr}B
&=\operatorname{tr}\!\left[\gamma^\lambda B(\gamma^\lambda)^{-1}\right]
=-\operatorname{tr}B=0 .
\end{aligned}
\tag{47.14}
$$

这里$\gamma^\lambda$的平方为$\pm I_4$，保证了它可逆；相似变换一面保持迹，一面将矩阵变为其负值，因此迹再次只能为零。这个选择对$\mu=\nu$和$\mu\ne\nu$都成立，因为四维中总有可用的$\lambda$。

接着计算$F^{\mu\nu\rho\sigma}
=\operatorname{tr}(\gamma_5\gamma^\mu\gamma^\nu\gamma^\rho\gamma^\sigma)$。交换任意两个相邻指标时，克利福德关系产生的是$-2g^{\mu\nu}\operatorname{tr}(\gamma_5\gamma^\rho\gamma^\sigma)$一类补项，刚才已经求得这类二阶迹为零。因此$F$完全反对称，有重复指标的分量也随之为零；只要求出一个四指标互异的分量，其余分量便由排列的符号确定。

取$3210$次序，代入$\gamma_5$后，相同的空间矩阵恰好逐对相邻：
<span id="eq:c47-epsilon-normalization"></span>

$$
\begin{aligned}
F^{3210}
&=i\operatorname{tr}
(\gamma^0\gamma^1\gamma^2\gamma^3
 \gamma^3\gamma^2\gamma^1\gamma^0)\\
&=i(-1)^3\operatorname{tr}[(\gamma^0)^2]
=-4i .
\end{aligned}
\tag{47.15}
$$

三个空间gamma的平方各给一个$-1$，时间gamma的平方给$+1$。将四个标签完全反转需要六次交换，属于偶排列，所以取$\epsilon^{0123}=+1$时，也有$\epsilon^{3210}=+1$。由此固定整体系数：
<span id="eq:c47-gamma5-four"></span>

$$
\operatorname{tr}
(\gamma_5\gamma^\mu\gamma^\nu\gamma^\rho\gamma^\sigma)
=-4i\epsilon^{\mu\nu\rho\sigma}.
\tag{47.16}
$$

写成四个普通四矢量的斜线形式时，矢量分量与gamma指标相缩并。逐个保留指标的位置，得到
<span id="eq:c47-epsilon-contraction"></span>

$$
\begin{aligned}
\operatorname{tr}(\gamma_5\slashed a\slashed b\slashed c\slashed d)
&=-4i\epsilon^{\mu\nu\rho\sigma}a_\mu b_\nu c_\rho d_\sigma\\
&=-4i\epsilon_{\mu\nu\rho\sigma}a^\mu b^\nu c^\rho d^\sigma,
\qquad \epsilon_{0123}=-1 .
\end{aligned}
\tag{47.17}
$$

降下四个指标时，只有时间指标引入负号，因此最后的取向分量为$-1$。例如依次取四个坐标基四矢量，第一个斜线矩阵为$\slashed a=-\gamma^0$，其余三个为$\gamma^1,\gamma^2,\gamma^3$，上式于是给出$+4i$；它与式[（47.16）](#eq:c47-gamma5-four)的$0123$分量相差的，正是降低时间指标带来的负号。

含一个$\gamma_5$和更多普通gamma的迹也可以按同一路线计算：先用式[（47.12）](#eq:c47-gamma5-definition)将前者展开成四个具体gamma，再应用偶数递推式[（47.10）](#eq:c47-general-even-recursion)。这个过程始终在四维内进行，最后只留下度规与上述取向张量。

<span id="c47-contractions"></span>

## 两端gamma的缩并

费米子圈图中还会出现两端分别为$\gamma^\mu$和$\gamma_\mu$、中间夹着若干矩阵的乘积。这次所求的对象本身是矩阵，未必处于迹内，因此要直接用克利福德关系将两端移到一起，不能借助迹的循环性。为了给维数正规化作准备，先将度规的完全缩并写成$g^{\mu\nu}g_{\mu\nu}=d$。在具体的四维矩阵中，当然有$d=4$；暂时保留$d$，就能看清维数从何处进入各项系数。

最简单的情形是两端gamma之间没有其它矩阵。度规对称，gamma交换子的缩并为零，只留下反对易的部分，因而
<span id="eq:c47-contract-zero"></span>

$$
\gamma^\mu\gamma_\mu
=\frac12g_{\mu\nu}\{\gamma^\mu,\gamma^\nu\}
=-g_{\mu\nu}g^{\mu\nu}I
=-dI .
\tag{47.18}
$$

中间多一个$\slashed a$时，将最右端的gamma向左移一步，即可利用刚求出的完全缩并：
<span id="eq:c47-contract-one"></span>

$$
\begin{aligned}
\gamma^\mu\slashed a\gamma_\mu
&=\gamma^\mu(-\gamma_\mu\slashed a-2a_\mu I)\\
&=-\gamma^\mu\gamma_\mu\slashed a-2\slashed a
=(d-2)\slashed a .
\end{aligned}
\tag{47.19}
$$

在这个结果中，$d$来自两个gamma的完全缩并，$-2$则来自最右端gamma越过$\slashed a$时的反对易子。把这一步用于更长的矩阵链，就得到缩并的递推关系。

记$A_j=\slashed a_j$、$C_n=\gamma^\mu A_1\cdots A_n\gamma_\mu$，并取$C_0=-dI$。先让最右端gamma越过$A_n$，再将反对易子中的$a_{n\mu}\gamma^\mu$认作$A_n$，便有
<span id="eq:c47-contraction-recursion"></span>

$$
\begin{aligned}
C_n
&=-\gamma^\mu A_1\cdots A_{n-1}\gamma_\mu A_n
  -2a_{n\mu}\gamma^\mu A_1\cdots A_{n-1}\\
&=-C_{n-1}A_n-2A_nA_1\cdots A_{n-1}.
\end{aligned}
\tag{47.20}
$$

第二项的$A_n$位于最左端；若要把它移回最右端，还须逐次加入反对易子产生的补项。保留这个位置，就能看出下文三个gamma的缩并为何出现反序乘积。

先令$A=\slashed a$、$B=\slashed b$、$C=\slashed c$。对于中间有两个因子的情况，递推给出
<span id="eq:c47-contract-two"></span>

$$
\begin{aligned}
\gamma^\mu AB\gamma_\mu
&=-(d-2)AB-2BA\\
&=-(d-2)AB+2AB+4(ab)I\\
&=4(ab)I-(d-4)AB .
\end{aligned}
\tag{47.21}
$$

二因子的缩并已化为内积项和原有矩阵乘积。继续增加一个因子，并代入刚得到的二因子缩并式，有
<span id="eq:c47-contract-three"></span>

$$
\begin{aligned}
\gamma^\mu ABC\gamma_\mu
&=-[4(ab)I-(d-4)AB]C-2CAB\\
&=(d-4)ABC-4(ab)C-2CAB\\
&=(d-4)ABC+2CBA .
\end{aligned}
\tag{47.22}
$$

最后一步将$BA=-AB-2(ab)I$左乘相应因子，得到$2CBA=-2CAB-4(ab)C$，正好合并前一行的两项。因此，三个矢量按$c,b,a$反序出现，是递推中把最后一个因子移到最前面所致。

在四维中，维数差的项消失，上述各式化为
<span id="eq:c47-contractions-four-d"></span>

$$
\begin{aligned}
\gamma^\mu\gamma_\mu&=-4I,&
\gamma^\mu A\gamma_\mu&=2A,\\
\gamma^\mu AB\gamma_\mu&=4(ab)I,&
\gamma^\mu ABC\gamma_\mu&=2CBA.
\end{aligned}
\tag{47.23}
$$

用于维数正规化时则要稍晚再取四维极限。代入$d=4-\varepsilon$后保留的$\varepsilon$项，可能与圈积分中的$1/\varepsilon$极点相乘而留下有限贡献。例如
<span id="eq:c47-evanescent-times-pole"></span>

$$
\frac1{\varepsilon}\gamma^\mu ABC\gamma_\mu
=\frac{2}{\varepsilon}CBA-ABC,
\qquad d=4-\varepsilon .
\tag{47.24}
$$

若在缩并这一步就令$d=4$，右边的有限项便会丢失。这就是计算费米子圈图时需要保留$d$的原因。这里$\varepsilon$是无量纲的维度参数，而费曼分母中的正小量具有质量平方量纲，两者承担不同的调节作用。

<span id="c47-dimensional-gamma5"></span>

## 四维的$\gamma_5$与维数延拓

上述缩并只用到了克利福德关系和$g^\mu{}_\mu=d$，因此可以先得到关于$d$的多项式，再作$d=4-\varepsilon$的形式延拓。需要取迹时，本书仍取归一$\operatorname{tr}1=4$。这里延拓的是代数规则；非整数$d$并不对应一组具有非整数个坐标指标的四阶有限矩阵。

将$\gamma_5$也带入这种延拓时，还要处理它的四维定义。四维中非零的$\epsilon$迹、与所有gamma的反对易性以及迹的循环性，在$d\ne4$时不能全部原样保留，原因可以直接从前面的缩并式看出。把第四个斜线矩阵记为$D=\slashed e$，并记$T=\operatorname{tr}(\gamma_5ABCD)$。先假定本节证明的低阶$\gamma_5$零迹仍然成立；这样一来，交换任意相邻的$A,B,C,D$所产生的补项依旧为零，$T$便仍是四个矢量的完全反对称函数。再由式[（47.20）](#eq:c47-contraction-recursion)多递推一步，有
<span id="eq:c47-contract-four"></span>

$$
\gamma^\mu ABCD\gamma_\mu
=-2CBAD-(d-4)ABCD-2DABC .
\tag{47.25}
$$

同一个两端缩并式可以用两种次序求含$\gamma_5$的迹。先假定$\gamma_5$与参与$d$维缩并的所有gamma都反对易，利用循环性将最右端gamma移到最左端，得到
<span id="eq:c47-gamma5-dim-first"></span>

$$
\begin{aligned}
L&:=\operatorname{tr}(\gamma_5\gamma^\mu ABCD\gamma_\mu)\\
&=\operatorname{tr}(\gamma_\mu\gamma_5\gamma^\mu ABCD)\\
&=-\operatorname{tr}(\gamma_5\gamma_\mu\gamma^\mu ABCD)
=dT .
\end{aligned}
\tag{47.26}
$$

再从刚才求得的四因子缩并式出发。由于$CBAD$和$DABC$相对于$ABCD$都是奇排列，相应的两个迹均为$-T$。代入式[（47.25）](#eq:c47-contract-four)，同一个量便成为
<span id="eq:c47-gamma5-dim-conflict"></span>

$$
L=2T-(d-4)T+2T=(8-d)T,\qquad
(d-4)T=0 .
\tag{47.27}
$$

当$d\ne4$时，两种计算若要相容，就必须有$T=0$，这与四维非零的$\epsilon$迹相冲突。因此，本节含$\gamma_5$的迹公式保留其四维适用范围，而上述维数缩并式按不含$\gamma_5$的代数前提使用。遇到同时包含两者的圈图时，须先规定相应的延拓办法。

<span id="c47-matrix-basis"></span>

## 十六个矩阵组成的基

前面已经求出了习题47.1、47.2所需的零迹和两端缩并。习题47.3进一步问：任意$4\times4$复矩阵能否写成以下五组矩阵的线性组合？

$$
I_4,\qquad \gamma^\mu,\qquad
S^{\mu\nu}=\frac{i}{4}[\gamma^\mu,\gamma^\nu]\ (\mu<\nu),
\qquad \gamma^\mu\gamma_5,\qquad\gamma_5.
$$

这些矩阵的数目为$1+4+6+4+1=16$，恰好等于$4\times4$复矩阵空间的维数。只要证明线性无关，它们就是一组基。取希尔伯特–施密特内积

$$
(X,Y)_{\rm HS}=\operatorname{tr}(X^\dagger Y),\qquad
\|X\|_{\rm HS}^2=\sum_{a,b}|X_{ab}|^2,
$$

然后将问题改写为十六个矩阵的正交性。对任意子集$J=\{\mu_1<\cdots<\mu_r\}\subseteq\{0,1,2,3\}$，定义$\Gamma_J=\gamma^{\mu_1}\cdots\gamma^{\mu_r}$，并令$\Gamma_\varnothing=I_4$。在[第36节的表示](/posts/srednicki-36/#c36)中，$\gamma^0$厄米，三个空间gamma反厄米；结合它们各自的平方，每个gamma都是酉矩阵。因此

<span id="eq:c47-subset-orthogonality"></span>

$$
\Gamma_J^\dagger\Gamma_J=I_4,\qquad
\operatorname{tr}(\Gamma_J^\dagger\Gamma_J)=4.
$$

若$J\ne K$，把$\Gamma_J^\dagger\Gamma_K$中相同指标的gamma移到一起，用平方关系消去。余下的指标正好是非空对称差$J\mathbin{\triangle}K$，每个指标只出现一次，换序只留下整体正负号。余下一个或三个gamma时，迹由奇数迹公式为零；余下两个不同gamma时，迹为$-4g^{\mu\nu}=0$；余下四个时，乘积正比于$\gamma_5$，迹也为零。于是

$$
\operatorname{tr}(\Gamma_J^\dagger\Gamma_K)=4\delta_{JK}.
$$

将$\sum_Jc_J\Gamma_J=0$左乘$\Gamma_K^\dagger$并取迹，立即得到$4c_K=0$。这就证明了十六个有序乘积的线性无关。

它们与开头五组矩阵一一对应：零次和一次乘积给$I_4$和$\gamma^\mu$；当$\mu<\nu$时，$S^{\mu\nu}=(i/2)\gamma^\mu\gamma^\nu$；$\gamma^\mu\gamma_5$中重复的指标消去后，留下其余三个gamma的乘积；$\gamma_5$给四次乘积。每次对应只乘一个非零复数，因而五组矩阵也构成正交基。它们的范数分别为

<span id="eq:c47-basis-norms"></span>

$$
\begin{aligned}
\|I_4\|_{\rm HS}^2
=\|\gamma^\mu\|_{\rm HS}^2
=\|\gamma^\mu\gamma_5\|_{\rm HS}^2
=\|\gamma_5\|_{\rm HS}^2&=4,\\
\|S^{\mu\nu}\|_{\rm HS}^2&=1\quad(\mu<\nu).
\end{aligned}
$$

张量生成元的系数$i/2$使范数平方多了$1/4$。对任意矩阵$X$作正交投影，便得到各个展开系数：

<span id="eq:c47-general-matrix-expansion"></span>

$$
\begin{aligned}
X={}&\frac14\operatorname{tr}(X)I_4
+\frac14\sum_{\mu=0}^3
 \operatorname{tr}[(\gamma^\mu)^\dagger X],\gamma^\mu\\
&+\sum_{\mu<\nu}
 \operatorname{tr}[(S^{\mu\nu})^\dagger X],S^{\mu\nu}\\
&+\frac14\sum_{\mu=0}^3
 \operatorname{tr}[(\gamma^\mu\gamma_5)^\dagger X],\gamma^\mu\gamma_5
+\frac14\operatorname{tr}(\gamma_5X)\gamma_5.
\end{aligned}
$$

这里的和按固定矩阵基逐个求取，厄米共轭已经包含时间与空间gamma的不同厄米性。任意旋量矩阵耦合由此分成标量、矢量、反对称张量、轴矢量和赝标量五部分；[第40节](/posts/srednicki-40/)讨论的双线性量正好覆盖这五组。

---

[← 第 46 节](/posts/srednicki-46/) · [章节地图](/srednicki/) · [第 48 节 →](/posts/srednicki-48/)
