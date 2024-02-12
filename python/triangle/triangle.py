"""Solution to Triangle."""

from __future__ import annotations

NUMBER_OF_SIDES = 3


def is_triangle(sides: list[float]) -> bool:
    """Determine whether given sides make a valid triangle.

    :param sides: list[int | float] - A list of side lengths.
    :return: bool - Is the triangle valid?
    """
    return 2 * max(sides) < sum(sides)


def is_equilateral(sides: list[float]) -> bool:
    """Determine whether the triangle is equilateral.

    :param sides: list[int | float] - A list of side lengths.
    :return: bool - Is the triangle equilateral?
    """
    return is_triangle(sides) and len(set(sides)) == 1


def is_isosceles(sides: list[float]) -> bool:
    """Determine whether the triangle is isosceles.

    :param sides: list[int | float] - A list of side lengths.
    :return: bool - Is the triangle isosceles?
    """
    return is_triangle(sides) and len(set(sides)) < NUMBER_OF_SIDES


def is_scalene(sides: list[float]) -> bool:
    """Determine whether the triangle is scalene.

    :param sides: list[int | float] - A list of side lengths.
    :return: bool - Is the triangle scalene?
    """
    return is_triangle(sides) and len(set(sides)) == NUMBER_OF_SIDES
