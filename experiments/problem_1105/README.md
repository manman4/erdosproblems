# Erdős problem #1105: path and cycle anti-Ramsey enumeration

This directory starts an exact computation associated with
[Erdős problem #1105](https://www.erdosproblems.com/1105).  For
`3 <= k <= n`, let `AR(n, P_k)` be the maximum number of colors in an edge
coloring of `K_n` that contains no rainbow copy of the path `P_k` on `k`
vertices.

An unofficial Japanese translation of the problem statement is available in
[`PROBLEM_JA.md`](PROBLEM_JA.md).

The intended OEIS object is the triangular array

```text
T(n, k) = AR(n, P_k),  3 <= k <= n,
```

read by rows in increasing `n`, and within each row in increasing `k`.

## Naive computation

`enumerate_paths_bruteforce.py` does not use the published formula.  It treats
an edge coloring as a partition of `E(K_n)` into nonempty color classes and
enumerates every such partition exactly once, up to renaming the colors.  It
then tests every labeled copy of every path `P_k` directly.  Consequently, a
stored coloring proves each lower bound, while exhaustive enumeration of all
partitions proves the corresponding upper bound.

The number of partitions of an `m`-element set is the Bell number `B_m`:

```text
n = 5: m = 10, B_m = 115975
n = 6: m = 15, B_m = 1382958545
```

The Python script therefore deliberately refuses `n > 5`.  This is a small,
independent check of the definitions and initial values, not the eventual
fast implementation.

## Suggested command

Run the computation from the repository root:

```bash
/usr/bin/time -p python experiments/problem_1105/enumerate_paths_bruteforce.py \
  --max-n 5
```

The default output is
`experiments/problem_1105/results_paths_bruteforce.json`.  It includes the
flattened triangle and one witness coloring for each pair `(n, k)`.  Existing
output is not replaced unless `--force` is supplied; use a different
`--output` filename for a reproducibility rerun.

Verify the saved counts, formula values, flattened ordering, and witnesses
with a separate rainbow-path detector:

```bash
python experiments/problem_1105/verify_paths_bruteforce.py
```

The verifier does not import the enumerator.  It computes Bell numbers from
Stirling numbers of the second kind and searches for rainbow paths by a
vertex-by-vertex depth-first search, rather than using precomputed path
permutations.

The calculation is expected to agree with Long-Tu Yuan's exact formula for
`n >= k >= 5`.  The cases `k=3,4` are included so that the OEIS triangle uses
the natural full range `n >= k >= 3`.

## Formula-free C search

`enumerate_paths_c.c` uses the same mathematical search space but is not a
line-by-line port of the Python program.  It assigns colors recursively and
checks a path as soon as all of its edges have been assigned.  A subtree is
discarded only if every relevant `k` has already acquired a rainbow path, or
if even giving every remaining edge a new color cannot improve the best
coloring already found.  Neither the search nor its initial bounds use the
published anti-Ramsey formula.

Compile with warnings enabled and place the disposable binary outside the
repository:

```bash
cc -O3 -std=c11 -Wall -Wextra -Wpedantic \
  experiments/problem_1105/enumerate_paths_c.c \
  -o /tmp/enumerate_paths_c
```

First check the overlap with the Python computation:

```bash
/usr/bin/time -p /tmp/enumerate_paths_c --max-n 5
```

Then compute rows beyond the Python limit separately.  A separate output avoids
overwriting the overlap result and makes reruns easier to compare:

```bash
/usr/bin/time -p /tmp/enumerate_paths_c \
  --min-n 6 --max-n 6 \
  --output experiments/problem_1105/results_paths_c_n6.json
```

The `n=7` search is supported but may be much more expensive.  It handles 21
edges and precomputes 6825 labeled undirected paths:

```bash
/usr/bin/time -p /tmp/enumerate_paths_c \
  --min-n 7 --max-n 7 \
  --output experiments/problem_1105/results_paths_c_n7.json
```

Progress is printed every ten million search nodes by default.  Use
`--progress-every N` to change the interval.  Ctrl-C or `SIGTERM` stops the
recursive search without writing a partial result file.  The program also
checks for an existing output file before starting a potentially long search.

The same independent witness and formula checker accepts the C output:

```bash
python experiments/problem_1105/verify_paths_bruteforce.py \
  --input experiments/problem_1105/results_paths_c.json
```

Here `terminal_colorings` counts only leaves reached after pruning, not all Bell
number colorings.  Every omitted subtree has either an already completed
rainbow path for each still-relevant `k`, or an upper bound no better than the
incumbent recorded by the search.

The C search is still exponential.  Its `n <= 7` limit is intentional; raising
the constant without another complexity review is not supported.

## Naive cycle computation

The second OEIS candidate associated with the problem is the triangular array

```text
T(n, k) = AR(n, C_k),  3 <= k <= n,
```

where `C_k` is the cycle on `k` vertices.  The published result is stated using
the minimum number of colors that forces a rainbow cycle; this is one more than
the maximum number of colors avoiding one used here.

`enumerate_cycles_bruteforce.py` is formula-free.  It enumerates all canonical
set partitions of `E(K_n)` and directly tests every labeled undirected cycle.
Rotations and reversals of a cycle are removed before the search.  As with the
naive path search, the Bell-number growth makes `n = 5` the deliberate limit.

Run the exhaustive computation from the repository root:

```bash
/usr/bin/time -p python \
  experiments/problem_1105/enumerate_cycles_bruteforce.py \
  --max-n 5
```

Then verify the number of colorings and cycles, the stored witness colorings,
the flattened row order, and the published formula using an independent DFS
cycle detector:

```bash
python experiments/problem_1105/verify_cycles_bruteforce.py
```

The expected initial rows are deliberately not hard-coded in the enumerator.
They should be obtained by exhaustive search before relying on the formula.

## Formula-free C cycle search

`enumerate_cycles_c.c` uses restricted-growth colorings and incremental cycle
checks.  It prunes only after a completed rainbow cycle makes a target `k`
irrelevant, or when the number of remaining edges cannot improve the current
best value.  The published formula is not used for searching or initialization.

Compile it with warnings enabled:

```bash
cc -O3 -std=c11 -Wall -Wextra -Wpedantic \
  experiments/problem_1105/enumerate_cycles_c.c \
  -o /tmp/enumerate_cycles_c
```

First reproduce the Python range and compare every overlapping entry:

```bash
/usr/bin/time -p /tmp/enumerate_cycles_c --max-n 5

python experiments/problem_1105/verify_cycles_bruteforce.py \
  --input experiments/problem_1105/results_cycles_c.json \
  --reference experiments/problem_1105/results_cycles_bruteforce.json
```

Then compute `n = 6` in a separate output file:

```bash
/usr/bin/time -p /tmp/enumerate_cycles_c \
  --min-n 6 --max-n 6 \
  --output experiments/problem_1105/results_cycles_c_n6.json

python experiments/problem_1105/verify_cycles_bruteforce.py \
  --input experiments/problem_1105/results_cycles_c_n6.json
```

The C search supports `n <= 7`, but `n = 7` should be attempted separately
only after reviewing the `n = 6` search statistics.  Interrupting with Ctrl-C
or `SIGTERM` writes no partial JSON, and an existing output file is not replaced
unless `--force` is supplied.
