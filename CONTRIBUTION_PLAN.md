# 貢献計画・進捗メモ

最終更新: 2026-09-06

このファイルは、`teorth/erdosproblems` への貢献候補、調査結果、作業状況を継続的に記録するための個人用メモです。

## 現在の方針

最初の貢献では、未解決問題そのものの証明ではなく、再現・検証しやすい小規模計算またはデータ改善を目指します。

第一候補は Erdős problem #84 のサイクル集合の計算です。

- 上流 Issue: [#290: Computing sequence for Erdős problem #84](https://github.com/teorth/erdosproblems/issues/290)
- 内容: `n` 頂点グラフに現れ得るサイクル長集合の種類数 `f(n)` を計算する
- 目標: 小さい `n` の正確な値、再現可能なコード、独立した検算方法を用意する
- 現在の状態: 二つの独立な方法で `n = 3, 4, 5, 6, 7` を検算済み

## 作業チェックリスト

### 1. リポジトリの準備

- [x] 上流リポジトリを `upstream` remote として追加する
- [x] `upstream/main` を基点とする作業ブランチ `compute-problem-84` を作る
- [ ] Python仮想環境を作る
- [ ] `requirements.txt` の依存関係をインストールする
- [ ] `python scripts/validate.py` が成功することを確認する
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

- [ ] [問題ページ](https://www.erdosproblems.com/84)の定義とコメントを読む
- [x] 上流 Issue #290 の最新状況を再確認する（open、既存コメントなし）
- [x] Issue本文と実装で、`n`頂点グラフのサイクル長集合を数える定義が一致することを確認する
- [ ] 既知の小さい値や関連文献を確認する
- [ ] OEISを定義と添字の両方から検索する

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
- [ ] 単調性や理論上の上下限などの sanity check を行う

### 4. 成果の共有

- [x] AI支援を利用した範囲を報告文案に明記する
- [x] コード、値、検算方法を上流 Issue #290 に報告する
- [ ] 必要なら `data/problems.yaml` の更新PRを作る
- [ ] 数学的な詳しい議論は erdosproblems.com の問題ページへ投稿する

## その他の候補

| 優先度 | 分野 | 候補 | 状態・所感 |
|---|---|---|---|
| 1 | Python・グラフ | [Issue #290 / Problem #84](https://github.com/teorth/erdosproblems/issues/290) | 第一候補。範囲を限定しやすい |
| 2 | Web・データ設計 | [Issue #370: forum情報の追加](https://github.com/teorth/erdosproblems/issues/370) | スキーマ、生成処理、UIの変更候補 |
| 3 | 最適化・MILP | [Issue #300 / Problem #425](https://github.com/teorth/erdosproblems/issues/300) | 既存計算の独立検算が必要 |
| 4 | 計算幾何 | [Issue #298 / Problem #1086](https://github.com/teorth/erdosproblems/issues/298) | 点配置の探索が必要 |
| 5 | SAT・Ramsey理論 | [Issue #291 / Problem #181](https://github.com/teorth/erdosproblems/issues/291) | 難度は比較的高い |
| 6 | Lean | [Issue #392 / Problem #510](https://github.com/teorth/erdosproblems/issues/392) | 形式化経験が必要 |

ローカルの `data/problems.yaml` では、OEIS欄が `possible` のみとなっている問題が266件ある。Problem #84が難しい場合は、対話表で `OEIS = possible` と得意なタグを組み合わせて次の候補を探す。

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

- ブランチ: `compute-problem-84`
- remote: 自分のforkを指す `origin` と、本家を指す `upstream`
- 作業ツリー: このファイルを追加する前はclean
- テスト: `python3 -m pytest -q` は成功（3 passed）
- validation: `PyYAML` が未導入のため、`python3 scripts/validate.py` は現在実行不可

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

## 次にやること

1. maintainerや他の参加者からの返信を待つ。
2. 指摘があれば計算・説明・コードを修正する。
3. 必要と判断された場合のみ、データ更新PRや追加計算を行う。
