"""Solution to Blackjack."""

from __future__ import annotations

CARD_VALUE_TEN = 10


def value_of_card(card: str) -> int:
    """Determine the scoring value of the card.

    :param card: The given card.
    :type card: str
    :return: The value of the given card.
    :rtype: int
    """
    if card in "JQK":
        return 10
    if card == "A":
        return 1
    return int(card)


def higher_card(card_one: str, card_two: str) -> str | tuple[str, str]:
    """Determine which card in the hand has a higher value.

    :param card_one: The first card in hand.
    :type card_one: str
    :param card_two: The second card in hand.
    :type card_two: str
    :return: The resulting tuple contains both cards if they are of equal value.
    :rtype: str | tuple[str, str]
    """
    if value_of_card(card_one) > value_of_card(card_two):
        return card_one
    if value_of_card(card_one) < value_of_card(card_two):
        return card_two
    return card_one, card_two


def value_of_ace(card_one: str, card_two: str) -> int:
    """Calculate the most advantageous value for the ace card.

    :param card_one: The first card in hand.
    :type card_one: str
    :param card_two: The second card in hand.
    :type card_two: str
    :return: Either 1 or 11 for the value of the upcoming ace card.
    :rtype: int
    """
    sum_of_cards = value_of_card(card_one) + value_of_card(card_two)
    if "A" in (card_one, card_two) or sum_of_cards > CARD_VALUE_TEN:
        return 1
    return 11


def is_blackjack(card_one: str, card_two: str) -> bool:
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one: The first card in hand.
    :type card_one: str
    :param card_two: The second card in hand.
    :type card_two: str
    :return: True if two cards are worth 21, False otherwise.
    :rtype: bool
    """
    return "A" in (card_one, card_two) and CARD_VALUE_TEN in (
        value_of_card(card_one),
        value_of_card(card_two),
    )


def can_split_pairs(card_one: str, card_two: str) -> bool:
    """Determine if a player can split their hand into two hands.

    :param card_one: The first card in hand.
    :type card_one: str
    :param card_two: The second card in hand.
    :type card_two: str
    :return: True if the hand can be split, False otherwise.
    :rtype: bool
    """
    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one: str, card_two: str) -> bool:
    """Determine if a blackjack player can place a double down bet.

    :param card_one: The first card in hand.
    :type card_one: str
    :param card_two: The second card in hand.
    :type card_two: str
    :return: True if the sum of the hand is 9, 10, or 11, False otherwise.
    :rtype: bool
    """
    return value_of_card(card_one) + value_of_card(card_two) in {9, 10, 11}
