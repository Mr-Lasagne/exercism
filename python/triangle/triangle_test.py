"""Test suite for Triangle."""

from __future__ import annotations

import pytest

from python.triangle.triangle import is_equilateral, is_isosceles, is_scalene


@pytest.mark.parametrize(
    ("sides", "expected"),
    [
        pytest.param([2, 2, 2], True, id="all_sides_are_equal_is_equilateral"),
        pytest.param([2, 3, 2], False, id="any_side_is_unequal_is_not_equilateral"),
        pytest.param([5, 4, 6], False, id="no_sides_are_equal_is_not_equilateral"),
        pytest.param([0, 0, 0], False, id="all_zero_sides_is_not_equilateral"),
        pytest.param([0.5, 0.5, 0.5], True, id="all_sides_equal_float_is_equilateral"),
    ],
)
def test_is_equilateral(sides: list[float], *, expected: bool) -> None:
    """Verify that `is_equilateral` returns correctly."""
    assert is_equilateral(sides) == expected


@pytest.mark.parametrize(
    ("sides", "expected"),
    [
        pytest.param([3, 4, 4], True, id="last_two_sides_are_equal_is_isosceles"),
        pytest.param([4, 4, 3], True, id="first_two_sides_are_equal_is_isosceles"),
        pytest.param([4, 3, 4], True, id="first_and_last_sides_are_equal_is_isosceles"),
        pytest.param([4, 4, 4], True, id="equilateral_triangles_are_also_isosceles"),
        pytest.param([2, 3, 4], False, id="no_sides_are_equal_is_not_isosceles"),
        pytest.param(
            [1, 1, 3],
            False,
            id="first_triangle_inequality_violation_is_not_isosceles",
        ),
        pytest.param(
            [1, 3, 1],
            False,
            id="second_triangle_inequality_violation_is_not_isosceles",
        ),
        pytest.param(
            [3, 1, 1],
            False,
            id="third_triangle_inequality_violation_is_not_isosceles",
        ),
        pytest.param(
            [0.5, 0.4, 0.5],
            True,
            id="isosceles_with_float_sides_is_isosceles",
        ),
    ],
)
def test_is_isosceles(sides: list[float], *, expected: bool) -> None:
    """Verify that `is_equilateral` returns correctly."""
    assert is_isosceles(sides) == expected


@pytest.mark.parametrize(
    ("sides", "expected"),
    [
        pytest.param([5, 4, 6], True, id="no_sides_are_equal_is_scalene"),
        pytest.param([4, 4, 4], False, id="all_sides_are_equal_is_not_scalene"),
        pytest.param(
            [4, 4, 3],
            False,
            id="first_and_second_sides_are_equal_is_not_scalene",
        ),
        pytest.param(
            [3, 4, 3],
            False,
            id="first_and_third_sides_are_equal_is_not_scalene",
        ),
        pytest.param(
            [4, 3, 3],
            False,
            id="second_and_third_sides_are_equal_is_not_scalene",
        ),
        pytest.param(
            [7, 3, 2],
            False,
            id="violation_of_triangle_inequality_is_not_scalene",
        ),
        pytest.param(
            [0.5, 0.4, 0.6],
            True,
            id="scalene_with_float_sides_is_scalene",
        ),
    ],
)
def test_is_scalene(sides: list[float], *, expected: bool) -> None:
    """Verify that `is_equilateral` returns correctly."""
    assert is_scalene(sides) == expected


if __name__ == "__main__":
    pytest.main()
