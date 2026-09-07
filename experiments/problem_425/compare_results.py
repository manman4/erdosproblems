#!/usr/bin/env python3
"""Compare the direct-product and forbidden-set computations."""

from __future__ import annotations

import argparse
import json
from itertools import combinations
from pathlib import Path

from enumerate_forbidden_sets import (
    DEFAULT_OUTPUT as DEFAULT_FORBIDDEN_OUTPUT,
    avoids_forbidden_sets,
    collision_masks,
)


HERE = Path(__file__).resolve().parent
DEFAULT_BASELINE_OUTPUT = HERE / "results_bruteforce.json"
MAX_EQUIVALENCE_N = 20


def direct_product_check(values: tuple[int, ...]) -> bool:
    """Check pair products by sorting them, independently of the baseline."""
    products = [left * right for left, right in combinations(values, 2)]
    products.sort()
    return all(
        products[index - 1] != products[index]
        for index in range(1, len(products))
    )


def values_mask(values: tuple[int, ...]) -> int:
    mask = 0
    for value in values:
        mask |= 1 << (value - 1)
    return mask


def decode_subset(mask: int, n: int) -> tuple[int, ...]:
    return tuple(value for value in range(1, n + 1) if mask & (1 << (value - 1)))


def load_values(path: Path) -> dict[int, dict[str, object]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if payload.get("problem") != 425:
        raise AssertionError(f"{path}: expected problem 425")
    values = payload.get("values")
    if not isinstance(values, list) or not values:
        raise AssertionError(f"{path}: expected a nonempty values list")

    indexed: dict[int, dict[str, object]] = {}
    for value in values:
        if not isinstance(value, dict):
            raise AssertionError(f"{path}: every value must be an object")
        n = value.get("n")
        if not isinstance(n, int):
            raise AssertionError(f"{path}: every n must be an integer")
        if n in indexed:
            raise AssertionError(f"{path}: duplicate n={n}")
        indexed[n] = value
    return indexed


def verify_witness(label: str, value: dict[str, object]) -> None:
    n = value.get("n")
    claimed = value.get("F_n")
    witness = value.get("witness")
    if not isinstance(n, int) or not isinstance(claimed, int):
        raise AssertionError(f"{label}: n and F_n must be integers")
    if not isinstance(witness, list) or not all(
        isinstance(element, int) for element in witness
    ):
        raise AssertionError(f"{label}, n={n}: invalid witness representation")
    if witness != sorted(set(witness)):
        raise AssertionError(f"{label}, n={n}: witness is not a set")
    if any(element < 1 or element > n for element in witness):
        raise AssertionError(f"{label}, n={n}: witness element outside 1..n")
    if len(witness) != claimed:
        raise AssertionError(f"{label}, n={n}: witness size differs from F_n")
    if not direct_product_check(tuple(witness)):
        raise AssertionError(f"{label}, n={n}: witness has a product collision")


def compare_result_files(baseline_path: Path, forbidden_path: Path) -> None:
    baseline = load_values(baseline_path)
    forbidden = load_values(forbidden_path)
    if baseline.keys() != forbidden.keys():
        raise AssertionError("the result files cover different n values")

    for n in baseline:
        baseline_value = baseline[n]
        forbidden_value = forbidden[n]
        verify_witness("baseline", baseline_value)
        verify_witness("forbidden-set", forbidden_value)
        if baseline_value.get("F_n") != forbidden_value.get("F_n"):
            raise AssertionError(
                f"n={n}: baseline gives {baseline_value.get('F_n')}, "
                f"forbidden-set gives {forbidden_value.get('F_n')}"
            )
        print(f"matched n={n}: F(n)={baseline_value['F_n']}")


def verify_predicate_equivalence(max_n: int) -> None:
    """Compare both representations on every subset through max_n."""
    for n in range(1, max_n + 1):
        forbidden = collision_masks(n)
        for mask in range(1 << n):
            values = decode_subset(mask, n)
            direct = direct_product_check(values)
            by_forbidden_sets = avoids_forbidden_sets(mask, forbidden)
            if direct != by_forbidden_sets:
                raise AssertionError(
                    f"n={n}: predicates disagree for subset {values}"
                )
        print(f"predicate equivalence n={n}: checked {1 << n} subsets")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--baseline", type=Path, default=DEFAULT_BASELINE_OUTPUT
    )
    parser.add_argument(
        "--forbidden", type=Path, default=DEFAULT_FORBIDDEN_OUTPUT
    )
    parser.add_argument("--equivalence-max-n", type=int, default=16)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if not 1 <= args.equivalence_max_n <= MAX_EQUIVALENCE_N:
        raise SystemExit(
            f"require 1 <= equivalence-max-n <= {MAX_EQUIVALENCE_N}"
        )

    compare_result_files(args.baseline, args.forbidden)
    verify_predicate_equivalence(args.equivalence_max_n)
    print("ok - independent values, witnesses, and predicates agree")


if __name__ == "__main__":
    main()
