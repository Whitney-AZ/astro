---
title: 群表示的一个范畴论视角
date: 2025-08-30
summary: 大概算一个小巧思
category: 笔记
tags: [数学, 物理, 范畴论, 代数]
---

&emsp;&emsp;在经典的群表示论中，一个一般的群在某个数域$k$上的一个线性表示指的是一个如下的群同态：

$$
\rho: G \to GL(V)
$$

其中$V$就是我们熟悉的表示空间。在这里，对于$\mathrm{dim}V = n$的情况，$GL(V)$指的是$k$上的一般线性群$GL_n(k)$。$\rho$作为一个同态，必须保持$G$的群结构：

$$
\rho(gh) = \rho(g)\rho(h).
$$

敏锐的读者可能已经发现，这个要求已经很有交换图的意味了，因此试图用一个范畴的角度来思考表示大概是非常自然的。

&emsp;&emsp;我们首先试图将群提升为一个范畴。我们考虑一个仅有一个对象的范畴$\mathcal{C}_G$:

$$
\mathbf{Ob}(\mathcal{C}_G) = \mathbf{*}
$$

这样做的好处是，此时我们就可以将原来群中的元素全部看作是范畴中的同构，并且有天然的态射合成作为群乘法。也就是说，我们作这样的对应：

$$
\mathbf{Hom}(\mathbf{*},\mathbf{*}) \ni h\circ g \Leftrightarrow h\cdot g \in G
$$

这样自然也有单位态射$\mathbf{id}$作为群$G$的单位元。而由于我们要求态射全部为同构，逆元也是一定存在的；如此，我们成功的构造出了一个具有范畴结构的群（好奇怪的说法）。

> 当然对于这个单一对象，我们可以理解为是类似于李群对应的流形之类的东西，这样群元作为态射这一观点就更自然了。

&emsp;&emsp;对于一般线性群对应的范畴，我们也可以用类似的视角来构造。但是，我们先试图用表示$\rho$作用在$\mathcal{C}_G$上，看看会得到什么。我们先将对于对象的作用搁在一边，考虑

$$
 \rho(\mathbf{Hom(\mathbf{*},\mathbf{*})}) \Leftrightarrow \rho(g).
$$

我们期望得到一个一般线性群的元素，而一般线性群的元素恰好是线性空间上的变换，因此我们又得到了一个像$\mathcal{C}_G$类似的结构：某个底空间作为对象，线性变换作为态射的范畴。此时我们可以断定，这个范畴就是线性空间范畴$\mathbf{Vect}_k$。此时，函子作用在$\mathbf{*}$上的像就不言自明了：

$$
\rho :\mathbf{*}\to V :: \mathbf{Hom}(\mathbf{*},\mathbf{*}) \to \mathbf{Hom}(V,V).
$$

至此，我们自然的从群的表示中诱导出了一个函子。

---

&emsp;&emsp;我们构造的这个小toy model有什么用呢？为了展现范畴论的强大，我们将像$\mathbf{Vect}_k$换成一个由光滑流形和流形间的光滑映射组成的范畴$\mathbf{Man}$。现在这个函子变成了：

$$
\rho: \mathbf{*} \to M :: \mathbf{Hom}(\mathbf{*},\mathbf{*}) \to \mathbf{Hom}(M,M)\qquad (M\in \mathbf{Man})
$$

我们来考虑一下这个函子具体描述的过程。给定一个群元

$$
g\in \mathbf{Hom}(\mathbf{*},\mathbf{*}),
$$

$\rho(g)$给出了一个$\phi\in \mathbf{Hom}(M,M)$，而这正是流形上的一个光滑变换。也就是说，这个函子事实上描述了群$G$作用在流形$M$上的结果。
