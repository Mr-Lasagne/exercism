"""Test suite for Grains."""

import pytest

from python.grains.grains import square, total


@pytest.mark.parametrize(
    ("number", "expected"),
    [
        pytest.param(1, 1, id="grains_on_square_1"),
        pytest.param(2, 2, id="grains_on_square_2"),
        pytest.param(3, 4, id="grains_on_square_3"),
        pytest.param(4, 8, id="grains_on_square_4"),
        pytest.param(16, 32_768, id="grains_on_square_16"),
        pytest.param(32, 2_147_483_648, id="grains_on_square_32"),
        pytest.param(64, 9_223_372_036_854_775_808, id="grains_on_square_64"),
    ],
)
def test_square_with_valid_input(number: int, expected: int) -> None:
    """Verify that `square` returns correctly."""
    assert square(number) == expected


@pytest.mark.parametrize(
    ("number", "expected"),
    [
        pytest.param(0, "Number must be between 1 and 64.", id="square_0_is_invalid"),
        pytest.param(
            -1,
            "Number must be between 1 and 64.",
            id="negative_square_is_invalid",
        ),
        pytest.param(
            65,
            "Number must be between 1 and 64.",
            id="square_greater_than_64_is_invalid",
        ),
    ],
)
def test_square_with_invalid_input(number: int, expected: str) -> None:
    """Verify `square` raises error with invalid input."""
    with pytest.raises(ValueError, match=expected) as err:
        square(number)
    assert str(err.value) == expected


def test_total() -> None:
    """Verify that `total` returns correctly."""
    output = 18_446_744_073_709_551_615
    assert total() == output


if __name__ == "__main__":
    pytest.main()
