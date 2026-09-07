#!/usr/bin/env python3
"""Compute small exact values of F(n) for Erdős problem #425.

F(n) is the largest size of a subset A of {1, ..., n} for which the products
a*b are distinct over all unordered pairs of distinct elements a < b in A.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Iterable


HERE = Path(__file__).resolve().parent
DEFAULT_OUTPUT = HERE / "results_bruteforce.json"
MAX_N = 22


def has_distinct_pair_products(values: Iterable[int]) -> bool:
    """Return whether all products from distinct unordered pairs are unique."""
    items = tuple(values)
    products: set[int] = set()
    for left_index, left in enumerate(items):
        for right in items[left_index + 1 :]:
            product = left * right
            if product in products:
                return False
            products.add(product)
    return True


def decode_subset(mask: int, n: int) -> tuple[int, ...]:
    """Decode a bit mask as a subset of {1, ..., n}."""
    return tuple(value for value in range(1, n + 1) if mask & (1 << (value - 1)))


def exact_value(n: int) -> dict[str, object]:
    """Return F(n) and one witness after an exhaustive subset search."""
    if not 1 <= n <= MAX_N:
        raise ValueError(f"require 1 <= n <= {MAX_N}")

    best_size = 0
    best_witness: tuple[int, ...] = ()
    tested_subsets = 0

    for mask in range(1 << n):
        size = mask.bit_count()
        if size <= best_size:
            continue

        candidate = decode_subset(mask, n)
        tested_subsets += 1
        if has_distinct_pair_products(candidate):
            best_size = size
            best_witness = candidate

    return {
        "n": n,
        "subset_count": 1 << n,
        "tested_subsets": tested_subsets,
        "F_n": best_size,
        "witness": list(best_witness),
    }


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
        "method": "all subsets by bit mask; direct duplicate-product test",
        "values": values,
    }
    args.output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

    for value in values:
        print(
            f"n={value['n']}: subsets={value['subset_count']}, "
            f"tested={value['tested_subsets']}, F(n)={value['F_n']}, "
            f"witness={value['witness']}"
        )
    print(f"wrote {args.output}")


if __name__ == "__main__":
    main()
