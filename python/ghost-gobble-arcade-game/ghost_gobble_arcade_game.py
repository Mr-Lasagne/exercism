"""Keyword arguments solution to Ghost Gobble Arcade Game."""


def can_eat_ghost(*, power_pellet_active: bool, touching_ghost: bool) -> bool:
    """Verify that Pac-Man can eat a ghost.

    :param power_pellet_active: Does Pac-Man have a power pellet active?
    :type power_pellet_active: bool
    :param touching_ghost: Is Pac-Man touching a ghost?
    :type touching_ghost: bool
    :return: True if Pac-Man has a power pellet active and is touching a ghost,
        False otherwise.
    :rtype: bool
    """
    return power_pellet_active and touching_ghost


def has_scored(*, touching_power_pellet: bool, touching_dot: bool) -> bool:
    """Verify that Pac-Man has just scored.

    :param touching_power_pellet: Is Pac-Man touching a power pellet?
    :type touching_power_pellet: bool
    :param touching_dot: Is Pac-Man touching a dot?
    :type touching_dot: bool
    :return: True if Pac-Man is touching a power pellet or a dot, False
        otherwise.
    :rtype: bool
    """
    return touching_power_pellet or touching_dot


def has_lost(*, power_pellet_active: bool, touching_ghost: bool) -> bool:
    """Trigger the game loop to end (GAME OVER).

    :param power_pellet_active: Does Pac-Man have a power pellet active?
    :type power_pellet_active: bool
    :param touching_ghost: Is Pac-Man touching a ghost?
    :type touching_ghost: bool
    :return: True if Pac-Man does not have a power pellet active and is touching
        a ghost.
    :rtype: bool
    """
    return touching_ghost and not power_pellet_active


def has_won(
    *,
    has_eaten_all_dots: bool,
    power_pellet_active: bool,
    touching_ghost: bool,
) -> bool:
    """Trigger the victory event.

    :param has_eaten_all_dots: Has Pac-Man "eaten" all the dots?
    :type has_eaten_all_dots: bool
    :param power_pellet_active: Does Pac-Man have a power pellet active?
    :type power_pellet_active: bool
    :param touching_ghost: Is Pac-Man touching a ghost?
    :type touching_ghost: bool
    :return: True if Pac-Man has "eaten" all the dots and has not lost according
        to the function `has_lost`, False otherwise.
    :rtype: bool
    """
    return has_eaten_all_dots and not has_lost(
        power_pellet_active=power_pellet_active,
        touching_ghost=touching_ghost,
    )
