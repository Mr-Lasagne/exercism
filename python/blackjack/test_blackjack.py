"""Test suite for Blackjack."""

from __future__ import annotations

import pytest

from python.blackjack.blackjack import (
    can_double_down,
    can_split_pairs,
    higher_card,
    is_blackjack,
    value_of_ace,
    value_of_card,
)


def test_value_of_card() -> None:
    """Verify `value_of_card` returns correctly."""
    output = 10
    assert value_of_card("K") == output


@pytest.mark.parametrize(
    ("card_one", "card_two", "expected"),
    [
        pytest.param("K", "10", ("K", "10"), id="higher_card_both"),
        pytest.param("10", "9", "10", id="higher_card_card_one"),
        pytest.param("6", "7", "7", id="higher_card_card_two"),
    ],
)
def test_higher_card(
    card_one: str,
    card_two: str,
    expected: str | tuple[str, str],
) -> None:
    """Verify `higher_card` returns correctly."""
    assert higher_card(card_one, card_two) == expected


@pytest.mark.parametrize(
    ("card_one", "card_two", "expected"),
    [
        pytest.param("2", "3", 11, id="value_of_ace_11"),
        pytest.param("10", "2", 1, id="value_of_ace_1"),
    ],
)
def test_value_of_ace(card_one: str, card_two: str, expected: int) -> None:
    """Verify `value_of_ace` returns correctly."""
    assert value_of_ace(card_one, card_two) == expected


def test_is_blackjack() -> None:
    """Verify `is_blackjack` returns correctly."""
    assert is_blackjack("A", "K") is True


def test_can_split_pairs() -> None:
    """Verify `can_split_pairs` returns correctly."""
    assert can_split_pairs("Q", "K") is True


def test_can_double_down() -> None:
    """Verify `can_double_down` returns correctly."""
    assert can_double_down("A", "9") is True


if __name__ == "__main__":
    pytest.main()
