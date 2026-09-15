---
    title: "Srednicki §1 相对论量子力学的尝试"
    date: 2026-09-09
    category: 笔记
    tags: [物理, 量子场论, Srednicki]
    series: "Srednicki QFT"
    srednickiSections: [1]
    hideFromHome: true
    draft: false
---

在qm中，纯态由Hilbert Space中的射线表示，可观测量由自伴算符表示，态满足薛定谔方程：

$$
    \begin{gathered}
        i\hbar\frac{d}{dt}|\psi(t)\rangle=H|\psi(t)\rangle,
        \\
        |\psi(t)\rangle=e^{-iHt/\hbar}|\psi(0)\rangle,
        \\
        \frac{d}{dt}\langle\psi|\psi\rangle=\frac{i}{\hbar}\langle\psi|(H^\dagger-H)|\psi\rangle=0.
    \end{gathered}
$$

最后一个式子保证演化过程是保归一化的。现在我们就可以考虑非相对论粒子的动力学：考虑一个无自旋的自由粒子，其哈密顿量为 $H=\mathbf P^2/(2m)$，在位置基底下 $P_i=-i\hbar\partial_i$，因此在状态方程左右同乘一个 $\langle\mathbf x|$，就得到熟悉的位置空间方程：

$$
i\hbar\partial_t\psi(\mathbf x,t)=-\frac{\hbar^2}{2m}\nabla^2\psi(\mathbf x,t).
$$

现在我们要尝试将其扩展到相对论的情形下。第一个想到的方案可能是考虑将哈密顿量换成 $H_+=\sqrt{c^2\mathbf P^2+m^2c^4}$。我们在这里选择了有物理意义的正能量分支。

我们先考虑这个假设的低能极限。令 $z=\mathbf p^2/(m^2c^2)$，利用泰勒展开 $(1+z)^{1/2}=1+z/2-z^2/8+O(z^3)$，得

$$
E_{\mathbf p}=mc^2+\frac{\mathbf p^2}{2m}-\frac{\mathbf p^4}{8m^3c^2}+O\!\left(\frac{\mathbf p^6}{m^5c^4}\right).
$$

当 $|\mathbf p|/(mc)\ll1$ 时，保留前两项就得到静止能和非相对论动能。

虽然低能极限没有问题，但是平方根并不是一个好的结构。我们可以先转变回位置表象：

$$
(H_+\psi)(\mathbf x)=\int d^3y\,K(\mathbf x-\mathbf y)\psi(\mathbf y),\qquad K(\mathbf r)=\int\frac{d^3p}{(2\pi\hbar)^3}\,E_{\mathbf p}e^{i\mathbf p\cdot\mathbf r/\hbar}.
$$

由于能量不能写作多项式的形式，在位置表象下他就不能写作有限阶的局域算符。这意味着这种“相对论量子力学”不是局域的。我们并不想要这样一种理论。

我们发现问题在于能量的根号结构，因此我们尝试消去平方根，对演化方程两侧作用 $i\hbar\partial_t$ 便得到

$$
-\hbar^2\partial_t^2\psi=H_+^2\psi=(-\hbar^2c^2\nabla^2+m^2c^4)\psi.
$$

这个方程解决了局域性的问题。接下来要解决的问题就是，他是否符合相对论的原理。为了证明这个方程是洛伦兹协变的，我们只需要考虑这个方程在一个洛伦兹变换的作用下是否维持形式。我们考虑四维的导数算符

$$
\partial_\mu\equiv\frac{\partial}{\partial x^\mu}=\left(c^{-1}\partial_t,\boldsymbol\nabla\right),\quad\partial^\mu=g^{\mu\nu}\partial_\nu=\left(-c^{-1}\partial_t,\boldsymbol\nabla\right),\quad \partial^\mu x^\nu=g^{\mu\nu}.
$$

在洛伦兹变换下，这两个导数算符的变换关系为

$$
\bar\partial_\mu=(\Lambda^{-1})^\nu{}_{\mu}\partial_\nu,
\qquad
\bar\partial^\rho
=g^{\rho\mu}(\Lambda^{-1})^\nu{}_{\mu}\partial_\nu
=\Lambda^\rho{}_{\sigma}\partial^\sigma.
$$

因此 $\partial^2 = \partial_\mu\partial^\mu$ 的是洛伦兹不变的：

$$
\bar\partial^2
=g_{\mu\nu}\Lambda^\mu{}_{\rho}\Lambda^\nu{}_{\sigma}
\partial^\rho\partial^\sigma=\partial^2.
$$

因此如果改写波动方程为

$$
\begin{gathered}
    -\hbar^2\partial_t^2\psi=(-\hbar^2c^2\nabla^2+m^2c^4)\psi\\
    \left(+\frac{1}{c^2}\partial_t^2 - \nabla^2  + \frac{m^2c^2}{\hbar^2}\right)\psi = 0 \Longrightarrow \left(-\partial^2 + \frac{m^2c^2}{\hbar^2}\right)\psi = 0
\end{gathered}
$$

就会发现其事实上是洛伦兹协变的。这个方程被称为**Klein Gordon方程**。在这里我们区分一下不变和协变的区别：不变的概念是对物理量的概念，指其在洛伦兹变化下不发生相应的变化；洛伦兹协变是指对于方程而言其在洛伦兹变化下维持方程形式，其中的量可能按其类型而按照洛伦兹变换的规律发生一定变化。

KG方程虽然满足相对论的原理，但却不满足概率守恒原理。由于能量本征值有正负两个分支，平面波解需要写成两个平面波的叠加：

$$
\psi(\mathbf x,t)=u_{\mathbf p}(\mathbf x)
\left(Ae^{-iE_{\mathbf p}t/\hbar}+Be^{+iE_{\mathbf p}t/\hbar}\right).
$$

但在计算其模方时，会发现有干涉项出现：

$$
\int d^3x\,|\psi|^2
=|A|^2+|B|^2+2\operatorname{Re}\!\left(A^*B e^{2iE_{\mathbf p}t/\hbar}\right).
$$

这导致概率不是守恒的。

---

当然对于薛定谔方程的相对论尝试，狄拉克提出了一种新的思路：既然问题出现在相对论能量关系，我们可不可以维持导数结构，通过引入矩阵来给出对应的能量关系呢？

我们尝试

$$
i\hbar\partial_t\psi=H_D\psi,
\qquad H_D=c\alpha^jP_j+mc^2\beta,
\qquad \alpha^{j\dagger}=\alpha^j,\quad\beta^\dagger=\beta.
$$

并考察这个哈密顿量能否给出正确的能量关系。我们将哈密顿量平方得到

$$
H_D^2
=\frac{c^2}{2}\{\alpha^j,\alpha^k\}P_jP_k
+mc^3\{\alpha^j,\beta\}P_j+m^2c^4\beta^2.
$$

第一项的 $1/2$来自交换 $j,k$ 后的平均：矩阵乘积的反对称部分与对称的 $P_jP_k$ 缩并为零。要求结果对所有动量都等于 $(c^2\mathbf P^2+m^2c^4)I$，就须逐一比较二次、一次和常数项的系数。这给出矩阵必须满足的代数：

$$
\{\alpha^j,\alpha^k\}=2\delta^{jk}I,
\qquad \{\alpha^j,\beta\}=0,
\qquad \beta^2=I.
$$

这些条件使 $H_D^2=(c^2\mathbf P^2+m^2c^4)I$。接下来我们考虑这个矩阵的形式。为了满足上述的对易关系，我们先来考虑Pauli矩阵

$$
\sigma^1=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
\sigma^2=\begin{pmatrix}0&-i\\i&0\end{pmatrix},\quad
\sigma^3=\begin{pmatrix}1&0\\0&-1\end{pmatrix},
\qquad \{\sigma^i,\sigma^j\}=2\delta^{ij}I_2.
$$

这显然没什么问题。但是我们还要求 $\{\alpha^j, \beta\} = 0$，这是一个比较困难的要求。由于Pauli矩阵构成 $\mathcal{M}_{2\times 2}(\mathbb{C})$ 的一组完备基，任何的复 $2\times2$ 矩阵均可写为 $B=b_0I+b_j\sigma^j$。若它与三个Pauli矩阵都反对易，则 $\{B,\sigma^i\}=2b_0\sigma^i+2b_iI=0$。由于 $I,\sigma^i$ 线性独立，必有 $b_0=b_i=0$，于是 $B=0$，这与 $B^2=I$ 冲突。

当然我们也不能选取奇数维的矩阵。因为 $\beta$ 厄米且 $\beta^2=I$，其本征值只有 $\pm1$。要比较两类本征值的个数，可计算矩阵的迹。对任意固定 $i$，由 $\alpha_i^2=I$ 和迹的循环性得

$$
\operatorname{tr}\beta
=\operatorname{tr}(\alpha_i^2\beta)
=\operatorname{tr}(\alpha_i\beta\alpha_i)
=-\operatorname{tr}\beta=0.
$$

因此 $+1$ 和 $-1$ 的个数相同，因此必为偶数维的。我们尝试取

$$
\alpha^i=\begin{pmatrix}0&\sigma^i\\\sigma^i&0\end{pmatrix},
\qquad
\beta=\begin{pmatrix}I_2&0\\0&-I_2\end{pmatrix}.
$$

用块矩阵相乘，得到 $\alpha^i\alpha^j=\operatorname{diag}(\sigma^i\sigma^j,\sigma^i\sigma^j)$；同时，$\alpha^i\beta$ 与 $\beta\alpha^i$ 的两个非对角块正好相反，因此这组四维矩阵满足对易关系。

增加的分量解决了矩阵代数的问题，却带来了新的能谱问题。对固定 $\mathbf p$，$H_D$ 是四维厄米矩阵，满足 $H_D^2=E_{\mathbf p}^2I$ 且迹为零。因此当 $E_{\mathbf p}>0$ 时，本征值必为 $+E,+E,-E,-E$。负能支随 $|\mathbf p|\to\infty$ 趋于负无穷，因而这种单电子谱解释没有最低能态。自由方程本身不会使能量本征态自动跃迁；一旦相互作用能把正支态接到负支态，就可能接连跃迁至更低的能量，稳定性问题由此显现。

### Dirac 海

Dirac海（Dirac sea）的设想借助了电子服从Pauli不相容原理这一原理。相对于这个参考占据态，移去能量 $-E$、电荷 $-e$的一个电子，会使能量和电荷分别改变 $\Delta E=+E$、$\Delta Q=+e$。因此留下的空穴具有正电子所需的正能量和正电荷。这样一来，海的表述就让我们从一个粒子的波动方程走到了多粒子状态。我们之前遇到的种种困难提示我们重新考察时间和空间在原有描述中的地位：普通量子力学的 $t$ 是演化参数，$\mathbf x$ 却往往是位置算符的本征值。虽然二者在位置波函数中并列出现，含义并不相同，把它们混合的相对论对称性也就较难显现。下面的两条路径都从构造之初改变这种不对称。

第一条路径以世界线参数标记 $X^\mu(\tau)$，在量子化时把包括坐标时间在内的 $X^\mu$ 都提升为算符，而以 $\tau$ 担任演化参数。对有质量经典轨迹，几何固有时满足 $c^2d\tau^2=-g_{\mu\nu}dX^\mu dX^\nu$。沿同一曲线作单调重参数不改变世界线，但新参数一般不再满足这个固有时归一化，因此须区分任意世界线参数与几何固有时。若保留 $c$，应写 $X^0=cT$；$X^0=T$ 适用于 $c=1$ 或 $T$ 本身指长度量纲坐标的约定。再增加一个参数，得到 $X^\mu(\sigma,\tau)$，就可描述二维世界面，而这正是弦论所选择的表述。

另一条路径更适合本书接下来的工作：为每个空间点赋予算符 $\varphi(\mathbf x)$，再通过海森堡演化引入时间依赖：

$$
\varphi(\mathbf x,t)
=e^{iHt/\hbar}\varphi(\mathbf x,0)e^{-iHt/\hbar},
\qquad
\frac{\partial\varphi}{\partial t}=\frac{i}{\hbar}[H,\varphi]
$$

对第一式求导时，左指数产生 $+iH/\hbar$，右指数产生 $-iH/\hbar$，合起来便得到第二行的对易子。这样，$\mathbf x,t$ 都成为海森堡算符的标签。这正是场论选择的表述。

### 多粒子空间
