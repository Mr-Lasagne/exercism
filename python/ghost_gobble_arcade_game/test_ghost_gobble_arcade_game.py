"""Test suite for Ghost Gobble Arcade Game."""

import pytest

from python.ghost_gobble_arcade_game.ghost_gobble_arcade_game import (
    AllDotsEatenState,
    PowerPelletActiveState,
    TouchingDotState,
    TouchingGhostState,
    TouchingPowerPelletState,
    can_eat_ghost,
    has_lost,
    has_scored,
    has_won,
)


@pytest.mark.parametrize(
    ("power_pellet_active", "touching_ghost", "expected"),
    [
        pytest.param(
            PowerPelletActiveState.ACTIVE,
            TouchingGhostState.TOUCHING,
            True,
            id="ghost_gets_eaten",
        ),
        pytest.param(
            PowerPelletActiveState.INACTIVE,
            TouchingGhostState.TOUCHING,
            False,
            id="ghost_does_not_get_eaten_because_no_power_pellet_active",
        ),
        pytest.param(
            PowerPelletActiveState.ACTIVE,
            TouchingGhostState.NOT_TOUCHING,
            False,
            id="ghost_does_not_get_eaten_because_not_touching_ghost",
        ),
    ],
)
def test_can_eat_ghost(
    power_pellet_active: PowerPelletActiveState,
    touching_ghost: TouchingGhostState,
    *,
    expected: bool,
) -> None:
    """Verify `can_eat_ghost` returns correctly."""
    assert can_eat_ghost(power_pellet_active, touching_ghost) == expected


@pytest.mark.parametrize(
    ("touching_power_pellet", "touching_dot", "expected"),
    [
        pytest.param(
            TouchingPowerPelletState.NOT_TOUCHING,
            TouchingDotState.TOUCHING,
            True,
            id="score_when_touching_dot",
        ),
        pytest.param(
            TouchingPowerPelletState.TOUCHING,
            TouchingDotState.NOT_TOUCHING,
            True,
            id="score_when_touching_power_pellet",
        ),
        pytest.param(
            TouchingPowerPelletState.NOT_TOUCHING,
            TouchingDotState.NOT_TOUCHING,
            False,
            id="no_score_when_not_touching_power_pellet_or_dot",
        ),
    ],
)
def test_score_when_eating_dot(
    touching_power_pellet: TouchingPowerPelletState,
    touching_dot: TouchingDotState,
    *,
    expected: bool,
) -> None:
    """Verify `has_scored` returns correctly."""
    assert has_scored(touching_power_pellet, touching_dot) == expected


@pytest.mark.parametrize(
    ("power_pellet_active", "touching_ghost", "expected"),
    [
        pytest.param(
            PowerPelletActiveState.INACTIVE,
            TouchingGhostState.TOUCHING,
            True,
            id="lose_if_touching_ghost_without_power_pellet_active",
        ),
        pytest.param(
            PowerPelletActiveState.ACTIVE,
            TouchingGhostState.TOUCHING,
            False,
            id="do_not_lose_if_touching_ghost_with_power_pellet_active",
        ),
        pytest.param(
            PowerPelletActiveState.ACTIVE,
            TouchingGhostState.NOT_TOUCHING,
            False,
            id="do_not_lose_if_not_touching_ghost",
        ),
    ],
)
def test_has_lost(
    power_pellet_active: PowerPelletActiveState,
    touching_ghost: TouchingGhostState,
    *,
    expected: bool,
) -> None:
    """Verify `has_lost` returns correctly."""
    assert has_lost(power_pellet_active, touching_ghost) == expected


@pytest.mark.parametrize(
    ("has_eaten_all_dots", "power_pellet_active", "touching_ghost", "expected"),
    [
        pytest.param(
            AllDotsEatenState.ALL_EATEN,
            PowerPelletActiveState.INACTIVE,
            TouchingGhostState.NOT_TOUCHING,
            True,
            id="win_if_all_dots_eaten",
        ),
        pytest.param(
            AllDotsEatenState.ALL_EATEN,
            PowerPelletActiveState.INACTIVE,
            TouchingGhostState.TOUCHING,
            False,
            id="do_not_win_if_all_dots_eaten_but_touching_ghost",
        ),
        pytest.param(
            AllDotsEatenState.ALL_EATEN,
            PowerPelletActiveState.ACTIVE,
            TouchingGhostState.TOUCHING,
            True,
            id="win_if_all_dots_eaten_and_touching_ghost_with_power_pellet_active",
        ),
        pytest.param(
            AllDotsEatenState.NOT_EATEN,
            PowerPelletActiveState.ACTIVE,
            TouchingGhostState.TOUCHING,
            False,
            id="do_not_win_if_all_dots_not_eaten",
        ),
    ],
)
def test_has_won(
    has_eaten_all_dots: AllDotsEatenState,
    power_pellet_active: PowerPelletActiveState,
    touching_ghost: TouchingGhostState,
    *,
    expected: bool,
) -> None:
    """Verify `has_won` returns correctly."""
    assert (
        has_won(
            has_eaten_all_dots,
            power_pellet_active,
            touching_ghost,
        )
        == expected
    )


if __name__ == "__main__":
    pytest.main()
