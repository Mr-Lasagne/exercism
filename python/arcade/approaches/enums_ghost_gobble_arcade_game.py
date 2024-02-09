"""Enums solution to Ghost Gobble Arcade Game."""

from enum import Enum


class PowerPelletActiveState(Enum):
    """Power pellet activity states."""

    INACTIVE = 0
    ACTIVE = 1


class TouchingGhostState(Enum):
    """Touching ghost states."""

    NOT_TOUCHING = 0
    TOUCHING = 1


class TouchingPowerPelletState(Enum):
    """Touching power pellet states."""

    NOT_TOUCHING = 0
    TOUCHING = 1


class TouchingDotState(Enum):
    """Touching dot states."""

    NOT_TOUCHING = 0
    TOUCHING = 1


class AllDotsEatenState(Enum):
    """Eaten all dots states."""

    NOT_EATEN = 0
    ALL_EATEN = 1


def can_eat_ghost(
    power_pellet_active: PowerPelletActiveState,
    touching_ghost: TouchingGhostState,
) -> bool:
    """Verify that Pac-Man can eat a ghost.

    :param power_pellet_active: Is the power pellet active or inactive?
    :type power_pellet_active: PowerPelletActiveState
    :param touching_ghost: Is Pac-Man touching a ghost or not?
    :type touching_ghost: TouchingGhostState
    :return: True if Pac-Man has a power pellet active and is touching a ghost,
        False otherwise.
    :rtype: bool
    """
    return (
        power_pellet_active == PowerPelletActiveState.ACTIVE
        and touching_ghost == TouchingGhostState.TOUCHING
    )


def has_scored(
    touching_power_pellet: TouchingPowerPelletState,
    touching_dot: TouchingDotState,
) -> bool:
    """Verify that Pac-Man has just scored.

    :param touching_power_pellet: Is Pac-Man touching a power pellet?
    :type touching_power_pellet: TouchingPowerPelletState
    :param touching_dot: Is Pac-Man touching a dot?
    :type touching_dot: TouchingDotState
    :return: True if Pac-Man is touching a power pellet or a dot, False
        otherwise.
    :rtype: bool
    """
    return (
        touching_power_pellet == TouchingPowerPelletState.TOUCHING
        or touching_dot == TouchingDotState.TOUCHING
    )


def has_lost(
    power_pellet_active: PowerPelletActiveState,
    touching_ghost: TouchingGhostState,
) -> bool:
    """Trigger the game loop to end (GAME OVER).

    :param power_pellet_active: Does Pac-Man have a power pellet active?
    :type power_pellet_active: PowerPelletActiveState
    :param touching_ghost: Is Pac-Man touching a ghost?
    :type touching_ghost: TouchingGhostState
    :return: True if Pac-Man does not have a power pellet active and is touching
        a ghost.
    :rtype: bool
    """
    return (
        touching_ghost == TouchingGhostState.TOUCHING
        and power_pellet_active == PowerPelletActiveState.INACTIVE
    )


def has_won(
    has_eaten_all_dots: AllDotsEatenState,
    power_pellet_active: PowerPelletActiveState,
    touching_ghost: TouchingGhostState,
) -> bool:
    """Trigger the victory event.

    :param has_eaten_all_dots: Has Pac-Man "eaten" all the dots?
    :type has_eaten_all_dots: AllDotsEatenState
    :param power_pellet_active: Does Pac-Man have a power pellet active?
    :type power_pellet_active: PowerPelletActiveState
    :param touching_ghost: Is Pac-Man touching a ghost?
    :type touching_ghost: TouchingGhostState
    :return: True if Pac-Man has "eaten" all the dots and has not lost according
        to the function `has_lost`, False otherwise.
    :rtype: bool
    """
    return has_eaten_all_dots == AllDotsEatenState.ALL_EATEN and not has_lost(
        power_pellet_active,
        touching_ghost,
    )
