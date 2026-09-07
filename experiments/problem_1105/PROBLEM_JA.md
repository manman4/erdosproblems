# Erdős problem #1105 日本語訳（非公式）

出典:

- [Erdős problem #1105](https://www.erdosproblems.com/1105)
- P. Erdős, M. Simonovits and V. T. Sós, *Anti-Ramsey theorems* (1975)

## 定義

グラフ `G` と正整数 `n` に対し、反Ramsey数 `AR(n, G)` を、完全グラフ
`K_n` の辺を彩色して `G` の虹色コピーを生じさせないときに使用できる
色数の最大値とする。

ここで、`G` のコピーが**虹色**であるとは、そのすべての辺が互いに異なる
色をもつことをいう。

## 問題文

`C_k` を `k` 頂点のサイクルとする。次は正しいか。

$$
\operatorname{AR}(n,C_k)
=
\left(\frac{k-2}{2}+\frac{1}{k-1}\right)n+O(1).
$$

次に、`P_k` を `k` 頂点のパスとし、

$$
\ell=\left\lfloor\frac{k-1}{2}\right\rfloor
$$

とおく。`n \geq k \geq 5` のとき、次の等式は正しいか。

$$
\operatorname{AR}(n,P_k)
=
\max\left\{
\binom{k-2}{2}+1,
\binom{\ell-1}{2}+(\ell-1)(n-\ell+1)+\epsilon
\right\},
$$

ただし、`k` が奇数なら `\epsilon=1`、`k` が偶数なら `\epsilon=2` とする。

## 記号と訳について

- `P_k` は `k` 本の辺をもつパスではなく、`k` 個の頂点と `k-1` 本の辺を
  もつパスである。
- `AR(n,G)` は、虹色 `G` の出現を避けられる**最大**色数である。
- サイクルの式における `O(1)` は、`k` を固定して `n` を大きくしたときの
  有界項であり、その定数は `k` に依存してよい。
- `n<k` では `K_n` に `P_k` も `C_k` も存在しないため、すべての辺を
  異なる色にでき、反Ramsey数は自明に `\binom{n}{2}` となる。問題文が
  `n\geq k` を扱うのは、この非自明な範囲に限定するためである。
- サイクルに関するMontellano-Ballesteros--Neumann-Laraの論文では、虹色
  `C_k` の出現を保証する**最小**色数を `h(n,k)` と書いている。この二つの
  記法の間には `h(n,k)=AR(n,C_k)+1` の関係がある。

## 現在の状況

問題ページでは全体が解決済みとされている。

- サイクルについては、J. J. Montellano-BallesterosとV. Neumann-Laraが
  [2005年の論文](https://doi.org/10.1007/s00373-005-0619-y)で
  `n \geq k \geq 3` における厳密値を決定した。上の漸近式はその帰結である。
- パスについては、Long-Tu Yuanの
  [2021年のプレプリント](https://arxiv.org/abs/2102.00807)が、上の公式を
  `n \geq k \geq 5` の全範囲で証明している。

したがって、パスの式はサイクルの証明の副産物ではない。両者はErdős、
Simonovits、Sósによって提示された、関連する二つの反Ramsey問題である。

## 今回の計算との関係

このディレクトリでは、OEISの候補としてパスの三角配列

$$
T(n,k)=\operatorname{AR}(n,P_k),\qquad 3\leq k\leq n,
$$

を行ごとに読む。論文の公式が対象とする `k \geq 5` だけでなく、自然な
定義域全体を表すために `k=3,4` も含める。

現在のPython版とC版は、論文の公式を探索に使用せず、辺彩色を直接調べて
小さい `n` の値と具体的なwitness彩色を求める。公式は計算終了後の照合に
のみ使用する。
