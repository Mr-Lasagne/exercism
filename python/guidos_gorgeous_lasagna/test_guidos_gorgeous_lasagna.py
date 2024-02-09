"""Test suite for Guido's Gorgeous Lasagna."""

import pytest

from python.guidos_gorgeous_lasagna.guidos_gorgeous_lasagna import (
    bake_time_remaining,
    total_elapsed_cooking_time,
    total_layer_preparation_time,
)


def test_bake_time_remaining() -> None:
    """Verify that `bake_time_remaining` returns correctly."""
    output = 30
    assert bake_time_remaining(10) == output


def test_total_layer_preparation_time() -> None:
    """Verify that `total_layer_preparation_time` returns correctly."""
    output = 4
    assert total_layer_preparation_time(2) == output


def test_total_elapsed_cooking_time() -> None:
    """Verify that `total_elapsed_cooking_time` returns correctly."""
    output = 26
    assert total_elapsed_cooking_time(3, 20) == output


if __name__ == "__main__":
    pytest.main()
