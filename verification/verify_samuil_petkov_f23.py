#!/usr/bin/env python3
"""Exact audit for the manuscript 'The Exact Planar Data-Selection Constant F(2,3)'.

This script is supplementary.  The mathematical proof does not depend on
floating-point computation or an optimization solver.
"""

from __future__ import annotations

from fractions import Fraction as F
from itertools import product
import random
import sympy as sp


def sympy_certificate_checks() -> None:
    p1, p2 = sp.symbols("p1 p2", real=True)
    p3 = 1 - p1 - p2
    p = sp.Matrix([p1, p2, p3])

    def s(a: int, b: int, c: int) -> sp.Matrix:
        assert a + b + c == 3
        return sp.Matrix([sp.Rational(a, 3), sp.Rational(b, 3), sp.Rational(c, 3)])

    def outer(x: sp.Matrix) -> sp.Matrix:
        return x * x.T

    target = sp.Rational(1, 5) * (sp.diag(p1, p2, p3) - p * p.T)

    cases = {
        "A": (
            [s(1, 1, 1), s(1, 2, 0), s(2, 1, 0), s(3, 0, 0)],
            [
                sp.Rational(9, 5) * p3,
                sp.Rational(9, 5) * p2 - sp.Rational(3, 10),
                sp.Rational(9, 5) * p1 - sp.Rational(3, 5),
                sp.Rational(1, 10),
            ],
        ),
        "B": (
            [s(2, 0, 1), s(2, 1, 0), s(3, 0, 0)],
            [
                sp.Rational(9, 5) * p3,
                sp.Rational(9, 5) * p2,
                (9 * p1 - 4) / 5,
            ],
        ),
    }

    for name, (points, weights) in cases.items():
        assert sp.factor(sum(weights) - 1) == 0
        matrix = sp.zeros(3)
        for point, weight in zip(points, weights, strict=True):
            matrix += weight * outer(point - p)
        difference = (matrix - target).applyfunc(lambda x: sp.factor(sp.expand(x)))
        assert difference == sp.zeros(3)
        print(f"Case {name}: the nine entries of the covariance identity vanish exactly.")

    # Boundary support checks.
    edge_A = {p1: sp.Rational(5, 6), p2: sp.Rational(1, 6)}
    A_weights = cases["A"][1]
    assert A_weights[0].subs(edge_A) == 0  # p3 = 0; s111 uses label 3.

    edge_B = {p1: sp.Rational(11, 12), p2: sp.Rational(1, 12)}
    B_weights = cases["B"][1]
    assert B_weights[0].subs(edge_B) == 0  # p3 = 0; s201 uses label 3.

    vertex = {p1: 1, p2: 0}
    assert B_weights[0].subs(vertex) == 0
    assert B_weights[1].subs(vertex) == 0
    assert B_weights[2].subs(vertex) == 1
    print("Zero-weight label checks pass on both chambers and at a simplex vertex.")


def compositions_of_three(number_of_labels: int) -> list[tuple[int, ...]]:
    output: list[tuple[int, ...]] = []

    def rec(prefix: tuple[int, ...], remaining_labels: int, total: int) -> None:
        if remaining_labels == 1:
            output.append(prefix + (total,))
            return
        for value in range(total + 1):
            rec(prefix + (value,), remaining_labels - 1, total - value)

    rec((), number_of_labels, 3)
    return output


def dot(x: tuple[F, F], y: tuple[F, F]) -> F:
    return x[0] * y[0] + x[1] * y[1]


def add(x: tuple[F, F], y: tuple[F, F]) -> tuple[F, F]:
    return (x[0] + y[0], x[1] + y[1])


def scale(a: F, x: tuple[F, F]) -> tuple[F, F]:
    return (a * x[0], a * x[1])


def exact_instance(
    points: list[tuple[F, F]], weights: list[F]
) -> tuple[tuple[F, F], F, F]:
    assert len(points) == len(weights)
    assert all(w > 0 for w in weights)
    assert sum(weights, F(0)) == 1

    mean = (F(0), F(0))
    for point, weight in zip(points, weights, strict=True):
        mean = add(mean, scale(weight, point))

    variance = F(0)
    for point, weight in zip(points, weights, strict=True):
        centered = (point[0] - mean[0], point[1] - mean[1])
        variance += weight * dot(centered, centered)

    q_values: list[F] = []
    for k in compositions_of_three(len(points)):
        selected = (F(0), F(0))
        for count, point in zip(k, points, strict=True):
            selected = add(selected, scale(F(count, 3), point))
        error = (selected[0] - mean[0], selected[1] - mean[1])
        q_values.append(dot(error, error))

    return mean, variance, min(q_values)


def lower_bound_and_planar_examples() -> None:
    mean, variance, q = exact_instance(
        [(F(0), F(0)), (F(1), F(0))],
        [F(5, 6), F(1, 6)],
    )
    assert mean == (F(1, 6), F(0))
    assert variance == F(5, 36)
    assert q == F(1, 36)
    assert (variance + q) / variance == F(6, 5)
    print("Six-point collinear extremizer: exact ratio 6/5.")

    mean, variance, q = exact_instance(
        [(F(1), F(-1)), (F(1), F(5)), (F(-5), F(-1))],
        [F(2, 3), F(1, 6), F(1, 6)],
    )
    assert mean == (F(0), F(0))
    assert variance == F(10)
    assert q == F(2)
    assert (variance + q) / variance == F(6, 5)
    print("Noncollinear extremizer: exact ratio 6/5.")


def rational_stress_test(seed: int = 20260718, trials: int = 500) -> None:
    """Exact finite stress test of the proved three-point inequality."""
    rng = random.Random(seed)
    patterns = compositions_of_three(3)

    for _ in range(trials):
        raw = [rng.randint(1, 20) for _ in range(3)]
        total = sum(raw)
        p = [F(value, total) for value in raw]
        points = [
            (F(rng.randint(-10, 10)), F(rng.randint(-10, 10)))
            for _ in range(2)
        ]
        # Solve the centroid equation for the third point.
        third = (
            -(p[0] * points[0][0] + p[1] * points[1][0]) / p[2],
            -(p[0] * points[0][1] + p[1] * points[1][1]) / p[2],
        )
        points.append(third)

        variance = sum(
            (weight * dot(point, point) for point, weight in zip(points, p, strict=True)),
            F(0),
        )
        errors: list[F] = []
        for k in patterns:
            selected = (F(0), F(0))
            for count, point in zip(k, points, strict=True):
                selected = add(selected, scale(F(count, 3), point))
            errors.append(dot(selected, selected))
        assert min(errors) <= variance / 5

    print(f"Exact rational stress test: {trials} centered three-point instances passed (seed {seed}).")


def main() -> None:
    sympy_certificate_checks()
    lower_bound_and_planar_examples()
    rational_stress_test()
    print("All exact audit checks passed.")


if __name__ == "__main__":
    main()
