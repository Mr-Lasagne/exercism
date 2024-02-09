"""Test suite for Ghost Gobble Arcade Game."""

import pytest
from ghost_gobble_arcade_game import can_eat_ghost, has_lost, has_scored, has_won


def test_ghost_gets_eaten() -> None:
    """Verify `can_eat_ghost` returns correctly."""
    assert can_eat_ghost(power_pellet_active=True, touching_ghost=True) is True


def test_ghost_does_not_get_eaten_because_no_power_pellet_active() -> None:
    """Verify `can_eat_ghost` returns correctly."""
    assert can_eat_ghost(power_pellet_active=False, touching_ghost=True) is False


def test_ghost_does_not_get_eaten_because_not_touching_ghost() -> None:
    """Verify `can_eat_ghost` returns correctly."""
    assert can_eat_ghost(power_pellet_active=True, touching_ghost=False) is False


def test_score_when_eating_dot() -> None:
    """Verify `has_scored` returns correctly."""
    assert has_scored(touching_power_pellet=False, touching_dot=True) is True


def test_score_when_eating_power_pellet() -> None:
    """Verify `has_scored` returns correctly."""
    assert has_scored(touching_power_pellet=True, touching_dot=False) is True


def test_no_score_when_nothing_eaten() -> None:
    """Verify `has_scored` returns correctly."""
    assert has_scored(touching_power_pellet=False, touching_dot=False) is False


def test_lose_if_touching_a_ghost_without_a_power_pellet_active() -> None:
    """Verify `has_lost` returns correctly."""
    assert has_lost(power_pellet_active=False, touching_ghost=True) is True


def test_dont_lose_if_touching_a_ghost_with_a_power_pellet_active() -> None:
    """Verify `has_lost` returns correctly."""
    assert has_lost(power_pellet_active=True, touching_ghost=True) is False


def test_dont_lose_if_not_touching_a_ghost() -> None:
    """Verify `has_lost` returns correctly."""
    assert has_lost(power_pellet_active=True, touching_ghost=False) is False


def test_win_if_all_dots_eaten() -> None:
    """Verify `has_won` returns correctly."""
    assert (
        has_won(
            has_eaten_all_dots=True,
            power_pellet_active=False,
            touching_ghost=False,
        )
        is True
    )


def test_dont_win_if_all_dots_eaten_but_touching_a_ghost() -> None:
    """Verify `has_won` returns correctly."""
    assert (
        has_won(
            has_eaten_all_dots=True,
            power_pellet_active=False,
            touching_ghost=True,
        )
        is False
    )


def test_win_if_all_dots_eaten_and_touching_a_ghost_with_a_power_pellet_active() -> (
    None
):
    """Verify `has_won` returns correctly."""
    assert (
        has_won(
            has_eaten_all_dots=True,
            power_pellet_active=True,
            touching_ghost=True,
        )
        is True
    )


def test_dont_win_if_not_all_dots_eaten() -> None:
    """Verify `has_won` returns correctly."""
    assert (
        has_won(
            has_eaten_all_dots=False,
            power_pellet_active=True,
            touching_ghost=True,
        )
        is False
    )


if __name__ == "__main__":
    pytest.main()
