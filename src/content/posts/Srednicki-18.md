---
title: 'Srednicki §18 高阶修正与可重整化性'
date: 2026-09-14
category: 笔记
tags: [物理, 量子场论, Srednicki]
series: 'Srednicki QFT'
srednickiSections: [18]
hideFromHome: true
draft: false
---

<span id="c18"></span>

在六维$\varphi^3$理论中，一圈两点函数的发散由$Z_\varphi,Z_m$吸收，三点函数的发散由$Z_g$吸收，而四点及更多外腿的一圈1PI函数已经有限。把计算推进到更高阶以后，能否仍用有限种系数吸收全部发散，是接下来要解决的问题。如果逐阶调节有限个拉格朗日量系数，就能使每阶结果有限，这个理论便称为可重整化的（renormalizable）。最初漏掉的相互作用也可以补入，只要补入的种类有限，所需的独立参数便不会随计算阶数无限增加。若高阶计算不断要求新的独立局部项，则称为不可重整化理论。

这里考察的是微扰展开中每一阶的紫外发散。第14节已经用归一化条件确定了质量和场的含义，现在须进一步说明所需条件有多少种，以及怎样在含有发散子图的高阶图中使用它们。我们先按圈动量的幂次判断可能出现的发散，再考察其局部结构和子图减除。

<span id="c18-power-counting"></span>

## 从圈动量的幂次开始

先考虑一个具有一般无导数势的实标量场，取

<span id="eq:c18-general-lagrangian"></span>

$$
\mathcal L
=-\frac12Z_\varphi\partial_\mu\varphi\partial^\mu\varphi
-\frac12Z_m m^2\varphi^2
-\sum_{n\ge3}\frac{Z_ng_n}{n!}\varphi^n .
\tag{18.1}
$$

每个$Z$都无量纲，$n$价顶点的费曼规则为$-iZ_ng_n$。本节把势项统一写成负号，因此与前面使用的正号立方相互作用比较时，应取$g_3=-g$。真空项和线性反项仍由[第9节](/posts/srednicki-09/#c09)的真空归一及无蝌蚪条件处理；这里先考察两点及更高点函数。

设一幅连通图有$E$条外腿、$I$条内线和$L$个独立圈，其中$n$价顶点有$v_n$个，总顶点数为$v=\sum_n v_n$。小写$v_n$计数顶点，仍用大写$V_n$表示1PI顶点函数。以下均从图权重中提出总动量守恒delta，并截去外传播子。这样，每个独立圈带来$d$维积分，每条标量内线在大动量下给出两个逆动量幂。先固定各圈动量之间的比例，再将它们同时放大$R$倍，径向积分就具有如下形式：

<span id="eq:c18-superficial-degree"></span>

$$
\int^\infty dR\,R^{dL-1-2I}.
\qquad
\omega(G)=dL-2I .
\tag{18.2}
$$

$\omega$称为表面发散度（superficial degree of divergence）。当$\omega=0$时，径向积分可能出现对数发散；当$\omega>0$时，则可能出现幂发散，所以把$\omega\ge0$列为危险情形。“表面”二字指出了这一步计数的范围：它只考察全部圈动量按固定比例共同变大的区域，一部分动量远大于其余动量的区域还须另行检查。

为了从相互作用的形式直接判断这些危险图，可以把表面发散度改写成耦合的质量维数。[第12节](/posts/srednicki-12/#c12)由动能项得到

<span id="eq:c18-coupling-dimension"></span>

$$
[\varphi]=\frac{d-2}{2},\qquad
[g_n]=d-\frac n2(d-2).
\tag{18.3}
$$

一个$E$腿截肢图的维数，应与候选的$E$价局部顶点相同。把该顶点的系数维数记为$[g_E]=d-E(d-2)/2$；即使原模型没有实际的$g_E$项，仍可用这一形式作维数比较。另一方面，将积分、传播子和各个耦合的维数相加，又得到

<span id="eq:c18-diagram-dimension"></span>

$$
[\text{图}]
=[g_E]
=dL-2I+\sum_n v_n[g_n].
\tag{18.4}
$$

从图的总维数中减去耦合所带的维数，便留下积分本身的表面发散度。因此有

<span id="eq:c18-degree-from-couplings"></span>

$$
\omega(G)=[g_E]-\sum_n v_n[g_n].
\tag{18.5}
$$

这个关系也可以直接从图的连接方式推得。每条内线占两个顶点半边，每条外腿占一个，故$\sum_n nv_n=2I+E$。在连通图中任选一棵生成树，它用$v-1$条边连起全部顶点；其余每条内线各提供一个独立圈，因而$L=I-v+1$。将这两个恒等式代入表面发散度，逐项整理为

<span id="eq:c18-topological-derivation"></span>

$$
\begin{aligned}
\omega
&=d(I-v+1)-2I\\
&=d+(d-2)I-d\sum_n v_n\\
&=d-\frac{d-2}{2}E
-\sum_n v_n\left[d-\frac n2(d-2)\right].
\end{aligned}
\tag{18.6}
$$

因此，式[（18.5）](#eq:c18-degree-from-couplings)反映的是图本身的连接关系，形式上的接触顶点只用于维数比较，无须假定它已经出现在原拉格朗日量中。

若某个顶点含有$r_v$个导数，分子最多会再带来$r_v$个大动量幂，就须相应修改计数及耦合维数：

<span id="eq:c18-derivative-counting"></span>

$$
\omega=dL-2I+\sum_v r_v,\qquad
[g_{n,r}]=d-\frac n2(d-2)-r .
\tag{18.7}
$$

后面出现的$Ap^2$二价反项就是一个例子。具体的张量收缩还可能使分子中的领先项相消，因此按最高动量幂算得的发散度仍只是危险程度的上界。

<span id="c18-negative-dimension"></span>

## 负维耦合为什么不断要求新参数

式[（18.5）](#eq:c18-degree-from-couplings)把高阶图的危险程度与耦合维数联系了起来。若某个独立耦合具有负维数，增加这种顶点就会增大$\omega$，使外腿很多、原先会收敛的图也可能产生局部发散。对于无导数标量势，这个条件等价于

<span id="eq:c18-negative-dimension-bound"></span>

$$
[g_n]<0
\quad\Longleftrightarrow\quad
n>\frac{2d}{d-2},\qquad d>2.
\tag{18.8}
$$

据此，四维的非负维势耦合至多到$\varphi^4$，六维至多到$\varphi^3$。上式除以了$d-2$，所以二维须直接回到式[（18.3）](#eq:c18-coupling-dimension)：此时所有$[g_n]=2$，维数判据不再给出有限的$n$上界，讨论二维多项式理论时应先给定有限的最高幂次。

为了看清负维耦合怎样要求新参数，考虑一个具体的四维例子。取相互作用$-g_6\varphi^6/6!$，其耦合维数为$[g_6]=-2$。将两个六价顶点用两条内线相连，便留下八条外腿，所得一圈图满足

<span id="eq:c18-phi-six-bubble-count"></span>

$$
I=2,\qquad v_6=2,\qquad E=8,\qquad L=1,\qquad\omega=0.
\tag{18.9}
$$

现在求出这个图的发散系数。八条带标签的外腿分成两组，每组四条；交换两组得到同一张图，故分组数为$\binom84/2=35$。对一个固定分组，两条平行内线可以互换，对称因子为2。用收缩数也能得到同一权重：把两个分组分派给展开中的两个顶点有$2!$种方式，每组四个外场占据一个六价顶点有$6!/2!$种方式，剩下的两对内场有$2!$种连接，而展开分母是$2!(6!)^2$。于是每个分组的系数为

<span id="eq:c18-phi-six-combinatorics"></span>

$$
\frac{2!\,(6!/2!)^2\,2!}{2!(6!)^2}=\frac12.
\tag{18.10}
$$

为抽出发散的局部部分，取$m>0$并将外动量置零。两顶点与两条内线的相位相乘为$(-ig_6)^2(1/i)^2=g_6^2$，Wick旋转再带来$i$。采用欧氏球形截断$q^2\le\Lambda^2$，先将积分化为径向形式：

<span id="eq:c18-phi-six-radial-integral"></span>

$$
\begin{aligned}
I_\Lambda
&=\int_{q^2\le\Lambda^2}\frac{d^4q}{(2\pi)^4}
  \frac1{(q^2+m^2)^2}\\
&=\frac1{8\pi^2}\int_0^\Lambda
  \frac{q^3\,dq}{(q^2+m^2)^2}
 =\frac1{16\pi^2}\int_0^{\Lambda^2}
  \frac{t\,dt}{(t+m^2)^2}.
\end{aligned}
\tag{18.11}
$$

第二行使用四维单位球面的面积$2\pi^2$，再以$t=q^2$换元。将分子拆成$t=(t+m^2)-m^2$后，原函数为$\ln(t+m^2)+m^2/(t+m^2)$，代入两端便得

<span id="eq:c18-phi-six-integral-evaluated"></span>

$$
I_\Lambda
=\frac1{16\pi^2}
\left[
 \ln\left(1+\frac{\Lambda^2}{m^2}\right)
 +\frac{m^2}{\Lambda^2+m^2}-1
\right].
\tag{18.12}
$$

把积分与图数、单图权重相乘，八点1PI函数在这一阶含有

<span id="eq:c18-new-eight-point-counterterm"></span>

$$
V_8^{\text{这一圈}}
=\frac{35g_6^2}{2}I_\Lambda
=\frac{35g_6^2}{32\pi^2}
 \ln\frac{\Lambda^2}{m^2}+O(\Lambda^0).
\tag{18.13}
$$

这里出现了非零的八腿局部发散，调节两腿、四腿或六腿项都无法吸收它，因而须加入$-\delta g_8\varphi^8/8!$。新项的树级权重为$-i\delta g_8$，所以$\delta g_8$的发散部分应取上述对数项的正系数，两者相加才会抵消。维数也一致：$[g_6^2]=-4=[g_8]$。

加入八价项以后，将一个六价点与一个八价点用两条线相连，又会留下十条外腿，圈动量积分仍为同一个对数积分。一般地，六价点与$2r$价点产生$2r+2$腿的局部项，普通多项式微扰便依次要求$\varphi^8,\varphi^{10},\ldots$。每个新系数都需要新的归一条件，独立参数的种类因而随阶数增加，这正是此例不可重整化的原因。

这里计数的是独立局部相互作用。某些算符组合可以通过场变量的改变移去，例如将自由场换成 $\varphi+a\varphi^2/\Lambda$，保留 $1/\Lambda$ 的一次项，有

<span id="eq:c18-field-redefinition"></span>

$$
\begin{aligned}
\delta\mathcal L_0
&=-\frac{2a}{\Lambda}\varphi(\partial\varphi)^2
  -\frac{am^2}{\Lambda}\varphi^3\\
&=\frac a\Lambda\varphi^2(\partial^2-m^2)\varphi
 -\partial_\mu\!\left(\frac a\Lambda\varphi^2\partial^\mu\varphi\right).
\end{aligned}
$$

右边把这组项写成最低阶场方程项与全导数。按这种局部换元约化算符基后，再计数剩余的独立系数。不可重整化理论在截断尺度以下仍可使用：将维数为$-r$的系数写成$c_r/\Lambda^r$，它在特征动量$Q$处带来$c_r(Q/\Lambda)^r$。当$Q/\Lambda$足够小、系数大小受控时，便可按给定精度保留有限种项。[第29节](/posts/srednicki-29/#c29)将沿这一思路发展有效场论。

<span id="c18-local-counterterms"></span>

## 非负维耦合与局部反项

再看所有非零独立耦合都满足$[g_n]\ge0$的情形。式[（18.5）](#eq:c18-degree-from-couplings)给出

<span id="eq:c18-nonnegative-coupling-bound"></span>

$$
\omega(G)\le[g_E]=d-\frac{E(d-2)}2.
\tag{18.14}
$$

在$d>2$时，外腿足够多的图便没有整体紫外危险。对于余下的图，还须求出发散部分怎样依赖外动量，才能判断拉格朗日量中的哪些项能吸收它。局部反项在动量空间只能是有限阶多项式，所以下一步要说明，紫外发散也具有这种形式。

先考虑没有子图发散的图，在欧氏域取所有质量为正，把外动量合记为$p$，被积函数记为$f(q,p)$。对外动量求导会改善传播子的高动量衰减：每求一次导数至少改善一幂，例如

<span id="eq:c18-external-derivative-improvement"></span>

$$
\frac{\partial}{\partial p_\mu}
\frac1{(q+p)^2+m^2}
=-\frac{2(q+p)_\mu}{[(q+p)^2+m^2]^2}
=O(|q|^{-3}).
\tag{18.15}
$$

因此，可以用外动量的Taylor展开分离发散部分。若$\omega$为非负整数，沿直线$tp$应用一元Taylor公式，得到

<span id="eq:c18-taylor-remainder"></span>

$$
\begin{aligned}
f(q,p)&=\sum_{r=0}^{\omega}
 \frac1{r!}
 \left.\left(p\cdot\frac{\partial}{\partial p'}\right)^r
 f(q,p')\right|_{p'=0}
 +\mathcal R_{\omega+1}(q,p),\\
\mathcal R_{\omega+1}(q,p)
&=\frac1{\omega!}\int_0^1dt\,(1-t)^\omega
 \left.
 \left(p\cdot\frac{\partial}{\partial p'}\right)^{\omega+1}
 f(q,p')\right|_{p'=tp}.
\end{aligned}
\tag{18.16}
$$

式中$p$只作外部系数，导数先作用于$p'$，再取所列的值。余项含有$\omega+1$次导数，整体UV次数至多为$-1$，所以整体发散只能来自前面有限个Taylor系数，也就是外动量的局部多项式。对单圈积分，这已控制全部紫外端点；多圈图中只让部分动量变大的区域，将在下面的子图减除中处理。

二点标量函数只依赖$p^2$。若其危险次数至多为2，洛伦兹不变性就把局部多项式限制为

<span id="eq:c18-two-point-local-polynomial"></span>

$$
c_0+c_1p^2 .
\tag{18.17}
$$

奇次动量项需要一个固定向量才能缩并成标量，而这里没有这样的向量。上述两项因此正好对应$Bm^2+Ap^2$，其中$[Bm^2]=2$、$[A]=0$。三点或四点图若只有$\omega=0$，则需要常数顶点反项；即使某个允许的相互作用起初设为零，只要没有对称性保护，圈图产生的相应常数项仍须补入拉格朗日量。

在六维纯$\varphi^3$模型中，$[g]=0$，式[（18.5）](#eq:c18-degree-from-couplings)成为$\omega=6-2E$。四维$\varphi^3+\varphi^4$模型则有$\omega=4-E-v_3$，因为$[g_3]=1$、$[g_4]=0$。结合局部多项式的阶数限制，可列出以下候选反项。

| 局部部分   | 四维标量模型                                          | 六维立方模型     |
| ---------- | ----------------------------------------------------- | ---------------- |
| 真空与一点 | 常数、$\varphi$                                       | 常数、$\varphi$  |
| 两点       | $\varphi^2$、$\partial_\mu\varphi\partial^\mu\varphi$ | 同左             |
| 三点       | $\varphi^3$                                           | $\varphi^3$      |
| 四点       | $\varphi^4$                                           | 无整体四点反项   |
| 更多外腿   | 无新的非负维结构                                      | 无新的非负维结构 |

一点函数只有零总动量，含导数的线性项是全导数，因而不再提供独立系数；真空常数则参与真空归一。若保留某种对称性，还须按该对称性筛选表中各项。对于多场模型，允许的指标收缩和动能混合也要一并列入。因此这里所说的有限反项，是有限个独立局部结构，而不是给每一种外腿数仅配一个常数。

<span id="c18-subdivergence"></span>

## 整体收敛，子图仍可发散

现在回到表面计数尚未考察的动量区域。图18a是第17节已经求出的箱图，它有$I=4,L=1$，在六维$\omega=-2$，单圈积分有限。

<span id="c18-box-figure"></span>

![六维一圈四腿箱图，整体表面发散度为负二](/images/srednicki/s18-box.svg)

图18a：四腿箱图。外部短线表示截肢外腿；
四条内线和四个三价点围成一个圈。

若在箱图的一条边上插入两点泡图（bubble），就得到图18b左侧的两圈图。整幅图有六个三价点、七条内线和两个圈，故整体表面发散度为

<span id="eq:c18-overall-two-loop-degree"></span>

$$
\omega(G)=6\times2-2\times7=-2.
\tag{18.18}
$$

然而，上方泡图单独含两条内线和一个圈，其$\omega(\gamma)=6-4=2$。保持外面箱图的圈动量不动，只让泡图的内部动量变大，就会遇到第14节已经求出的两点发散。全部动量共同缩放所得到的负次数，没有控制到这一子区域；需要把泡图与相应的两点反项放在一起处理。

<span id="c18-subtraction-figure"></span>

![箱图内的两点泡子图与相应二价反项插入，二者在同一阶相加](/images/srednicki/s18-subtractions.svg)

图18b：在箱图同一条边上分别插入两点泡图和二价抵消项。
两图必须相加。记流经该边的动量为$p$，
叉号代表$-i(Ap^2+Bm^2)$。图中箭头标明$p$的方向，$a,b$标明泡图与外圈的接入点。

设未修正的传播子为$\widetilde\Delta_0(p)=1/(p^2+m^2-i0)$。泡图的截肢部分是$i\Pi_{\rm loop}(p^2)$，右图叉号给出$-i(Ap^2+Bm^2)$。两者连接的是同一段传播子，因此应在同一个调节下先将两图相加：

<span id="eq:c18-subgraph-and-counterterm"></span>

$$
\begin{aligned}
&\frac{\widetilde\Delta_0}{i}\,
  i\Pi_{\rm loop}\,
  \frac{\widetilde\Delta_0}{i}
+\frac{\widetilde\Delta_0}{i}\,
 [-i(Ap^2+Bm^2)]\,
  \frac{\widetilde\Delta_0}{i}\\
&\hspace{12mm}
=\frac{\widetilde\Delta_0^2}{i}
 [\Pi_{\rm loop}-Ap^2-Bm^2]
=\frac{\widetilde\Delta_0^2}{i}\Pi_R(p^2).
\end{aligned}
\tag{18.19}
$$

两个传播子的$1/i$与插入的$i$相乘后，仍留下$1/i$。这里给$\Pi_R$加下标，只为表明已作第14节的在壳减除。将该节得到的发散部分代入，就能看到泡图与反项如何逐项抵消；当时采用$\varepsilon=6-d$、$\alpha=g^2/(4\pi)^3$，结果为

<span id="eq:c18-explicit-subgraph-pole-cancellation"></span>

$$
\Pi_{\rm loop}\big|_{\rm div}
=-\frac{\alpha}{\varepsilon}
 \left(m^2+\frac{p^2}{6}\right),\quad
A\big|_{\rm div}=-\frac{\alpha}{6\varepsilon},\quad
B\big|_{\rm div}=-\frac{\alpha}{\varepsilon}.
\tag{18.20}
$$

将这三项代入式[（18.19）](#eq:c18-subgraph-and-counterterm)，$p^2$项和$m^2$项分别相消，有限部分则由$\Pi_R(-m^2)=\Pi_R'(-m^2)=0$确定。反项吸收了泡图的局部发散，留下的有限动量依赖继续参与高阶修正。

右图虽然几何上只有一个圈，却与左图处在同一耦合阶数：四个箱图角点给$g^4$，叉号系数从$g^2$开始，合起来也是$g^6$。它的五条内线给出$dL-2I=6-10=-4$，其中$Ap^2$又带来两个分子动量幂，使这一部分的整体次数为$-2$；质量反项没有这样的分子幂，次数仍为$-4$。这也说明在式[（18.7）](#eq:c18-derivative-counting)中，反项顶点的导数必须参与计数。

子图的极点消去后，还须判断外圈是否收敛。第14节已经求得，在欧氏大$p^2$处，减除后的自能满足

$$
\Pi_R(p^2)=O\!\left(g^2p^2[1+\ln(p^2/m^2)]\right).
$$

因此，被修正的传播段$\widetilde\Delta_0^2\Pi_R$与一条自由传播子相比，在高动量端只多出一个对数。再乘其余三条箱图传播子，外圈积分的绝对值在大$q$处便受下式控制：

<span id="eq:c18-renormalized-outer-integral"></span>

$$
\text{常数}\times
\int^\infty dq\,
 \frac{1+\ln(q^2/m^2)}{q^3}
\tag{18.21}
$$

令$t=q^2/m^2$，有$q^{-3}dq=dt/(2m^2t^2)$；又因$\int_T^\infty(1+\ln t)t^{-2}dt=(2+\ln T)/T$，这个紫外尾积分收敛。取$m>0$和有限欧氏外动量也排除了此例的红外端点。因此两图相加后，唯一的危险两点子区域被减除，外圈留下有限的积分。

这个例子表明，$\omega<0$只保证共同缩放区域的收敛，不能独自判断整个多圈图。反过来，$\omega\ge0$也只筛出需要检查的图；领先分子项或由对称性联系的图之间仍可能相消，电动力学中的例子将展示这种由对称性引起的相消。因而本节将表面次数非负的子图称为“危险子图”，其发散系数是否非零，仍由实际积分决定。

<span id="c18-forest"></span>

## 从子图减除到任意阶

多圈图中的子图可以互不相交、彼此嵌套，也可以相互重叠。BPHZ 局部减除定理将这些情况统一起来：对有质量的欧氏标量或狄拉克场，采用通常传播子与局部多项式顶点，按每个表面发散度非负的 1PI 子图作外动量 Taylor 减除，再用森林公式组合各项，得到逐阶紫外收敛的积分。正质量使零动量减除点也没有红外奇性。下面展开其递推结构；定理与森林公式可参阅 [Herzog 的综述第 3.1–3.2 节](https://arxiv.org/pdf/1711.06121#page=5)。

记$T_G$为图$G$对外动量取至$\omega(G)$阶的局部Taylor投影；当$\omega(G)<0$时取$T_G=0$。先减去真子图，得到$\bar R G$，再对图本身作整体减除：

<span id="eq:c18-renormalization-recursion"></span>

$$
C(G)=-T_G\bar R G,\qquad
RG=(1-T_G)\bar R G.
\tag{18.22}
$$

其中$\bar R$按较小子图的减除结果递归构造。对任一组互不相交的危险真子图$\gamma_1,\ldots,\gamma_s$，将各子图替换为已经确定的局部反项$C(\gamma_j)$，并收缩为相应的局部顶点。若以$G/\{\gamma_j\}$表示收缩后的图，就有

<span id="eq:c18-proper-subgraph-recursion"></span>

$$
\bar R G
=G+\sum_{\{\gamma_1,\ldots,\gamma_s\}}
 \left[\prod_{j=1}^s C(\gamma_j)\right]
 G/\{\gamma_1,\ldots,\gamma_s\}.
\tag{18.23}
$$

求和遍历非空的相容子图组。每个子图反项已含其内部更小子图的减除，所以递推从内向外进行。对于上面只有一个泡图子发散的箱图，上式恰好只留下原图和带叉图两项，而整体$T_G=0$，与刚才的处理相同。将各层递推全部代入，就得到森林公式（forest formula）：

<span id="eq:c18-forest-formula"></span>

$$
RG=\sum_{\mathcal F}
 \left[\prod_{\gamma\in\mathcal F}(-T_\gamma)\right]G .
\tag{18.24}
$$

空森林给出原图；非空森林中的子图彼此不相交，或一个包含另一个。嵌套时，乘积先作用于内层，必要时也包括整幅图的减除。相互重叠而不互相包含的两个子图无法同时收缩，因而分别进入不同森林项。正是这种组合，使不同紫外区域获得相容的减除。

递推还说明了反项为何能逐阶确定：真子图的减除只需使用较小图中已经确定的数据，整体剩余发散再由$T_G$抽取为次数不超过$\omega(G)$的局部多项式。在有限个基本场、$d>2$、通常动能及非负维独立耦合的条件下，允许的外腿数与导数阶都有上界。把所有符合所保留对称性的这些局部项纳入拉格朗日量，便得到有限的反项基。局部减除定理保证每阶积分有限，而计幂保证参数种类有限，两者共同说明这类理论的可重整化性。

上述定理用欧氏零点作Taylor减除，前文则用物理在壳条件定义参数；两种减除可以通过有限局部项互相转换。以二点函数为例，令$z=p^2$，并设$F(z)$已减去全部真子图。两种整体减除多项式分别为

<span id="eq:c18-subtraction-scheme-conversion"></span>

$$
\begin{aligned}
P_E(z)&=F(0)+zF'(0),\\
P_{\rm OS}(z)&=F(z_0)+(z-z_0)F'(z_0),
\qquad z_0=-m^2 .
\end{aligned}
\tag{18.25}
$$

若$F$剩余的UV奇异部分为$a+bz$，两个投影都会把它原样取出，故$P_{\rm OS}-P_E$是有限的局部多项式。在质量壳附近具有前文已建立的解析性时，作这一有限改动便可恢复$\Pi(-m^2)=\Pi'(-m^2)=0$。三点函数的整体危险次数为零，其有限常数同理由$V_3(0,0,0)=g$确定。因此，局部减除的收敛结论可以与前面采用的质量、场和耦合定义接在一起。

<span id="c18-spin-preview"></span>

## 带自旋的场

狄拉克场的动能为 $i\overline\Psi\gamma^\mu\partial_\mu\Psi$。伽马矩阵无量纲，动能中的一个导数贡献一个质量幂，因此

<span id="eq:c18-fermion-dimension"></span>

$$
2[\Psi]+1=d,\qquad [\Psi]=\frac{d-1}{2}.
\tag{18.26}
$$

含 $r$ 个标量场和 $n$ 个费米双线性的无导数项，系数的维数为

<span id="eq:c18-yukawa-dimension"></span>

$$
\begin{aligned}
\mathcal L_{\rm int}&\supset g_{r,n}\varphi^r(\overline\Psi\Psi)^n,\\
[g_{r,n}]&=d-\frac r2(d-2)-n(d-1),\\
[g_{0,n}]&=d-n(d-1).
\end{aligned}
\tag{18.27}
$$

四维中，混合项满足 $[g_{r,n}]=4-r-3n$。对 $r,n\ge1$，非负维数只允许 $r=n=1$，即无量纲的汤川耦合 $g\varphi\overline\Psi\Psi$。纯费米相互作用至少含两个双线性，$n=2$ 时系数维数已经是 $-2$；四费米项由此属于低能有效相互作用。若有多个场及自旋、内部对称性指标，还应分别列出允许的独立缩并。

对规范场，传播子的高动量衰减与规范对称性共同限制反项。[第73–74节](/posts/srednicki-73/#c73)将建立规范场的量子理论，[第85–86节](/posts/srednicki-85/#c85)再讨论自发对称性破缺后的质量与相互作用。

两点子图的计算与一般局部减除结构合起来，说明了怎样把低阶已知的反项用于高阶图。下一节将把所有两点和三点修正直接装进图的组成部分，进一步组织高阶展开。

---

[← 第 17 节](/posts/srednicki-17/) · [章节地图](/srednicki/) · [第 19 节 →](/posts/srednicki-19/)
