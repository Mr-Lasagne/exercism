"""Test suite for Exercism's Python exercise: Guido's Gorgeous Lasagna."""

import pytest
from guidos_gorgeous_lasagna import (
    bake_time_remaining,
    total_elapsed_cooking_time,
    total_layer_preparation_time,
)


def test_bake_time_remaining() -> None:
    """Functionality of `bake_time_remaining`."""
    output = 30
    assert bake_time_remaining(10) == output


def test_total_layer_preparation_time() -> None:
    """Functionality of `total_layer_preparation_time`."""
    output = 4
    assert total_layer_preparation_time(2) == output


def test_total_elapsed_cooking_time() -> None:
    """Functionality of `total_elapsed_cooking_time`."""
    output = 26
    assert total_elapsed_cooking_time(3, 20) == output


if __name__ == "__main__":
    pytest.main()
