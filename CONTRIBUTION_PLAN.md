# 貢献計画・進捗メモ

最終更新: 2026-09-08

このファイルは、Erdős problemsに関連する数列のOEIS登録候補、調査結果、
計算状況、および必要に応じた`teorth/erdosproblems`への報告を継続的に
記録するための個人用メモです。

## forkの運用方針

このforkの`main`は、上流へのPRを作るためだけの複製ではなく、Erdős
problemsとOEISに関する個人用の研究辞書として使用する。上流の収録範囲に
入らない日本語訳、証明、計算コード、実行結果および候補調査ログも保存する。

- 個人用の記録は`main`に蓄積し、問題ごとの計算・検証は
  `compute-problem-N`ブランチで進める。
- 上流へ提出するPR用ブランチは、個人用`main`ではなく、その時点の最新の
  `upstream/main`から作成する。
- 上流PRには、上流リポジトリの目的と`CONTRIBUTING.md`に合う最小限の差分
  だけを含める。
- 個人用`main`と`upstream/main`が分岐することを許容する。同期時に個人用の
  記録を削除したり、上流PRへ意図せず混入させたりしない。
- 上流に載せない資料であっても、出典、AI支援の範囲、検証方法および
  再現手順を可能な限り記録する。

## 現在の方針

Erdős problem #84 のサイクル長集合と、Problem #1105 のパス・サイクルの
反Ramsey数をOEISへ登録しました。対応する上流データ更新PRはレビュー待ちです。

- 上流 Issue: [#290: Computing sequence for Erdős problem #84](https://github.com/teorth/erdosproblems/issues/290)
- 上流 PR: [#406: Link problem 84 to OEIS A399654](https://github.com/teorth/erdosproblems/pull/406)
- OEIS: [A399654](https://oeis.org/A399654)
- 内容: `n` 頂点グラフに現れ得るサイクル長集合の種類数 `f(n)` を計算する
- 目標: 小さい `n` の正確な値、再現可能なコード、独立した検算方法を用意する
- 現在の状態: `n = 10` まで既知値を独立再現し、`n = 11` では全1,018,997,864個の非同型単純グラフを列挙して `f(11) = 247` を得た。再実行結果もSHA-256まで一致した

- Problem #1105: [Erdős Problem 1105](https://www.erdosproblems.com/1105)
- 上流 PR: [#408: Link problem 1105 to OEIS A399683 and A399687](https://github.com/teorth/erdosproblems/pull/408)
- OEIS: [A399683](https://oeis.org/A399683)（パス）、[A399687](https://oeis.org/A399687)（サイクル）
- 現在の状態: 論文の厳密公式から三角配列を作成し、公式を使わないPython版とC版の列挙でも小さい場合を検証した

### 今後の優先目標と候補選定方針

主目的は、Erdős problemsに関連し、まだOEISに登録されていない数列を、
OEISの規則に従って登録することである。上流リポジトリへのIssueやPRは
主目的ではなく、計算の共有や、承認されたA番号を対応付ける必要がある
場合に行う。

次の候補は、Problem #84と同様に、以下の条件を満たすものを優先する。

1. 人間が作成した論文、学位論文、書籍などの一次資料に、有限個の既知値
   または値を決定できる厳密な公式がある。
2. 定義、添字の開始位置、同じ要素の使用可否などが明確である。
3. 定義と初期項の両方からOEISを検索しても、同じ数列が見つからない。
4. 既知値を、資料の計算とは別の実装または別の数学的表現で再現できる。
5. 可能なら、既知範囲を少なくとも一項延長し、witness、実行コマンド、
   実行環境、再実行結果およびチェックサムを保存できる。

AIのみを出典とする値は、複数のAI支援実装が一致していても、この目的の
第一候補にはしない。AIは候補調査、探索コードの補助、検証方法の提案、
誤りの検出に利用できるが、OEISへ投稿する説明、コメント、プログラムは
投稿者自身が理解、検証し、責任を持てるものにする。上流リポジトリへ
共有する場合は、同リポジトリのより厳しい`CONTRIBUTING.md`にも従う。

Problem #425の計算は探索的な再現として`compute-problem-425`ブランチに
保存する。ただし、既知の有限表がAI working reportを中心としているため、
現時点ではOEIS投稿や上流PRを進めず、人間による一次資料に既知項がある
別の候補を優先する。

## 作業チェックリスト

### 1. リポジトリの準備

- [x] 上流リポジトリを `upstream` remote として追加する
- [x] `upstream/main` を基点とする作業ブランチ `compute-problem-84` を作る
- [x] Python仮想環境を作る
- [x] `requirements.txt` の依存関係をインストールする
- [x] `python scripts/validate.py` が成功することを確認する
- [x] `python3 -m pytest -q` を実行する（3 tests passed）

想定コマンド:

```bash
git remote add upstream https://github.com/teorth/erdosproblems.git
git fetch upstream
git switch -c compute-problem-84 upstream/main

python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python scripts/validate.py
python -m pytest -q
```

### 2. Problem #84 の調査

- [x] [問題ページ](https://www.erdosproblems.com/84)の定義とコメントを読む
- [x] 上流 Issue #290 の状況を確認し、計算結果をコメントする
- [x] Issue本文と実装で、`n`頂点グラフのサイクル長集合を数える定義が一致することを確認する
- [x] Dunåsの修士論文とNenadovの論文を確認する
- [x] OEISを定義と添字の両方から検索する
- [x] A399654をOEISへ登録し、`f(0), ..., f(11)` を掲載する

### 3. 計算と検証

- [x] 小さい `n` の全ラベル付きグラフを列挙する実装を作る
- [x] 各グラフのサイクル長集合を求める実装を作る
- [x] 異なるサイクル長集合の個数 `f(n)` を集計する
- [x] 非同型グラフと別のサイクル判定を使う独立実装を作る
- [x] `n = 3, 4, 5` で両実装の全サイクル長集合が一致することを確認する
- [x] `n = 6` で両実装の全サイクル長集合が一致することを確認する
- [x] `n = 7` で両実装の全サイクル長集合が一致することを確認する
- [x] 実行時間、Python・ライブラリのバージョン、実行コマンドを記録する
- [x] 得られた値と具体的な実現グラフを保存する
- [x] 単調性、既知の上下限、既知値との一致をsanity checkとして確認する
- [x] C++版で `n = 11` を二度完全列挙し、出力がSHA-256まで一致することを確認する
- [x] 保存した247個のwitnessをNetworkXと構造の異なる部分集合DPで再検証する

### 4. 成果の共有

- [x] AI支援を利用した範囲を報告文案に明記する
- [x] コード、値、検算方法を上流 Issue #290 に報告する
- [x] `data/problems.yaml` の更新PR #406を作る
- [ ] 数学的な詳しい議論は erdosproblems.com の問題ページへ投稿する

## その他の候補

| 優先度 | 分野 | 候補 | 状態・所感 |
|---|---|---|---|
| 完了 | Python・グラフ | [Issue #290 / Problem #84](https://github.com/teorth/erdosproblems/issues/290) | A399654を登録し、PR #406を提出済み |
| 完了 | グラフ・反Ramsey理論 | [Problem #1105](https://www.erdosproblems.com/1105) | パスをA399683、サイクルをA399687として登録し、PR #408を提出済み |
| 2 | Web・データ設計 | [Issue #370: forum情報の追加](https://github.com/teorth/erdosproblems/issues/370) | スキーマ、生成処理、UIの変更候補 |
| 3 | 最適化・MILP | [Issue #300 / Problem #425](https://github.com/teorth/erdosproblems/issues/300) | 既存計算の独立検算が必要 |
| 4 | 計算幾何 | [Issue #298 / Problem #1086](https://github.com/teorth/erdosproblems/issues/298) | 点配置の探索が必要 |
| 5 | SAT・Ramsey理論 | [Issue #291 / Problem #181](https://github.com/teorth/erdosproblems/issues/291) | 難度は比較的高い |
| 6 | Lean | [Issue #392 / Problem #510](https://github.com/teorth/erdosproblems/issues/392) | 形式化経験が必要 |

2026-09-06時点のローカルの `data/problems.yaml` では、OEIS欄が `possible` のみとなっている問題が266件あった。次の候補を選ぶ前に最新の`upstream/main`で再集計し、対話表で `OEIS = possible` と得意なタグを組み合わせて探す。

### 候補調査ログ

一度確認して見送った候補も、同じ調査を繰り返したり、既に作業中の人と
競合したりしないように記録する。「見送り」は数学的価値が低いという
意味ではなく、現在の「人間による一次資料の既知項を独立再現してOEISへ
登録する」という目的に合うかどうかの判断である。

| Problem | 判断 | 理由・再検討条件 |
|---|---|---|
| [#425](https://www.erdosproblems.com/425) | 当面見送り | 有限表の主要な公開出典がAI working reportであり、ローカル計算もAI支援を含む。人間による独立した有限表または再実装が得られれば再検討する。探索結果は`compute-problem-425`に保存した。 |
| [#272](https://www.erdosproblems.com/272) | 競合回避 | Zhanfu Yangの[2026年プレプリント](https://arxiv.org/abs/2607.23004)が`t(3), ..., t(12)`を厳密計算しているが、Claude支援を明記し、著者自身がOEISへ投稿予定と述べている。投稿状況が長期間変わらない場合のみ、著者への確認後に再検討する。 |
| [#1005](https://www.erdosproblems.com/1005) | 対象外 | 関連数列は既に[OEIS A386893](https://oeis.org/A386893)として登録されている。 |
| [#82](https://www.erdosproblems.com/82) | 対象外 | 関連する「`n`頂点グラフの最大正則誘導部分グラフの大きさの最小値」の数列は、既に[OEIS A390257](https://oeis.org/A390257)として登録されている。 |
| [#284](https://www.erdosproblems.com/284) | 競合回避 | [Issue #271](https://github.com/teorth/erdosproblems/issues/271)で、既存の担当者が人間によるclean-room再実装とOEIS投稿を進行中と明記している。 |
| [#293](https://www.erdosproblems.com/293) | 当面見送り | [Issue #403](https://github.com/teorth/erdosproblems/issues/403)の値はAI支援コードによるもので、問題文の定義にも過去の曖昧さがある。人間による一次資料の有限表という条件を満たさない。 |
| [#336](https://www.erdosproblems.com/336) | 優先度を下げる | 現在確認できる厳密値は少なく、次の値にも未確定の幅があるため、OEISの新規数列として照合・検証するには項数が不足している。厳密値が追加された場合に再検討する。 |
| [#393](https://www.erdosproblems.com/393) | 対象外 | 関連数列は既に[OEIS A388302](https://oeis.org/A388302)として登録されている。 |
| [#644](https://www.erdosproblems.com/644) | 予備調査で見送り | 特殊なパラメータに対する式への言及はあるが、人間による一次資料の有限表、定義、添字をまだ十分に確認できていない。一次資料を特定できた場合に候補へ戻す。 |
| [#857](https://www.erdosproblems.com/857) | 当面見送り | 現在見つかった計算活動はAI支援・形式化を中心としており、Problem #84型の人間由来の既知項を持つ一次資料という条件を満たすことを確認できていない。人間による論文の有限表が見つかれば再検討する。 |
| [#993](https://www.erdosproblems.com/993) | 対象外 | 論文には木の独立集合多項式の単峰性を29頂点まで検証した範囲があるが、それ自体は各`n`に自然数値を割り当てる有限表ではなく、今回のOEIS登録目標に直接対応しない。 |
| [#181](https://www.erdosproblems.com/181), [#506](https://www.erdosproblems.com/506), [#1086](https://www.erdosproblems.com/1086) | 優先度を下げる | 自然な数列はあるが、現在のHELP WANTED Issueには登録に十分な人間由来の既知項がなく、計算も比較的難しい。新しい論文・学位論文の有限表が見つかれば再検討する。 |

## 貢献時の注意

- データ編集の中心は `data/problems.yaml`。
- READMEの表、`status`、`formalized` は自動生成されるため、原則として直接編集しない。
- 数列は最初の数項だけで判断せず、OEIS側と問題側の定義を比較する。
- 添字の開始位置、空集合、順序付き・順序なし、同じ要素の使用可否などを確認する。
- AIが生成した数列やコードを、そのままOEISへ投稿しない。
- AI支援を使ったGitHub上の報告では、その利用を明示する。
- OEISへ新規投稿する場合は、人間による独立した再実装と検証が必要。
- 詳細は `CONTRIBUTING.md` と [Issue #356](https://github.com/teorth/erdosproblems/issues/356) を参照する。

## 現在確認できている環境

- ブランチ: `main`（計算成果は`compute-problem-84`と`compute-problem-1105`、PR用変更は`codex/link-problem-84-a399654`と`link-problem-1105-oeis`）
- remote: 自分のforkを指す `origin` と、本家を指す `upstream`
- 作業ツリー: このファイルの更新を除きclean
- テスト: `python3 -m pytest -q` は成功（3 passed）
- validation: `.venv/bin/python scripts/validate.py` は成功

## 進捗ログ

### 2026-09-06

- `README.md` と `CONTRIBUTING.md` を確認した。
- 上流のopen Issueとhelp wanted Issueを確認した。
- OEIS対応付けがプロジェクトの主要な貢献対象であることを確認した。
- 第一候補として Problem #84 / Issue #290 を選んだ。
- ローカルテスト3件が成功した。
- validationには依存関係のインストールが必要だと確認した。
- `upstream` remoteを追加し、最新の`upstream/main`を取得した。
- `upstream/main`に個人用進捗メモのコミットを加えた状態から、作業ブランチ`compute-problem-84`を作成した。
- 全ラベル付きグラフと辺マスクの部分集合伝播を使う列挙器を作成した（未実行）。
- NetworkX Graph Atlasと頂点順列による直接判定を使う独立列挙器を作成した（未実行）。
- 両結果の比較スクリプトと、小さい既知グラフを使う検証スクリプトを作成した（未実行）。
- 二つの列挙器を `n <= 5` で実行し、`f(3)=2`, `f(4)=4`, `f(5)=6` を得た。
- `compare_results.py` により、個数だけでなく実現可能なサイクル長集合全体が両方式で一致した。
- 非同型グラフ側の実行環境では NetworkX 3.6.1 を使用した。
- 計算結果を `results_labeled.json` と `results_unlabeled.json` に保存した。
- 二つの列挙器を `n <= 6` で実行し、`f(6)=11` を得た。
- `n = 6` でも実現可能なサイクル長集合全体が両方式で一致した。
- 二つの列挙器を `n <= 7` で実行し、`f(7)=21` を得た。
- `n = 7` でも実現可能なサイクル長集合全体が両方式で一致した。
- `n = 7` までの候補列は `2, 4, 6, 11, 21`（添字は `n = 3` から）。
- NetworkX Graph Atlas方式の実行時間は real 1.10秒、user 0.94秒、sys 0.06秒だった。
- 全ラベル付きグラフ方式の実行時間は real 3.28秒、user 3.25秒、sys 0.02秒だった。
- `verify_problem_84.py` が成功し、パス、単一サイクル、完全グラフと `n=3,4,5` の方式間一致を確認した。
- 実行環境は Python 3.13.5、NetworkX 3.6.1。
- Issue #290へ投稿する英語の報告文案を `ISSUE_290_REPORT.md` に作成した。
- Issue #290がopenで既存コメントがなく、今回の定義と一致することを再確認した。
- forkへpushした固定コミットへのリンクを報告文案に追加した。
- Issue #290へ計算結果、二つの検算方法、実行環境、コードリンク、AI利用開示を投稿した。
- 投稿URL: https://github.com/teorth/erdosproblems/issues/290#issuecomment-5557656877
- 2026年のUppsala大学修士論文ですでに `f(1), ..., f(10)` が計算されていることを確認した。
- `n=8`以降を全ラベル付き列挙せず計算するため、nauty `geng` の非同型グラフをストリーミングする列挙器を作成した（未実行）。
- 新しいnauty方式を既存二方式および既知値と照合する検証スクリプトを作成した（未実行）。
- nauty方式で12,346個の非同型8頂点グラフを列挙し、`f(8)=40` を得た。
- nauty方式は`n<=7`で既存二方式のサイクル長集合全体と一致し、`n=8`では既知値と一致した。
- `n<=8`のnauty列挙と検証はすべて成功した。実行時間はreal 0.98秒、user 0.88秒、sys 0.04秒だった。
- nauty方式で274,668個の非同型9頂点グラフを列挙し、既知値`f(9)=75`を再現した。
- `n<=9`の検証はすべて成功した。実行時間はreal 38.66秒、user 38.61秒、sys 0.16秒だった。

### 2026-09-07

- Pythonのnauty方式で12,005,168個の非同型10頂点グラフを列挙し、既知値`f(10)=133`を再現した。
- 高速化のため列挙器をC++へ移植し、数学的な正しさと実装上の安全性を再確認した。
- nauty `geng` 2.9.3が生成した全1,018,997,864個の非同型11頂点単純グラフを処理し、`f(11)=247`を得た。
- `n=11`の完全列挙を二度実行し、247個のcycle setとgraph6 witnessを含むJSONがバイト単位で一致した。
- 一致したJSONのSHA-256は`12adf4d7012a0e0fbd58baeb7662a23220dd73b078db8e5c0b3c39e07325a26e`。
- 保存した全witnessをNetworkXで再計算し、構造の異なる部分集合DPでも検証した。
- Dunåsの2026年Uppsala大学修士論文にある`n<=10`の値と一致することを確認した。
- OEISに[A399654](https://oeis.org/A399654)が公開され、`f(0), ..., f(11) = 1, 1, 1, 2, 4, 6, 11, 21, 40, 75, 133, 247`が掲載された。
- Issue #290に`n=11`の結果、二度の実行、ハッシュ、検証方法、コードリンク、AI利用開示を追記した。
- `data/problems.yaml`のProblem #84について`oeis: ["possible"]`を`oeis: ["A399654"]`へ変更するPR #406を提出した。
- PR用の差分に対して`.venv/bin/python scripts/validate.py`と`git diff --check`が成功した。

### 2026-09-08

- Problem #1105に対応するパスの反Ramsey数の三角配列を[A399683](https://oeis.org/A399683)として登録した。
- Problem #1105に対応するサイクルの反Ramsey数の三角配列を[A399687](https://oeis.org/A399687)として登録した。
- Pythonの全分割列挙と、公式を使わないCの枝刈り列挙を用いて、小さい`n`の値を相互検証した。
- パスの小さい場合`T(n,3)=1`、`T(4,4)=3`、`T(n,4)=2`（`n >= 5`）の人間による証明を記録し、再検査した。
- 上流に該当issueがないことを確認し、issueを新設せず、Problem #1105の`oeis`欄を更新するPR #408を提出した。
- PR #408は最新の`upstream/main`から作った1行だけの差分で、`.venv/bin/python scripts/validate.py`が成功した。

## 次にやること

1. 上流PR #406と#408のCI・レビューを待つ。
2. 修正依頼があれば、それぞれのPR用ブランチで対応する。
3. マージ後に`main`を`upstream/main`へ同期し、PR専用ブランチを削除する。
4. 計算記録を保持するため、`compute-problem-84`と`compute-problem-1105`は残す。
5. 次のOEIS登録候補を選ぶ前に、最新のIssueと`data/problems.yaml`を改めて確認する。
