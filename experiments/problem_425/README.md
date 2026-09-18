# Erdős problem #425: small exact enumeration

This directory contains an exploratory exact computation for the finite
function associated with [Erdős problem
#425](https://www.erdosproblems.com/425).

For `n >= 1`, let `F(n)` be the maximum size of a set
`A subseteq {1, ..., n}` such that the products `a*b`, over all distinct
unordered pairs `a < b` in `A`, are all different. Products `a*a` are not part
of this definition.

## A. Direct-product baseline

`enumerate_bruteforce.py` enumerates every subset of `{1, ..., n}` as a bit
mask. A subset larger than the best witness found so far is tested by directly
forming all pair products and rejecting the first duplicate. Skipping subsets
that cannot improve the current best does not affect exactness.

The implementation is deliberately simple and is limited to `n <= 22`. It is
intended to establish small reference values before implementing a faster exact
solver.

`verify_bruteforce_results.py` checks each saved witness and enumerates every
subset of size `F(n)+1`, using the same direct-product predicate. Since the
property is inherited by subsets, the absence of a valid set of that size
proves the required upper bound. The verifier also checks the elementary bounds
`pi(n)+1 <= F(n) <= F(n-1)+1`.

## B. Independent forbidden-set computation

`enumerate_forbidden_sets.py` uses a structurally different representation. It
first groups all pairs `a < b` by their product. Two different pairs with the
same product cannot share an element, since cancellation would make the pairs
identical. Every collision therefore gives a forbidden four-element subset.

The script searches candidate sets in decreasing order of size and accepts a
set precisely when it contains none of the precomputed forbidden subsets. It
does not import or call the direct-product predicate from the baseline program.

`compare_results.py` compares the values and witnesses produced by the two
enumerators. As an additional representation check, it can exhaustively compare
the direct-product and forbidden-set predicates on every subset through a
chosen small value of `n`.

## Commands

From the repository root:

```bash
/usr/bin/time -p python experiments/problem_425/enumerate_bruteforce.py \
  --max-n 20
python experiments/problem_425/verify_bruteforce_results.py

/usr/bin/time -p python experiments/problem_425/enumerate_forbidden_sets.py \
  --max-n 20
python experiments/problem_425/compare_results.py \
  --equivalence-max-n 16
```

The enumerators write `results_bruteforce.json` and
`results_forbidden_sets.json` in this directory. Each value includes one
optimal witness set and the number of candidate subsets tested by that search.

## Use of AI tools

These initial programs were written with AI assistance and are exploratory
evidence only. They must not be submitted to the OEIS as a human-generated
computation. Any OEIS submission requires a genuinely independent human
derivation and must follow the repository's `CONTRIBUTING.md` rules.
