#!/usr/bin/env python3
"""Compute small exact F(n) values using forbidden collision sets.

This implementation is independent of enumerate_bruteforce.py. It turns every
equality a*b = c*d between different pairs a < b and c < d into a forbidden
four-element subset, then searches candidate sets in decreasing size order.
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from itertools import combinations
from pathlib import Path


HERE = Path(__file__).resolve().parent
DEFAULT_OUTPUT = HERE / "results_forbidden_sets.json"
MAX_N = 22


def values_mask(values: tuple[int, ...]) -> int:
    """Encode a subset of positive integers as a bit mask."""
    mask = 0
    for value in values:
        mask |= 1 << (value - 1)
    return mask


def collision_masks(n: int) -> tuple[int, ...]:
    """Return the distinct four-element masks that force product collisions."""
    pairs_by_product: dict[int, list[tuple[int, int]]] = defaultdict(list)
    for left in range(1, n + 1):
        for right in range(left + 1, n + 1):
            pairs_by_product[left * right].append((left, right))

    forbidden: set[int] = set()
    for equal_product_pairs in pairs_by_product.values():
        for first, second in combinations(equal_product_pairs, 2):
            elements = set(first + second)
            if len(elements) != 4:
                raise AssertionError(
                    f"distinct equal-product pairs are not disjoint: "
                    f"{first}, {second}"
                )
            forbidden.add(values_mask(tuple(elements)))
    return tuple(sorted(forbidden))


def avoids_forbidden_sets(candidate_mask: int, forbidden: tuple[int, ...]) -> bool:
    """Return whether candidate_mask contains no forbidden collision mask."""
    return all(candidate_mask & collision != collision for collision in forbidden)


def exact_value(n: int) -> dict[str, object]:
    """Return F(n) and one witness by descending-size exhaustive search."""
    if not 1 <= n <= MAX_N:
        raise ValueError(f"require 1 <= n <= {MAX_N}")

    forbidden = collision_masks(n)
    tested_subsets = 0
    universe = range(1, n + 1)

    for size in range(n, -1, -1):
        for candidate in combinations(universe, size):
            tested_subsets += 1
            if avoids_forbidden_sets(values_mask(candidate), forbidden):
                return {
                    "n": n,
                    "forbidden_set_count": len(forbidden),
                    "tested_subsets": tested_subsets,
                    "F_n": size,
                    "witness": list(candidate),
                }

    raise AssertionError("the empty set should always be a valid candidate")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--min-n", type=int, default=1)
    parser.add_argument("--max-n", type=int, default=20)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if not 1 <= args.min_n <= args.max_n <= MAX_N:
        raise SystemExit(f"require 1 <= min-n <= max-n <= {MAX_N}")

    values = [exact_value(n) for n in range(args.min_n, args.max_n + 1)]
    payload = {
        "problem": 425,
        "method": "equal-product pairs as forbidden four-element subsets",
        "values": values,
    }
    args.output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

    for value in values:
        print(
            f"n={value['n']}: forbidden={value['forbidden_set_count']}, "
            f"tested={value['tested_subsets']}, F(n)={value['F_n']}, "
            f"witness={value['witness']}"
        )
    print(f"wrote {args.output}")


if __name__ == "__main__":
    main()
