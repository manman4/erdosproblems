# Erdős problem #1105: path and cycle anti-Ramsey numbers

This directory contains exact computations associated with
[Erdős problem #1105](https://www.erdosproblems.com/1105).

For a graph `G`, let `AR(n, G)` be the maximum number of colors in an
edge-coloring of `K_n` that contains no rainbow copy of `G`.  The two OEIS
triangles arising from the problem are kept in separate directories:

- [`A399683/`](A399683/) — paths `P_k`;
- [`A399687/`](A399687/) — cycles `C_k`.

Both triangles use the nontrivial range `3 <= k <= n` and are read by rows
in increasing `n`, then increasing `k`.

The shared, unofficial Japanese translation of the problem statement is in
[`PROBLEM_JA.md`](PROBLEM_JA.md).  Sequence-specific programs, results,
proofs, and reproduction instructions are contained in the corresponding
OEIS-numbered directory.
