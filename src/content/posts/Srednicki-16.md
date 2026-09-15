---
title: 'Srednicki §16 顶点的圈修正'
date: 2026-09-14
category: 笔记
tags: [物理, 量子场论, Srednicki]
series: 'Srednicki QFT'
srednickiSections: [16]
hideFromHome: true
draft: false
---

<span id="c16"></span>

传播子的圈修正描述粒子在两次相互作用之间的传播；要把圈修正纳入散射计算，还须求出顶点本身怎样改变。现在考察三价顶点，将三个场相接的单粒子不可约部分求和，再把它与完整传播子组合起来。仍考虑六维附近、质量 $m>0$ 的实标量立方理论。

<span id="c16-triangle"></span>

## 三角图与精确顶点

把三个外传播子截去，将所有三腿单粒子不可约图相加，定义精确顶点 $iV_3(k_1,k_2,k_3)$。三个外动量都取流入，因此动量守恒给出

<span id="eq:c16-incoming-momenta"></span>

$$
k_1+k_2+k_3=0,\qquad
k_3^2=k_1^2+k_2^2+2k_1\cdot k_2 .
\tag{16.1}
$$

若一条腿代表出射粒子，传入顶点函数的便是该粒子动量的负值。这一约定使各条腿可以统一处理。在 $d=6-\varepsilon$ 时，先把有质量维数的耦合写成 $g_d=g\widetilde\mu^{\varepsilon/2}$；三价顶点的树级值为 $iZ_g g_d$。接下来的一阶修正来自三角图，圈动量按图16a所示的方向选取。

<span id="c16-figure"></span>

![三条外腿均取流入的三角图，内线标明圈动量路由](/images/srednicki/s16-triangle.svg)

图16a：三价顶点的一圈三角图。
外线只标记截肢后的动量，箭头表示动量流向。
右、下、左三条内线依次带 $\ell$、$\ell+k_2$、$\ell-k_1$。
流入右顶点的 $\ell$ 与 $k_2$ 合成下边的动量；
左顶点则用 $k_2+k_3=-k_1$，将流入的
$\ell+k_2+k_3$ 接到流出的 $\ell-k_1$。

写圈积分之前，先按第9节的方法确定收缩的组合系数。三阶展开的分母为 $3!(3!)^3$；将三个固定外标签分配给三个积分顶点有 $3!$ 种安排，在每个顶点选取与外场相接的场槽又有 $3^3$ 种。每个顶点余下的两个场槽须分别接向另外两个顶点，共有 $2^3$ 种选法；这些选择一经确定，全部内线的配对也就确定。因此净系数为

<span id="eq:c16-symmetry-factor"></span>

$$
\frac{3!\,3^3\,2^3}{3!(3!)^3}=1.
\tag{16.2}
$$

三角图的对称因子因而为1。由于外标签已经固定，旋转或翻转图形并不产生需要再除去的等价收缩。再给每条内线配上传播子 $\widetilde\Delta/i$，其中 $\widetilde\Delta(p^2)=(p^2+m^2-i0)^{-1}$，便得到顶点的树项与一圈项：

<span id="eq:c16-loop-amplitude"></span>

$$
\begin{aligned}
iV_{3,d}(k_1,k_2,k_3)
={}&iZ_g g_d
 +(ig_d)^3\left(\frac1i\right)^3
 \int\frac{d^d\ell}{(2\pi)^d}
 \frac1{[(\ell-k_1)^2+m^2-i0]}\\
&\hspace{20mm}\times
 \frac1{[(\ell+k_2)^2+m^2-i0](\ell^2+m^2-i0)}
 +O(g_d^5).
\end{aligned}
\tag{16.3}
$$

圈图中的三个 $Z_g$ 只需取1，因为每增加一个 $Z_g-1=O(g_d^2)$，就会把该项提高到下一圈的阶数；内线上的自能插入也从更高阶开始贡献。三个顶点与三条内线的相位相乘为 $(i)^3(1/i)^3=1$，所以圈积分前留下正的 $g_d^3$。这样，计算的关键就归结为三个传播分母的积分。

<span id="c16-parameters"></span>

## 合并三个分母

利用[第14节证明的参数公式](/posts/srednicki-14/#eq:c14-general-feynman-proof)，可将三个分母合并，再通过平移圈动量完成平方。三个一次分母合并时的系数为 $\Gamma(3)=2!$，将它计入参数测度，定义

<span id="eq:c16-parameter-measure"></span>

$$
\begin{aligned}
\int dF_3\,F
&=2\int_0^1dx_1\int_0^{1-x_1}dx_2\,
 F(x_1,x_2,1-x_1-x_2),\\
\int dF_3&=2\int_0^1(1-x_1)\,dx_1=1.
\end{aligned}
\tag{16.4}
$$

这里消去 $x_3$ 时，约束delta的换元因子为1；剩下的三角形参数区面积是 $1/2$，所以带上前面的系数后，测度的总积分恰为1。这个归一化稍后将直接决定紫外极点和高动量对数的系数。令三个原分母分别为 $A_1,A_2,A_3$，先逐项展开它们的加权和：

<span id="eq:c16-combine-denominators"></span>

$$
\begin{aligned}
\frac1{A_1A_2A_3}
&=\int dF_3\,[x_1A_1+x_2A_2+x_3A_3]^{-3},\\
x_1A_1+x_2A_2+x_3A_3
&=\ell^2-2\ell\cdot(x_1k_1-x_2k_2)
  +x_1k_1^2+x_2k_2^2+m^2-i0 .
\end{aligned}
\tag{16.5}
$$

参数约束 $x_1+x_2+x_3=1$ 使 $\ell^2$ 的系数成为1，也使三个分母的负虚部合成同一个Feynman处方。为消去圈动量的一次项，作平移

<span id="eq:c16-loop-shift"></span>

$$
q=\ell-x_1k_1+x_2k_2,\qquad
x_1A_1+x_2A_2+x_3A_3=q^2+D,
\tag{16.6}
$$

移入平方项的部分须从常数项中扣除，因此剩余的参数质量为

<span id="eq:c16-mass-first-form"></span>

$$
D=m^2+x_1(1-x_1)k_1^2+x_2(1-x_2)k_2^2
       +2x_1x_2k_1\cdot k_2-i0.
\tag{16.7}
$$

合并分母与配方由此完成，平移的Jacobian为1。这些运算先在圈积分收敛、参数质量为正的区域进行，再沿共同的Feynman边界作解析延拓。所得常数项还可以利用动量守恒写得更对称：用式[（16.1）](#eq:c16-incoming-momenta)消去内积后，两个平方项的系数分别化为 $x_1(1-x_1)-x_1x_2=x_1x_3$ 和 $x_2(1-x_2)-x_1x_2=x_2x_3$，于是得到对称形式

<span id="eq:c16-symmetric-mass"></span>

$$
D=m^2+x_1x_3k_1^2+x_2x_3k_2^2+x_1x_2k_3^2-i0.
\tag{16.8}
$$

这时全部外动量依赖都落在三个不变量中。若同时交换外标签与相应的参数，参数区域和测度保持不变，因而积分所得的顶点函数对三条外腿对称，符合三个相同标量场的要求。

<span id="c16-dimreg"></span>

## 圈积分和维数极点

完成平方后，圈积分只含一个二次式分母的幂，可以沿用第14节的Wick旋转。当 $D>0$ 时，取 $q^0=i\bar q_d$，于是 $d^dq=i\,d^d\bar q$，而 $q^2+D$ 变成 $\bar q^2+D$。旋转产生的 $i$ 与式[（16.3）](#eq:c16-loop-amplitude)左侧的公共因子相消，留下带正号的欧氏积分：

<span id="eq:c16-euclidean-vertex"></span>

$$
\frac{V_{3,d}}{g_d}
=Z_g+g_d^2\int dF_3
 \int\frac{d^d\bar q}{(2\pi)^d}
 \frac1{(\bar q^2+D)^3}+O(g_d^4).
\tag{16.9}
$$

在计算前，先看积分在哪些维数收敛。大径向动量处，测度与分母合成 $\bar q^{d-1}\bar q^{-6}d\bar q=\bar q^{d-7}d\bar q$，因此紫外收敛要求 $d<6$；而 $D>0$ 排除了原点处由分母产生的红外发散。在[第14节的径向积分公式](/posts/srednicki-14/#eq:c14-master-recalled)中代入 $a=0,b=3$，角面积与径向积分相乘，得到

<span id="eq:c16-radial-integral"></span>

$$
\begin{aligned}
\int\frac{d^d\bar q}{(2\pi)^d}
 \frac1{(\bar q^2+D)^3}
&=\frac{\Gamma(3-d/2)\Gamma(d/2)}
 {(4\pi)^{d/2}\Gamma(3)\Gamma(d/2)}
 D^{\,d/2-3}\\
&=\frac{\Gamma(3-d/2)}
 {2(4\pi)^{d/2}}D^{\,d/2-3}.
\end{aligned}
\tag{16.10}
$$

分母中的2来自三次分母所对应的Gamma函数 $\Gamma(3)=2$。原动量积分在 $0<d<6$ 的正质量区域收敛，右边的Gamma函数表达式则给出了继续到其他维数所需的亚纯延拓。现在令 $d=6-\varepsilon$，把耦合与圈积分的尺度因子合并；由于 $g_d^2(4\pi)^{-d/2}
=\alpha(4\pi\widetilde\mu^2)^{\varepsilon/2}$，得到无量纲的比值

<span id="eq:c16-dimensionally-regulated"></span>

$$
\frac{V_{3,d}}{g_d}
=Z_g+\frac\alpha2\Gamma(\varepsilon/2)
 \int dF_3
 \left(\frac{4\pi\widetilde\mu^2}{D}\right)^{\varepsilon/2}
 +O(\alpha^2),\qquad
\alpha=\frac{g^2}{(4\pi)^3}.
\tag{16.11}
$$

为使顶点按六维量纲记述，定义 $V_3=\widetilde\mu^{-\varepsilon/2}V_{3,d}$，因而 $V_3/g=V_{3,d}/g_d$。下文使用这个无量纲比值，并在反项减除以后取有限的六维极限。为找出需要减去的部分，使用[Gamma 函数递推式](/posts/srednicki-14/#eq:c14-gamma-pole-proof)在零附近的展开，同时展开含尺度的幂：

<span id="eq:c16-pole-expansion"></span>

$$
\begin{aligned}
\Gamma(\varepsilon/2)
 &=\frac2\varepsilon-\gamma+O(\varepsilon),\\
\left(\frac{4\pi\widetilde\mu^2}{D}\right)^{\varepsilon/2}
 &=1+\frac{\varepsilon}{2}
     \ln\frac{4\pi\widetilde\mu^2}{D}
     +O(\varepsilon^2),\\
\Gamma(\varepsilon/2)
 \left(\frac{4\pi\widetilde\mu^2}{D}\right)^{\varepsilon/2}
 &=\frac2\varepsilon+
     \ln\frac{4\pi\widetilde\mu^2}{D}-\gamma
     +O(\varepsilon).
\end{aligned}
\tag{16.12}
$$

极点乘上幂展开的一阶项，恰好留下有限的对数。再利用 $\int dF_3=1$，并将常数并入尺度定义 $\mu^2=4\pi e^{-\gamma}\widetilde\mu^2$，便得到

<span id="eq:c16-unsubtracted-log"></span>

$$
\frac{V_3}{g}
=Z_g+\frac\alpha2
 \left[\frac2\varepsilon+\int dF_3\ln\frac{\mu^2}{D}\right]
 +O(\alpha^2).
\tag{16.13}
$$

式中已略去随调节量消失的 $O(\varepsilon)$ 项，剩下的极点须由顶点反项抵消。有限动量对数沿用同一 $D-i0$ 的分支，这一处方在继续到类时外动量时仍须保留。

<span id="c16-coupling"></span>

## 怎样定义耦合常数

将顶点反项记为 $C$，即 $Z_g=1+C$。为了区分局部反项与动量依赖，把 $\ln(\mu^2/D)$ 拆成 $2\ln(\mu/m)-\ln(D/m^2)$，将式[（16.13）](#eq:c16-unsubtracted-log)写为

<span id="eq:c16-counterterm-isolation"></span>

$$
\frac{V_3}{g}
=1+\left\{\alpha\left[\frac1\varepsilon+\ln\frac\mu m\right]+C\right\}
-\frac\alpha2\int dF_3\ln\frac D{m^2}
+O(\alpha^2).
\tag{16.14}
$$

发散部分与所有外动量无关，因此原拉氏量中的局部三价反项就足以抵消它。反项的有限部分尚有选择余地，将这部分记为一个常数，取

<span id="eq:c16-c-counterterm"></span>

$$
C=-\alpha\left[\frac1\varepsilon+\ln\frac\mu m+\kappa_C\right]
  +O(\alpha^2)
\tag{16.15}
$$

代回顶点后，极点和辅助尺度的对数同时消去，留下有限结果

<span id="eq:c16-finite-vertex"></span>

$$
\frac{V_3(k_1,k_2,k_3)}g
=1-\frac\alpha2\int dF_3\ln\frac D{m^2}
  -\alpha\kappa_C+O(\alpha^2).
\tag{16.16}
$$

有限常数 $\kappa_C$ 规定耦合 $g$ 的定义。选定一个顶点归一化条件，再用包含圈修正的截面拟合 $g$，便确定了参数。不同归一化条件之间的有限换算，可以直接从顶点比较得到。

例如，用 $\kappa_C$ 与 $\kappa_C'$ 两种条件描述同一个顶点，并在当前阶数令 $g'=g+\delta g$。将两种参数写法代入式[（16.16）](#eq:c16-finite-vertex)并比较，得到

<span id="eq:c16-finite-coupling-conversion"></span>

$$
\begin{aligned}
g\left(1-\frac\alpha2 J-\alpha\kappa_C\right)
&=(g+\delta g)
 \left(1-\frac\alpha2 J-\alpha\kappa_C'\right)+O(g\alpha^2),\\
\delta g&=g\alpha(\kappa_C'-\kappa_C)+O(g\alpha^2),
\qquad
J=\int dF_3\ln\frac D{m^2}.
\end{aligned}
\tag{16.17}
$$

式中把 $\alpha'$ 换成 $\alpha$ 所产生的差已属于下一阶，因此一次有限的耦合换算便能补偿减除常数的改变。本节选择零动量处的顶点来定义耦合：所有外动量为零时，$D=m^2$，参数对数逐点为零，故

<span id="eq:c16-zero-momentum-value"></span>

$$
\frac{V_3(0,0,0)}g=1-\alpha\kappa_C+O(\alpha^2).
\tag{16.18}
$$

取 $\kappa_C=0$ 后，便得到归一化条件

<span id="eq:c16-zero-momentum-condition"></span>

$$
V_3(0,0,0)=g.
\tag{16.19}
$$

这是在离壳零动量点定义的耦合。这个条件也能逐阶延用：在更高阶将低阶已知项代入 $V_3(0,0,0)$，再调节 $C$ 的新一阶常数，就能继续维持零动量处的归一化。

<span id="c16-soft-leg"></span>

## 一个可以算完的动量例

耦合确定以后，在当前阶数，顶点随外动量的变化由有限的参数积分给出。一般的三个不变量仍会留下二维积分；在式[（16.4）](#eq:c16-parameter-measure)中取 $x_1=t,\ x_2=(1-t)v,\ x_3=(1-t)(1-v)$，Jacobian为 $1-t$，便可将三角形参数区改写成固定正方形：

<span id="eq:c16-square-parameter-integral"></span>

$$
\begin{aligned}
J&=2\int_0^1dt\int_0^1dv\,(1-t)\ln\frac{D(t,v)}{m^2},\\
D(t,v)&=m^2+t(1-t)(1-v)k_1^2+(1-t)^2v(1-v)k_2^2\\
&\quad+t(1-t)vk_3^2-i0.
\end{aligned}
\tag{16.20}
$$

先在对数宗量为正的区域计算，再将其他动量取值沿规定的下岸延拓，这个表示便保留了顶点的完整参数依赖。为看清有限修正如何随动量改变，下面选一个可以直接积分的运动学例子。

取欧氏动量 $k_1=p,\ k_2=-p,\ k_3=0$，记 $p^2=Q^2>0$、$u=Q^2/m^2$。一条外腿的动量为零后，参数质量只依赖一个参数：

<span id="eq:c16-one-soft-leg-parameter"></span>

$$
D=m^2+Q^2x_3(1-x_3),\qquad
J(u)=2\int_0^1dx\,(1-x)\ln[1+ux(1-x)].
\tag{16.21}
$$

固定 $x_3=x$，对另一个参数积分就得到权重 $2(1-x)$。对数在 $x\mapsto1-x$ 下不变，所以将换元前后的式子相加再除以2，便可消去显式权重，把积分化为

<span id="eq:c16-symmetric-log-integral"></span>

$$
J(u)=\int_0^1dx\,\ln[1+ux(1-x)].
\tag{16.22}
$$

为评价这个对数积分，令 $t=2x-1$ 并利用被积函数的偶性，将积分归并到正半区间。再记 $a=1+u/4$、$b=u/4$、$r^2=a/b=1+4/u$，积分便成为

<span id="eq:c16-even-log-integral"></span>

$$
J(u)=\int_0^1dt\,\ln(a-bt^2).
\tag{16.23}
$$

对数求导后会变成有理函数，因而适合先作分部积分。边界项 $[t\ln(a-bt^2)]_0^1=0$，其中上端点因 $a-b=1$ 而为零，于是

<span id="eq:c16-soft-leg-closed"></span>

$$
\begin{aligned}
J(u)
&=2b\int_0^1dt\,\frac{t^2}{a-bt^2}\\
&=2\int_0^1dt\left[-1+\frac{r^2}{r^2-t^2}\right]\\
&=-2+2r\,\operatorname{arctanh}\frac1r.
\end{aligned}
\tag{16.24}
$$

最后一个有理函数用原函数 $\int dt/(r^2-t^2)=r^{-1}\operatorname{arctanh}(t/r)$ 积分。在 $u>0$ 的运动学下，$r>1$，所以这些函数都取实值。将结果代回减除后的顶点，得到完整的一圈修正：

<span id="eq:c16-soft-leg-vertex"></span>

$$
\frac{V_3(p,-p,0)}g
=1+\alpha\left[1-r\,\operatorname{arctanh}\frac1r\right]
+O(\alpha^2).
\tag{16.25}
$$

这个闭式同时包含小动量和大动量的行为。先看小 $u$ 区间，直接展开式[（16.22）](#eq:c16-symmetric-log-integral)最为方便。由于 $0\le x(1-x)\le1/4$，在 $|u|<4$ 时对数级数一致收敛，可以逐项积分。前两项所需的积分为 $\int_0^1x(1-x)dx=1/6$ 和 $\int_0^1x^2(1-x)^2dx=1/30$，因而

<span id="eq:c16-soft-leg-low-momentum"></span>

$$
\begin{aligned}
J(u)&=\frac u6-\frac{u^2}{60}+O(u^3),\\
\frac{V_3(p,-p,0)}g
&=1-\frac{\alpha u}{12}+\frac{\alpha u^2}{120}
 +O(\alpha u^3,\alpha^2).
\end{aligned}
\tag{16.26}
$$

当 $Q\to0$ 时，顶点回到定义所要求的 $g$；在有限但小的 $Q$ 处，圈图带来平滑的动量修正，其变化尺度由质量 $m$ 控制。

<span id="c16-high-energy"></span>

## 大动量为何产生对数

同一个例子也能说明高动量行为。先利用 $r^2-1=4/u$ 将反双曲正切改写为对数：

<span id="eq:c16-soft-leg-large-log"></span>

$$
2\operatorname{arctanh}\frac1r
=\ln\frac{r+1}{r-1}
=\ln u+2\ln\frac{r+1}{2}.
\tag{16.27}
$$

当 $u\to+\infty$ 时，$r=1+O(u^{-1})$，因此大动量渐近式为

<span id="eq:c16-soft-leg-high-momentum"></span>

$$
\begin{aligned}
J(u)&=\ln u-2+O\!\left(\frac{\ln u}{u}\right),\\
\frac{V_3(p,-p,0)}g
&=1-\frac\alpha2
 \left[\ln\frac{Q^2}{m^2}-2
 +O\!\left(\frac{m^2}{Q^2}\ln\frac{Q^2}{m^2}\right)\right]
 +O(\alpha^2).
\end{aligned}
\tag{16.28}
$$

除了随动量增长的对数，闭式还给出了这个运动学下的有限常数。一般情形中，对数的系数可以直接从参数表示读出，但还须说明参数积分为何只留下有限的余项。先取欧氏的非负不变量 $k_i^2=Q^2r_i$，保持 $r_i$ 固定且至少一个非零，定义

<span id="eq:c16-hard-ratios"></span>

$$
\begin{aligned}
f(x)&=x_1x_3r_1+x_2x_3r_2+x_1x_2r_3,\\
J&=\ln\frac{Q^2}{m^2}
 +\int dF_3\ln\left[f(x)+\frac{m^2}{Q^2}\right].
\end{aligned}
\tag{16.29}
$$

第一项的系数为1，来自归一化参数测度的总权重。第二项在参数区内部容易取极限，需要考察的是边界上对数宗量趋于零的位置。若 $r_1>0$，则 $f\ge r_1x_1x_3$；其他非零 $r_i$ 也给出同样形式的估计。因此只须控制参数边界的对数，而这些对数的积分为

<span id="eq:c16-endpoint-log-control"></span>

$$
\begin{aligned}
\int dF_3\,|\ln x_1|
&=-2\int_0^1dx_1\,(1-x_1)\ln x_1\\
&=-2\left(-1+\frac14\right)=\frac32 .
\end{aligned}
\tag{16.30}
$$

其中两个初等积分可由分部积分得到：$\int_0^1\ln x\,dx=-1$、$\int_0^1x\ln x\,dx=-1/4$，两项边界都因 $x^a\ln x\to0$ 而消失。由此可知 $|\ln x_1|+|\ln x_3|$ 可积；另一方面，$f$ 在紧参数区有上界，因而式[（16.29）](#eq:c16-hard-ratios)中的对数上下界都受到可积函数的控制。取 $Q\to\infty$ 后，第二项趋于有限常数，最终得到

<span id="eq:c16-general-high-log"></span>

$$
\begin{aligned}
J&=\ln\frac{Q^2}{m^2}
   +\int dF_3\ln f(x)+o(1),\\
\frac{V_3}{g}
&=1-\frac\alpha2
 \left[\ln\frac{Q^2}{m^2}+O(1)\right]+O(\alpha^2).
\end{aligned}
\tag{16.31}
$$

大对数正是这样从完整参数积分中产生的。其他允许的硬运动学可由同一解析函数继续得到；经过阈值时须保留对数的虚部，接近额外的软或共线边界时则须重新检查尺度比。在这些条件下，顶点的相对圈修正与第14节的自能相对修正一样，都会随能量按对数增长。一圈结果作为树级的小修正使用时，需要 $\alpha|\ln(Q^2/m^2)|\ll1$；超出这一范围后，可用[第28节的重整化群方法](/posts/srednicki-28/#c28)重新组织这些大对数。

---

[← 第 15 节](/posts/srednicki-15/) · [章节地图](/srednicki/) · [第 17 节 →](/posts/srednicki-17/)
