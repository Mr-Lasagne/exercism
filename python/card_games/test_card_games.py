"""Test suite for Card Games."""

from __future__ import annotations

import pytest

from python.card_games.card_games import (
    approx_average_is_average,
    average_even_is_average_odd,
    card_average,
    concatenate_rounds,
    get_rounds,
    list_contains_round,
    maybe_double_last,
)


@pytest.mark.parametrize(
    ("number", "expected"),
    [
        (0, [0, 1, 2]),
        (1, [1, 2, 3]),
        (10, [10, 11, 12]),
        (27, [27, 28, 29]),
        (99, [99, 100, 101]),
        (666, [666, 667, 668]),
    ],
)
def test_get_rounds(number: int, expected: list[int]) -> None:
    """Verify `get_rounds` returns correctly."""
    assert get_rounds(number) == expected


@pytest.mark.parametrize(
    ("rounds_1", "rounds_2", "expected"),
    [
        ([], [], []),
        ([0, 1], [], [0, 1]),
        ([], [1, 2], [1, 2]),
        ([1], [2], [1, 2]),
        ([27, 28, 29], [35, 36], [27, 28, 29, 35, 36]),
        ([1, 2, 3], [4, 5, 6], [1, 2, 3, 4, 5, 6]),
    ],
)
def test_concatenate_rounds(
    rounds_1: list[int],
    rounds_2: list[int],
    expected: list[int],
) -> None:
    """Verify `concatenate_rounds` returns correctly."""
    assert concatenate_rounds(rounds_1, rounds_2) == expected


@pytest.mark.parametrize(
    ("rounds", "target_round", "expected"),
    [
        ([], 1, False),
        ([1, 2, 3], 0, False),
        ([27, 28, 29, 35, 36], 30, False),
        ([1], 1, True),
        ([1, 2, 3], 1, True),
        ([27, 28, 29, 35, 36], 29, True),
    ],
)
def test_list_contains_round(
    rounds: list[int],
    target_round: int,
    *,
    expected: bool,
) -> None:
    """Verify `list_contains_round` returns correctly."""
    assert list_contains_round(rounds, target_round) == expected


@pytest.mark.parametrize(
    ("hand", "expected"),
    [([1], 1.0), ([5, 6, 7], 6.0), ([1, 2, 3, 4], 2.5), ([1, 10, 100], 37.0)],
)
def test_card_average(hand: list[int], expected: float) -> None:
    """Verify `card_average` returns correctly."""
    assert card_average(hand) == expected


@pytest.mark.parametrize(
    ("hand", "expected"),
    [
        ([0, 1, 5], False),
        ([3, 6, 9, 12, 150], False),
        ([1, 2, 3, 5, 9], False),
        ([2, 3, 4, 7, 8], False),
        ([1, 2, 3], True),
        ([2, 3, 4], True),
        ([2, 3, 4, 8, 8], True),
        ([1, 2, 4, 5, 8], True),
    ],
)
def test_approx_average_is_average(hand: list[int], *, expected: bool) -> None:
    """Verify `approx_average_is_average` returns correctly."""
    assert approx_average_is_average(hand) == expected


@pytest.mark.parametrize(
    ("hand", "expected"),
    [
        ([5, 6, 8], False),
        ([1, 2, 3, 4], False),
        ([1, 2, 3], True),
        ([5, 6, 7], True),
        ([1, 3, 5, 7, 9], True),
    ],
)
def test_average_even_is_average_odd(hand: list[int], *, expected: bool) -> None:
    """Verify `average_even_is_average_odd` returns correctly."""
    assert average_even_is_average_odd(hand) == expected


@pytest.mark.parametrize(
    ("hand", "expected"),
    [
        ([1, 2, 11], [1, 2, 22]),
        ([5, 9, 11], [5, 9, 22]),
        ([5, 9, 10], [5, 9, 10]),
        ([1, 2, 3], [1, 2, 3]),
        ([1, 11, 8], [1, 11, 8]),
    ],
)
def test_maybe_double_last(hand: list[int], expected: list[int]) -> None:
    """Verify `maybe_double_last` returns correctly."""
    assert maybe_double_last(hand) == expected


if __name__ == "__main__":
    pytest.main()
