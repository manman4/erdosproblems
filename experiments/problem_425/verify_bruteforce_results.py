#!/usr/bin/env python3
"""Verify the saved small exact values for Erdős problem #425."""

from __future__ import annotations

import argparse
import json
from itertools import combinations
from pathlib import Path

from enumerate_bruteforce import DEFAULT_OUTPUT, has_distinct_pair_products


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 1
    return True


def prime_count(n: int) -> int:
    return sum(is_prime(value) for value in range(1, n + 1))


def verify_value(value: dict[str, object]) -> None:
    n = value["n"]
    claimed = value["F_n"]
    witness = value["witness"]
    if not isinstance(n, int) or not isinstance(claimed, int):
        raise AssertionError("n and F_n must be integers")
    if not isinstance(witness, list) or not all(
        isinstance(element, int) for element in witness
    ):
        raise AssertionError(f"n={n}: witness must be a list of integers")
    if witness != sorted(set(witness)):
        raise AssertionError(f"n={n}: witness is not a strictly increasing set")
    if any(element < 1 or element > n for element in witness):
        raise AssertionError(f"n={n}: witness element outside 1..n")
    if len(witness) != claimed:
        raise AssertionError(f"n={n}: witness size does not equal F_n")
    if not has_distinct_pair_products(witness):
        raise AssertionError(f"n={n}: witness has a repeated pair product")

    # If a larger valid set existed, it would contain a valid subset of size
    # claimed + 1. Exhausting that single size therefore proves the upper bound.
    checked = 0
    for candidate in combinations(range(1, n + 1), claimed + 1):
        checked += 1
        if has_distinct_pair_products(candidate):
            raise AssertionError(
                f"n={n}: found a larger valid set than claimed: {candidate}"
            )

    if claimed < prime_count(n) + 1:
        raise AssertionError(f"n={n}: F_n is below the {{1}} union primes bound")

    print(
        f"verified n={n}: F(n)={claimed}, witness={witness}, "
        f"checked {checked} subsets of size {claimed + 1}"
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    payload = json.loads(args.input.read_text(encoding="utf-8"))
    values = payload.get("values")
    if not isinstance(values, list) or not values:
        raise SystemExit("input must contain a nonempty values list")

    previous_n: int | None = None
    previous_f: int | None = None
    for value in values:
        if not isinstance(value, dict):
            raise AssertionError("every value must be an object")
        verify_value(value)
        n = value["n"]
        claimed = value["F_n"]
        if previous_n is not None:
            if n != previous_n + 1:
                raise AssertionError("n values must be consecutive")
            if not previous_f <= claimed <= previous_f + 1:
                raise AssertionError(
                    f"n={n}: expected F(n-1) <= F(n) <= F(n-1)+1"
                )
        previous_n = n
        previous_f = claimed

    print("ok - witnesses, upper bounds, and sanity checks passed")


if __name__ == "__main__":
    main()
