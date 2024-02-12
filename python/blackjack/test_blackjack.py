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


@pytest.mark.parametrize(
    ("card", "expected"),
    [
        ("2", 2),
        ("5", 5),
        ("8", 8),
        ("A", 1),
        ("10", 10),
        ("J", 10),
        ("Q", 10),
        ("K", 10),
    ],
)
def test_value_of_card(card: str, expected: int) -> None:
    """Verify `value_of_card` returns correctly."""
    assert value_of_card(card) == expected


@pytest.mark.parametrize(
    ("card_one", "card_two", "expected"),
    [
        ("A", "A", ("A", "A")),
        ("10", "J", ("10", "J")),
        ("3", "A", "3"),
        ("3", "6", "6"),
        ("Q", "10", ("Q", "10")),
        ("4", "4", ("4", "4")),
        ("9", "10", "10"),
        ("6", "9", "9"),
        ("4", "8", "8"),
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
        ("2", "3", 11),
        ("3", "6", 11),
        ("5", "2", 11),
        ("8", "2", 11),
        ("5", "5", 11),
        ("Q", "A", 1),
        ("10", "2", 1),
        ("7", "8", 1),
        ("J", "9", 1),
        ("K", "K", 1),
        ("2", "A", 1),
        ("A", "2", 1),
    ],
)
def test_value_of_ace(card_one: str, card_two: str, expected: int) -> None:
    """Verify `value_of_ace` returns correctly."""
    assert value_of_ace(card_one, card_two) == expected


@pytest.mark.parametrize(
    ("card_one", "card_two", "expected"),
    [
        ("A", "K", True),
        ("10", "A", True),
        ("10", "9", False),
        ("A", "A", False),
        ("4", "7", False),
        ("9", "2", False),
        ("Q", "K", False),
    ],
)
def test_is_blackjack(card_one: str, card_two: str, *, expected: bool) -> None:
    """Verify `is_blackjack` returns correctly."""
    assert is_blackjack(card_one, card_two) == expected


@pytest.mark.parametrize(
    ("card_one", "card_two", "expected"),
    [
        ("Q", "K", True),
        ("6", "6", True),
        ("A", "A", True),
        ("10", "A", False),
        ("10", "9", False),
    ],
)
def test_can_split_pairs(card_one: str, card_two: str, *, expected: bool) -> None:
    """Verify `can_split_pairs` returns correctly."""
    assert can_split_pairs(card_one, card_two) == expected


@pytest.mark.parametrize(
    ("card_one", "card_two", "expected"),
    [
        ("A", "9", True),
        ("K", "A", True),
        ("4", "5", True),
        ("A", "A", False),
        ("10", "2", False),
        ("10", "9", False),
    ],
)
def test_can_double_down(card_one: str, card_two: str, *, expected: bool) -> None:
    """Verify `can_double_down` returns correctly."""
    assert can_double_down(card_one, card_two) == expected


if __name__ == "__main__":
    pytest.main()
