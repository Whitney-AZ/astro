---
title: 'Srednicki §48 自旋平均截面'
date: 2026-09-14
category: 笔记
tags: [物理, 量子场论, Srednicki]
series: 'Srednicki QFT'
srednickiSections: [48]
hideFromHome: true
draft: false
---

<span id="c48"></span>

第46节把自旋求和写成了矩阵迹，第47节又给出了求迹的规则。现在将这两步接起来，先计算电子与正电子的弹性散射，再计算电子与标量的弹性散射，最后把结果换成可以观察的角分布。相互作用仍取$g\varphi\bar\Psi\Psi$，因而这里的电子正电子过程由标量交换产生。以下保留树级振幅所给的$g^4$阶模平方，并对独立、未极化的入射束取平均。

<span id="c48-pair-start"></span>

## 电子正电子散射的四个迹

将电子的入射、出射动量记为$p_1,p_1'$，正电子的记为$p_2,p_2'$。四条外腿满足$p_i^2=p_i'^2=-m^2$，动量守恒为$p_1+p_2=p_1'+p_2'$。曼德尔斯塔姆变量定义为
<span id="eq:c48-pair-mandelstam"></span>

$$
\begin{aligned}
s&=-(p_1+p_2)^2=-(p_1'+p_2')^2,\\
t&=-(p_1-p_1')^2=-(p_2-p_2')^2,\\
u&=-(p_1-p_2')^2=-(p_2-p_1')^2,\qquad s+t+u=4m^2 .
\end{aligned}
\tag{48.1}
$$

展开这些平方，例如有$s=2m^2-2(p_1p_2)$和$t=2m^2+2(p_1p_1')$。三式相加以后，右边成为$6m^2+2p_1\cdot(p_1'+p_2'-p_2)=6m^2+2p_1^2=4m^2$，于是得到三个变量的和式。反过来解出内积，就得到六个关系：
<span id="eq:c48-pair-dot-products"></span>

$$
\begin{aligned}
(p_1p_2)=(p_1'p_2')&=m^2-\frac{s}{2},\\
(p_1p_1')=(p_2p_2')&=\frac{t}{2}-m^2,\\
(p_1p_2')=(p_1'p_2)&=\frac{u}{2}-m^2 .
\end{aligned}
\tag{48.2}
$$

先列出这组运动学关系，求迹以后便可随时将外动量的内积换成不变量。接下来把固定自旋外积简记为$R_i=u_i\bar u_i$、$V_i=v_i\bar v_i$，出射量加撇号。用四个系数分别收集两个图的平方及其干涉：
<span id="eq:c48-fixed-phi"></span>

$$
\begin{aligned}
\Phi_{ss}&=\operatorname{tr}(R_1V_2)\operatorname{tr}(V_2'R_1'),\\
\Phi_{tt}&=\operatorname{tr}(R_1R_1')\operatorname{tr}(V_2'V_2),\\
\Phi_{st}&=\operatorname{tr}(R_1R_1'V_2'V_2),\\
\Phi_{ts}&=\operatorname{tr}(R_1V_2V_2'R_1').
\end{aligned}
\tag{48.3}
$$

前两项对应各图的平方，后两项保留两种干涉的矩阵次序。这些次序已在[第46节](/posts/srednicki-46/#c46-two-lines)通过外旋量的指标收缩得到；现在补上各道分母，便有
<span id="eq:c48-pair-fixed-square"></span>

$$
\begin{aligned}
|\mathcal T|^2=g^4\bigg[
&\frac{\Phi_{ss}}{(M^2-s)^2}
-\frac{\Phi_{st}+\Phi_{ts}}{(M^2-s)(M^2-t)}\\
&+\frac{\Phi_{tt}}{(M^2-t)^2}
\bigg].
\end{aligned}
\tag{48.4}
$$

其中$M$是内部标量的质量。干涉前的相对负号继承自两个树图的费米置换号，第45节固定福克次序所带的公共负号则已在模平方中消去。以下采用实耦合，并在离开内线极点的树级边界值上计算。

每束入射粒子都有两个等权自旋态，两束独立制备，因而四种初态组合取等权平均；两个末粒子的自旋只作求和。将这一运算记为
<span id="eq:c48-pair-spin-average"></span>

$$
\langle X\rangle
=\frac14\sum_{\sigma_1,\sigma_2,\sigma_1',\sigma_2'}X .
\tag{48.5}
$$

按照第46节的办法，可以先对各条外腿使用完整性关系。记
<span id="eq:c48-completeness"></span>

$$
U_i:=\sum_{\sigma_i}R_i=-\slashed p_i+m,\qquad
W_i:=\sum_{\sigma_i}V_i=-\slashed p_i-m ,
\tag{48.6}
$$

出射外腿也有同样的关系。在式[（48.3）](#eq:c48-fixed-phi)的每一项中，四个自旋标签各出现一次，因此求和可以分别作用于四个外积，而保留它们原有的乘法次序。于是
<span id="eq:c48-pair-average-traces"></span>

$$
\begin{aligned}
\langle\Phi_{ss}\rangle
&=\frac14\operatorname{tr}(U_1W_2)\operatorname{tr}(W_2'U_1'),\\
\langle\Phi_{tt}\rangle
&=\frac14\operatorname{tr}(U_1U_1')\operatorname{tr}(W_2'W_2),\\
\langle\Phi_{st}\rangle&=\frac14\operatorname{tr}(U_1U_1'W_2'W_2),\\
\langle\Phi_{ts}\rangle&=\frac14\operatorname{tr}(U_1W_2W_2'U_1').
\end{aligned}
\tag{48.7}
$$

自旋标签与外旋量至此都被消去，余下的是四条由动量和质量构成的矩阵链。

<span id="c48-pair-squares"></span>

## 两个平方项

先看二因子迹。将两个因子相乘后，含一个gamma的项迹为零，只留下二阶项与质量常数项：
<span id="eq:c48-annihilation-trace"></span>

$$
\begin{aligned}
\operatorname{tr}(U_1W_2)
&=\operatorname{tr}\!\left[
\slashed p_1\slashed p_2+m\slashed p_1-m\slashed p_2-m^2I\right]\\
&=-4(p_1p_2)-4m^2
=2s-8m^2 .
\end{aligned}
\tag{48.8}
$$

最后一步使用了式[（48.2）](#eq:c48-pair-dot-products)的内积关系。另一条湮灭链中的内积$p_1'p_2'$与此相同，所以两个迹具有相同的值。直接图的两个外积则带同号质量项，展开时常数项的符号随之改变，得到
<span id="eq:c48-other-pair-traces"></span>

$$
\begin{aligned}
\operatorname{tr}(W_2'U_1')&=2(s-4m^2),\\
\operatorname{tr}(U_1U_1')
&=-4(p_1p_1')+4m^2=2(4m^2-t),\\
\operatorname{tr}(W_2'W_2)
&=-4(p_2'p_2)+4m^2=2(4m^2-t).
\end{aligned}
\tag{48.9}
$$

每个迹都带一个因子二，两个相乘给$2^2$，恰好抵消初态平均的$1/4$。因此
<span id="eq:c48-pair-squares"></span>

$$
\langle\Phi_{ss}\rangle=(s-4m^2)^2,\qquad
\langle\Phi_{tt}\rangle=(t-4m^2)^2 .
\tag{48.10}
$$

这两个结果由$s\leftrightarrow t$联系起来，也可以直接从迹的结构看出。作形式替换$p_2\leftrightarrow-p_1'$时，$W_2$变为$-U_1'$，而$U_1'$变为$-W_2$，两个负号分别进入两个迹，再在乘积中消去。动量守恒同时使$s$与$t$互换，$u$保持不变。因此这是有理表达式之间的交叉替换；其中出现的负能动量标签，要在相应的新过程中重新解释。

<span id="c48-pair-interference"></span>

## 干涉迹的六个质量项

接着计算$\langle\Phi_{st}\rangle$。展开四个因子时，只有选择零个、两个或四个斜线矩阵的项可能有非零迹。选四个斜线矩阵时总系数为正；选两个时，符号还取决于另外两个质量项。两个$U$中的质量为$+m$，两个$W$中的质量为$-m$，所以要逐对选出留下的斜线因子。逐项展开，得到
<span id="eq:c48-interference-expansion"></span>

$$
\begin{aligned}
\langle\Phi_{st}\rangle
={}&\frac14\operatorname{tr}
(\slashed p_1\slashed p_1'\slashed p_2'\slashed p_2)\\
&+\frac{m^2}{4}\operatorname{tr}\!\big[
\slashed p_1\slashed p_1'-\slashed p_1\slashed p_2'
-\slashed p_1\slashed p_2\\
&\hspace{31mm}
-\slashed p_1'\slashed p_2'
-\slashed p_1'\slashed p_2
+\slashed p_2'\slashed p_2\big]
+\frac{m^4}{4}\operatorname{tr}I .
\end{aligned}
\tag{48.11}
$$

例如留下$p_1,p_1'$时，其余两个质量项的乘积为$(-m)(-m)$，所以第一对取正号；留下$p_1,p_2'$时，其余乘积为$(+m)(-m)$，便取负号。其余四对也按同样的选择确定符号，留下的矩阵始终保持原次序。

随后代入第47节的二阶迹和四阶迹，便能将每个$\operatorname{tr}$化为内积：
<span id="eq:c48-interference-dots"></span>

$$
\begin{aligned}
\langle\Phi_{st}\rangle
={}&(p_1p_1')(p_2'p_2)
 -(p_1p_2')(p_1'p_2)+(p_1p_2)(p_1'p_2')\\
&-m^2\big[
(p_1p_1')-(p_1p_2')-(p_1p_2)\\
&\hspace{24mm}-(p_1'p_2')-(p_1'p_2)+(p_2'p_2)
\big]+m^4 .
\end{aligned}
\tag{48.12}
$$

现在只剩内积的整理。暂记$r=m^2$，第一行的三个配对分别由$t,u,s$给出，方括号内六个内积则两两相同。代入前面的运动学关系，有
<span id="eq:c48-interference-polynomial"></span>

$$
\begin{aligned}
\langle\Phi_{st}\rangle
={}&\left(\frac t2-r\right)^2
-\left(\frac u2-r\right)^2
+\left(r-\frac s2\right)^2\\
&-r(s+t-u-2r)+r^2 .
\end{aligned}
\tag{48.13}
$$

先用$s+t=4r-u$合并前三个平方：
<span id="eq:c48-three-square-reduction"></span>

$$
\begin{aligned}
&\frac{s^2+t^2-u^2}{4}+r(u-s-t)+r^2\\
&=\frac{(4r-u)^2-2st-u^2}{4}
  +r(2u-4r)+r^2
=r^2-\frac{st}{2}.
\end{aligned}
\tag{48.14}
$$

余下两项合为$-r(2r-2u)+r^2=2ru-r^2$，再与刚才的结果相加，得到
<span id="eq:c48-pair-interference"></span>

$$
\langle\Phi_{st}\rangle=-\frac{st}{2}+2m^2u,\qquad
\langle\Phi_{ts}\rangle=\langle\Phi_{st}\rangle .
\tag{48.15}
$$

第二种干涉也可由$p_2\leftrightarrow-p_1'$的交叉替换求出：四因子迹变为另一种次序，所产生的两个负号抵消，而最终多项式在$s\leftrightarrow t$下不变。因此两个平均干涉系数相等。第46节已由狄拉克共轭说明，固定自旋的两种干涉迹互为复共轭；这里经过自旋求和，内积表达式又全为实数，便进一步得到相同的数值。

将两个平方项与两个干涉项代回模平方，得到
<span id="eq:c48-pair-result"></span>

$$
\begin{aligned}
\langle|\mathcal T|^2\rangle_{e^-e^+}
=g^4\bigg[
&\frac{(s-4m^2)^2}{(M^2-s)^2}
+\frac{st-4m^2u}{(M^2-s)(M^2-t)}\\
&+\frac{(t-4m^2)^2}{(M^2-t)^2}
\bigg].
\end{aligned}
\tag{48.16}
$$

中间一项的分子来自式[（48.4）](#eq:c48-pair-fixed-square)中的负号乘$2\langle\Phi_{st}\rangle$。各分子与分母的质量维数均为4，模平方因而无量纲。固定$M>0$、$M^2\ne4m^2$，再取$s\to4m^2$、$t,u\to0$的弹性阈值极限，湮灭项和干涉项消失，只剩$16g^4m^4/M^4$，正好接回第46节用静止旋量直接求得的结果。

<span id="c48-cross-section"></span>

## 从平均模平方到截面

要得到截面，还需加入[第11节](/posts/srednicki-11/#c11)的相空间与通量因子。相空间、态归一和入射通量的处理与自旋无关，因此将其中固定自旋的模平方换成刚求得的平均值即可。沿用该章已经求出的二体相空间，写成
<span id="eq:c48-invariant-cross-section"></span>

$$
\begin{aligned}
d\Phi_2&:=(2\pi)^4\delta^4(p_1+p_2-p_1'-p_2')
\frac{d^3p_1'}{(2\pi)^3\,2E_1'}
\frac{d^3p_2'}{(2\pi)^3\,2E_2'},\\
d\sigma&=\frac{\langle|\mathcal T|^2\rangle}
{4\sqrt{(p_1p_2)^2-m^4}}\,d\Phi_2 .
\end{aligned}
\tag{48.17}
$$

此处$d\Phi_2$就是第11节的$d{\rm LIPS}_2$。在质心系令$q=|\mathbf p_1|$、$q'=|\mathbf p_1'|$，弹性运动学给出$q'=q=\sqrt{s-4m^2}/2$。在这些条件下，式[（11.23）](/posts/srednicki-11/#eq:c11-invariant-flux)和
[（11.29）](/posts/srednicki-11/#eq:c11-two-body-evaluated)分别成为
$\sqrt{(p_1p_2)^2-m^4}=q\sqrt s$与$d\Phi_2=q'\,d\Omega/(16\pi^2\sqrt s)$。于是相空间中的出射动量因子与通量中的入射动量因子相消，留下
<span id="eq:c48-pair-angular"></span>

$$
\frac{d\sigma_{e^-e^+}}{d\Omega_{\rm CM}}
=\frac{\langle|\mathcal T|^2\rangle_{e^-e^+}}{64\pi^2s},
\qquad s>4m^2 .
\tag{48.18}
$$

末态电子和正电子可以区分，计数时没有相同粒子的阶乘。要把这个结果写成角分布，只须采用质心系关系
<span id="eq:c48-pair-angle-substitution"></span>

$$
t=-2q^2(1-\cos\theta),\qquad
u=-2q^2(1+\cos\theta),\qquad q^2=\frac s4-m^2 .
\tag{48.19}
$$

未极化初态没有额外的自旋方向，绕入射轴转动不会改变概率，因此方位角分布均匀。利用$dt=2q^2d\cos\theta$，还可将截面改写为
<span id="eq:c48-pair-t-cross-section"></span>

$$
\frac{d\sigma_{e^-e^+}}{dt}
=\frac{2\pi}{2q^2}\frac{d\sigma_{e^-e^+}}{d\Omega_{\rm CM}}
=\frac{\langle|\mathcal T|^2\rangle_{e^-e^+}}
{16\pi s(s-4m^2)} .
\tag{48.20}
$$

式[（48.17）](#eq:c48-invariant-cross-section)同样适用于其它参考系，角变量的变换则要使用该参考系的雅可比行列式。若$M>2m$且$s$接近$M^2$，内部标量能够衰变，此时树式的极点须按[第25节](/posts/srednicki-25/#c25)的办法处理，不能直接在共振区域积分固定阶结果。

还可以从这个截面看出一个有用的高能极限。取$s\gg m^2,M^2$并保持散射角非零，使$|t|$与$s$同阶。式[（48.16）](#eq:c48-pair-result)中三个分式的领先项各为1，因而
<span id="eq:c48-pair-high-energy"></span>

$$
\begin{aligned}
\langle|\mathcal T|^2\rangle_{e^-e^+}
&=3g^4+g^4O\!\left(\frac{m^2+M^2}{s}\right),\\
\frac{d\sigma_{e^-e^+}}{d\Omega_{\rm CM}}
&=\frac{3g^4}{64\pi^2s}
+O\!\left(\frac{g^4(m^2+M^2)}{s^2}\right).
\end{aligned}
\tag{48.21}
$$

这一展开固定了散射角，前向区域$|t|\lesssim M^2$仍须保留完整质量分母。在高能的有限角区间内，领先角分布趋于常数，而截面按$1/s$下降。

<span id="c48-scalar-start"></span>

## 电子与标量的散射

下面转到$e^-(p)\varphi(k)\to e^-(p')\varphi(k')$。电子与标量分别满足$p^2=p'^2=-m^2$、$k^2=k'^2=-M^2$，因此这一过程的运动学变量为
<span id="eq:c48-scalar-mandelstam"></span>

$$
\begin{aligned}
s&=-(p+k)^2=-(p'+k')^2,\\
t&=-(p-p')^2=-(k-k')^2,\\
u&=-(p-k')^2=-(k-p')^2,\qquad s+t+u=2m^2+2M^2 .
\end{aligned}
\tag{48.22}
$$

展开三个平方，再用$p+k=p'+k'$，即可得到最后的和式。对这些运动学恒等式而言，与四费米例相比只须换入相应的外腿质量。进一步解出内积，就有
<span id="eq:c48-scalar-dot-products"></span>

$$
\begin{aligned}
(pk)=(p'k')&=\frac{m^2+M^2-s}{2},\\
(pp')&=\frac{t-2m^2}{2},\qquad
(kk')=\frac{t-2M^2}{2},\\
(pk')=(p'k)&=\frac{u-m^2-M^2}{2}.
\end{aligned}
\tag{48.23}
$$

第46节已经利用外腿狄拉克方程，将该过程的振幅整理为$\bar u'Au$。现在代入电子自旋的完整性关系，得到
<span id="eq:c48-scalar-matrix"></span>

$$
\begin{aligned}
\langle|\mathcal T|^2\rangle_{e^-\varphi}
&=\frac12\operatorname{tr}(P'APA),\\
P&=-\slashed p+m,\qquad P'=-\slashed p'+m,\\
A&=g^2\left[\frac{N_s}{m^2-s}+\frac{N_u}{m^2-u}\right],\\
N_s&=-\slashed k+2m,\qquad N_u=\slashed k'+2m .
\end{aligned}
\tag{48.24}
$$

这里仅平均一个入射电子的自旋，所以系数为$1/2$。按迹的循环性，也可写成$\operatorname{tr}(APAP')$，结果与上式一致。外标量仍取第45节的稳定质量区间$0<M<2m$；在此范围内，两个内部费米分母不落在极点上，实耦合$g$给出$\bar A=A$。

在这一过程中，重新用$\Phi$表示本例两个道所产生的四个系数：
<span id="eq:c48-scalar-four-traces"></span>

$$
\begin{aligned}
\langle\Phi_{ss}\rangle&=\frac12\operatorname{tr}(P'N_sPN_s),&
\langle\Phi_{uu}\rangle&=\frac12\operatorname{tr}(P'N_uPN_u),\\
\langle\Phi_{su}\rangle&=\frac12\operatorname{tr}(P'N_sPN_u),&
\langle\Phi_{us}\rangle&=\frac12\operatorname{tr}(P'N_uPN_s).
\end{aligned}
\tag{48.25}
$$

其中$N_s,N_u$已包含各道约简后的分子。两幅树图在振幅中相加，因此模平方的两个混合项前都为正号，于是
<span id="eq:c48-scalar-result-structure"></span>

$$
\begin{aligned}
\langle|\mathcal T|^2\rangle_{e^-\varphi}
=g^4\bigg[
&\frac{\langle\Phi_{ss}\rangle}{(m^2-s)^2}
+\frac{\langle\Phi_{su}\rangle+\langle\Phi_{us}\rangle}
{(m^2-s)(m^2-u)}\\
&+\frac{\langle\Phi_{uu}\rangle}{(m^2-u)^2}
\bigg].
\end{aligned}
\tag{48.26}
$$

观察四条链，可以用$k\leftrightarrow-k'$的替换减少重复计算：它在矩阵中交换$N_s$与$N_u$，而保留$P,P'$；在运动学中，将$s=-(p+k)^2$变为$-(p-k')^2=u$，同时保持$t$不变。因此$\Phi_{ss}$与$\Phi_{uu}$相互变换，$\Phi_{su}$与$\Phi_{us}$也相互变换。只要求出一个平方系数和一个干涉系数，其余两个就随之确定。

<span id="c48-mixed-trace"></span>

## 一个通用的四因子迹

这两种独立计算具有同样的矩阵结构，可以先用一个通式完成共同的求迹步骤。令$x,y$为任意实四矢量，定义
<span id="eq:c48-h-definition"></span>

$$
H(x,y):=\frac12\operatorname{tr}
\big[(-\slashed p'+m)(\slashed x+2m)
(-\slashed p+m)(\slashed y+2m)\big].
\tag{48.27}
$$

四个系数就分别是$H(-k,-k)$、$H(k',k')$、$H(-k,k')$和$H(k',-k)$。沿第一个例子的办法，按所取斜线矩阵的个数展开，保留四阶、二阶与常数三组：
<span id="eq:c48-h-expansion"></span>

$$
\begin{aligned}
H(x,y)={}&\frac12\operatorname{tr}
(\slashed p'\slashed x\slashed p\slashed y)\\
&+\frac{m^2}{2}\operatorname{tr}\!\big[
-2\slashed p'\slashed x+4\slashed p'\slashed p
-2\slashed p'\slashed y\\
&\hspace{31mm}
-2\slashed x\slashed p+\slashed x\slashed y
-2\slashed p\slashed y\big]
+2m^4\operatorname{tr}I .
\end{aligned}
\tag{48.28}
$$

各组系数可以直接从被留下的因子读出。保留$p',p$时，其余两项各为$2m$，给二阶项系数$4m^2$；保留$x,y$时，其余两项各为$m$，给$m^2$。若只保留一个外动量与一个$x$或$y$，外动量前的负号乘另外两个质量项$m(2m)$，便给出$-2m^2$。常数项为$m(2m)m(2m)=4m^4$，再乘迹前的$1/2$。这样就逐项得到上式的六个二阶系数与常数系数。

再代入第47节的二阶和四阶迹，得到只含内积的通式
<span id="eq:c48-h-evaluated"></span>

$$
\begin{aligned}
H(x,y)={}&2\big[(p'x)(py)+(p'y)(px)
 -(pp')(xy)\big]\\
&+4m^2(p+p')\cdot(x+y)
 -8m^2(pp')-2m^2(xy)+8m^4 .
\end{aligned}
\tag{48.29}
$$

所得表达式在$x\leftrightarrow y$下对称，因此对于这里的实树幅，两个混合系数直接相等。这既能与前面的交叉替换相联系，也会减少随后的内积整理。

<span id="c48-scalar-squares"></span>

## 两个平方分子的系数

先求平方系数。为使质量项的收集更清楚，继续记$r=m^2$，另记$R=M^2$，并引入三个内积的缩写：
<span id="eq:c48-scalar-dot-abbreviations"></span>

$$
\begin{aligned}
a:=(pk)&=\frac{r+R-s}{2},&
b:=(p'k)&=\frac{u-r-R}{2},\\
h:=(pp')&=\frac t2-r .
\end{aligned}
\tag{48.30}
$$

$a,b,h$在这里只代表内积。代入$x=y=-k$，四阶部分给出$4ab+2Rh$，二阶与常数部分给出$-8r(a+b)-8rh+2rR+8r^2$。将它们相加，并代入内积的表达式，有
<span id="eq:c48-ss-before-collection"></span>

$$
\begin{aligned}
\langle\Phi_{ss}\rangle
&=4ab+2R(h+r)-8r(a+b)-8rh+8r^2\\
&=(r+R-s)(u-r-R)+(R-4r)t\\
&\hspace{12mm}+4r(s-u)+16r^2 .
\end{aligned}
\tag{48.31}
$$

第二行使用了$h+r=t/2$和$a+b=(u-s)/2$，先将各项写成不变量，再利用$s+t+u$的关系消去一个变量。令$L=r+R$，于是$t=2L-s-u$。首项展开为$-su+L(s+u)-L^2$，含$t$的那一项展开为$2(R-4r)L-(R-4r)(s+u)$。将线性项和常数项分别收集，得到
<span id="eq:c48-ss-coefficients"></span>

$$
\begin{aligned}
L(s+u)-(R-4r)(s+u)+4r(s-u)
&=9rs+ru,\\
-L^2+2(R-4r)L+16r^2
&=7r^2-8rR+R^2 .
\end{aligned}
\tag{48.32}
$$

加上前面单独留下的二次项，并恢复两种质量，得到
<span id="eq:c48-ss-polynomial"></span>

$$
\langle\Phi_{ss}\rangle
=-su+m^2(9s+u)+7m^4-8m^2M^2+M^4 .
\tag{48.33}
$$

其中系数9来自$(s+u)$项中的$5r$与$s-u$项中的$4r$相加，而$u$的系数为$5r-4r=r$。另一个平方系数只须交换$s,u$，由此得到
<span id="eq:c48-uu-polynomial"></span>

$$
\langle\Phi_{uu}\rangle
=-su+m^2(9u+s)+7m^4-8m^2M^2+M^4 .
\tag{48.34}
$$

在原迹中，这一步交换的是两个标量动量，费米外腿和自旋平均均保持原样，因此没有新增的费米负号或平均系数。

<span id="c48-scalar-interference"></span>

## 两个干涉分子的系数

接着取$x=-k,y=k'$。内积表给出$(p'k')=(pk)=a$和$(pk')=(p'k)=b$，因而式[（48.29）](#eq:c48-h-evaluated)中的$(p+p')\cdot(-k+k')=-(a+b)+(b+a)=0$，全部线性于$x+y$的项相消。再记$\ell=(kk')=t/2-R$，余下各项为
<span id="eq:c48-su-before-collection"></span>

$$
\begin{aligned}
\langle\Phi_{su}\rangle
&=-2(a^2+b^2)+2(h+r)\ell-8rh+8r^2\\
&=-\frac12(r+R-s)^2-\frac12(u-r-R)^2\\
&\hspace{8mm}+\frac12t(t-2R)-4rt+16r^2 .
\end{aligned}
\tag{48.35}
$$

两个平方前的负号来自$x=-k$与$y=k'$所取的相反号，$\ell$项则保留两个不同标量动量的内积。仍用$L=r+R$，先将二次项集中，写成
<span id="eq:c48-su-quadratic"></span>

$$
\begin{aligned}
\langle\Phi_{su}\rangle
={}&\frac12(t^2-s^2-u^2)+L(s+u)-L^2\\
&-(R+4r)t+16r^2 .
\end{aligned}
\tag{48.36}
$$

代入$t=2L-s-u$，二次部分成为$\frac12(t^2-s^2-u^2)=2L^2-2L(s+u)+su$。将它与余下项合并，线性系数与常数系数分别为
<span id="eq:c48-su-coefficients"></span>

$$
\begin{aligned}
\bigl[-L+(R+4r)\bigr](s+u)&=3r(s+u),\\
L^2-2L(R+4r)+16r^2&=9r^2-8rR-R^2 .
\end{aligned}
\tag{48.37}
$$

恢复质量记号，并利用两个混合迹的对称性，得到
<span id="eq:c48-su-polynomial"></span>

$$
\begin{aligned}
\langle\Phi_{su}\rangle
&=su+3m^2(s+u)+9m^4-8m^2M^2-M^4,\\
\langle\Phi_{us}\rangle&=\langle\Phi_{su}\rangle .
\end{aligned}
\tag{48.38}
$$

混合系数中最后的$M^4$取负号，和两个平方系数中的正号不同。将式[（48.33）](#eq:c48-ss-polynomial)、
[（48.34）](#eq:c48-uu-polynomial)和
[（48.38）](#eq:c48-su-polynomial)代入
式[（48.26）](#eq:c48-scalar-result-structure)，四个分子便全部化成了不变量。两个干涉分子虽相等，却不必为正；可观察的非负模平方由三组分式合在一起给出。

<span id="c48-scalar-checks"></span>

## 电子标量截面与两个极限

换算截面时，入射通量要使用两种质量。质心系三动量满足$q^2=\lambda(s,m^2,M^2)/(4s)$，其中$\lambda(s,r,R)=(s-r-R)^2-4rR$；由于过程仍为弹性散射，$q'=q$。代入第11节的相空间与通量关系，就得到
<span id="eq:c48-scalar-cross-section"></span>

$$
\begin{aligned}
\frac{d\sigma_{e^-\varphi}}{d\Omega_{\rm CM}}
&=\frac{\langle|\mathcal T|^2\rangle_{e^-\varphi}}{64\pi^2s},\\
\frac{d\sigma_{e^-\varphi}}{dt}
&=\frac{\langle|\mathcal T|^2\rangle_{e^-\varphi}}
{16\pi\lambda(s,m^2,M^2)},\\
t&=-2q^2(1-\cos\theta),\qquad
u=2m^2+2M^2-s-t .
\end{aligned}
\tag{48.39}
$$

将最后一行的角度关系代入三个分式，即可求出第一式的角分布。阈值以上通量为正；取阈值极限时，先约去弹性相空间与通量中共同的$q$，再计算剩余表达式。

先看静止极限，令$p=p'=(m,\mathbf0)$、$k=k'=(M,\mathbf0)$。此时$s=(m+M)^2$、$u=(m-M)^2$、$t=0$，四个多项式分别化为
<span id="eq:c48-threshold-numerators"></span>

$$
\begin{aligned}
\langle\Phi_{ss}\rangle&=4m^2(2m+M)^2,\\
\langle\Phi_{uu}\rangle&=4m^2(2m-M)^2,\\
\langle\Phi_{su}\rangle=\langle\Phi_{us}\rangle
&=4m^2(4m^2-M^2).
\end{aligned}
\tag{48.40}
$$

结合$m^2-s=-M(2m+M)$和$m^2-u=M(2m-M)$，两个平方分式各给$4m^2/M^2$，两个干涉分式合起来给$-8m^2/M^2$。三者恰好抵消，因而$\langle|\mathcal T|^2\rangle\to0$；这与第46节的静止旋量结果一致，也显出两道干涉在阈值处的作用。这里所取的$0<M<2m$保证两个分母均非零。

再看固定角高能极限。令$s\gg m^2,M^2$，同时保持$-u/s$为非零的有限数。四个分子的领先项依次为$-su,-su,su,su$，代回各道分母，得到
<span id="eq:c48-scalar-high-energy"></span>

$$
\begin{aligned}
\langle|\mathcal T|^2\rangle_{e^-\varphi}
&=g^4\left(2-\frac us-\frac su\right)
 +g^4O\!\left(\frac{m^2+M^2}{s}\right),\\
u&=-\frac{s}{2}(1+\cos\theta)+O(m^2+M^2),\\
\frac{d\sigma_{e^-\varphi}}{d\Omega_{\rm CM}}
&=\frac{g^4}{64\pi^2s}
\left[2+\frac{1+\cos\theta}{2}+\frac{2}{1+\cos\theta}\right]
\\
&\hspace{8mm}+O\!\left(\frac{g^4(m^2+M^2)}{s^2}\right).
\end{aligned}
\tag{48.41}
$$

趋于后向$\theta\to\pi$时，$u$不再与$s$同阶，必须回到带质量的完整分母，因此不能将固定角展开直接用于该端点的积分。在其适用角区间内，电子标量散射的领先项仍有明显的角度依赖，与前一个例子不同。

<span id="c48-crossed-annihilation"></span>

## 交叉过程中的初态自旋平均

将上面的结果用于$e^-(p_1)e^+(p_2)\to\varphi(k_1)\varphi(k_2)$，可以具体看出交叉时的符号和统计权重。令$s=-(p_1+p_2)^2$、$t=-(p_1-k_1)^2$、$u=-(p_1-k_2)^2$。从[第45节的两幅湮灭图](/posts/srednicki-45/)出发，在右端使用电子方程，就有

<span id="eq:c48-crossed-annihilation-trace"></span>

$$
\begin{aligned}
\mathcal T_{\rm ann}&=\bar v_2 B u_1,\\
B&=g^2\left[\frac{\slashed k_1+2m}{m^2-t}
             +\frac{\slashed k_2+2m}{m^2-u}\right],\\
\langle|\mathcal T_{\rm ann}|^2\rangle
&=\frac14\operatorname{tr}
 [(-\slashed p_2-m)B(-\slashed p_1+m)B].
\end{aligned}
$$

两束入射费米粒子各取一次平均，故迹前为$1/4$。现在对电子–标量散射的迹作替换

$$
p\mapsto p_1,\qquad p'\mapsto-p_2,\qquad
k\mapsto-k_1,\qquad k'\mapsto k_2.
$$

旧的$(s,t,u)$随之变成新的$(t,s,u)$，矩阵$A$变成$B$，出射电子的完整性核则变为

$$
-\slashed p'+m\mapsto\slashed p_2+m=-(-\slashed p_2-m).
$$

因此，电子–标量散射的$1/2$迹经过替换后，等于湮灭过程的$1/4$迹的负两倍。用$F(s,t,u)=\langle|\mathcal T|^2\rangle_{e^-\varphi}$记式[（48.26）](#eq:c48-scalar-result-structure)，就得到

<span id="eq:c48-crossing-average"></span>

$$
\boxed{\langle|\mathcal T_{\rm ann}|^2\rangle=-\frac12F(t,s,u)}.
$$

负号来自完整性核，$1/2$来自初态平均之比$(1/4)/(1/2)$。中译本习题48.2给出的整体负号适用于比较自旋求和；沿用正文的自旋平均定义时，还要计入这个权重。

为将答案明确写出，定义已经求得的两个多项式

$$
\begin{aligned}
f(x,y)&=-xy+m^2(9x+y)+7m^4-8m^2M^2+M^4,\\
h(x,y)&=xy+3m^2(x+y)+9m^4-8m^2M^2-M^4.
\end{aligned}
$$

湮灭过程的平均模平方便是

<span id="eq:c48-annihilation-result"></span>

$$
\begin{aligned}
\langle|\mathcal T_{\rm ann}|^2\rangle=-\frac{g^4}{2}\bigg[
&\frac{f(t,u)}{(m^2-t)^2}
+\frac{2h(t,u)}{(m^2-t)(m^2-u)}\\
&+\frac{f(u,t)}{(m^2-u)^2}\bigg].
\end{aligned}
$$

交换两个末标量使$t,u$互换，结果保持不变。取树式的零质量极限，并保持$0<\theta<\pi$，有$t=-s(1-\cos\theta)/2$、$u=-s(1+\cos\theta)/2$，从而

$$
\langle|\mathcal T_{\rm ann}|^2\rangle
=\frac{g^4}{2}\left(\frac ut+\frac tu-2\right)
=\frac{2g^4\cos^2\theta}{1-\cos^2\theta}.
$$

例如$\cos\theta=1/2$时得到$2g^4/3$。交叉后的不变量属于新的物理区域，在该区域中，完整表达式仍是非负的振幅模平方。

求截面时，还需处理两个相同末标量的计数。对标有$k_1$的出射方向，二体相空间先给出

<span id="eq:c48-annihilation-phase-space"></span>

$$
\begin{aligned}
\frac{d\sigma_{\rm ord}}{d\Omega_{\rm CM}}
&=\frac1{64\pi^2s}\sqrt{\frac{s-4M^2}{s-4m^2}}
  \langle|\mathcal T_{\rm ann}|^2\rangle,\\
\sigma&=\frac1{2!}\int d\Omega_{\rm CM},
\frac{d\sigma_{\rm ord}}{d\Omega_{\rm CM}},
\qquad s>\max(4m^2,4M^2).
\end{aligned}
$$

全角积分把同一个双标量末态数了两遍，最后的$1/2!$消去这次重复。也可以只积一半方向区域，便无需再除二。这个末态计数与上面初态平均的$1/2$各有自己的来源。

<span id="c48-crossed-electrons"></span>

## 两电子散射的交叉关系

另一个交叉例是$e^-(p_1)e^-(p_2)\to e^-(p_1')e^-(p_2')$。第45节的振幅为直接项减交换项：

$$
\mathcal T_{ee}=g^2\left[
\frac{(\bar u_1'u_1)(\bar u_2'u_2)}{M^2-t}
-\frac{(\bar u_2'u_1)(\bar u_1'u_2)}{M^2-u}
\right].
$$

两束独立、未极化电子仍给初态平均$1/4$。两个平方项分别给$(t-4m^2)^2$和$(u-4m^2)^2$；干涉项则用$U_i=-\slashed p_i+m$写成四因子迹。这次六个二阶项的剩余质量因子全为$+m^2$。令$r=m^2$，代入内积表得

$$
\begin{aligned}
\frac14\operatorname{tr}(U_1U_2'U_2U_1')
={}&\left(\frac u2-r\right)^2
-\left(r-\frac s2\right)^2
+\left(\frac t2-r\right)^2\\
&-r(-s+t+u-2r)+r^2\\
={}&-\frac{tu}{2}+2rs.
\end{aligned}
$$

最后一步用了$t+u=4r-s$：三个平方合为$r^2-tu/2$，后两项合为$2rs-r^2$。另一个干涉迹为其复共轭，数值相同。于是

<span id="eq:c48-electron-electron-result"></span>

$$
\begin{aligned}
\langle|\mathcal T_{ee}|^2\rangle=g^4\bigg[
&\frac{(t-4m^2)^2}{(M^2-t)^2}
+\frac{tu-4m^2s}{(M^2-t)(M^2-u)}\\
&+\frac{(u-4m^2)^2}{(M^2-u)^2}\bigg].
\end{aligned}
$$

这正是电子正电子结果[（48.16）](#eq:c48-pair-result)的$s\leftrightarrow u$替换。两个正电子外腿的完整性核各带一次负号，乘积取正；两边又都有两个初态费米粒子，平均权重相同。求总截面时，对有标签的末电子作全角积分后再除以$2!$，消去同一末态的重复计数。

---

[← 第 47 节](/posts/srednicki-47/) · [章节地图](/srednicki/) · [第 49 节 →](/posts/srednicki-49/)
