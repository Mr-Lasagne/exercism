"""Test suite for Guido's Gorgeous Lasagna."""

import pytest

from python.guidos_gorgeous_lasagna.guidos_gorgeous_lasagna import (
    bake_time_remaining,
    total_elapsed_cooking_time,
    total_layer_preparation_time,
)


@pytest.mark.parametrize(
    ("elapsed_bake_time", "expected"),
    [(1, 39), (2, 38), (5, 35), (10, 30), (15, 25), (23, 17), (33, 7), (39, 1)],
)
def test_bake_time_remaining(elapsed_bake_time: int, expected: int) -> None:
    """Verify that `bake_time_remaining` returns correctly."""
    assert bake_time_remaining(elapsed_bake_time) == expected


@pytest.mark.parametrize(
    ("number_of_layers", "expected"),
    [(1, 2), (2, 4), (5, 10), (8, 16), (11, 22), (15, 30)],
)
def test_total_layer_preparation_time(number_of_layers: int, expected: int) -> None:
    """Verify that `total_layer_preparation_time` returns correctly."""
    assert total_layer_preparation_time(number_of_layers) == expected


@pytest.mark.parametrize(
    ("number_of_layers", "elapsed_bake_time", "expected"),
    [(1, 3, 5), (2, 7, 11), (5, 8, 18), (8, 4, 20), (11, 15, 37), (15, 20, 50)],
)
def test_total_elapsed_cooking_time(
    number_of_layers: int,
    elapsed_bake_time: int,
    expected: int,
) -> None:
    """Verify that `total_elapsed_cooking_time` returns correctly."""
    assert total_elapsed_cooking_time(number_of_layers, elapsed_bake_time) == expected


if __name__ == "__main__":
    pytest.main()
