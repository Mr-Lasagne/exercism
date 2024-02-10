"""Solution to Card Games."""

from __future__ import annotations

JACK_VALUE = 11


def get_rounds(current_round: int) -> list[int]:
    """Create a list containing the current and next two round numbers.

    :param current_round: The current round number.
    :type current_round: int
    :return: The current round and the two that follow.
    :rtype: list[int]
    """
    return [current_round, current_round + 1, current_round + 2]


def concatenate_rounds(rounds_1: list[int], rounds_2: list[int]) -> list[int]:
    """Concatenate two lists of round numbers.

    :param rounds_1: The first rounds played.
    :type rounds_1: list[int]
    :param rounds_2: The second list of rounds played.
    :type rounds_2: list[int]
    :return: All rounds played.
    :rtype: list[int]
    """
    return rounds_1 + rounds_2


def list_contains_round(rounds: list[int], target_round: int) -> bool:
    """Check if the list of rounds contains the specified number.

    :param rounds: The rounds played.
    :type rounds: list[int]
    :param target_round: The specified round number.
    :type target_round: int
    :return: True if the round was played, False otherwise.
    :rtype: bool
    """
    return target_round in rounds


def card_average(hand: list[int]) -> float:
    """Calculate the average card value from the list.

    :param hand: The cards in hand.
    :type hand: list[int]
    :return: The average value of the cards in the hand.
    :rtype: float
    """
    return sum(hand) / len(hand)


def approx_average_is_average(hand: list[int]) -> bool:
    """Determine if either approximate average equals the actual average.

    :param hand: The cards in hand.
    :type hand: list[int]
    :return: True if at least one of the approximate averages equals the `true
        average`, False otherwise.
    :rtype: bool
    """
    midrange = (hand[0] + hand[-1]) / 2
    median = hand[len(hand) // 2]
    return card_average(hand) in {midrange, median}


def average_even_is_average_odd(hand: list[int]) -> bool:
    """Determine if the even and odd averages are equal.

    :param hand: The cards in hand.
    :type hand: list[int]
    :return: True if even and odd averages are equal, False otherwise.
    :rtype: bool
    """
    return card_average(hand[::2]) == card_average(hand[1::2])


def maybe_double_last(hand: list[int]) -> list[int]:
    """Multiply a Jack card value in the last index position by 2.

    :param hand: The cards in hand.
    :type hand: list
    :return: The hand with the Jacks (if present) value doubled.
    :rtype: list
    """
    if hand[-1] == JACK_VALUE:
        hand[-1] *= 2
    return hand
