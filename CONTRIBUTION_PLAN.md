# 貢献計画・進捗メモ

最終更新: 2026-09-06

このファイルは、`teorth/erdosproblems` への貢献候補、調査結果、作業状況を継続的に記録するための個人用メモです。

## 現在の方針

最初の貢献では、未解決問題そのものの証明ではなく、再現・検証しやすい小規模計算またはデータ改善を目指します。

第一候補は Erdős problem #84 のサイクル集合の計算です。

- 上流 Issue: [#290: Computing sequence for Erdős problem #84](https://github.com/teorth/erdosproblems/issues/290)
- 内容: `n` 頂点グラフに現れ得るサイクル長集合の種類数 `f(n)` を計算する
- 目標: 小さい `n` の正確な値、再現可能なコード、独立した検算方法を用意する
- 現在の状態: 未着手

## 作業チェックリスト

### 1. リポジトリの準備

- [ ] 上流リポジトリを `upstream` remote として追加する
- [ ] `upstream/main` から作業ブランチを作る
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
- [ ] 上流 Issue #290 の最新状況を再確認する
- [ ] サイクル、単純グラフ、同型なグラフの扱いなど、計算上の定義を明文化する
- [ ] 既知の小さい値や関連文献を確認する
- [ ] OEISを定義と添字の両方から検索する

### 3. 計算と検証

- [ ] 小さい `n` の全グラフを列挙する実装を作る
- [ ] 各グラフのサイクル長集合を求める
- [ ] 異なるサイクル長集合の個数 `f(n)` を集計する
- [ ] 少なくとも一部の範囲を別実装または別アルゴリズムで検算する
- [ ] 実行時間、Python・ライブラリのバージョン、実行コマンドを記録する
- [ ] 得られた値と具体的な実現グラフを保存する
- [ ] 単調性や理論上の上下限などの sanity check を行う

### 4. 成果の共有

- [ ] AI支援を利用した範囲を明記する
- [ ] コード、値、検算方法を上流 Issue #290 に報告する
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

- ブランチ: `main`
- remote: 自分のforkを指す `origin` のみ
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

## 次にやること

1. `upstream` remoteとPython仮想環境を準備する。
2. Problem #84の問題文とforumの既存議論を読む。
3. `n <= 5` 程度を対象に、最小の列挙プログラムを試作する。
